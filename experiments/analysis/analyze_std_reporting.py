#!/usr/bin/env python3
"""Plot the quarterly share of papers reporting a nonzero standard deviation."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update(
    {
        "font.size": 16,
        "axes.labelsize": 17,
        "xtick.labelsize": 15,
        "ytick.labelsize": 15,
        "legend.fontsize": 15,
    }
)

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from backend.std_reporting_analysis import (  # noqa: E402
    load_paper_observations,
    load_paper_result_observations,
    summarize_quarterly,
    summarize_yearly,
    summarize_yearly_by_std_fraction,
    write_csv,
    write_report,
)


def crop_pdf(output_path: Path) -> None:
    """Crop whitespace from a generated PDF in place using pdfcrop."""
    fd, cropped_path = tempfile.mkstemp(
        prefix=f".{output_path.stem}-cropped-",
        suffix=".pdf",
        dir=output_path.parent,
    )
    os.close(fd)
    Path(cropped_path).unlink()
    try:
        subprocess.run(
            ["pdfcrop", "--quiet", str(output_path), cropped_path],
            check=True,
        )
        os.replace(cropped_path, output_path)
    finally:
        Path(cropped_path).unlink(missing_ok=True)


def write_figure(summaries, output_path: Path) -> None:
    """Write count and reporting-rate panels for the quarterly series."""
    if not summaries:
        raise ValueError("No result-bearing papers with parseable publication dates were found")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    labels = [summary.quarter for summary in summaries]
    counts = [summary.papers_with_std for summary in summaries]
    rates = [summary.reporting_rate * 100 for summary in summaries]

    fig, (count_ax, rate_ax) = plt.subplots(2, 1, figsize=(12, 7), sharex=True)
    count_ax.bar(labels, counts, color="#4472c4")
    count_ax.set_ylabel("Papers reporting std")
    count_ax.grid(axis="y", alpha=0.25)
    rate_ax.plot(labels, rates, color="#d62728", marker="o", linewidth=2)
    rate_ax.set_ylabel("Reporting rate (%)")
    rate_ax.set_ylim(0, 100)
    rate_ax.grid(axis="y", alpha=0.25)
    rate_ax.set_xlabel("Publication quarter")
    tick_step = max(1, len(labels) // 16)
    rate_ax.set_xticks(
        range(0, len(labels), tick_step), labels[::tick_step], rotation=45, ha="right"
    )
    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    if output_path.suffix.lower() == ".pdf":
        crop_pdf(output_path)


def write_yearly_percentage_figure(summaries, output_path: Path, *, start_year: int = 2017) -> None:
    """Write a percentage-only annual plot from *start_year* onward."""
    summaries = [summary for summary in summaries if summary.year >= start_year]
    if not summaries:
        raise ValueError(f"No yearly summaries available from {start_year} onward")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    years = [summary.year for summary in summaries]
    rates = [summary.reporting_rate * 100 for summary in summaries]
    paper_counts = [summary.total_papers for summary in summaries]

    fig, ax = plt.subplots(figsize=(10, 4.8))
    count_ax = ax.twinx()
    count_ax.bar(
        years,
        paper_counts,
        width=0.7,
        color="#4472c4",
        alpha=0.35,
        label="Papers with results",
        zorder=1,
    )
    ax.patch.set_visible(False)
    ax.plot(
        years,
        rates,
        color="#d62728",
        marker="o",
        linewidth=2.5,
        label="Reporting rate",
        zorder=3,
    )
    ax.set_xlabel("Publication year")
    ax.set_ylabel("Reporting rate (%)")
    ax.set_ylim(0, 100)
    ax.set_xticks(years)
    ax.grid(axis="y", alpha=0.25)
    count_ax.set_ylabel("Papers with results")
    count_ax.set_ylim(0, max(paper_counts) * 1.2)
    ax.legend(loc="upper left")
    count_ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    if output_path.suffix.lower() == ".pdf":
        crop_pdf(output_path)


def write_threshold_yearly_percentage_figure(
    summaries, output_path: Path, *, start_year: int = 2017
) -> None:
    """Write the annual plot for papers with >30% std-bearing results."""
    summaries = [summary for summary in summaries if summary.year >= start_year]
    if not summaries:
        raise ValueError(f"No yearly summaries available from {start_year} onward")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    years = [summary.year for summary in summaries]
    rates = [summary.reporting_rate * 100 for summary in summaries]
    paper_counts = [summary.total_papers for summary in summaries]

    fig, ax = plt.subplots(figsize=(10, 4.8))
    count_ax = ax.twinx()
    count_ax.bar(
        years,
        paper_counts,
        width=0.7,
        color="#4472c4",
        alpha=0.35,
        label="Papers with results",
        zorder=1,
    )
    ax.patch.set_visible(False)
    ax.plot(
        years,
        rates,
        color="#d62728",
        marker="o",
        linewidth=2.5,
        label="Papers with >30% std-bearing results",
        zorder=3,
    )
    ax.set_xlabel("Publication year")
    ax.set_ylabel("Papers reporting stds (%)")
    ax.set_ylim(0, 100)
    ax.set_xticks(years)
    ax.grid(axis="y", alpha=0.25)
    count_ax.set_ylabel("Papers with results")
    count_ax.set_ylim(0, max(paper_counts) * 1.2)
    ax.legend(loc="upper left")
    count_ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    if output_path.suffix.lower() == ".pdf":
        crop_pdf(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=Path("data/benchmarks.db"))
    parser.add_argument(
        "--output-dir", type=Path, default=Path("experiments/std_reporting_over_time")
    )
    args = parser.parse_args()

    observations = load_paper_observations(args.db)
    summaries = summarize_quarterly(observations)
    yearly_summaries = summarize_yearly(observations)
    threshold_yearly_summaries = summarize_yearly_by_std_fraction(
        load_paper_result_observations(args.db)
    )
    write_csv(summaries, args.output_dir / "std_reporting_over_time.csv")
    write_report(summaries, args.output_dir / "report.md")
    write_figure(summaries, args.output_dir / "std_reporting_over_time.pdf")
    write_yearly_percentage_figure(
        yearly_summaries,
        args.output_dir / "std_reporting_yearly_percentage_from_2017.pdf",
    )
    write_threshold_yearly_percentage_figure(
        threshold_yearly_summaries,
        args.output_dir / "std_reporting_yearly_percentage_gt30_from_2017.pdf",
    )

    conference_dir = args.output_dir / "conference_only"
    conference_observations = load_paper_observations(args.db, conference_only=True)
    conference_summaries = summarize_quarterly(conference_observations)
    conference_yearly_summaries = summarize_yearly(conference_observations)
    conference_threshold_summaries = summarize_yearly_by_std_fraction(
        load_paper_result_observations(args.db, conference_only=True)
    )
    write_csv(conference_summaries, conference_dir / "std_reporting_over_time.csv")
    write_report(conference_summaries, conference_dir / "report.md")
    write_figure(conference_summaries, conference_dir / "std_reporting_over_time.pdf")
    write_yearly_percentage_figure(
        conference_yearly_summaries,
        conference_dir / "std_reporting_yearly_percentage_from_2017.pdf",
    )
    write_threshold_yearly_percentage_figure(
        conference_threshold_summaries,
        conference_dir / "std_reporting_yearly_percentage_gt30_from_2017.pdf",
    )
    for summary in summaries:
        print(
            f"{summary.quarter}: {summary.papers_with_std}/{summary.total_papers} "
            f"({summary.reporting_rate:.1%})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
