"""Tests for the fixed dataset-only validation helpers."""

import json
import threading
import time
from pathlib import Path

import yaml

from backend.extraction_validation import (
    exact_value_match_stats,
    load_manifest,
    normalized_result_value,
    pairwise_disagreements,
)
from backend.llm_backends import LlmBackend, ModelRoute
from backend.llm_extractor import DatasetInfo, ExtractionOutput, LLMExtractor, ResultEntry
from experiments.extraction import validate_extraction as validation


def test_manifest_has_fixed_cohort_and_manual_review_papers() -> None:
    manifest = load_manifest(Path("config/extraction_validation.yaml"))

    assert manifest.revision == "dataset-extraction-v3"
    assert [model.model_id for model in manifest.models] == [
        "zai-org/GLM-5.2-FP8",
        "cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit",
        "google/gemma-4-31B-it",
        "moonshotai/Kimi-K2.7-Code",
        "Qwen/Qwen3-Coder-30B-A3B-Instruct",
        "openai/gpt-oss-120b",
        "MiniMaxAI/MiniMax-M3-MXFP8",
        "meta-llama/Llama-3.3-70B-Instruct",
        "meta-llama/Llama-3.1-8B-Instruct",
    ]
    assert manifest.reference_model == "zai-org/GLM-5.2-FP8"
    assert len(manifest.papers) == 10
    assert [paper.arxiv_id for paper in manifest.papers] == [
        "2110.14446",
        "2205.12454",
        "2311.01038",
        "2305.13315",
        "2305.18407",
        "2306.10466",
        "2405.02795",
        "2405.16435",
        "2502.09263",
        "2506.04765",
    ]
    assert sum(len(paper.datasets) for paper in manifest.papers) == 113
    assert manifest.manual_review_papers == ("2506.04765", "2405.16435", "2311.01038")


def test_pairwise_disagreements_ignores_scale_and_rounding_but_reports_missing_rows() -> None:
    left = ExtractionOutput(
        results=[
            ResultEntry(model="GCN", dataset="Cora", metric="Accuracy", value=91.0),
            ResultEntry(model="GAT", dataset="Cora", metric="Accuracy", value=0.8),
        ]
    )
    right = ExtractionOutput(
        results=[ResultEntry(model="GCN", dataset="Cora", metric="Accuracy", value=0.91)]
    )

    differences = pairwise_disagreements({"left": left, "right": right}, ["left", "right"])

    assert len(differences) == 1
    assert differences[0]["kind"] == "presence"
    assert differences[0]["key"] == "gat / cora / accuracy"


def test_exact_value_matching_ignores_model_and_metric_but_stays_on_dataset() -> None:
    target = ExtractionOutput(
        results=[
            ResultEntry(model="NewName", dataset="Cora", metric="Accuracy", value=0.91),
            ResultEntry(model="NewName", dataset="Cora", metric="F1", value=0.8),
            ResultEntry(model="NewName", dataset="PubMed", metric="Accuracy", value=0.8),
        ]
    )
    other = ExtractionOutput(
        results=[
            ResultEntry(model="OldName", dataset="Cora", metric="ROC-AUC", value=80.0),
            ResultEntry(model="Different", dataset="PubMed", metric="MAE", value=0.8001),
        ]
    )

    stats = exact_value_match_stats(target, [other])

    assert stats.total_values == 3
    assert stats.shared_key_values == 0
    assert stats.key_unmatched_values == 3
    assert stats.exact_value_matches == 1
    assert stats.exact_value_unmatched == 2
    assert stats.exact_match_fraction == 1 / 3


def test_exact_value_matching_normalizes_percentage_scale() -> None:
    target = ExtractionOutput(
        results=[ResultEntry(model="NewName", dataset="Cora", metric="Accuracy", value=91.0)]
    )
    other = ExtractionOutput(
        results=[ResultEntry(model="OldName", dataset="Cora", metric="Accuracy", value=0.91)]
    )

    stats = exact_value_match_stats(target, [other])

    assert stats.exact_value_matches == 1
    assert normalized_result_value(target.results[0]) == normalized_result_value(other.results[0])


def test_exact_value_matching_uses_decimal_percentage_scaling() -> None:
    target = ResultEntry(model="NewName", dataset="Arxiv-year", metric="Accuracy", value=36.7)
    other = ResultEntry(model="OldName", dataset="arXiv-year", metric="Accuracy", value=0.367)

    assert normalized_result_value(target) == normalized_result_value(other)


