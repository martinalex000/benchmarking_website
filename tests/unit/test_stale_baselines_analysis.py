from pathlib import Path
from types import SimpleNamespace

import matplotlib.pyplot as plt
import pytest

import backend.stale_baselines_analysis as stale_baselines_analysis
from backend.at_pub_timeline import AtPubTimeline
from backend.stale_baselines_analysis import (
    CATEGORY_LABELS,
    SELECTED_DATASET_GROUPS,
    _comparison_row,
    _filtered_truth,
    _gap_closed_percentage,
    _grouped_counts,
    _histogram_percentage_weights,
    _materially_worse,
    _normalized_category_values,
    _ordered_selected_dataset_groups,
    _selected_dataset_paper_counts,
    _selected_gap_closure_values,
    plot_selected_gap_closure_histogram,
    summarize,
)


def _row(*, paper: str, category: str, prior_value: float | None) -> dict:
    return {
        "paper": paper,
        "category": category,
        "prior_value": prior_value,
        "prior_days_available": 100,
        "benchmark": "lrgb",
        "group": "Peptides-func",
    }


def test_materially_worse_accounts_for_metric_direction_and_uncertainty() -> None:
    assert _materially_worse(0.80, 0.90, True, None, None)
    assert _materially_worse(0.20, 0.10, False, None, None)
    assert not _materially_worse(0.89, 0.90, True, 0.02, None)


def test_materially_worse_uses_counts_and_fixed_reference_rule() -> None:
    assert not _materially_worse(0.8, 0.81, True, 0.02, 0.02)
    assert _materially_worse(0.8, 0.81, True, 0.02, 0.02, 100, 100)
    assert _materially_worse(0.81, 0.8, False, 0.02, 0.02, 100, 100)
    assert not _materially_worse(0.8, 0.81, True, 0.02, None, None, 100)
    assert _materially_worse(0.8, 0.81, True, None, None)


def test_reference_and_comparison_records_preserve_repetition_counts() -> None:
    result = SimpleNamespace(
        paper=SimpleNamespace(
            arxiv_id="test", title="Test", venue="ICLR", published_date="2024-01-01"
        ),
        model=SimpleNamespace(canonical_name="GCN"),
        effective_model_name="GCN",
        dataset_variant=SimpleNamespace(
            dataset=SimpleNamespace(name="Cora", task_type="node_classification", benchmark=None)
        ),
        display_value=0.8,
        display_std=0.02,
        num_runs=100,
        higher_is_better=True,
        metric_name="Accuracy",
    )
    historical = AtPubTimeline([result], True).best_for_model("gcn")
    current = _filtered_truth([result], True)["gcn"]
    assert historical["num_runs"] == current["num_runs"] == 100
    reference = {**historical, "value": 0.81, "arxiv_id": "reference"}
    comparison = _comparison_row(
        result, today_truth=reference, prior_truth=reference, sota_truth=reference
    )
    assert comparison["category"] == "prior_better"
    for prefix in ("reported", "prior", "today", "sota"):
        assert comparison[f"{prefix}_num_runs"] == 100


def test_gap_closed_percentage_accounts_for_metric_direction() -> None:
    assert _gap_closed_percentage(0.70, 0.80, 0.90, True) == pytest.approx(50.0)
    assert _gap_closed_percentage(0.90, 0.80, 0.70, False) == pytest.approx(50.0)
    assert _gap_closed_percentage(0.70, 0.70, 0.90, True) == pytest.approx(0.0)
    assert _gap_closed_percentage(0.70, 0.90, 0.90, True) == pytest.approx(100.0)
    assert _gap_closed_percentage(0.70, None, 0.90, True) is None


def test_gap_closure_values_include_only_prior_better_results() -> None:
    rows = [
        {"dataset": "Cora", "category": "prior_better", "gap_closed_pct": 25.0},
        {"dataset": "Cora", "category": "future_only", "gap_closed_pct": None},
        {"dataset": "MUTAG", "category": "prior_better", "gap_closed_pct": 75.0},
        {"dataset": "Other", "category": "prior_better", "gap_closed_pct": 90.0},
    ]

    assert _selected_gap_closure_values(rows) == [25.0, 75.0]
    assert _selected_gap_closure_values(rows, ["Cora"]) == [25.0]


def test_histogram_percentage_weights_normalize_each_distribution() -> None:
    assert _histogram_percentage_weights([10.0, 20.0, 30.0]).sum() == pytest.approx(100.0)
    assert len(_histogram_percentage_weights([])) == 0


