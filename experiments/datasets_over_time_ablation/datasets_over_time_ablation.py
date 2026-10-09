"""Compare canonical database usage with compatibility-independent extraction usage."""

from __future__ import annotations

import argparse
import ast
import json
import sqlite3
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from matplotlib.lines import Line2D
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, joinedload

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from backend.models import Dataset, DatasetVariant, Result  # noqa: E402
from backend.results_parser import (  # noqa: E402
    resolve_dataset_variant_with_reason,
    result_is_leaderboard_eligible,
)
from experiments.datasets_over_time.datasets_over_time_helpers import (  # noqa: E402
    compute_percentages_and_counts,
    compute_union_relative_shares,
    filter_conference_papers,
    filter_peer_reviewed_papers,
    plot_line_charts,
)

BASE_DIR = Path(__file__).resolve().parent
LABELS = ("Current: eligible database", "Ablation: extracted + DB fallback")


def load_yaml(text: str):
    """Use PyYAML's fast safe loader when available."""
    if hasattr(yaml, "CSafeLoader"):
        return yaml.load(text, Loader=yaml.CSafeLoader)
    return yaml.safe_load(text)


def original_settings() -> dict:
    """Read configuration without executing the original experiment's plotting code."""
    names = {
        "dataset_list",
        "benchmark_list",
        "TIME_STEP",
        "START_DATE",
        "PLOT_END_DATE",
        "BENCHMARK_START_YEARS",
    }
    source = ROOT / "experiments/datasets_over_time/datasets_over_time.py"
    settings = {}
    for node in ast.parse(source.read_text()).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in names:
                    settings[target.id] = ast.literal_eval(node.value)
    if settings.keys() != names:
        raise ValueError("Original experiment configuration has changed; review the ablation")
    return settings


def read_extraction(directory: Path, arxiv_id: str) -> tuple[list[dict] | None, str, str]:
    """None means unavailable; an empty list is a successful empty extraction."""
    if not arxiv_id:
        return None, "no_arxiv_id", ""
    paths = [directory / arxiv_id / "extracted" / f"llm_output.{ext}" for ext in ("yaml", "json")]
    path = next((path for path in paths if path.is_file()), None)
    if path is None:
        return None, "missing_file", ""
    try:
        text = path.read_text(encoding="utf-8")
        payload = json.loads(text) if path.suffix == ".json" else load_yaml(text)
        if not isinstance(payload, dict) or payload.get("error"):
            return None, "invalid_payload", str(path)
        if payload.get("arxiv_id") and str(payload["arxiv_id"]) != arxiv_id:
            return None, "paper_id_mismatch", str(path)
        extracted = payload.get("results")
        if not isinstance(extracted, dict) or extracted.get("error"):
            return None, "invalid_results", str(path)
        entries = extracted.get("results")
        if not isinstance(entries, list) or any(not isinstance(row, dict) for row in entries):
            return None, "invalid_result_list", str(path)
        return entries, "available" if entries else "available_empty", str(path)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError):
        return None, "unreadable_file", str(path)


def dataset_name_map(datasets: pd.DataFrame, variants: pd.DataFrame) -> dict[str, str]:
    """Build dataset identities, excluding ambiguous generic variant names."""
    candidates = defaultdict(set)
    for name in datasets["dataset_name"]:
        candidates[name.strip().casefold()].add(name)
    for row in variants.itertuples():
        candidates[row.variant_name.strip().casefold()].add(row.dataset_name)
    # The parser's additional OGB alias; all configured aliases are handled separately.
    candidates["ogbg-moltox21"].add("Tox21")
    return {key: next(iter(values)) for key, values in candidates.items() if len(values) == 1}


