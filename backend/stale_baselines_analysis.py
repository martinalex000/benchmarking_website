"""Analyze whether papers reused materially inferior, stale benchmark baselines.

The analysis is deliberately restricted to curated primary-metric rows and uses
the same leaderboard eligibility and model canonicalization as the Hugo export.
For each baseline row, the prior reference excludes the paper being evaluated;
this prevents a paper's own result from making its baseline look historically
competitive.
"""

from __future__ import annotations

import csv
import json
import math
import random
import sqlite3
from collections import defaultdict
from collections.abc import Iterable
from datetime import date
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MaxNLocator, PercentFormatter, ScalarFormatter
from matplotlib.transforms import ScaledTranslation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.at_pub_timeline import clear_at_pub_caches
from backend.export_to_hugo import (
    _global_ranks_cached,
    _model_key,
    _primary_metric_results,
    clear_export_caches,
)
from backend.models import Result
from backend.venue import is_conference_publication_venue

LRGB_SHORT_NAME = "lrgb"
LRGB_DATASETS = frozenset(
    {"COCO-SP", "PCQM-Contact", "PascalVOC-SP", "Peptides-func", "Peptides-struct"}
)
SELECTED_DATASET_GROUPS = (
    ("Citation datasets", ("Cora", "CiteSeer", "PubMed")),
    ("TU datasets", ("MUTAG", "NCI1", "PROTEINS", "ENZYMES", "D&D")),
    (
        "OGB",
        (
            "ogbg-molhiv",
            "ogbg-molpcba",
            "ogbn-products",
            "ogbn-papers100M",
            "ogbn-arxiv",
        ),
    ),
    (
        "Legacy heterophilic",
        ("Texas", "Wisconsin", "Cornell", "Actor", "Chameleon", "Squirrel"),
    ),
    (
        "Modern heterophilic",
        ("Roman-empire", "Amazon-ratings", "Minesweeper", "Tolokers", "Questions"),
    ),
    ("LRGB", ("COCO-SP", "PCQM-Contact", "PascalVOC-SP", "Peptides-func", "Peptides-struct")),
)
SELECTED_DATASET_NAMES = frozenset(
    dataset for _, datasets in SELECTED_DATASET_GROUPS for dataset in datasets
)
SELECTED_DATASET_LABELS = {
    "ogbg-molhiv": "molhiv",
    "ogbg-molpcba": "molpcba",
    "ogbn-products": "products",
    "ogbn-papers100M": "papers100M",
    "ogbn-arxiv": "arxiv",
}
CATEGORY_LABELS = {
    "prior_better": "Better result available at publication",
    "future_only": "Better result since publication",
    "no_gap": "No material better result found",
}
CATEGORY_COLORS = {
    "prior_better": "#c43d4b",
    "future_only": "#c47a00",
    "no_gap": "#c5ccd3",
}
GAP_CLOSURE_BINS = np.arange(0, 101, 10)


def _ro_session(db_path: Path):
    """Return a SQLAlchemy session factory backed by an immutable SQLite view."""
    resolved = db_path.resolve()

    def connect() -> sqlite3.Connection:
        return sqlite3.connect(
            f"file:{resolved}?mode=ro&immutable=1",
            check_same_thread=False,
            uri=True,
        )

    engine = create_engine("sqlite://", creator=connect)
    return engine, sessionmaker(bind=engine, expire_on_commit=False)


def _finite(value: Any) -> float | None:
    if value is None:
        return None
    try:
        converted = float(value)
    except (TypeError, ValueError):
        return None
    return converted if math.isfinite(converted) else None


def _date_text(value: Any) -> str:
    return str(value or "")[:10]


def _days_between(later: str, earlier: str) -> int | None:
    if not later or not earlier:
        return None
    try:
        return (date.fromisoformat(later) - date.fromisoformat(earlier)).days
    except ValueError:
        return None


def _directional_shortfall(
    reported: float | None, reference: float | None, higher_is_better: bool
) -> float | None:
    if reported is None or reference is None:
        return None
    return (reference - reported) if higher_is_better else (reported - reference)


def _materially_worse(
    reported: float | None,
    reference: float | None,
    higher_is_better: bool,
    reported_std: float | None,
    reference_std: float | None,
) -> bool:
    shortfall = _directional_shortfall(reported, reference, higher_is_better)
    if shortfall is None or shortfall <= 1e-12:
        return False
    combined_std = (reported_std or 0.0) + (reference_std or 0.0)
    return shortfall > combined_std and shortfall > 1e-12


def _gap_closed_percentage(
    reported: float | None,
    prior: float | None,
    sota: float | None,
    higher_is_better: bool,
) -> float | None:
    """Return the better baseline result's share of the dataset SOTA gap."""
    prior_gap = _directional_shortfall(reported, prior, higher_is_better)
    sota_gap = _directional_shortfall(reported, sota, higher_is_better)
    if prior_gap is None or sota_gap is None or sota_gap <= 1e-12:
        return None
    return max(0.0, min(100.0, 100.0 * prior_gap / sota_gap))


def _benchmark_label(result: Result) -> str:
    dataset = result.dataset_variant.dataset
    benchmark = dataset.benchmark
    return (benchmark.short_name if benchmark else "other") or "other"


def _is_lrgb(result: Result) -> bool:
    return _benchmark_label(result).casefold() == LRGB_SHORT_NAME


def _group_label(result: Result) -> str:
    dataset = result.dataset_variant.dataset
    return dataset.name if _is_lrgb(result) else _benchmark_label(result)


