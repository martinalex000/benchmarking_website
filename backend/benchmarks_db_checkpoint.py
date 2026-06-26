"""SQLite WAL checkpoint helpers for version-controlled benchmarks.db."""

from __future__ import annotations

import sqlite3
from pathlib import Path

BENCHMARKS_DB_REL = "data/benchmarks.db"
GIT_LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"


def is_git_lfs_pointer(db_path: Path) -> bool:
    """Return True when *db_path* is a Git LFS pointer instead of a SQLite file."""
    try:
        header = db_path.read_bytes()[: len(GIT_LFS_POINTER_PREFIX)]
    except OSError:
        return False
    return header == GIT_LFS_POINTER_PREFIX


def is_benchmarks_db_sidecar(git_path: str) -> bool:
    """Return True if *git_path* is a SQLite sidecar, not the main DB file."""
    if git_path == BENCHMARKS_DB_REL:
        return False
    return git_path.startswith("data/benchmarks.db")


def wal_checkpoint_truncate(db_path: Path) -> None:
    """Merge WAL pages into the main DB and truncate the WAL file."""
    conn = sqlite3.connect(db_path, timeout=30)
    try:
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    finally:
        conn.close()


def sidecar_paths(db_path: Path) -> list[Path]:
    """Return WAL/SHM sidecar paths that may exist beside *db_path*."""
    parent = db_path.parent
    stem = db_path.name
    return [
        parent / f"{stem}-wal",
        parent / f"{stem}-shm",
        parent / f"{stem}-wal.bak",
        parent / f"{stem}-shm.bak",
    ]
