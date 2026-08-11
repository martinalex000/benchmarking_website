"""Shared SQLite lock-contention helpers."""

from __future__ import annotations

import logging
import sqlite3
import time
from collections.abc import Callable
from contextlib import suppress

logger = logging.getLogger(__name__)

DB_LOCK_RETRY_LIMIT = 12
DB_LOCK_RETRY_BASE_SLEEP_S = 0.25
DB_BUSY_TIMEOUT_MS = 60_000


def is_sqlite_lock_error(exc: BaseException) -> bool:
    if isinstance(exc, sqlite3.OperationalError):
        message = str(exc).casefold()
        return "locked" in message or "busy" in message

    orig = getattr(exc, "orig", None)
    if isinstance(orig, sqlite3.OperationalError):
        message = str(orig).casefold()
        return "locked" in message or "busy" in message
    return False


def configure_sqlite_connection(
    conn: sqlite3.Connection,
    *,
    busy_timeout_ms: int = DB_BUSY_TIMEOUT_MS,
) -> None:
    conn.execute(f"PRAGMA busy_timeout = {busy_timeout_ms}")
    conn.execute("PRAGMA foreign_keys = ON")


def run_db_transaction(
    conn: sqlite3.Connection,
    fn: Callable[[sqlite3.Cursor], None],
    *,
    max_retries: int = DB_LOCK_RETRY_LIMIT,
) -> None:
    """Run a write transaction, retrying when SQLite reports lock contention."""
    for attempt in range(max_retries):
        try:
            cur = conn.cursor()
            fn(cur)
            conn.commit()
            return
        except sqlite3.OperationalError as exc:
            if not is_sqlite_lock_error(exc):
                raise
            with suppress(sqlite3.Error):
                conn.rollback()
            if attempt + 1 >= max_retries:
                raise
            wait = DB_LOCK_RETRY_BASE_SLEEP_S * (2**attempt)
            logger.warning(
                "SQLite database locked — retrying in %.2fs (attempt %d/%d)",
                wait,
                attempt + 1,
                max_retries,
            )
            time.sleep(wait)


def commit_with_sqlite_retry(
    commit: Callable[[], None],
    *,
    max_retries: int = DB_LOCK_RETRY_LIMIT,
) -> None:
    """Retry a commit callback when SQLite reports lock contention."""
    for attempt in range(max_retries):
        try:
            commit()
            return
        except Exception as exc:
            if not is_sqlite_lock_error(exc) or attempt + 1 >= max_retries:
                raise
            wait = DB_LOCK_RETRY_BASE_SLEEP_S * (2**attempt)
            logger.warning(
                "SQLite database locked during commit — retrying in %.2fs (attempt %d/%d)",
                wait,
                attempt + 1,
                max_retries,
            )
            time.sleep(wait)
