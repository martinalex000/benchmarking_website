#!/usr/bin/env python3
"""Add one or more arXiv papers to the processing queue.

Examples::

    uv run python scripts/queue_paper.py 2206.08164
    uv run python scripts/queue_paper.py 2206.08164 2406.08993 --important
    uv run python scripts/queue_paper.py --file config/priority_papers.txt --important
    uv run python scripts/queue_paper.py export
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from pathlib import Path

from rich.console import Console

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.config import normalize_arxiv_id
from backend.db import init_db, session_scope
from backend.models import Paper, TodoPaper
from backend.todo_queue import add_todo_paper

console = Console()

_DEFAULT_LIST = Path(__file__).resolve().parent.parent / "config" / "priority_papers.txt"

_ARXIV_URL = re.compile(
    r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/([^/?#]+)(?:\.pdf)?/?$",
    re.IGNORECASE,
)


def normalize_input(value: str) -> str:
    """Normalize a bare arXiv ID or full abstract/PDF URL."""
    raw = value.strip()
    match = _ARXIV_URL.fullmatch(raw)
    if match:
        raw = match.group(1)
        if raw.lower().endswith(".pdf"):
            raw = raw[:-4]
    return normalize_arxiv_id(raw)


def read_arxiv_ids(path: Path) -> list[str]:
    """Read one arXiv ID or URL per line, allowing comments and blank lines."""
    values: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        value = raw_line.split("#", 1)[0].strip()
        if value:
            values.append(value)
    return values


def collect_arxiv_ids(values: Sequence[str], file_path: Path | None) -> list[str]:
    """Validate and de-duplicate all inputs before queueing anything."""
    raw_values = list(values)
    if file_path is not None:
        if not file_path.is_file():
            raise ValueError(f"File not found: {file_path}")
        raw_values.extend(read_arxiv_ids(file_path))

    if not raw_values:
        raise ValueError("Provide at least one arXiv ID or use --file")

    normalized: list[str] = []
    seen: set[str] = set()
    errors: list[str] = []
    for value in raw_values:
        try:
            arxiv_id = normalize_input(value)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if arxiv_id not in seen:
            seen.add(arxiv_id)
            normalized.append(arxiv_id)

    if errors:
        raise ValueError("\n".join(errors))
    return normalized


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


def export_queue_file(output: Path) -> int:
    """Write the current paper and manually important queues to a list file."""
    papers = _paper_rows()
    important = _important_rows()
    paper_ids = {arxiv_id for arxiv_id, _title in papers}

    lines = [
        "# Papers for queue_paper.py (one arXiv ID per line).",
        "# This file does not alter config/seed_data.yaml.",
        "#",
        "# Queue these papers with:",
        "#   uv run python scripts/queue_paper.py --file " f"{output} --important",
        "",
        "# --- papers table (benchmarks.db) ---",
    ]
    for arxiv_id, title in papers:
        suffix = f"  # {title}" if title else ""
        lines.append(f"{arxiv_id}{suffix}")

    lines.extend(["", "# --- manually important (todo_papers.is_manually_important) ---"])
    if important:
        if {arxiv_id for arxiv_id, _title in important}.issubset(paper_ids):
            lines.append("# Subset of the papers table; listed again for clarity.")
        for arxiv_id, title in important:
            suffix = f"  # {title}" if title else ""
            lines.append(f"{arxiv_id}{suffix}")
    else:
        lines.append("# (none)")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(papers) + len(important)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Add arXiv papers to the shared processing queue.",
        epilog=("Use 'export' to write the current database queues to " f"{_DEFAULT_LIST}."),
    )
    parser.add_argument("arxiv_ids", nargs="*", metavar="ARXIV_ID")
    parser.add_argument(
        "--file",
        type=Path,
        metavar="PATH",
        help="Read one arXiv ID per line; blank lines and # comments are ignored",
    )
    parser.add_argument(
        "--important",
        action="store_true",
        help="Prioritize these papers and requeue any with a terminal status",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and show papers without changing the queue",
    )
    return parser


def build_export_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export current queues to an arXiv list file.")
    parser.add_argument(
        "--output",
        type=Path,
        default=_DEFAULT_LIST,
        help=f"Output path (default: {_DEFAULT_LIST})",
    )
    return parser


def export_main(argv: Sequence[str]) -> int:
    args = build_export_parser().parse_args(argv)
    count = export_queue_file(args.output)
    console.print(f"[green]Wrote {count} row(s) to {args.output}[/green]")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments and arguments[0] == "export":
        return export_main(arguments[1:])

    parser = build_parser()
    args = parser.parse_args(arguments)
    try:
        arxiv_ids = collect_arxiv_ids(args.arxiv_ids, args.file)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    if args.dry_run:
        label = "important" if args.important else "normal priority"
        console.print(f"[bold]Would queue {len(arxiv_ids)} paper(s) ({label}):[/bold]")
        for arxiv_id in arxiv_ids:
            console.print(f"  {arxiv_id}")
        return 0

    counts = {"added": 0, "updated": 0, "unchanged": 0}
    for arxiv_id in arxiv_ids:
        _changed, message = add_todo_paper(
            arxiv_id,
            added_by="queue_paper.py",
            is_manually_important=args.important,
        )
        if message.startswith("Added"):
            counts["added"] += 1
            color = "green"
        elif message.startswith("Marked"):
            counts["updated"] += 1
            color = "green"
        else:
            counts["unchanged"] += 1
            color = "yellow"
        console.print(f"[{color}]{message}[/{color}]")

    console.print(
        f"\n[bold]Queued {len(arxiv_ids)} paper(s):[/bold] "
        f"{counts['added']} added, {counts['updated']} updated, "
        f"{counts['unchanged']} unchanged."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
