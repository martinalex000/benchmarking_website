"""Shared todo queue operations and CLI-facing helpers."""

from __future__ import annotations

import logging
import re
import secrets
import subprocess
import sys
import threading
import time
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import case, func, or_
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
from backend.process_env import project_subprocess_env

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
    is_manually_important: bool = False


@dataclass(frozen=True)
class TodoQueueClaim:
    todo_id: int
    processing_token: str


@dataclass(frozen=True)
class TodoQueueRequeueResult:
    arxiv_id: str
    status: str | None
    changed: bool
    ok: bool
    message: str


_REQUEUEABLE_STATUSES = frozenset(
    {
        TodoPaperStatus.DONE.value,
        TodoPaperStatus.FAILED.value,
        TodoPaperStatus.REJECTED.value,
    }
)


def _priority_order(query):
    # Four fairness buckets: important first attempts, ordinary first attempts,
    # important retries, and ordinary retries. Attempts are then compared only
    # within a bucket so a retry cannot jump ahead of an untouched paper.
    importance = func.coalesce(TodoPaper.is_manually_important, 0)
    bucket = case(
        (
            (importance == 1) & (TodoPaper.attempts == 0),
            0,
        ),
        (
            (importance != 1) & (TodoPaper.attempts == 0),
            1,
        ),
        (importance == 1, 2),
        else_=3,
    )
    return query.order_by(
        bucket.asc(),
        TodoPaper.attempts.asc(),
        TodoPaper.seen_count.desc(),
        TodoPaper.created_at.asc(),
        TodoPaper.id.asc(),
    )


@dataclass
class TodoQueueRunResult:
    returncode: int
    stdout: str = ""
    stderr: str = ""
    retryable: bool = False
    failure_kind: str | None = None


@dataclass
class TodoQueueProcessItem:
    arxiv_id: str
    status: str
    note: str


@dataclass
class TodoQueueProcessSummary:
    total_selected: int
    counts: dict[str, int] = field(
        default_factory=lambda: {"pending": 0, "done": 0, "rejected": 0, "failed": 0}
    )
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
        is_manually_important=bool(getattr(row, "is_manually_important", 0)),
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


_RETRYABLE_FAILURE_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"\b(?:429|rate[- ]?limit|too many requests)\b", "rate_limited"),
    (r"\b(?:500|502|503|504)\b|internal server error|model not loaded", "endpoint_unavailable"),
    (r"timed? ?out|timeout|wall-clock limit", "timeout"),
    (
        r"connection (?:reset| refused|error)|temporarily unavailable|service unavailable",
        "transport",
    ),
    (r"no module named|import error|could not import", "runtime_environment"),
)


def _classify_retryable_output(result: TodoQueueRunResult) -> str | None:
    """Classify failures that should return to pending instead of terminal failed."""
    if result.returncode == 0 or result.returncode == 2 or result.retryable:
        return result.failure_kind or ("runner_retryable" if result.retryable else None)
    output = f"{result.stderr}\n{result.stdout}".casefold()
    for pattern, kind in _RETRYABLE_FAILURE_PATTERNS:
        if re.search(pattern, output, flags=re.IGNORECASE):
            return kind
    return None


def load_queue_entries(
    *,
    status: str | None = TodoPaperStatus.PENDING.value,
    limit: int = 0,
    order: str = "priority",
    important_only: bool = False,
) -> list[TodoQueueEntry]:
    init_db()
    status_filter = _normalize_status_filter(status)

    with session_scope() as session:
        query = session.query(TodoPaper)
        if status_filter is not None:
            query = query.filter(TodoPaper.status == status_filter)
        if important_only:
            query = query.filter(TodoPaper.is_manually_important == 1)

        if order == "priority":
            query = _priority_order(query)
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
    is_manually_important: bool = False,
    requeue: bool = False,
) -> tuple[bool, str]:
    init_db()
    with session_scope() as session:
        existing = session.query(TodoPaper).filter_by(arxiv_id=arxiv_id).first()
        if existing:
            if not is_manually_important:
                return False, f"Already in todo queue: {arxiv_id} (status={existing.status})"

            existing.is_manually_important = 1
            if title:
                existing.title = title
            if reason:
                existing.reason = reason
            if added_by:
                existing.added_by = added_by
            # Importance means the paper must be evaluated again, even when it
            # was already handled by the queue.  Keep ``requeue`` in the API
            # for callers that still pass it, but it is intentionally redundant.
            if existing.status in _REQUEUEABLE_STATUSES:
                existing.status = TodoPaperStatus.PENDING.value
                existing.attempts = 0
                existing.processing_token = None
            return True, f"Marked {arxiv_id} as manually important (status={existing.status})"

        session.add(
            TodoPaper(
                arxiv_id=arxiv_id,
                title=title,
                reason=reason,
                added_by=added_by,
                status=TodoPaperStatus.PENDING.value,
                is_manually_important=1 if is_manually_important else 0,
                created_at=_utcnow_iso(),
            )
        )

    suffix = " (manually important)" if is_manually_important else ""
    return True, f"Added {arxiv_id} to todo queue{suffix}"


