"""Regression tests for scripts/repopulate_db.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def _load_repopulate_db_module():
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "repopulate_db.py"
    spec = importlib.util.spec_from_file_location("test_repopulate_db_script", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_repopulate_db_uses_current_run_extraction_api(monkeypatch):
    module = _load_repopulate_db_module()

    calls: list[dict] = []

    def fake_run_extraction(
        arxiv_id,
        *,
        model_tier,
        screen_first,
        fallback_on_failure,
        extraction_strategy,
        verbose,
    ):
        calls.append(
            {
                "arxiv_id": arxiv_id,
                "model_tier": model_tier,
                "screen_first": screen_first,
                "fallback_on_failure": fallback_on_failure,
                "extraction_strategy": extraction_strategy,
                "verbose": verbose,
            }
        )
        return True

    monkeypatch.setattr(module, "_discover_arxiv_ids", lambda only=None: ["2401.17791"])
    monkeypatch.setattr(module, "_has_download", lambda arxiv_id: True)
    monkeypatch.setattr(module, "init_db", lambda: None)
    monkeypatch.setattr(module.console, "print", lambda *args, **kwargs: None)
    monkeypatch.setattr(module.console, "rule", lambda *args, **kwargs: None)

    import backend.llm_extractor as llm_extractor_module

    monkeypatch.setattr(llm_extractor_module, "run_extraction", fake_run_extraction)

    original_argv = sys.argv[:]
    try:
        sys.argv = ["repopulate_db.py", "--skip-parse"]
        module.main()
    finally:
        sys.argv = original_argv

    assert calls == [
        {
            "arxiv_id": "2401.17791",
            "model_tier": "primary",
            "screen_first": True,
            "fallback_on_failure": True,
            "extraction_strategy": "two-step",
            "verbose": True,
        }
    ]
