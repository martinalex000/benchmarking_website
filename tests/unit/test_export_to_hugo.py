"""Focused regression tests for export helper behavior."""

import shutil
from pathlib import Path

import pytest

from backend.at_pub_timeline import AtPubEvent, AtPubTimeline, global_best_per_model_as_of_date
from backend.export_helpers import truncate_words as _truncate_words
from backend.export_to_hugo import (
    INITIAL_DATASET_HTML_ROWS,
    _architecture_counts,
    _benchmark_coverage_entries,
    _build_chart_points,
    _cleanup_stale_hugo_content,
    _collect_dataset_papers,
    _comparison_source_date_label,
    _conference_export_fields,
    _dataset_chart_default_log_scale,
    _dataset_chart_hidden_models,
    _dataset_export_metadata,
    _dedup_result_rows,
    _description_class_target_count,
    _enrich_paper_result_row,
    _fmt_date,
    _gap_magnitude,
    _global_ranks_cached,
    _has_paper_value_gap,
    _is_value_better_than,
    _is_value_worse_than,
    _metric_counts,
    _normalize_conference,
    _normalize_model_family,
    _paper_dataset_export_meta,
    _plain_core_baseline_kind,
    _plain_model,
    _publication_year,
    _rank_for_value,
    _resolve_global_rank,
    _sanitize_model,
    _sanitize_title,
    _select_global_context_rows,
    _write_dataset_variant_json_files,
    clear_export_caches,
)
from backend.leaderboard_compare import has_paper_value_difference


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
    assert has_paper_value_difference(0.81, 0.8)
    assert not has_paper_value_difference(0.8, 0.8 + 1e-13)


def test_gap_magnitude_reports_any_numeric_difference():
    assert _gap_magnitude(0.81, 0.8) == pytest.approx(0.01)
    assert _gap_magnitude(0.81, 0.81) is None
    assert _gap_magnitude(None, 0.8) is None


def test_collect_model_value_mismatches_includes_at_pub_fields():
    from backend.db import session_scope
    from backend.export_to_hugo import _collect_model_value_mismatches, clear_export_caches

    clear_export_caches()
    with session_scope() as session:
        rows = _collect_model_value_mismatches(session)
    if not rows:
        return
    row = rows[0]
    for key in (
        "at_pub_value",
        "at_pub_source_arxiv",
        "worse_than_at_pub",
        "surpassed_since_pub",
        "at_pub_differs_from_today",
    ):
        assert key in row


def test_is_value_worse_than_respects_std_overlap():
    assert _is_value_worse_than(0.80, 0.81, True, 0.02, 0.02) is False
    assert _is_value_worse_than(0.70, 0.81, True) is True


def test_is_value_better_than_respects_std_overlap():
    assert _is_value_better_than(0.82, 0.81, True, 0.02, 0.02) is False
    assert _is_value_better_than(0.90, 0.81, True) is True


def _enrich_test_row(**overrides) -> dict:
    row = {
        "model_key": "gcn",
        "paper_value": 0.72,
        "paper_std": None,
        "value": 0.72,
        "std": None,
        "is_baseline": False,
        "is_global_top": False,
    }
    row.update(overrides)
    return row


def test_enrich_paper_result_row_marks_at_pub_improvement_for_proposed():
    truth_map = {
        "gcn": {
            "value": 0.72,
            "std": None,
            "arxiv_id": "2101.00797",
            "title": "Improving Paper",
            "date_iso": "2021-01-04",
            "venue": "AAAI",
        }
    }
    at_pub_map = {
        "gcn": {
            "value": 0.28,
            "std": None,
            "arxiv_id": "2007.02133",
            "title": "Prior GCN Paper",
            "date_iso": "2020-07-04",
            "venue": "ICML",
        }
    }
    row = _enrich_test_row(is_baseline=False, paper_value=0.72)
    _enrich_paper_result_row(
        row,
        truth_map=truth_map,
        model_to_rank={"gcn": 1},
        global_top_all=[{"model_key": "gcn", "value": 0.72}],
        arxiv_id="2101.00797",
        higher_is_better=True,
        at_pub_map=at_pub_map,
    )
    assert row["better_than_at_pub"] is True
    assert row["comparison_type"] == "improved"
    assert row["has_value_gap"] is True
    assert row["comparison_source_arxiv"] == "2007.02133"


