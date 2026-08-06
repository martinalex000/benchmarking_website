"""Tests for compare_models artifact persistence and cache reuse."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from backend.config import cfg
from backend.llm_backends import LlmBackend, ModelRoute
from backend.llm_extractor import ExtractionOutput, ResultEntry
from scripts import compare_models as cm


def _write_compare_artifact(
    artifact_dir: Path,
    *,
    arxiv_id: str,
    model_used: str,
    label: str,
    results: list[dict] | None = None,
) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "arxiv_id": arxiv_id,
        "model_used": model_used,
        "extracted_at": "2026-01-01T00:00:00+00:00",
        "experiment": {"label": label, "strategy": "auto", "result_output_format": "json"},
        "results": {
            "results": results
            or [
                {
                    "model": "TestModel",
                    "dataset": "Cora",
                    "metric": "Accuracy",
                    "value": 0.91,
                }
            ],
            "extraction_confidence": "HIGH",
            "extraction_notes": "",
            "discovered_datasets": [],
            "paper_has_statistics": False,
        },
        "usage": {"total_duration_s": 12.5},
    }
    (artifact_dir / "llm_output.yaml").write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def test_compare_artifact_dir_matches_process_paper_layout(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    arxiv_id = "2206.08164"
    model = "qwen3.5-27b"
    expected = (
        tmp_path
        / arxiv_id
        / "extracted"
        / "experiments"
        / cm._slugify_label(cm._compare_experiment_label(model))
    )
    assert cm._compare_artifact_dir(arxiv_id, model) == expected


def test_plan_jobs_reuses_cache_when_not_forced(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    arxiv_id = "2206.08164"
    model = "qwen3.5-27b"
    artifact_dir = cm._compare_artifact_dir(arxiv_id, model)
    _write_compare_artifact(
        artifact_dir,
        arxiv_id=arxiv_id,
        model_used=model,
        label=cm._compare_experiment_label(model),
    )

    backend = LlmBackend(label="external", endpoint="http://example", api_key="k")
    model_routes = {model: ModelRoute(model_id=model, backend=backend)}
    paper_inputs = {
        arxiv_id: ("paper text", [], None, "Test Paper"),
    }
    opts = cm._ProcessOptions(
        baseline_model_id="glm-4.7",
        model_routes=model_routes,
    )
    llm_jobs, cached, plan = cm._plan_compare_jobs(
        paper_inputs,
        [model],
        model_routes,
        opts,
    )
    assert llm_jobs == []
    assert len(cached) == 1
    assert cached[0].source == "cached"
    assert plan[0].source == "cached"


def test_plan_jobs_force_all_runs_llm(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    arxiv_id = "2206.08164"
    model = "qwen3.5-27b"
    artifact_dir = cm._compare_artifact_dir(arxiv_id, model)
    _write_compare_artifact(
        artifact_dir,
        arxiv_id=arxiv_id,
        model_used=model,
        label=cm._compare_experiment_label(model),
    )

    backend = LlmBackend(label="external", endpoint="http://example", api_key="k")
    model_routes = {model: ModelRoute(model_id=model, backend=backend)}
    paper_inputs = {arxiv_id: ("paper text", [], None, "Test Paper")}
    opts = cm._ProcessOptions(
        baseline_model_id="glm-4.7",
        model_routes=model_routes,
        force_all=True,
    )
    llm_jobs, cached, plan = cm._plan_compare_jobs(
        paper_inputs,
        [model],
        model_routes,
        opts,
    )
    assert len(llm_jobs) == 1
    assert cached == []
    assert plan[0].source == "fresh"


def test_plan_jobs_auto_includes_cached_model_outside_test_list(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    arxiv_id = "2206.08164"
    cached_model = "gemma-3-27b-it"
    test_model = "qwen3.5-27b"
    _write_compare_artifact(
        cm._compare_artifact_dir(arxiv_id, cached_model),
        arxiv_id=arxiv_id,
        model_used=cached_model,
        label=cm._compare_experiment_label(cached_model),
    )

    backend = LlmBackend(label="external", endpoint="http://example", api_key="k")
    model_routes = {
        test_model: ModelRoute(model_id=test_model, backend=backend),
        cached_model: ModelRoute(model_id=cached_model, backend=backend),
    }
    paper_inputs = {arxiv_id: ("paper text", [], None, "Test Paper")}
    opts = cm._ProcessOptions(baseline_model_id="glm-4.7", model_routes=model_routes)
    llm_jobs, cached, plan = cm._plan_compare_jobs(
        paper_inputs,
        [test_model],
        model_routes,
        opts,
    )
    assert len(llm_jobs) == 1
    assert llm_jobs[0].model == test_model
    auto_rows = [row for row in plan if row.source == "auto_included"]
    assert len(auto_rows) == 1
    assert auto_rows[0].model == cached_model
    assert any(item.source == "auto_included" for item in cached)


def test_cached_paper_ids_for_model(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    paper_a = "2206.08164"
    paper_b = "2301.00001"
    model = "qwen3.5-27b"
    _write_compare_artifact(
        cm._compare_artifact_dir(paper_a, model),
        arxiv_id=paper_a,
        model_used=model,
        label=cm._compare_experiment_label(model),
    )
    cached = cm._cached_paper_ids_for_model(model, [paper_a, paper_b])
    assert cached == [paper_a]
    assert cm._count_cached_papers(model, [paper_a, paper_b]) == 1


def test_format_cached_traces_column() -> None:
    assert cm._format_cached_traces_column(["2206.08164"], ["2206.08164"]) == "[green]yes[/green]"
    assert cm._format_cached_traces_column(["2206.08164"], []) == "[dim]—[/dim]"
    assert (
        cm._format_cached_traces_column(["2206.08164", "2301.00001"], ["2206.08164"])
        == "2206.08164"
    )
    assert (
        cm._format_cached_traces_column(["2206.08164", "2301.00001"], ["2206.08164", "2301.00001"])
        == "[green]all 2[/green]"
    )


def test_write_comparison_json(tmp_path: Path) -> None:
    artifact_dir = tmp_path / "artifact"
    artifact_dir.mkdir()
    cmp = cm.PaperComparison(
        arxiv_id="2206.08164",
        llm_model="qwen3.5-27b",
        baseline_count=3,
        hits=2,
        source="fresh",
        artifact_path=artifact_dir,
        extracted_at="2026-01-01T00:00:00+00:00",
    )
    cm._write_comparison_json(artifact_dir, cmp, "glm-4.7")
    data = json.loads((artifact_dir / "comparison.json").read_text(encoding="utf-8"))
    assert data["baseline_model"] == "glm-4.7"
    assert data["source"] == "fresh"
    assert data["hits"] == 2


def test_store_compare_extraction_result_waits_for_baseline(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    job = cm.CompareJob(
        model="qwen3.5-27b",
        endpoint="http://example",
        api_key="k",
        backend="external",
        arxiv_id="2206.08164",
        paper_title="Test Paper",
        paper_text="paper text",
        baseline=[],
        latex_paper=None,
    )
    extraction = cm._CompareExtractionResult(
        job=job,
        out=ExtractionOutput(results=[]),
        duration_s=1.0,
        error=None,
        call_log=[],
        source="fresh",
        artifact_path=tmp_path / "artifact",
        extracted_at="2026-01-01T00:00:00+00:00",
    )
    opts = cm._ProcessOptions(baseline_model_id="glm-4.7")
    pending: list[cm._CompareExtractionResult] = []
    results: list[cm.PaperComparison] = []

    cm._store_compare_extraction_result(extraction, opts, pending=pending, results=results)

    assert results == []
    assert pending == [extraction]


def test_store_compare_extraction_result_without_baseline_is_extraction_only(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    artifact_dir = tmp_path / "artifact"
    extraction = cm._CompareExtractionResult(
        job=cm.CompareJob(
            model="qwen3.5-27b",
            endpoint="http://example",
            api_key="k",
            backend="external",
            arxiv_id="2206.08164",
            paper_title="Test Paper",
            paper_text="paper text",
            baseline=[],
            latex_paper=None,
        ),
        out=ExtractionOutput(results=[]),
        duration_s=1.0,
        error=None,
        call_log=[],
        source="fresh",
        artifact_path=artifact_dir,
        extracted_at="2026-01-01T00:00:00+00:00",
    )
    opts = cm._ProcessOptions(
        baseline_model_id="glm-4.7",
        ensure_baseline=False,
    )
    pending: list[cm._CompareExtractionResult] = []
    results: list[cm.PaperComparison] = []

    cm._store_compare_extraction_result(extraction, opts, pending=pending, results=results)

    assert pending == []
    assert len(results) == 1
    assert results[0].error == "comparison skipped: no baseline available"
    assert results[0].artifact_path == artifact_dir


def test_flush_pending_for_paper_writes_comparison_json(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    arxiv_id = "2206.08164"
    baseline_dir = tmp_path / arxiv_id / "extracted"
    baseline_dir.mkdir(parents=True)
    baseline_payload = {
        "model_used": "glm-4.7",
        "results": {
            "results": [
                {"model": "GNN", "dataset": "Cora", "metric": "Accuracy", "value": 0.9},
            ]
        },
    }
    (baseline_dir / "llm_output.yaml").write_text(
        yaml.safe_dump(baseline_payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    artifact_dir = cm._compare_artifact_dir(arxiv_id, "qwen3.5-27b")
    _write_compare_artifact(
        artifact_dir,
        arxiv_id=arxiv_id,
        model_used="qwen3.5-27b",
        label=cm._compare_experiment_label("qwen3.5-27b"),
    )
    loaded = cm._CompareExtractionResult(
        job=cm.CompareJob(
            model="qwen3.5-27b",
            endpoint="http://example",
            api_key="k",
            backend="external",
            arxiv_id=arxiv_id,
            paper_title="Test Paper",
            paper_text="paper text",
            baseline=[],
            latex_paper=None,
        ),
        out=ExtractionOutput(
            results=[
                ResultEntry(
                    model="TestModel",
                    dataset="Cora",
                    metric="Accuracy",
                    value=0.91,
                )
            ]
        ),
        duration_s=1.0,
        error=None,
        call_log=[],
        source="fresh",
        artifact_path=artifact_dir,
        extracted_at="2026-01-01T00:00:00+00:00",
    )

    opts = cm._ProcessOptions(baseline_model_id="glm-4.7", persist=True)
    pending = [loaded]
    results: list[cm.PaperComparison] = []

    cm._flush_pending_for_paper(arxiv_id, opts, pending=pending, results=results)

    assert pending == []
    assert len(results) == 1
    assert (artifact_dir / "comparison.json").exists()


def test_load_baseline_reads_main_extracted_artifact(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    arxiv_id = "2206.08164"
    extracted = tmp_path / arxiv_id / "extracted"
    extracted.mkdir(parents=True)
    payload = {
        "model_used": "glm-4.7",
        "results": {
            "results": [
                {"model": "GNN", "dataset": "Cora", "metric": "Accuracy", "value": 0.9},
            ]
        },
    }
    (extracted / "llm_output.yaml").write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    baseline = cm._load_baseline(arxiv_id, "glm-4.7")
    assert len(baseline) == 1
    assert baseline[0]["dataset"] == "Cora"


def test_load_baseline_collapses_implementation_marker_variants(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    arxiv_id = "2406.08993"
    extracted = tmp_path / arxiv_id / "extracted"
    extracted.mkdir(parents=True)
    payload = {
        "model_used": "glm-4.7",
        "results": {
            "results": [
                {"model": "GraphGPS", "dataset": "Cora", "metric": "Accuracy", "value": 0.9119},
                {"model": "GraphGPS*", "dataset": "Cora", "metric": "Accuracy", "value": 0.9179},
            ]
        },
    }
    (extracted / "llm_output.yaml").write_text(
        yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    baseline = cm._load_baseline(arxiv_id, "glm-4.7")
    assert len(baseline) == 1
    assert baseline[0]["model"] == "GraphGPS"
    assert baseline[0]["value"] == 0.9179


def test_compare_matches_unstarred_candidate_to_starred_baseline(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setattr(cfg, "papers_dir", tmp_path)
    baseline = [
        {"model": "GraphGPS", "dataset": "Cora", "metric": "Accuracy", "value": 0.9179},
    ]
    candidate = ExtractionOutput(
        results=[
            ResultEntry(
                model="GraphGPS",
                dataset="Cora",
                metric="Accuracy",
                value=0.9179,
            )
        ]
    )
    cmp = cm._compare("2406.08993", "test-model", baseline, candidate, [])
    assert cmp.baseline_count == 1
    assert cmp.hits == 1
    assert cmp.misses == 0