def _comparison_row(
    result: Result,
    *,
    today_truth: dict[str, Any],
    prior_truth: dict[str, Any] | None,
    sota_truth: dict[str, Any],
) -> dict[str, Any] | None:
    paper = result.paper
    dataset = result.dataset_variant.dataset
    reported = _finite(result.display_value)
    reported_std = _finite(result.display_std)
    today_value = _finite(today_truth.get("value"))
    today_std = _finite(today_truth.get("std"))
    sota_value = _finite(sota_truth.get("value"))
    sota_std = _finite(sota_truth.get("std"))
    paper_date = _date_text(paper.published_date if paper else "")
    prior_value = _finite(prior_truth.get("value")) if prior_truth else None
    prior_std = _finite(prior_truth.get("std")) if prior_truth else None
    higher = bool(result.higher_is_better)
    prior_better = _materially_worse(reported, prior_value, higher, reported_std, prior_std)
    today_better = _materially_worse(reported, today_value, higher, reported_std, today_std)
    if prior_better:
        category = "prior_better"
    elif today_better:
        category = "future_only"
    else:
        category = "no_gap"

    prior_date = _date_text(prior_truth.get("date_iso")) if prior_truth else ""
    today_date = _date_text(today_truth.get("date_iso"))
    prior_shortfall = _directional_shortfall(reported, prior_value, higher)
    today_shortfall = _directional_shortfall(reported, today_value, higher)
    gap_closed_pct = (
        _gap_closed_percentage(reported, prior_value, sota_value, higher) if prior_better else None
    )
    relative_gap = (
        100.0 * prior_shortfall / abs(prior_value)
        if prior_shortfall is not None and prior_value and prior_value != 0
        else None
    )
    return {
        "paper": paper.arxiv_id if paper else "",
        "title": paper.title if paper else "",
        "paper_date": paper_date,
        "year": int(paper_date[:4]) if len(paper_date) >= 4 and paper_date[:4].isdigit() else None,
        "benchmark": _benchmark_label(result),
        "group": _group_label(result),
        "dataset": dataset.name,
        "task": dataset.task_type or "",
        "metric": result.metric_name,
        "model": result.effective_model_name,
        "higher_is_better": higher,
        "reported_value": reported,
        "reported_std": reported_std,
        "prior_value": prior_value,
        "prior_std": prior_std,
        "prior_source_paper": prior_truth.get("arxiv_id", "") if prior_truth else "",
        "prior_source_date": prior_date,
        "prior_source_title": prior_truth.get("title", "") if prior_truth else "",
        "prior_days_available": _days_between(paper_date, prior_date),
        "today_value": today_value,
        "today_std": today_std,
        "today_source_paper": today_truth.get("arxiv_id", ""),
        "today_source_date": today_date,
        "sota_value": sota_value,
        "sota_std": sota_std,
        "sota_source_paper": sota_truth.get("arxiv_id", ""),
        "sota_source_date": _date_text(sota_truth.get("date_iso")),
        "prior_better": prior_better,
        "today_better": today_better,
        "category": category,
        "prior_shortfall": prior_shortfall,
        "today_shortfall": today_shortfall,
        "relative_gap_pct": relative_gap,
        "gap_closed_pct": gap_closed_pct,
    }