def test_enrich_paper_result_row_worse_than_at_pub_applies_to_proposed():
    truth_map = {
        "gcn": {
            "value": 0.85,
            "std": None,
            "arxiv_id": "9999.00001",
            "title": "Today Best",
            "date_iso": "2022-01-01",
            "venue": "NeurIPS",
        }
    }
    at_pub_map = {
        "gcn": {
            "value": 0.80,
            "std": None,
            "arxiv_id": "8888.00001",
            "title": "At Pub Best",
            "date_iso": "2020-01-01",
            "venue": "ICML",
        }
    }
    row = _enrich_test_row(is_baseline=False, paper_value=0.70)
    _enrich_paper_result_row(
        row,
        truth_map=truth_map,
        model_to_rank={"gcn": 1},
        global_top_all=[{"model_key": "gcn", "value": 0.85}],
        arxiv_id="7777.00001",
        higher_is_better=True,
        at_pub_map=at_pub_map,
    )
    assert row["worse_than_at_pub"] is True
    assert row["comparison_type"] == "behind"
    assert row["has_value_gap"] is True


def test_enrich_paper_result_row_marks_improvement_surpassed_since_pub():
    truth_map = {
        "gcn": {
            "value": 0.90,
            "std": None,
            "arxiv_id": "9999.00002",
            "title": "Later Best",
            "date_iso": "2024-01-01",
            "venue": "ICML",
        }
    }
    at_pub_map = {
        "gcn": {
            "value": 0.70,
            "std": None,
            "arxiv_id": "8888.00002",
            "title": "Prior Best",
            "date_iso": "2020-01-01",
            "venue": "NeurIPS",
        }
    }
    row = _enrich_test_row(is_baseline=True, paper_value=0.80)
    _enrich_paper_result_row(
        row,
        truth_map=truth_map,
        model_to_rank={"gcn": 1},
        global_top_all=[{"model_key": "gcn", "value": 0.90}],
        arxiv_id="2305.17589",
        higher_is_better=True,
        at_pub_map=at_pub_map,
    )
    assert row["better_than_at_pub"] is True
    assert row["surpassed_since_pub"] is True
    assert row["improvement_surpassed_since_pub"] is True


def test_paper_dataset_export_meta_flags_non_primary_metric():
    meta = _paper_dataset_export_meta("Micro-F1", ["Accuracy"], "Accuracy")
    assert meta["uses_non_primary_metric"] is True
    assert meta["paper_has_primary_metric"] is False
    assert meta["metric"] == "Accuracy"
    assert meta["dataset_primary_metric"] == "Micro-F1"


def test_resolve_global_rank_uses_leaderboard_or_value_fallback():
    global_rows = [
        {"model_key": "gcn", "value": 0.8},
        {"model_key": "gin", "value": 0.75},
    ]
    model_to_rank = {"gcn": 1, "gin": 2}

    assert (
        _resolve_global_rank(
            {"model_key": "gcn", "sort_value": 0.7},
            model_to_rank,
            global_rows,
            True,
        )
        == 1
    )
    assert (
        _resolve_global_rank(
            {"model_key": "coe", "sort_value": 0.77},
            model_to_rank,
            global_rows,
            True,
        )
        == 2
    )
    assert (
        _resolve_global_rank(
            {"model_key": "coe", "value": 0.77},
            {},
            global_rows,
            True,
        )
        == 2
    )


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
        ("JMLR", "JMLR"),
        ("Journal of machine learning research", "JMLR"),
        ("Graph Learning Conference", "LoG"),
        ("LoG 2023", "LoG"),
        ("Learning on Graphs Conference", "LoG"),
        ("The Web Conference", "WWW"),
        ("World Wide Web Conference", "WWW"),
        ("WWW2025", "WWW"),
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
        ("Journal of machine learning research", "2023-01-01", "JMLR 2023"),
        ("The Web Conference", "2020-02-05", "WWW 2020"),
        ("Learning on Graphs Conference", "2023-08-31", "LoG 2023"),
        ("arXiv.org", "2024-01-01", ""),
        ("ICLR 2023", "2023", "ICLR 2023"),
    ],
)
def test_conference_export_fields_include_year(venue, published_date, expected):
    assert _conference_export_fields(venue, published_date)["published_conference"] == expected


