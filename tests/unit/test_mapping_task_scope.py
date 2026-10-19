import hashlib

import pytest

from backend.mapping.binding import candidate_identity
from backend.mapping.task_scope import TaskScopeReview, guard_task_scope


def fixture(decision="compatible"):
    source = "Predictions on explainer subgraphs measure explanation accuracy.\nGem & 72.8\n"
    row = {
        "result_id": 12,
        "evaluation_task": "graph_classification",
        "action": "propose_count",
        "proposed_num_runs": 10,
        "selected_candidate": {
            "table_id": 1,
            "metric": "Accuracy",
            "cell_evidence": {"start_line": 2, "end_line": 2},
        },
        "correction": {"old": {"value": 0.72}, "corrected": {"value": 0.728}},
    }
    review = TaskScopeReview(
        result_id=12,
        independently_verified=True,
        source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        candidate_sha256=candidate_identity(row["selected_candidate"]),
        intended_task="graph_classification",
        measured_task="explanation_evaluation",
        measured_metric="explanation_accuracy",
        decision=decision,
        task_evidence=[{"start_line": 1, "end_line": 1}],
        cell_scope_evidence=[{"start_line": 2, "end_line": 2}],
        explanation="Explanation predictions are not full-input classifier performance.",
        call_refs=["verifier_attempt_001/output.json"],
    )
    return row, source, review


def test_verified_incompatible_target_quarantines_without_numeric_repair():
    row, source, review = fixture("incompatible")
    result = guard_task_scope(row, source, review)
    assert result["action"] == "propose_quarantine"
    assert result["reason"] == "incompatible_evaluation_target"
    assert result["proposed_num_runs"] is None
    assert result["correction"] is None
    assert result["withheld_task_scope_repair"] == row["correction"]
    assert row["action"] == "propose_count"


def test_compatible_review_retains_action_and_correction():
    row, source, review = fixture()
    review = review.model_copy(
        update={"measured_task": "graph_classification", "measured_metric": "Accuracy"}
    )
    result = guard_task_scope(row, source, review)
    assert result["action"] == "propose_count"
    assert result["correction"] == row["correction"]


@pytest.mark.parametrize(
    "change",
    [
        {"independently_verified": False},
        {"source_sha256": "stale"},
        {"candidate_sha256": "wrong cell"},
        {"intended_task": "node_classification"},
        {"result_id": 13},
        {"task_evidence": []},
        {"cell_scope_evidence": []},
        {"call_refs": []},
        {"decision": "unclear"},
    ],
)
def test_missing_or_unbound_review_never_authorizes_changes(change):
    row, source, review = fixture("incompatible")
    review = TaskScopeReview.model_validate({**review.model_dump(), **change})
    result = guard_task_scope(row, source, review)
    assert result["action"] == "task_scope_unresolved"
    assert result["proposed_num_runs"] is None
    assert result["correction"] is None


def test_missing_review_does_not_invent_task_compatibility():
    row, source, _ = fixture()
    assert guard_task_scope(row, source, None)["action"] == "task_scope_unresolved"


def test_compatible_flag_cannot_override_contradictory_task_fields():
    row, source, review = fixture("compatible")
    assert guard_task_scope(row, source, review)["action"] == "task_scope_unresolved"