def requeue_todo_papers(arxiv_ids: Iterable[str]) -> list[TodoQueueRequeueResult]:
    """Move existing terminal queue rows back to pending without changing importance."""
    ordered_ids = list(dict.fromkeys(arxiv_ids))
    if not ordered_ids:
        return []

    init_db()
    with session_scope() as session:
        rows = session.query(TodoPaper).filter(TodoPaper.arxiv_id.in_(ordered_ids)).all()
        rows_by_arxiv_id = {row.arxiv_id: row for row in rows}
        results: list[TodoQueueRequeueResult] = []

        for arxiv_id in ordered_ids:
            row = rows_by_arxiv_id.get(arxiv_id)
            if row is None:
                results.append(
                    TodoQueueRequeueResult(
                        arxiv_id=arxiv_id,
                        status=None,
                        changed=False,
                        ok=False,
                        message=f"Not in todo queue: {arxiv_id}",
                    )
                )
                continue

            if row.status in _REQUEUEABLE_STATUSES:
                row.status = TodoPaperStatus.PENDING.value
                row.attempts = 0
                results.append(
                    TodoQueueRequeueResult(
                        arxiv_id=arxiv_id,
                        status=row.status,
                        changed=True,
                        ok=True,
                        message=f"Requeued {arxiv_id} (status=pending, attempts=0)",
                    )
                )
            elif row.status == TodoPaperStatus.PENDING.value:
                results.append(
                    TodoQueueRequeueResult(
                        arxiv_id=arxiv_id,
                        status=row.status,
                        changed=False,
                        ok=True,
                        message=f"Already pending: {arxiv_id}",
                    )
                )
            elif row.status == TodoPaperStatus.PROCESSING.value:
                results.append(
                    TodoQueueRequeueResult(
                        arxiv_id=arxiv_id,
                        status=row.status,
                        changed=False,
                        ok=False,
                        message=f"Cannot requeue {arxiv_id} while it is processing",
                    )
                )
            else:
                results.append(
                    TodoQueueRequeueResult(
                        arxiv_id=arxiv_id,
                        status=row.status,
                        changed=False,
                        ok=False,
                        message=f"Cannot requeue {arxiv_id} (status={row.status})",
                    )
                )

    return results


def set_todo_paper_importance(
    arxiv_id: str,
    *,
    important: bool,
    requeue: bool = False,
) -> tuple[bool, str]:
    init_db()
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id=arxiv_id).first()
        if row is None:
            return False, f"Not in todo queue: {arxiv_id}"

        row.is_manually_important = 1 if important else 0
        # Marking a paper important always schedules a fresh evaluation.  The
        # ``requeue`` argument remains for backwards compatibility with older
        # callers, but is no longer required.
        if important and row.status in _REQUEUEABLE_STATUSES:
            row.status = TodoPaperStatus.PENDING.value
            row.attempts = 0
            row.processing_token = None

        action = "marked as manually important" if important else "unmarked as manually important"
        return True, f"{arxiv_id} {action} (status={row.status})"


def build_queue_report(limit: int = 10) -> TodoQueueReport:
    init_db()
    with session_scope() as session:
        rows = session.query(TodoPaper).all()
        counts: dict[str, int] = {status.value: 0 for status in TodoPaperStatus}
        for row in rows:
            key = row.status or TodoPaperStatus.PENDING.value
            counts[key] = counts.get(key, 0) + 1

        pending_rows = (
            _priority_order(
                session.query(TodoPaper).filter(
                    TodoPaper.status == TodoPaperStatus.PENDING.value,
                )
            )
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
    script_path = Path(__file__).resolve().with_name("paper_processor.py")
    if not script_path.exists():
        raise FileNotFoundError(f"paper_processor.py not found at expected path: {script_path}")
    cmd = [
        sys.executable,
        str(script_path),
        arxiv_id,
        "--model",
        model,
        "--skip-export",  # workers never trigger Hugo export; run export_to_hugo separately
        "--queue-managed",
    ]
    if force:
        cmd.append("--force")
    project_root = script_path.parents[1]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(project_root),
        env=project_subprocess_env(project_root),
    )
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
WORKER_HEARTBEAT_SECONDS = 60.0
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
        stale_query = session.query(TodoPaper).filter(
            TodoPaper.status == TodoPaperStatus.PROCESSING.value,
            or_(
                TodoPaper.last_attempt_at.is_(None),
                TodoPaper.last_attempt_at < cutoff,
            ),
        )
        return int(
            stale_query.update(
                {
                    TodoPaper.status: TodoPaperStatus.PENDING.value,
                    TodoPaper.processing_token: None,
                },
                synchronize_session=False,
            )
            or 0
        )