@pytest.mark.parametrize(
    ("venue", "date_iso", "expected"),
    [
        ("International Conference on Learning Representations", "2024-05-07", "ICLR 2024"),
        ("NeurIPS 2024", "2024-12-10", "NeurIPS 2024"),
        ("arXiv.org", "2024-01-15", "2024"),
        ("", "2023-07-01", "2023"),
        ("", "", ""),
    ],
)
def test_comparison_source_date_label_prefers_conference(venue, date_iso, expected):
    assert _comparison_source_date_label(venue, date_iso) == expected


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

    from backend.export_to_hugo import RECENT_RESULTS_MONTHS, _count_recent_leaderboard_rows

    cutoff = (date.today() - timedelta(days=30 * RECENT_RESULTS_MONTHS)).isoformat()
    recent = (date.today() - timedelta(days=30)).isoformat()
    old = (date.today() - timedelta(days=30 * (RECENT_RESULTS_MONTHS + 1))).isoformat()
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


def test_at_pub_timeline_excludes_paper_and_respects_cutoff():
    events = [
        AtPubEvent("2020-01-01", 0.70, None, "1111.0001", "Early", "", "GCN"),
        AtPubEvent("2021-06-01", 0.80, None, "2222.0002", "Later", "", "GCN"),
        AtPubEvent("2022-01-01", 0.75, None, "3333.0003", "Mid", "", "GCN"),
    ]
    timeline = AtPubTimeline([], True)
    timeline._by_model = {"gcn": events}

    as_of_2021 = timeline.truth_map("2021-06-01")
    assert as_of_2021["gcn"]["value"] == 0.80
    assert as_of_2021["gcn"]["arxiv_id"] == "2222.0002"

    excluding = timeline.truth_map("2022-01-01", exclude_arxiv="3333.0003")
    assert excluding["gcn"]["value"] == 0.80