def resolve_name(raw: str, arxiv_id: str, names: dict, aliases: dict) -> str | None:
    paper_aliases = aliases.get("paper_aliases", {}).get(arxiv_id, {})
    paper_aliases = {key.strip().casefold(): value for key, value in paper_aliases.items()}
    global_aliases = {
        key.strip().casefold(): value for key, value in aliases.get("aliases", {}).items()
    }
    normalized = paper_aliases.get(
        raw.strip().casefold(), global_aliases.get(raw.strip().casefold(), raw)
    )
    exact = names.get(normalized.strip().casefold())
    if exact:
        return exact
    # Reuse production name matching without applying its compatibility/storage
    # gates. Synthetic IDs point to logical datasets, so split inference is immaterial.
    canonical = sorted(set(names.values()))
    identifiers = {name: i for i, name in enumerate(canonical)}
    mapping = {key: identifiers[name] for key, name in names.items()}
    dataset_id, _ = resolve_dataset_variant_with_reason(normalized, None, variant_map=mapping)
    return canonical[dataset_id] if dataset_id is not None else None


def load_database(
    snapshot: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, tuple[pd.DataFrame, set[tuple[int, str]]]]:
    """Use the same eligibility predicate as the original, on one consistent snapshot."""
    uri = f"file:{snapshot}?mode=ro"
    with sqlite3.connect(uri, uri=True) as connection:
        papers = pd.read_sql_query(
            "SELECT id AS paper_id, arxiv_id, title AS paper_title, "
            "published_date AS paper_timestamp, venue AS paper_venue, extraction_status FROM papers",
            connection,
        )
        datasets = pd.read_sql_query(
            "SELECT d.id, d.name AS dataset_name, b.name AS benchmark_name FROM datasets d "
            "LEFT JOIN benchmarks b ON b.id=d.benchmark_id",
            connection,
        )
        variants = pd.read_sql_query(
            "SELECT dv.name AS variant_name, d.name AS dataset_name FROM dataset_variants dv "
            "JOIN datasets d ON d.id=dv.dataset_id",
            connection,
        )
    engine = create_engine("sqlite://", creator=lambda: sqlite3.connect(uri, uri=True))
    records, eligible_pairs = [], set()
    with Session(engine) as session:
        results = (
            session.query(Result)
            .options(
                joinedload(Result.model),
                joinedload(Result.paper),
                joinedload(Result.dataset_variant)
                .joinedload(DatasetVariant.dataset)
                .joinedload(Dataset.benchmark),
            )
            .all()
        )
        for result in results:
            dataset = result.dataset_variant.dataset
            pair = (result.paper_id, dataset.name)
            records.append(pair)
            if result_is_leaderboard_eligible(result):
                eligible_pairs.add(pair)
    engine.dispose()
    stored = pd.DataFrame(records, columns=["paper_id", "dataset_name"]).drop_duplicates()
    return papers, datasets, variants, (stored, eligible_pairs)


def build_usage(papers, stored, eligible_pairs, datasets, names, aliases, papers_dir):
    mask = pd.Series(
        [tuple(row) in eligible_pairs for row in stored.itertuples(index=False, name=None)],
        index=stored.index,
        dtype=bool,
    )
    baseline = stored.loc[mask]
    stored_by_paper = stored.groupby("paper_id")["dataset_name"].agg(set).to_dict()
    memberships, coverage, unresolved = [], [], []
    resolved_names = {}
    for paper in papers.itertuples(index=False):
        arxiv_id = paper.arxiv_id or ""
        entries, status, path = read_extraction(papers_dir, arxiv_id)
        fallback = entries is None
        found = stored_by_paper.get(paper.paper_id, set()) if fallback else set()
        for entry in entries or []:
            raw = entry.get("dataset")
            # Count result rows, not discovery mentions. Protocol, value, origin, and
            # quarantine status deliberately do not gate this permissive ablation.
            if not isinstance(raw, str) or not raw.strip():
                unresolved.append(
                    {"paper_id": paper.paper_id, "arxiv_id": arxiv_id, "raw_dataset": repr(raw)}
                )
                continue
            key = (arxiv_id, raw)
            if key not in resolved_names:
                resolved_names[key] = resolve_name(raw, arxiv_id, names, aliases)
            name = resolved_names[key]
            if name:
                found.add(name)
            else:
                unresolved.append(
                    {"paper_id": paper.paper_id, "arxiv_id": arxiv_id, "raw_dataset": raw}
                )
        memberships.extend(
            {
                "paper_id": paper.paper_id,
                "dataset_name": name,
                "evidence_source": "database_fallback" if fallback else "extraction",
            }
            for name in sorted(found)
        )
        coverage.append(
            {
                "paper_id": paper.paper_id,
                "arxiv_id": arxiv_id,
                "status": status,
                "extraction_status": paper.extraction_status,
                "path": path,
                "fallback": fallback,
                "stored_datasets": len(stored_by_paper.get(paper.paper_id, set())),
                "ablation_datasets": len(found),
                "extracted_rows": len(entries) if entries is not None else None,
            }
        )
    ablation = pd.DataFrame(memberships, columns=["paper_id", "dataset_name", "evidence_source"])

    def enrich(frame):
        return frame.merge(papers, on="paper_id").merge(datasets, on="dataset_name")

    return (
        enrich(baseline),
        enrich(ablation),
        pd.DataFrame(coverage),
        pd.DataFrame(unresolved, columns=["paper_id", "arxiv_id", "raw_dataset"]).drop_duplicates(),
    )