def load_analysis_rows(
    db_path: Path, *, conference_only: bool = False
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Load comparable baseline rows and return rows plus population metadata."""
    clear_export_caches()
    clear_at_pub_caches()
    engine, session_factory = _ro_session(db_path)
    try:
        with session_factory() as session:
            results = _primary_metric_results(session)
            baseline_results = [result for result in results if bool(result.is_baseline)]
            if conference_only:
                baseline_results = [
                    result
                    for result in baseline_results
                    if is_conference_publication_venue(result.paper.venue if result.paper else "")
                ]
            rows: list[dict[str, Any]] = []
            skipped_no_truth = 0
            skipped_no_value = 0
            timeline_cache: dict[tuple[str, str, bool], Any] = {}
            truth_cache: dict[tuple[str, str, bool], dict[str, dict[str, Any]]] = {}
            sota_cache: dict[tuple[str, str, bool], dict[str, Any] | None] = {}
            for result in baseline_results:
                reported = _finite(result.display_value)
                if reported is None:
                    skipped_no_value += 1
                    continue
                dataset = result.dataset_variant.dataset
                metric = dataset.primary_metric or result.metric_name
                higher = bool(result.higher_is_better)
                cache_key = (dataset.name, metric, higher)
                if cache_key not in truth_cache:
                    _, global_rows, truth = _global_ranks_cached(session, *cache_key)
                    truth_cache[cache_key] = truth
                    sota_cache[cache_key] = global_rows[0] if global_rows else None
                model_key = _model_key(result.effective_model_name)
                today_truth = truth_cache[cache_key].get(model_key)
                sota_truth = sota_cache[cache_key]
                if not today_truth or not sota_truth:
                    skipped_no_truth += 1
                    continue
                if cache_key not in timeline_cache:
                    from backend.at_pub_timeline import at_pub_timeline

                    timeline_cache[cache_key] = at_pub_timeline(session, *cache_key)
                paper_date = _date_text(result.paper.published_date if result.paper else "")
                prior_truth = timeline_cache[cache_key].best_for_model(
                    model_key,
                    paper_date,
                    exclude_arxiv=result.paper.arxiv_id if result.paper else "",
                )
                row = _comparison_row(
                    result,
                    today_truth=today_truth,
                    prior_truth=prior_truth,
                    sota_truth=sota_truth,
                )
                if row:
                    rows.append(row)
            metadata = {
                "db": str(db_path),
                "eligible_primary_rows": len(results),
                "baseline_rows": len(baseline_results),
                "comparable_baseline_rows": len(rows),
                "skipped_no_today_truth": skipped_no_truth,
                "skipped_no_value": skipped_no_value,
                "lrgb_rows": sum(row["benchmark"] == LRGB_SHORT_NAME for row in rows),
                "generated_on": date.today().isoformat(),
                "conference_only": conference_only,
            }
            return rows, metadata
    finally:
        engine.dispose()


def summarize(rows: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate row-level classifications by LRGB dataset and benchmark."""
    rows = list(rows)

    def stats(group_rows: list[dict[str, Any]]) -> dict[str, Any]:
        counts = {
            category: sum(row["category"] == category for row in group_rows)
            for category in CATEGORY_LABELS
        }
        total = len(group_rows)
        prior_reference_rows = sum(row["prior_value"] is not None for row in group_rows)
        return {
            "rows": total,
            **counts,
            "prior_reference_rows": prior_reference_rows,
            "prior_rate": counts["prior_better"] / total if total else None,
            "prior_rate_given_reference": (
                counts["prior_better"] / prior_reference_rows if prior_reference_rows else None
            ),
            "any_gap_rate": (
                (counts["prior_better"] + counts["future_only"]) / total if total else None
            ),
            "papers": len({row["paper"] for row in group_rows if row["paper"]}),
        }

    by_group: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_group[row["group"]].append(row)
    benchmark_stats = {
        group: stats(group_rows)
        for group, group_rows in sorted(by_group.items())
        if group not in LRGB_DATASETS
    }
    benchmark_group_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        benchmark_group_rows[_benchmark_group_name(row)].append(row)
    benchmark_group_stats = {
        group: stats(group_rows) for group, group_rows in sorted(benchmark_group_rows.items())
    }
    lrgb_stats = {dataset: stats(by_group.get(dataset, [])) for dataset in sorted(LRGB_DATASETS)}
    prior_rows = [row for row in rows if row["category"] == "prior_better"]
    lrgb_prior = [row for row in prior_rows if row["benchmark"] == LRGB_SHORT_NAME]

    def paper_level_stats(group_rows: list[dict[str, Any]]) -> dict[str, Any]:
        by_paper: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in group_rows:
            by_paper[row["paper"]].append(row)
        paper_count = len(by_paper)
        papers_with_prior = sum(
            any(row["category"] == "prior_better" for row in paper_rows)
            for paper_rows in by_paper.values()
        )
        papers_with_any_gap = sum(
            any(row["category"] in {"prior_better", "future_only"} for row in paper_rows)
            for paper_rows in by_paper.values()
        )
        return {
            "papers": paper_count,
            "papers_with_prior_better": papers_with_prior,
            "papers_with_any_gap": papers_with_any_gap,
            "prior_rate": papers_with_prior / paper_count if paper_count else None,
            "any_gap_rate": papers_with_any_gap / paper_count if paper_count else None,
        }

    paper_level = {
        "all": paper_level_stats(rows),
        "lrgb": paper_level_stats([row for row in rows if row["benchmark"] == LRGB_SHORT_NAME]),
        "other": paper_level_stats([row for row in rows if row["benchmark"] != LRGB_SHORT_NAME]),
    }
    return {
        "overall": stats(rows),
        "lrgb": lrgb_stats,
        "benchmarks": benchmark_stats,
        "benchmark_groups": benchmark_group_stats,
        "paper_level": paper_level,
        "prior_rows": len(prior_rows),
        "lrgb_prior_rows": len(lrgb_prior),
        "lrgb_prior_median_lag_days": (
            float(
                np.median(
                    [
                        row["prior_days_available"]
                        for row in lrgb_prior
                        if row["prior_days_available"] is not None
                    ]
                )
            )
            if any(row["prior_days_available"] is not None for row in lrgb_prior)
            else None
        ),
    }


def _save_figure(fig: plt.Figure, output_dir: Path, stem: str, *, tight: bool = True) -> list[Path]:
    paths = [output_dir / f"{stem}.png", output_dir / f"{stem}.pdf"]
    save_kwargs = {"bbox_inches": "tight"} if tight else {}
    fig.savefig(paths[0], dpi=220, **save_kwargs)
    try:
        fig.savefig(paths[1], **save_kwargs)
    except (OSError, RuntimeError) as exc:
        # Network-backed workspaces can transiently reject a second large write;
        # the PNG remains sufficient for inspection and paper-figure review.
        paths.pop()
        print(f"Warning: could not write {stem}.pdf: {exc}")
    plt.close(fig)
    return paths


def _benchmark_group_name(row: dict[str, Any]) -> str:
    return "LRGB" if row["benchmark"] == LRGB_SHORT_NAME else row["benchmark"]


def _paper_categories(group_rows: list[dict[str, Any]]) -> list[str]:
    by_paper: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in group_rows:
        by_paper[row["paper"]].append(row)
    categories: list[str] = []
    for paper_rows in by_paper.values():
        if any(row["category"] == "prior_better" for row in paper_rows):
            categories.append("prior_better")
        elif any(row["category"] == "future_only" for row in paper_rows):
            categories.append("future_only")
        else:
            categories.append("no_gap")
    return categories


def _absolute_counts(group_rows: list[dict[str, Any]], unit: str) -> dict[str, int]:
    categories = (
        _paper_categories(group_rows)
        if unit == "papers"
        else [row["category"] for row in group_rows]
    )
    return {category: categories.count(category) for category in CATEGORY_LABELS}


def _normalized_category_values(counts: dict[str, int]) -> dict[str, float]:
    total = counts["total"]
    return {
        category: 100 * counts[category] / total if total else 0.0 for category in CATEGORY_LABELS
    }


def _grouped_counts(
    rows: list[dict[str, Any]], *, dimension: str, unit: str, min_papers: int = 0
) -> dict[str, dict[str, int]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        name = _benchmark_group_name(row) if dimension == "benchmark" else row["dataset"]
        grouped[name].append(row)
    if min_papers:
        grouped = {
            name: group_rows
            for name, group_rows in grouped.items()
            if len({row["paper"] for row in group_rows}) >= min_papers
        }
    return {
        name: {
            **_absolute_counts(group_rows, unit),
            "total": sum(_absolute_counts(group_rows, unit).values()),
            "papers": len({row["paper"] for row in group_rows}),
        }
        for name, group_rows in grouped.items()
    }


def _selected_dataset_paper_counts(
    rows: list[dict[str, Any]],
    *,
    unit: str = "papers",
) -> tuple[dict[str, dict[str, int]], list[tuple[str, list[str]]]]:
    """Return counts in the requested dataset blocks, preserving their order."""
    rows_by_dataset: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        rows_by_dataset[row["dataset"]].append(row)

    counts: dict[str, dict[str, int]] = {}
    groups: list[tuple[str, list[str]]] = []
    for group_name, dataset_names in SELECTED_DATASET_GROUPS:
        present = [dataset for dataset in dataset_names if dataset in rows_by_dataset]
        groups.append((group_name, present))
        counts.update(
            {
                dataset: {
                    **_absolute_counts(rows_by_dataset[dataset], unit),
                    "total": sum(_absolute_counts(rows_by_dataset[dataset], unit).values()),
                    "papers": len({row["paper"] for row in rows_by_dataset[dataset]}),
                }
                for dataset in present
            }
        )
    return counts, groups


def _ordered_selected_dataset_groups(
    counts: dict[str, dict[str, int]], groups: list[tuple[str, list[str]]]
) -> list[tuple[str, list[str]]]:
    descending_groups = {"Legacy heterophilic", "Modern heterophilic", "LRGB"}
    return [
        (
            group_name,
            sorted(
                datasets,
                key=lambda dataset: -counts[dataset]["total"],
            )
            if group_name in descending_groups
            else datasets,
        )
        for group_name, datasets in groups
    ]


def _selected_dataset_plot_layout(
    counts: dict[str, dict[str, int]], groups: list[tuple[str, list[str]]]
) -> tuple[list[str], np.ndarray, list[tuple[str, float, float]]]:
    dataset_groups = [
        (name, datasets)
        for name, datasets in _ordered_selected_dataset_groups(counts, groups)
        if datasets
    ]
    positions: list[float] = []
    section_spans: list[tuple[str, float, float]] = []
    group_gap = 0.375
    for group_index, (group_name, datasets) in enumerate(dataset_groups):
        start = len(positions) + group_index * group_gap
        group_positions = [start + offset for offset in range(len(datasets))]
        positions.extend(group_positions)
        section_spans.append((group_name, group_positions[0], group_positions[-1]))
    return (
        [dataset for _, datasets in dataset_groups for dataset in datasets],
        np.array(positions),
        section_spans,
    )


def _plot_absolute_stacked(
    counts: dict[str, dict[str, int]],
    output_dir: Path,
    *,
    stem: str,
    title: str,
    unit_label: str,
    footer: str,
) -> list[Path]:
    groups = sorted(counts, key=lambda group: (-counts[group]["total"], group))
    y = np.arange(len(groups))
    fig_height = max(5.5, 0.32 * len(groups) + 1.8)
    fig, ax = plt.subplots(figsize=(8.5, fig_height))
    left = np.zeros(len(groups))
    for category in CATEGORY_LABELS:
        values = np.array([counts[group][category] for group in groups])
        ax.barh(
            y,
            values,
            left=left,
            color=CATEGORY_COLORS[category],
            label=CATEGORY_LABELS[category],
            height=0.72,
        )
        left += values
    ax.set_yticks(y, groups)
    ax.invert_yaxis()
    max_total = max((counts[group]["total"] for group in groups), default=1)
    ax.set_xlim(0, max_total * 1.18)
    ax.set_xlabel(f"Number of {unit_label}")
    ax.grid(axis="x", color="#dce1e6", linewidth=0.7)
    ax.set_axisbelow(True)
    for index, group in enumerate(groups):
        total = counts[group]["total"]
        ax.text(total + max_total * 0.015, index, f"n={total}", va="center", fontsize=8)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    fig.suptitle(title, x=0.07, ha="left", fontsize=15, fontweight="bold")
    fig.text(0.07, 0.01, footer, fontsize=8.5, color="#4f5965")
    fig.subplots_adjust(left=0.27, right=0.91, bottom=0.09, top=0.92)
    return _save_figure(fig, output_dir, stem)


def plot_benchmark_paper_counts(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    return _plot_absolute_stacked(
        _grouped_counts(rows, dimension="benchmark", unit="papers"),
        output_dir,
        stem="figure_1_stale_baselines_by_benchmark_papers",
        title="Stale baselines across benchmark groups",
        unit_label="papers",
        footer=(
            "Each paper is counted once per benchmark group. Red takes precedence over yellow: a paper with "
            "both an already-available and later gap is counted only as red."
        ),
    )


def plot_dataset_paper_counts(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    return _plot_absolute_stacked(
        _grouped_counts(rows, dimension="dataset", unit="papers", min_papers=5),
        output_dir,
        stem="figure_2_stale_baselines_by_dataset_papers",
        title="Stale baselines across individual datasets",
        unit_label="papers",
        footer=(
            "Datasets reported by fewer than five papers are omitted. Each paper is counted once per dataset; "
            "red takes precedence over yellow."
        ),
    )


def plot_benchmark_entry_counts(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    return _plot_absolute_stacked(
        _grouped_counts(rows, dimension="benchmark", unit="entries"),
        output_dir,
        stem="figure_3_stale_baselines_by_benchmark_entries",
        title="Stale baseline entries across benchmark groups",
        unit_label="baseline entries",
        footer=(
            "Unlike the paper-level plot, every comparable baseline entry contributes one count. Red and yellow "
            "are mutually exclusive by construction."
        ),
    )


def plot_dataset_entry_counts(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    return _plot_absolute_stacked(
        _grouped_counts(rows, dimension="dataset", unit="entries", min_papers=5),
        output_dir,
        stem="figure_4_stale_baselines_by_dataset_entries",
        title="Stale baseline entries across individual datasets",
        unit_label="baseline entries",
        footer=(
            "Datasets reported by fewer than five papers are omitted. Every comparable baseline entry contributes "
            "one count; red and yellow are mutually exclusive by construction."
        ),
    )


def _plot_selected_dataset_counts(
    rows: list[dict[str, Any]],
    output_dir: Path,
    *,
    unit: str,
    unit_label: str,
    stem: str,
) -> list[Path]:
    counts, groups = _selected_dataset_paper_counts(rows, unit=unit)
    labels, x, section_spans = _selected_dataset_plot_layout(counts, groups)
    fig, ax = plt.subplots(figsize=(9.8, 4.0))
    bottom = np.zeros(len(labels))
    bar_width = 0.78
    for category in CATEGORY_LABELS:
        values = np.array([counts[dataset][category] for dataset in labels])
        ax.bar(
            x,
            values,
            bottom=bottom,
            color=CATEGORY_COLORS[category],
            label=CATEGORY_LABELS[category],
            width=bar_width,
        )
        bottom += values
    ax.set_xticks(x, [SELECTED_DATASET_LABELS.get(dataset, dataset) for dataset in labels])
    within_group_gap = 1.0 - bar_width
    ax.set_xlim(x[0] - bar_width / 2 - within_group_gap, x[-1] + bar_width / 2)
    ax.tick_params(axis="x", length=0, pad=3)
    plt.setp(ax.get_xticklabels(), rotation=55, ha="right", rotation_mode="anchor")
    x_shift = ScaledTranslation(-3 / 72, 0, fig.dpi_scale_trans)
    for label in ax.get_xticklabels():
        label.set_transform(label.get_transform() + x_shift)
    max_total = max((counts[dataset]["total"] for dataset in labels), default=1)
    ax.set_ylim(0, max_total * 1.045)
    ax.set_ylabel(f"Number of {unit_label}")
    ax.grid(axis="y", color="#dce1e6", linewidth=0.7)
    ax.set_axisbelow(True)
    segment_threshold = max_total * 0.045
    percentage_font = FontProperties(family="DejaVu Sans", stretch="condensed", size=6.5)
    label_step = max_total * 0.05
    percentage_labels: list[tuple[float, float, str, str]] = []
    for index, dataset in enumerate(labels):
        total = counts[dataset]["total"]
        prior_count = counts[dataset]["prior_better"]
        future_count = counts[dataset]["future_only"]
        prior_pct = 100 * counts[dataset]["prior_better"] / total if total else 0
        future_pct = 100 * counts[dataset]["future_only"] / total if total else 0
        fallback: list[tuple[str, float, str]] = []
        if prior_count >= segment_threshold:
            percentage_labels.append((x[index], prior_count / 2, f"{prior_pct:.0f}%", "white"))
        else:
            fallback.append(("prior", prior_pct, CATEGORY_COLORS["prior_better"]))
        if future_count >= segment_threshold:
            percentage_labels.append(
                (
                    x[index],
                    prior_count + future_count / 2,
                    f"{future_pct:.0f}%",
                    "#242b33",
                )
            )
        else:
            fallback.append(("future", future_pct, CATEGORY_COLORS["future_only"]))
        if fallback:
            gray_start = prior_count + future_count
            for line, (_, percentage, color) in enumerate(fallback):
                percentage_labels.append(
                    (
                        x[index],
                        gray_start + (line + 0.5) * label_step,
                        f"{percentage:.0f}%",
                        color,
                    )
                )
    for x_position, y_position, label, color in percentage_labels:
        ax.text(
            x_position,
            y_position,
            label,
            ha="center",
            va="center",
            fontproperties=percentage_font,
            color=color,
        )
    for group_name, start, end in section_spans:
        midpoint = (start + end) / 2
        ax.text(
            midpoint,
            1.005,
            group_name,
            transform=ax.get_xaxis_transform(),
            ha="center",
            va="bottom",
            fontsize=8.5,
            fontweight="bold",
            color="#4f5965",
            clip_on=False,
        )
    ax.spines[["top", "right"]].set_visible(False)
    fig.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 0.035),
        frameon=False,
        fontsize=9.5,
        ncol=3,
    )
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.36, top=0.82)
    return _save_figure(fig, output_dir, stem, tight=False)


def plot_selected_dataset_paper_counts(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    return _plot_selected_dataset_counts(
        rows,
        output_dir,
        unit="papers",
        unit_label="papers",
        stem="figure_6_stale_baselines_selected_dataset_papers",
    )


def plot_selected_dataset_result_counts(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    return _plot_selected_dataset_counts(
        rows,
        output_dir,
        unit="entries",
        unit_label="results",
        stem="figure_7_stale_baselines_selected_dataset_results",
    )


def _plot_selected_dataset_percentage_counts(
    rows: list[dict[str, Any]],
    output_dir: Path,
    *,
    unit: str,
    unit_label: str,
    stem: str,
) -> list[Path]:
    counts, groups = _selected_dataset_paper_counts(rows, unit=unit)
    labels, x, section_spans = _selected_dataset_plot_layout(counts, groups)
    fig, ax = plt.subplots(figsize=(9.8, 4.0))
    bar_width = 0.78
    bottom = np.zeros(len(labels))
    percentage_font = FontProperties(family="DejaVu Sans", stretch="condensed", size=6.5)
    text_colors = {
        "prior_better": "white",
        "future_only": "#242b33",
        "no_gap": "#242b33",
    }
    for category in CATEGORY_LABELS:
        values = np.array(
            [_normalized_category_values(counts[dataset])[category] for dataset in labels]
        )
        ax.bar(
            x,
            values,
            bottom=bottom,
            color=CATEGORY_COLORS[category],
            label=CATEGORY_LABELS[category],
            width=bar_width,
        )
        for index, value in enumerate(values):
            if category == "future_only" and value < 5:
                normalized_counts = _normalized_category_values(counts[labels[index]])
                gray_start = normalized_counts["prior_better"] + normalized_counts["future_only"]
                gray_height = normalized_counts["no_gap"]
                if gray_height:
                    y_position = gray_start + min(2.5, gray_height / 2)
                else:
                    y_position = bottom[index] + value / 2
                text_color = CATEGORY_COLORS["future_only"]
            elif value >= 5:
                y_position = bottom[index] + value / 2
                text_color = text_colors[category]
            else:
                y_position = None
            if y_position is not None:
                ax.text(
                    x[index],
                    y_position,
                    f"{value:.0f}%",
                    ha="center",
                    va="center",
                    fontproperties=percentage_font,
                    color=text_color,
                )
        bottom += values
    within_group_gap = 1.0 - bar_width
    ax.set_xlim(x[0] - bar_width / 2 - within_group_gap, x[-1] + bar_width / 2)
    ax.set_ylim(0, 100)
    ax.set_xticks(x, [SELECTED_DATASET_LABELS.get(dataset, dataset) for dataset in labels])
    ax.tick_params(axis="x", length=0, pad=3)
    plt.setp(ax.get_xticklabels(), rotation=55, ha="right", rotation_mode="anchor")
    x_shift = ScaledTranslation(-3 / 72, 0, fig.dpi_scale_trans)
    for label in ax.get_xticklabels():
        label.set_transform(label.get_transform() + x_shift)
    ax.set_ylabel(f"Share of {unit_label}")
    ax.set_yticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.grid(axis="y", color="#dce1e6", linewidth=0.7)
    ax.set_axisbelow(True)
    for group_name, start, end in section_spans:
        ax.text(
            (start + end) / 2,
            1.005,
            group_name,
            transform=ax.get_xaxis_transform(),
            ha="center",
            va="bottom",
            fontsize=8.5,
            fontweight="bold",
            color="#4f5965",
            clip_on=False,
        )
    ax.spines[["top", "right"]].set_visible(False)
    fig.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 0.035),
        frameon=False,
        fontsize=9.5,
        ncol=3,
    )
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.36, top=0.82)
    return _save_figure(fig, output_dir, stem, tight=False)


def plot_selected_dataset_paper_percentages(
    rows: list[dict[str, Any]], output_dir: Path
) -> list[Path]:
    return _plot_selected_dataset_percentage_counts(
        rows,
        output_dir,
        unit="papers",
        unit_label="papers",
        stem="figure_8_stale_baselines_selected_dataset_paper_percentages",
    )


def plot_selected_dataset_result_percentages(
    rows: list[dict[str, Any]], output_dir: Path
) -> list[Path]:
    return _plot_selected_dataset_percentage_counts(
        rows,
        output_dir,
        unit="entries",
        unit_label="results",
        stem="figure_9_stale_baselines_selected_dataset_result_percentages",
    )


def _selected_gap_closure_values(
    rows: list[dict[str, Any]], datasets: Iterable[str] | None = None
) -> list[float]:
    selected = set(datasets) if datasets is not None else SELECTED_DATASET_NAMES
    return [
        float(row["gap_closed_pct"])
        for row in rows
        if row["category"] == "prior_better"
        and row.get("gap_closed_pct") is not None
        and (selected is None or row["dataset"] in selected)
    ]


def _style_gap_closure_axis(ax: Any) -> None:
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 101, 20), [f"{value}%" for value in range(0, 101, 20)])
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))
    ax.grid(axis="y", color="#dce1e6", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)