def count_pending_important() -> int:
    init_db()
    with session_scope() as session:
        return (
            session.query(TodoPaper)
            .filter(
                TodoPaper.status == TodoPaperStatus.PENDING.value,
                TodoPaper.is_manually_important == 1,
            )
            .count()
        )


def _claim_one_pending(*, important_only: bool = False) -> TodoQueueClaim | None:
    """Atomically claim the top-priority pending paper.

    Uses a raw SQL UPDATE with a WHERE status='pending' guard so that concurrent
    workers (multiple processes) cannot both claim the same paper.  SQLite
    serialises writes, so exactly one writer succeeds when two processes race.
    """
    engine = get_engine()
    now_iso = _utcnow_iso()
    processing_token = secrets.token_urlsafe(24)

    important_filter = " AND is_manually_important = 1" if important_only else ""

    with engine.connect() as conn:
        for _ in range(_CLAIM_RACE_RETRY_LIMIT):
            row = conn.execute(
                _sql_text(
                    "WITH candidate AS ("
                    "  SELECT id FROM todo_papers"
                    "  WHERE status = 'pending'"
                    f"{important_filter}"
                    "  ORDER BY "
                    "    CASE "
                    "      WHEN COALESCE(is_manually_important, 0) = 1 AND attempts = 0 THEN 0 "
                    "      WHEN COALESCE(is_manually_important, 0) != 1 AND attempts = 0 THEN 1 "
                    "      WHEN COALESCE(is_manually_important, 0) = 1 THEN 2 "
                    "      ELSE 3 "
                    "    END, attempts ASC, seen_count DESC, created_at ASC, id ASC"
                    "  LIMIT 1"
                    ") "
                    "UPDATE todo_papers "
                    "SET status = 'processing', attempts = attempts + 1, "
                    "last_attempt_at = :now, processing_token = :processing_token "
                    "WHERE id = (SELECT id FROM candidate) AND status = 'pending' "
                    "RETURNING id"
                ),
                {
                    "now": now_iso,
                    "processing_token": processing_token,
                },
            ).first()
            conn.commit()

            if row is not None:
                return TodoQueueClaim(
                    todo_id=int(row[0]),
                    processing_token=processing_token,
                )

        return None


def _has_pending_candidates(*, important_only: bool = False) -> bool:
    important_filter = " AND is_manually_important = 1" if important_only else ""
    engine = get_engine()
    with engine.connect() as conn:
        row = conn.execute(
            _sql_text(
                f"SELECT 1 FROM todo_papers WHERE status = 'pending'{important_filter} LIMIT 1"
            ),
            {},
        ).first()
    return row is not None


def _get_entry_by_id(todo_id: int) -> TodoQueueEntry | None:
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(id=todo_id).first()
        return _row_to_entry(row) if row else None


def _heartbeat_processing(todo_id: int, processing_token: str) -> bool:
    """Refresh a claim lease, returning false when ownership has been lost."""
    with session_scope() as session:
        row = (
            session.query(TodoPaper)
            .filter(
                TodoPaper.id == todo_id,
                TodoPaper.status == TodoPaperStatus.PROCESSING.value,
                TodoPaper.processing_token == processing_token,
            )
            .first()
        )
        if row is None:
            return False
        row.last_attempt_at = _utcnow_iso()
        return True


class _ProcessingLease:
    """Refresh a processing claim independently of runner output."""

    def __init__(self, todo_id: int, processing_token: str) -> None:
        self.todo_id = todo_id
        self.processing_token = processing_token
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None

    def __enter__(self) -> _ProcessingLease:
        self._thread = threading.Thread(
            target=self._run,
            name=f"todo-lease-{self.todo_id}",
            daemon=True,
        )
        self._thread.start()
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback) -> None:
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join(timeout=WORKER_HEARTBEAT_SECONDS)

    def _run(self) -> None:
        while not self._stop_event.wait(WORKER_HEARTBEAT_SECONDS):
            try:
                owns_lease = _heartbeat_processing(self.todo_id, self.processing_token)
            except Exception:  # pragma: no cover - defensive background-thread guard
                logger.exception(
                    "Failed to refresh processing lease for todo paper id=%s", self.todo_id
                )
                continue
            if not owns_lease:
                logger.warning("Lost processing lease for todo paper id=%s", self.todo_id)
                return


