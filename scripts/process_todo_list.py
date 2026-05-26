#!/usr/bin/env python3
"""process_todo_list.py — batch-process papers from the todo_papers queue.

Reads papers from todo_papers WHERE status='pending', ordered by seen_count DESC,
and runs run_manual.py on each.  Updates the todo row with the outcome:
  • 'done'      — extraction succeeded
  • 'rejected'  — stage-1 or stage-2 screening rejected the paper
  • 'failed'    — run_manual exited with an error; attempts counter incremented

Usage::
    uv run python scripts/process_todo_list.py
    uv run python scripts/process_todo_list.py --limit 10
    uv run python scripts/process_todo_list.py --model primary --limit 5
    uv run python scripts/process_todo_list.py --dry-run          # show queue only
    uv run python scripts/process_todo_list.py --max-attempts 3   # skip if attempts >= N
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich import box
from rich.console import Console
from rich.table import Table

console = Console()


def _utcnow() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


def _load_queue(limit: int, max_attempts: int) -> list:
    from backend.db import init_db, session_scope
    from backend.models import TodoPaper, TodoPaperStatus

    init_db()
    with session_scope() as session:
        q = (
            session.query(TodoPaper)
            .filter(
                TodoPaper.status == TodoPaperStatus.PENDING.value,
                TodoPaper.attempts < max_attempts,
            )
            .order_by(TodoPaper.seen_count.desc(), TodoPaper.created_at.asc())
        )
        if limit:
            q = q.limit(limit)
        rows = q.all()
        # Detach from session so we can use them after the session closes.
        return [
            {
                "id": r.id,
                "arxiv_id": r.arxiv_id,
                "title": r.title or "",
                "attempts": r.attempts,
                "seen_count": r.seen_count,
            }
            for r in rows
        ]


def _mark_todo(todo_id: int, status: str, note: str | None = None) -> None:
    from backend.db import session_scope
    from backend.models import TodoPaper, TodoPaperStatus

    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(id=todo_id).first()
        if row is None:
            return
        if status == TodoPaperStatus.FAILED.value:
            row.attempts = (row.attempts or 0) + 1
        else:
            row.status = status
        row.last_attempt_at = _utcnow()
        if note:
            row.note = note


def _run_paper(arxiv_id: str, model: str, dry_run: bool) -> str:
    """Run run_manual on a single paper. Returns 'done', 'rejected', or 'failed'."""
    from backend.models import todo_paper_status_from_exit_code

    cmd = [
        sys.executable,
        str(Path(__file__).parent / "run_manual.py"),
        arxiv_id,
        "--model",
        model,
    ]
    if dry_run:
        console.print(f"  [dim][dry-run] would run: {' '.join(cmd)}[/dim]")
        return "dry-run"

    result = subprocess.run(cmd, capture_output=False)
    return todo_paper_status_from_exit_code(result.returncode).value


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch-process the todo_papers queue.")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        metavar="N",
        help="Maximum number of papers to process (0 = unlimited)",
    )
    parser.add_argument(
        "--model",
        default="primary",
        metavar="TIER",
        help="Model tier to use (primary/fallback/small or an explicit model name)",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=3,
        metavar="N",
        help="Skip papers that have already failed this many times (default: 3)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the queue and commands without running anything",
    )
    args = parser.parse_args()

    queue = _load_queue(limit=args.limit, max_attempts=args.max_attempts)

    if not queue:
        console.print(
            "[green]Todo queue is empty (or all remaining papers exceeded max-attempts).[/green]"
        )
        return

    # ── Show queue ────────────────────────────────────────────────────────
    table = Table(show_header=True, header_style="bold", box=box.SIMPLE, show_edge=False)
    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("arXiv ID", style="cyan", width=13)
    table.add_column("Seen", justify="right", width=6)
    table.add_column("Tries", justify="right", width=6)
    table.add_column("Title")

    for i, p in enumerate(queue, 1):
        title = p["title"]
        if len(title) > 72:
            title = title[:69] + "…"
        table.add_row(str(i), p["arxiv_id"], str(p["seen_count"]), str(p["attempts"]), title)

    console.print(
        f"\n[bold]{len(queue)}[/bold] paper(s) queued (model=[cyan]{args.model}[/cyan]):\n"
    )
    console.print(table)

    if args.dry_run:
        console.print("\n[dim]Dry-run mode — no papers were processed.[/dim]")
        return

    # ── Process ───────────────────────────────────────────────────────────
    counts = {"done": 0, "rejected": 0, "failed": 0}

    for i, paper in enumerate(queue, 1):
        aid = paper["arxiv_id"]
        console.rule(f"[bold]({i}/{len(queue)}) arXiv:{aid}[/bold]")

        outcome = _run_paper(aid, model=args.model, dry_run=False)
        counts[outcome] = counts.get(outcome, 0) + 1

        _mark_todo(
            todo_id=paper["id"],
            status=outcome,
            note=f"processed by process_todo_list.py at {_utcnow().isoformat(timespec='seconds')}",
        )

        status_color = {"done": "green", "rejected": "yellow", "failed": "red"}.get(outcome, "dim")
        console.print(f"  → [{status_color}]{outcome}[/{status_color}]")

    # ── Summary ───────────────────────────────────────────────────────────
    console.rule("[bold]Summary[/bold]")
    console.print(
        f"  [green]{counts['done']}[/green] done   "
        f"[yellow]{counts['rejected']}[/yellow] rejected   "
        f"[red]{counts['failed']}[/red] failed"
    )

    # Re-export dev pages so todo list reflects updated statuses
    console.print("\n[dim]Refreshing dev pages…[/dim]")
    try:
        from backend.export_to_hugo import export_development_data

        export_development_data()
    except Exception as exc:
        console.print(f"  [yellow]Dev page export failed: {exc}[/yellow]")

    console.rule("[green]Done[/green]")


if __name__ == "__main__":
    main()
