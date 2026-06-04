"""Focused regression tests for export helper behavior."""

import shutil

import pytest

from backend.export_helpers import truncate_words as _truncate_words
from backend.export_to_hugo import (
    _benchmark_coverage_entries,
    _conference_export_fields,
    _dataset_export_metadata,
    _dedup_result_rows,
    _description_class_target_count,
    _fmt_date,
    _global_ranks_cached,
    _has_paper_value_difference,
    _has_paper_value_gap,
    _normalize_conference,
    _normalize_model_family,
    _plain_core_baseline_kind,
    _plain_model,
    _publication_year,
    _rank_for_value,
    _sanitize_model,
    _sanitize_title,
    _select_global_context_rows,
    clear_export_caches,
)


def test_sanitize_title_replaces_linebreaks_and_strips_commands():
    title = "Graph\\\\Learning \\emph{for} Molecules"

    assert _sanitize_title(title) == "Graph - Learning Molecules"


def test_truncate_words_uses_sanitized_title():
    title = "Graph\\\\Learning for Molecules and Materials"

    assert _truncate_words(title, 3) == "Graph - Learning..."


def test_sanitize_model_formats_subscripts_and_superscripts():
    model = "GNN$_{L}$ / Net\\textsubscript{small} / Model$^{2}$ / Deep\\textsuperscript{xl} ~\\cite{foo} (ours)"

    assert _sanitize_model(model) == (
        "GNN<sub>L</sub> / Net<sub>small</sub> / Model<sup>2</sup> / Deep<sup>xl</sup>"
    )
    assert _plain_model(_sanitize_model(model)) == "GNNL / Netsmall / Model2 / Deepxl"


def test_value_gap_respects_reported_uncertainty():
    assert _has_paper_value_gap(0.81, None, 0.8, None)
    assert not _has_paper_value_gap(0.81, 0.02, 0.8, None)
    assert not _has_paper_value_gap(0.81, None, 0.8, 0.02)
    assert not _has_paper_value_gap(None, None, 0.8, None)
    assert _has_paper_value_difference(0.81, 0.8)
    assert not _has_paper_value_difference(0.8, 0.8 + 1e-13)


def test_rank_for_value_replaces_existing_model_and_inserts_new_one():
    rows = [
        {"model_key": "gcn", "value": 0.8},
        {"model_key": "gin", "value": 0.75},
    ]

    assert _rank_for_value(rows, "gcn", 0.7, higher_is_better=True) == 2
    assert _rank_for_value(rows, "sage", 0.77, higher_is_better=True) == 2
    assert _rank_for_value(rows, "gin", 0.85, higher_is_better=True) == 1
    assert _rank_for_value(rows, "mae-model", 0.09, higher_is_better=False) == 1
    assert _rank_for_value(rows, "", 0.7, higher_is_better=True) is None


@pytest.mark.parametrize(
    ("description", "expected"),
    [
        ("Node classification on arXiv citation network (40 subject areas).", 40),
        ("Node classification on Amazon product co-purchase graph (47 categories).", 47),
        ("Protein-protein interaction node classification (121 GO labels, multi-label).", 121),
        ("Multi-task graph regression on peptide structural properties (11 targets).", 11),
        ("Analog circuit topology design across 3 circuit-size datasets.", None),
    ],
)
def test_description_class_target_count_extracts_only_relevant_summary_counts(
    description, expected
):
    assert _description_class_target_count(description) == expected


def test_fmt_date_uses_consistent_human_readable_output():
    assert _fmt_date("2025-01-30") == "Jan 30, 2025"
    assert _fmt_date("2025-01") == "Jan 2025"


@pytest.mark.parametrize(
    ("venue", "expected"),
    [
        ("NeurIPS 2024", "NeurIPS"),
        ("Neural Information Processing Systems", "NeurIPS"),
        ("ICLR 2023", "ICLR"),
        ("International Conference on Learning Representations", "ICLR"),
        ("Proceedings of the 40th International Conference on Machine Learning", "ICML"),
        ("International Conference on Machine Learning", "ICML"),
        ("Transactions on Machine Learning Research", "TMLR"),
        ("Trans. Mach. Learn. Res.", "TMLR"),
        ("Graph Learning Conference", "LoG"),
        ("ACM SIGKDD Conference", "KDD"),
        ("Knowledge Discovery and Data Mining", "KDD"),
        ("AAAI 2025", "AAAI"),
        ("AAAI Conference on Artificial Intelligence", "AAAI"),
        ("NeurIPS Datasets and Benchmarks", "NeurIPS"),
        ("LOG IN", ""),
        ("arXiv.org", ""),
        ("Workshop on Something", ""),
    ],
)
def test_normalize_conference_maps_common_venues(venue, expected):
    assert _normalize_conference(venue) == expected


