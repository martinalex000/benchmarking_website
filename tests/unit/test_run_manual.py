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


def test_should_run_pre_screen_skips_when_force_or_existing(monkeypatch, tmp_path):
    run_manual = _load_run_manual()
    from backend.config import cfg

    paper_root = tmp_path / "papers" / "2402.08170"
    extracted = paper_root / "extracted"
    extracted.mkdir(parents=True)
    monkeypatch.setattr(cfg, "papers_dir", tmp_path / "papers")

    assert (
        run_manual._should_run_pre_screen(
            "2402.08170",
            skip_screen=False,
            force_extract=True,
        )
        is False
    )
    assert (
        run_manual._should_run_pre_screen(
            "2402.08170",
            skip_screen=True,
            force_extract=False,
        )
        is False
    )

    llm_out = extracted / "llm_output.yaml"
    llm_out.write_text("results: {}\n", encoding="utf-8")
    assert (
        run_manual._should_run_pre_screen(
            "2402.08170",
            skip_screen=False,
            force_extract=False,
        )
        is False
    )

    llm_out.unlink()
    assert (
        run_manual._should_run_pre_screen(
            "2402.08170",
            skip_screen=False,
            force_extract=False,
        )
        is True
    )


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
    from backend.config import cfg

    monkeypatch.setattr(cfg, "semantic_scholar_api_key", "")
    monkeypatch.setattr(run_manual, "_fetch_semantic_scholar_metadata", lambda arxiv_id: {})
    monkeypatch.setattr(
        "backend.llm_extractor.fetch_arxiv_metadata",
        lambda arxiv_id: {"published_date": "2023-01-01"},
    )

    assert run_manual._resolve_published_date("2403.00001") == "2023-01-01"


def test_resolve_published_date_skips_arxiv_when_semantic_scholar_key_set(monkeypatch):
    run_manual = _load_run_manual()
    from backend.config import cfg

    monkeypatch.setattr(cfg, "semantic_scholar_api_key", "test-key")
    monkeypatch.setattr(run_manual, "_fetch_semantic_scholar_metadata", lambda arxiv_id: {})

    def _should_not_call(_arxiv_id: str) -> dict:
        raise AssertionError("fetch_arxiv_metadata should not be called when S2 key is set")

    monkeypatch.setattr("backend.llm_extractor.fetch_arxiv_metadata", _should_not_call)

    assert run_manual._resolve_published_date("2403.00001") == "2024-03"


def test_resolve_published_date_falls_back_to_arxiv_id(monkeypatch):
    run_manual = _load_run_manual()
    from backend.config import cfg

    monkeypatch.setattr(cfg, "semantic_scholar_api_key", "")
    monkeypatch.setattr(run_manual, "_fetch_semantic_scholar_metadata", lambda arxiv_id: {})
    monkeypatch.setattr("backend.llm_extractor.fetch_arxiv_metadata", lambda arxiv_id: {})

    assert run_manual._resolve_published_date("2403.00001") == "2024-03"


def test_print_llm_backend_status_reports_unreachable_local(monkeypatch, capsys):
    run_manual = _load_run_manual()
    from backend.config import cfg
    from backend.llm_backends import BackendProbe, LlmBackend, ModelRoute

    monkeypatch.setattr(cfg, "llm_local_endpoint", "http://127.0.0.1:8000/v1")
    monkeypatch.setattr(cfg, "llm_endpoint", "https://example.com/v1")
    monkeypatch.setattr(cfg, "model_primary", "local-model")
    monkeypatch.setattr(cfg, "model_small", "small-model")

    local = LlmBackend(label="local", endpoint="http://127.0.0.1:8000/v1", api_key="local")
    external = LlmBackend(label="external", endpoint="https://example.com/v1", api_key="external")
    monkeypatch.setattr(
        run_manual,
        "configured_backends",
        lambda: [local, external],
    )
    monkeypatch.setattr(
        run_manual,
        "probe_backends",
        lambda backends: [
            BackendProbe(local, False, error="connection refused"),
            BackendProbe(external, True, ("small-model",)),
        ],
    )
    monkeypatch.setattr(
        run_manual,
        "fetch_model_routes",
        lambda backends: {
            "small-model": ModelRoute("small-model", external),
        },
    )

    run_manual._print_llm_backend_status(extraction_tier="primary", do_screen=True)

    captured = capsys.readouterr().out
    assert "Local vLLM: not reachable" in captured
    assert "http://127.0.0.1:8000/v1" in captured
    assert "connection refused" in captured
    assert "External:" in captured
    assert "pre-screen:" in captured
    assert "extraction:" in captured
