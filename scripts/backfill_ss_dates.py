"""Backfill exact publication dates from Semantic Scholar for papers that only have monthly granularity.

Usage::
    uv run python scripts/backfill_ss_dates.py --limit 1000 --sleep 0.3
    uv run python scripts/backfill_ss_dates.py --dry-run --limit 50
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

# Ensure project root is on PYTHONPATH so ``backend`` imports work when the
# script is executed directly.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.db import init_db, session_scope  # noqa: E402
from backend.llm_extractor import fetch_semantic_scholar_published_date  # noqa: E402
from backend.models import Paper  # noqa: E402

logger = logging.getLogger(__name__)


def needs_refill(date_str: str | None) -> bool:
    """Return True when the date is missing or lacks a day component."""
    if not date_str:
        return True
    stripped = date_str.strip()
    return len(stripped) < 10  # anything shorter than YYYY-MM-DD


def backfill(dry_run: bool = False, limit: int = 0, sleep: float = 0.25) -> None:
    init_db()
    updated = 0
    skipped = 0
    failed = 0

    with session_scope() as session:
        papers = session.query(Paper).all()
        to_refill = [p for p in papers if needs_refill(p.published_date)]

    logger.info(
        "Found %d paper(s) needing date refinement out of %d total",
        len(to_refill),
        len(papers),
    )

    if limit > 0:
        to_refill = to_refill[:limit]
        logger.info("Processing first %d items (limit active)", limit)

    for paper in to_refill:
        arxiv_id = paper.arxiv_id
        if not arxiv_id:
            skipped += 1
            continue

        new_date = fetch_semantic_scholar_published_date(arxiv_id)
        if not new_date:
            failed += 1
            logger.debug("No SS date for arXiv:%s (current=%r)", arxiv_id, paper.published_date)
            continue

        if new_date != paper.published_date:
            logger.info("Updating arXiv:%s  %s → %s", arxiv_id, paper.published_date, new_date)
            if not dry_run:
                with session_scope() as session:
                    live = session.get(Paper, paper.id)
                    if live:
                        live.published_date = new_date
            updated += 1
        else:
            skipped += 1

        if sleep > 0:
            time.sleep(sleep)

    logger.info("Done — updated: %d, skipped/unchanged: %d, failed: %d", updated, skipped, failed)


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Backfill exact paper dates from Semantic Scholar")
    parser.add_argument(
        "--dry-run", action="store_true", help="Print changes without writing to DB"
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="Process at most N papers (0 = unlimited)"
    )
    parser.add_argument(
        "--sleep", type=float, default=0.25, help="Seconds to sleep between API calls"
    )
    args = parser.parse_args(argv)
    backfill(dry_run=args.dry_run, limit=args.limit, sleep=args.sleep)


if __name__ == "__main__":
    main()
