#!/usr/bin/env python3
"""Semantic Scholar maintenance entrypoint.

This script can:
- seed and maintain the ``todo_papers`` queue from Semantic Scholar citations/references
- backfill missing author metadata from LaTeX caches with S2 ORCID enrichment
- backfill venue/date metadata from Semantic Scholar
- repair untrusted or missing publication venues (e.g. bogus ``LOG IN`` journal matches)

Usage examples::

    uv run python scripts/maintenance_semanticscholar.py todo
    uv run python scripts/maintenance_semanticscholar.py metadata
    uv run python scripts/maintenance_semanticscholar.py repair-venues --dry-run
    uv run python scripts/maintenance_semanticscholar.py all --limit 500
    uv run python scripts/maintenance_semanticscholar.py todo --seed 2401.01234
"""

from __future__ import annotations

import argparse
import random
import sqlite3
import sys
import time
from pathlib import Path

from sqlalchemy import or_
from tqdm import tqdm

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.config import cfg  # noqa: E402
from backend.db import init_db, session_scope  # noqa: E402
from backend.llm_metadata import _extract_metadata_from_latex_cache  # noqa: E402
from backend.models import Paper, Result  # noqa: E402
from backend.paper_storage import PaperStorage  # noqa: E402
from backend.s2_todo_crawl import (  # noqa: E402
    S2Client,
    crawl_seed,
    ensure_s2_tables,
    fetch_top_todo_rows,
    get_uncrawled_seeds,
    load_local_corpus_from_papers_table,
    repair_todo_counts,
    sync_todo_status_with_local_corpus,
)
from backend.semantic_scholar import (  # noqa: E402
    cache_paper_metadata,
    fetch_paper_metadata,
    resolve_paper_authors,
    resolve_paper_venue,
)
from backend.text_cleanup import authors_look_broken  # noqa: E402
from backend.venue import (  # noqa: E402
    normalize_conference_short,
    venue_needs_resolution,
)

_PROCESSED_STATUSES = {"extracted", "quarantined_yaml_parse", "quarantined_method_name"}


def _latex_dir_for(arxiv_id: str) -> Path:
    return cfg.papers_dir / arxiv_id / "latex"


def _papers_needing_authors(session, *, with_results_only: bool) -> list[Paper]:
    query = session.query(Paper).filter(Paper.extraction_status.in_(_PROCESSED_STATUSES))
    if with_results_only:
        query = (
            query.join(Paper.results)
            .filter(or_(Result.is_problematic.is_(None), Result.is_problematic == 0))
            .distinct()
        )
    return [
        paper for paper in query.all() if not paper.authors or authors_look_broken(paper.authors)
    ]


def _count_papers_with_broken_authors(session, *, with_results_only: bool) -> int:
    query = session.query(Paper).filter(Paper.extraction_status.in_(_PROCESSED_STATUSES))
    if with_results_only:
        query = (
            query.join(Paper.results)
            .filter(or_(Result.is_problematic.is_(None), Result.is_problematic == 0))
            .distinct()
        )
    return sum(1 for paper in query.all() if paper.authors and authors_look_broken(paper.authors))


def _papers_needing_publication(session, *, with_results_only: bool) -> list[Paper]:
    query = session.query(Paper)
    if with_results_only:
        query = (
            query.join(Paper.results)
            .filter(or_(Result.is_problematic.is_(None), Result.is_problematic == 0))
            .distinct()
        )
    return [
        paper
        for paper in query.all()
        if not paper.venue or not paper.published_date or len(paper.published_date or "") < 10
    ]


def _count_papers_needing_authors(session, *, with_results_only: bool) -> int:
    return len(_papers_needing_authors(session, with_results_only=with_results_only))


def _count_papers_needing_publication(session, *, with_results_only: bool) -> int:
    return len(_papers_needing_publication(session, with_results_only=with_results_only))


def _count_uncrawled_seeds(conn: sqlite3.Connection) -> int:
    return len(get_uncrawled_seeds(conn))


def _count_todo_rows(conn: sqlite3.Connection) -> int:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM todo_papers")
    row = cur.fetchone()
    return int(row[0] or 0) if row else 0


