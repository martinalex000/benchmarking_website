"""Regression tests for todo queue status handling."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

from backend.models import (
    TODO_PAPER_FILTER_VALUES,
    TodoPaperStatus,
    todo_paper_status_from_exit_code,
)


def _load_script_module(script_name: str, module_name: str):
    script_path = Path(__file__).resolve().parents[2] / "scripts" / script_name
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


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


def test_process_todo_list_run_paper_uses_shared_exit_code_mapping(monkeypatch):
    module = _load_script_module("process_todo_list.py", "test_process_todo_list_script")

    monkeypatch.setattr(module.console, "print", lambda *args, **kwargs: None)

    monkeypatch.setattr(
        module.subprocess, "run", lambda *args, **kwargs: SimpleNamespace(returncode=0)
    )
    assert (
        module._run_paper("2401.17791", model="primary", dry_run=False)
        == TodoPaperStatus.DONE.value
    )

    monkeypatch.setattr(
        module.subprocess, "run", lambda *args, **kwargs: SimpleNamespace(returncode=2)
    )
    assert (
        module._run_paper("2401.17791", model="primary", dry_run=False)
        == TodoPaperStatus.REJECTED.value
    )

    monkeypatch.setattr(
        module.subprocess, "run", lambda *args, **kwargs: SimpleNamespace(returncode=17)
    )
    assert (
        module._run_paper("2401.17791", model="primary", dry_run=False)
        == TodoPaperStatus.FAILED.value
    )


def test_find_todo_papers_parser_accepts_rejected_status(monkeypatch):
    module = _load_script_module("find_todo_papers.py", "test_find_todo_papers_script")

    called: dict[str, str | None] = {"status": None}
    monkeypatch.setattr(module, "cmd_list", lambda status: called.__setitem__("status", status))
    monkeypatch.setattr(module, "cmd_add", lambda *args, **kwargs: None)
    monkeypatch.setattr(module, "cmd_process", lambda *args, **kwargs: None)

    original_argv = sys.argv[:]
    try:
        sys.argv = ["find_todo_papers.py", "list", "--status", TodoPaperStatus.REJECTED.value]
        module.main()
    finally:
        sys.argv = original_argv

    assert called["status"] == TodoPaperStatus.REJECTED.value
