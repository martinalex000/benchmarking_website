"""Regression checks for extraction coverage and compatibility-independent counting."""

import json

import pandas as pd
from sqlalchemy import create_engine

from backend.models import Base
from experiments.datasets_over_time_ablation.datasets_over_time_ablation import (
    build_usage,
    compare_counts,
    dataset_name_map,
    load_database,
    original_settings,
    plot_comparison,
    read_extraction,
    resolve_name,
)


def test_shared_plot_scale_includes_the_larger_ablation(tmp_path, monkeypatch):
    import matplotlib.pyplot as plt

    periods = pd.period_range("2022", "2023", freq="Y")
    current = pd.DataFrame({"A": [1, 2]}, index=periods)
    ablation = pd.DataFrame({"A": [10, 20]}, index=periods)
    figures = []
    original_close = plt.close
    monkeypatch.setattr(plt, "close", lambda figure: figures.append(figure))
    plot_comparison(
        [(current, current, current), (ablation, ablation, ablation)],
        ["A"],
        "dataset",
        tmp_path,
        {},
    )
    for figure in figures:
        if hasattr(figure, "axes"):
            assert figure.axes[0].get_ylim()[1] > 20
            assert list(figure.axes[0].get_xticks()) == [2022, 2023]
            original_close(figure)


def test_database_reader_uses_the_supplied_snapshot(tmp_path):
    snapshot = tmp_path / "snapshot.db"
    engine = create_engine(f"sqlite:///{snapshot}")
    Base.metadata.create_all(engine)
    engine.dispose()
    papers, datasets, variants, (stored, eligible) = load_database(snapshot)
    assert papers.empty and datasets.empty and variants.empty and stored.empty
    assert eligible == set()


def write_extraction(root, arxiv_id, entries):
    path = root / arxiv_id / "extracted" / "llm_output.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"arxiv_id": arxiv_id, "results": {"results": entries}}))


def test_missing_empty_and_invalid_extractions_are_distinct(tmp_path):
    assert read_extraction(tmp_path, "missing")[1] == "missing_file"
    write_extraction(tmp_path, "empty", [])
    assert read_extraction(tmp_path, "empty")[:2] == ([], "available_empty")
    write_extraction(tmp_path, "invalid", ["not a result"])
    assert read_extraction(tmp_path, "invalid")[:2] == (None, "invalid_result_list")
    write_extraction(tmp_path, "wrong", [])
    path = tmp_path / "wrong/extracted/llm_output.json"
    path.write_text(json.dumps({"arxiv_id": "other", "results": {"results": []}}))
    assert read_extraction(tmp_path, "wrong")[1] == "paper_id_mismatch"
    yaml_path = tmp_path / "wrong/extracted/llm_output.yaml"
    yaml_path.write_text("!!python/object:builtins.object {}")
    assert read_extraction(tmp_path, "wrong")[1] == "unreadable_file"


def test_ablation_ignores_compatibility_and_falls_back_only_when_unavailable(tmp_path):
    papers = pd.DataFrame(
        [
            {
                "paper_id": i,
                "arxiv_id": str(i),
                "paper_timestamp": pd.Timestamp("2023-01-01"),
                "paper_title": str(i),
                "paper_venue": "ICML 2023",
                "extraction_status": "extracted",
            }
            for i in range(1, 5)
        ]
    )
    datasets = pd.DataFrame({"dataset_name": ["A", "B"], "benchmark_name": ["Suite", "Suite"]})
    stored = pd.DataFrame({"paper_id": [1, 2, 3], "dataset_name": ["A", "A", "B"]})
    write_extraction(
        tmp_path,
        "1",
        [
            {"dataset": "B", "protocol_decision": "nonstandard", "value": 1},
            {"dataset": "B", "protocol_decision": "uncertain", "value": 2},
            {"dataset": "unknown", "value": 3},
        ],
    )
    write_extraction(tmp_path, "2", [])
    write_extraction(tmp_path, "4", [{"dataset": "B", "value": 1}])
    current, ablation, coverage, unresolved = build_usage(
        papers,
        stored,
        {(1, "A"), (2, "A")},
        datasets,
        {"a": "A", "b": "B"},
        {},
        tmp_path,
    )
    assert set(zip(current.paper_id, current.dataset_name, strict=True)) == {(1, "A"), (2, "A")}
    assert set(zip(ablation.paper_id, ablation.dataset_name, strict=True)) == {
        (1, "B"),
        (3, "B"),
        (4, "B"),
    }
    assert coverage.loc[coverage.fallback, "paper_id"].tolist() == [3]
    assert unresolved.raw_dataset.tolist() == ["unknown"]
    comparison, _ = compare_counts(current, ablation, "benchmark", ["Suite"], original_settings())
    row = comparison.loc[comparison.period == "2023"].iloc[0]
    assert row.current_count == 2
    assert row.ablation_count == 3
    assert row.ablation_union_share_pct == 100


def test_exact_names_aliases_and_ambiguous_variants():
    datasets = pd.DataFrame({"dataset_name": ["Actor", "MovieLens Film"]})
    variants = pd.DataFrame(
        {"variant_name": ["standard", "standard"], "dataset_name": datasets.dataset_name}
    )
    names = dataset_name_map(datasets, variants)
    assert "standard" not in names
    aliases = {"aliases": {"Film": "Actor"}, "paper_aliases": {"paper": {"Film": "MovieLens Film"}}}
    assert resolve_name("FILM", "other", names, aliases) == "Actor"
    assert resolve_name("film", "paper", names, aliases) == "MovieLens Film"
    assert resolve_name("Actor-like", "other", names, aliases) is None
