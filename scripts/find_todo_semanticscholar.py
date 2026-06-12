#!/usr/bin/env python3
"""Crawl Semantic Scholar to seed `todo_papers` in the SQLite DB.

When --seed is omitted the script crawls ALL papers already in the `papers` table
that have not yet been fully crawled (i.e. not present in `s2_crawl_state`).
"""

from __future__ import annotations

import argparse
import os
import sqlite3
from collections.abc import Iterable
from pathlib import Path

from rich.console import Console
from rich.table import Table

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
try:
    from dotenv import load_dotenv as _load_dotenv

    _load_dotenv(_PROJECT_ROOT / ".env", override=False)
except ImportError:
    pass

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

console = Console()


def _render_top_report(conn: sqlite3.Connection, top_n: int) -> None:
    rows = fetch_top_todo_rows(conn, top_n)
    table = Table(show_header=True, header_style="bold")
    table.add_column("#", width=4)
    table.add_column("arXiv", style="cyan", width=14)
    table.add_column("seen_count", width=8)
    table.add_column("title")
    for index, (arxiv_id, title, seen_count) in enumerate(rows, 1):
        table.add_row(str(index), arxiv_id, str(seen_count), title)
    console.print(table)


def main(argv: Iterable[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Seed todo_papers via Semantic Scholar crawl",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "When --seed is omitted, all papers already in the database are used as seeds\n"
            "(except those already crawled). The API key is read from SEMANTIC_SCHOLAR_API_KEY\n"
            "in the environment / .env file."
        ),
    )
    parser.add_argument(
        "--seed",
        "-s",
        action="append",
        default=None,
        help="Seed arXiv ID (repeatable). Omit to crawl all DB papers.",
    )
    parser.add_argument(
        "--limit",
        "-n",
        type=int,
        default=5000,
        help="Max citations/references fetched per seed (default: 5000)",
    )
    parser.add_argument(
        "--db-path", default=None, help="Path to SQLite DB (defaults to data/benchmarks.db)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-crawl seeds even if already recorded in s2_crawl_state",
    )
    parser.add_argument(
        "--top", type=int, default=15, help="Show top-N todo papers after run (default: 15)"
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    db_path = Path(args.db_path) if args.db_path else _PROJECT_ROOT / "data" / "benchmarks.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    key_source = (
        "SEMANTIC_SCHOLAR_API_KEY"
        if os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
        else "S2_API_KEY" if os.environ.get("S2_API_KEY") else "none (rate-limited)"
    )
    console.print(f"API key source: [dim]{key_source}[/dim]")
    console.print(f"Using DB: [cyan]{db_path}[/cyan]")

    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")
    ensure_s2_tables(conn)
    load_local_corpus_from_papers_table(conn)
    repair_todo_counts(conn)
    sync_todo_status_with_local_corpus(conn)

    seeds = args.seed
    if not seeds:
        seeds = get_uncrawled_seeds(conn)
        if seeds:
            console.print(f"[dim]No --seed given: crawling {len(seeds)} uncrawled DB papers.[/dim]")
        else:
            console.print(
                "[yellow]No seeds given and no uncrawled papers in DB. Nothing to do.[/yellow]"
            )
            conn.close()
            return

    s2 = S2Client(min_delay=1.0)
    for seed in seeds:
        console.print(f"\n[bold]Processing seed {seed.strip()} (limit={args.limit})[/bold]")
        stats = crawl_seed(s2, conn, seed.strip(), args.limit, args.force)
        console.print(
            f"  Citations: {stats['citations']} → {stats['cite_added']} added, "
            f"{stats['cite_missing']} missing arXiv IDs"
        )
        console.print(
            f"  References: {stats['references']} → {stats['ref_added']} added, "
            f"{stats['ref_missing']} missing arXiv IDs"
        )

    repair_todo_counts(conn)
    sync_todo_status_with_local_corpus(conn)

    console.print("\n[green]Crawl complete.[/green]")
    _render_top_report(conn, args.top)
    conn.close()

    console.print("\n[dim]Refreshing generated dev data…[/dim]")
    try:
        from backend.export_to_hugo import export_development_data

        export_development_data()
        console.print("[green]Generated dev data updated.[/green]")
    except Exception as exc:
        console.print(f"[yellow]Could not refresh generated dev data: {exc}[/yellow]")


if __name__ == "__main__":
    main()
