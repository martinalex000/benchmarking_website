"""Regression tests for curated benchmark membership and provenance metadata."""

from pathlib import Path

import yaml


def _benchmarks():
    path = Path(__file__).parents[2] / "config" / "seed_data.yaml"
    return {
        item["name"]: item
        for item in yaml.safe_load(path.read_text(encoding="utf-8"))["benchmarks"]
    }


def test_lrgb_datasets_include_canonical_statistics():
    datasets = {dataset["name"]: dataset for dataset in _benchmarks()["LRGB"]["datasets"]}

    assert {
        name: tuple(
            dataset[field] for field in ("num_graphs", "avg_nodes", "avg_edges", "num_classes")
        )
        for name, dataset in datasets.items()
    } == {
        "Peptides-func": (15535, 150.94, 307.30, 10),
        "Peptides-struct": (15535, 150.94, 307.30, 11),
        "PascalVOC-SP": (11355, 479.40, 2710.48, 21),
        "COCO-SP": (123286, 476.88, 2693.67, 81),
        "PCQM-Contact": (529434, 30.14, 61.09, 1),
    }


def test_heterophily_groups_have_curated_membership_and_sources():
    benchmarks = _benchmarks()

    legacy = benchmarks["Heterophilic Graphs"]
    assert legacy["is_legacy"] is True
    assert [item["name"] for item in legacy["datasets"]][:6] == [
        "Texas",
        "Wisconsin",
        "Cornell",
        "Actor",
        "Chameleon",
        "Squirrel",
    ]
    assert {item["arxiv_id"] for item in legacy["source_papers"]} == {
        "2002.05287",
        "2110.14446",
    }

    replacement = benchmarks["Heterophily Benchmark"]
    assert [item["name"] for item in replacement["datasets"]] == [
        "Roman-empire",
        "Amazon-ratings",
        "Minesweeper",
        "Tolokers",
        "Questions",
    ]
    assert replacement["source_papers"][0]["arxiv_id"] == "2302.11640"


def test_heterogeneous_group_uses_hgb_introduction_and_magnn_provenance():
    group = _benchmarks()["Heterogeneous Graph Benchmarks"]
    assert group["arxiv_id"] == "2112.14936"
    assert [item["arxiv_id"] for item in group["source_papers"]] == [
        "2112.14936",
        "2002.01680",
    ]
