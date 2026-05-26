#!/usr/bin/env python3
"""Unified user-facing todo queue interface.

Default behavior with no subcommand: process the next few pending papers.
"""

from __future__ import annotations

import argparse

from rich import box
from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table

from backend.models import TODO_PAPER_FILTER_VALUES, TodoPaperStatus
from backend.todo_queue import (
    add_todo_paper,
    build_queue_report,
    load_queue_entries,
    process_queue,
    recompute_queue_counts,
)

console = Console()


def _truncate(text: str, limit: int = 72) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def _render_queue_table(rows, *, title: str) -> None:
    table = Table(
        show_header=True,
        header_style="bold",
        box=box.SIMPLE,
        show_edge=False,
        title=title,
    )
    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("arXiv", style="cyan", width=13)
    table.add_column("Status", width=10)
    table.add_column("Seen", justify="right", width=6)
    table.add_column("Tries", justify="right", width=6)
    table.add_column("Title")

    for index, row in enumerate(rows, start=1):
        table.add_row(
            str(index),
            row.arxiv_id,
            row.status,
            str(row.seen_count),
            str(row.attempts),
            _truncate(row.title),
        )

    console.print(table)


def cmd_process(args: argparse.Namespace) -> None:
    selected = load_queue_entries(
        status=TodoPaperStatus.PENDING.value,
        limit=args.limit,
        max_attempts=args.max_attempts,
        order="priority",
    )
    if not selected:
        console.print("[green]No pending todo papers are ready to process.[/green]")
        return

    _render_queue_table(selected, title="Pending queue")

    if args.dry_run:
        console.print("\n[dim]Dry-run mode — nothing was processed.[/dim]")
        return

    failures: list[tuple[str, str, str]] = []
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        console=console,
    )

    with progress:
        task_id = progress.add_task("Processing todo queue", total=len(selected))

        def on_start(entry, index, total):
            progress.update(
                task_id,
                description=f"Processing {entry.arxiv_id} ({index}/{total})",
            )

        def on_finish(entry, status, result, index, total):
            progress.advance(task_id, 1)
            if status != TodoPaperStatus.DONE.value:
                excerpt = result.stderr or result.stdout or "no output captured"
                failures.append(
                    (entry.arxiv_id, status, _truncate(excerpt.replace("\n", " | "), 120))
                )

        summary = process_queue(
            limit=args.limit,
            model=args.model,
            force=args.force,
            max_attempts=args.max_attempts,
            dry_run=False,
            refresh_dev_exports=not args.no_export,
            on_start=on_start,
            on_finish=on_finish,
        )

    console.print(
        "\n"
        f"[green]{summary.counts['done']} done[/green]  "
        f"[yellow]{summary.counts['rejected']} rejected[/yellow]  "
        f"[red]{summary.counts['failed']} failed[/red]"
    )
    if summary.refreshed_dev_exports:
        console.print("[dim]Development exports refreshed.[/dim]")
    elif summary.refresh_error:
        console.print(
            f"[yellow]Development export refresh failed: {summary.refresh_error}[/yellow]"
        )

    if failures:
        table = Table(
            show_header=True,
            header_style="bold",
            box=box.SIMPLE,
            show_edge=False,
            title="Non-success outcomes",
        )
        table.add_column("arXiv", style="cyan", width=13)
        table.add_column("Status", width=10)
        table.add_column("Excerpt")
        for arxiv_id, status, excerpt in failures:
            table.add_row(arxiv_id, status, excerpt)
        console.print(table)


def cmd_report(args: argparse.Namespace) -> None:
    report = build_queue_report(limit=args.limit, max_attempts=args.max_attempts)
    console.print(
        f"[bold]Todo queue[/bold]  pending={report.counts.get('pending', 0)}  "
        f"processing={report.counts.get('processing', 0)}  done={report.counts.get('done', 0)}  "
        f"rejected={report.counts.get('rejected', 0)}  failed={report.counts.get('failed', 0)}"
    )
    console.print()

    if report.pending_rows:
        _render_queue_table(report.pending_rows, title="Top pending papers")
    else:
        console.print("[dim]No pending papers ready to process.[/dim]")

    if report.recent_rows:
        _render_queue_table(report.recent_rows, title="Recent queue outcomes")


def cmd_list(args: argparse.Namespace) -> None:
    rows = load_queue_entries(status=args.status, limit=args.limit, order=args.order)
    if not rows:
        console.print("[dim]No matching todo queue rows.[/dim]")
        return
    _render_queue_table(rows, title=f"Todo queue ({args.status})")


def cmd_add(args: argparse.Namespace) -> None:
    created, message = add_todo_paper(
        args.arxiv_id,
        title=args.title,
        reason=args.reason,
        added_by=args.added_by,
    )
    color = "green" if created else "yellow"
    console.print(f"[{color}]{message}[/{color}]")


def cmd_recompute_counts(_args: argparse.Namespace) -> None:
    updated = recompute_queue_counts()
    console.print(f"[green]Updated {updated} todo row(s).[/green]")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Unified todo_papers queue interface")
    sub = parser.add_subparsers(dest="command")

    process_parser = sub.add_parser("process", help="Process the next pending papers")
    process_parser.add_argument("--limit", type=int, default=5, metavar="N")
    process_parser.add_argument("--model", default="primary", metavar="TIER")
    process_parser.add_argument("--force", action="store_true")
    process_parser.add_argument("--max-attempts", type=int, default=3, metavar="N")
    process_parser.add_argument("--dry-run", action="store_true")
    process_parser.add_argument("--no-export", action="store_true")

    report_parser = sub.add_parser("report", help="Show queue summary and top pending papers")
    report_parser.add_argument("--limit", type=int, default=10, metavar="N")
    report_parser.add_argument("--max-attempts", type=int, default=3, metavar="N")

    list_parser = sub.add_parser("list", help="Show raw queue rows")
    list_parser.add_argument("--status", default="all", choices=TODO_PAPER_FILTER_VALUES)
    list_parser.add_argument("--limit", type=int, default=25, metavar="N")
    list_parser.add_argument(
        "--order", default="priority", choices=("priority", "recent", "last-attempt")
    )

    add_parser = sub.add_parser("add", help="Add a paper to the queue")
    add_parser.add_argument("arxiv_id")
    add_parser.add_argument("--title")
    add_parser.add_argument("--reason")
    add_parser.add_argument("--added-by")

    sub.add_parser("recompute-counts", help="Recompute queue citation counters")

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    command = args.command or "process"

    if command == "process":
        cmd_process(args)
    elif command == "report":
        cmd_report(args)
    elif command == "list":
        cmd_list(args)
    elif command == "add":
        cmd_add(args)
    elif command == "recompute-counts":
        cmd_recompute_counts(args)
    else:
        parser.error(f"Unsupported command: {command}")


if __name__ == "__main__":
    main()
