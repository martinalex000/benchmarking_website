"""Tests for manually important todo queue priority."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import pytest

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import TodoPaper, TodoPaperStatus
from backend.todo_queue import (
    add_todo_paper,
    count_pending_important,
    load_queue_entries,
    process_queue,
    set_todo_paper_importance,
)


def _configure_temp_db(monkeypatch, tmp_path):
    db_path = tmp_path / "benchmarks.db"
    monkeypatch.setattr(cfg, "db_path", db_path)
    monkeypatch.setattr(cfg, "data_dir", tmp_path)
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))


def _insert_todo(
    arxiv_id: str,
    *,
    seen_count: int = 0,
    status: str = TodoPaperStatus.PENDING.value,
    is_manually_important: bool = False,
) -> None:
    with session_scope() as session:
        session.add(
            TodoPaper(
                arxiv_id=arxiv_id,
                status=status,
                seen_count=seen_count,
                is_manually_important=1 if is_manually_important else 0,
                created_at="2024-01-01T00:00:00Z",
            )
        )


def test_manually_important_paper_sorted_before_higher_seen_count(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("1111.1111", seen_count=100)
    _insert_todo("2222.2222", seen_count=1, is_manually_important=True)

    rows = load_queue_entries(status=TodoPaperStatus.PENDING.value, order="priority")

    assert [row.arxiv_id for row in rows] == ["2222.2222", "1111.1111"]
    assert rows[0].is_manually_important is True


def test_add_important_upgrades_existing_row(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("3333.3333", seen_count=5, status=TodoPaperStatus.DONE.value)

    created, message = add_todo_paper(
        "3333.3333",
        is_manually_important=True,
        reason="OGB leaderboard",
    )

    assert created is True
    assert "manually important" in message

    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="3333.3333").one()
        assert row.is_manually_important == 1
        assert row.reason == "OGB leaderboard"
        assert row.status == TodoPaperStatus.DONE.value


def test_add_important_with_requeue_resets_done_status(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("4444.4444", status=TodoPaperStatus.DONE.value)

    created, _message = add_todo_paper("4444.4444", is_manually_important=True, requeue=True)

    assert created is True
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="4444.4444").one()
        assert row.is_manually_important == 1
        assert row.status == TodoPaperStatus.PENDING.value


def test_mark_important_requeue_moves_done_to_pending(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("5555.5555", status=TodoPaperStatus.DONE.value)

    ok, message = set_todo_paper_importance("5555.5555", important=True, requeue=True)

    assert ok is True
    assert "manually important" in message
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="5555.5555").one()
        assert row.is_manually_important == 1
        assert row.status == TodoPaperStatus.PENDING.value


def _load_todo_queue_cli():
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "todo_queue.py"
    spec = importlib.util.spec_from_file_location("test_todo_queue_cli_priority", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_todo_queue_mark_important_dispatch(monkeypatch):
    module = _load_todo_queue_cli()
    called = {"mark": False}

    monkeypatch.setattr(
        module,
        "set_todo_paper_importance",
        lambda arxiv_id, *, important, requeue=False: called.__setitem__("mark", True)
        or (True, "ok"),
    )

    module.main(["mark-important", "2406.08993", "--requeue"])

    assert called["mark"] is True


def test_todo_queue_add_without_important_still_refuses_duplicate(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("6666.6666")

    created, message = add_todo_paper("6666.6666")

    assert created is False
    assert "Already in todo queue" in message


def test_count_pending_important_only_counts_flagged_rows(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("1111.1111", is_manually_important=True)
    _insert_todo("2222.2222")

    assert count_pending_important() == 1


def test_important_only_load_queue_entries_filters_rows(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("1111.1111", is_manually_important=True)
    _insert_todo("2222.2222")

    rows = load_queue_entries(
        status=TodoPaperStatus.PENDING.value,
        important_only=True,
    )

    assert [row.arxiv_id for row in rows] == ["1111.1111"]


def test_process_queue_important_only_dry_run_respects_filter(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("1111.1111", is_manually_important=True)
    _insert_todo("2222.2222")

    summary = process_queue(limit=5, dry_run=True, important_only=True)

    assert summary.total_selected == 1


def test_todo_queue_cli_important_only_resolves_limit(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("1111.1111", is_manually_important=True)
    _insert_todo("2222.2222", is_manually_important=True)

    module = _load_todo_queue_cli()
    args = argparse.Namespace(limit=None, important_only=True, max_attempts=3)
    assert module._resolve_process_limit(args) == 2


def test_unmark_important_clears_flag(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("7777.7777", is_manually_important=True)

    ok, _message = set_todo_paper_importance("7777.7777", important=False)

    assert ok is True
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="7777.7777").one()
        assert row.is_manually_important == 0


def test_set_importance_missing_row_returns_false(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)

    ok, message = set_todo_paper_importance("8888.8888", important=True)

    assert ok is False
    assert "Not in todo queue" in message


def test_todo_queue_unmark_important_exits_on_failure(monkeypatch):
    module = _load_todo_queue_cli()
    monkeypatch.setattr(
        module,
        "set_todo_paper_importance",
        lambda arxiv_id, *, important: (False, "missing"),
    )

    with pytest.raises(SystemExit) as exc_info:
        module.main(["unmark-important", "2406.08993"])

    assert exc_info.value.code == 1
