"""Focused tests for parse_and_store side-effect summaries."""

from __future__ import annotations

import json
from pathlib import Path

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Paper
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
                "codebase_url": "https://github.com/example/project",
            }
        ),
        encoding="utf-8",
    )
    storage.text_path.write_text(
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
