"""Focused tests for parse_and_store side-effect summaries."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Model, Paper, Result
from backend.paper_storage import PaperStorage
from backend.results_parser import parse_and_store_with_summary


def _configure_temp_workspace(monkeypatch, tmp_path: Path) -> None:
    root = tmp_path / "workspace"
    data_dir = root / "data"
    papers_dir = root / "papers"
    logs_dir = root / "logs"
    site_dir = root / "site"
    config_dir = root / "config"

    for directory in (data_dir, papers_dir, logs_dir, site_dir, config_dir):
        directory.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "data_dir", data_dir)
    monkeypatch.setattr(cfg, "papers_dir", papers_dir)
    monkeypatch.setattr(cfg, "logs_dir", logs_dir)
    monkeypatch.setattr(cfg, "site_dir", site_dir)
    monkeypatch.setattr(cfg, "config_dir", config_dir)
    monkeypatch.setattr(cfg, "db_path", data_dir / "benchmarks.db")

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None


def test_parse_and_store_with_summary_reports_side_effects(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()
    monkeypatch.setattr(
        "backend.results_parser.find_verified_repository_link",
        lambda **_kwargs: {
            "verified_url": "https://github.com/example/project",
            "confidence": 0.91,
            "reason": "README matches the paper title.",
            "verification_model": "fake-small",
            "source_kind": "latex",
            "candidate_urls": ["https://github.com/example/project"],
            "checked_candidates": [],
        },
    )

    with session_scope() as session:
        benchmark = Benchmark(name="Long Range Graph Benchmark", short_name="lrgb")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="Peptides-func",
            task_type="graph_classification",
            primary_metric="AP",
            higher_is_better=1,
        )
        session.add(dataset)
        session.flush()
        session.add(DatasetVariant(dataset_id=dataset.id, name="Standard", is_standard=1))

    storage = PaperStorage("2401.17791")
    storage.ensure_dirs()
    storage.metadata_path.write_text(
        json.dumps(
            {
                "title": "Summary Test Paper",
                "abstract": "GraphGPS on Peptides-func.",
            }
        ),
        encoding="utf-8",
    )
    (storage.latex_dir / "expanded.tex").write_text(
        "GraphGPS on Peptides-func with source code at https://github.com/example/project",
        encoding="utf-8",
    )
    storage.llm_output_path.write_text(
        json.dumps(
            {
                "model_used": "fake-primary",
                "results": {
                    "proposed_model": {"name": "GraphGPS", "params_millions": 6.9},
                    "results": [
                        {
                            "model": "GraphGPS",
                            "is_proposed": True,
                            "dataset": "Peptides-func",
                            "metric": "AP",
                            "value": 0.6535,
                            "higher_is_better": True,
                        }
                    ],
                },
            }
        ),
        encoding="utf-8",
    )

    summary = parse_and_store_with_summary("2401.17791")

    assert summary.arxiv_id == "2401.17791"
    assert summary.extraction_model == "fake-primary"
    assert summary.created_stub_paper is True
    assert summary.metadata_changed is True
    assert summary.new_results == 1
    assert summary.updated_results == 0
    assert summary.created_models == ["GraphGPS"]
    assert summary.skipped_unknown_datasets == []
    assert summary.skipped_invalid_values == []
    assert summary.overrides_applied == 0

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2401.17791").one()

    assert paper.title == "Summary Test Paper"
    assert paper.codebase_url == "https://github.com/example/project"


def test_parse_and_store_persists_model_metadata(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        benchmark = Benchmark(name="Long Range Graph Benchmark", short_name="lrgb")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="Peptides-func",
            task_type="graph_classification",
            primary_metric="AP",
            higher_is_better=1,
        )
        session.add(dataset)
        session.flush()
        session.add(DatasetVariant(dataset_id=dataset.id, name="Standard", is_standard=1))

    storage = PaperStorage("2505.20853")
    storage.ensure_dirs()
    storage.llm_output_path.write_text(
        json.dumps(
            {
                "model_used": "fake-primary",
                "model_sizes": [
                    {
                        "model_name": "GraphGPS (ours)",
                        "matched_result_name": "GraphGPS",
                        "params_millions": 6.9,
                    }
                ],
                "results": {
                    "proposed_model": {
                        "name": "GraphGPS",
                        "model_type": "hybrid",
                        "params_millions": 6.9,
                    },
                    "baseline_models": [
                        {"name": "GCN", "model_type": "gnn", "params_millions": 1.2}
                    ],
                    "results": [
                        {
                            "model": "GraphGPS",
                            "is_proposed": True,
                            "dataset": "Peptides-func",
                            "metric": "AP",
                            "value": 0.6535,
                            "higher_is_better": True,
                            "uses_external_data": False,
                        },
                        {
                            "model": "GCN",
                            "is_proposed": False,
                            "dataset": "Peptides-func",
                            "metric": "AP",
                            "value": 0.5930,
                            "higher_is_better": True,
                        },
                    ],
                },
            }
        ),
        encoding="utf-8",
    )

    summary = parse_and_store_with_summary("2505.20853")
    assert summary.new_results == 2

    with session_scope() as session:
        graphgps = session.query(Model).filter_by(canonical_name="GraphGPS").one()
        gcn = session.query(Model).filter_by(canonical_name="GCN").one()
        results = (
            session.query(Result)
            .filter_by(paper_id=session.query(Paper).filter_by(arxiv_id="2505.20853").one().id)
            .all()
        )

    assert graphgps.model_type == "hybrid"
    assert graphgps.size_params == 6_900_000
    assert gcn.model_type == "gnn"
    params_by_model = {
        session.get(Model, r.model_id).canonical_name: r.params_millions for r in results
    }
    assert params_by_model["GraphGPS"] == pytest.approx(6.9)
    assert params_by_model["GCN"] == pytest.approx(1.2)


def test_parse_and_store_with_summary_quarantines_suspicious_method_names(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        benchmark = Benchmark(name="Citation Benchmark", short_name="citation")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="Cora",
            task_type="node_classification",
            primary_metric="Accuracy",
            higher_is_better=1,
        )
        session.add(dataset)
        session.flush()
        session.add(DatasetVariant(dataset_id=dataset.id, name="Standard", is_standard=1))

    storage = PaperStorage("2309.04082")
    storage.ensure_dirs()
    storage.metadata_path.write_text(
        json.dumps(
            {
                "title": "Curve Your Attention: Mixed-Curvature Transformers for Graph Representation Learning"
            }
        ),
        encoding="utf-8",
    )
    storage.text_path.write_text(
        "We propose FPS-T for graph representation learning.", encoding="utf-8"
    )
    storage.llm_output_path.write_text(
        json.dumps(
            {
                "model_used": "fake-primary",
                "results": {
                    "proposed_model": {"name": r"\modelname{}"},
                    "results": [
                        {
                            "model": r"\modelname{}",
                            "is_proposed": True,
                            "dataset": "Cora",
                            "metric": "Accuracy",
                            "value": 0.91,
                            "higher_is_better": True,
                        }
                    ],
                },
            }
        ),
        encoding="utf-8",
    )

    summary = parse_and_store_with_summary("2309.04082")

    assert summary.quarantined is True
    assert "proposed model name still contains LaTeX or citation text" in summary.quarantine_reasons
    assert r"\modelname" in summary.quarantine_model_names
    assert summary.new_results == 0

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2309.04082").one()
        result_count = session.query(Result).count()

    assert paper.extraction_status == "quarantined_method_name"
    assert result_count == 0


def test_parse_and_store_ignores_dataset_statistics_parse_failure(monkeypatch, tmp_path):
    from backend.results_parser import _is_fatal_extraction_parse_failure

    assert _is_fatal_extraction_parse_failure("extract_dataset_statistics: boom") is False
    assert _is_fatal_extraction_parse_failure("extract_dataset:QM9:g1: boom") is True

    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        benchmark = Benchmark(name="Quantum Chemistry", short_name="qchem")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="QM9",
            task_type="graph_regression",
            primary_metric="gap",
            higher_is_better=0,
        )
        session.add(dataset)
        session.flush()
        session.add(DatasetVariant(dataset_id=dataset.id, name="Standard split", is_standard=1))

    storage = PaperStorage("2102.09844")
    storage.ensure_dirs()
    storage.metadata_path.write_text(
        json.dumps({"title": "E(n) Equivariant Graph Neural Networks"})
    )
    storage.text_path.write_text("Benchmark on QM9.", encoding="utf-8")
    storage.llm_output_path.write_text(
        json.dumps(
            {
                "model_used": "test-model",
                "results": {
                    "proposed_model": {"name": "EGNN"},
                    "baseline_models": [],
                    "results": [
                        {
                            "model": "EGNN",
                            "is_proposed": True,
                            "dataset": "QM9",
                            "metric": "gap",
                            "value": 0.04,
                            "higher_is_better": False,
                        }
                    ],
                },
            }
        ),
        encoding="utf-8",
    )
    storage.llm_calls_path.write_text(
        yaml.safe_dump(
            [
                {
                    "call_type": "extract_dataset_statistics",
                    "parse_error": "JSON parse failed",
                }
            ]
        ),
        encoding="utf-8",
    )

    summary = parse_and_store_with_summary("2102.09844")

    assert summary.quarantined is False
    assert summary.new_results == 1
