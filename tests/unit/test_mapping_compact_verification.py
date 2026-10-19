import pytest

from backend.mapping.compact_verification import (
    CompactCandidateAddition,
    CompactCandidatePatch,
    CompactFactPatch,
    CompactRepairPatch,
    CompactRowDecision,
    CompactVerification,
    compact_verification_prompt,
    merge_compact_verification,
)
from backend.mapping.coverage import coverage_flags
from backend.mapping.decisions import Repair
from backend.mapping.outputs import MappingCandidate, MappingFact, PresentationReview


def candidate():
    return MappingCandidate(
        table_id=1,
        displayed_mean=0.7,
        displayed_std=None,
        divisor=1,
        method="M",
        dataset="D",
        metric="Accuracy",
        configuration="default",
        eligibility="benchmark",
        main_experiment=True,
        row_evidence={"start_line": 1, "end_line": 1},
        column_evidence={"start_line": 1, "end_line": 1},
        cell_evidence={"start_line": 1, "end_line": 1},
        protocol={
            "design": "unknown",
            "training_repetitions": None,
            "cv_folds": None,
            "cv_repetitions": None,
            "dataset_splits": None,
            "repetitions_per_split": None,
            "reported_runs": None,
            "variability_scope": "unknown",
            "evidence": [],
            "scope_evidence": [],
            "explanation": "unknown",
        },
        cell_column_index=1,
        configuration_axes={},
        identity_evidence=[],
    )


def fact(result_id=10, origin="unclear", candidates=None):
    return MappingFact(
        result_id=result_id,
        candidates=[] if candidates is None else candidates,
        origin=origin,
        origin_evidence=[],
        execution_evidence=[],
        repair=None,
        explanation="initial extraction",
    )


def decision(result_id=10, verified=(), selected=None, presentations=()):
    return CompactRowDecision(
        result_id=result_id,
        verified_candidate_indices=list(verified),
        selected_candidate_index=selected,
        origin_supported=False,
        execution_supported=False,
        protocol_supported=False,
        repair_supported=False,
        setting_status="unverified",
        eligibility="unclear",
        presentations=list(presentations),
        protocol_scope_review=None,
        explanation="No candidate cell verified.",
    )


def output(*, ids=(10,), patches=()):
    return CompactVerification(
        reviewed_result_ids=list(ids),
        fact_patches=list(patches),
        repair_patches=[],
        candidate_patches=[],
        candidate_additions=[],
        decisions=[decision(result_id) for result_id in ids],
    )


def test_merges_compact_decisions_without_reemitting_facts():
    merged, counts = merge_compact_verification(
        [fact()], output(), [10], "source line one\nsource line two"
    )

    assert merged.verdicts[0].result_id == 10
    assert merged.verdicts[0].corrected_fact.origin == "unclear"
    assert counts == {
        "applied_fact_patches": 0,
        "applied_repair_patches": 0,
        "applied_candidate_patches": 0,
        "added_candidates": 0,
        "ignored_no_op_patches": 0,
    }


def test_applies_only_evidenced_fact_patch_and_ignores_noop():
    patches = [
        CompactFactPatch(
            result_id=10,
            field="origin",
            new_value="copied",
            evidence=[{"start_line": 1, "end_line": 1}],
            reason="The paper attributes this baseline to the cited result.",
        ),
        CompactFactPatch(
            result_id=10,
            field="execution_evidence",
            new_value=[],
            evidence=[{"start_line": 2, "end_line": 2}],
            reason="No-op must be ignored rather than retried.",
        ),
    ]

    merged, counts = merge_compact_verification(
        [fact()], output(patches=patches), [10], "Explicitly copied.\nMore source."
    )

    assert merged.verdicts[0].corrected_fact.origin == "copied"
    assert counts == {
        "applied_fact_patches": 1,
        "applied_repair_patches": 0,
        "applied_candidate_patches": 0,
        "added_candidates": 0,
        "ignored_no_op_patches": 1,
    }