def test_global_best_per_model_reuses_dataset_metric_rows(monkeypatch):
    clear_export_caches()
    query_calls = 0

    class FakeQuery:
        def options(self, *_args, **_kwargs):
            return self

        def join(self, *_args, **_kwargs):
            return self

        def filter(self, *_args, **_kwargs):
            return self

        def all(self):
            nonlocal query_calls
            query_calls += 1
            return []

    class FakeSession:
        def query(self, *_args, **_kwargs):
            return FakeQuery()

    session = FakeSession()
    global_best_per_model_as_of_date(session, "Cora", "Accuracy", True, "2020-01-01")
    global_best_per_model_as_of_date(session, "Cora", "Accuracy", True, "2024-06-01")
    global_best_per_model_as_of_date(session, "Cora", "F1", True, "2024-06-01")

    assert query_calls == 2


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

    from backend.leaderboard_compare import primary_proposed_from_results

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
    chosen = primary_proposed_from_results(
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


def _write_stub_hugo_page(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\ntitle: stub\n---\n", encoding="utf-8")


def test_cleanup_stale_hugo_content_removes_orphan_pages(monkeypatch, tmp_path):
    content = tmp_path / "content"
    _write_stub_hugo_page(content / "papers" / "stale-paper" / "index.md")
    _write_stub_hugo_page(content / "papers" / "keep-paper" / "index.md")
    _write_stub_hugo_page(content / "datasets" / "stale-ds" / "index.md")
    _write_stub_hugo_page(content / "datasets" / "keep-ds" / "index.md")

    monkeypatch.setattr("backend.export_to_hugo._CONTENT", content)

    removed_papers, removed_datasets = _cleanup_stale_hugo_content(
        keep_paper_ids={"keep-paper"},
        keep_dataset_slugs={"keep-ds"},
    )

    assert removed_papers == 1
    assert removed_datasets == 1
    assert not (content / "papers" / "stale-paper").exists()
    assert (content / "papers" / "keep-paper").exists()
    assert not (content / "datasets" / "stale-ds").exists()
    assert (content / "datasets" / "keep-ds").exists()


def test_export_paper_removes_stale_content_when_no_results(monkeypatch, tmp_path):
    from backend.db import init_db, session_scope
    from backend.export_to_hugo import export_paper
    from backend.models import Paper

    content = tmp_path / "content"
    _write_stub_hugo_page(content / "papers" / "2402.04821" / "index.md")
    monkeypatch.setattr("backend.export_to_hugo._CONTENT", content)

    db_path = tmp_path / "benchmarks.db"
    monkeypatch.setattr("backend.config.cfg.db_path", db_path)
    monkeypatch.setattr("backend.config.cfg.base_dir", tmp_path)
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db()

    with session_scope() as session:
        session.add(
            Paper(
                arxiv_id="2402.04821",
                title="No Results Paper",
                extraction_status="extracted",
            )
        )

    assert export_paper("2402.04821") is False
    assert not (content / "papers" / "2402.04821").exists()


def test_export_dataset_removes_stale_content_when_not_exportable(monkeypatch, tmp_path):
    from backend.db import init_db, session_scope
    from backend.export_to_hugo import export_dataset
    from backend.models import Benchmark, Dataset, DatasetVariant

    content = tmp_path / "content"
    _write_stub_hugo_page(content / "datasets" / "no-results-yet" / "index.md")
    monkeypatch.setattr("backend.export_to_hugo._CONTENT", content)

    db_path = tmp_path / "benchmarks.db"
    monkeypatch.setattr("backend.config.cfg.db_path", db_path)
    monkeypatch.setattr("backend.config.cfg.base_dir", tmp_path)
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db()

    with session_scope() as session:
        benchmark = Benchmark(name="OGB", short_name="ogb")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="No Results Yet",
            task_type="node_classification",
            primary_metric="Accuracy",
            higher_is_better=1,
        )
        session.add(dataset)
        session.flush()
        session.add(DatasetVariant(dataset_id=dataset.id, name="Standard split", is_standard=1))
        session.flush()
        dataset_id = dataset.id

    assert export_dataset(dataset_id) is False
    assert not (content / "datasets" / "no-results-yet").exists()


def test_export_all_removes_stale_paper_pages_on_full_export(monkeypatch, tmp_path):
    from backend.db import init_db, session_scope
    from backend.export_to_hugo import export_all
    from backend.models import Benchmark, Dataset, DatasetVariant, Model, Paper, Result

    site_dir = tmp_path / "site"
    content = site_dir / "content"
    data_dir = site_dir / "data"
    config_dir = tmp_path / "config"
    for directory in (content, data_dir, config_dir):
        directory.mkdir(parents=True, exist_ok=True)
    (config_dir / "dataset_overrides.yaml").write_text("{}\n", encoding="utf-8")

    _write_stub_hugo_page(content / "papers" / "stale-paper" / "index.md")
    _write_stub_hugo_page(content / "datasets" / "stale-dataset" / "index.md")

    monkeypatch.setattr("backend.export_to_hugo._SITE_DIR", site_dir)
    monkeypatch.setattr("backend.export_to_hugo._CONTENT", content)
    monkeypatch.setattr("backend.export_to_hugo._DATA_DIR", data_dir)
    monkeypatch.setattr("backend.export_to_hugo._STATIC", site_dir / "static")
    monkeypatch.setattr(
        "backend.export_to_hugo._DATASET_OVERRIDES_FILE", config_dir / "dataset_overrides.yaml"
    )
    monkeypatch.setattr("backend.config.cfg.db_path", tmp_path / "benchmarks.db")
    monkeypatch.setattr("backend.config.cfg.base_dir", tmp_path)
    monkeypatch.setattr("backend.config.cfg.site_dir", site_dir)
    monkeypatch.setattr("backend.config.cfg.config_dir", config_dir)

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db()
    clear_export_caches()

    with session_scope() as session:
        benchmark = Benchmark(name="OGB", short_name="ogb")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="ogbn-arxiv",
            task_type="node_classification",
            primary_metric="Accuracy",
            higher_is_better=1,
        )
        session.add(dataset)
        session.flush()
        variant = DatasetVariant(dataset_id=dataset.id, name="Standard split", is_standard=1)
        model = Model(name="GCN", canonical_name="gcn", paper_id=None, is_baseline=1)
        paper = Paper(
            arxiv_id="2401.17791",
            title="Exportable Paper",
            extraction_status="extracted",
            published_date="2024-01-01",
        )
        session.add_all((variant, model, paper))
        session.flush()
        session.add(
            Result(
                paper_id=paper.id,
                model_id=model.id,
                dataset_variant_id=variant.id,
                metric_name="Accuracy",
                metric_value=0.75,
                higher_is_better=1,
                is_baseline=1,
            )
        )

    export_all(skip_development=True)

    assert not (content / "papers" / "stale-paper").exists()
    assert not (content / "datasets" / "stale-dataset").exists()
    assert (content / "papers" / "2401.17791" / "index.md").exists()
    assert (content / "datasets" / "ogbn-arxiv" / "index.md").exists()