def test_exact_value_matching_requires_exact_normalized_value() -> None:
    target = ExtractionOutput(
        results=[ResultEntry(model="NewName", dataset="Cora", metric="Accuracy", value=0.9001)]
    )
    other = ExtractionOutput(
        results=[ResultEntry(model="OldName", dataset="Cora", metric="Accuracy", value=0.9)]
    )

    stats = exact_value_match_stats(target, [other])

    assert stats.exact_value_matches == 0
    assert stats.exact_value_unmatched == 1


def test_exact_value_matching_preserves_duplicate_target_entries() -> None:
    target = ExtractionOutput(
        results=[
            ResultEntry(model="PST", dataset="QM9", metric="mu", value=0.23),
            ResultEntry(model="PST", dataset="QM9", metric="mu", value=0.023),
        ]
    )
    other = ExtractionOutput(
        results=[ResultEntry(model="Other", dataset="QM9", metric="gap", value=0.23)]
    )

    stats = exact_value_match_stats(target, [other])

    assert stats.total_values == 2
    assert stats.duplicate_keys == 1
    assert stats.exact_value_matches == 1
    assert stats.exact_value_unmatched == 1


def test_known_datasets_skip_discovery_and_skip_extraction_without_selected_tables(
    monkeypatch,
) -> None:
    extractor = LLMExtractor()
    monkeypatch.setattr(
        extractor,
        "discover_datasets",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("discovery called")),
    )
    monkeypatch.setattr("backend.llm_tasks._known_dataset_context", lambda *_args: {})
    monkeypatch.setattr(
        extractor,
        "_emit_discovery_statistics_summary",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("statistics event emitted")),
    )
    monkeypatch.setattr(extractor, "_read_result_prompt", lambda: "prompt")
    monkeypatch.setattr(
        extractor,
        "_build_rag_context",
        lambda *_args, **_kwargs: (
            "context",
            {
                "paragraphs_selected": 0,
                "paragraphs_total": 0,
                "tables_selected": 0,
                "tables_total": 0,
                "table_selection_mode": "all",
                "context_total_chars": 0,
            },
        ),
    )
    extraction_calls = 0

    def fake_extract(*_args, **_kwargs):
        nonlocal extraction_calls
        extraction_calls += 1
        return ExtractionOutput()

    monkeypatch.setattr(extractor, "_extract_dataset_with_retries", fake_extract)

    output = extractor.extract_results_two_step(
        "paper text",
        [],
        known_datasets=[DatasetInfo(name="Cora")],
    )

    assert [dataset.name for dataset in output.discovered_datasets] == ["Cora"]
    assert output.results == []
    assert extraction_calls == 0


def _write_manifest(path: Path, *, models: list[dict], papers: int = 1) -> None:
    path.write_text(
        yaml.safe_dump(
            {
                "revision": "test-v1",
                "models": models,
                "papers": [
                    {"arxiv_id": f"paper-{index}", "datasets": ["Cora"]} for index in range(papers)
                ],
                "manual_review_papers": [],
            }
        ),
        encoding="utf-8",
    )


def test_manifest_requires_exactly_one_reference(tmp_path: Path) -> None:
    path = tmp_path / "manifest.yaml"
    _write_manifest(path, models=[{"model_id": "model-a", "role": "advanced"}])

    try:
        load_manifest(path)
    except ValueError as exc:
        assert "exactly one reference" in str(exc)
    else:
        raise AssertionError("manifest without a reference should fail")


def test_validation_revision_changes_artifact_namespace(tmp_path: Path) -> None:
    first = tmp_path / "first.yaml"
    second = tmp_path / "second.yaml"
    models = [{"model_id": "reference", "role": "reference"}]
    _write_manifest(first, models=models)
    _write_manifest(second, models=models)
    payload = yaml.safe_load(second.read_text(encoding="utf-8"))
    payload["revision"] = "test-v2"
    second.write_text(yaml.safe_dump(payload), encoding="utf-8")

    first_manifest = load_manifest(first)
    second_manifest = load_manifest(second)

    assert first_manifest.digest != second_manifest.digest
    assert validation._validation_label(
        first_manifest, "reference"
    ) != validation._validation_label(second_manifest, "reference")


def test_preflight_fails_before_loading_papers_when_model_is_missing(
    monkeypatch, tmp_path: Path
) -> None:
    path = tmp_path / "manifest.yaml"
    _write_manifest(path, models=[{"model_id": "required", "role": "reference"}])
    monkeypatch.setattr(validation, "configured_backends", lambda: [])
    monkeypatch.setattr(validation, "fetch_model_routes", lambda _backends: {})
    monkeypatch.setattr(
        validation,
        "_load_inputs",
        lambda _manifest: (_ for _ in ()).throw(AssertionError("paper inputs loaded")),
    )

    assert validation.main(["--manifest", str(path)]) == 1