def compare_counts(current, ablation, group, names, settings):
    years = pd.period_range(
        settings["START_DATE"], settings["PLOT_END_DATE"], freq=settings["TIME_STEP"]
    )
    if group == "dataset":
        dates = pd.concat([current["paper_timestamp"], ablation["paper_timestamp"]])
        if len(dates):
            years = pd.period_range(
                dates.min(), settings["PLOT_END_DATE"], freq=settings["TIME_STEP"]
            )
    tables = []
    for frame in (current, ablation):
        share, count = compute_percentages_and_counts(
            frame.copy(), group, BASE_DIR, settings["TIME_STEP"], print_info=False
        )
        union = compute_union_relative_shares(frame, group, settings["TIME_STEP"])
        tables.append(
            tuple(
                table.reindex(index=years, columns=names, fill_value=0).fillna(0)
                for table in (count, share, union)
            )
        )
    rows = []
    for year in years:
        for name in names:
            before, after = tables[0][0].loc[year, name], tables[1][0].loc[year, name]
            rows.append(
                {
                    "period": str(year),
                    f"{group}_name": name,
                    "current_count": int(before),
                    "ablation_count": int(after),
                    "delta": int(after - before),
                    "current_share_pct": tables[0][1].loc[year, name],
                    "ablation_share_pct": tables[1][1].loc[year, name],
                    "current_union_share_pct": tables[0][2].loc[year, name],
                    "ablation_union_share_pct": tables[1][2].loc[year, name],
                }
            )
    return pd.DataFrame(rows), tables


