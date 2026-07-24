"""Compare current LRGB results with a historical SQLite snapshot.

This command is intentionally read-only. It produces a compact Markdown audit
that can be reviewed before any recovery merge is attempted.

Example::

    uv run python scripts/audit_lrgb_regression.py \
      --historical-db /tmp/lrgb-old.db \
      --output LRGB_REGRESSION_AUDIT.md
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


def _connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def _dataset_counts(connection: sqlite3.Connection) -> dict[str, int]:
    rows = connection.execute(
        """
        SELECT d.name, COUNT(*) AS count
        FROM results r
        JOIN dataset_variants v ON v.id = r.dataset_variant_id
        JOIN datasets d ON d.id = v.dataset_id
        JOIN benchmarks b ON b.id = d.benchmark_id
        WHERE lower(b.short_name) = 'lrgb'
        GROUP BY d.name
        ORDER BY d.name
        """
    )
    return {row["name"]: row["count"] for row in rows}


def _paper_counts(connection: sqlite3.Connection) -> dict[str, int]:
    rows = connection.execute(
        """
        SELECT p.arxiv_id, COUNT(*) AS count
        FROM papers p
        JOIN results r ON r.paper_id = p.id
        JOIN dataset_variants v ON v.id = r.dataset_variant_id
        JOIN datasets d ON d.id = v.dataset_id
        JOIN benchmarks b ON b.id = d.benchmark_id
        WHERE lower(b.short_name) = 'lrgb'
        GROUP BY p.arxiv_id
        """
    )
    return {row["arxiv_id"]: row["count"] for row in rows}


def _all_paper_counts(connection: sqlite3.Connection) -> dict[str, int]:
    rows = connection.execute(
        """
        SELECT p.arxiv_id, COUNT(*) AS count
        FROM papers p
        JOIN results r ON r.paper_id = p.id
        WHERE p.arxiv_id IS NOT NULL
        GROUP BY p.arxiv_id
        """
    )
    return {row["arxiv_id"]: row["count"] for row in rows}


def build_report(current_db: Path, historical_db: Path) -> str:
    current = _connect(current_db)
    historical = _connect(historical_db)
    try:
        current_datasets = _dataset_counts(current)
        historical_datasets = _dataset_counts(historical)
        current_papers = _paper_counts(current)
        historical_papers = _paper_counts(historical)
        current_all_papers = _all_paper_counts(current)
        historical_all_papers = _all_paper_counts(historical)
    finally:
        current.close()
        historical.close()

    dataset_names = sorted(set(current_datasets) | set(historical_datasets))
    historical_total = sum(historical_datasets.values())
    current_total = sum(current_datasets.values())
    historical_all_ids = set(historical_all_papers)
    current_all_ids = set(current_all_papers)
    reduced_all = [
        paper_id
        for paper_id in historical_all_ids & current_all_ids
        if current_all_papers[paper_id] < historical_all_papers[paper_id]
    ]
    zero_all = [paper_id for paper_id in historical_all_ids if paper_id not in current_all_ids]
    more_than_ten_percent = [
        paper_id
        for paper_id in reduced_all
        if current_all_papers[paper_id] / historical_all_papers[paper_id] < 0.9
    ]
    fewer_all = len(zero_all) + len(reduced_all)
    more_than_ten_percent_all = len(zero_all) + len(more_than_ten_percent)
    lines = [
        "# LRGB Regression Audit",
        "",
        f"Historical database: `{historical_db}`  ",
        f"Current database: `{current_db}`",
        "",
        "This report was generated without modifying either database.",
        "",
        "## Summary",
        "",
        "| Measure | Historical | Current | Difference |",
        "|---|---:|---:|---:|",
        f"| LRGB result rows | {historical_total} | {current_total} | {current_total - historical_total:+d} |",
        f"| Papers with LRGB rows | {len(historical_papers)} | {len(current_papers)} | {len(current_papers) - len(historical_papers):+d} |",
        "",
        "## All-benchmark paper-level coverage",
        "",
        "These counts compare papers by arXiv ID across the complete result table, not just LRGB.",
        "",
        "| Measure | Count |",
        "|---|---:|",
        f"| Historical papers with results | {len(historical_all_papers)} |",
        f"| Historical-result papers with zero current rows | {len(zero_all)} |",
        f"| Historical-result papers with fewer current rows | {fewer_all} |",
        f"| Historical-result papers down by more than 10% | {more_than_ten_percent_all} |",
        "",
        "## Dataset comparison",
        "",
        "| Dataset | Historical | Current | Difference | Retention |",
        "|---|---:|---:|---:|---:|",
    ]
    for name in dataset_names:
        old = historical_datasets.get(name, 0)
        new = current_datasets.get(name, 0)
        retention = f"{100 * new / old:.1f}%" if old else "n/a"
        lines.append(f"| {name} | {old} | {new} | {new - old:+d} | {retention} |")

    lost_papers = sorted(set(historical_papers) - set(current_papers))
    reduced_papers = sorted(
        (paper_id for paper_id in set(historical_papers) & set(current_papers)),
        key=lambda paper_id: (current_papers[paper_id] - historical_papers[paper_id], paper_id),
    )
    lines.extend(
        [
            "",
            "## Papers with no surviving LRGB rows",
            "",
            f"{len(lost_papers)} historical LRGB papers have no current LRGB rows.",
            "",
            ", ".join(f"`{paper_id}`" for paper_id in lost_papers) or "None.",
            "",
            "## Largest paper-level reductions",
            "",
            "| arXiv ID | Historical | Current | Difference |",
            "|---|---:|---:|---:|",
        ]
    )
    for paper_id in reduced_papers[:30]:
        old = historical_papers[paper_id]
        new = current_papers[paper_id]
        lines.append(f"| `{paper_id}` | {old} | {new} | {new - old:+d} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--historical-db", type=Path, required=True)
    parser.add_argument("--current-db", type=Path, default=Path("data/benchmarks.db"))
    parser.add_argument("--output", type=Path, default=Path("LRGB_REGRESSION_AUDIT.md"))
    args = parser.parse_args()
    args.output.write_text(build_report(args.current_db, args.historical_db), encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
