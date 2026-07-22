"""Create a re-evaluation list for papers that lost historical result rows."""

from __future__ import annotations

import argparse
import sqlite3
from datetime import UTC, datetime
from pathlib import Path


def _counts(path: Path) -> dict[str, int]:
    with sqlite3.connect(path) as connection:
        rows = connection.execute(
            """
            SELECT p.arxiv_id, COUNT(*)
            FROM papers p JOIN results r ON r.paper_id = p.id
            WHERE p.arxiv_id IS NOT NULL
            GROUP BY p.arxiv_id
            """
        )
        return {str(arxiv_id): int(count) for arxiv_id, count in rows}


def write_list(historical_db: Path, current_db: Path, output: Path) -> int:
    historical = _counts(historical_db)
    current = _counts(current_db)
    lost = sorted(
        arxiv_id for arxiv_id, count in historical.items() if current.get(arxiv_id, 0) < count
    )
    zero = sum(current.get(arxiv_id, 0) == 0 for arxiv_id in lost)
    generated_at = datetime.now(UTC).isoformat()
    lines = [
        "# Historical-result papers with fewer current rows, for full re-evaluation.",
        "# Includes zero-result and partially reduced papers; one arXiv ID per line.",
        f"# Historical DB: {historical_db}",
        f"# Current DB: {current_db}",
        f"# Cohort: {len(lost)} papers ({zero} with zero current rows)",
        f"# Generated at: {generated_at}",
        "# Mark with:",
        "#   UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/mark_reextract_papers.py "
        "mark-list --file config/re_evaluate_historical_losses.txt --yes --requeue "
        "--reason historical_result_loss",
        "",
        *lost,
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    return len(lost)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--historical-db", type=Path, required=True)
    parser.add_argument("--current-db", type=Path, default=Path("data/benchmarks.db"))
    parser.add_argument(
        "--output", type=Path, default=Path("config/re_evaluate_historical_losses.txt")
    )
    args = parser.parse_args()
    count = write_list(args.historical_db, args.current_db, args.output)
    print(f"Wrote {count} paper ID(s) to {args.output}")


if __name__ == "__main__":
    main()
