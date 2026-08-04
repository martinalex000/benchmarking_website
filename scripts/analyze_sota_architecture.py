"""Analyze historical SOTA ownership by model architecture type."""

from __future__ import annotations

import argparse
import logging
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from pdfCropMargins import pdfCropMargins

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))

from backend.config import cfg  # noqa: E402
from backend.db import init_db, session_scope  # noqa: E402
from backend.sota_architecture_analysis import (  # noqa: E402
    OwnershipSnapshot,
    analyze_snapshots,
    compare_override_effects,
    historical_cutoffs,
    load_analysis_rows,
    monthly_cutoffs,
)

logger = logging.getLogger(__name__)
PLOT_START_YEAR = 2017
PAPER_FONTS = {
    "tick": 13,
    "label": 15,
    "title": 18,
    "legend": 12,
}
PLOT_CATEGORY_ORDER = (
    "MPGNN",
    "Graph Transformer",
    "LLM",
    "Walk",
    "Traditional",
    "Unknown",
)
PLOT_CATEGORY_MAP = {
    "gnn": "MPGNN",
    "transformer_involving": "Graph Transformer",
    "llm": "LLM",
    "walk": "Walk",
    "unknown": "Unknown",
    "svm_kernel": "Traditional",
    "random_forest": "Traditional",
    "decision_tree": "Traditional",
    "boosting": "Traditional",
    "other_traditional": "Traditional",
}


def _fmt_share(value: float | None) -> str:
    return "—" if value is None else f"{value * 100:.1f}%"


def _style_axes(ax: plt.Axes, *, title: bool = False) -> None:
    ax.tick_params(axis="both", labelsize=PAPER_FONTS["tick"])
    ax.xaxis.label.set_size(PAPER_FONTS["label"])
    ax.yaxis.label.set_size(PAPER_FONTS["label"])
    if title:
        ax.title.set_size(PAPER_FONTS["title"])


def _style_date_axis(ax: plt.Axes, plot_end: date) -> None:
    ax.set_xlim(date(PLOT_START_YEAR, 1, 1), plot_end)
    ax.xaxis.set_major_locator(mdates.YearLocator(month=1, day=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))


def _display_category_weights(snapshot: OwnershipSnapshot) -> dict[str, float]:
    """Aggregate internal architecture categories into paper-facing labels."""
    weights = dict.fromkeys(PLOT_CATEGORY_ORDER, 0.0)
    for category, weight in snapshot.category_weights.items():
        weights[PLOT_CATEGORY_MAP.get(category, "Unknown")] += weight
    return weights


