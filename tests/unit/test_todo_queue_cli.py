"""Tests for the unified todo queue CLI."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_todo_queue_module():
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "todo_queue.py"
    spec = importlib.util.spec_from_file_location("test_todo_queue_cli", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_todo_queue_no_args_shows_help(capsys):
    """Running with no subcommand should print help and exit 0."""
    import pytest

    module = _load_todo_queue_module()

    with pytest.raises(SystemExit) as exc_info:
        module.main([])

    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "worker" in captured.out or "process" in captured.out


def test_todo_queue_report_dispatch(monkeypatch):
    module = _load_todo_queue_module()

    called = {"report": False}
    monkeypatch.setattr(module, "cmd_process", lambda args: None)
    monkeypatch.setattr(module, "cmd_report", lambda args: called.__setitem__("report", True))
    monkeypatch.setattr(module, "cmd_list", lambda args: None)
    monkeypatch.setattr(module, "cmd_add", lambda args: None)
    monkeypatch.setattr(module, "cmd_recompute_counts", lambda args: None)

    module.main(["report"])

    assert called["report"] is True
