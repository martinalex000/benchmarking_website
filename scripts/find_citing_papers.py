#!/usr/bin/env python3
"""Discover papers citing a benchmark paper and mark selected ones as important.

Queries Semantic Scholar for citing papers, shows processing status against the
local database, then interactively marks selected papers as manually important in
`todo_papers`. Process them afterwards with:

    uv run python scripts/process_papers.py dashboard --workers 10

Usage::
    uv run python scripts/find_citing_papers.py 2206.08164
    uv run python scripts/find_citing_papers.py 2206.08164 --limit 100
    uv run python scripts/find_citing_papers.py 2206.08164 --show-all
    uv run python scripts/find_citing_papers.py 2206.08164 --mark-all
    uv run python scripts/find_citing_papers.py 2206.08164 --mark-all --limit 5000
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich import box
from rich.console import Console
from rich.table import Table

from backend.config import cfg, normalize_arxiv_id
from backend.s2_todo_crawl import S2Client, infer_arxiv_id_from_s2
from backend.todo_queue import add_todo_paper

console = Console()
_MARK_EXAMPLE_COUNT = 3


def _mark_papers_as_important(
    papers: list[dict[str, Any]],
    *,
    seed_arxiv_id: str,
) -> tuple[int, list[str]]:
    reason = f"cites {seed_arxiv_id}"
    marked = 0
    examples: list[str] = []
    for paper in papers:
        arxiv_id = paper["arxiv_id"]
        _created, message = add_todo_paper(
            arxiv_id,
            title=paper.get("title"),
            reason=reason,
            added_by="find_citing_papers",
            is_manually_important=True,
            requeue=True,
        )
        marked += 1
        if len(examples) < _MARK_EXAMPLE_COUNT:
            examples.append(f"{arxiv_id}: {message}")
    return marked, examples


def _print_mark_summary(marked: int, examples: list[str]) -> None:
    for example in examples:
        console.print(f"  [dim]• {example}[/dim]")
    remaining = marked - len(examples)
    if remaining > 0:
        console.print(f"  [dim]… and {remaining} more[/dim]")
    console.rule(f"[green]Marked {marked} paper(s) as manually important[/green]")
    console.print(
        "\nProcess them with:\n"
        "  [cyan]uv run python scripts/process_papers.py dashboard --workers 10[/cyan]"
    )


def _get_processed_ids() -> dict[str, str]:
    from backend.db import init_db, session_scope
    from backend.models import Paper

    init_db()
    with session_scope() as session:
        rows = session.query(Paper.arxiv_id, Paper.extraction_status).all()
        return {row.arxiv_id: row.extraction_status for row in rows if row.arxiv_id}


def _get_rejected_ids() -> dict[str, str]:
    from backend.db import init_db, session_scope
    from backend.models import PaperCandidate

    init_db()
    with session_scope() as session:
        rows = (
            session.query(PaperCandidate.arxiv_id, PaperCandidate.final_status)
            .filter(PaperCandidate.final_status.in_(["rejected_stage1", "rejected_stage2"]))
            .all()
        )
        return {row.arxiv_id: row.final_status for row in rows if row.arxiv_id}


def _has_local_extraction(arxiv_id: str) -> bool:
    from backend.paper_storage import PaperStorage

    return PaperStorage(arxiv_id).llm_output_path.exists()


def _pick_papers(candidates: list[dict[str, Any]]) -> list[str]:
    console.print(
        "\nEnter numbers to select (space/comma-separated), [bold]a[/bold] for all, or [bold]q[/bold] to quit:"
    )
    raw = input("> ").strip()
    if not raw or raw.lower() == "q":
        return []
    if raw.lower() == "a":
        return [candidate["arxiv_id"] for candidate in candidates]

    selected: list[str] = []
    for token in re.split(r"[\s,]+", raw):
        token = token.strip()
        if not token:
            continue
        try:
            index = int(token) - 1
            if 0 <= index < len(candidates):
                selected.append(candidates[index]["arxiv_id"])
            else:
                console.print(f"[yellow]  Index {token} out of range — skipped[/yellow]")
        except ValueError:
            console.print(f"[yellow]  Not a number: {token!r} — skipped[/yellow]")
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find citing papers and mark selected ones as manually important.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "arxiv_id",
        help="arXiv ID of the benchmark/dataset paper (e.g. 2206.08164)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Max number of citing papers to fetch (default: 200)",
    )
    parser.add_argument(
        "--show-all",
        action="store_true",
        help="Show all citing papers, including those without arXiv IDs",
    )
    parser.add_argument(
        "--mark-all",
        action="store_true",
        help=(
            "Mark every citing paper with an arXiv ID as manually important "
            "(non-interactive; includes already-processed papers)"
        ),
    )
    args = parser.parse_args()

    raw = args.arxiv_id.strip()
    match = re.match(r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", raw)
    if match:
        raw = match.group(1)
    seed_arxiv_id = normalize_arxiv_id(raw)

    if not cfg.semantic_scholar_api_key:
        console.print(
            "[red]SEMANTIC_SCHOLAR_API_KEY is required for Semantic Scholar lookups.[/red]"
        )
        sys.exit(1)

    console.rule(f"[bold]Citations of arXiv:{seed_arxiv_id}[/bold]")

    s2 = S2Client(min_delay=1.0)
    console.print("\n[bold]1. Looking up paper on Semantic Scholar…[/bold]")
    s2_id = s2.paper_id_for_arxiv(seed_arxiv_id)
    if not s2_id:
        console.print("[red]Could not find paper on Semantic Scholar. Aborting.[/red]")
        sys.exit(1)
    console.print(f"  Found S2 ID: [cyan]{s2_id}[/cyan]")

    console.print(f"\n[bold]2. Fetching up to {args.limit} citing papers…[/bold]")
    with console.status("[dim]Fetching citations from Semantic Scholar…[/dim]"):
        citations = s2.fetch_citations(s2_id, args.limit)
    console.print(f"  Retrieved [cyan]{len(citations)}[/cyan] citing papers.")

    console.print("\n[bold]3. Checking processing status…[/bold]")
    processed = _get_processed_ids()
    rejected = _get_rejected_ids()

    arxiv_papers: list[dict[str, Any]] = []
    no_arxiv: list[dict[str, Any]] = []

    for paper in citations:
        arxiv_id = infer_arxiv_id_from_s2(paper)
        if arxiv_id:
            has_extraction = _has_local_extraction(arxiv_id)
            db_status = processed.get(arxiv_id)
            reject_status = rejected.get(arxiv_id)

            if db_status:
                status = db_status
            elif reject_status == "rejected_stage1":
                status = "rejected_s1"
            elif reject_status == "rejected_stage2":
                status = "rejected_s2"
            elif has_extraction:
                status = "extracted (not in DB)"
            else:
                status = "new"

            arxiv_papers.append(
                {
                    "arxiv_id": arxiv_id,
                    "title": paper.get("title") or "",
                    "year": paper.get("year") or "",
                    "status": status,
                }
            )
        else:
            no_arxiv.append(paper)

    def _sort_key(paper: dict[str, Any]) -> tuple[int, int]:
        order = {"new": 0, "rejected_s1": 1, "rejected_s2": 2}
        status = paper["status"]
        return (order.get(status, 3), -int(paper.get("year") or 0))

    arxiv_papers.sort(key=_sort_key)

    new_count = sum(1 for paper in arxiv_papers if paper["status"] == "new")
    done_count = sum(
        1 for paper in arxiv_papers if paper["status"] in ("done", "extracted (not in DB)")
    )
    rejected_count = sum(1 for paper in arxiv_papers if paper["status"].startswith("rejected"))

    console.print(
        f"\n  [green]{len(arxiv_papers)}[/green] with arXiv IDs  "
        f"([yellow]{new_count}[/yellow] new, "
        f"[green]{done_count}[/green] already processed, "
        f"[red]{rejected_count}[/red] rejected, "
        f"[dim]{len(no_arxiv)}[/dim] without arXiv ID)"
    )

    if not args.mark_all:
        table = Table(show_header=True, header_style="bold", box=box.SIMPLE, show_edge=False)
        table.add_column("#", style="dim", justify="right", width=4)
        table.add_column("arXiv ID", style="cyan", width=13)
        table.add_column("Year", width=6)
        table.add_column("Status", width=24)
        table.add_column("Title")

        candidates: list[dict[str, Any]] = []
        for paper in arxiv_papers:
            status = paper["status"]
            is_done = status in ("done", "extracted (not in DB)")
            if not is_done:
                candidates.append(paper)
                num = str(len(candidates))
            else:
                num = "–"

            if status == "new":
                status_str = "[bold green]new[/bold green]"
            elif status == "done":
                status_str = "[dim]done[/dim]"
            elif status == "extracted (not in DB)":
                status_str = "[yellow]extracted (not in DB)[/yellow]"
            elif status == "failed":
                status_str = "[red]failed[/red]"
            elif status == "pending":
                status_str = "[yellow]pending[/yellow]"
            elif status == "rejected_s1":
                status_str = "[red]rejected (stage 1)[/red]"
            elif status == "rejected_s2":
                status_str = "[red]rejected (stage 2)[/red]"
            else:
                status_str = f"[dim]{status}[/dim]"

            title = paper["title"]
            if len(title) > 72:
                title = title[:69] + "…"
            table.add_row(num, paper["arxiv_id"], str(paper["year"]), status_str, title)

        console.print(table)
    else:
        candidates = [
            paper
            for paper in arxiv_papers
            if paper["status"] not in ("done", "extracted (not in DB)")
        ]
        console.print(
            f"  [dim]Skipping per-paper table in --mark-all mode "
            f"({len(arxiv_papers)} arXiv papers to queue).[/dim]"
        )

    if args.show_all and no_arxiv:
        console.print(f"\n[dim]Papers without arXiv IDs ({len(no_arxiv)}):[/dim]")
        for paper in no_arxiv[:20]:
            console.print(f"  [dim]• {(paper.get('title') or 'untitled')[:80]}[/dim]")
        if len(no_arxiv) > 20:
            console.print(f"  [dim]… and {len(no_arxiv) - 20} more[/dim]")

    if args.mark_all:
        if not arxiv_papers:
            console.print("[yellow]No citing papers with arXiv IDs found.[/yellow]")
            return
        console.print(
            f"\n[bold]Marking all {len(arxiv_papers)} citing paper(s) with arXiv IDs "
            "as manually important…[/bold]"
        )
        marked, examples = _mark_papers_as_important(arxiv_papers, seed_arxiv_id=seed_arxiv_id)
        _print_mark_summary(marked, examples)
        return

    if not candidates:
        console.print("[green]All arXiv-indexed citing papers are already processed.[/green]")
        return

    console.print(
        f"\n[bold]{len(candidates)}[/bold] unprocessed paper(s) available."
        f" Enter indices to mark as important (e.g. [bold]1 3 5[/bold]), "
        f"[bold]a[/bold] for all, or [bold]q[/bold] to quit:"
    )
    selected_ids = _pick_papers(candidates)
    if not selected_ids:
        console.print("[dim]No papers selected. Exiting.[/dim]")
        return

    marked, examples = _mark_papers_as_important(
        [paper for paper in candidates if paper["arxiv_id"] in selected_ids],
        seed_arxiv_id=seed_arxiv_id,
    )
    _print_mark_summary(marked, examples)


if __name__ == "__main__":
    main()
