"""Tests for variant deduplication keyed by model identity."""

from backend.llm_extractor import ResultEntry, _dedupe_result_entries


def test_dedupe_keeps_distinct_proposed_models():
    results = [
        ResultEntry(
            model="FooGNN",
            is_proposed=True,
            dataset="Cora",
            metric="Accuracy",
            value=0.82,
        ),
        ResultEntry(
            model="BarGNN",
            is_proposed=True,
            dataset="Cora",
            metric="Accuracy",
            value=0.84,
        ),
    ]
    deduped = _dedupe_result_entries(results)
    assert len(deduped) == 2
    models = {r.model for r in deduped}
    assert models == {"FooGNN", "BarGNN"}


def test_dedupe_collapses_same_model_variants():
    results = [
        ResultEntry(
            model="GraphGPS",
            is_proposed=False,
            dataset="Cora",
            metric="Accuracy",
            value=0.9119,
        ),
        ResultEntry(
            model="GraphGPS*",
            is_proposed=False,
            dataset="Cora",
            metric="Accuracy",
            value=0.9179,
        ),
    ]
    deduped = _dedupe_result_entries(results)
    assert len(deduped) == 1
    assert deduped[0].value == 0.9179
