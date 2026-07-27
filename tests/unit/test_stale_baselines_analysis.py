from backend.stale_baselines_analysis import (
    CATEGORY_LABELS,
    SELECTED_DATASET_GROUPS,
    _grouped_counts,
    _materially_worse,
    _ordered_selected_dataset_groups,
    _selected_dataset_paper_counts,
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