def _postprocess_output(raw_path: Path, final_path: Path, tool: str, args: list[str]) -> None:
    """Crop one output with an external tool, falling back to the raw output."""
    if shutil.which(tool) is None:
        logger.warning("%s is unavailable; keeping uncropped %s", tool, final_path.name)
        shutil.copyfile(raw_path, final_path)
        return
    try:
        subprocess.run([tool, *args], check=True, capture_output=True, text=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        logger.warning("%s failed for %s; keeping uncropped output: %s", tool, final_path.name, exc)
        shutil.copyfile(raw_path, final_path)


def _crop_pdf(raw_path: Path, final_path: Path) -> None:
    """Crop a generated PDF in-process, retaining none of its detected margins."""
    try:
        _, exit_code, _, stderr = pdfCropMargins.crop(
            ["-p", "0", str(raw_path), "-o", str(final_path)],
            quiet=True,
        )
        if exit_code not in (None, 0) or not final_path.is_file():
            detail = stderr.strip() if stderr else f"exit code {exit_code}"
            raise RuntimeError(detail)
    except Exception as exc:
        logger.warning(
            "pdfCropMargins failed for %s; keeping uncropped output: %s", final_path.name, exc
        )
        shutil.copyfile(raw_path, final_path)


def _save_cropped_figure(fig: plt.Figure, output_dir: Path, filename_stem: str) -> Path:
    """Save PNG/PDF outputs, cropping their margins as part of figure generation."""
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_png = output_dir / f".{filename_stem}.raw.png"
    raw_pdf = output_dir / f".{filename_stem}.raw.pdf"
    png_path = output_dir / f"{filename_stem}.png"
    pdf_path = output_dir / f"{filename_stem}.pdf"
    try:
        fig.savefig(raw_png, dpi=220, bbox_inches="tight")
        fig.savefig(raw_pdf, bbox_inches="tight")
        _postprocess_output(
            raw_png,
            png_path,
            "convert",
            [str(raw_png), "-trim", "+repage", str(png_path)],
        )
        _crop_pdf(raw_pdf, pdf_path)
    finally:
        raw_png.unlink(missing_ok=True)
        raw_pdf.unlink(missing_ok=True)
    return png_path


def _write_figure(snapshots: list[OwnershipSnapshot], output_dir: Path) -> Path:
    snapshots = [
        snapshot for snapshot in snapshots if snapshot.cutoff >= date(PLOT_START_YEAR, 1, 1)
    ]
    if not snapshots:
        raise ValueError(f"No ownership snapshots available from {PLOT_START_YEAR} onward")
    categories = [
        category
        for category in PLOT_CATEGORY_ORDER
        if any(_display_category_weights(snapshot)[category] for snapshot in snapshots)
    ]
    if not categories:
        raise ValueError("No categorized ownership snapshots available")
    dates = [snapshot.cutoff for snapshot in snapshots]
    plot_end = dates[-1]
    ownership = [
        [_display_category_weights(snapshot)[category] for snapshot in snapshots]
        for category in categories
    ]

    fig, (ax_share, ax_transformer) = plt.subplots(
        2, 1, figsize=(11, 5.5), sharex=True, gridspec_kw={"height_ratios": [2, 1]}
    )
    colors = plt.get_cmap("tab10").colors
    ax_share.stackplot(
        dates, ownership, labels=categories, colors=colors[: len(categories)], alpha=0.9
    )
    ax_share.set_ylim(bottom=0)
    _style_date_axis(ax_share, plot_end)
    ax_share.set_ylabel("#Datasets")
    ax_share.legend(loc="upper left", ncol=3, fontsize=PAPER_FONTS["legend"])
    transformer = [snapshot.shares.get("transformer_involving", 0.0) for snapshot in snapshots]
    ax_transformer.plot(dates, transformer, color="#d62728", linewidth=2.5)
    ax_transformer.fill_between(dates, transformer, color="#d62728", alpha=0.18)
    ax_transformer.set_ylim(0, 1)
    _style_date_axis(ax_transformer, plot_end)
    ax_transformer.set_ylabel("Transformer share")
    ax_transformer.grid(axis="y", alpha=0.25)
    _style_axes(ax_share)
    _style_axes(ax_transformer)
    fig.tight_layout()
    output_path = _save_cropped_figure(fig, output_dir, "architecture_ownership_over_time")
    plt.close(fig)
    return output_path


def _write_task_level_figure(
    snapshots_by_level: dict[str, list[OwnershipSnapshot]],
    output_dir: Path,
    *,
    filename_stem: str = "architecture_ownership_by_task_level",
) -> Path:
    """Write count-based ownership stacks for node- and graph-level tasks."""
    categories = [
        category
        for category in PLOT_CATEGORY_ORDER
        if any(
            _display_category_weights(snapshot)[category]
            for snapshots in snapshots_by_level.values()
            for snapshot in snapshots
        )
    ]
    if not categories:
        raise ValueError("No categorized task-level snapshots available")

    fig, axes = plt.subplots(1, 2, figsize=(15, 4.5), sharey=True)
    colors = plt.get_cmap("tab10").colors
    plot_end = max(
        snapshot.cutoff
        for snapshots in snapshots_by_level.values()
        for snapshot in snapshots
        if snapshot.cutoff >= date(PLOT_START_YEAR, 1, 1)
    )
    for ax, level in zip(axes, ("node", "graph"), strict=True):
        snapshots = [
            snapshot
            for snapshot in snapshots_by_level[level]
            if snapshot.cutoff >= date(PLOT_START_YEAR, 1, 1)
        ]
        if not snapshots:
            ax.set_visible(False)
            continue
        dates = [snapshot.cutoff for snapshot in snapshots]
        ownership = [
            [_display_category_weights(snapshot)[category] for snapshot in snapshots]
            for category in categories
        ]
        ax.stackplot(
            dates, ownership, labels=categories, colors=colors[: len(categories)], alpha=0.9
        )
        ax.set_ylim(bottom=0)
        _style_date_axis(ax, plot_end)
        if level == "node":
            ax.set_ylabel("#Datasets")
        ax.set_title(f"{level.title()}-level tasks")
        ax.grid(axis="y", alpha=0.25)
        _style_axes(ax, title=True)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="center left",
        bbox_to_anchor=(0.84, 0.5),
        fontsize=PAPER_FONTS["legend"],
        frameon=True,
    )
    fig.subplots_adjust(left=0.07, right=0.82, bottom=0.18, top=0.88, wspace=0.08)
    output_path = _save_cropped_figure(fig, output_dir, filename_stem)
    plt.close(fig)
    return output_path


def _ownership_table(snapshot: OwnershipSnapshot) -> list[str]:
    lines = [
        "| Dataset | Papers | Weight | Winner model(s) | Winner type(s) | Papers |",
        "|---|---:|---:|---|---|---|",
    ]

    def compact(values: tuple[str, ...], limit: int = 8) -> str:
        if len(values) <= limit:
            return ", ".join(values)
        return ", ".join(values[:limit]) + f", (+{len(values) - limit} more)"

    for item in snapshot.ownership:
        lines.append(
            f"| {item.dataset} | {item.paper_count} | {item.weight:.3f} | "
            f"{compact(item.winner_models)} | {compact(item.winner_types)} | "
            f"{compact(item.winner_arxiv_ids)} |"
        )
    return lines


