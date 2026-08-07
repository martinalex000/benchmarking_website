"""Tests for historical SOTA architecture ownership analysis."""

from datetime import date

import pytest

from backend.model_metadata_defaults import lookup_default_model_type
from backend.sota_architecture_analysis import (
    AnalysisRow,
    analyze_snapshots,
    architecture_category,
    compare_override_effects,
    historical_cutoffs,
    monthly_cutoffs,
    square_root_weight,
)
from experiments.analysis.analyze_sota_architecture import PLOT_CATEGORY_MAP, _postprocess_output


def row(
    dataset_id: int,
    dataset: str,
    paper_id: int,
    published: str,
    value: float,
    model_type: str | None,
    *,
    std: float | None = None,
    higher: bool = True,
    level: str | None = "node",
    model: str | None = None,
) -> AnalysisRow:
    return AnalysisRow(
        dataset_id=dataset_id,
        dataset=dataset,
        metric="Accuracy",
        higher_is_better=higher,
        value=value,
        std=std,
        paper_id=paper_id,
        arxiv_id=f"{paper_id:04d}.0001",
        paper_date=date.fromisoformat(published),
        model=model or f"model-{paper_id}",
        model_type=model_type,
        model_type_before_override=model_type,
        task_level=level,
    )


def test_architecture_category_combines_transformers():
    assert architecture_category("graph_transformer") == "transformer_involving"
    assert architecture_category("hybrid") == "transformer_involving"
    assert architecture_category(None) == "unknown"


def test_gat_is_classified_as_message_passing_gnn():
    assert lookup_default_model_type("GAT") == "gnn"


def test_plot_category_labels_collapse_to_six_paper_labels():
    assert PLOT_CATEGORY_MAP == {
        "gnn": "MPGNN",
        "transformer_involving": "Transformer",
        "llm": "LLM",
        "walk": "Walk",
        "svm_kernel": "Traditional",
        "random_forest": "Traditional",
        "decision_tree": "Traditional",
        "boosting": "Traditional",
        "other_traditional": "Traditional",
        "unknown": "Unknown",
    }


def test_crop_fallback_keeps_raw_output_when_tool_is_missing(tmp_path):
    raw = tmp_path / "raw.png"
    final = tmp_path / "final.png"
    raw.write_bytes(b"raw image")

    _postprocess_output(raw, final, "missing-crop-tool", [])

    assert final.read_bytes() == b"raw image"


def test_task_level_filter_keeps_only_requested_tasks():
    rows = [
        row(1, "Cora", 1, "2020-01-01", 0.8, "gnn", level="node"),
        row(2, "MUTAG", 2, "2020-02-01", 0.8, "hybrid", level="graph"),
    ]

    snapshot = analyze_snapshots(
        rows,
        cutoffs=[date(2020, 12, 31)],
        min_papers=1,
        task_level="graph",
    )[0]

    assert [item.dataset for item in snapshot.ownership] == ["MUTAG"]


def test_square_root_weight():
    assert square_root_weight(9) == pytest.approx(3.0)


def test_historical_cutoffs_use_year_end_and_latest_date():
    rows = [
        row(1, "Cora", 1, "2020-05-01", 0.7, "gnn"),
        row(1, "Cora", 2, "2021-05-01", 0.8, "hybrid"),
    ]
    assert historical_cutoffs(rows) == [date(2020, 12, 31), date(2021, 5, 1)]


def test_monthly_cutoffs_end_at_latest_partial_month():
    rows = [
        row(1, "Cora", 1, "2026-01-15", 0.7, "gnn"),
        row(1, "Cora", 2, "2026-02-15", 0.8, "gnn"),
        row(1, "Cora", 3, "2026-05-30", 0.9, "hybrid"),
    ]

    assert monthly_cutoffs(rows) == [
        date(2026, 1, 31),
        date(2026, 2, 28),
        date(2026, 3, 31),
        date(2026, 4, 30),
        date(2026, 5, 30),
    ]


