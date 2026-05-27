"""Integration tests for the extract -> parse -> export pipeline path."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Paper, PipelineRun, Result
from backend.paper_storage import PaperStorage


def _configure_temp_workspace(monkeypatch, tmp_path: Path) -> Path:
    root = tmp_path / "workspace"
    data_dir = root / "data"
    papers_dir = root / "papers"
    logs_dir = root / "logs"
    site_dir = root / "site"
    config_dir = root / "config"

    for directory in (data_dir, papers_dir, logs_dir, site_dir, config_dir):
        directory.mkdir(parents=True, exist_ok=True)

    dataset_overrides = config_dir / "dataset_overrides.yaml"
    dataset_overrides.write_text("{}\n", encoding="utf-8")

    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "data_dir", data_dir)
    monkeypatch.setattr(cfg, "papers_dir", papers_dir)
    monkeypatch.setattr(cfg, "logs_dir", logs_dir)
    monkeypatch.setattr(cfg, "site_dir", site_dir)
    monkeypatch.setattr(cfg, "config_dir", config_dir)
    monkeypatch.setattr(cfg, "db_path", data_dir / "benchmarks.db")

    import backend.db as db_module
    from backend import export_to_hugo

    db_module._engine = None
    db_module._SessionFactory = None

    monkeypatch.setattr(export_to_hugo, "_SITE_DIR", site_dir)
    monkeypatch.setattr(export_to_hugo, "_CONTENT", site_dir / "content")
    monkeypatch.setattr(export_to_hugo, "_DATA_DIR", site_dir / "data")
    monkeypatch.setattr(export_to_hugo, "_STATIC", site_dir / "static")
    monkeypatch.setattr(export_to_hugo, "_DATASET_OVERRIDES_FILE", dataset_overrides)
    export_to_hugo._MODEL_RENAME_CACHE.clear()
    export_to_hugo._DATASET_OVERRIDE_CACHE.clear()
    export_to_hugo._PAPER_PARAM_CACHE.clear()

    return root


def test_pipeline_extract_parse_export_flow(monkeypatch, tmp_path):
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
        session.add(
            Paper(
                arxiv_id="2401.17791",
                title="Integration Test Paper",
                abstract="We evaluate GraphGPS on Peptides-func.",
                extraction_status="downloaded",
                discovery_source="integration-test",
                published_date="2024-01-01",
            )
        )

    from backend import pipeline

    def fake_run_extraction(arxiv_id: str, model_tier: str = "primary", verbose: bool = False):
        storage = PaperStorage(arxiv_id)
        storage.ensure_dirs()
        storage.text_path.write_text(
            "GraphGPS and GCN are evaluated on Peptides-func.", encoding="utf-8"
        )
        storage.llm_output_path.write_text(
            json.dumps(
                {
                    "model_used": f"fake-{model_tier}",
                    "results": {
                        "proposed_model": {"name": "GraphGPS", "params_millions": 6.9},
                        "baseline_models": [{"name": "GCN", "params_millions": 2.1}],
                        "results": [
                            {
                                "model": "GraphGPS",
                                "is_proposed": True,
                                "dataset": "Peptides-func",
                                "metric": "AP",
                                "value": 0.6535,
                                "std": 0.004,
                                "higher_is_better": True,
                            },
                            {
                                "model": "GCN",
                                "is_proposed": False,
                                "dataset": "Peptides-func",
                                "metric": "AP",
                                "value": 0.593,
                                "higher_is_better": True,
                            },
                        ],
                    },
                }
            ),
            encoding="utf-8",
        )

        with session_scope() as session:
            paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).one()
            paper.extraction_status = "extracted"

        return True

    monkeypatch.setattr("backend.llm_extractor.run_extraction", fake_run_extraction)

    pipeline.stage_extract(SimpleNamespace(model="primary", force=False, paper=None))
    pipeline.stage_parse(SimpleNamespace(force=False, paper=None))
    pipeline.stage_export(SimpleNamespace(paper=["2401.17791"]))

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2401.17791").one()
        results = session.query(Result).filter_by(paper_id=paper.id).all()
        runs = session.query(PipelineRun).filter_by(paper_id=paper.id).all()
        result_pairs = {(result.model.name, result.metric_value) for result in results}
        run_pairs = {(run.stage, run.status) for run in runs}

    assert paper.extraction_model == "fake-primary"
    assert paper.extraction_status == "extracted"
    assert len(results) == 2
    assert {result.metric_name for result in results} == {"AP"}
    assert result_pairs == {
        ("GraphGPS", 0.6535),
        ("GCN", 0.593),
    }
    assert run_pairs >= {
        ("extract", "success"),
        ("parse", "success"),
    }

    paper_page = cfg.site_dir / "content" / "papers" / "2401.17791" / "index.md"
    dataset_page = cfg.site_dir / "content" / "datasets" / "peptides-func" / "index.md"

    assert paper_page.exists()
    assert dataset_page.exists()
    assert "GraphGPS" in paper_page.read_text(encoding="utf-8")
    assert "Peptides-func" in dataset_page.read_text(encoding="utf-8")


def test_pipeline_extract_failure_records_failed_run(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        session.add(
            Paper(
                arxiv_id="2402.00789",
                title="Extraction Failure Paper",
                abstract="Downloaded already but extraction will fail.",
                extraction_status="downloaded",
                discovery_source="integration-test",
                published_date="2024-02-01",
            )
        )

    from backend import pipeline

    monkeypatch.setattr(
        "backend.llm_extractor.run_extraction",
        lambda arxiv_id, model_tier="primary", verbose=False: False,
    )

    pipeline.stage_extract(SimpleNamespace(model="primary", force=False, paper=["2402.00789"]))

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2402.00789").one()
        runs = session.query(PipelineRun).filter_by(paper_id=paper.id).all()

    assert paper.extraction_status == "downloaded"
    assert {(run.stage, run.status) for run in runs} == {("extract", "failed")}


def test_pipeline_parse_failure_still_exports_paper_page(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        session.add(
            Paper(
                arxiv_id="2402.04821",
                title="Malformed Extraction Output",
                abstract="This paper has malformed extraction output.",
                extraction_status="extracted",
                discovery_source="integration-test",
                published_date="2024-02-02",
            )
        )

    storage = PaperStorage("2402.04821")
    storage.ensure_dirs()
    storage.llm_output_path.write_text("{not valid json", encoding="utf-8")

    from backend import pipeline

    pipeline.stage_parse(SimpleNamespace(force=False, paper=["2402.04821"]))
    pipeline.stage_export(SimpleNamespace(paper=["2402.04821"]))

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id="2402.04821").one()
        runs = session.query(PipelineRun).filter_by(paper_id=paper.id).all()
        results = session.query(Result).filter_by(paper_id=paper.id).all()

    assert results == []
    assert ("parse", "failed") in {(run.stage, run.status) for run in runs}

    paper_page = cfg.site_dir / "content" / "papers" / "2402.04821" / "index.md"
    assert paper_page.exists()
    assert "has_results: false" in paper_page.read_text(encoding="utf-8")


def test_export_paper_cleans_abstract_artifacts(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        session.add(
            Paper(
                arxiv_id="2407.18480",
                title="Scalable Graph Compressed Convolutions",
                abstract=(
                    "Designing effective graph neural networks~(GNNs) is challenging. "
                    r"GQT (\textbf{G}raph \textbf{Q}uantized \textbf{T}okenizer) improves "
                    r"results by 82.47\% over a 10\times range. Code is available "
                    "at~https://example.com."
                ),
                extraction_status="extracted",
                discovery_source="integration-test",
                published_date="2024-07-01",
            )
        )

    from backend.export_to_hugo import export_paper

    assert export_paper("2407.18480") is True

    paper_page = cfg.site_dir / "content" / "papers" / "2407.18480" / "index.md"
    page_text = paper_page.read_text(encoding="utf-8")
    normalized_page_text = page_text.replace("\n  ", " ")

    assert "graph neural networks~(GNNs)" not in page_text
    assert "at~https://example.com" not in page_text
    assert r"\textbf{G}" not in page_text
    assert r"\%" not in page_text
    assert r"\times" not in page_text
    assert "graph neural networks (GNNs) is challenging." in normalized_page_text
    assert (
        "GQT (Graph Quantized Tokenizer) improves results by 82.47% over a 10 x range."
        in normalized_page_text
    )
    assert "available at https://example.com." in normalized_page_text