def plot_relative_overlay(tables, names, group, output, start_years):
    """Overlay both arms, retaining the original experiment's colors and start years."""
    names = list(names)
    if "TU Dortmund" in names:
        names = ["TU Dortmund", *[name for name in names if name != "TU Dortmund"]]
    fig, ax = plt.subplots(figsize=(9.4, 6.4))
    for i, name in enumerate(names):
        for series, linestyle in zip(tables, ("-", "--"), strict=True):
            table = series[2]
            values = table[name].to_numpy(dtype=float).copy()
            values[table.index.year < start_years.get(name, 0)] = np.nan
            ax.plot(
                table.index.year,
                values,
                color=f"C{i}",
                linestyle=linestyle,
                linewidth=2.2,
                marker="o",
                markersize=5,
                markerfacecolor=f"C{i}" if linestyle == "-" else "white",
            )
    scope = {
        "conference_only": "Conference publications",
        "peer_reviewed": "Peer-reviewed publications",
        "all_papers": "All papers",
    }.get(output.name, output.name.replace("_", " ").capitalize())
    ax.set_title(f"{group.capitalize()} usage over time: {scope.lower()}", fontsize=16)
    ax.set_xlabel("Publication year", fontsize=16)
    ax.set_ylabel("Share of papers (%)", fontsize=16)
    ax.set_xticks(tables[0][2].index.year)
    ax.set_ylim(0, 108)
    ax.tick_params(axis="both", labelsize=13)
    ax.grid(axis="y", alpha=0.2)
    group_handles = [
        Line2D(
            [0],
            [0],
            color=f"C{i}",
            linewidth=2.2,
            label=f"{name} (legacy)" if name in {"TU Dortmund", "Heterophilic Graphs"} else name,
        )
        for i, name in enumerate(names)
    ]
    fig.legend(
        handles=group_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.13),
        ncol=3,
        fontsize=11,
        frameon=False,
    )
    style_handles = [
        Line2D([0], [0], color="black", linewidth=2.2, linestyle=style, label=label)
        for style, label in (
            ("-", "Normal (eligible database)"),
            ("--", "Ablation (extraction + DB fallback)"),
        )
    ]
    fig.legend(
        handles=style_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.07),
        ncol=2,
        fontsize=11,
        frameon=False,
    )
    first, last = tables[0][2].index.year.min(), tables[0][2].index.year.max()
    fig.text(
        0.5,
        0.025,
        f"{scope}, {first}–{last}. Each variant uses its own yearly union of papers\n"
        f"using any of the selected {group} groups as the denominator.",
        ha="center",
        va="bottom",
        fontsize=9,
    )
    fig.subplots_adjust(left=0.11, right=0.98, top=0.91, bottom=0.29)
    output.mkdir(parents=True, exist_ok=True)
    for extension in ("png", "pdf"):
        fig.savefig(output / f"{group}_relative_overlay.{extension}", dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_comparison(tables, names, group, output, start_years):
    if group == "benchmark":
        # Match the original pivot ordering, styling, basename, and PDF crop
        # for a directly substitutable figure, saved only in this sibling.
        plot_line_charts(
            tables[1][2].sort_index(axis=1),
            "benchmarks_relative_lines",
            output,
            ylabel="Share of papers (%)",
            start_years=start_years,
        )
    plot_relative_overlay(tables, names, group, output, start_years)
    for metric, index, ylabel in (
        ("counts", 0, "Number of unique papers"),
        ("relative", 2, "Share of union of papers (%)"),
    ):
        fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharex=True, sharey=True)
        for ax, series, title in zip(axes, tables, LABELS, strict=True):
            table = series[index]
            for i, name in enumerate(names):
                values = table[name].to_numpy(dtype=float).copy()
                values[table.index.year < start_years.get(name, 0)] = np.nan
                ax.plot(table.index.year, values, marker="o", label=name, color=f"C{i}")
            ax.set(title=title, xlabel="Publication year")
            ax.set_xticks(table.index.year)
            ax.tick_params(axis="x", rotation=45)
            ax.grid(axis="y", alpha=0.2)
        maximum = max(float(series[index].to_numpy().max()) for series in tables)
        axes[0].set_ylim(0, max(1, maximum * 1.08))
        axes[0].set_ylabel(ylabel)
        handles, labels = axes[0].get_legend_handles_labels()
        fig.legend(handles, labels, loc="outside lower center", ncol=3)
        fig.suptitle(f"{group.capitalize()} usage: {metric}")
        fig.tight_layout(rect=(0, 0.12, 1, 0.96))
        output.mkdir(parents=True, exist_ok=True)
        for extension in ("png", "pdf"):
            fig.savefig(
                output / f"{group}_{metric}_comparison.{extension}", dpi=150, bbox_inches="tight"
            )
        plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharex=True, sharey=True)
    for ax, series, title in zip(axes, tables, LABELS, strict=True):
        table = series[0]
        bottom = np.zeros(len(table))
        for i, name in enumerate(names):
            values = table[name].to_numpy(dtype=float)
            ax.bar(table.index.year, values, bottom=bottom, label=name, color=f"C{i}")
            bottom += values
        ax.set(title=title, xlabel="Publication year")
        ax.set_xticks(table.index.year)
        ax.tick_params(axis="x", rotation=45)
    maximum = max(float(series[0].sum(axis=1).max()) for series in tables)
    axes[0].set_ylim(0, max(1, maximum * 1.08))
    axes[0].set_ylabel("Paper–group uses (papers may use multiple groups)")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=3)
    fig.suptitle(f"{group.capitalize()} usage: stacked counts")
    fig.tight_layout(rect=(0, 0.12, 1, 0.96))
    for extension in ("png", "pdf"):
        fig.savefig(
            output / f"{group}_stacked_comparison.{extension}", dpi=150, bbox_inches="tight"
        )
    plt.close(fig)


