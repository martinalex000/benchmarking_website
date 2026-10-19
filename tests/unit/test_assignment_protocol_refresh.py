import hashlib
import json

import pytest

from backend.repetition_metadata import Verification
from experiments.table_provenance_experiment.assignment_pipeline_checks import (
    has_reviewed_inner_cv,
    reviewed_protocol,
)
from experiments.table_provenance_experiment.assignment_protocol_refresh import (
    update_single_cv_keys,
)
from experiments.table_provenance_experiment.check_protocol_binding import input_total
from experiments.table_provenance_experiment.run_mapping_batch import IdentityVerdict
from experiments.table_provenance_experiment.verify_stored_mapping_v3 import propose
from tests.unit.test_mapping_protocol_binding import key
from tests.unit.test_result_table_mapping_v3 import fixture


def verification(record, **changes):
    return Verification.model_validate(
        {
            "methods": [
                {
                    "table_id": record["table_id"],
                    "name": record["method"]["name"],
                    **dict.fromkeys(
                        (
                            "benchmark_supported",
                            "origin_supported",
                            "count_supported",
                            "unit_correct",
                            "uniform_datasets",
                        ),
                        True,
                    ),
                    "explanation": "Primary source confirms performance folds",
                    **changes,
                }
            ]
        }
    )


def test_single_cv_refresh_accepts_folds_without_inventing_outer_repeat():
    previous = key(
        design="single_cv",
        cv_folds=10,
        repetitions=None,
        status="unstated",
        count_evidence=[{"start_line": 1, "end_line": 1}],
    )
    previous["previous_verdict"]["count_supported"] = False
    updated = update_single_cv_keys([previous], verification(previous), "We perform 10-fold CV.")
    assert input_total(updated[0]) == 10
    assert updated[0]["method"]["repetitions"] is None
    assert input_total(previous) is None


def test_single_cv_refresh_respects_tuning_rejection_and_source_grounding():
    previous = key(
        design="single_cv",
        cv_folds=10,
        repetitions=None,
        status="unstated",
        count_evidence=[{"start_line": 1, "end_line": 1}],
    )
    updated = update_single_cv_keys(
        [previous],
        verification(previous, count_supported=False),
        "We tune parameters using 10-fold CV.",
    )
    assert input_total(updated[0]) is None
    updated = update_single_cv_keys([previous], verification(previous), "No fold count stated.")
    assert input_total(updated[0]) is None


def reviewed_fixture():
    row, initial, source = fixture()
    source = source.replace("5 runs", "10-fold CV for tuning, repeated 10 times")
    row.update(dataset="Cora", metric="Accuracy", variant="10-fold CV")
    raw = initial.model_dump()
    raw.update(selected_candidate_index=0, presentations=[])
    raw["corrected_fact"]["candidates"][0].update(
        cell_column_index=1,
        configuration_axes={"setting": "default"},
        identity_evidence=[{"start_line": 2, "end_line": 2}],
    )
    verdict = IdentityVerdict.model_validate(raw)
    record = {
        "table_id": 1,
        "method": "Own",
        "count": 10,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "evidence": [{"start_line": 5, "end_line": 5}],
        "scope_evidence": [{"start_line": 5, "end_line": 5}],
        "interpretation": "Human-reviewed: ten evaluations, inner tuning folds excluded",
    }
    return row, verdict, source, record


def test_reviewed_count_remains_scoped_and_does_not_change_origins(tmp_path):
    row, verdict, source, record = reviewed_fixture()
    updated = reviewed_protocol(verdict, [record], source)
    assert updated.corrected_fact.origin == verdict.corrected_fact.origin
    assert updated.corrected_fact.candidates[0].protocol.training_repetitions == 10
    assert verdict.corrected_fact.candidates[0].protocol.training_repetitions == 5
    assert propose(row, updated, source, allow_identity=True)["proposed_num_runs"] is None
    (tmp_path / "reviewed_protocols.json").write_text(json.dumps([record]))
    assert has_reviewed_inner_cv(updated, source, tmp_path)
    assert (
        propose(row, updated, source, allow_identity=True, reviewed_inner_cv=True)[
            "proposed_num_runs"
        ]
        == 10
    )
    wrong = {**record, "method": "Other"}
    assert reviewed_protocol(verdict, [wrong], source) == verdict
    with pytest.raises(ValueError, match="source/identity"):
        reviewed_protocol(verdict, [{**record, "source_sha256": "wrong"}], source)
