"""Unit tests for dataset statistics discovery helpers."""

from backend.llm_extractor import (
    DatasetInfo,
    DatasetList,
    _apply_statistics_ripgrep_precheck,
    _merge_dataset_lists,
)


def test_merge_dataset_lists_merges_statistics_fields():
    first = DatasetList(
        datasets=[
            DatasetInfo(
                name="Peptides-func",
                statistics_mentioned=True,
                statistics_sources=["Table 2"],
            )
        ]
    )
    second = DatasetList(
        datasets=[
            DatasetInfo(
                name="peptides-func",
                table_refs=["Table 1"],
                statistics_sources=["Section 3"],
            )
        ]
    )
    merged = _merge_dataset_lists(first, second)
    ds = merged.datasets[0]
    assert ds.statistics_mentioned is True
    assert ds.table_refs == ["Table 1"]
    assert ds.statistics_sources == ["Table 2", "Section 3"]


def test_apply_statistics_ripgrep_precheck_flags_nearby_markers():
    datasets = DatasetList(datasets=[DatasetInfo(name="Peptides-func", statistics_mentioned=False)])
    text = (
        "We evaluate on Peptides-func with #graphs = 15,535 and avg. #nodes of 150.94 "
        "in the standard split."
    )
    updated = _apply_statistics_ripgrep_precheck(datasets, text)
    assert updated.datasets[0].statistics_mentioned is True