def _finalize_todo(
    todo_id: int,
    status: TodoPaperStatus,
    note: str,
    *,
    processing_token: str,
) -> bool:
    with session_scope() as session:
        row = (
            session.query(TodoPaper)
            .filter(
                TodoPaper.id == todo_id,
                TodoPaper.status == TodoPaperStatus.PROCESSING.value,
                TodoPaper.processing_token == processing_token,
            )
            .first()
        )
        if row is None:
            return False
        row.status = status.value
        row.last_attempt_at = _utcnow_iso()
        row.processing_token = None
        row.note = note
        return True


def mark_todo_paper_done(arxiv_id: str, note: str) -> bool:
    """Mark a todo paper done after a successful direct manual run."""
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id=arxiv_id).first()
        if row is None:
            return False
        row.status = TodoPaperStatus.DONE.value
        row.last_attempt_at = _utcnow_iso()
        row.processing_token = None
        row.note = note
        return True


def process_queue(
    *,
    limit: int = 5,
    model: str = "primary",
    force: bool = False,
    dry_run: bool = False,
    refresh_dev_exports: bool = True,
    important_only: bool = False,
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
            important_only=important_only,
        )
        summary.total_selected = len(selected)
        return summary

    processed_count = 0
    empty_retries = 0
    while processed_count < limit:
        # Atomically claim the next pending paper; safe across concurrent workers
        claim = _claim_one_pending(important_only=important_only)
        if claim is None:
            # Avoid false "queue empty" under high contention by retrying when
            # pending rows still exist but another worker won this instant.
            if empty_retries < _PROCESS_QUEUE_EMPTY_RETRIES and _has_pending_candidates(
                important_only=important_only
            ):
                empty_retries += 1
                time.sleep(_PROCESS_QUEUE_EMPTY_RETRY_SLEEP_S)
                continue
            break  # No more eligible pending papers

        empty_retries = 0

        entry = _get_entry_by_id(claim.todo_id)
        if entry is None:
            continue  # Shouldn't happen; skip defensively

        processed_count += 1
        summary.total_selected += 1

        if on_start:
            on_start(entry, processed_count, limit)

        with _ProcessingLease(entry.id, claim.processing_token):
            try:
                # Manually important papers are explicit requests for a fresh
                # evaluation, so they imply fresh extraction behavior.
                result = runner(
                    entry.arxiv_id,
                    model=model,
                    force=force or entry.is_manually_important,
                )
                failure_kind = _classify_retryable_output(result)
                status = (
                    TodoPaperStatus.PENDING
                    if failure_kind is not None
                    else todo_paper_status_from_exit_code(result.returncode)
                )
                excerpt = _tail_text(result.stderr or result.stdout)
                note = f"processed by todo_queue.py at {_utcnow_iso()}"
                if failure_kind:
                    note = f"{note}\nretryable failure: {failure_kind}"
                if excerpt:
                    note = f"{note}\n{excerpt}"
            except KeyboardInterrupt:
                raise
            except Exception as exc:  # pragma: no cover - defensive wrapper
                logger.exception("Todo queue runner failed for %s", entry.arxiv_id)
                result = TodoQueueRunResult(
                    returncode=1,
                    stderr=str(exc),
                    retryable=True,
                    failure_kind="runner_exception",
                )
                status = TodoPaperStatus.PENDING
                note = f"processed by todo_queue.py at {_utcnow_iso()}\n{type(exc).__name__}: {exc}"

            finalized = _finalize_todo(
                entry.id,
                status,
                note,
                processing_token=claim.processing_token,
            )

        if not finalized:
            logger.warning(
                "Skipping outcome for %s because its processing lease was lost", entry.arxiv_id
            )
            continue
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
    "WORKER_HEARTBEAT_SECONDS",
    "TodoQueueEntry",
    "TodoQueueClaim",
    "TodoQueueProcessSummary",
    "TodoQueueReport",
    "TodoQueueRequeueResult",
    "TodoQueueRunResult",
    "add_todo_paper",
    "build_queue_report",
    "count_pending_important",
    "load_queue_entries",
    "process_queue",
    "requeue_todo_papers",
    "recompute_queue_counts",
    "release_stale_processing_papers",
    "run_manual_subprocess",
    "set_todo_paper_importance",
]
