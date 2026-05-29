"""Shared todo queue operations and CLI-facing helpers."""

from __future__ import annotations

import logging
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import text as _sql_text

from backend.db import get_engine, init_db, session_scope
from backend.models import (
    TODO_PAPER_FILTER_VALUES,
    Paper,
    Result,
    TodoPaper,
    TodoPaperStatus,
    todo_paper_status_from_exit_code,
)

logger = logging.getLogger(__name__)


def _utcnow_iso() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


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
    script_path = Path(__file__).resolve().parents[1] / "scripts" / "run_manual.py"
    if not script_path.exists():
        raise FileNotFoundError(f"run_manual.py not found at expected path: {script_path}")
    cmd = [
        sys.executable,
        str(script_path),
        arxiv_id,
        "--model",
        model,
        "--skip-export",  # workers never trigger Hugo export; run export_to_hugo separately
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


WORKER_LOCK_TIMEOUT_MINUTES = 15
_CLAIM_RACE_RETRY_LIMIT = 24
_PROCESS_QUEUE_EMPTY_RETRIES = 8
_PROCESS_QUEUE_EMPTY_RETRY_SLEEP_S = 0.25


def release_stale_processing_papers(stale_minutes: int = WORKER_LOCK_TIMEOUT_MINUTES) -> int:
    """Reset 'processing' papers stuck longer than *stale_minutes* back to 'pending'.

    Call this at the start of each worker run so papers from crashed workers become
    available again for the next worker.

    Note: last_attempt_at is stored as ISO8601 string. String comparison works but is
    brittle; a cleaner fix would store as INTEGER UNIX epoch (requires DB migration).
    """
    from datetime import timedelta

    init_db()
    cutoff = (datetime.now(UTC) - timedelta(minutes=stale_minutes)).strftime("%Y-%m-%dT%H:%M:%SZ")
    with session_scope() as session:
        stale_rows = (
            session.query(TodoPaper)
            .filter(
                TodoPaper.status == TodoPaperStatus.PROCESSING.value,
                TodoPaper.last_attempt_at < cutoff,
            )
            .all()
        )
        for row in stale_rows:
            row.status = TodoPaperStatus.PENDING.value
        return len(stale_rows)


def _claim_one_pending(max_attempts: int) -> int | None:
    """Atomically claim the top-priority pending paper. Returns the claimed row ID or None.

    Uses a raw SQL UPDATE with a WHERE status='pending' guard so that concurrent
    workers (multiple processes) cannot both claim the same paper.  SQLite
    serialises writes, so exactly one writer succeeds when two processes race.
    """
    engine = get_engine()
    now_iso = _utcnow_iso()

    with engine.connect() as conn:
        for _ in range(_CLAIM_RACE_RETRY_LIMIT):
            row = conn.execute(
                _sql_text(
                    "WITH candidate AS ("
                    "  SELECT id FROM todo_papers"
                    "  WHERE status = 'pending' AND attempts < :max_attempts"
                    "  ORDER BY seen_count DESC, created_at ASC"
                    "  LIMIT 1"
                    ") "
                    "UPDATE todo_papers "
                    "SET status = 'processing', attempts = attempts + 1, last_attempt_at = :now "
                    "WHERE id = (SELECT id FROM candidate) AND status = 'pending' "
                    "RETURNING id"
                ),
                {"max_attempts": max_attempts, "now": now_iso},
            ).first()
            conn.commit()

            if row is not None:
                return int(row[0])

        return None


def _has_pending_candidates(max_attempts: int) -> bool:
    engine = get_engine()
    with engine.connect() as conn:
        row = conn.execute(
            _sql_text(
                "SELECT 1 FROM todo_papers"
                " WHERE status = 'pending' AND attempts < :max_attempts"
                " LIMIT 1"
            ),
            {"max_attempts": max_attempts},
        ).first()
    return row is not None


def _get_entry_by_id(todo_id: int) -> TodoQueueEntry | None:
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(id=todo_id).first()
        return _row_to_entry(row) if row else None


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
    init_db()

    # Release any papers stuck in 'processing' from crashed workers before selecting new ones
    release_stale_processing_papers()

    summary = TodoQueueProcessSummary(total_selected=0)

    if dry_run:
        selected = load_queue_entries(
            status=TodoPaperStatus.PENDING.value,
            limit=limit,
            max_attempts=max_attempts,
        )
        summary.total_selected = len(selected)
        return summary

    processed_count = 0
    empty_retries = 0
    while processed_count < limit:
        # Atomically claim the next pending paper; safe across concurrent workers
        candidate_id = _claim_one_pending(max_attempts)
        if candidate_id is None:
            # Avoid false "queue empty" under high contention by retrying when
            # pending rows still exist but another worker won this instant.
            if empty_retries < _PROCESS_QUEUE_EMPTY_RETRIES and _has_pending_candidates(
                max_attempts
            ):
                empty_retries += 1
                time.sleep(_PROCESS_QUEUE_EMPTY_RETRY_SLEEP_S)
                continue
            break  # No more eligible pending papers

        empty_retries = 0

        entry = _get_entry_by_id(candidate_id)
        if entry is None:
            continue  # Shouldn't happen; skip defensively

        processed_count += 1
        summary.total_selected += 1

        if on_start:
            on_start(entry, processed_count, limit)

        try:
            result = runner(entry.arxiv_id, model=model, force=force)
            status = todo_paper_status_from_exit_code(result.returncode)
            excerpt = _tail_text(result.stderr or result.stdout)
            note = f"processed by todo_queue.py at {_utcnow_iso()}"
            if excerpt:
                note = f"{note}\n{excerpt}"
        except KeyboardInterrupt:
            raise
        except Exception as exc:  # pragma: no cover - defensive wrapper
            logger.exception("Todo queue runner failed for %s", entry.arxiv_id)
            result = TodoQueueRunResult(returncode=1, stderr=str(exc))
            status = TodoPaperStatus.FAILED
            note = f"processed by todo_queue.py at {_utcnow_iso()}\n{type(exc).__name__}: {exc}"

        _finalize_todo(entry.id, status, note)
        summary.counts[status.value] = summary.counts.get(status.value, 0) + 1
        summary.items.append(
            TodoQueueProcessItem(arxiv_id=entry.arxiv_id, status=status.value, note=note)
        )
        if on_finish:
            on_finish(entry, status.value, result, processed_count, limit)

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
    "WORKER_LOCK_TIMEOUT_MINUTES",
    "TodoQueueEntry",
    "TodoQueueProcessSummary",
    "TodoQueueReport",
    "TodoQueueRunResult",
    "add_todo_paper",
    "build_queue_report",
    "load_queue_entries",
    "process_queue",
    "recompute_queue_counts",
    "release_stale_processing_papers",
    "run_manual_subprocess",
]
