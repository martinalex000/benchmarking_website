from types import SimpleNamespace as NS

from experiments.table_provenance_experiment.mapping_repair_feedback import repair_feedback


def verdict(metric="Accuracy", mean=65.31, std=0.24, divisor=100, repair=None):
    candidate = NS(metric=metric, displayed_mean=mean, displayed_std=std, divisor=divisor)
    return NS(selected_candidate_index=0, corrected_fact=NS(candidates=[candidate], repair=repair))


def test_correct_fractional_accuracy_does_not_need_numeric_repair():
    row = {"result_id": 1, "metric": "Accuracy", "value": 0.6531, "std": 0.0024}
    assert repair_feedback(row, verdict()) == []


def test_percent_expansion_is_rejected():
    row = {"result_id": 1, "metric": "Accuracy", "value": 0.6531, "std": 0.0024}
    assert any("divisor=100" in error for error in repair_feedback(row, verdict(divisor=1)))


def test_metric_prose_without_fields_is_not_a_repair():
    row = {"result_id": 1, "metric": "ROC-AUC", "value": 0.6531, "std": 0.0024}
    repair = NS(
        old_metric=None, corrected_metric=None, corrected_value=0.6531, corrected_std=0.0024
    )
    assert any(
        "metric repair fields" in error for error in repair_feedback(row, verdict(repair=repair))
    )


def test_mae_may_exceed_one_without_percent_conversion():
    row = {"result_id": 1, "metric": "MAE", "value": 2.0, "std": 0.24}
    assert repair_feedback(row, verdict(metric="MAE", mean=2.0, divisor=1)) == []


def test_unknown_origin_still_needs_source_numeric_repair():
    row = {"result_id": 1, "metric": "MAE", "value": 0.088, "std": 0.002}
    assert repair_feedback(row, verdict(metric="MAE", mean=0.526, std=0.051, divisor=1))