def write_report(output: Path, summary: dict):
    lines = [
        "# Dataset-usage extraction ablation",
        "",
        "Current = eligible database results; ablation = saved extracted result rows, "
        "independent of compatibility, with unfiltered database fallback when unavailable.",
        "",
        f"Cohort: {summary['dated_papers_through_2025']:,} dated database papers through 2025. "
        f"Excluded for missing date or later publication: {summary['excluded_undated_or_after_end']:,}.",
        "",
        f"Unavailable extraction files/payloads: **{summary['fallback_papers']:,}**. "
        f"Of these, **{summary['fallback_papers_with_stored_results']:,}** have stored results "
        "that can contribute fallback usage. See `data/missing_extractions.csv` for every paper.",
        "",
        "Extraction coverage: "
        + "; ".join(
            f"{status}: {count:,}" for status, count in summary["extraction_status_counts"].items()
        )
        + ".",
        "",
        f"Unresolved paper/name pairs: {summary['unresolved_paper_name_pairs']:,}. "
        "These include untracked datasets; see `data/unresolved_dataset_names.csv`.",
        "",
        "Counts deduplicate within each paper and group. A paper may use multiple groups. "
        "Relative plots use each arm's own union of papers using any selected group.",
        "",
        "This permissive ablation includes quarantined, copied, and nonstandard rows. "
        "Saved extractions may differ from those that produced stored rows, so gains "
        "and losses are both reported. The change is broader than compatibility filtering alone.",
        "",
    ]
    for scope, groups in summary["comparisons"].items():
        lines.extend([f"## {scope.replace('_', ' ').capitalize()}", ""])
        for group, metrics in groups.items():
            before, after = (
                metrics["current_paper_group_uses"],
                metrics["ablation_paper_group_uses"],
            )
            change = f" ({(after / before - 1) * 100:+.1f}%)" if before else ""
            lines.extend(
                [
                    f"### {group.capitalize()} usage",
                    "",
                    f"Paper–group uses: **{before:,} → {after:,}**{change}. "
                    f"Added: {metrics['added']:,}; removed: {metrics['removed']:,}. "
                    f"Unique papers: {metrics['current_unique_papers']:,} → {metrics['ablation_unique_papers']:,}.",
                    "",
                    f"Current papers missing extraction: {metrics['current_papers_missing_extraction']:,}. "
                    f"Ablation papers contributing fallback: {metrics['ablation_fallback_papers']:,}.",
                    "",
                ]
            )
            table = pd.read_csv(output / "data" / f"{scope}_{group}_comparison.csv")
            totals = table.groupby(f"{group}_name")[["current_count", "ablation_count"]].sum()
            for name, row in totals.iterrows():
                lines.append(
                    f"- {name}: {int(row.current_count):,} → {int(row.ablation_count):,} paper uses."
                )
            lines.extend(
                [
                    "",
                    f"![{scope} {group} counts](plots/{scope}/{group}_counts_comparison.png)",
                    "",
                    f"![{scope} {group} relative shares](plots/{scope}/{group}_relative_comparison.png)",
                    "",
                    f"![{scope} {group} solid/dashed relative curves](plots/{scope}/{group}_relative_overlay.png)",
                    "",
                ]
            )
    (output / "report.md").write_text("\n".join(lines) + "\n")


