"""Unit tests for verbose extraction progress output."""

from types import SimpleNamespace

from backend.dataset_stats_parsing import classify_table_roles, is_statistics_table
from backend.llm_extractor import CallRecord, DatasetInfo, DatasetList
from backend.llm_tasks import (
    _dataset_statistics_extra_with_tables,
    _dataset_statistics_hint_block,
    _enrich_dataset_statistics_from_tables,
    _statistics_table_summaries,
)


def test_dataset_statistics_extra_and_hint_block():
    datasets = [
        DatasetInfo(
            name="Peptides-func",
            statistics_mentioned=True,
            statistics_sources=["Table 2"],
        ),
        DatasetInfo(name="Cora", statistics_mentioned=False),
    ]
    stat_tables = [{"number": 2, "caption": "Statistics", "in_appendix": False}]
    extra = _dataset_statistics_extra_with_tables(datasets, stat_table_summaries=stat_tables)
    assert extra[0]["statistics_mentioned"] is True
    assert extra[0]["statistics_table_numbers"] == [2]
    assert "Peptides-func" in _dataset_statistics_hint_block(datasets)
    assert "Cora" not in _dataset_statistics_hint_block(datasets)


def test_statistics_table_detection_and_enrichment():
    table = SimpleNamespace(
        number=2,
        caption="Statistics of the five proposed LRGB datasets.",
        in_appendix=False,
        markdown="Peptides-func 15535 150.94",
        body="Peptides-func\n15535",
        header=["Dataset", "Graphs"],
    )
    assert is_statistics_table(table) is True
    summaries = _statistics_table_summaries([table])
    assert summaries == [{"number": 2, "caption": table.caption, "in_appendix": False}]

    datasets = DatasetList(
        datasets=[
            DatasetInfo(name="Peptides-func"),
            DatasetInfo(name="Cora"),
        ]
    )
    _enrich_dataset_statistics_from_tables(datasets, [table])
    assert datasets.datasets[0].statistics_mentioned is True
    assert datasets.datasets[0].statistics_sources == ["Table 2"]
    assert datasets.datasets[1].statistics_mentioned is False


def test_table_role_evidence_supports_statistics_results_and_mixed_tables():
    statistics = SimpleNamespace(
        caption="Dataset statistics",
        header=["Dataset", "#Nodes", "#Edges", "#Classes"],
        markdown="Cora 2708 5429 7",
    )
    results = SimpleNamespace(
        caption="Benchmark results",
        header=["Method", "Accuracy"],
        markdown="GCN 0.81",
    )
    mixed = SimpleNamespace(
        caption="Dataset statistics and benchmark results",
        header=["Dataset", "#Nodes", "Method", "Accuracy"],
        markdown="Cora 2708 GCN 0.81",
    )

    statistics_roles = classify_table_roles(statistics)
    result_roles = classify_table_roles(results)
    mixed_roles = classify_table_roles(mixed)

    assert statistics_roles.statistics_only is True
    assert "statistics" in statistics_roles.roles
    assert "results" in result_roles.roles
    assert "statistics" in mixed_roles.roles
    assert "results" in mixed_roles.roles
    assert mixed_roles.statistics_only is False


def test_table_selection_call_record_carries_dataset_statistics():
    rec = CallRecord(
        call_type="select_tables:all",
        system_prompt="",
        user_content="",
        success=True,
        extra={
            "selected_tables_per_dataset": {"Peptides-func": [3, 4]},
            "tables_total": 8,
            "dataset_statistics": _dataset_statistics_extra_with_tables(
                [
                    DatasetInfo(
                        name="Peptides-func",
                        statistics_mentioned=True,
                        statistics_sources=["Table 2"],
                    )
                ],
                stat_table_summaries=[{"number": 2, "caption": "Statistics", "in_appendix": False}],
            ),
            "statistics_tables": [{"number": 2, "caption": "Statistics", "in_appendix": False}],
            "paper_has_statistics": True,
        },
    )
    assert rec.extra["dataset_statistics"][0]["statistics_mentioned"] is True
    assert rec.extra["paper_has_statistics"] is True