def _write_report(
    output_dir: Path,
    *,
    after: list[OwnershipSnapshot],
    audit,
    min_papers: int,
    weight: str,
) -> Path:
    current = after[-1] if after else None
    lines = [
        "# Historical SOTA architecture ownership",
        "",
        "Generated from the canonical benchmark database using standard variants, "
        "primary metrics, protocol-eligible rows, and non-problematic results.",
        "",
        "This is an ownership statistic, not a causal estimate of which architecture "
        "drove improvement. Transformer-involving combines `graph_transformer` and `hybrid`.",
        "",
        "## Current snapshot",
        "",
        f"- Minimum papers per dataset: **{min_papers}**",
        f"- Dataset weight: **{weight}**",
        f"- Datasets meeting threshold: **{len(current.ownership) if current else 0}**",
        "- Shares are normalized over datasets meeting the threshold; unresolved winners are "
        "shown as `unknown`.",
        "",
        "| Architecture category | Weighted share |",
        "|---|---:|",
    ]
    if current:
        for category, share in sorted(current.shares.items(), key=lambda item: -item[1]):
            lines.append(f"| `{category}` | {_fmt_share(share)} |")
    lines.extend(
        [
            "",
            "## Override and metadata audit",
            "",
            f"- Winner states with missing architecture metadata before overrides: **{audit.unknown_winner_states_before}**",
            f"- Winner states classified after local-paper review: **{audit.classified_from_unknown_states}**",
            f"- Current dataset winners changed: **{audit.changed_current_datasets}**",
            f"- Historical dataset/cutoff states changed: **{audit.changed_cutoff_states}**",
            f"- Problematic result rows removed by overrides: **{audit.problematic_rows_removed}**",
            f"- Transformer-involving share before corrections: **{_fmt_share(audit.transformer_share_before)}**",
            f"- Transformer-involving share after corrections: **{_fmt_share(audit.transformer_share_after)}**",
            "",
            "## Historical snapshots",
            "",
            "| Cutoff | Datasets | Total weight | Transformer-involving | GNN |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for snapshot in after:
        lines.append(
            f"| {snapshot.cutoff.isoformat()} | {len(snapshot.ownership)} | "
            f"{snapshot.total_weight:.3f} | "
            f"{_fmt_share(snapshot.shares.get('transformer_involving'))} | "
            f"{_fmt_share(snapshot.shares.get('gnn'))} |"
        )
    if current:
        lines.extend(["", "## Current dataset detail", "", *_ownership_table(current)])
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def run_analysis(
    *,
    output_dir: Path,
    min_papers: int = 5,
    weight: str = "uniform",
    papers_root: Path | None = None,
) -> tuple[Path, Path, Path, Path]:
    """Run the analysis and return report and figure paths."""
    init_db()
    with session_scope() as session:
        before_rows = load_analysis_rows(session, papers_root=papers_root, apply_overrides=False)
        after_rows = load_analysis_rows(session, papers_root=papers_root, apply_overrides=True)
    annual_cutoffs = historical_cutoffs(after_rows)
    monthly_plot_cutoffs = monthly_cutoffs(after_rows)
    report_after = analyze_snapshots(
        after_rows, cutoffs=annual_cutoffs, min_papers=min_papers, weight=weight
    )
    plot_after = analyze_snapshots(
        after_rows, cutoffs=monthly_plot_cutoffs, min_papers=min_papers, weight=weight
    )
    task_snapshots = {
        level: analyze_snapshots(
            after_rows,
            cutoffs=monthly_plot_cutoffs,
            min_papers=min_papers,
            weight=weight,
            task_level=level,
        )
        for level in ("node", "graph")
    }
    single_winner_task_snapshots = {
        level: analyze_snapshots(
            after_rows,
            cutoffs=monthly_plot_cutoffs,
            min_papers=min_papers,
            weight=weight,
            task_level=level,
            winner_policy="single_mean",
        )
        for level in ("node", "graph")
    }
    audit = compare_override_effects(before_rows, after_rows, min_papers=min_papers, weight=weight)
    report_path = _write_report(
        output_dir,
        after=report_after,
        audit=audit,
        min_papers=min_papers,
        weight=weight,
    )
    figure_path = _write_figure(plot_after, output_dir)
    task_level_figure_path = _write_task_level_figure(task_snapshots, output_dir)
    single_winner_figure_path = _write_task_level_figure(
        single_winner_task_snapshots,
        output_dir,
        filename_stem="architecture_ownership_by_task_level_single_winner",
    )
    return report_path, figure_path, task_level_figure_path, single_winner_figure_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=cfg.project_root / "experiments" / "sota_architecture_ownership",
    )
    parser.add_argument("--min-papers", type=int, default=5)
    parser.add_argument("--weight", choices=("sqrt", "uniform"), default="uniform")
    parser.add_argument("--papers-root", type=Path, default=None)
    args = parser.parse_args()
    if args.min_papers < 1:
        parser.error("--min-papers must be positive")
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    report, figure, task_level_figure, single_winner_figure = run_analysis(
        output_dir=args.output_dir,
        min_papers=args.min_papers,
        weight=args.weight,
        papers_root=args.papers_root,
    )
    print(f"Report: {report}")
    print(f"Figure: {figure}")
    print(f"Task-level figure: {task_level_figure}")
    print(f"Single-winner task-level figure: {single_winner_figure}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