@pytest.mark.parametrize(
    ("venue", "published_date", "expected"),
    [
        ("International Conference on Learning Representations", "2024-05-07", "ICLR 2024"),
        ("NeurIPS 2024", "2024-12-10", "NeurIPS 2024"),
        ("International Conference on Machine Learning", "2023-07-01", "ICML 2023"),
        ("arXiv.org", "2024-01-01", ""),
        ("ICLR 2023", "2023", "ICLR 2023"),
    ],
)
def test_conference_export_fields_include_year(venue, published_date, expected):
    assert _conference_export_fields(venue, published_date)["published_conference"] == expected


def test_publication_year_accepts_iso_dates_and_year_prefixes():
    assert _publication_year("2024-05-07") == "2024"
    assert _publication_year("2023") == "2023"
    assert _publication_year("") == ""


def test_dedup_result_rows_preserves_first_row_and_keeps_meaningful_differences():
    rows = [
        {
            "model_key": "signnet",
            "model": "SignNet",
            "metric": "MAE",
            "value": 0.024,
            "std": 0.0026,
            "paper_value": 0.0853,
            "paper_std": 0.0026,
            "true_value": 0.024,
            "true_std": 0.003,
            "sort_value": 0.024,
            "sort_std": 0.003,
            "is_baseline": True,
            "has_value_gap": True,
            "has_value_note": False,
            "value_gap_source_arxiv": "2405.02795",
            "rank_delta": 140,
        },
        {
            "model_key": "signnet",
            "model": "SignNet",
            "metric": "MAE",
            "value": 0.024,
            "std": 0.0026,
            "paper_value": 0.0853,
            "paper_std": 0.0026,
            "true_value": 0.024,
            "true_std": 0.003,
            "sort_value": 0.024,
            "sort_std": 0.003,
            "is_baseline": True,
            "has_value_gap": True,
            "has_value_note": False,
            "value_gap_source_arxiv": "2405.02795",
            "rank_delta": 140,
        },
        {
            "model_key": "signnet",
            "model": "SignNet",
            "metric": "MAE",
            "value": 0.024,
            "std": 0.0026,
            "paper_value": 0.0853,
            "paper_std": 0.0026,
            "true_value": 0.024,
            "true_std": 0.003,
            "sort_value": 0.024,
            "sort_std": 0.003,
            "is_baseline": False,
            "has_value_gap": True,
            "has_value_note": False,
            "value_gap_source_arxiv": "2405.02795",
            "rank_delta": 140,
        },
    ]

    unique = _dedup_result_rows(
        rows,
        (
            "model_key",
            "model",
            "metric",
            "value",
            "std",
            "paper_value",
            "paper_std",
            "true_value",
            "true_std",
            "sort_value",
            "sort_std",
            "is_baseline",
            "has_value_gap",
            "has_value_note",
            "value_gap_source_arxiv",
            "rank_delta",
        ),
    )

    assert len(unique) == 2
    assert unique[0]["is_baseline"] is True
    assert unique[1]["is_baseline"] is False


@pytest.mark.parametrize(
    ("model_name", "expected"),
    [
        ("GCN", "gcn"),
        ("GIN", "gin"),
        ("GraphSAGE", "sage"),
        ("SAGE", "sage"),
        ("MLP", "mlp"),
        ("GatedGCN", "gatedgcn"),
        ("Gated GCN", "gatedgcn"),
        ("GCNII", ""),
        ("SignNet", ""),
    ],
)
def test_normalize_model_family_recognizes_core_baselines(model_name, expected):
    assert _normalize_model_family(model_name) == expected


@pytest.mark.parametrize(
    ("model_name", "expected"),
    [
        ("GCN", "gcn"),
        ("GIN", "gin"),
        ("GraphSAGE", "sage"),
        ("MLP", "mlp"),
        ("GatedGCN", "gatedgcn"),
        ("CompGCN", ""),
        ("GCNII", ""),
        ("MLP-4L", ""),
        ("GraphMLP", ""),
    ],
)
def test_plain_core_baseline_kind_only_matches_plain_names(model_name, expected):
    assert _plain_core_baseline_kind(model_name) == expected


def _global_row(model: str, value: float, rank: int, *, higher_is_better: bool = True) -> dict:
    return {
        "model": model,
        "model_key": model.lower(),
        "value": value,
        "sort_value": value,
        "std": None,
        "is_baseline": True,
        "global_rank": rank,
        "higher_is_better": higher_is_better,
    }


