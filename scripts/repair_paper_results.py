"""Delete and re-parse benchmark results for selected papers.

Usage::

    uv run python -m scripts.repair_paper_results 2005.00687 1706.08566 1707.01476
    uv run python -m scripts.repair_paper_results 2005.00687 --export
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.db import init_db, session_scope
from backend.models import Model, Paper, Result
from backend.results_parser import parse_and_store

logger = logging.getLogger(__name__)


def _delete_paper_results(arxiv_ids: list[str]) -> tuple[int, int]:
    deleted_results = 0
    with session_scope() as session:
        for arxiv_id in arxiv_ids:
            paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
            if paper is None:
                logger.warning("No paper row for %s — skipping delete", arxiv_id)
                continue
            count = (
                session.query(Result).filter_by(paper_id=paper.id).delete(synchronize_session=False)
            )
            deleted_results += count
            logger.info("Deleted %d result(s) for %s", count, arxiv_id)

    deleted_models = 0
    with session_scope() as session:
        referenced = {row[0] for row in session.query(Result.model_id).distinct().all()}
        orphan_query = session.query(Model)
        if referenced:
            orphan_query = orphan_query.filter(Model.id.notin_(referenced))
        orphans = orphan_query.all()
        for model in orphans:
            session.delete(model)
            deleted_models += 1
        if orphans:
            logger.info("Deleted %d orphan model(s)", deleted_models)
    return deleted_results, deleted_models


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Delete and re-parse paper results")
    parser.add_argument("arxiv_ids", nargs="+", metavar="ARXIV_ID")
    parser.add_argument(
        "--export",
        action="store_true",
        help="Run Hugo export after re-parsing",
    )
    args = parser.parse_args(argv)

    init_db()
    deleted_results, deleted_models = _delete_paper_results(args.arxiv_ids)
    print(f"Deleted {deleted_results} result(s) and {deleted_models} orphan model(s)")

    parsed: list[str] = []
    for arxiv_id in args.arxiv_ids:
        count = parse_and_store(arxiv_id)
        print(f"Re-parsed {arxiv_id}: {count} result(s) stored")
        parsed.append(arxiv_id)

    if args.export and parsed:
        from backend.export_to_hugo import export_all

        export_all(arxiv_ids=parsed)
        print(f"Exported Hugo content for {len(parsed)} paper(s)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