def _histogram_percentage_weights(values: list[float]) -> np.ndarray:
    return np.full(len(values), 100.0 / len(values)) if values else np.array([])


def _plot_gap_closure_histogram(values: list[float], output_dir: Path, stem: str) -> list[Path]:
    fig, ax = plt.subplots(figsize=(4.2, 2.8))
    ax.hist(
        values,
        bins=GAP_CLOSURE_BINS,
        color=CATEGORY_COLORS["prior_better"],
        edgecolor="white",
        linewidth=0.6,
    )
    _style_gap_closure_axis(ax)
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel("Share of gap to current SOTA closed at publication", fontsize=9)
    ax.set_ylabel("Number of results", fontsize=10)
    fig.subplots_adjust(left=0.21, right=0.95, bottom=0.23, top=0.96)
    return _save_figure(fig, output_dir, stem, tight=False)


def plot_selected_gap_closure_histogram(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    return _plot_gap_closure_histogram(
        _selected_gap_closure_values(rows),
        output_dir,
        "figure_10_stale_baseline_gap_closure_selected_results",
    )


def plot_selected_gap_closure_group_histograms(
    rows: list[dict[str, Any]], output_dir: Path
) -> list[Path]:
    counts, groups = _selected_dataset_paper_counts(rows, unit="papers")
    groups = [
        (group_name, datasets)
        for group_name, datasets in _ordered_selected_dataset_groups(counts, groups)
        if datasets
    ]

    fig, axes = plt.subplots(2, 3, figsize=(9.8, 5.0), sharex=True, sharey=True)
    axes_flat = axes.flat
    for ax, (group_name, datasets) in zip(axes_flat, groups, strict=True):
        values = _selected_gap_closure_values(rows, datasets)
        ax.hist(
            values,
            bins=GAP_CLOSURE_BINS,
            weights=_histogram_percentage_weights(values),
            color=CATEGORY_COLORS["prior_better"],
            edgecolor="white",
            linewidth=0.6,
        )
        _style_gap_closure_axis(ax)
        ax.set_title(group_name, fontsize=9, fontweight="bold", color="#4f5965", pad=5)

    for ax in axes[0, :]:
        ax.tick_params(labelbottom=False)
    for ax in axes[:, 1:].flat:
        ax.tick_params(labelleft=False)
    fig.supxlabel("Share of gap to current SOTA closed at publication", y=0.04)
    fig.supylabel("Share of results", x=0.012)
    fig.subplots_adjust(left=0.08, right=0.99, bottom=0.15, top=0.91, wspace=0.18, hspace=0.34)
    return _save_figure(
        fig,
        output_dir,
        "figure_11_stale_baseline_gap_closure_selected_groups",
        tight=False,
    )


def _jittered_points(ax: Any, values: list[float], x: float, color: str, seed: int) -> None:
    if len(values) > 700:
        random_generator = random.Random(seed)
        values = random_generator.sample(values, 700)
    jitter = np.random.default_rng(seed).normal(0, 0.055, len(values))
    ax.scatter(values, np.full(len(values), x) + jitter, s=7, alpha=0.2, color=color, linewidths=0)


def plot_availability_lag(rows: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    values_by_group: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        if row["category"] != "prior_better" or row["prior_days_available"] is None:
            continue
        values_by_group[_benchmark_group_name(row)].append(row["prior_days_available"] / 365.25)
    values_by_group = {
        group: values for group, values in values_by_group.items() if len(values) >= 5
    }
    groups = sorted(values_by_group, key=lambda group: (-len(values_by_group[group]), group))
    fig_height = max(5.5, 0.32 * len(groups) + 1.8)
    fig, ax = plt.subplots(figsize=(8.0, fig_height))
    positions = np.arange(1, len(groups) + 1)
    box = ax.boxplot(
        [values_by_group[group] for group in groups],
        positions=positions,
        vert=False,
        patch_artist=True,
        showfliers=False,
        widths=0.58,
        medianprops={"color": "#242b33", "linewidth": 1.5},
    )
    for patch in box["boxes"]:
        patch.set_facecolor("#f1b4ba")
        patch.set_alpha(0.8)
    for index, group in enumerate(groups, start=1):
        _jittered_points(ax, values_by_group[group], index, "#a32839", index + 17)
        median = np.median(values_by_group[group]) if values_by_group[group] else float("nan")
        label = (
            f"n={len(values_by_group[group])}; median={median:.1f} y"
            if values_by_group[group]
            else "n=0"
        )
        ax.text(1.01, index, label, transform=ax.get_yaxis_transform(), va="center", fontsize=8)
    ax.set_yticks(positions, groups)
    ax.set_xlabel("Years since the prior best was published")
    ax.set_title(
        "Better results were often available well before stale baselines were reported",
        loc="left",
        fontsize=14,
        fontweight="bold",
    )
    ax.grid(axis="x", color="#dce1e6", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False)
    fig.text(
        0.1,
        0.01,
        "Lag is measured from the prior reference paper to the paper reusing the baseline. "
        "Benchmark groups with fewer than five stale entries are omitted.",
        fontsize=8.5,
        color="#4f5965",
    )
    fig.subplots_adjust(left=0.27, right=0.86, bottom=0.13, top=0.88)
    return _save_figure(fig, output_dir, "figure_5_stale_baseline_availability_lag_all_benchmarks")


def write_outputs(
    rows: list[dict[str, Any]], metadata: dict[str, Any], output_dir: Path
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary_data = summarize(rows)
    rows_path = output_dir / "stale_baselines.csv"
    with rows_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else [])
        writer.writeheader()
        writer.writerows(rows)
    summary_path = output_dir / "stale_baselines_summary.json"
    summary_path.write_text(
        json.dumps({"metadata": metadata, "summary": summary_data}, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    figure_paths = [
        *plot_benchmark_paper_counts(rows, output_dir),
        *plot_dataset_paper_counts(rows, output_dir),
        *plot_benchmark_entry_counts(rows, output_dir),
        *plot_dataset_entry_counts(rows, output_dir),
        *plot_selected_dataset_paper_counts(rows, output_dir),
        *plot_selected_dataset_result_counts(rows, output_dir),
        *plot_selected_dataset_paper_percentages(rows, output_dir),
        *plot_selected_dataset_result_percentages(rows, output_dir),
        *plot_selected_gap_closure_histogram(rows, output_dir),
        *plot_selected_gap_closure_group_histograms(rows, output_dir),
        *plot_availability_lag(rows, output_dir),
    ]
    return [rows_path, summary_path, *figure_paths]


def write_report(
    rows: list[dict[str, Any]], metadata: dict[str, Any], output_dir: Path, paths: list[Path]
) -> Path:
    summary_data = summarize(rows)
    overall = summary_data["overall"]
    lrgb = summary_data["lrgb"]
    lrgb_rows = sum(item["rows"] for item in lrgb.values())
    lrgb_prior = sum(item["prior_better"] for item in lrgb.values())
    lrgb_any = sum(item["prior_better"] + item["future_only"] for item in lrgb.values())
    lrgb_papers = summary_data["paper_level"]["lrgb"]
    all_papers = summary_data["paper_level"]["all"]

    def pct(value: int, total: int) -> str:
        return f"{100 * value / total:.1f}%" if total else "n/a"

    lines = [
        "# Stale-baselines exploratory analysis",
        "",
        f"Generated from `{metadata['db']}` on {metadata['generated_on']}.",
        "",
        "## Main result",
        "",
        f"Across {overall['rows']:,} comparable primary-metric baseline rows, "
        f"{overall['prior_better']:,} ({pct(overall['prior_better'], overall['rows'])}) "
        "were materially below a result from another paper already available by the "
        "paper's publication date. A further "
        f"{overall['future_only']:,} ({pct(overall['future_only'], overall['rows'])}) "
        "were only behind a later result.",
        "",
        f"At the paper level, {all_papers['papers_with_prior_better']:,}/{all_papers['papers']:,} "
        f"papers ({pct(all_papers['papers_with_prior_better'], all_papers['papers'])}) contained "
        "at least one stale baseline; red takes precedence over yellow when a paper has both types of gap.",
        "",
        f"For LRGB, {lrgb_prior:,}/{lrgb_rows:,} rows ({pct(lrgb_prior, lrgb_rows)}) "
        "were already behind a prior result, and "
        f"{lrgb_any:,}/{lrgb_rows:,} ({pct(lrgb_any, lrgb_rows)}) were behind either a prior or later best.",
        "",
        f"Conditioning on the {sum(item['prior_reference_rows'] for item in lrgb.values()):,} LRGB rows "
        "for which a prior reference existed, the already-available shortfall rate was "
        f"{pct(lrgb_prior, sum(item['prior_reference_rows'] for item in lrgb.values()))}; "
        "the corresponding rate outside LRGB, over all non-LRGB rows with a prior reference, was "
        f"{pct(summary_data['overall']['prior_better'] - lrgb_prior, summary_data['overall']['prior_reference_rows'] - sum(item['prior_reference_rows'] for item in lrgb.values()))}.",
        "",
        f"At the paper level, {lrgb_papers['papers_with_prior_better']}/{lrgb_papers['papers']} "
        f"LRGB papers ({pct(lrgb_papers['papers_with_prior_better'], lrgb_papers['papers'])}) "
        "contained at least one baseline already behind a prior result; "
        f"{lrgb_papers['papers_with_any_gap']}/{lrgb_papers['papers']} "
        f"({pct(lrgb_papers['papers_with_any_gap'], lrgb_papers['papers'])}) contained a gap to either a prior or later best.",
        "",
        "These are row-level descriptive statistics, not evidence that the baseline was deliberately copied. "
        "They quantify a reproducibility/benchmarking failure mode: a paper reports a materially inferior "
        "value for a named baseline despite a better value being available in the literature.",
        "",
        "## Recommended paper figures",
        "",
        "1. **Main figure — benchmark groups:** use `figure_1_stale_baselines_by_benchmark_papers`. It shows "
        "absolute paper counts, with LRGB included as one benchmark group alongside all other groups.",
        "2. **Dataset detail:** use `figure_2_stale_baselines_by_dataset_papers`. It shows individual datasets "
        "and omits datasets reported by fewer than five papers.",
        "3. **Entry-level benchmark groups:** use `figure_3_stale_baselines_by_benchmark_entries` to show how the "
        "picture changes when every baseline entry, rather than every paper, contributes one count.",
        "4. **Entry-level datasets:** use `figure_4_stale_baselines_by_dataset_entries` for the corresponding "
        "individual-dataset view, using the same five-paper minimum.",
        "5. **Selected dataset families:** use `figure_6_stale_baselines_selected_dataset_papers` to compare "
        "the requested citation, OGB, heterophilic, LRGB, and TU dataset blocks.",
        "6. **Selected result-level appendix:** use `figure_7_stale_baselines_selected_dataset_results` for "
        "the same dataset families while counting every comparable baseline result.",
        "7. **Selected paper percentages:** use `figure_8_stale_baselines_selected_dataset_paper_percentages` "
        "for the normalized paper-level comparison.",
        "8. **Selected result percentages:** use `figure_9_stale_baselines_selected_dataset_result_percentages` "
        "for the normalized result-level comparison.",
        "9. **Gap closure:** use `figure_10_stale_baseline_gap_closure_selected_results` for the pooled "
        "distribution and `figure_11_stale_baseline_gap_closure_selected_groups` for the grouped distributions.",
        "10. **Availability lag:** use `figure_5_stale_baseline_availability_lag_all_benchmarks` for the lag "
        "distribution across all benchmark groups. Groups with fewer than five stale entries are omitted.",
        "",
        "## Definition and caveats",
        "",
        "- Population: stored rows marked `is_baseline`, restricted to the dataset primary metric and the "
        "current leaderboard eligibility contract.",
        "- `prior_better`: the reported value is worse than the best result from another paper published on or "
        "before the evaluated paper, after accounting for both reported standard deviations when present.",
        "- Gap closure is the fraction of the reported-result-to-dataset-SOTA gap covered by the better "
        "baseline result available at publication. The gap-closure histograms include only `prior_better` "
        "results; future-only results have no publication-time reference and are excluded.",
        "- The evaluated paper is explicitly excluded from the prior reference. This is stricter than the "
        "existing page-of-shame display and avoids self-comparison artifacts.",
        "- Model names are compared after the repository's canonicalization and implementation-marker cleanup. "
        "Extraction errors, model mismatches, and protocol differences can still affect the estimate.",
        "- Rows are not independent: one paper can contribute many baselines. The paper-level plot handles this "
        "for its primary count; report both units in the paper and consider a cluster bootstrap for uncertainty.",
        "",
        "## Output files",
        "",
    ]
    lines.extend(f"- `{path.name}`" for path in paths)
    report_path = output_dir / "stale_baselines_analysis.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def run(db_path: Path, output_dir: Path) -> list[Path]:
    rows, metadata = load_analysis_rows(db_path)
    paths = write_outputs(rows, metadata, output_dir)
    report_path = write_report(rows, metadata, output_dir, paths)
    return [*paths, report_path]
