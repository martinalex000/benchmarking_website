"""Tests for result-row deduplication after model-name normalization."""

from backend.llm_extractor import ResultEntry, _dedupe_result_entries


def test_dedupe_result_entries_keeps_better_value():
    results = [
        ResultEntry(
            model="GraphGPS",
            is_proposed=False,
            dataset="Cora",
            metric="Accuracy",
            value=0.9119,
        ),
        ResultEntry(
            model="GraphGPS",
            is_proposed=False,
            dataset="Cora",
            metric="Accuracy",
            value=0.9179,
        ),
    ]
    deduped = _dedupe_result_entries(results)
    assert len(deduped) == 1
    assert deduped[0].value == 0.9179


def test_dedupe_result_entries_lower_is_better():
    results = [
        ResultEntry(
            model="ModelA",
            is_proposed=False,
            dataset="ZINC",
            metric="MAE",
            value=0.20,
            higher_is_better=False,
        ),
        ResultEntry(
            model="ModelA",
            is_proposed=False,
            dataset="ZINC",
            metric="MAE",
            value=0.15,
            higher_is_better=False,
        ),
    ]
    deduped = _dedupe_result_entries(results)
    assert len(deduped) == 1
    assert deduped[0].value == 0.15
