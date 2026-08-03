"""Build descriptive comparisons between plain MLPs and graph methods."""

from __future__ import annotations

import csv
import json
import math
import tempfile
from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from backend.model_name_resolution import normalize_model_name_for_resolution
from backend.models import Dataset, DatasetVariant, Result
from backend.results_parser import result_is_leaderboard_eligible

NODE_TASKS = frozenset({"node_classification", "node_regression"})


def _result_value(result: Any) -> float | None:
    value = result.display_value
    return float(value) if value is not None and math.isfinite(float(value)) else None


def _result_std(result: Any) -> float | None:
    value = result.display_std
    return float(value) if value is not None else None


def _model_name(result: Any) -> str:
    return str(
        getattr(result, "effective_model_name", None)
        or (result.model.canonical_name if result.model else "")
    ).strip()


def _method_key(name: str) -> str:
    return normalize_model_name_for_resolution(name).casefold()


def _normalized_task(value: Any) -> str:
    return str(value or "").strip().casefold().replace("-", "_").replace(" ", "_")


def _is_llm_augmented_mlp(result: Any, name: str | None = None) -> bool:
    model_name = (name or _model_name(result)).casefold().replace(" ", "")
    feature_source = str(getattr(result, "input_feature_source", "") or "").casefold()
    return feature_source == "llm_features" or (
        "mlp" in model_name and ("llm" in model_name or "bert" in model_name)
    )


def is_comparison_eligible(result: Any) -> bool:
    """Return whether a result is eligible for the canonical MLP statistics."""
    variant = result.dataset_variant
    dataset = variant.dataset if variant else None
    if not dataset or dataset.task_type not in NODE_TASKS:
        return False
    evaluation_task = getattr(result, "evaluation_task", None)
    if evaluation_task and _normalized_task(evaluation_task) != _normalized_task(dataset.task_type):
        return False
    return bool(
        result_is_leaderboard_eligible(result)
        and result.metric_name == dataset.primary_metric
        and not result.is_problematic
        and _result_value(result) is not None
        and not _is_llm_augmented_mlp(result)
    )


def _is_better(candidate: Any, incumbent: Any | None, higher_is_better: bool) -> bool:
    if incumbent is None:
        return True
    candidate_value = _result_value(candidate)
    incumbent_value = _result_value(incumbent)
    if candidate_value is None:
        return False
    if incumbent_value is None:
        return True
    return (
        candidate_value > incumbent_value if higher_is_better else candidate_value < incumbent_value
    )


def _comparison_class(result: Any, mlp: Any, higher_is_better: bool) -> str:
    value = _result_value(result)
    reference = _result_value(mlp)
    if value is None or reference is None or math.isclose(value, reference, abs_tol=1e-12):
        return "tied"
    if higher_is_better:
        return "better" if value > reference else "worse"
    return "better" if value < reference else "worse"


def _paper_id(result: Any) -> str:
    paper = getattr(result, "paper", None)
    return str(getattr(paper, "arxiv_id", "") or getattr(result, "paper_id", ""))


def _source(result: Any) -> dict[str, Any]:
    paper = getattr(result, "paper", None)
    return {
        "paper": _paper_id(result),
        "title": str(getattr(paper, "title", "") or ""),
        "value": _result_value(result),
        "std": _result_std(result),
        "model": _model_name(result),
        "table": str(getattr(result, "table_ref", "") or ""),
        "source_ref": str(getattr(result, "source_ref", "") or ""),
        "protocol_note": str(getattr(result, "protocol_note", "") or ""),
    }