def print_info(*, db_path: Path | None, include_all: bool) -> None:
    init_db()
    with session_scope() as session:
        with_results_only = not include_all
        author_count = _count_papers_needing_authors(session, with_results_only=with_results_only)
        broken_author_count = _count_papers_with_broken_authors(
            session, with_results_only=with_results_only
        )
        publication_count = _count_papers_needing_publication(
            session, with_results_only=with_results_only
        )
        venue_repair_count = _count_papers_needing_venue_repair(
            session,
            with_results_only=with_results_only,
            include_known_wrong=False,
        )

    path = db_path or cfg.db_path
    conn = sqlite3.connect(str(path))
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        ensure_s2_tables(conn)
        load_local_corpus_from_papers_table(conn)
        todo_total = _count_todo_rows(conn)
        todo_seeds = _count_uncrawled_seeds(conn)
    finally:
        conn.close()

    scope = "processed papers with benchmark results" if not include_all else "processed papers"
    print("Semantic Scholar maintenance info")
    print(f"- authors backfill: {author_count} {scope} need author metadata")
    print(f"- broken authors: {broken_author_count} {scope} have LaTeX-contaminated authors")
    print(f"- publication backfill: {publication_count} {scope} need venue/date metadata")
    print(f"- venue repair: {venue_repair_count} {scope} need venue correction")
    print(f"- todo crawl: {todo_seeds} uncrawled DB seed paper(s) available")
    print(f"- todo_papers table: {todo_total} row(s) currently tracked")


def _authors_for_paper(arxiv_id: str) -> list[dict[str, str | None]] | None:
    latex_names: list[str] | None = None
    latex_dir = _latex_dir_for(arxiv_id)
    if latex_dir.exists():
        latex_meta = _extract_metadata_from_latex_cache(latex_dir)
        raw_names = latex_meta.get("authors")
        if isinstance(raw_names, list) and raw_names:
            latex_names = [str(name) for name in raw_names if str(name).strip()]
    try:
        authors = resolve_paper_authors(arxiv_id, latex_names=latex_names)
        if authors and not authors_look_broken(authors):
            return authors
    except Exception:
        return None
    return None


def backfill_authors(*, dry_run: bool, limit: int, with_results_only: bool) -> None:
    init_db()
    updated = 0
    skipped = 0

    with session_scope() as session:
        papers = _papers_needing_authors(session, with_results_only=with_results_only)
        total_needed = len(papers)
        scope = "with benchmark results" if with_results_only else "processed"
        if limit > 0:
            print(f"Found {total_needed} {scope} paper(s) needing authors — limited to {limit}")
            random.shuffle(papers)
            papers = papers[:limit]
        elif total_needed:
            print(f"Found {total_needed} {scope} paper(s) needing author backfill")

        with tqdm(total=len(papers), desc="0 updated, 0 skipped", unit="paper") as pbar:
            for paper in papers:
                if not paper.arxiv_id:
                    skipped += 1
                    pbar.set_description(f"{updated} updated, {skipped} skipped, no arxiv_id")
                else:
                    authors = _authors_for_paper(paper.arxiv_id)
                    if authors:
                        paper.authors = authors
                        PaperStorage(paper.arxiv_id).update_metadata({"authors": authors})
                        updated += 1
                        pbar.set_description(f"{updated} updated, {skipped} skipped, success")
                    else:
                        skipped += 1
                        pbar.set_description(
                            f"{updated} updated, {skipped} skipped, unresolved authors"
                        )
                pbar.update()
                time.sleep(1.1)

        if dry_run:
            session.rollback()

    print(f"Done — updated: {updated}, skipped/unchanged: {skipped}")


def _paper_needs_venue_repair(paper: Paper, *, include_known_wrong: bool) -> bool:
    if venue_needs_resolution(paper.venue):
        return True
    if not include_known_wrong:
        return False
    raw = " ".join(str(paper.venue or "").split()).strip()
    return bool(raw) and not normalize_conference_short(raw)


def _papers_needing_venue_repair(
    session, *, with_results_only: bool, include_known_wrong: bool
) -> list[Paper]:
    query = session.query(Paper)
    if with_results_only:
        query = (
            query.join(Paper.results)
            .filter(or_(Result.is_problematic.is_(None), Result.is_problematic == 0))
            .distinct()
        )
    return [
        paper
        for paper in query.all()
        if paper.arxiv_id
        and _paper_needs_venue_repair(paper, include_known_wrong=include_known_wrong)
    ]