def test_build_chart_points_uses_primary_metric_only():
    rows = [
        {
            "date_iso": "2024-01-01",
            "metric_values": [0.91, 0.5],
            "metric_stds": [0.01, None],
            "model": "GCN",
            "model_plain": "GCN",
            "arxiv_id": "2401.00001",
            "title": "Test",
            "is_baseline": True,
            "codebase_url": "https://github.com/example",
            "architecture_type": "gnn",
            "is_std_outlier": False,
        }
    ]

    points = _build_chart_points(rows)

    assert len(points) == 1
    assert points[0]["value"] == 0.91
    assert points[0]["std"] == 0.01
    assert points[0]["has_code"] is True
    assert points[0]["is_baseline"] is True


def test_architecture_counts_and_dataset_papers_helpers():
    rows = [
        {"architecture_type": "gnn", "arxiv_id": "1", "title": "A", "date_iso": "2024-02-01"},
        {"architecture_type": "hybrid", "arxiv_id": "2", "title": "B", "date_iso": "2024-01-01"},
        {
            "architecture_type": "svm_kernel",
            "arxiv_id": "1",
            "title": "A",
            "date_iso": "2024-02-01",
        },
    ]

    counts = _architecture_counts(rows)
    papers = _collect_dataset_papers(rows)

    assert counts == {
        "gnn": 1,
        "hybrid": 1,
        "graph_transformer": 0,
        "llm": 0,
        "walk": 0,
        "traditional": 1,
    }
    assert [p["arxiv_id"] for p in papers] == ["1", "2"]


def test_metric_counts_helper():
    rows = [
        {"metric_values": [0.9, 0.8, None]},
        {"metric_values": [0.85, None, 0.1]},
        {"metric_values": [None, 0.7, 0.2]},
    ]
    assert _metric_counts(rows, ["Accuracy", "F1", "Loss"]) == [2, 2, 2]


def test_write_dataset_variant_json_files(monkeypatch, tmp_path):
    static_dir = tmp_path / "site" / "static"
    monkeypatch.setattr(
        "backend.export_to_hugo._DATASETS_DATA_DIR", static_dir / "data" / "datasets"
    )
    rows = [
        {"metric_values": [0.8], "metric_stds": [None], "model": "MLP", "date_iso": "2024-01-01"}
    ]

    rows_url, chart_url = _write_dataset_variant_json_files(
        "cora",
        "random-10-fold",
        rows,
        ["Accuracy"],
        "Accuracy",
        True,
    )

    assert rows_url == "/data/datasets/cora/random-10-fold-rows.json"
    assert chart_url == "/data/datasets/cora/random-10-fold-chart.json"
    assert (static_dir / "data" / "datasets" / "cora" / "random-10-fold-rows.json").exists()
    assert (static_dir / "data" / "datasets" / "cora" / "random-10-fold-chart.json").exists()


