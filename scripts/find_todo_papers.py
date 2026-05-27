#!/usr/bin/env python3
"""Compatibility wrapper for the unified todo queue CLI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console

from backend.todo_queue import TODO_PAPER_FILTER_VALUES, add_todo_paper, recompute_queue_counts
from scripts.todo_queue import main as todo_queue_main

console = Console()


def cmd_add(
    arxiv_id: str,
    title: str | None,
    reason: str | None,
    added_by: str | None,
) -> None:
    created, message = add_todo_paper(
        arxiv_id,
        title=title,
        reason=reason,
        added_by=added_by,
    )
    color = "green" if created else "yellow"
    console.print(f"[{color}]{message}[/{color}]")


def cmd_list(status: str | None) -> None:
    argv = ["list"]
    if status:
        argv.extend(["--status", status])
    todo_queue_main(argv)


def cmd_process(limit: int, model: str, force: bool) -> None:
    argv = ["process", "--limit", str(limit), "--model", model]
    if force:
        argv.append("--force")
    todo_queue_main(argv)


def cmd_recompute_counts() -> None:
    updated = recompute_queue_counts()
    console.print(f"[green]Updated {updated} todo row(s).[/green]")


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage todo_papers queue")
    sub = parser.add_subparsers(dest="cmd")

    add_parser = sub.add_parser("add")
    add_parser.add_argument("arxiv_id")
    add_parser.add_argument("--title")
    add_parser.add_argument("--reason")
    add_parser.add_argument("--added-by")

    list_parser = sub.add_parser("list")
    list_parser.add_argument("--status", default="pending", choices=TODO_PAPER_FILTER_VALUES)

    process_parser = sub.add_parser("process")
    process_parser.add_argument("--limit", type=int, default=10)
    process_parser.add_argument("--model", default="primary")
    process_parser.add_argument("--force", action="store_true")

    sub.add_parser("recompute-counts")

    args = parser.parse_args()
    if args.cmd == "add":
        cmd_add(args.arxiv_id, args.title, args.reason, args.added_by)
    elif args.cmd == "list":
        cmd_list(args.status)
    elif args.cmd == "process":
        cmd_process(args.limit, args.model, args.force)
    elif args.cmd == "recompute-counts":
        cmd_recompute_counts()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