def test_applies_multiple_candidate_field_patches_without_replacing_candidate():
    patches = [
        CompactCandidatePatch(
            result_id=10,
            candidate_index=0,
            field="table_id",
            new_value=3,
            evidence=[{"start_line": 1, "end_line": 1}],
            reason="The cited source span belongs to table inventory entry 3.",
        ),
        CompactCandidatePatch(
            result_id=10,
            candidate_index=0,
            field="divisor",
            new_value=100,
            evidence=[{"start_line": 1, "end_line": 1}],
            reason="The table reports percentages.",
        ),
        CompactCandidatePatch(
            result_id=10,
            candidate_index=0,
            field="cell_column_index",
            new_value=2,
            evidence=[{"start_line": 1, "end_line": 1}],
            reason="The cell is in the third physical column.",
        ),
    ]
    merged, counts = merge_compact_verification(
        [fact(candidates=[candidate()])],
        CompactVerification(
            reviewed_result_ids=[10],
            fact_patches=[],
            repair_patches=[],
            candidate_patches=patches,
            candidate_additions=[],
            decisions=[decision()],
        ),
        [10],
        "source line one",
    )

    corrected = merged.verdicts[0].corrected_fact.candidates[0]
    assert (corrected.table_id, corrected.divisor, corrected.cell_column_index) == (3, 100, 2)
    assert corrected.method == "M"
    assert counts == {
        "applied_fact_patches": 0,
        "applied_repair_patches": 0,
        "applied_candidate_patches": 3,
        "added_candidates": 0,
        "ignored_no_op_patches": 0,
    }


def test_applies_typed_repair_patch():
    repair = Repair(
        old_value=0.7,
        old_std=None,
        old_model="M",
        old_variant="old",
        corrected_value=0.75,
        corrected_std=None,
        corrected_model="M",
        corrected_variant="source-backed",
        evidence=[{"start_line": 1, "end_line": 1}],
        explanation="The source table contains the corrected score.",
    )
    patch = CompactRepairPatch(
        result_id=10,
        new_value=repair,
        evidence=[{"start_line": 1, "end_line": 1}],
        reason="The source cell differs from the stored value.",
    )
    merged, counts = merge_compact_verification(
        [fact()],
        CompactVerification(
            reviewed_result_ids=[10],
            fact_patches=[],
            repair_patches=[patch],
            candidate_patches=[],
            candidate_additions=[],
            decisions=[decision()],
        ),
        [10],
        "source line one",
    )

    assert merged.verdicts[0].corrected_fact.repair == repair
    assert counts == {
        "applied_fact_patches": 0,
        "applied_repair_patches": 1,
        "applied_candidate_patches": 0,
        "added_candidates": 0,
        "ignored_no_op_patches": 0,
    }


def test_rejects_missing_or_duplicate_reviewed_ids():
    with pytest.raises(ValueError, match="reviewed_result_ids"):
        merge_compact_verification([fact()], output(ids=()), [10], "source line one")


def test_rejects_duplicate_fact_patch_paths():
    patch = CompactFactPatch(
        result_id=10,
        field="origin",
        new_value="copied",
        evidence=[{"start_line": 1, "end_line": 1}],
        reason="source-backed",
    )
    with pytest.raises(ValueError, match="Duplicate fact patch"):
        merge_compact_verification(
            [fact()], output(patches=[patch, patch]), [10], "source line one"
        )


def test_rejects_duplicate_candidate_patch_paths():
    patch = CompactCandidatePatch(
        result_id=10,
        candidate_index=0,
        field="table_id",
        new_value=3,
        evidence=[{"start_line": 1, "end_line": 1}],
        reason="source-backed",
    )
    with pytest.raises(ValueError, match="Duplicate candidate patch"):
        merge_compact_verification(
            [fact(candidates=[candidate()])],
            CompactVerification(
                reviewed_result_ids=[10],
                fact_patches=[],
                repair_patches=[],
                candidate_patches=[patch, patch],
                candidate_additions=[],
                decisions=[decision()],
            ),
            [10],
            "source line one",
        )


