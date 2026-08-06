#!/usr/bin/env python3
"""Rank papers with unusual per-dataset distributions of reported result means."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rich.console import Console
from rich.table import Table

from backend.paper_task_anomaly import run, write_csv_report, write_json_report


def _print_summary(report: dict, *, limit: int) -> None:
    console = Console()
    counts = report["counts"]
    console.print(
        f"Scored {counts['observations_scored']:,} paper/dataset/metric observations; "
        f"flagged {counts['suspicious_papers']:,} papers "
        f"({counts['clustering_candidates']:,} observations have a clustering signal)."
    )
    table = Table(title="Suspicious task evaluations", show_header=True)
    table.add_column("Score", justify="right")
    table.add_column("arXiv", style="cyan")
    table.add_column("Dataset / metric")
    table.add_column("Reasons")
    table.add_column("Title")
    papers = report["papers"] if limit == 0 else report["papers"][:limit]
    for paper in papers:
        top = paper["observations"][0]
        table.add_row(
            f"{paper['score']:.2f}",
            paper["arxiv_id"] or "—",
            f"{top['dataset']} / {top['metric']}",
            ", ".join(top["reasons"]),
            paper["title"][:60],
        )
    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=Path("data/benchmarks.db"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/suspicious_task_papers.json"),
        help="JSON report path",
    )
    parser.add_argument("--csv", type=Path, help="Optional flattened CSV report path")
    parser.add_argument("--min-results", type=int, default=3)
    parser.add_argument("--min-cohort-size", type=int, default=8)
    parser.add_argument("--min-cluster-size", type=int, default=5)
    parser.add_argument("--robust-threshold", type=float, default=4.5)
    parser.add_argument("--include-problematic", action="store_true")
    parser.add_argument(
        "--reviewed",
        type=Path,
        help="Reviewed-observation manifest (default: config/anomaly_reviewed.yaml)",
    )
    parser.add_argument(
        "--include-cluster-only",
        action="store_true",
        help="Also flag HDBSCAN noise/minority-cluster papers without a statistical signal",
    )
    parser.add_argument("--limit", type=int, default=50, help="Rows printed; 0 prints all")
    args = parser.parse_args()

    if args.min_results < 2:
        parser.error("--min-results must be at least 2 so a spread can be estimated")
    if args.min_cohort_size < 3:
        parser.error("--min-cohort-size must be at least 3")
    if args.min_cluster_size < 2:
        parser.error("--min-cluster-size must be at least 2")
    if args.robust_threshold <= 0:
        parser.error("--robust-threshold must be positive")

    report = run(
        args.db,
        min_results=args.min_results,
        min_cohort_size=args.min_cohort_size,
        min_cluster_size=args.min_cluster_size,
        robust_threshold=args.robust_threshold,
        include_problematic=args.include_problematic,
        include_cluster_only=args.include_cluster_only,
        reviewed_path=args.reviewed,
    )
    write_json_report(args.output, report)
    if args.csv:
        write_csv_report(args.csv, report)
    _print_summary(report, limit=args.limit)
    print(args.output)
    if args.csv:
        print(args.csv)


if __name__ == "__main__":
    main()