def _count_papers_needing_venue_repair(
    session, *, with_results_only: bool, include_known_wrong: bool
) -> int:
    return len(
        _papers_needing_venue_repair(
            session,
            with_results_only=with_results_only,
            include_known_wrong=include_known_wrong,
        )
    )


def backfill_publication(*, dry_run: bool, limit: int, with_results_only: bool) -> None:
    init_db()
    updated = 0
    skipped = 0

    with session_scope() as session:
        papers = _papers_needing_publication(session, with_results_only=with_results_only)
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
                    meta = fetch_paper_metadata(paper.arxiv_id)
                    if meta:
                        cache_paper_metadata(paper.arxiv_id, meta)
                        changed = False
                        if venue_needs_resolution(paper.venue):
                            resolved_venue = resolve_paper_venue(paper.arxiv_id, meta)
                            if resolved_venue:
                                paper.venue = resolved_venue
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


def repair_venues(
    *,
    dry_run: bool,
    limit: int,
    with_results_only: bool,
    include_known_wrong: bool,
) -> None:
    init_db()
    updated = 0
    skipped = 0

    with session_scope() as session:
        papers = _papers_needing_venue_repair(
            session,
            with_results_only=with_results_only,
            include_known_wrong=include_known_wrong,
        )
        total_needed = len(papers)
        scope = "with benchmark results" if with_results_only else "in database"
        if limit > 0:
            if limit < total_needed:
                print(
                    f"Found {total_needed} {scope} paper(s) needing venue repair — limited to {limit}"
                )
            else:
                print(f"Found {total_needed} {scope} paper(s) needing venue repair")
            random.shuffle(papers)
            papers = papers[:limit]
        else:
            if total_needed:
                print(f"Found {total_needed} {scope} paper(s) needing venue repair")

        with tqdm(total=len(papers), desc="0 updated, 0 skipped", unit="paper") as pbar:
            for paper in papers:
                arxiv_id = paper.arxiv_id
                if not arxiv_id:
                    skipped += 1
                    pbar.set_description(f"{updated} updated, {skipped} skipped, no arxiv_id")
                else:
                    before = paper.venue
                    resolved_venue = resolve_paper_venue(arxiv_id)
                    if resolved_venue and resolved_venue != before:
                        paper.venue = resolved_venue
                        updated += 1
                        pbar.set_description(
                            f"{updated} updated, {skipped} skipped, {before!r}->{resolved_venue!r}"
                        )
                    else:
                        skipped += 1
                        pbar.set_description(f"{updated} updated, {skipped} skipped, no change")
                pbar.update()
                time.sleep(1.1)

        if dry_run:
            session.rollback()

    print(f"Done — updated: {updated}, skipped/unchanged: {skipped}")