def test_selected_gap_closure_histogram_uses_absolute_y_axis(monkeypatch, tmp_path: Path) -> None:
    captured: dict[str, object] = {}

    def capture_figure(fig, output_dir, stem, *, tight=True):
        captured["figure"] = fig
        return []

    monkeypatch.setattr(stale_baselines_analysis, "_save_figure", capture_figure)
    plot_selected_gap_closure_histogram(
        [{"dataset": "Cora", "category": "prior_better", "gap_closed_pct": 25.0}],
        tmp_path,
    )

    figure = captured["figure"]
    axis = figure.axes[0]
    assert axis.get_ylabel() == "Number of results"
    assert axis.yaxis.get_major_formatter().__class__.__name__ == "ScalarFormatter"
    plt.close(figure)


def test_summary_reports_row_and_paper_level_rates() -> None:
    rows = [
        _row(paper="a", category="prior_better", prior_value=0.9),
        _row(paper="a", category="no_gap", prior_value=0.8),
        _row(paper="b", category="future_only", prior_value=None),
    ]

    summary = summarize(rows)

    assert summary["overall"]["prior_better"] == 1
    assert summary["overall"]["prior_reference_rows"] == 2
    assert summary["overall"]["prior_rate_given_reference"] == 0.5
    assert summary["paper_level"]["lrgb"]["papers_with_prior_better"] == 1
    assert summary["paper_level"]["lrgb"]["papers_with_any_gap"] == 2


def test_paper_counts_give_red_precedence_over_yellow() -> None:
    rows = [
        {"paper": "a", "benchmark": "lrgb", "dataset": "P", "category": "prior_better"},
        {"paper": "a", "benchmark": "lrgb", "dataset": "P", "category": "future_only"},
        {"paper": "b", "benchmark": "lrgb", "dataset": "P", "category": "future_only"},
    ]

    counts = _grouped_counts(rows, dimension="benchmark", unit="papers")

    assert counts["LRGB"] == {
        "prior_better": 1,
        "future_only": 1,
        "no_gap": 0,
        "total": 2,
        "papers": 2,
    }


def test_selected_dataset_counts_preserve_requested_blocks() -> None:
    rows = [
        {"paper": "cora-paper", "dataset": "Cora", "category": "prior_better"},
        {"paper": "ogb-paper", "dataset": "ogbn-arxiv", "category": "future_only"},
        {"paper": "tu-paper", "dataset": "MUTAG", "category": "no_gap"},
    ]

    counts, groups = _selected_dataset_paper_counts(rows)

    assert [name for name, datasets in groups if datasets] == [
        "Citation datasets",
        "TU datasets",
        "OGB",
    ]
    assert counts["Cora"]["prior_better"] == 1
    assert counts["ogbn-arxiv"]["future_only"] == 1
    assert counts["MUTAG"]["no_gap"] == 1


def test_selected_dataset_ogb_subset_is_compact() -> None:
    groups = dict(SELECTED_DATASET_GROUPS)

    assert groups["OGB"] == (
        "ogbg-molhiv",
        "ogbg-molpcba",
        "ogbn-products",
        "ogbn-papers100M",
        "ogbn-arxiv",
    )


def test_selected_dataset_result_counts_keep_multiple_rows_from_one_paper() -> None:
    rows = [
        {"paper": "a", "dataset": "Cora", "category": "prior_better"},
        {"paper": "a", "dataset": "Cora", "category": "future_only"},
    ]

    counts, _ = _selected_dataset_paper_counts(rows, unit="entries")

    assert counts["Cora"]["prior_better"] == 1
    assert counts["Cora"]["future_only"] == 1
    assert counts["Cora"]["total"] == 2


def test_selected_dataset_order_sorts_only_requested_groups() -> None:
    counts = {
        "Cora": {"total": 1},
        "MUTAG": {"total": 2},
        "NCI1": {"total": 1},
        "COCO-SP": {"total": 3},
        "PCQM-Contact": {"total": 1},
        "Peptides-func": {"total": 2},
        "Peptides-struct": {"total": 1},
    }
    groups = [
        ("Citation datasets", ["Cora"]),
        ("TU datasets", ["MUTAG", "NCI1"]),
        ("LRGB", ["PCQM-Contact", "COCO-SP", "Peptides-func", "Peptides-struct"]),
    ]

    ordered = _ordered_selected_dataset_groups(counts, groups)

    assert ordered[1][1] == ["MUTAG", "NCI1"]
    assert ordered[2][1] == ["COCO-SP", "Peptides-func", "PCQM-Contact", "Peptides-struct"]


def test_category_labels_use_publication_timing_language() -> None:
    assert CATEGORY_LABELS["prior_better"] == "Better result available at publication"
    assert CATEGORY_LABELS["future_only"] == "Better result since publication"


def test_normalized_category_values_sum_to_one_hundred() -> None:
    values = _normalized_category_values(
        {"prior_better": 2, "future_only": 1, "no_gap": 1, "total": 4}
    )

    assert sum(values.values()) == 100
