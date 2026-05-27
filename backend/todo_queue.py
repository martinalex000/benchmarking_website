"""Shared todo queue operations and CLI-facing helpers."""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from backend.db import init_db, session_scope
from backend.models import (
    TODO_PAPER_FILTER_VALUES,
    Paper,
    Result,
    TodoPaper,
    TodoPaperStatus,
    todo_paper_status_from_exit_code,
)


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class TodoQueueEntry:
    id: int
    arxiv_id: str
    title: str
    status: str
    attempts: int
    seen_count: int
    cited_by_count: int
    cites_existing_count: int
    reason: str
    last_attempt_at: str | None


@dataclass
class TodoQueueRunResult:
    returncode: int
    stdout: str = ""
    stderr: str = ""


@dataclass
class TodoQueueProcessItem:
    arxiv_id: str
    status: str
    note: str


@dataclass
class TodoQueueProcessSummary:
    total_selected: int
    counts: dict[str, int] = field(default_factory=lambda: {"done": 0, "rejected": 0, "failed": 0})
    items: list[TodoQueueProcessItem] = field(default_factory=list)
    refreshed_dev_exports: bool = False
    refresh_error: str | None = None


@dataclass
class TodoQueueReport:
    counts: dict[str, int]
    pending_rows: list[TodoQueueEntry]
    recent_rows: list[TodoQueueEntry]


def _row_to_entry(row: TodoPaper) -> TodoQueueEntry:
    return TodoQueueEntry(
        id=row.id,
        arxiv_id=row.arxiv_id,
        title=row.title or "",
        status=row.status or "",
        attempts=row.attempts or 0,
        seen_count=getattr(row, "seen_count", 0) or 0,
        cited_by_count=getattr(row, "cited_by_count", 0) or 0,
        cites_existing_count=getattr(row, "cites_existing_count", 0) or 0,
        reason=row.reason or "",
        last_attempt_at=row.last_attempt_at,
    )


def _normalize_status_filter(status: str | None) -> str | None:
    if status is None or status == "all":
        return None
    return status


def _tail_text(text: str, max_lines: int = 8) -> str:
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""
    return "\n".join(lines[-max_lines:])


def load_queue_entries(
    *,
    status: str | None = TodoPaperStatus.PENDING.value,
    limit: int = 0,
    max_attempts: int | None = None,
    order: str = "priority",
) -> list[TodoQueueEntry]:
    init_db()
    status_filter = _normalize_status_filter(status)

    with session_scope() as session:
        query = session.query(TodoPaper)
        if status_filter is not None:
            query = query.filter(TodoPaper.status == status_filter)
        if status_filter == TodoPaperStatus.PENDING.value and max_attempts is not None:
            query = query.filter(TodoPaper.attempts < max_attempts)

        if order == "priority":
            query = query.order_by(TodoPaper.seen_count.desc(), TodoPaper.created_at.asc())
        elif order == "recent":
            query = query.order_by(TodoPaper.created_at.desc())
        elif order == "last-attempt":
            query = query.order_by(TodoPaper.last_attempt_at.desc(), TodoPaper.created_at.desc())
        else:
            raise ValueError(f"Unsupported queue order: {order}")

        if limit:
            query = query.limit(limit)

        return [_row_to_entry(row) for row in query.all()]


def add_todo_paper(
    arxiv_id: str,
    *,
    title: str | None = None,
    reason: str | None = None,
    added_by: str | None = None,
) -> tuple[bool, str]:
    init_db()
    with session_scope() as session:
        existing = session.query(TodoPaper).filter_by(arxiv_id=arxiv_id).first()
        if existing:
            return False, f"Already in todo queue: {arxiv_id} (status={existing.status})"

        session.add(
            TodoPaper(
                arxiv_id=arxiv_id,
                title=title,
                reason=reason,
                added_by=added_by,
                status=TodoPaperStatus.PENDING.value,
                created_at=_utcnow_iso(),
            )
        )

    return True, f"Added {arxiv_id} to todo queue"