def test_select_global_context_rows_adds_top_models_and_core_baselines():
    global_top = [
        _global_row("GraphGPS", 0.95, 1),
        _global_row("SignNet", 0.90, 2),
        _global_row("GIN", 0.85, 3),
        _global_row("GCN", 0.70, 4),
        _global_row("MLP", 0.60, 5),
        _global_row("GraphSAGE", 0.65, 6),
    ]

    selected = _select_global_context_rows(global_top, {"signnet"})

    assert [row["model"] for row in selected] == [
        "GraphGPS",
        "GIN",
        "GCN",
        "MLP",
    ]


def test_select_global_context_rows_uses_dataset_ranks_not_backfill():
    """Ranks 4+ must not replace rank 2/3 slots when those models are already on the paper."""
    global_top = [
        _global_row("GraphGPS", 0.95, 1),
        _global_row("SignNet", 0.90, 2),
        _global_row("GIN", 0.85, 3),
        _global_row("CompGCN", 0.84, 4),
        _global_row("novel graph MLP mixer", 0.83, 5),
        _global_row("GraphSAGE", 0.65, 6),
    ]

    selected = _select_global_context_rows(global_top, {"signnet"})

    assert [row["model"] for row in selected] == [
        "GraphGPS",
        "GIN",
        "GraphSAGE",
    ]


def test_select_global_context_rows_picks_best_plain_gnn_not_compgcn():
    global_top = [
        _global_row("GraphGPS", 0.95, 1),
        _global_row("CompGCN", 0.92, 2),
        _global_row("GCN", 0.70, 3),
        _global_row("GIN", 0.85, 4),
    ]

    selected = _select_global_context_rows(global_top, set())

    assert [row["model"] for row in selected] == [
        "GraphGPS",
        "CompGCN",
        "GCN",
        "GIN",
    ]


def test_count_recent_leaderboard_rows_uses_publication_cutoff():
    from datetime import date, timedelta

    from backend.export_to_hugo import RECENT_RESULTS_YEARS, _count_recent_leaderboard_rows

    cutoff = (date.today() - timedelta(days=365 * RECENT_RESULTS_YEARS)).isoformat()
    recent = (date.today() - timedelta(days=30)).isoformat()
    old = (date.today() - timedelta(days=365 * (RECENT_RESULTS_YEARS + 1))).isoformat()
    rows = [
        {"date_iso": recent},
        {"date_iso": old},
        {"date_iso": ""},
        {"date_iso": cutoff},
    ]

    assert _count_recent_leaderboard_rows(rows) == 2


def test_dataset_export_metadata_uses_cache(monkeypatch):
    from backend import export_to_hugo

    clear_export_caches()
    calls: list[int] = []
    monkeypatch.setattr(
        export_to_hugo,
        "_dataset_page_export_metadata",
        lambda _session, dataset_id: calls.append(dataset_id)
        or {"exportable": True, "result_count": 1},
    )
    export_to_hugo._DATASET_EXPORT_META_CACHE[42] = {"exportable": True, "result_count": 99}

    meta = _dataset_export_metadata(object(), 42)

    assert meta["result_count"] == 99
    assert calls == []


def test_benchmark_totals_exportable_uses_dataset_metadata_cache(monkeypatch):
    from backend import export_to_hugo

    clear_export_caches()
    calls: list[int] = []
    monkeypatch.setattr(
        export_to_hugo,
        "_dataset_page_export_metadata",
        lambda _session, dataset_id: calls.append(dataset_id)
        or {"exportable": True, "result_count": 1},
    )
    for did in (7, 8):
        export_to_hugo._DATASET_EXPORT_META_CACHE[did] = {"exportable": True, "result_count": 5}

    class FakeDataset:
        def __init__(self, dataset_id: int):
            self.id = dataset_id

    class FakeBenchmark:
        def __init__(self, name: str, dataset_ids: list[int]):
            self.name = name
            self.datasets = [FakeDataset(i) for i in dataset_ids]

    benchmarks = [FakeBenchmark("GNN", [7, 8])]
    totals = export_to_hugo._benchmark_totals_exportable(object(), benchmarks)
    assert totals == {"GNN": 2}
    assert calls == []

    totals_again = export_to_hugo._benchmark_totals_exportable(object(), benchmarks)
    assert totals_again == {"GNN": 2}
    assert calls == []


