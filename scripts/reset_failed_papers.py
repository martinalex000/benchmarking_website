#!/usr/bin/env python3
"""Reset failed paper and todo-queue records back to pending.

Usage::

    UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/reset_failed_papers.py
    UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/reset_failed_papers.py --dry-run
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.db import init_db, session_scope
from backend.models import Paper, TodoPaper, TodoPaperStatus


def reset_failed_papers(*, dry_run: bool = False) -> int:
    """Reset failed extraction records and failed todo-queue records.

    Failed pipeline-run history remains intact so the database keeps its audit
    trail. Return the total number of changed records across both tables.
    """
    init_db()
    with session_scope() as session:
        papers = (
            session.query(Paper)
            .filter(Paper.extraction_status == "failed")
            .order_by(Paper.arxiv_id)
            .all()
        )
        todo_papers = (
            session.query(TodoPaper)
            .filter(TodoPaper.status == TodoPaperStatus.FAILED.value)
            .order_by(TodoPaper.arxiv_id)
            .all()
        )
        if not dry_run:
            for paper in papers:
                paper.extraction_status = "pending"
            for todo_paper in todo_papers:
                todo_paper.status = TodoPaperStatus.PENDING.value
                todo_paper.attempts = 0

    action = "Would reset" if dry_run else "Reset"
    print(
        f"{action} {len(papers)} failed extraction record(s) and "
        f"{len(todo_papers)} failed todo row(s) to pending."
    )
    return len(papers) + len(todo_papers)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report failed papers without changing the database",
    )
    args = parser.parse_args(argv)
    reset_failed_papers(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
