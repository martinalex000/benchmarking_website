"""Unit tests for baseline aggregator helpers."""

from types import SimpleNamespace

import pytest

from backend.baseline_aggregator import (
    BaselineGroup,
    _merge_similar_groups,
    _milestones_from_results,
)


def make_group(name: str, values: list, model_id: int = 1, higher: bool = True) -> BaselineGroup:
    g = BaselineGroup(canonical_name=name, model_id=model_id, higher_is_better=higher)
    g.values = values
    g.stds = [None] * len(values)
    g.paper_ids = list(range(len(values)))
    g.arxiv_ids = [str(i) for i in range(len(values))]
    return g


def test_group_best_higher():
    g = make_group("GCN", [0.6, 0.7, 0.65], higher=True)
    assert g.best == pytest.approx(0.7)
    assert g.worst == pytest.approx(0.6)


def test_group_best_lower():
    g = make_group("GCN", [0.3, 0.2, 0.25], higher=False)
    assert g.best == pytest.approx(0.2)
    assert g.worst == pytest.approx(0.3)


def test_group_mean():
    g = make_group("GCN", [0.6, 0.7])
    assert g.mean == pytest.approx(0.65)


def test_group_std_across_papers():
    g = make_group("GCN", [0.6, 0.8])
    expected_std = pytest.approx(0.1414, abs=1e-3)
    assert g.std_across_papers == expected_std


def test_merge_similar_groups():
    g1 = make_group("GraphSAGE", [0.75], model_id=1)
    g2 = make_group("Graph SAGE", [0.76], model_id=2)  # similar name
    g3 = make_group("GCN", [0.65], model_id=3)  # different

    merged = _merge_similar_groups([g1, g2, g3], threshold=85)
    assert len(merged) == 2
    combined = next(g for g in merged if "sage" in g.canonical_name.lower())
    assert len(combined.values) == 2


def test_merge_no_overlap():
    g1 = make_group("GCN", [0.65], model_id=1)
    g2 = make_group("GAT", [0.70], model_id=2)
    merged = _merge_similar_groups([g1, g2], threshold=85)
    assert len(merged) == 2


def test_representative_std_from_best():
    g = make_group("Model", [0.8, 0.9])
    g.stds = [None, 0.01]  # std for the best (0.9) is 0.01
    assert g.representative_std == pytest.approx(0.01)


def test_merge_does_not_combine_gcn_and_gin_virtual():
    g1 = make_group("GCN + Virtual Node", [0.75], model_id=1)
    g2 = make_group("GIN + Virtual Node", [0.76], model_id=2)
    merged = _merge_similar_groups([g1, g2], threshold=85)
    assert len(merged) == 2


def test_merge_combines_gcn_virt_spelling_variants():
    g1 = make_group("GCN + Virtual Node", [0.75], model_id=1)
    g2 = make_group("GCN + Virt. Node", [0.76], model_id=2)
    merged = _merge_similar_groups([g1, g2], threshold=85)
    assert len(merged) == 1
    assert len(merged[0].values) == 2


def test_milestones_use_override_std():
    result = SimpleNamespace(
        higher_is_better=True,
        display_value=0.9,
        display_std=0.01,
        metric_std=0.5,
        paper=SimpleNamespace(
            arxiv_id="2401.00001",
            title="Paper",
            published_date="2024-01-01",
        ),
        model=SimpleNamespace(canonical_name="GIN"),
    )

    milestones = _milestones_from_results([result])

    assert milestones[0]["value"] == pytest.approx(0.9)
    assert milestones[0]["std"] == pytest.approx(0.01)
