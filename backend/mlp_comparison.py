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
HETEROPHILY_BENCHMARKS = frozenset({"Heterophilic Graphs", "Heterophily Benchmark"})
MLP_CITATION_DATASETS = frozenset({"Cora", "CiteSeer", "PubMed"})
MLP_FIGURE_GROUP_ORDER = (
    "Citation",
    "Classic",
    "Heterophilic Graphs (legacy)",
    "Heterophily Benchmark (non-legacy)",
    "OGB",
)
MLP_FIGURE_GROUP_LABELS = {
    "Heterophilic Graphs (legacy)": "Legacy heterophilic",
    "Heterophily Benchmark (non-legacy)": "Modern heterophilic",
}
MLP_FIGURE_DATASET_ORDER = {
    dataset: index
    for index, dataset in enumerate(
        (
            "Cora",
            "CiteSeer",
            "PubMed",
            "Amazon-Photo",
            "Amazon-Computers",
            "Coauthor-CS",
            "WikiCS",
            "Reddit",
            "Coauthor-Physics",
            "Wisconsin",
            "Squirrel",
            "Chameleon",
            "Texas",
            "Cornell",
            "Roman-empire",
            "Actor",
            "Tolokers",
            "Amazon-ratings",
            "Film",
            "Questions",
            "Minesweeper",
            "ogbn-arxiv",
            "ogbn-products",
            "ogbn-papers100M",
            "ogbn-mag",
            "ogbn-proteins",
        )
    )
}
MLP_COMPARISON_COLORS = {
    "better": "#2F6690",
    "tied": "#F2A541",
    "worse": "#c43d4b",
}


def _result_value(result: Any) -> float | None:
    value = result.display_value
    return float(value) if value is not None and math.isfinite(float(value)) else None


def _result_std(result: Any) -> float | None:
    value = result.display_std
    return float(value) if value is not None and math.isfinite(float(value)) else None


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
    combined_std = (_result_std(result) or 0.0) + (_result_std(mlp) or 0.0)
    if abs(value - reference) <= combined_std:
        return "tied"
    if higher_is_better:
        return "better" if value > reference else "worse"
    return "better" if value < reference else "worse"


