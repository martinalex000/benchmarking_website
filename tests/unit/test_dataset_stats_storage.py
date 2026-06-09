"""Unit tests for dataset statistics workspace storage."""

from pathlib import Path

from backend.dataset_stats_storage import DatasetStatsStorage, slugify_dataset_name


def test_slugify_dataset_name():
    assert slugify_dataset_name("Peptides-func") == "peptides-func"
    assert slugify_dataset_name("ogbg-molhiv") == "ogbg-molhiv"


def test_save_and_load_paper_stats(tmp_path: Path):
    storage = DatasetStatsStorage(datasets_root=tmp_path / "datasets")
    payload = DatasetStatsStorage.build_payload(
        arxiv_id="2206.08164",
        paper_title="Test Paper",
        dataset_entry={
            "name": "Peptides-func",
            "num_graphs": 15535,
            "avg_nodes": 150.94,
        },
        extraction_model="test-model",
    )
    path = storage.save_paper_stats("Peptides-func", "2206.08164", payload)
    assert path.exists()
    assert path == tmp_path / "datasets" / "peptides-func" / "papers" / "2206.08164.yaml"

    loaded = storage.load_paper_stats("Peptides-func", "2206.08164")
    assert loaded is not None
    assert loaded["num_graphs"] == 15535
    assert loaded["arxiv_id"] == "2206.08164"


def test_list_paper_stats_for_arxiv(tmp_path: Path):
    storage = DatasetStatsStorage(datasets_root=tmp_path / "datasets")
    for dataset_name in ("Peptides-func", "ZINC"):
        storage.save_paper_stats(
            dataset_name,
            "1234.56789",
            {"name": dataset_name, "num_graphs": 100},
        )
    found = storage.list_paper_stats_for_arxiv("1234.56789")
    assert len(found) == 2
    assert {slug for slug, _ in found} == {"peptides-func", "zinc"}
