#!/usr/bin/env python3
"""Manage a simple todo queue of arXiv papers.

Commands:
  add <arxiv_id> [--title TITLE] [--reason REASON] [--added-by NAME]
  list [--status pending|processing|done|failed|all]
  process [--limit N] [--model primary] [--force]

The `process` command will call `run_manual.py` for each pending entry and
update the `todo_papers` table with success/failure state.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.db import init_db, session_scope
from backend.models import TodoPaper, Paper, Result
from rich.console import Console
from rich.table import Table

console = Console()


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cmd_add(arxiv_id: str, title: str | None, reason: str | None, added_by: str | None) -> None:
    init_db()
    with session_scope() as session:
        existing = session.query(TodoPaper).filter_by(arxiv_id=arxiv_id).first()
        if existing:
            console.print(
                f"[yellow]Already in todo queue:[/yellow] {arxiv_id} (status={existing.status})"
            )
            return

        tp = TodoPaper(
            arxiv_id=arxiv_id,
            title=title,
            reason=reason,
            added_by=added_by,
            status="pending",
            created_at=_utcnow_iso(),
        )
        session.add(tp)
    console.print(f"[green]Added[/green] {arxiv_id} to todo queue")


def cmd_list(status: str | None) -> None:
    init_db()
    with session_scope() as session:
        q = session.query(TodoPaper)
        if status and status != "all":
            q = q.filter_by(status=status)
        rows: List[TodoPaper] = q.order_by(TodoPaper.created_at.desc()).all()

    table = Table(show_header=True, header_style="bold")
    table.add_column("id", width=4)
    table.add_column("arXiv", style="cyan", width=13)
    table.add_column("status", width=10)
    table.add_column("attempts", width=8)
    table.add_column("cited_by", width=10)
    table.add_column("cites_existing", width=12)
    table.add_column("reason")

    for r in rows:
        table.add_row(
            str(r.id),
            r.arxiv_id,
            r.status or "",
            str(r.attempts or 0),
            str(getattr(r, "cited_by_count", 0)),
            str(getattr(r, "cites_existing_count", 0)),
            r.reason or "",
        )

    console.print(table)


def _run_manual_for(arxiv_id: str, run_args: List[str]) -> int:
    cmd = [sys.executable, str(Path(__file__).parent / "run_manual.py"), arxiv_id]
    cmd += run_args
    console.rule(f"Processing {arxiv_id}")
    proc = subprocess.run(cmd)
    return proc.returncode


def cmd_process(limit: int, model: str, force: bool) -> None:
    init_db()
    run_args = ["--model", model]
    if force:
        run_args.append("--force")

    with session_scope() as session:
        pending = (
            session.query(TodoPaper)
            .filter_by(status="pending")
            .order_by(TodoPaper.created_at.asc())
            .limit(limit)
            .all()
        )

        if not pending:
            console.print("[green]No pending todo papers.[/green]")
            return

        for tp in pending:
            tp.status = "processing"
            tp.attempts = (tp.attempts or 0) + 1
            tp.last_attempt_at = _utcnow_iso()
            session.commit()

            rc = _run_manual_for(tp.arxiv_id, run_args)

            with session_scope() as s2:
                row = s2.query(TodoPaper).get(tp.id)
                if rc == 0:
                    row.status = "done"
                else:
                    row.status = "failed"
                row.last_attempt_at = _utcnow_iso()

    console.print("[green]Processing complete.[/green]")


def cmd_recompute_counts() -> None:
    """Recompute `cited_by_count` for todo entries from existing `results` records.

    `cited_by_count` is computed as the number of `Result` rows whose
    `source_paper` has an `arxiv_id` equal to the todo entry's arXiv ID.
    `cites_existing_count` is left as 0 by default; a future enhancement can
    query Semantic Scholar for references and match against our `papers`.
    """
    init_db()
    console.print("Recomputing todo_papers counters…")
    with session_scope() as session:
        todo_rows = session.query(TodoPaper).all()
        for tp in todo_rows:
            # count results where source_paper.arxiv_id == tp.arxiv_id
            count = (
                session.query(Result)
                .join(Paper, Result.source_paper_id == Paper.id)
                .filter(Paper.arxiv_id == tp.arxiv_id)
                .count()
            )
            tp.cited_by_count = count
            tp.cites_existing_count = getattr(tp, "cites_existing_count", 0) or 0
        console.print(f"Updated {len(todo_rows)} todo rows")


def main() -> None:
    p = argparse.ArgumentParser(description="Manage todo_papers queue")
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser("add")
    a.add_argument("arxiv_id")
    a.add_argument("--title")
    a.add_argument("--reason")
    a.add_argument("--added-by")

    l = sub.add_parser("list")
    l.add_argument("--status", default="pending", help="pending|processing|done|failed|all")

    pr = sub.add_parser("process")
    pr.add_argument("--limit", type=int, default=10)
    pr.add_argument("--model", default="primary")
    pr.add_argument("--force", action="store_true")

    args = p.parse_args()

    if args.cmd == "add":
        cmd_add(args.arxiv_id, args.title, args.reason, args.added_by)
    elif args.cmd == "list":
        cmd_list(args.status)
    elif args.cmd == "process":
        cmd_process(args.limit, args.model, args.force)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