def test_rejects_candidate_patch_with_invalid_index_or_value():
    patch = CompactCandidatePatch(
        result_id=10,
        candidate_index=1,
        field="table_id",
        new_value=3,
        evidence=[{"start_line": 1, "end_line": 1}],
        reason="source-backed",
    )
    with pytest.raises(ValueError, match="out of range"):
        merge_compact_verification(
            [fact(candidates=[candidate()])],
            CompactVerification(
                reviewed_result_ids=[10],
                fact_patches=[],
                repair_patches=[],
                candidate_patches=[patch],
                candidate_additions=[],
                decisions=[decision()],
            ),
            [10],
            "source line one",
        )

    bad_value = patch.model_copy(update={"candidate_index": 0, "field": "divisor", "new_value": 10})
    with pytest.raises(ValueError, match="Input should be 1 or 100"):
        merge_compact_verification(
            [fact(candidates=[candidate()])],
            CompactVerification(
                reviewed_result_ids=[10],
                fact_patches=[],
                repair_patches=[],
                candidate_patches=[bad_value],
                candidate_additions=[],
                decisions=[decision()],
            ),
            [10],
            "source line one",
        )


def test_rejects_evidence_outside_source():
    patch = CompactFactPatch(
        result_id=10,
        field="origin",
        new_value="copied",
        evidence=[{"start_line": 3, "end_line": 3}],
        reason="source-backed",
    )
    with pytest.raises(ValueError, match="outside the source"):
        merge_compact_verification([fact()], output(patches=[patch]), [10], "one line\ntwo lines")


def test_compact_prompt_replaces_full_fact_output_contract():
    prompt = compact_verification_prompt(
        "Return corrected_fact as a FULL replacement fact.\n\n"
        "Verification rules mention corrected_fact and complete row coverage."
    )

    assert "Do NOT re-emit the complete fact" in prompt
    assert "candidate_patches" in prompt
    assert "candidate_additions" in prompt
    assert "repair_patches" in prompt
    assert "explanatory prose alone is not a correction" in prompt
    assert "FULL replacement fact" not in prompt
    assert "source-first fact after applying all patches" in prompt


def test_adds_source_grounded_candidate_missing_from_initial_facts():
    addition = CompactCandidateAddition(
        result_id=10,
        candidate=candidate(),
        reason="The table is an additional same-experiment presentation.",
    )
    verification = CompactVerification(
        reviewed_result_ids=[10],
        fact_patches=[],
        repair_patches=[],
        candidate_patches=[],
        candidate_additions=[addition],
        decisions=[
            decision(
                verified=[0],
                selected=0,
                presentations=[
                    PresentationReview(
                        table_id=1,
                        decision="same_experiment",
                        evidence=[{"start_line": 1, "end_line": 1}],
                        explanation="A second same-experiment presentation.",
                    )
                ],
            )
        ],
    )

    merged, counts = merge_compact_verification([fact()], verification, [10], "source line one")

    assert len(merged.verdicts[0].corrected_fact.candidates) == 1
    assert merged.verdicts[0].verified_candidate_indices == [0]
    assert counts["added_candidates"] == 1
    assert coverage_flags(merged.verdicts[0], [1], "source line one") == []


def test_rejects_candidate_addition_with_out_of_source_evidence():
    invalid = MappingCandidate.model_validate(
        candidate().model_dump() | {"cell_evidence": {"start_line": 2, "end_line": 2}}
    )
    verification = CompactVerification(
        reviewed_result_ids=[10],
        fact_patches=[],
        repair_patches=[],
        candidate_patches=[],
        candidate_additions=[
            CompactCandidateAddition(result_id=10, candidate=invalid, reason="source-backed")
        ],
        decisions=[decision()],
    )
    with pytest.raises(ValueError, match="outside the source"):
        merge_compact_verification([fact()], verification, [10], "one line")