def run(db_path: Path, papers_dir: Path, output: Path):
    settings = original_settings()
    # SQLite backup includes committed WAL contents and never checkpoints the source.
    with tempfile.TemporaryDirectory(prefix="dataset-usage-") as temporary:
        snapshot = Path(temporary) / "benchmarks.db"
        with (
            sqlite3.connect(f"file:{db_path.resolve()}?mode=ro", uri=True) as source,
            sqlite3.connect(snapshot) as target,
        ):
            source.backup(target)
        print("Loading database usage and current eligibility...", flush=True)
        papers, datasets, variants, (stored, eligible) = load_database(snapshot)
    dates = pd.to_datetime(papers["paper_timestamp"], format="mixed", errors="coerce")
    papers = papers.loc[dates.notna() & (dates <= pd.Timestamp(settings["PLOT_END_DATE"]))].copy()
    papers["paper_timestamp"] = dates.loc[papers.index]
    aliases = load_yaml((ROOT / "config/dataset_aliases.yaml").read_text())
    print(f"Reading saved extractions for {len(papers)} dated papers...", flush=True)
    current, ablation, coverage, unresolved = build_usage(
        papers,
        stored,
        eligible,
        datasets,
        dataset_name_map(datasets, variants),
        aliases,
        papers_dir,
    )
    data_dir = output / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    coverage.to_csv(data_dir / "extraction_coverage.csv", index=False)
    coverage.loc[coverage["fallback"]].to_csv(data_dir / "missing_extractions.csv", index=False)
    unresolved.to_csv(data_dir / "unresolved_dataset_names.csv", index=False)
    current.to_csv(data_dir / "current_usage.csv", index=False)
    ablation.to_csv(data_dir / "ablation_usage.csv", index=False)
    changes = current[["paper_id", "dataset_name"]].merge(
        ablation[["paper_id", "dataset_name", "evidence_source"]],
        how="outer",
        on=["paper_id", "dataset_name"],
        indicator=True,
    )
    changes.to_csv(data_dir / "membership_comparison.csv", index=False)
    summary = {
        "database": str(db_path.resolve()),
        "papers_dir": str(papers_dir.resolve()),
        "settings": settings,
        "dated_papers_through_2025": len(papers),
        "excluded_undated_or_after_end": int(len(dates) - len(papers)),
        "extraction_status_counts": coverage["status"].value_counts().to_dict(),
        "fallback_papers": int(coverage["fallback"].sum()),
        "fallback_papers_with_stored_results": int(
            (coverage["fallback"] & (coverage["stored_datasets"] > 0)).sum()
        ),
        "unresolved_paper_name_pairs": len(unresolved),
        "comparisons": {},
    }
    filters = {
        "all_papers": lambda df: df.copy(),
        "conference_only": filter_conference_papers,
        "peer_reviewed": filter_peer_reviewed_papers,
    }
    for scope, select in filters.items():
        summary["comparisons"][scope] = {}
        for group, names in (
            ("benchmark", settings["benchmark_list"]),
            ("dataset", settings["dataset_list"]),
        ):
            frames = []
            for frame in (current, ablation):
                mask = frame[f"{group}_name"].isin(names)
                if group == "benchmark":
                    mask &= frame["paper_timestamp"] >= pd.Timestamp(settings["START_DATE"])
                frames.append(select(frame.loc[mask]))
            comparison, tables = compare_counts(*frames, group, names, settings)
            comparison.to_csv(data_dir / f"{scope}_{group}_comparison.csv", index=False)
            plot_comparison(
                tables,
                names,
                group,
                output / "plots" / scope,
                settings["BENCHMARK_START_YEARS"] if group == "benchmark" else {},
            )
            before = set(
                frames[0][["paper_id", f"{group}_name"]].itertuples(index=False, name=None)
            )
            after = set(frames[1][["paper_id", f"{group}_name"]].itertuples(index=False, name=None))
            summary["comparisons"][scope][group] = {
                "current_paper_group_uses": len(before),
                "ablation_paper_group_uses": len(after),
                "added": len(after - before),
                "removed": len(before - after),
                "current_unique_papers": int(frames[0]["paper_id"].nunique()),
                "ablation_unique_papers": int(frames[1]["paper_id"].nunique()),
                "current_papers_missing_extraction": int(
                    (coverage["fallback"] & coverage["paper_id"].isin(frames[0]["paper_id"])).sum()
                ),
                "ablation_fallback_papers": int(
                    (coverage["fallback"] & coverage["paper_id"].isin(frames[1]["paper_id"])).sum()
                ),
            }
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    write_report(output, summary)
    print(json.dumps(summary, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=ROOT / "data/benchmarks.db")
    parser.add_argument("--papers-dir", type=Path, default=ROOT / "papers")
    parser.add_argument("--output-dir", type=Path, default=BASE_DIR)
    args = parser.parse_args()
    run(args.db, args.papers_dir, args.output_dir)


if __name__ == "__main__":
    main()
