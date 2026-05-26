"""Regression tests for DB bootstrap indexes."""

from __future__ import annotations

from pathlib import Path

from backend.config import cfg
from backend.db import get_engine, init_db


def _configure_temp_workspace(monkeypatch, tmp_path: Path) -> None:
    root = tmp_path / "workspace"
    data_dir = root / "data"
    papers_dir = root / "papers"
    logs_dir = root / "logs"

    for directory in (data_dir, papers_dir, logs_dir):
        directory.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "data_dir", data_dir)
    monkeypatch.setattr(cfg, "papers_dir", papers_dir)
    monkeypatch.setattr(cfg, "logs_dir", logs_dir)
    monkeypatch.setattr(cfg, "db_path", data_dir / "benchmarks.db")

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None


def test_init_db_creates_todo_queue_indexes_idempotently(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)

    init_db()
    init_db()

    with get_engine().connect() as conn:
        index_rows = conn.exec_driver_sql("PRAGMA index_list(todo_papers)").fetchall()

    index_names = {row[1] for row in index_rows}

    assert "idx_todo_status" in index_names
    assert "idx_todo_created_at" in index_names
    assert "idx_todo_seen_count" in index_names