def backfill_todo(*, db_path: Path | None, limit: int, seed: list[str] | None, top: int) -> None:
    path = db_path or cfg.db_path
    conn = sqlite3.connect(str(path))
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        ensure_s2_tables(conn)
        load_local_corpus_from_papers_table(conn)
        repair_todo_counts(conn)
        sync_todo_status_with_local_corpus(conn)

        seeds = seed
        if not seeds:
            seeds = get_uncrawled_seeds(conn)
            if seeds:
                print(f"[dim]No --seed given: crawling {len(seeds)} uncrawled DB papers.[/dim]")
            else:
                print(
                    "[yellow]No seeds given and no uncrawled papers in DB. Nothing to do.[/yellow]"
                )
                return

        s2 = S2Client(min_delay=1.0)
        for item in seeds:
            print(f"\n[bold]Processing seed {item.strip()} (limit={limit})[/bold]")
            stats = crawl_seed(s2, conn, item.strip(), limit, False)
            print(
                f"  Citations: {stats['citations']} → {stats['cite_added']} added, "
                f"{stats['cite_missing']} missing arXiv IDs"
            )
            print(
                f"  References: {stats['references']} → {stats['ref_added']} added, "
                f"{stats['ref_missing']} missing arXiv IDs"
            )

        repair_todo_counts(conn)
        sync_todo_status_with_local_corpus(conn)

        print("\nTop todo papers:")
        for idx, (arxiv_id, title, seen_count) in enumerate(fetch_top_todo_rows(conn, top), 1):
            print(f"{idx:>2}. {arxiv_id}  ({seen_count})  {title}")

        try:
            from backend.export_to_hugo import export_development_data

            export_development_data()
        except Exception as exc:
            print(f"[yellow]Could not refresh generated dev data: {exc}[/yellow]")
    finally:
        conn.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Semantic Scholar maintenance tasks")
    subparsers = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--limit", type=int, default=0, help="Process at most N papers")

    p_authors = subparsers.add_parser("authors", parents=[common], help="Backfill authors")
    p_authors.add_argument(
        "--include-all", action="store_true", help="Include processed papers without results"
    )
    p_authors.add_argument("--dry-run", action="store_true", help="Do not write DB changes")

    p_publication = subparsers.add_parser(
        "publication", parents=[common], help="Backfill venue/date"
    )
    p_publication.add_argument(
        "--include-all", action="store_true", help="Include papers without results"
    )
    p_publication.add_argument("--dry-run", action="store_true", help="Do not write DB changes")

    p_repair_venues = subparsers.add_parser(
        "repair-venues", parents=[common], help="Repair untrusted or missing venues"
    )
    p_repair_venues.add_argument(
        "--include-all", action="store_true", help="Include papers without results"
    )
    p_repair_venues.add_argument(
        "--include-known-wrong",
        action="store_true",
        help="Also repair non-empty venues that do not normalize to a known conference",
    )
    p_repair_venues.add_argument("--dry-run", action="store_true", help="Do not write DB changes")

    p_todo = subparsers.add_parser("todo", help="Seed and maintain todo_papers")
    p_todo.add_argument("--seed", "-s", action="append", default=None, help="Seed arXiv ID")
    p_todo.add_argument("--limit", "-n", type=int, default=5000, help="Max citations/references")
    p_todo.add_argument("--db-path", default=None, help="Path to SQLite DB")
    p_todo.add_argument("--top", type=int, default=15, help="Top-N todo rows to show")

    p_info = subparsers.add_parser("info", help="Show maintenance impact statistics")
    p_info.add_argument(
        "--include-all", action="store_true", help="Include processed papers without results"
    )
    p_info.add_argument("--db-path", default=None, help="Path to SQLite DB")

    p_all = subparsers.add_parser("all", parents=[common], help="Run all maintenance tasks")
    p_all.add_argument(
        "--include-all", action="store_true", help="Include processed papers without results"
    )
    p_all.add_argument("--dry-run", action="store_true", help="Do not write DB changes")
    p_all.add_argument("--seed", "-s", action="append", default=None, help="Seed arXiv ID")
    p_all.add_argument("--db-path", default=None, help="Path to SQLite DB")
    p_all.add_argument("--top", type=int, default=15, help="Top-N todo rows to show")

    args = parser.parse_args(argv)

    if args.command == "authors":
        backfill_authors(
            dry_run=args.dry_run,
            limit=args.limit,
            with_results_only=not args.include_all,
        )
    elif args.command == "publication":
        backfill_publication(
            dry_run=args.dry_run,
            limit=args.limit,
            with_results_only=not args.include_all,
        )
    elif args.command == "repair-venues":
        repair_venues(
            dry_run=args.dry_run,
            limit=args.limit,
            with_results_only=not args.include_all,
            include_known_wrong=args.include_known_wrong,
        )
    elif args.command == "todo":
        backfill_todo(db_path=args.db_path, limit=args.limit, seed=args.seed, top=args.top)
    elif args.command == "info":
        print_info(db_path=args.db_path, include_all=args.include_all)
    elif args.command == "all":
        print_info(db_path=args.db_path, include_all=args.include_all)
        backfill_authors(
            dry_run=args.dry_run,
            limit=args.limit,
            with_results_only=not args.include_all,
        )
        backfill_publication(
            dry_run=args.dry_run,
            limit=args.limit,
            with_results_only=not args.include_all,
        )
        backfill_todo(db_path=args.db_path, limit=args.limit or 5000, seed=args.seed, top=args.top)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
