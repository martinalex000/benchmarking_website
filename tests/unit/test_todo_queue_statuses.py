"""Regression tests for todo queue status handling."""

from __future__ import annotations

from backend.models import (
    TODO_PAPER_FILTER_VALUES,
    TodoPaperStatus,
    todo_paper_status_from_exit_code,
)


def test_todo_status_mapping_includes_rejected_and_failed():
    assert TODO_PAPER_FILTER_VALUES == (
        "pending",
        "processing",
        "done",
        "failed",
        "rejected",
        "all",
    )
    assert todo_paper_status_from_exit_code(0) is TodoPaperStatus.DONE
    assert todo_paper_status_from_exit_code(2) is TodoPaperStatus.REJECTED
    assert todo_paper_status_from_exit_code(1) is TodoPaperStatus.FAILED