def compare_results(results: Iterable[Result], *, min_papers: int = 10) -> list[dict[str, Any]]:
    """Build one descriptive comparison row per eligible dataset.

    The reference is the best eligible plain MLP. The comparison population is
    the best eligible non-MLP result from each paper, including baselines. Datasets
    need results from at least ``min_papers`` distinct papers to avoid unstable
    comparisons of sparsely evaluated benchmarks.
    """
    grouped: defaultdict[tuple[str, str], list[Any]] = defaultdict(list)
    for result in results:
        if is_comparison_eligible(result):
            dataset = result.dataset_variant.dataset
            grouped[(dataset.name, result.metric_name)].append(result)

    comparisons: list[dict[str, Any]] = []
    for (dataset_name, metric_name), dataset_results in sorted(grouped.items()):
        dataset = dataset_results[0].dataset_variant.dataset
        higher_is_better = bool(dataset_results[0].higher_is_better)
        mlp_results = [
            result
            for result in dataset_results
            if _method_key(_model_name(result)) == "mlp"
            and bool(getattr(result, "is_baseline", False))
            and not _is_llm_augmented_mlp(result)
        ]
        if not mlp_results:
            continue

        best_mlp = max(
            mlp_results,
            key=lambda result: (
                _result_value(result) if higher_is_better else -_result_value(result)
            ),
        )

        non_mlp_by_paper: defaultdict[str, list[Any]] = defaultdict(list)
        for result in dataset_results:
            paper_id = _paper_id(result)
            if not paper_id or _method_key(_model_name(result)) == "mlp":
                continue
            non_mlp_by_paper[paper_id].append(result)

        best_by_paper = {
            paper_id: max(
                paper_results,
                key=lambda result: (
                    _result_value(result) if higher_is_better else -_result_value(result)
                ),
            )
            for paper_id, paper_results in non_mlp_by_paper.items()
            if paper_results
        }
        if not best_by_paper:
            continue
        if len(best_by_paper) < min_papers:
            continue

        non_mlp_by_method: defaultdict[str, list[Any]] = defaultdict(list)
        for result in dataset_results:
            method_key = _method_key(_model_name(result))
            if method_key != "mlp":
                non_mlp_by_method[method_key].append(result)
        best_by_method = {
            method_key: max(
                method_results,
                key=lambda result: (
                    _result_value(result) if higher_is_better else -_result_value(result)
                ),
            )
            for method_key, method_results in non_mlp_by_method.items()
        }
        method_keys = {
            _method_key(_model_name(result))
            for result in dataset_results
            if _method_key(_model_name(result)) != "mlp"
        }

        counts = {"better": 0, "tied": 0, "worse": 0}
        paper_rows: list[dict[str, Any]] = []
        for paper_id, result in sorted(best_by_paper.items()):
            classification = _comparison_class(result, best_mlp, higher_is_better)
            paper_rows.append(
                {
                    "paper": paper_id,
                    "classification": classification,
                    "source": _source(result),
                }
            )

        for result in best_by_method.values():
            counts[_comparison_class(result, best_mlp, higher_is_better)] += 1

        sota = best_mlp
        for result in best_by_paper.values():
            if _is_better(result, sota, higher_is_better):
                sota = result

        mlp_value = _result_value(best_mlp)
        sota_value = _result_value(sota)
        directional_gap = sota_value - mlp_value if higher_is_better else mlp_value - sota_value
        comparisons.append(
            {
                "dataset": dataset_name,
                "group": (
                    dataset.benchmark.name
                    if getattr(dataset, "benchmark", None)
                    else "Other benchmarks"
                ),
                "metric": metric_name,
                "higher_is_better": higher_is_better,
                "reference_type": "best_non_mlp_result_per_paper",
                "paper_count": len(paper_rows),
                "method_count": len(method_keys),
                "better_count": counts["better"],
                "tied_count": counts["tied"],
                "worse_count": counts["worse"],
                "at_least_mlp_count": counts["better"] + counts["tied"],
                "mlp": _source(best_mlp),
                "sota": _source(sota),
                "mlp_to_sota_gap": directional_gap,
                "paper_results": paper_rows,
            }
        )
    return sorted(comparisons, key=lambda row: (-row["at_least_mlp_count"], row["dataset"]))