def test_export_dataset_trims_html_rows_and_writes_json(monkeypatch, tmp_path):
    import yaml

    from backend.db import init_db, session_scope
    from backend.export_to_hugo import export_dataset
    from backend.models import Benchmark, Dataset, DatasetVariant, Model, Paper, Result

    site_dir = tmp_path / "site"
    content = site_dir / "content"
    static_dir = site_dir / "static"
    for directory in (content, static_dir, tmp_path / "config"):
        directory.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr("backend.export_to_hugo._CONTENT", content)
    monkeypatch.setattr("backend.export_to_hugo._SITE_DIR", site_dir)
    monkeypatch.setattr("backend.export_to_hugo._STATIC", static_dir)
    monkeypatch.setattr(
        "backend.export_to_hugo._DATASETS_DATA_DIR", static_dir / "data" / "datasets"
    )
    monkeypatch.setattr("backend.config.cfg.db_path", tmp_path / "benchmarks.db")
    monkeypatch.setattr("backend.config.cfg.base_dir", tmp_path)
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db()

    with session_scope() as session:
        benchmark = Benchmark(name="Planetoid", short_name="planetoid")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="Cora",
            task_type="node_classification",
            primary_metric="Accuracy",
            higher_is_better=1,
        )
        session.add(dataset)
        session.flush()
        variant = DatasetVariant(dataset_id=dataset.id, name="Random 10-fold", is_standard=1)
        model = Model(name="GCN", canonical_name="GCN", model_type="gnn")
        session.add_all((variant, model))
        session.flush()
        for idx in range(INITIAL_DATASET_HTML_ROWS + 5):
            paper = Paper(
                arxiv_id=f"2401.{idx:05d}",
                title=f"Paper {idx}",
                published_date="2024-01-01",
            )
            session.add(paper)
            session.flush()
            session.add(
                Result(
                    paper_id=paper.id,
                    model_id=model.id,
                    dataset_variant_id=variant.id,
                    metric_name="Accuracy",
                    metric_value=0.5 + idx * 0.001,
                    higher_is_better=1,
                    is_baseline=1,
                )
            )
        dataset_id = dataset.id

    assert export_dataset(dataset_id) is True

    page = content / "datasets" / "cora" / "index.md"
    assert page.exists()
    front_matter = yaml.safe_load(page.read_text(encoding="utf-8").split("---", 2)[1])
    variant_data = front_matter["variants"][0]

    assert variant_data["row_count"] == INITIAL_DATASET_HTML_ROWS + 5
    assert len(variant_data["rows"]) == INITIAL_DATASET_HTML_ROWS
    assert variant_data["rows_json"].endswith("-rows.json")
    assert variant_data["chart_json"].endswith("-chart.json")
    assert variant_data["metric_counts"] == [INITIAL_DATASET_HTML_ROWS + 5]
    assert len(front_matter["papers"]) == INITIAL_DATASET_HTML_ROWS + 5
    assert (static_dir / "data" / "datasets" / "cora" / "random-10-fold-rows.json").exists()


def test_metrics_order_for_qm9_puts_gap_first():
    from backend.export_to_hugo import _metrics_order_for_dataset

    available = {"mu", "alpha", "gap", "H"}
    ordered = _metrics_order_for_dataset(
        "QM9",
        available,
        "gap",
        ["gap", "mu", "alpha", "H"],
    )
    assert ordered[0] == "gap"
    assert ordered.index("mu") < ordered.index("H")


def test_qm9_chart_display_overrides():
    clear_export_caches()
    assert _dataset_chart_default_log_scale("QM9") is True
    assert _dataset_chart_hidden_models("QM9") == ["MLP"]


def test_build_multi_metric_rows_respects_metrics_order():
    from types import SimpleNamespace

    from backend.export_to_hugo import _build_multi_metric_rows

    paper = SimpleNamespace(
        arxiv_id="1234.5678",
        title="Paper",
        published_date="2024-01-01",
        venue=None,
        codebase_url="",
    )
    model = SimpleNamespace(canonical_name="GIN", model_type="gnn")
    base = {
        "higher_is_better": False,
        "is_baseline": True,
        "is_overridden": False,
        "override_reason": "",
        "uses_external_data": 0,
        "params_millions": None,
        "model": model,
        "paper": paper,
    }
    results = [
        SimpleNamespace(
            metric_name="mu",
            metric_value=0.1,
            metric_std=None,
            display_value=0.1,
            **base,
        ),
        SimpleNamespace(
            metric_name="gap",
            metric_value=0.05,
            metric_std=None,
            display_value=0.05,
            **base,
        ),
    ]

    metrics, _hib, rows = _build_multi_metric_rows(
        results,
        "gap",
        metrics_order=["gap", "mu"],
    )
    assert metrics == ["gap", "mu"]
    assert rows[0]["metric_values"] == [0.05, 0.1]


def test_merged_metric_labels_for_qm9():
    from backend.export_to_hugo import _merged_metric_labels, _metric_display_names

    labels = _merged_metric_labels("QM9")
    display = _metric_display_names(["gap", "mu"], labels)
    assert display[0] == "HOMO-LUMO gap"
    assert display[1] == "Dipole moment"