def test_preflight_only_checks_routes_without_loading_papers(monkeypatch, tmp_path: Path) -> None:
    path = tmp_path / "manifest.yaml"
    _write_manifest(path, models=[{"model_id": "required", "role": "reference"}])
    backend = LlmBackend(label="external", endpoint="http://example", api_key="key")
    route = ModelRoute("required", backend)
    monkeypatch.setattr(validation, "configured_backends", lambda: [backend])
    monkeypatch.setattr(validation, "fetch_model_routes", lambda _backends: {"required": route})
    monkeypatch.setattr(
        validation,
        "_load_inputs",
        lambda _manifest: (_ for _ in ()).throw(AssertionError("paper inputs loaded")),
    )

    assert validation.main(["--manifest", str(path), "--preflight-only"]) == 0


def test_three_workers_per_model_and_models_overlap(monkeypatch, tmp_path: Path) -> None:
    path = tmp_path / "manifest.yaml"
    _write_manifest(
        path,
        models=[
            {"model_id": "reference", "role": "reference"},
            {"model_id": "advanced", "role": "advanced"},
        ],
        papers=7,
    )
    manifest = load_manifest(path)
    backend = LlmBackend(label="external", endpoint="http://example", api_key="key")
    routes = {model.model_id: ModelRoute(model.model_id, backend) for model in manifest.models}
    paper_inputs = [
        validation.PaperInputs(
            paper=paper,
            paper_text="text",
            latex_paper=None,
            title=paper.arxiv_id,
        )
        for paper in manifest.papers
    ]
    active = {model.model_id: 0 for model in manifest.models}
    peaks = {model.model_id: 0 for model in manifest.models}
    globally_active: set[str] = set()
    models_overlapped = threading.Event()
    lock = threading.Lock()

    def fake_run_job(_manifest, inputs, model, _route, *, force):
        assert force is False
        with lock:
            active[model] += 1
            peaks[model] = max(peaks[model], active[model])
            globally_active.add(model)
            if len(globally_active) > 1:
                models_overlapped.set()
        time.sleep(0.03)
        with lock:
            active[model] -= 1
            if active[model] == 0:
                globally_active.discard(model)
        return validation.JobResult(
            inputs.paper.arxiv_id,
            model,
            None,
            None,
            "failed",
            0.03,
            {},
            (),
            "expected test failure",
        )

    monkeypatch.setattr(validation, "configured_backends", lambda: [backend])
    monkeypatch.setattr(validation, "fetch_model_routes", lambda _backends: routes)
    monkeypatch.setattr(validation, "_load_inputs", lambda _manifest: (paper_inputs, []))
    monkeypatch.setattr(validation, "_run_job", fake_run_job)
    monkeypatch.setattr(validation, "_build_reports", lambda **_kwargs: None)

    result = validation.main(["--manifest", str(path), "--output-dir", str(tmp_path / "report")])

    assert result == 1
    assert peaks == {"reference": 3, "advanced": 3}
    assert models_overlapped.is_set()


def test_report_contains_model_roles_coverage_and_no_false_disagreement(tmp_path: Path) -> None:
    path = tmp_path / "manifest.yaml"
    _write_manifest(
        path,
        models=[
            {"model_id": "reference", "role": "reference"},
            {"model_id": "candidate", "role": "advanced"},
        ],
    )
    manifest = load_manifest(path)
    output = ExtractionOutput(
        results=[ResultEntry(model="GCN", dataset="Cora", metric="Accuracy", value=0.9)]
    )
    report_rows = [
        validation._job_row(
            validation.JobResult(
                "paper-0",
                model,
                output,
                tmp_path / model,
                "fresh",
                1.0,
                {"total_tokens": 10},
                (),
            ),
            role,
            ("Cora",),
        )
        for model, role in (("reference", "reference"), ("candidate", "advanced"))
    ]
    output_dir = tmp_path / "report"

    validation._build_reports(
        manifest=manifest,
        run_id="test-run",
        manifest_path=path,
        output_dir=output_dir,
        report_rows=report_rows,
        all_outputs={"paper-0": {"reference": output, "candidate": output}},
        artifacts={
            "paper-0": {
                "reference": tmp_path / "reference",
                "candidate": tmp_path / "candidate",
            }
        },
    )

    report = json.loads((output_dir / "report.json").read_text(encoding="utf-8"))
    assert report["models"][1] == {"model_id": "candidate", "role": "advanced"}
    assert report["advanced_model_disagreements"] == []
    markdown = (output_dir / "report.md").read_text(encoding="utf-8")
    assert "1/1" in markdown