def build_queue_report(limit: int = 10, max_attempts: int = 3) -> TodoQueueReport:
    init_db()
    with session_scope() as session:
        rows = session.query(TodoPaper).all()
        counts: dict[str, int] = {status.value: 0 for status in TodoPaperStatus}
        for row in rows:
            key = row.status or TodoPaperStatus.PENDING.value
            counts[key] = counts.get(key, 0) + 1

        pending_rows = (
            session.query(TodoPaper)
            .filter(
                TodoPaper.status == TodoPaperStatus.PENDING.value,
                TodoPaper.attempts < max_attempts,
            )
            .order_by(TodoPaper.seen_count.desc(), TodoPaper.created_at.asc())
            .limit(limit)
            .all()
        )
        recent_rows = (
            session.query(TodoPaper)
            .filter(TodoPaper.status != TodoPaperStatus.PENDING.value)
            .order_by(TodoPaper.last_attempt_at.desc(), TodoPaper.created_at.desc())
            .limit(limit)
            .all()
        )

    return TodoQueueReport(
        counts=counts,
        pending_rows=[_row_to_entry(row) for row in pending_rows],
        recent_rows=[_row_to_entry(row) for row in recent_rows],
    )


def recompute_queue_counts() -> int:
    init_db()
    with session_scope() as session:
        todo_rows = session.query(TodoPaper).all()
        for todo in todo_rows:
            count = (
                session.query(Result)
                .join(Paper, Result.source_paper_id == Paper.id)
                .filter(Paper.arxiv_id == todo.arxiv_id)
                .count()
            )
            todo.cited_by_count = count
            todo.cites_existing_count = getattr(todo, "cites_existing_count", 0) or 0
        return len(todo_rows)


def run_manual_subprocess(arxiv_id: str, *, model: str, force: bool) -> TodoQueueRunResult:
    cmd = [
        sys.executable,
        str(Path(__file__).resolve().parents[1] / "scripts" / "run_manual.py"),
        arxiv_id,
        "--model",
        model,
    ]
    if force:
        cmd.append("--force")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return TodoQueueRunResult(
        returncode=result.returncode,
        stdout=result.stdout or "",
        stderr=result.stderr or "",
    )


def _mark_processing(todo_id: int) -> None:
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(id=todo_id).first()
        if row is None:
            return
        row.status = TodoPaperStatus.PROCESSING.value
        row.attempts = (row.attempts or 0) + 1
        row.last_attempt_at = _utcnow_iso()


def _finalize_todo(todo_id: int, status: TodoPaperStatus, note: str) -> None:
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(id=todo_id).first()
        if row is None:
            return
        row.status = status.value
        row.last_attempt_at = _utcnow_iso()
        row.note = note


def process_queue(
    *,
    limit: int = 5,
    model: str = "primary",
    force: bool = False,
    max_attempts: int = 3,
    dry_run: bool = False,
    refresh_dev_exports: bool = True,
    runner=run_manual_subprocess,
    on_start=None,
    on_finish=None,
) -> TodoQueueProcessSummary:
    selected = load_queue_entries(
        status=TodoPaperStatus.PENDING.value,
        limit=limit,
        max_attempts=max_attempts,
        order="priority",
    )
    summary = TodoQueueProcessSummary(total_selected=len(selected))

    if dry_run or not selected:
        return summary

    for index, entry in enumerate(selected, start=1):
        _mark_processing(entry.id)
        if on_start:
            on_start(entry, index, len(selected))

        try:
            result = runner(entry.arxiv_id, model=model, force=force)
            status = todo_paper_status_from_exit_code(result.returncode)
            excerpt = _tail_text(result.stderr or result.stdout)
            note = f"processed by todo_queue.py at {_utcnow_iso()}"
            if excerpt:
                note = f"{note}\n{excerpt}"
        except Exception as exc:  # pragma: no cover - defensive wrapper
            result = TodoQueueRunResult(returncode=1, stderr=str(exc))
            status = TodoPaperStatus.FAILED
            note = f"processed by todo_queue.py at {_utcnow_iso()}\n{exc}"

        _finalize_todo(entry.id, status, note)
        summary.counts[status.value] = summary.counts.get(status.value, 0) + 1
        summary.items.append(
            TodoQueueProcessItem(arxiv_id=entry.arxiv_id, status=status.value, note=note)
        )
        if on_finish:
            on_finish(entry, status.value, result, index, len(selected))

    if refresh_dev_exports:
        try:
            from backend.export_to_hugo import export_development_data

            export_development_data()
            summary.refreshed_dev_exports = True
        except Exception as exc:  # pragma: no cover - reporting should stay non-fatal
            summary.refresh_error = str(exc)

    return summary


__all__ = [
    "TODO_PAPER_FILTER_VALUES",
    "TodoQueueEntry",
    "TodoQueueProcessSummary",
    "TodoQueueReport",
    "TodoQueueRunResult",
    "add_todo_paper",
    "build_queue_report",
    "load_queue_entries",
    "process_queue",
    "recompute_queue_counts",
    "run_manual_subprocess",
]
