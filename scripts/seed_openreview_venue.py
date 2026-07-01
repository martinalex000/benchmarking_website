#!/usr/bin/env python3
"""Enqueue OpenReview conference papers as manually important todo items.

Fetches submissions from configured OpenReview venues (LoG by default), resolves
arXiv IDs from note metadata or by matching title+authors against the papers table,
and flags each match as ``is_manually_important`` in ``todo_papers``.

Requires OpenReview credentials in ``.env``::

    OPENREVIEW_TOKEN=...   # recommended; see scripts/openreview_login.py

Or username/password (less secure)::

    OPENREVIEW_USERNAME=you@example.com
    OPENREVIEW_PASSWORD=your-password

Usage::

    uv run python scripts/seed_openreview_venue.py --list
    uv run python scripts/seed_openreview_venue.py --venue log --year 2023 --dry-run
    uv run python scripts/seed_openreview_venue.py --all-log
    uv run python scripts/seed_openreview_venue.py --venue-id logconference.io/LOG/2024/Conference
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml
from rich.console import Console
from rich.table import Table

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.config import cfg, normalize_arxiv_id  # noqa: E402
from backend.db import init_db, session_scope  # noqa: E402
from backend.models import Paper  # noqa: E402
from backend.openreview_client import OpenReviewClient, OpenReviewError  # noqa: E402
from backend.paper_matching import match_paper_by_title_authors, titles_match  # noqa: E402
from backend.todo_queue import add_todo_paper  # noqa: E402

console = Console()
_VENUES_FILE = cfg.config_dir / "openreview_venues.yaml"


def _load_venue_configs() -> list[dict]:
    if not _VENUES_FILE.exists():
        return []
    data = yaml.safe_load(_VENUES_FILE.read_text(encoding="utf-8")) or {}
    venues = data.get("venues") or []
    return [venue for venue in venues if isinstance(venue, dict) and venue.get("id")]


def _select_venues(
    *,
    venue_id: str | None,
    venue_label: str | None,
    year: int | None,
    all_log: bool,
) -> list[dict]:
    venues = _load_venue_configs()
    if venue_id:
        return [venue for venue in venues if venue.get("id") == venue_id]
    if all_log or (venue_label and venue_label.lower() in {"log", "log conference"}):
        return venues
    if year is not None:
        return [venue for venue in venues if int(venue.get("year") or 0) == year]
    if venue_label:
        needle = venue_label.lower()
        return [venue for venue in venues if needle in str(venue.get("label", "")).lower()]
    return []


def _resolve_arxiv_id(
    paper,
    *,
    db_papers: list[Paper],
) -> tuple[str, str]:
    arxiv_id = normalize_arxiv_id(paper.arxiv_id) if paper.arxiv_id else ""
    if arxiv_id:
        return arxiv_id, "openreview-metadata"
    match = match_paper_by_title_authors(
        db_papers,
        title=paper.title,
        authors=paper.authors,
    )
    if match and match.arxiv_id:
        return normalize_arxiv_id(match.arxiv_id), "title-authors"
    return "", "unresolved"


def seed_venue(
    venue_cfg: dict,
    *,
    dry_run: bool,
    requeue: bool,
    client: OpenReviewClient,
    db_papers: list[Paper],
) -> dict[str, int]:
    venue_id = str(venue_cfg["id"])
    canonical_venue = str(venue_cfg.get("canonical_venue") or "")
    counts = {
        "fetched": 0,
        "queued": 0,
        "matched_db": 0,
        "skipped_no_arxiv": 0,
        "already_important": 0,
    }

    submissions = client.fetch_venue_submissions(venue_id)
    counts["fetched"] = len(submissions)

    for submission in submissions:
        arxiv_id, match_kind = _resolve_arxiv_id(submission, db_papers=db_papers)
        if not arxiv_id:
            counts["skipped_no_arxiv"] += 1
            console.print(
                f"[yellow]skip[/yellow] {submission.title[:80]} — no arXiv id "
                f"(authors={', '.join(submission.authors[:3])})"
            )
            continue
        if match_kind == "title-authors":
            counts["matched_db"] += 1

        reason = f"openreview:{venue_cfg.get('label') or venue_id}"
        if dry_run:
            counts["queued"] += 1
            console.print(
                f"[cyan]would queue[/cyan] {arxiv_id} — {submission.title[:80]} " f"({match_kind})"
            )
            continue

        added, message = add_todo_paper(
            arxiv_id,
            title=submission.title,
            reason=reason,
            added_by="seed_openreview_venue",
            is_manually_important=True,
            requeue=requeue,
        )
        if added:
            counts["queued"] += 1
        else:
            counts["already_important"] += 1
        console.print(f"[green]{message}[/green]")

        if canonical_venue:
            with session_scope() as session:
                paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
                if paper is not None and (
                    not paper.venue
                    or paper.venue != canonical_venue
                    or titles_match(submission.venue, "LOG IN")
                ):
                    paper.venue = canonical_venue

    return counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Seed todo queue from OpenReview venues")
    parser.add_argument("--list", action="store_true", help="List configured venues and exit")
    parser.add_argument("--venue-id", help="Exact OpenReview venue group id")
    parser.add_argument("--venue", help="Short venue label such as 'log'")
    parser.add_argument("--year", type=int, help="Conference year (e.g. 2023)")
    parser.add_argument("--all-log", action="store_true", help="Seed all configured LoG years")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing")
    parser.add_argument("--requeue", action="store_true", help="Requeue done/failed papers")
    args = parser.parse_args(argv)

    venues = _load_venue_configs()
    if args.list:
        table = Table(title="Configured OpenReview venues")
        table.add_column("Label")
        table.add_column("Venue ID")
        table.add_column("Year")
        for venue in venues:
            table.add_row(
                str(venue.get("label") or ""),
                str(venue.get("id") or ""),
                str(venue.get("year") or ""),
            )
        console.print(table)
        return 0

    selected = _select_venues(
        venue_id=args.venue_id,
        venue_label=args.venue,
        year=args.year,
        all_log=args.all_log,
    )
    if not selected:
        console.print("[red]No venues matched the selection.[/red]")
        return 1

    try:
        client = OpenReviewClient.from_config()
    except OpenReviewError as exc:
        console.print(f"[red]{exc}[/red]")
        return 1

    init_db()
    with session_scope() as session:
        db_papers = session.query(Paper).all()

    totals = {
        "fetched": 0,
        "queued": 0,
        "matched_db": 0,
        "skipped_no_arxiv": 0,
        "already_important": 0,
    }
    for venue_cfg in selected:
        console.print(f"\n[bold]Venue {venue_cfg.get('label') or venue_cfg.get('id')}[/bold]")
        counts = seed_venue(
            venue_cfg,
            dry_run=args.dry_run,
            requeue=args.requeue,
            client=client,
            db_papers=db_papers,
        )
        for key, value in counts.items():
            totals[key] += value

    console.print(
        "\n[bold]Summary[/bold]: "
        f"fetched={totals['fetched']} "
        f"queued={totals['queued']} "
        f"matched_db={totals['matched_db']} "
        f"skipped_no_arxiv={totals['skipped_no_arxiv']} "
        f"already_important={totals['already_important']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
