"""Tests for manually important todo queue priority."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import pytest

import backend.todo_queue as todo_queue_module
from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import TodoPaper, TodoPaperStatus
from backend.todo_queue import (
    TodoQueueRunResult,
    _claim_one_pending,
    _finalize_todo,
    _heartbeat_processing,
    add_todo_paper,
    count_pending_important,
    load_queue_entries,
    mark_todo_paper_done,
    process_queue,
    requeue_todo_papers,
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
        assert row.status == TodoPaperStatus.PENDING.value


def test_add_important_always_requeues_done_status(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("4444.4444", status=TodoPaperStatus.DONE.value)

    created, _message = add_todo_paper("4444.4444", is_manually_important=True)

    assert created is True
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="4444.4444").one()
        assert row.is_manually_important == 1
        assert row.status == TodoPaperStatus.PENDING.value


def test_requeue_terminal_rows_resets_attempts_without_marking_important(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("4444.0001", status=TodoPaperStatus.FAILED.value)
    _insert_todo("4444.0002", status=TodoPaperStatus.DONE.value, is_manually_important=True)
    _insert_todo("4444.0003", status=TodoPaperStatus.REJECTED.value)
    with session_scope() as session:
        for row in session.query(TodoPaper).all():
            row.attempts = 10
            row.note = "previous outcome"

    results = requeue_todo_papers(["4444.0001", "4444.0002", "4444.0003"])

    assert [result.changed for result in results] == [True, True, True]
    with session_scope() as session:
        rows = session.query(TodoPaper).order_by(TodoPaper.arxiv_id).all()
        assert [row.status for row in rows] == ["pending", "pending", "pending"]
        assert [row.attempts for row in rows] == [0, 0, 0]
        assert [row.is_manually_important for row in rows] == [0, 1, 0]
        assert [row.note for row in rows] == ["previous outcome"] * 3


def test_requeue_handles_pending_processing_and_missing_rows(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("4444.0010", status=TodoPaperStatus.PENDING.value)
    _insert_todo("4444.0011", status=TodoPaperStatus.PROCESSING.value)
    with session_scope() as session:
        processing = session.query(TodoPaper).filter_by(arxiv_id="4444.0011").one()
        processing.attempts = 4

    results = requeue_todo_papers(["4444.0010", "4444.0011", "4444.0099"])

    assert [result.ok for result in results] == [True, False, False]
    assert results[0].changed is False
    assert results[1].status == TodoPaperStatus.PROCESSING.value
    assert results[2].status is None
    with session_scope() as session:
        processing = session.query(TodoPaper).filter_by(arxiv_id="4444.0011").one()
        assert processing.status == TodoPaperStatus.PROCESSING.value
        assert processing.attempts == 4


def test_mark_important_always_moves_done_to_pending(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("5555.5555", status=TodoPaperStatus.DONE.value)

    ok, message = set_todo_paper_importance("5555.5555", important=True)

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
        lambda arxiv_id, *, important, requeue=False: (
            called.__setitem__("mark", True) or (True, "ok")
        ),
    )

    module.main(["mark-important", "2406.08993", "--requeue"])

    assert called["mark"] is True


def test_todo_queue_requeue_dispatches_multiple_ids(monkeypatch):
    module = _load_todo_queue_cli()
    called = []

    monkeypatch.setattr(
        module,
        "requeue_todo_papers",
        lambda arxiv_ids: called.append(arxiv_ids) or [],
    )

    module.main(["requeue", "2406.08993", "2407.02263"])

    assert called == [["2406.08993", "2407.02263"]]


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


def test_process_queue_forces_manually_important_papers(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("9999.0001", is_manually_important=True)
    _insert_todo("9999.0002")
    force_values = []

    def runner(arxiv_id, *, model, force):
        force_values.append((arxiv_id, force))
        return TodoQueueRunResult(returncode=0)

    summary = process_queue(
        limit=2,
        force=False,
        refresh_dev_exports=False,
        runner=runner,
    )

    assert summary.total_selected == 2
    assert force_values == [("9999.0001", True), ("9999.0002", False)]


def test_processing_heartbeat_prevents_stale_reclaim(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("9999.0101")

    claim = _claim_one_pending(max_attempts=10)
    assert claim is not None

    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="9999.0101").one()
        row.last_attempt_at = "2000-01-01T00:00:00Z"

    assert _heartbeat_processing(claim.todo_id, claim.processing_token) is True
    assert todo_queue_module.release_stale_processing_papers(stale_minutes=15) == 0

    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="9999.0101").one()
        assert row.status == TodoPaperStatus.PROCESSING.value
        assert row.processing_token == claim.processing_token


def test_stale_release_handles_legacy_processing_rows(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("9999.0103", status=TodoPaperStatus.PROCESSING.value)

    assert todo_queue_module.release_stale_processing_papers(stale_minutes=15) == 1

    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="9999.0103").one()
        assert row.status == TodoPaperStatus.PENDING.value
        assert row.processing_token is None


def test_old_processing_owner_cannot_finalize_after_token_changes(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("9999.0102")

    claim = _claim_one_pending(max_attempts=10)
    assert claim is not None

    assert (
        _finalize_todo(
            claim.todo_id,
            TodoPaperStatus.DONE,
            "stale owner",
            processing_token="wrong-token",
        )
        is False
    )

    assert (
        _finalize_todo(
            claim.todo_id,
            TodoPaperStatus.DONE,
            "current owner",
            processing_token=claim.processing_token,
        )
        is True
    )

    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="9999.0102").one()
        assert row.status == TodoPaperStatus.DONE.value
        assert row.processing_token is None
        assert row.note == "current owner"


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


def test_direct_manual_run_can_mark_todo_paper_done(monkeypatch, tmp_path):
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_todo("8888.0001", status=TodoPaperStatus.PENDING.value)

    assert mark_todo_paper_done("8888.0001", "processed directly") is True

    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="8888.0001").one()
        assert row.status == TodoPaperStatus.DONE.value
        assert row.processing_token is None
        assert row.note == "processed directly"


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
