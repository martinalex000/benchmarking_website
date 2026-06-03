"""Tests for benchmarks.db WAL checkpoint helpers and pre-commit guard."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from backend.benchmarks_db_checkpoint import (
    is_benchmarks_db_sidecar,
    sidecar_paths,
    wal_checkpoint_truncate,
)


def test_is_benchmarks_db_sidecar():
    assert not is_benchmarks_db_sidecar("data/benchmarks.db")
    assert is_benchmarks_db_sidecar("data/benchmarks.db-wal")
    assert is_benchmarks_db_sidecar("data/benchmarks.db-shm")
    assert is_benchmarks_db_sidecar("data/benchmarks.db-wal.bak")
    assert not is_benchmarks_db_sidecar("data/other.db-wal")


def test_wal_checkpoint_truncate_merges_and_clears_sidecars(tmp_path: Path):
    db_path = tmp_path / "benchmarks.db"
    holder = sqlite3.connect(db_path)
    holder.execute("PRAGMA journal_mode=WAL")
    holder.execute("PRAGMA wal_autocheckpoint=0")
    holder.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")
    holder.execute("INSERT INTO t (v) VALUES ('x')")
    holder.commit()

    writer = sqlite3.connect(db_path)
    writer.execute("INSERT INTO t (v) VALUES ('y')")
    writer.commit()
    writer.close()

    wal_path = tmp_path / "benchmarks.db-wal"
    assert wal_path.exists()

    wal_checkpoint_truncate(db_path)
    holder.close()

    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT v FROM t ORDER BY v").fetchall()
    conn.close()
    assert rows == [("x",), ("y",)]
    assert not wal_path.exists() or wal_path.stat().st_size == 0


def test_sidecar_paths_lists_expected_files(tmp_path: Path):
    db_path = tmp_path / "benchmarks.db"
    names = {p.name for p in sidecar_paths(db_path)}
    assert names == {
        "benchmarks.db-wal",
        "benchmarks.db-shm",
        "benchmarks.db-wal.bak",
        "benchmarks.db-shm.bak",
    }