def write_comparison_outputs(
    comparisons: list[dict[str, Any]], output_dir: Path
) -> tuple[Path, Path, Path]:
    """Write plain JSON, CSV, and human-readable descriptive statistics."""
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "comparison.json"
    csv_path = output_dir / "comparison.csv"
    summary_path = output_dir / "summary.txt"
    json_path.write_text(json.dumps(comparisons, indent=2) + "\n", encoding="utf-8")

    fields = [
        "dataset",
        "group",
        "metric",
        "paper_count",
        "better_count",
        "tied_count",
        "worse_count",
        "at_least_mlp_count",
        "mlp_value",
        "mlp_paper",
        "sota_value",
        "sota_paper",
        "mlp_to_sota_gap",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in comparisons:
            writer.writerow(
                {
                    "dataset": row["dataset"],
                    "group": row["group"],
                    "metric": row["metric"],
                    "paper_count": row["paper_count"],
                    "better_count": row["better_count"],
                    "tied_count": row["tied_count"],
                    "worse_count": row["worse_count"],
                    "at_least_mlp_count": row["at_least_mlp_count"],
                    "mlp_value": row["mlp"]["value"],
                    "mlp_paper": row["mlp"]["paper"],
                    "sota_value": row["sota"]["value"],
                    "sota_paper": row["sota"]["paper"],
                    "mlp_to_sota_gap": row["mlp_to_sota_gap"],
                }
            )

    lines = [
        "MLP baseline comparison",
        "Reference: best eligible plain MLP; comparison: best eligible non-MLP result per paper.",
        "Counts are descriptive directional counts; no significance test is applied.",
        "",
    ]
    for row in comparisons:
        lines.append(
            f"{row['dataset']} ({row['metric']}): MLP {row['mlp']['value']:.4f} "
            f"[{row['mlp']['paper']}] | papers={row['paper_count']} | "
            f"better={row['better_count']} tied={row['tied_count']} "
            f"worse={row['worse_count']} | best={row['sota']['value']:.4f} "
            f"[{row['sota']['paper']}]"
        )
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, csv_path, summary_path


def write_comparison_figures(
    comparisons: list[dict[str, Any]], output_dir: Path
) -> tuple[Path, Path]:
    """Write grouped landscape better/tied/worse figures in PNG and PDF formats."""
    import os

    mpl_config_dir = Path(tempfile.mkdtemp(prefix="benchmarking-mlp-matplotlib-"))
    os.environ.setdefault("MPLCONFIGDIR", str(mpl_config_dir))
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    output_dir.mkdir(parents=True, exist_ok=True)
    grouped: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in comparisons:
        grouped[row["group"]].append(row)
    group_names = sorted(grouped, key=lambda group: (-len(grouped[group]), group))
    columns = 3
    panel_rows = (len(group_names) + columns - 1) // columns
    figure, axes = plt.subplots(
        panel_rows,
        columns,
        figsize=(18, max(10.5, panel_rows * 3.2)),
        squeeze=False,
        sharex=True,
    )
    colors = {
        "better": "#2F6690",
        "tied": "#F2A541",
        "worse": "#8F4068",
    }
    legend_handles = None
    for panel_index, group_name in enumerate(group_names):
        axis = axes[panel_index // columns][panel_index % columns]
        rows = sorted(grouped[group_name], key=lambda row: (-row["paper_count"], row["dataset"]))
        labels = [row["dataset"] for row in rows]
        totals = [row["paper_count"] for row in rows]
        denominators = [max(total, 1) for total in totals]
        better = [
            100 * row["better_count"] / denominator
            for row, denominator in zip(rows, denominators, strict=True)
        ]
        tied = [
            100 * row["tied_count"] / denominator
            for row, denominator in zip(rows, denominators, strict=True)
        ]
        worse = [
            100 * row["worse_count"] / denominator
            for row, denominator in zip(rows, denominators, strict=True)
        ]
        positions = list(range(len(rows)))
        first = axis.barh(positions, better, color=colors["better"], label="Better than MLP")
        second = axis.barh(
            positions, tied, left=better, color=colors["tied"], label="Tied with MLP"
        )
        third = axis.barh(
            positions,
            worse,
            left=[
                better_value + tied_value
                for better_value, tied_value in zip(better, tied, strict=True)
            ],
            color=colors["worse"],
            label="Worse than MLP",
        )
        legend_handles = (first, second, third)
        axis.set_yticks(positions, labels, fontsize=8)
        axis.set_title(group_name, loc="left", fontsize=11, fontweight="bold")
        axis.set_xlim(0, 100)
        axis.invert_yaxis()
        axis.grid(axis="x", alpha=0.2)
        axis.set_axisbelow(True)
        axis.tick_params(axis="x", labelsize=8)
        for position, total in zip(positions, totals, strict=True):
            axis.text(101, position, f"n={total}", va="center", fontsize=7, clip_on=False)

    for axis in axes.flat[len(group_names) :]:
        axis.set_visible(False)
    for axis in axes[-1]:
        if axis.get_visible():
            axis.set_xlabel("Share of eligible papers (%)", fontsize=9)
    figure.suptitle("MLP baseline comparison grouped by benchmark family", fontsize=16, y=0.995)
    figure.text(
        0.5,
        0.965,
        "Each bar sums to 100%; n is the number of eligible papers contributing a non-MLP result.",
        ha="center",
        fontsize=10,
    )
    if legend_handles:
        figure.legend(
            legend_handles,
            ["Better than MLP", "Tied with MLP", "Worse than MLP"],
            loc="lower center",
            ncol=3,
            bbox_to_anchor=(0.5, 0.005),
            frameon=False,
        )
    figure.tight_layout(rect=(0, 0.04, 1, 0.95))

    png_path = output_dir / "better_tied_worse.png"
    pdf_path = output_dir / "better_tied_worse.pdf"
    figure.savefig(png_path, dpi=180)
    figure.savefig(pdf_path)
    plt.close(figure)
    return png_path, pdf_path


def load_comparison_results() -> list[Result]:
    """Load all result rows needed by the comparison through a read-only ORM query."""
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, joinedload

    from backend.config import cfg

    # Statistics generation must not enable WAL or otherwise mutate the
    # benchmark database.  The immutable URI also permits reading a database
    # while another process has an active WAL file.
    db_path = cfg.db_path.resolve()
    engine = create_engine(
        f"sqlite:///{db_path}?mode=ro&immutable=1",
        connect_args={"uri": True, "check_same_thread": False},
    )
    with Session(engine) as session:
        return (
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
