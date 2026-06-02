"""Regression tests for DB bootstrap indexes."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from backend.config import cfg
from backend.db import MIGRATIONS, get_engine, init_db


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


def test_init_db_applies_tracked_migrations_to_legacy_schema(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)

    conn = sqlite3.connect(cfg.db_path)
    conn.executescript(
        """
        CREATE TABLE results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paper_id INTEGER,
            model_id INTEGER,
            dataset_variant_id INTEGER,
            metric_name TEXT NOT NULL,
            metric_value REAL NOT NULL,
            higher_is_better INTEGER NOT NULL DEFAULT 1,
            is_problematic INTEGER NOT NULL DEFAULT 0
        );
        CREATE TABLE pending_datasets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            arxiv_id TEXT NOT NULL,
            dataset_name TEXT NOT NULL,
            created_at TEXT,
            UNIQUE(arxiv_id, dataset_name)
        );
        CREATE TABLE todo_papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            arxiv_id TEXT UNIQUE NOT NULL,
            title TEXT,
            reason TEXT,
            added_by TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            attempts INTEGER NOT NULL DEFAULT 0,
            last_attempt_at TEXT,
            note TEXT,
            created_at TEXT NOT NULL
        );
        CREATE INDEX idx_todo_status ON todo_papers(status);
        """
    )
    conn.commit()
    conn.close()

    init_db()
    init_db()

    with get_engine().connect() as conn2:
        migration_rows = conn2.exec_driver_sql(
            "SELECT name FROM schema_migrations ORDER BY name"
        ).fetchall()
        todo_columns = conn2.exec_driver_sql("PRAGMA table_info(todo_papers)").fetchall()
        pending_columns = conn2.exec_driver_sql("PRAGMA table_info(pending_datasets)").fetchall()
        result_columns = conn2.exec_driver_sql("PRAGMA table_info(results)").fetchall()
        index_rows = conn2.exec_driver_sql("PRAGMA index_list(todo_papers)").fetchall()

    migration_names = [row[0] for row in migration_rows]
    todo_column_names = {row[1] for row in todo_columns}
    pending_column_names = {row[1] for row in pending_columns}
    result_column_names = {row[1] for row in result_columns}
    index_names = {row[1] for row in index_rows}

    assert migration_names == [migration.name for migration in MIGRATIONS]
    assert "uses_external_data" in result_column_names
    assert "params_millions" in result_column_names
    assert "variant_inference_reason" in result_column_names
    assert {
        "paper_title",
        "metrics_seen",
        "suggestion",
        "status",
        "resolved_dataset_id",
        "updated_at",
    } <= pending_column_names
    assert {
        "cited_by_count",
        "cites_existing_count",
        "seen_count",
        "seen_from",
        "first_seen_at",
    } <= todo_column_names
    assert "idx_todo_created_at" in index_names
    assert "idx_todo_seen_count" in index_names