def test_primary_proposed_from_results_prefers_primary_metric_rows():
    from types import SimpleNamespace

    from backend.export_to_hugo import _primary_proposed_from_results

    class FakeModel:
        def __init__(self, name: str):
            self.canonical_name = name

    def row(model: str, metric: str, primary: str):
        ds = SimpleNamespace(primary_metric=primary)
        dv = SimpleNamespace(dataset=ds)
        return SimpleNamespace(
            model=FakeModel(model),
            dataset_variant=dv,
            metric_name=metric,
        )

    results = [
        row("Ablation-A", "Accuracy", "Accuracy"),
        row("MainMethod", "Accuracy", "Accuracy"),
        row("MainMethod", "Accuracy", "Accuracy"),
        row("MainMethod", "F1", "Accuracy"),
    ]
    chosen = _primary_proposed_from_results(
        results,
        ["Ablation-A", "MainMethod"],
    )
    assert chosen == "MainMethod"


def test_copy_main_figure_if_newer_skips_unchanged(tmp_path):
    from backend.export_to_hugo import _copy_main_figure_if_newer

    src = tmp_path / "fig.png"
    dest = tmp_path / "out" / "fig.png"
    src.write_bytes(b"source")
    dest.parent.mkdir(parents=True)
    shutil.copy2(src, dest)
    import os
    import time

    time.sleep(0.05)
    os.utime(dest, (time.time(), time.time()))
    _copy_main_figure_if_newer(src, dest)
    assert dest.read_bytes() == b"source"


def test_global_ranks_cached_reuses_module_cache(monkeypatch):
    from backend import export_to_hugo

    clear_export_caches()
    calls: list[tuple[str, str, bool]] = []

    def fake(session, ds_name, metric, hib):
        calls.append((ds_name, metric, hib))
        return {}, [], {}

    monkeypatch.setattr(export_to_hugo, "_global_ranks_for_dataset", fake)
    session = object()
    _global_ranks_cached(session, "Cora", "Accuracy", True)
    _global_ranks_cached(session, "Cora", "Accuracy", True)
    assert len(calls) == 1


def test_benchmark_coverage_entries_reports_evaluated_over_total():
    grouped = [
        {
            "benchmark": "Open Graph Benchmark",
            "datasets": [{"dataset": "ogbn-arxiv"}, {"dataset": "ogbn-products"}],
        },
        {"benchmark": "TUDataset", "datasets": [{"dataset": "MUTAG"}]},
    ]
    totals = {"Open Graph Benchmark": 5, "TUDataset": 12}

    coverage = _benchmark_coverage_entries(grouped, totals)

    assert coverage == [
        {
            "benchmark": "Open Graph Benchmark",
            "benchmark_slug": "open-graph-benchmark",
            "evaluated": 2,
            "total": 5,
        },
        {"benchmark": "TUDataset", "benchmark_slug": "tudataset", "evaluated": 1, "total": 12},
    ]


def test_benchmark_coverage_entries_falls_back_to_evaluated_when_total_unknown():
    grouped = [{"benchmark": "Other", "datasets": [{"dataset": "Custom"}]}]

    coverage = _benchmark_coverage_entries(grouped, {})

    assert coverage == [
        {"benchmark": "Other", "benchmark_slug": "other", "evaluated": 1, "total": 1}
    ]


def test_select_global_context_rows_skips_core_baselines_already_on_paper():
    global_top = [
        _global_row("GraphGPS", 0.95, 1),
        _global_row("SignNet", 0.90, 2),
        _global_row("Transformer", 0.88, 3),
        _global_row("GIN", 0.85, 4),
        _global_row("GCN", 0.70, 5),
    ]

    selected = _select_global_context_rows(global_top, {"gin", "gcn"})

    assert [row["model"] for row in selected] == ["GraphGPS", "SignNet", "Transformer"]


def test_select_global_context_rows_adds_gatedgcn_only_when_beats_plain_gnn_trio():
    global_top = [
        _global_row("GraphGPS", 0.95, 1),
        _global_row("SignNet", 0.90, 2),
        _global_row("Transformer", 0.89, 3),
        _global_row("GatedGCN", 0.88, 4),
        _global_row("GIN", 0.85, 5),
        _global_row("GCN", 0.70, 6),
    ]

    selected = _select_global_context_rows(global_top, set())
    assert [row["model"] for row in selected] == [
        "GraphGPS",
        "SignNet",
        "Transformer",
        "GIN",
        "GatedGCN",
    ]

    global_top_weak_gated = [
        _global_row("GraphGPS", 0.95, 1),
        _global_row("SignNet", 0.90, 2),
        _global_row("GIN", 0.85, 3),
        _global_row("GatedGCN", 0.80, 4),
        _global_row("GCN", 0.70, 5),
    ]
    selected_weak = _select_global_context_rows(global_top_weak_gated, set())
    assert [row["model"] for row in selected_weak] == [
        "GraphGPS",
        "SignNet",
        "GIN",
        "GCN",
    ]
