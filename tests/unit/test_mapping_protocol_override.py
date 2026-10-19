"""An upstream unknown is revisable, but never by unverified mapping prose."""

import copy
import hashlib

import pytest

from experiments.table_provenance_experiment.check_protocol_binding import (
    candidate_identity,
    check_binding,
)
from experiments.table_provenance_experiment.verify_stored_mapping_v3 import (
    Protocol,
    metric_key,
    total_models,
)


def fixture():
    source = "Own & 0.8 \\\\\nWe evaluate Own with 10 runs."
    protocol = Protocol(
        design="repeated_training",
        training_repetitions=10,
        cv_folds=None,
        cv_repetitions=None,
        dataset_splits=None,
        repetitions_per_split=None,
        reported_runs=10,
        variability_scope="training_runs",
        evidence=[{"start_line": 2, "end_line": 2}],
        scope_evidence=[{"start_line": 2, "end_line": 2}],
        explanation="Executed runs",
    )
    row = {
        "result_id": 1,
        "action": "propose_count",
        "proposed_num_runs": 10,
        "selected_candidate": {
            "table_id": 1,
            "method": "Own",
            "dataset": "Cora",
            "configuration": "GCN",
            "protocol": protocol.model_dump(),
        },
    }
    key = {
        "table_id": 1,
        "method": {"name": "Own", "origin": "self_evaluated", "status": "unknown"},
        "previous_verdict": {},
    }
    proof = {
        "result_id": 1,
        "independently_verified": True,
        "prior_reconciled": True,
        "scope_supported": True,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "candidate_sha256": candidate_identity(row["selected_candidate"]),
        "protocol": protocol.model_dump(),
        "explanation": "Missed scoped run statement",
        "call_refs": ["extract.json", "verify.json"],
    }
    return row, key, source, proof


def test_independent_source_bound_review_can_override_unknown():
    row, key, source, proof = fixture()
    result = check_binding(row, [key], source, [proof])
    assert result["action"] == "propose_count"
    assert result["protocol_binding"]["status"] == "independently_verified_protocol_override"
    assert result["protocol_binding"]["contains_unknown"] is True
    assert key["method"]["status"] == "unknown"


@pytest.mark.parametrize(
    "field,value",
    [
        ("independently_verified", False),
        ("prior_reconciled", False),
        ("scope_supported", False),
        ("source_sha256", "other"),
        ("candidate_sha256", "other"),
        ("call_refs", []),
        ("explanation", ""),
    ],
)
def test_incomplete_or_wrong_scope_review_does_not_bypass_guard(field, value):
    row, key, source, proof = fixture()
    proof[field] = value
    assert check_binding(row, [key], source, [proof])["action"] == "protocol_input_unresolved"


def test_duplicate_proof_and_cross_configuration_are_withheld():
    row, key, source, proof = fixture()
    assert check_binding(row, [key], source, [proof, proof])["proposed_num_runs"] is None
    row["selected_candidate"]["configuration"] = "GIN"
    assert check_binding(row, [key], source, [proof])["proposed_num_runs"] is None


def test_unsupported_number_and_changed_protocol_are_withheld():
    row, key, source, proof = fixture()
    proof["protocol"]["training_repetitions"] = 100
    assert check_binding(row, [key], source, [proof])["proposed_num_runs"] is None
    row["proposed_num_runs"] = 100
    row["selected_candidate"]["protocol"] = copy.deepcopy(proof["protocol"])
    assert check_binding(row, [key], source, [proof])["proposed_num_runs"] is None


def test_single_fixed_split_keeps_seed_count_but_resampling_is_special():
    _, _, _, proof = fixture()
    protocol = Protocol.model_validate(proof["protocol"])
    assert total_models(protocol.model_copy(update={"dataset_splits": 1})) == 10
    assert total_models(protocol.model_copy(update={"dataset_splits": 2})) is None
    assert (
        total_models(
            protocol.model_copy(update={"dataset_splits": 1, "variability_scope": "splits"})
        )
        is None
    )
    assert (
        total_models(protocol.model_copy(update={"dataset_splits": 1, "repetitions_per_split": 3}))
        is None
    )


def test_macro_f1_synonyms_do_not_conflate_micro_or_bare_f1():
    assert metric_key("macro F1") == metric_key("F1-macro")
    assert metric_key("micro F1") != metric_key("F1-macro")
    assert metric_key("F1") != metric_key("F1-macro")
