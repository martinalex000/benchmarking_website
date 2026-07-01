"""Backfill publication venue/date metadata from Semantic Scholar.

Usage::
    uv run python scripts/backfill_ss_publication.py --limit 500
    uv run python scripts/backfill_ss_publication.py --dry-run
    uv run python scripts/backfill_ss_publication.py --include-all
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from pathlib import Path

import requests
from sqlalchemy import or_
from tqdm import tqdm

_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root))

from backend.db import init_db, session_scope  # noqa: E402
from backend.models import Paper, Result  # noqa: E402
from backend.semantic_scholar import (  # noqa: E402
    _resolve_venue_from_s2,
    _s2_headers,
    resolve_paper_venue,
)
from backend.venue import venue_needs_resolution  # noqa: E402

_S2_BASE = "https://api.semanticscholar.org/graph/v1"


def _needs_backfill(paper: Paper) -> bool:
    return not paper.venue or not paper.published_date or len(paper.published_date or "") < 10


def _papers_needing_backfill(session, *, with_results_only: bool) -> list[Paper]:
    query = session.query(Paper)
    if with_results_only:
        query = (
            query.join(Paper.results)
            .filter(or_(Result.is_problematic.is_(None), Result.is_problematic == 0))
            .distinct()
        )
    return [paper for paper in query.all() if _needs_backfill(paper)]


def _fetch_metadata_individual(arxiv_id: str) -> dict[str, str] | None:
    """Fetch metadata for a single paper, returning None on failure."""
    try:
        url = f"{_S2_BASE}/paper/ARXIV:{arxiv_id}"
        resp = requests.get(
            url,
            headers=_s2_headers(),
            params={
                "fields": "title,abstract,year,publicationDate,venue,publicationVenue,journal,externalIds"
            },
            timeout=30,
        )
        if resp.status_code == 429:
            return None
        if resp.status_code >= 400:
            return None
        data = resp.json()
        if not isinstance(data, dict):
            return None
        meta: dict[str, str] = {}
        if data.get("title"):
            meta["title"] = str(data["title"]).strip()
        if data.get("abstract"):
            meta["abstract"] = str(data["abstract"]).strip()
        published_date = str(data.get("publicationDate") or "").strip()
        if published_date:
            meta["published_date"] = published_date[:10]
        else:
            year = data.get("year")
            if isinstance(year, int) and year > 0:
                meta["published_date"] = f"{year:04d}-01-01"
            elif isinstance(year, str) and year.isdigit():
                meta["published_date"] = f"{int(year):04d}-01-01"
        venue = _resolve_venue_from_s2(data)
        if not venue:
            venue = resolve_paper_venue(arxiv_id, {})
        if venue:
            meta["venue"] = venue
        if meta:
            return meta
        return None
    except requests.RequestException:
        return None


def backfill(
    dry_run: bool = False,
    limit: int = 0,
    *,
    with_results_only: bool = True,
) -> None:
    init_db()
    updated = 0
    skipped = 0

    with session_scope() as session:
        papers = _papers_needing_backfill(session, with_results_only=with_results_only)
        total_needed = len(papers)
        scope = "with benchmark results" if with_results_only else "in database"
        if limit > 0:
            if limit < total_needed:
                print(
                    f"Found {total_needed} {scope} paper(s) needing metadata — limited to {limit}"
                )
            else:
                print(f"Found {total_needed} {scope} paper(s) needing Semantic Scholar metadata")
            random.shuffle(papers)
            papers = papers[:limit]
        else:
            if total_needed:
                print(f"Found {total_needed} {scope} paper(s) needing Semantic Scholar metadata")

        with tqdm(total=len(papers), desc="0 updated, 0 skipped", unit="paper") as pbar:
            for paper in papers:
                if not paper.arxiv_id:
                    skipped += 1
                    pbar.set_description(f"{updated} updated, {skipped} skipped, no arxiv_id")
                else:
                    meta = _fetch_metadata_individual(paper.arxiv_id)
                    if meta:
                        changed = False
                        if meta.get("venue") and venue_needs_resolution(paper.venue):
                            paper.venue = meta["venue"]
                            changed = True
                        if meta.get("published_date") and (
                            not paper.published_date or len(paper.published_date) < 10
                        ):
                            paper.published_date = meta["published_date"]
                            changed = True
                        if changed:
                            updated += 1
                            pbar.set_description(f"{updated} updated, {skipped} skipped, success")
                        else:
                            skipped += 1
                            pbar.set_description(f"{updated} updated, {skipped} skipped, no change")
                    else:
                        skipped += 1
                        pbar.set_description(f"{updated} updated, {skipped} skipped, no metadata")
                pbar.update()
                time.sleep(1.1)

        if dry_run:
            session.rollback()

    print(f"Done — updated: {updated}, skipped/unchanged: {skipped}")


def main(argv: list[str] | None = None) -> None:
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
        "--include-all",
        action="store_true",
        help="Include papers without benchmark results (default: only papers with results)",
    )
    args = parser.parse_args(argv)
    backfill(
        dry_run=args.dry_run,
        limit=args.limit,
        with_results_only=not args.include_all,
    )


if __name__ == "__main__":
    main()
