"""Integration test for dataset statistics export helpers."""

from pathlib import Path

import backend.export_to_hugo as hugo_export
from backend.config import cfg
from backend.db import init_db, session_scope
from backend.export_to_hugo import _build_export_stats
from backend.hugo_dev_exports import _export_statistics_sources_page
from backend.models import Benchmark, Dataset, Paper, PaperDatasetStatistics


def _configure_workspace(monkeypatch, tmp_path: Path) -> None:
    root = tmp_path / "workspace"
    site_dir = root / "site"
    data_dir = root / "data"
    for directory in (site_dir, data_dir, site_dir / "content" / "dev"):
        directory.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "data_dir", data_dir)
    monkeypatch.setattr(cfg, "site_dir", site_dir)
    monkeypatch.setattr(cfg, "db_path", data_dir / "benchmarks.db")
    monkeypatch.setattr(hugo_export, "_SITE_DIR", site_dir)
    monkeypatch.setattr(hugo_export, "_CONTENT", site_dir / "content")
    monkeypatch.setattr(hugo_export, "_DATA_DIR", site_dir / "data")

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None


def test_build_export_stats_includes_extra_stats():
    ds = Dataset(name="Test", num_graphs=100, extra_stats='{"heterophily": 0.5}')
    stats = _build_export_stats(ds)
    assert stats["num_graphs"] == 100
    assert stats["extra_stats"] == {"heterophily": 0.5}


def test_statistics_sources_dev_page(tmp_path: Path, monkeypatch):
    _configure_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        bm = Benchmark(name="LRGB", short_name="LRGB", description="test")
        session.add(bm)
        session.flush()
        ds = Dataset(
            name="Peptides-func",
            benchmark_id=bm.id,
            num_graphs=15535,
            avg_nodes=150.94,
        )
        session.add(ds)
        session.flush()
        paper = Paper(
            arxiv_id="2206.08164",
            title="Graph Paper",
            venue="NeurIPS",
            published_date="2024-06-01",
            extraction_status="extracted",
        )
        session.add(paper)
        session.flush()
        session.add(
            PaperDatasetStatistics(
                paper_id=paper.id,
                dataset_id=ds.id,
                num_graphs=3000,
                raw_values='{"num_graphs": "3k"}',
                precision_hints='{"num_graphs": "abbreviated"}',
                match_status="matched",
                match_details='{"num_graphs": "3k ↔ 15535 via abbreviated"}',
            )
        )

        content_dev = tmp_path / "workspace" / "site" / "content" / "dev"
        _export_statistics_sources_page(session, hugo_export, content_dev)

    out = content_dev / "statistics-sources.md"
    assert out.exists()
    body = out.read_text(encoding="utf-8")
    assert "Statistics Sources & Discrepancies" in body
    assert "Peptides-func" in body
    assert "graphs=3k" in body
    assert "NeurIPS 2024" in body