def _classification_counts(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    counts = dict.fromkeys(("better", "tied", "worse"), 0)
    for row in rows:
        classification = row.get("classification")
        if classification in counts:
            counts[classification] += 1
    return counts


def _worse_share(counts: dict[str, int]) -> float:
    total = sum(counts.values())
    return 100 * counts["worse"] / total if total else 0.0


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


def _benchmark_group_label(dataset: Any) -> str:
    benchmark = getattr(dataset, "benchmark", None)
    benchmark_name = str(getattr(benchmark, "name", "") or "").strip()
    if not benchmark_name:
        return "Other benchmarks"
    if benchmark_name in HETEROPHILY_BENCHMARKS:
        status = "legacy" if bool(getattr(benchmark, "is_legacy", False)) else "non-legacy"
        return f"{benchmark_name} ({status})"
    return benchmark_name


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
                "group": _benchmark_group_label(dataset),
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
) -> tuple[Path, Path, Path, Path]:
    """Write matching method-level and per-paper comparison figures."""
    import os

    mpl_config_dir = Path(tempfile.mkdtemp(prefix="benchmarking-mlp-matplotlib-"))
    os.environ.setdefault("MPLCONFIGDIR", str(mpl_config_dir))
    import matplotlib
    from matplotlib.font_manager import FontProperties
    from matplotlib.transforms import ScaledTranslation

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    output_dir.mkdir(parents=True, exist_ok=True)
    colors = MLP_COMPARISON_COLORS

    def render_figure(level: str, png_name: str, pdf_name: str) -> tuple[Path, Path]:
        figure_rows: list[dict[str, Any]] = []
        for row in comparisons:
            if level == "method":
                figure_row = row
            else:
                paper_counts = _classification_counts(row["paper_results"])
                figure_row = {
                    **row,
                    **{f"{category}_count": count for category, count in paper_counts.items()},
                    "paper_count": sum(paper_counts.values()),
                }
            figure_rows.append(figure_row)

        grouped: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in figure_rows:
            group_name = row["group"]
            if group_name == "Classic" and row["dataset"] in MLP_CITATION_DATASETS:
                group_name = "Citation"
            if group_name in MLP_FIGURE_GROUP_ORDER:
                grouped[group_name].append(row)
        group_names = [group for group in MLP_FIGURE_GROUP_ORDER if grouped[group]]
        if not group_names and figure_rows:
            for row in figure_rows:
                grouped[row["group"]].append(row)
            group_names = sorted(grouped)

        figure, axis = plt.subplots(figsize=(9.8, 4.0))
        labels = []
        positions = []
        group_spans = []
        position = 0
        sort_field = "method_count" if level == "method" else "paper_count"
        for group_name in group_names:
            rows = sorted(
                grouped[group_name],
                key=lambda row: (-row[sort_field], row["dataset"]),
            )
            group_start = position
            for row in rows:
                positions.append(position)
                labels.append(row["dataset"])
                position += 1
            group_spans.append((group_name, group_start, position - 1))
            position += 0.375

        row_by_dataset = {row["dataset"]: row for group in group_names for row in grouped[group]}
        bottom = [0.0] * len(positions)
        segment_values = {}
        legend_handles = []
        category_labels = {
            "better": "Better than MLP",
            "tied": "Tied with MLP",
            "worse": "Worse than MLP",
        }
        for category in ("better", "tied", "worse"):
            values = [row_by_dataset[label][f"{category}_count"] for label in labels]
            segment_values[category] = values
            bars = axis.bar(
                positions,
                values,
                bottom=bottom,
                color=colors[category],
                width=0.78,
                label=category_labels[category],
            )
            legend_handles.append(bars)
            bottom = [current + value for current, value in zip(bottom, values, strict=True)]

        max_total = max(bottom, default=1)
        for group_name, start, end in group_spans:
            center = (start + end) / 2
            axis.text(
                center,
                1.005,
                MLP_FIGURE_GROUP_LABELS.get(group_name, group_name),
                transform=axis.get_xaxis_transform(),
                ha="center",
                va="bottom",
                fontweight="bold",
                fontsize=8.5,
                color="#4f5965",
                clip_on=False,
            )

        axis.set_ylabel("Unique methods" if level == "method" else "Eligible papers")
        display_labels = [label.removeprefix("ogbn-") for label in labels]
        axis.set_xticks(positions, display_labels)
        axis.tick_params(axis="x", length=0, pad=3)
        plt.setp(axis.get_xticklabels(), rotation=55, ha="right", rotation_mode="anchor")
        x_shift = ScaledTranslation(-3 / 72, 0, figure.dpi_scale_trans)
        for label in axis.get_xticklabels():
            label.set_transform(label.get_transform() + x_shift)
        if "Cora" in row_by_dataset:
            cora_total = sum(
                row_by_dataset["Cora"][f"{category}_count"]
                for category in ("better", "tied", "worse")
            )
            y_max = cora_total * 1.045
        else:
            y_max = max_total * 1.045
        axis.set_ylim(0, y_max)

        percentage_font = FontProperties(family="DejaVu Sans", stretch="condensed", size=6.5)
        pixels_per_data_unit = abs(
            axis.transData.transform((0, 1))[1] - axis.transData.transform((0, 0))[1]
        )
        label_height = percentage_font.get_size_in_points() * figure.dpi / 72 * 1.2
        centered_height = label_height / pixels_per_data_unit
        for x, better, tied, worse in zip(
            positions,
            segment_values["better"],
            segment_values["tied"],
            segment_values["worse"],
            strict=True,
        ):
            total = better + tied + worse
            if not worse or not total:
                continue
            centered = worse >= centered_height
            axis.text(
                x,
                better + tied + worse / 2 if centered else better + tied + worse,
                f"{_worse_share({'better': better, 'tied': tied, 'worse': worse}):.0f}%",
                ha="center",
                va="center" if centered else "top",
                fontproperties=percentage_font,
                color="white",
                clip_on=False,
            )

        within_group_gap = 1.0 - 0.78
        axis.set_xlim(
            positions[0] - 0.78 / 2 - within_group_gap,
            positions[-1] + 0.78 / 2,
        )
        axis.grid(axis="y", color="#dce1e6", linewidth=0.7)
        axis.set_axisbelow(True)
        axis.spines[["top", "right"]].set_visible(False)
        figure.legend(
            legend_handles,
            ["Better than MLP", "Tied with MLP", "Worse than MLP"],
            loc="lower center",
            bbox_to_anchor=(0.5, 0.035),
            frameon=False,
            fontsize=9.5,
            ncol=3,
        )
        figure.subplots_adjust(left=0.08, right=0.98, bottom=0.36, top=0.82)

        png_path = output_dir / png_name
        pdf_path = output_dir / pdf_name
        figure.savefig(png_path, dpi=180)
        figure.savefig(pdf_path)
        plt.close(figure)
        return png_path, pdf_path

    method_paths = render_figure("method", "better_tied_worse.png", "better_tied_worse.pdf")
    paper_paths = render_figure(
        "paper", "better_tied_worse_per_paper.png", "better_tied_worse_per_paper.pdf"
    )
    return (*method_paths, *paper_paths)


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
