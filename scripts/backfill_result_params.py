"""Backfill Result.params_millions from papers/*/extracted/llm_output.yaml.

Usage::

    uv run python scripts/backfill_result_params.py
    uv run python scripts/backfill_result_params.py --dry-run --limit 50
    uv run python scripts/backfill_result_params.py --paper 2410.10320
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.result_params_backfill import backfill_all_result_params_millions  # noqa: E402

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Backfill Result.params_millions in the DB")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without committing")
    parser.add_argument("--limit", type=int, default=0, help="Max papers to process (0 = all)")
    parser.add_argument(
        "--paper",
        "-p",
        action="append",
        dest="papers",
        metavar="ARXIV_ID",
        help="Limit to specific arXiv IDs (repeatable)",
    )
    args = parser.parse_args(argv)

    summary = backfill_all_result_params_millions(
        arxiv_ids=args.papers,
        dry_run=args.dry_run,
        limit=args.limit,
    )

    prefix = "[dry-run] " if args.dry_run else ""
    print(
        f"{prefix}papers={summary.papers_seen} with_yaml={summary.papers_with_yaml} "
        f"without_yaml={summary.papers_without_yaml} "
        f"updated={summary.results_updated} still_null={summary.results_still_null}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
