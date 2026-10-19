from types import SimpleNamespace as NS

import pytest

from experiments.table_provenance_experiment.mapping_repair_adapter import adapt_verified_repair
from tests.unit.test_result_mapping_batch import verdict


def test_unsupported_repair_is_not_created_or_promoted():
    original = verdict([])
    adapted = adapt_verified_repair({}, original, "")
    assert adapted == original
    assert adapted is not original


@pytest.mark.parametrize("grounded", [True, False])
def test_only_supported_grounded_repair_gets_exact_fields(monkeypatch, grounded):
    import copy

    from experiments.table_provenance_experiment import mapping_repair_adapter as adapter

    monkeypatch.setattr(adapter, "grounded_column", lambda cell, source: grounded)
    candidate = NS(displayed_mean=62.7, displayed_std=0.7, divisor=100, metric="Accuracy")
    repair = NS(corrected_model="GCN", corrected_variant="Standard")
    original = NS(
        selected_candidate_index=0,
        verified_candidate_indices=[0],
        repair_supported=True,
        corrected_fact=NS(candidates=[candidate], repair=repair),
    )
    original.model_copy = lambda deep: copy.deepcopy(original)
    row = {"value": 0.9, "std": 0.1, "model": "GC N", "variant": "", "metric": "ROC-AUC"}
    adapted = adapt_verified_repair(row, original, "source")
    fix = adapted.corrected_fact.repair
    if not grounded:
        assert not hasattr(fix, "old_value")
        return
    assert fix.old_model == "GC N"
    assert fix.old_metric == "ROC-AUC"
    assert fix.corrected_metric == "Accuracy"
    assert abs(fix.corrected_value - 0.627) < 1e-10
    assert abs(fix.corrected_std - 0.007) < 1e-10
    assert not hasattr(original.corrected_fact.repair, "old_value")


def test_missing_repair_is_derived_without_inventing_method_or_count(monkeypatch):
    import copy

    from experiments.table_provenance_experiment import mapping_repair_adapter as adapter
    from experiments.table_provenance_experiment.verify_stored_mapping import Span

    monkeypatch.setattr(adapter, "grounded_column", lambda cell, source: True)
    span = Span(start_line=1, end_line=1)
    candidate = NS(
        displayed_mean=62.7,
        displayed_std=0.7,
        divisor=100,
        metric="Accuracy",
        cell_evidence=span,
        column_evidence=span,
    )
    original = NS(
        selected_candidate_index=0,
        verified_candidate_indices=[0],
        repair_supported=False,
        corrected_fact=NS(candidates=[candidate], repair=None),
    )
    original.model_copy = lambda deep: copy.deepcopy(original)
    row = {"value": 0.9, "std": 0.1, "model": "GC N", "variant": "", "metric": "ROC-AUC"}
    adapted = adapt_verified_repair(row, original, "source")
    assert adapted.repair_supported
    assert adapted.corrected_fact.repair.corrected_model == row["model"]
    assert adapted.corrected_fact.repair.corrected_variant == row["variant"]
    assert original.corrected_fact.repair is None
