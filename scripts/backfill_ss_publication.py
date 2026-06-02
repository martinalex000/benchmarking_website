"""Backfill publication venue/date metadata from Semantic Scholar in batches.

Usage::
    uv run python scripts/backfill_ss_publication.py --limit 500 --batch-size 50
    uv run python scripts/backfill_ss_publication.py --dry-run
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.db import init_db, session_scope  # noqa: E402
from backend.models import Paper  # noqa: E402
from backend.semantic_scholar import fetch_paper_metadata_batch  # noqa: E402

logger = logging.getLogger(__name__)


def _needs_backfill(paper: Paper) -> bool:
    return not paper.venue or not paper.published_date or len(paper.published_date or "") < 10


def backfill(dry_run: bool = False, limit: int = 0, batch_size: int = 50) -> None:
    init_db()
    updated = 0
    skipped = 0

    with session_scope() as session:
        papers = [paper for paper in session.query(Paper).all() if _needs_backfill(paper)]
        if limit > 0:
            papers = papers[:limit]
        logger.info("Found %d paper(s) needing Semantic Scholar metadata", len(papers))

        for start in range(0, len(papers), batch_size):
            batch = papers[start : start + batch_size]
            meta_map = fetch_paper_metadata_batch(
                [paper.arxiv_id for paper in batch if paper.arxiv_id]
            )
            for paper in batch:
                if not paper.arxiv_id:
                    skipped += 1
                    continue
                meta = meta_map.get(paper.arxiv_id)
                if not meta:
                    skipped += 1
                    continue
                changed = False
                if meta.get("venue") and not paper.venue:
                    paper.venue = meta["venue"]
                    changed = True
                if meta.get("published_date") and (
                    not paper.published_date or len(paper.published_date) < 10
                ):
                    paper.published_date = meta["published_date"]
                    changed = True
                if changed:
                    updated += 1
                    logger.info(
                        "Updated arXiv:%s venue=%r date=%r",
                        paper.arxiv_id,
                        paper.venue,
                        paper.published_date,
                    )
            if dry_run:
                session.rollback()
                continue

    logger.info("Done — updated: %d, skipped/unchanged: %d", updated, skipped)


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(
        description="Backfill venue/date metadata from Semantic Scholar"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print changes without writing to DB"
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="Process at most N papers (0 = unlimited)"
    )
    parser.add_argument(
        "--batch-size", type=int, default=50, help="Batch size for Semantic Scholar requests"
    )
    args = parser.parse_args(argv)
    backfill(dry_run=args.dry_run, limit=args.limit, batch_size=args.batch_size)


if __name__ == "__main__":
    main()
