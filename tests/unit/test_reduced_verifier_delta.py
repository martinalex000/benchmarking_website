import importlib.util
import sys
from pathlib import Path

import pytest

from backend.mapping.decisions import Repair
from backend.mapping.outputs import MappingFact, MappingVerdict

RUNNER_PATH = (
    Path(__file__).resolve().parents[2]
    / "experiments/table_provenance_experiment/run_2026-10-14_reduced_verifier_probe/run_reduced_verifier.py"
)
RUNNER_SPEC = importlib.util.spec_from_file_location("run_reduced_verifier", RUNNER_PATH)
assert RUNNER_SPEC and RUNNER_SPEC.loader
RUNNER = importlib.util.module_from_spec(RUNNER_SPEC)
sys.modules[RUNNER_SPEC.name] = RUNNER
RUNNER_SPEC.loader.exec_module(RUNNER)
ReducedVerifierOutput = RUNNER.ReducedVerifierOutput
normalize_legacy_baseline = RUNNER.normalize_legacy_baseline
validate_delta = RUNNER.validate_delta


def baseline():
    fact = MappingFact(
        result_id=10,
        candidates=[],
        origin="unclear",
        origin_evidence=[],
        execution_evidence=[],
        repair=None,
        explanation="",
    )
    verdict = MappingVerdict(
        result_id=10,
        corrected_fact=fact,
        verified_candidate_indices=[],
        selected_candidate_index=None,
        origin_supported=False,
        execution_supported=False,
        protocol_supported=False,
        repair_supported=False,
        setting_status="unverified",
        eligibility="unclear",
        explanation="",
        presentations=[],
        protocol_scope_review=None,
    )
    return {"verdicts": [verdict.model_dump(mode="json")]}


def patch(*, new_value="supported", evidence=None):
    return {
        "field": "verdict.setting_status",
        "new_value": new_value,
        "evidence": (evidence if evidence is not None else [{"start_line": 1, "end_line": 1}]),
        "reason": "The source explicitly supports this setting.",
    }


def parsed(changes):
    return ReducedVerifierOutput.model_validate(
        {
            "reviewed_result_ids": [10],
            "corrections": [{"result_id": 10, "changes": changes}],
        }
    )


def test_applies_native_json_patch_without_echoing_old_value():
    merged = validate_delta(parsed([patch()]), baseline(), [10], "source evidence line\nother line")

    assert merged["verdicts"][0]["setting_status"] == "supported"


def test_rejects_noop_patch():
    with pytest.raises(ValueError, match="no-op field patch"):
        validate_delta(
            parsed([patch(new_value="unverified")]),
            baseline(),
            [10],
            "source evidence line",
        )


def test_rejects_missing_evidence_and_out_of_range_evidence():
    with pytest.raises(ValueError, match="needs source evidence"):
        validate_delta(parsed([patch(evidence=[])]), baseline(), [10], "source evidence line")

    with pytest.raises(ValueError, match="outside the source line range"):
        validate_delta(
            parsed([patch(evidence=[{"start_line": 2, "end_line": 2}])]),
            baseline(),
            [10],
            "source evidence line",
        )


def test_rejects_invalid_merged_verdict_schema():
    with pytest.raises(ValueError):
        validate_delta(
            parsed([patch(new_value="certain")]),
            baseline(),
            [10],
            "source evidence line",
        )


def test_legacy_baseline_adds_missing_review_as_unknown_without_changing_other_fields():
    old_baseline = baseline()
    del old_baseline["verdicts"][0]["protocol_scope_review"]

    normalized, defaults = normalize_legacy_baseline(old_baseline)

    assert normalized["verdicts"][0]["protocol_scope_review"] is None
    assert defaults == {"protocol_scope_review": [10]}
    assert "protocol_scope_review" not in old_baseline["verdicts"][0]
    assert (
        normalized["verdicts"][0]["corrected_fact"] == old_baseline["verdicts"][0]["corrected_fact"]
    )


def test_repair_old_fields_must_match_the_frozen_stored_row():
    repair = Repair(
        old_value=0.7,
        old_std=None,
        old_model="M",
        old_variant="old",
        old_metric="Accuracy",
        corrected_value=0.75,
        corrected_std=None,
        corrected_model="M",
        corrected_variant="source-backed",
        corrected_metric="Accuracy",
        evidence=[{"start_line": 1, "end_line": 1}],
        explanation="Source cell differs from the stored value.",
    )
    repair_patch = {
        "field": "fact.repair",
        "new_value": repair.model_dump(mode="json"),
        "evidence": [{"start_line": 1, "end_line": 1}],
        "reason": "The source cell supports this repair.",
    }
    rows = {
        10: {
            "value": 0.7,
            "std": None,
            "model": "M",
            "variant": "old",
            "metric": "Accuracy",
        }
    }

    merged = validate_delta(parsed([repair_patch]), baseline(), [10], "source line", rows)
    assert merged["verdicts"][0]["corrected_fact"]["repair"]["corrected_value"] == 0.75

    rows[10]["value"] = 0.71
    with pytest.raises(ValueError, match="do not match stored row 10"):
        validate_delta(parsed([repair_patch]), baseline(), [10], "source line", rows)
