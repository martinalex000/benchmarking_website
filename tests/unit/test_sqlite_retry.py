"""Tests for shared SQLite lock retry helpers."""

from __future__ import annotations

import sqlite3

from sqlalchemy import text

from backend.db import init_db, session_scope
from backend.sqlite_retry import commit_with_sqlite_retry, run_db_transaction


def test_run_db_transaction_retries_on_database_locked(monkeypatch):
    conn = sqlite3.connect(":memory:")
    attempts = {"count": 0}

    def _write(cur: sqlite3.Cursor) -> None:
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise sqlite3.OperationalError("database is locked")
        cur.execute("CREATE TABLE IF NOT EXISTS lock_retry_test (id INTEGER PRIMARY KEY)")

    monkeypatch.setattr("backend.sqlite_retry.time.sleep", lambda _seconds: None)
    run_db_transaction(conn, _write, max_retries=5)

    assert attempts["count"] == 3


def test_session_scope_retries_commit_on_database_locked(monkeypatch, tmp_path):
    db_path = tmp_path / "retry.db"
    init_db(str(db_path))
    attempts = {"count": 0}

    def _patched_commit_with_retry(commit, *, max_retries=12):
        def _commit_wrapper() -> None:
            attempts["count"] += 1
            if attempts["count"] < 3:
                raise sqlite3.OperationalError("database is locked")
            commit()

        return commit_with_sqlite_retry(_commit_wrapper, max_retries=max_retries)

    monkeypatch.setattr("backend.db.commit_with_sqlite_retry", _patched_commit_with_retry)
    monkeypatch.setattr("backend.sqlite_retry.time.sleep", lambda _seconds: None)

    with session_scope() as session:
        session.execute(
            text(
                "CREATE TABLE IF NOT EXISTS session_retry_test "
                "(id INTEGER PRIMARY KEY, label TEXT NOT NULL)"
            )
        )
        session.execute(
            text("INSERT INTO session_retry_test(id, label) VALUES (1, 'ok')"),
        )

    assert attempts["count"] == 3

    with session_scope() as session:
        row = session.execute(text("SELECT label FROM session_retry_test WHERE id = 1")).first()
    assert row is not None
    assert row[0] == "ok"
