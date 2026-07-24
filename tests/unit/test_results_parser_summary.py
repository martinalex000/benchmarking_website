"""Focused tests for parse_and_store side-effect summaries."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Model, Paper, Result
from backend.paper_storage import PaperStorage
from backend.results_parser import (
    _build_dataset_param_lookup,
    _extraction_quality_issues,
    _protocol_decision,
    _protocol_result_is_eligible,
    parse_and_store_with_summary,
    source_indicates_incompatible_protocol,
)


def test_extraction_quality_quarantines_partial_or_synthesized_output():
    assert _extraction_quality_issues(
        {
            "coverage_assessment": "partial",
            "extraction_notes": "Table was truncated; representative values were synthesized.",
        },
        [],
    )
    assert _extraction_quality_issues({"coverage_assessment": "complete"}, []) == []


def test_dataset_param_lookup_does_not_collapse_model_counts():
    lookup = _build_dataset_param_lookup(
        [
            {
                "model_name": "GatedGCN-VN",
                "dataset": "LRGB",
                "params_millions": 0.5,
            },
            {
                "model_name": "GatedGCN-VN",
                "dataset": "ogbg-molpcba",
                "params_millions": 57.0,
            },
        ]
    )

    assert lookup[("lrgb", "gatedgcn-vn")] == pytest.approx(0.5)
    assert lookup[("ogbg-molpcba", "gatedgcn-vn")] == pytest.approx(57.0)


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
    import backend.results_parser as results_parser_module

    db_module._engine = None
    db_module._SessionFactory = None
    results_parser_module._PROTOCOL_EXCLUSIONS = None
    results_parser_module._PROTOCOL_CONTRACTS = None


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
    assert summary.candidate_results == 1
    assert summary.created_models == ["GraphGPS"]
    assert summary.skipped_unknown_datasets == []
    assert summary.skipped_invalid_values == []
    assert summary.overrides_applied == 0

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2401.17791").one()
        stored_result = session.query(Result).filter_by(paper_id=paper.id).one()

    assert paper.title == "Summary Test Paper"
    assert paper.codebase_url == "https://github.com/example/project"
    assert stored_result.protocol_decision == "uncertain"


def test_forced_reparse_retains_existing_rows_when_extraction_has_no_results(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        paper = Paper(arxiv_id="2110.04375", title="Stale results")
        model = Model(name="Old model", canonical_name="Old model")
        benchmark = Benchmark(name="Citation Benchmark", short_name="citation")
        session.add_all([paper, model, benchmark])
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
        variant = DatasetVariant(dataset_id=dataset.id, name="Standard", is_standard=1)
        session.add(variant)
        session.flush()
        session.add(
            Result(
                paper_id=paper.id,
                model_id=model.id,
                dataset_variant_id=variant.id,
                metric_name="Accuracy",
                metric_value=0.9,
                higher_is_better=1,
            )
        )

    storage = PaperStorage("2110.04375")
    storage.ensure_dirs()
    storage.llm_output_path.write_text(
        json.dumps({"model_used": "fake-primary", "results": {"results": []}}),
        encoding="utf-8",
    )

    summary = parse_and_store_with_summary("2110.04375", replace_existing=True)

    assert summary.replaced_results == 0
    assert summary.candidate_results == 0
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2110.04375").one()
        assert session.query(Result).filter_by(paper_id=paper.id).count() == 1


def test_curated_excluded_paper_clears_existing_rows(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    (tmp_path / "workspace" / "config" / "protocol_exclusions.yaml").write_text(
        "exclude_all_results:\n  '2402.06737': 'SSL protocol'\n",
        encoding="utf-8",
    )
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
        variant = DatasetVariant(dataset_id=dataset.id, name="Planetoid split", is_standard=1)
        model = Model(name="ExGRG", canonical_name="ExGRG")
        paper = Paper(arxiv_id="2402.06737", title="SSL paper")
        session.add_all((variant, model, paper))
        session.flush()
        session.add(
            Result(
                paper_id=paper.id,
                model_id=model.id,
                dataset_variant_id=variant.id,
                metric_name="Accuracy",
                metric_value=0.82,
                higher_is_better=1,
            )
        )

    summary = parse_and_store_with_summary("2402.06737")

    assert summary.new_results == 0
    assert summary.replaced_results == 1
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2402.06737").one()
        assert session.query(Result).filter_by(paper_id=paper.id).count() == 0


def test_versioned_extraction_rejects_link_prediction_for_node_classification(
    monkeypatch, tmp_path
):
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

    storage = PaperStorage("2402.14802")
    storage.ensure_dirs()
    storage.llm_output_path.write_text(
        json.dumps(
            {
                "model_used": "fake-primary",
                "results": {
                    "protocol_validation_version": 1,
                    "proposed_model": {"name": "GRAFF-LP"},
                    "results": [
                        {
                            "model": "GRAFF-LP",
                            "is_proposed": True,
                            "dataset": "Cora",
                            "metric": "AUC",
                            "value": 0.99,
                            "higher_is_better": True,
                            "evaluation_task": "link_prediction",
                            "uses_standard_protocol": False,
                            "protocol_note": "Custom edge split.",
                        }
                    ],
                },
            }
        ),
        encoding="utf-8",
    )

    summary = parse_and_store_with_summary("2402.14802")

    assert summary.new_results == 0
    assert len(summary.skipped_protocol_mismatches) == 1
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2402.14802").one()
        assert session.query(Result).filter_by(paper_id=paper.id).count() == 0


@pytest.mark.parametrize("source_marker", ["out-of-distribution generalization"])
def test_source_protocol_backstop_keeps_ambiguous_non_task_evidence(source_marker):
    variant = SimpleNamespace(dataset=SimpleNamespace(task_type="node_classification"))

    assert not source_indicates_incompatible_protocol(
        {
            "metric": "Accuracy",
            "evaluation_task": "node_classification",
            "protocol_note": f"This table reports {source_marker}.",
        },
        variant,
        "The paper also discusses several unrelated benchmark tasks.",
    )


def test_source_protocol_backstop_rejects_attack_rows():
    variant = SimpleNamespace(dataset=SimpleNamespace(task_type="node_classification"))

    assert source_indicates_incompatible_protocol(
        {
            "metric": "Accuracy",
            "evaluation_task": "node_classification",
            "protocol_note": "This table reports backdoor attack success.",
        },
        variant,
        "",
    )


def test_source_protocol_backstop_does_not_scan_unrelated_paper_text():
    variant = SimpleNamespace(dataset=SimpleNamespace(task_type="graph_classification"))

    assert not source_indicates_incompatible_protocol(
        {
            "metric": "AP",
            "evaluation_task": "graph_classification",
            "uses_standard_protocol": True,
            "protocol_note": "Standard Peptides-func benchmark split.",
        },
        variant,
        "The same paper also reports PCQM-Contact link prediction.",
    )


def test_source_protocol_backstop_rejects_explicit_task_mismatch():
    variant = SimpleNamespace(dataset=SimpleNamespace(task_type="node_classification"))

    assert source_indicates_incompatible_protocol(
        {
            "metric": "AUC",
            "evaluation_task": "link_prediction",
            "uses_standard_protocol": False,
            "protocol_note": "Custom edge split for link prediction.",
        },
        variant,
        "",
    )


def test_source_protocol_backstop_rejects_llm_nonstandard_decision():
    variant = SimpleNamespace(dataset=SimpleNamespace(task_type="graph_classification"))

    assert source_indicates_incompatible_protocol(
        {
            "evaluation_task": "graph_classification",
            "protocol_decision": "nonstandard",
            "protocol_note": "Link prediction results using an edge split.",
        },
        variant,
        "",
    )


def test_source_protocol_backstop_rejects_selected_ogb_tasks_even_when_marked_standard():
    variant = SimpleNamespace(
        is_standard=True,
        split_type="scaffold",
        dataset=SimpleNamespace(task_type="graph_classification"),
    )

    assert source_indicates_incompatible_protocol(
        {
            "evaluation_task": "graph_classification",
            "protocol_decision": "standard",
            "protocol_note": "Average AP across selected balanced tasks; 8 of 128 tasks.",
        },
        variant,
        "",
    )


def test_declared_split_requires_protocol_evidence_for_standard_result():
    variant = SimpleNamespace(
        is_standard=True,
        split_type="scaffold",
        dataset=SimpleNamespace(task_type="graph_classification"),
    )

    decision = _protocol_decision(
        {
            "evaluation_task": "graph_classification",
            "protocol_decision": "standard",
        },
        variant,
    )

    assert decision == "uncertain"
    assert not _protocol_result_is_eligible(decision, variant)


def test_versioned_protocol_fields_are_optional_when_task_is_missing():
    variant = SimpleNamespace(dataset=SimpleNamespace(task_type="graph_classification"))

    assert not source_indicates_incompatible_protocol(
        {"metric": "AP", "uses_standard_protocol": False},
        variant,
        "",
    )


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
