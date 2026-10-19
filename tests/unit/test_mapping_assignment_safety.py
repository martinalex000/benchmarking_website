"""Safety gates preserve evidence and never change frozen decisions in place."""

import copy

from experiments.table_provenance_experiment.check_assignment_safety import (
    conflicting_prose_value,
    copied_evidence,
    earlier_exact,
    explicit_execution_rebuttal,
    partial_std_repair,
    safe_assignment,
)
from experiments.table_provenance_experiment.verify_stored_mapping_v3 import metric_key


def row(action="origin_unresolved"):
    return {
        "result_id": 1,
        "model": "FastGCN",
        "value": 0.92,
        "std": 0.005,
        "variant": "Planetoid",
        "action": action,
        "proposed_num_runs": None,
        "selected_candidate": None,
        "correction": None,
        "verdict": {"corrected_fact": {"origin_evidence": [{"start_line": 1, "end_line": 1}]}},
    }


def hint(std=0.005):
    return [{"result_id": 1, "matches": [{"model": "FastGCN", "value": 0.92, "std": std}]}]


def test_baseline_citation_does_not_establish_copying():
    current = row("copied_excluded")
    before = copy.deepcopy(current)
    result = safe_assignment(current, [], r"We compare with FastGCN \cite{fast}.", [])
    assert result["action"] == "origin_unresolved"
    assert current == before


def test_exact_earlier_match_is_strong_but_requires_same_std():
    assert earlier_exact(row(), hint())
    assert not earlier_exact(row(), hint(0.006))
    assert copied_evidence(row(), "Uninformative baseline list", hint())


def test_conditional_copying_does_not_identify_branch():
    assert not copied_evidence(row(), "Results are taken from prior work, otherwise we run it.", [])


def test_direct_copy_statement_is_supported():
    assert copied_evidence(row(), "Results are taken from the original paper.", [])


def test_conflicting_prose_rerun_blocks_cross_experiment_repair():
    current = row("copied_excluded")
    current["selected_candidate"] = {"divisor": 1, "table_id": 1, "method": "FastGCN"}
    current["correction"] = {
        "old": {"model": "FastGCN", "value": 0.92, "std": 0.005},
        "corrected": {"value": 0.937, "std": None},
    }
    source = "Using official code, FastGCN gets $0.920 \\pm 0.005$."
    assert conflicting_prose_value(current, source) == [1]
    result = safe_assignment(current, [], source, [])
    assert result["action"] == "configuration_scope_unresolved"
    assert result["correction"] is None


def test_percent_conversion_is_not_a_different_experiment():
    current = row()
    current["selected_candidate"] = {"divisor": 100}
    current["correction"] = {
        "old": {"model": "FastGCN", "value": 92.0, "std": 0.5},
        "corrected": {"value": 0.92, "std": 0.005},
    }
    assert conflicting_prose_value(current, "FastGCN 92.0 +/- 0.5") == []


def test_earlier_match_withholds_self_evaluated_count_without_automatic_copying():
    result = safe_assignment(row("propose_count"), [], "", hint())
    assert result["action"] == "origin_conflict_unresolved"
    assert result["proposed_num_runs"] is None


def test_explicit_execution_can_rebut_an_earlier_database_coincidence():
    current = row("propose_count")
    current["verdict"].update(origin_supported=True, execution_supported=True)
    current["verdict"]["corrected_fact"]["execution_evidence"] = [{"start_line": 1, "end_line": 1}]
    source = "We trained FastGCN ourselves and evaluated it on this benchmark."
    assert explicit_execution_rebuttal(current, source)
    assert safe_assignment(current, [], source, hint())["action"] == "propose_count"
    assert not explicit_execution_rebuttal(current, "We follow FastGCN's train/val/test split.")


def test_supported_setting_label_is_not_needlessly_rewritten():
    current = row()
    current["verdict"]["setting_status"] = "supported"
    old = {"model": "FastGCN", "value": 0.92, "std": 0.005, "variant": "Planetoid"}
    current["correction"] = {
        "old": old,
        "corrected": {**old, "variant": "Original split"},
        "explanation": "Refined wording",
    }
    assert safe_assignment(current, [], "", [])["correction"] is None


def test_copied_origin_is_not_a_replacement_split_label():
    current = row()
    current["verdict"]["setting_status"] = "contradicted"
    old = {"model": "FastGCN", "value": 0.92, "std": 0.005, "variant": "Planetoid"}
    current["correction"] = {
        "old": old,
        "corrected": {**old, "variant": "copied reported result"},
        "explanation": "Origin-only label",
    }
    assert safe_assignment(current, [], "", [])["correction"] is None


def test_within_fold_metadata_does_not_claim_outer_cv_variability():
    current = row()
    current["protocol"] = {
        "cv_repeat_unit": "within_fold",
        "cv_folds": 10,
        "cv_repetitions": 10,
        "variability_scope": "cv_averages",
    }
    protocol = safe_assignment(current, [], "", [])["protocol"]
    assert protocol["variability_scope"] == "unknown"
    assert "within each fold" in protocol["explanation"]


def test_metric_split_qualifiers_do_not_hide_macro_definition():
    assert metric_key("Test AP") == metric_key("AP")
    assert metric_key("Train Accuracy") == metric_key("Acc")
    assert metric_key("Test F1") == metric_key("F1")
    assert metric_key("Test F1-macro") != metric_key("F1")


def test_partial_normalization_from_grounded_percentage_cell(monkeypatch):
    import experiments.table_provenance_experiment.check_assignment_safety as safety

    # Anchoring has its own tests; this regression exercises the unit-conversion gate.
    monkeypatch.setattr(safety, "grounded_candidate", lambda candidate, source: candidate)
    current = row("repair_unverified")
    current.update(dataset="PubMed", metric="Accuracy", model="LabelProp", value=0.6344, std=0.04)
    span = {"start_line": 1, "end_line": 1}
    current["selected_candidate"] = {
        "table_id": 2,
        "displayed_mean": 63.44,
        "displayed_std": 0.04,
        "divisor": 100,
        "method": "LabelProp",
        "dataset": "PubMed",
        "metric": "Accuracy",
        "configuration": "Original split",
        "eligibility": "benchmark",
        "main_experiment": True,
        "row_evidence": span,
        "column_evidence": span,
        "cell_evidence": span,
        "protocol": {
            "design": "unknown",
            "explanation": "No count",
            "training_repetitions": None,
            "cv_folds": None,
            "cv_repetitions": None,
            "dataset_splits": None,
            "repetitions_per_split": None,
            "reported_runs": None,
            "variability_scope": "unknown",
            "evidence": [],
            "scope_evidence": [],
        },
    }
    assert partial_std_repair(current, "cell")["corrected"]["std"] == 0.0004
    current["std"] = 0.0004
    assert partial_std_repair(current, "cell") is None