def test_tied_winner_weight_is_split_by_model():
    rows = [
        row(1, "Cora", 1, "2020-01-01", 0.8, "gnn", std=0.02),
        row(1, "Cora", 2, "2020-02-01", 0.79, "hybrid", std=0.02),
        row(1, "Cora", 3, "2020-03-01", 0.78, "gnn", std=0.02),
    ]
    snapshots = analyze_snapshots(
        rows, cutoffs=[date(2020, 12, 31)], min_papers=3, weight="uniform"
    )
    snapshot = snapshots[0]
    assert snapshot.shares["gnn"] == pytest.approx(2 / 3)
    assert snapshot.shares["transformer_involving"] == pytest.approx(1 / 3)


def test_repeated_winning_rows_for_same_model_receive_one_share():
    rows = [
        row(1, "Cora", 1, "2020-01-01", 0.8, "gnn", std=0.02, model="Repeated GNN"),
        row(1, "Cora", 2, "2020-02-01", 0.8, "gnn", std=0.02, model="Repeated GNN"),
        row(1, "Cora", 3, "2020-03-01", 0.79, "hybrid", std=0.02, model="GT"),
    ]

    snapshot = analyze_snapshots(
        rows, cutoffs=[date(2020, 12, 31)], min_papers=3, weight="uniform"
    )[0]

    assert snapshot.ownership[0].winner_model_types == (
        ("GT", "transformer_involving"),
        ("Repeated GNN", "gnn"),
    )
    assert snapshot.shares["gnn"] == pytest.approx(0.5)
    assert snapshot.shares["transformer_involving"] == pytest.approx(0.5)


def test_single_mean_winner_does_not_share_ties():
    rows = [
        row(1, "Cora", 1, "2020-01-01", 0.8, "gnn", std=0.1),
        row(1, "Cora", 2, "2020-02-01", 0.79, "hybrid", std=0.1),
        row(1, "Cora", 3, "2020-03-01", 0.6, "walk"),
    ]

    snapshot = analyze_snapshots(
        rows,
        cutoffs=[date(2020, 12, 31)],
        min_papers=3,
        winner_policy="single_mean",
    )[0]

    assert snapshot.shares == {"gnn": 1.0}


def test_dataset_requires_minimum_papers_at_cutoff():
    rows = [
        row(1, "Cora", 1, "2020-01-01", 0.8, "gnn"),
        row(1, "Cora", 2, "2021-01-01", 0.9, "hybrid"),
    ]
    snapshots = analyze_snapshots(
        rows,
        cutoffs=[date(2020, 12, 31), date(2021, 12, 31)],
        min_papers=2,
    )
    assert snapshots[0].ownership == ()
    assert snapshots[1].ownership[0].winner_types == ("transformer_involving",)


def test_lower_is_better_selects_smallest_value():
    rows = [
        row(1, "QM9", 1, "2020-01-01", 0.4, "gnn", higher=False),
        row(1, "QM9", 2, "2020-02-01", 0.3, "hybrid", higher=False),
        row(1, "QM9", 3, "2020-03-01", 0.5, "walk", higher=False),
    ]
    snapshot = analyze_snapshots(rows, cutoffs=[date(2020, 12, 31)], min_papers=3)[0]
    assert snapshot.ownership[0].winner_types == ("transformer_involving",)


def test_override_audit_counts_unknown_winner_that_becomes_classified():
    before = [
        row(1, "Cora", 1, "2020-01-01", 0.8, None),
        row(1, "Cora", 2, "2020-02-01", 0.7, "gnn"),
        row(1, "Cora", 3, "2020-03-01", 0.6, "gnn"),
    ]
    after = [
        row(1, "Cora", 1, "2020-01-01", 0.8, "hybrid"),
        *before[1:],
    ]

    audit = compare_override_effects(before, after, min_papers=3)

    assert audit.unknown_winner_states_before == 1
    assert audit.classified_from_unknown_states == 1
    assert audit.changed_current_datasets == 1
    assert audit.transformer_share_before == pytest.approx(0.0)
    assert audit.transformer_share_after == pytest.approx(1.0)
