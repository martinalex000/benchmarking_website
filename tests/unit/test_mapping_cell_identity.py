"""A grounded numeric row is not enough to establish a cell or experiment."""

import pytest
from pydantic import ValidationError

from experiments.table_provenance_experiment.run_mapping_batch import (
    IdentityVerdict,
    source_first_content,
)
from experiments.table_provenance_experiment.verify_stored_mapping_v3 import (
    Candidate,
    Fact,
    Protocol,
    Span,
    Verdict,
    grounded_column,
    propose,
)


def fixture():
    source = "\n".join(
        [
            r"\begin{table}",
            r"Method & Cora coo & Cora reg-bound \\",
            r"Own & 80.0 $\pm$ 0.2 & 90.0 $\pm$ 0.3 \\",
            r"\end{table}",
            "We evaluate Own with 5 runs.",
        ]
    )
    protocol = Protocol(
        design="repeated_training",
        training_repetitions=5,
        cv_folds=None,
        cv_repetitions=None,
        dataset_splits=None,
        repetitions_per_split=None,
        reported_runs=5,
        variability_scope="training_runs",
        explanation="Explicit runs",
        evidence=[Span(start_line=5, end_line=5)],
        scope_evidence=[Span(start_line=5, end_line=5)],
    )
    candidate = Candidate(
        table_id=1,
        displayed_mean=80,
        displayed_std=0.2,
        divisor=100,
        method="Own",
        dataset="Cora",
        metric="Accuracy",
        configuration="coo",
        eligibility="benchmark",
        main_experiment=False,
        row_evidence=Span(start_line=3, end_line=3),
        column_evidence=Span(start_line=2, end_line=2),
        cell_evidence=Span(start_line=3, end_line=3),
        protocol=protocol,
        cell_column_index=1,
        configuration_axes={"graph_format": "coo"},
        identity_evidence=[Span(start_line=2, end_line=2)],
    )
    fact = Fact(
        result_id=1,
        candidates=[candidate],
        origin="self_evaluated",
        origin_evidence=[Span(start_line=5, end_line=5)],
        execution_evidence=[Span(start_line=5, end_line=5)],
        repair=None,
        explanation="Verified",
    )
    verdict = Verdict(
        result_id=1,
        corrected_fact=fact,
        verified_candidate_indices=[0],
        origin_supported=True,
        execution_supported=True,
        protocol_supported=True,
        repair_supported=False,
        setting_status="supported",
        eligibility="benchmark",
        explanation="Verified",
        selected_candidate_index=0,
    )
    row = {
        "result_id": 1,
        "model": "Own",
        "dataset": "Cora",
        "metric": "Accuracy",
        "variant": "coo",
        "value": 0.8,
        "std": 0.002,
    }
    return row, verdict, source


def test_matching_numeric_row_but_wrong_physical_column_is_rejected():
    _, verdict, source = fixture()
    candidate = verdict.corrected_fact.candidates[0]
    assert grounded_column(candidate, source)
    candidate.cell_column_index = 2
    assert not grounded_column(candidate, source)


def test_mean_and_std_must_be_in_the_same_cell():
    _, verdict, source = fixture()
    candidate = verdict.corrected_fact.candidates[0]
    candidate.displayed_std = 0.3
    assert not grounded_column(candidate, source)


def test_priority_does_not_jump_to_another_configuration():
    row, verdict, source = fixture()
    other = verdict.corrected_fact.candidates[0].model_copy(
        update={
            "displayed_mean": 90,
            "displayed_std": 0.3,
            "cell_column_index": 2,
            "configuration": "reg-bound",
            "configuration_axes": {"graph_format": "reg-bound"},
            "main_experiment": True,
        }
    )
    verdict.corrected_fact.candidates.append(other)
    verdict.verified_candidate_indices = [0, 1]
    result = propose(row, verdict, source, allow_identity=True)
    assert result["selected_candidate"]["configuration"] == "coo"
    assert result["proposed_num_runs"] == 5


def test_database_numeric_match_cannot_move_intended_dataset():
    row, verdict, source = fixture()
    verdict.corrected_fact.candidates[0].dataset = "Other dataset"
    assert (
        propose(row, verdict, source, allow_identity=True)["action"]
        == "dataset_identity_unresolved"
    )


def test_sole_verified_candidate_can_supply_omitted_selection():
    row, verdict, source = fixture()
    verdict.selected_candidate_index = None
    assert propose(row, verdict, source, allow_identity=True)["action"] == "propose_count"


def test_multiple_verified_candidates_still_require_explicit_selection():
    row, verdict, source = fixture()
    verdict.selected_candidate_index = None
    verdict.corrected_fact.candidates.append(verdict.corrected_fact.candidates[0].model_copy())
    verdict.verified_candidate_indices = [0, 1]
    assert (
        propose(row, verdict, source, allow_identity=True)["action"]
        == "experiment_identity_unresolved"
    )


def test_no_configuration_or_identity_evidence_means_abstention():
    _, verdict, source = fixture()
    candidate = verdict.corrected_fact.candidates[0]
    candidate.configuration_axes = {}
    assert not grounded_column(candidate, source)


def test_new_schema_requires_selection_instead_of_silently_defaulting_null():
    _, verdict, _ = fixture()
    data = verdict.model_dump()
    data["presentations"] = []
    assert IdentityVerdict.model_validate(data).selected_candidate_index == 0
    del data["selected_candidate_index"]
    with pytest.raises(ValidationError):
        IdentityVerdict.model_validate(data)


def test_new_schema_requires_column_and_verifies_selection_index():
    _, verdict, _ = fixture()
    data = verdict.model_dump()
    data["presentations"] = []
    data["selected_candidate_index"] = None
    with pytest.raises(ValidationError):
        IdentityVerdict.model_validate(data)
    data["selected_candidate_index"] = 0
    del data["corrected_fact"]["candidates"][0]["cell_column_index"]
    with pytest.raises(ValidationError):
        IdentityVerdict.model_validate(data)


def test_source_first_stage_does_not_receive_old_numeric_anchors(tmp_path):
    (tmp_path / "protocol_keys.json").write_text("[]")
    current = {
        "result_id": 1,
        "model": "Own",
        "dataset": "Cora",
        "variant": "Standard split",
        "metric": "Accuracy",
        "value": 0.987654321,
        "std": 0.123456789,
    }
    text = source_first_content(tmp_path, "A source table", "example", [current])
    assert "0.987654321" not in text
    assert "0.123456789" not in text
    assert '"dataset": "Cora"' in text
