"""Explicit overall-CV repeats cannot be collapsed into a single fold average."""

import pytest

from backend.repetition_consistency import protocol_consistency_errors


@pytest.mark.parametrize("number", ["10", "ten", "$10$"])
def test_overall_cv_repetitions_reject_single_cv(number):
    source = f"We use 10-fold cross validation. We then report averages by performing overall experiments {number} times."
    protocol = {"design": "single_cv", "evidence": [{"start_line": 1, "end_line": 1}]}
    assert protocol_consistency_errors(protocol, source) == [
        "single_cv_omits_explicit_overall_repetitions"
    ]


def test_ten_runs_alone_is_not_proof_of_ten_complete_cv_runs():
    protocol = {"design": "single_cv", "evidence": [{"start_line": 1, "end_line": 1}]}
    assert protocol_consistency_errors(protocol, "Mean over 10 runs of 10-fold CV.") == []


def test_other_experiment_scope_is_not_used_for_veto():
    protocol = {"design": "single_cv", "evidence": [{"start_line": 1, "end_line": 1}]}
    assert (
        protocol_consistency_errors(
            protocol, "Mean across the 10 folds.\nWe repeat overall experiments 10 times."
        )
        == []
    )


def test_corrected_repeated_cv_is_not_rejected():
    assert (
        protocol_consistency_errors(
            {"design": "repeated_cv"}, "We repeat overall experiments 10 times."
        )
        == []
    )
