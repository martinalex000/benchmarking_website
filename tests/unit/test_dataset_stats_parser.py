"""Unit tests for dataset statistics DB ingest."""

from pathlib import Path

from backend.dataset_stats_parser import (
    _zinc_variant_by_graph_count,
    parse_and_store_dataset_statistics,
)
from backend.dataset_stats_storage import DatasetStatsStorage
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Paper, PaperDatasetStatistics


def _seed_zinc_dataset(session) -> None:
    bm = Benchmark(name="GNN Benchmark", short_name="GNNB", description="test")
    session.add(bm)
    session.flush()
    ds = Dataset(name="ZINC", benchmark_id=bm.id)
    session.add(ds)
    session.flush()
    session.add(
        DatasetVariant(
            dataset_id=ds.id,
            name="Subset (12k)",
            num_graphs=12000,
            avg_nodes=23.2,
            avg_edges=49.8,
            is_standard=0,
        )
    )
    session.add(
        DatasetVariant(
            dataset_id=ds.id,
            name="Full",
            num_graphs=249456,
            avg_nodes=23.2,
            avg_edges=49.8,
            is_standard=1,
        )
    )
    paper = Paper(arxiv_id="2012.07397", title="Test Paper", extraction_status="extracted")
    session.add(paper)


def test_zinc_variant_by_graph_count():
    ds = Dataset(name="ZINC")
    ds.variants = [
        DatasetVariant(name="Subset (12k)", is_standard=0),
        DatasetVariant(name="Full", is_standard=1),
    ]
    assert _zinc_variant_by_graph_count(ds, 249455).name == "Full"
    assert _zinc_variant_by_graph_count(ds, 250000).name == "Full"
    assert _zinc_variant_by_graph_count(ds, 12000).name == "Subset (12k)"
    assert _zinc_variant_by_graph_count(ds, 120000) is None


def test_parse_and_store_zinc_ambiguous_size_has_no_variant(tmp_path: Path, monkeypatch):
    root = tmp_path / "workspace"
    datasets_dir = root / "datasets"
    db_path = root / "data" / "benchmarks.db"
    db_path.parent.mkdir(parents=True)

    from backend.config import cfg

    monkeypatch.setattr(cfg, "db_path", db_path)
    monkeypatch.setattr(cfg, "datasets_dir", datasets_dir)

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))
    with session_scope() as session:
        _seed_zinc_dataset(session)
        session.query(Paper).filter_by(arxiv_id="2012.07397").update({"arxiv_id": "1805.09076"})

    storage = DatasetStatsStorage(datasets_dir)
    storage.save_paper_stats(
        "ZINC",
        "1805.09076",
        {
            "name": "ZINC",
            "variant": "Standard split",
            "num_graphs": 120000,
            "avg_nodes": 22.7,
            "avg_edges": 49.3,
            "extracted_at": "2026-01-01T00:00:00Z",
        },
    )

    summary = parse_and_store_dataset_statistics("1805.09076")
    assert summary.stored == 1
    assert summary.mismatched == 1

    with session_scope() as session:
        row = session.query(PaperDatasetStatistics).one()
        assert row.dataset_variant_id is None
        assert row.match_status == "mismatch"


def test_parse_and_store_zinc_assigns_full_variant(tmp_path: Path, monkeypatch):
    root = tmp_path / "workspace"
    datasets_dir = root / "datasets"
    db_path = root / "data" / "benchmarks.db"
    db_path.parent.mkdir(parents=True)

    from backend.config import cfg

    monkeypatch.setattr(cfg, "db_path", db_path)
    monkeypatch.setattr(cfg, "datasets_dir", datasets_dir)

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))
    with session_scope() as session:
        _seed_zinc_dataset(session)

    storage = DatasetStatsStorage(datasets_dir)
    storage.save_paper_stats(
        "ZINC",
        "2012.07397",
        {
            "name": "ZINC",
            "variant": "Standard split",
            "num_graphs": 249455,
            "avg_nodes": 24.3,
            "avg_edges": 25.1,
            "extracted_at": "2026-01-01T00:00:00Z",
        },
    )

    summary = parse_and_store_dataset_statistics("2012.07397")
    assert summary.stored == 1

    with session_scope() as session:
        row = session.query(PaperDatasetStatistics).one()
        variant = session.get(DatasetVariant, row.dataset_variant_id)
        assert variant is not None
        assert variant.name == "Full"
        assert row.num_graphs == 249455


def _seed_peptides_dataset(session) -> None:
    bm = Benchmark(name="LRGB", short_name="LRGB", description="test")
    session.add(bm)
    session.flush()
    ds = Dataset(
        name="Peptides-func",
        benchmark_id=bm.id,
        num_graphs=15535,
        avg_nodes=150.94,
        avg_edges=307.30,
        num_classes=10,
    )
    session.add(ds)
    session.flush()
    variant = DatasetVariant(dataset_id=ds.id, name="Standard split", is_standard=1)
    session.add(variant)
    paper = Paper(arxiv_id="2206.08164", title="Test Paper", extraction_status="extracted")
    session.add(paper)


def test_parse_and_store_dataset_statistics_matched(tmp_path: Path, monkeypatch):
    root = tmp_path / "workspace"
    datasets_dir = root / "datasets"
    db_path = root / "data" / "benchmarks.db"
    db_path.parent.mkdir(parents=True)

    from backend.config import cfg

    monkeypatch.setattr(cfg, "db_path", db_path)
    monkeypatch.setattr(cfg, "datasets_dir", datasets_dir)

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))
    with session_scope() as session:
        _seed_peptides_dataset(session)

    storage = DatasetStatsStorage(datasets_dir)
    storage.save_paper_stats(
        "Peptides-func",
        "2206.08164",
        {
            "name": "Peptides-func",
            "num_graphs": 15535,
            "avg_nodes": 150.94,
            "avg_edges": 307.30,
            "num_classes": 10,
            "extra_stats": {"heterophily": 0.42},
            "extracted_at": "2026-01-01T00:00:00Z",
        },
    )

    summary = parse_and_store_dataset_statistics("2206.08164")
    assert summary.stored == 1
    assert summary.matched == 1
    assert summary.mismatched == 0

    with session_scope() as session:
        row = session.query(PaperDatasetStatistics).one()
        assert row.match_status == "matched"
        variant = session.query(DatasetVariant).filter_by(name="Standard split").one()
        assert variant.extra_stats is not None
        assert "heterophily" in variant.extra_stats


def test_parse_and_store_flags_abbreviated_mismatch(tmp_path: Path, monkeypatch):
    root = tmp_path / "workspace"
    datasets_dir = root / "datasets"
    db_path = root / "data" / "benchmarks.db"
    db_path.parent.mkdir(parents=True)

    from backend.config import cfg

    monkeypatch.setattr(cfg, "db_path", db_path)
    monkeypatch.setattr(cfg, "datasets_dir", datasets_dir)

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))
    with session_scope() as session:
        _seed_peptides_dataset(session)

    storage = DatasetStatsStorage(datasets_dir)
    storage.save_paper_stats(
        "Peptides-func",
        "2206.08164",
        {
            "name": "Peptides-func",
            "num_graphs": 1000,
            "raw_values": {"num_graphs": "1k"},
            "precision_hints": {"num_graphs": "abbreviated"},
            "extracted_at": "2026-01-01T00:00:00Z",
        },
    )

    summary = parse_and_store_dataset_statistics("2206.08164")
    assert summary.stored == 1
    assert summary.mismatched == 1

    with session_scope() as session:
        row = session.query(PaperDatasetStatistics).one()
        assert row.match_status == "mismatch"
