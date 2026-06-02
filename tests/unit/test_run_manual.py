import importlib
import sys
import types
from types import SimpleNamespace


def _load_run_manual():
    sys.modules.setdefault("defusedxml", types.ModuleType("defusedxml"))
    sys.modules.setdefault("defusedxml.ElementTree", types.ModuleType("defusedxml.ElementTree"))
    return importlib.import_module("scripts.run_manual")


def test_print_parse_summary_reports_existing_updates(capsys):
    run_manual = _load_run_manual()
    summary = SimpleNamespace(
        quarantined=False,
        new_results=0,
        updated_results=8,
        skipped_unknown_datasets=[],
        skipped_invalid_values=[],
        quarantine_model_names=[],
        quarantine_reasons=[],
    )

    run_manual._print_parse_summary(summary)

    captured = capsys.readouterr().out
    assert "0" in captured
    assert "existing result row(s) updated" in captured
    assert "Parsed 8 extracted row(s): 0 new, 8 updated." in captured


def test_resolve_published_date_prefers_semantic_scholar(monkeypatch):
    run_manual = _load_run_manual()
    monkeypatch.setattr(
        run_manual,
        "_fetch_semantic_scholar_metadata",
        lambda arxiv_id: {"published_date": "2024-03-15"},
    )
    monkeypatch.setattr(
        "backend.llm_extractor.fetch_arxiv_metadata",
        lambda arxiv_id: {"published_date": "2023-01-01"},
    )

    assert run_manual._resolve_published_date("2403.00001") == "2024-03-15"


def test_resolve_published_date_falls_back_to_arxiv_then_id(monkeypatch):
    run_manual = _load_run_manual()
    monkeypatch.setattr(run_manual, "_fetch_semantic_scholar_metadata", lambda arxiv_id: {})
    monkeypatch.setattr(
        "backend.llm_extractor.fetch_arxiv_metadata",
        lambda arxiv_id: {"published_date": "2023-01-01"},
    )

    assert run_manual._resolve_published_date("2403.00001") == "2023-01-01"


def test_resolve_published_date_falls_back_to_arxiv_id(monkeypatch):
    run_manual = _load_run_manual()
    monkeypatch.setattr(run_manual, "_fetch_semantic_scholar_metadata", lambda arxiv_id: {})
    monkeypatch.setattr("backend.llm_extractor.fetch_arxiv_metadata", lambda arxiv_id: {})

    assert run_manual._resolve_published_date("2403.00001") == "2024-03"
