#!/usr/bin/env python3
"""Mark papers from a list file as manually important in todo_papers.

Reads ``config/priority_papers.txt`` (one arXiv ID per line; ``#`` starts a
comment). Papers are enqueued when missing and flagged ``is_manually_important``
so workers process them before higher ``seen_count`` queue entries.

This does not touch ``config/seed_data.yaml`` or normal database seeding.

Usage::

    uv run python scripts/mark_priority_papers.py mark
    uv run python scripts/mark_priority_papers.py mark --requeue
    uv run python scripts/mark_priority_papers.py mark --dry-run
    uv run python scripts/mark_priority_papers.py export
    uv run python scripts/mark_priority_papers.py export --output path/to/list.txt
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rich.console import Console
from rich.table import Table

from backend.config import normalize_arxiv_id
from backend.db import init_db, session_scope
from backend.models import Paper, TodoPaper
from backend.todo_queue import add_todo_paper

console = Console()

_DEFAULT_LIST = Path(__file__).resolve().parent.parent / "config" / "priority_papers.txt"
_ARXIV_LINE = re.compile(r"^([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)\b")


def parse_priority_file(path: Path) -> list[str]:
    """Return de-duplicated arXiv IDs in file order."""
    seen: set[str] = set()
    ordered: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        match = _ARXIV_LINE.match(line)
        if not match:
            continue
        arxiv_id = normalize_arxiv_id(match.group(1))
        if arxiv_id in seen:
            continue
        seen.add(arxiv_id)
        ordered.append(arxiv_id)
    return ordered


def _paper_rows() -> list[tuple[str, str]]:
    init_db()
    with session_scope() as session:
        return [
            (row.arxiv_id, row.title or "")
            for row in session.query(Paper).order_by(Paper.arxiv_id).all()
            if row.arxiv_id
        ]


def _important_rows() -> list[tuple[str, str]]:
    init_db()
    with session_scope() as session:
        return [
            (row.arxiv_id, row.title or "")
            for row in session.query(TodoPaper)
            .filter(TodoPaper.is_manually_important == 1)
            .order_by(TodoPaper.arxiv_id)
            .all()
            if row.arxiv_id
        ]


def export_priority_file(output: Path) -> int:
    """Write priority list from current DB state."""
    papers = _paper_rows()
    important = _important_rows()
    important_ids = {arxiv_id for arxiv_id, _title in important}

    lines = [
        "# Priority papers for todo_queue processing (one arXiv ID per line).",
        "# Used by scripts/mark_priority_papers.py — does not alter config/seed_data.yaml.",
        "#",
        "# Regenerate from the DB with:",
        "#   uv run python scripts/mark_priority_papers.py export",
        "",
        "# --- papers table (benchmarks.db) ---",
    ]
    for arxiv_id, title in papers:
        suffix = f"  # {title}" if title else ""
        lines.append(f"{arxiv_id}{suffix}")

    lines.extend(
        [
            "",
            "# --- manually important (todo_papers.is_manually_important) ---",
        ]
    )
    if important:
        if important_ids.issubset({arxiv_id for arxiv_id, _ in papers}):
            lines.append("# Subset of the seed benchmark source papers; listed again for clarity.")
        for arxiv_id, title in important:
            suffix = f"  # {title}" if title else ""
            lines.append(f"{arxiv_id}{suffix}")
    else:
        lines.append("# (none)")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(papers) + len(important)


def cmd_export(args: argparse.Namespace) -> None:
    output = Path(args.output)
    count = export_priority_file(output)
    console.print(f"[green]Wrote {count} row(s) to {output}[/green]")


def cmd_mark(args: argparse.Namespace) -> None:
    list_path = Path(args.file)
    if not list_path.is_file():
        console.print(f"[red]Priority list not found: {list_path}[/red]")
        sys.exit(1)

    arxiv_ids = parse_priority_file(list_path)
    if not arxiv_ids:
        console.print(f"[yellow]No arXiv IDs found in {list_path}[/yellow]")
        return

    if args.dry_run:
        table = Table(show_header=True, header_style="bold", title="Would mark important")
        table.add_column("#", style="dim", justify="right")
        table.add_column("arXiv", style="cyan")
        for index, arxiv_id in enumerate(arxiv_ids, start=1):
            table.add_row(str(index), arxiv_id)
        console.print(table)
        console.print(f"\n[dim]Dry-run — {len(arxiv_ids)} paper(s); nothing changed.[/dim]")
        return

    created = 0
    updated = 0
    for arxiv_id in arxiv_ids:
        was_created, message = add_todo_paper(
            arxiv_id,
            reason="priority_papers.txt",
            added_by="mark_priority_papers.py",
            is_manually_important=True,
            requeue=args.requeue,
        )
        if was_created and "Added" in message:
            created += 1
        else:
            updated += 1
        console.print(message)

    console.print(
        f"\n[green]Marked {len(arxiv_ids)} paper(s) important "
        f"({created} added, {updated} updated).[/green]"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mark priority papers as manually important in todo_papers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    mark_parser = sub.add_parser(
        "mark",
        help="Read the priority list and mark each paper important",
    )
    mark_parser.add_argument(
        "--file",
        type=Path,
        default=_DEFAULT_LIST,
        help=f"Priority list path (default: {_DEFAULT_LIST})",
    )
    mark_parser.add_argument(
        "--requeue",
        action="store_true",
        help="Reset done/failed/rejected rows back to pending",
    )
    mark_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be marked without changing the DB",
    )

    export_parser = sub.add_parser(
        "export",
        help="Write priority list from papers + manually important todo rows",
    )
    export_parser.add_argument(
        "--output",
        type=Path,
        default=_DEFAULT_LIST,
        help=f"Output path (default: {_DEFAULT_LIST})",
    )

    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    if args.command == "mark":
        cmd_mark(args)
    elif args.command == "export":
        cmd_export(args)
    else:
        raise SystemExit(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
