"""Compact verification output that reuses source-first facts without echoing them."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Literal

from pydantic import Field, StrictBool, StrictInt

from backend.mapping.decisions import Repair
from backend.mapping.outputs import (
    MappingCandidate,
    MappingFact,
    MappingVerdict,
    MappingVerdicts,
    PresentationReview,
    ProtocolScopeReview,
)
from backend.mapping.schema import Span, StrictModel


class CompactFactPatch(StrictModel):
    result_id: StrictInt
    field: Literal[
        "origin",
        "origin_evidence",
        "execution_evidence",
    ]
    new_value: Any
    evidence: list[Span]
    reason: str


class CompactRepairPatch(StrictModel):
    result_id: StrictInt
    new_value: Repair | None
    evidence: list[Span]
    reason: str


class CompactCandidatePatch(StrictModel):
    result_id: StrictInt
    candidate_index: StrictInt = Field(ge=0)
    field: Literal[
        "table_id",
        "displayed_mean",
        "displayed_std",
        "divisor",
        "method",
        "dataset",
        "metric",
        "configuration",
        "eligibility",
        "main_experiment",
        "row_evidence",
        "column_evidence",
        "cell_evidence",
        "protocol",
        "cell_column_index",
        "configuration_axes",
        "identity_evidence",
    ]
    new_value: Any
    evidence: list[Span]
    reason: str


class CompactCandidateAddition(StrictModel):
    result_id: StrictInt
    candidate: MappingCandidate
    reason: str


class CompactRowDecision(StrictModel):
    result_id: StrictInt
    verified_candidate_indices: list[StrictInt]
    selected_candidate_index: StrictInt | None
    origin_supported: StrictBool
    execution_supported: StrictBool
    protocol_supported: StrictBool
    repair_supported: StrictBool
    setting_status: Literal["supported", "unverified", "contradicted"]
    eligibility: Literal["benchmark", "ablation", "other", "unclear"]
    presentations: list[PresentationReview]
    protocol_scope_review: ProtocolScopeReview | None
    explanation: str


class CompactVerification(StrictModel):
    reviewed_result_ids: list[StrictInt]
    fact_patches: list[CompactFactPatch]
    repair_patches: list[CompactRepairPatch]
    candidate_patches: list[CompactCandidatePatch]
    candidate_additions: list[CompactCandidateAddition]
    decisions: list[CompactRowDecision]


def merge_compact_verification(
    facts: list[MappingFact],
    verification: CompactVerification,
    expected_ids: list[int],
    source: str,
) -> tuple[MappingVerdicts, dict[str, int]]:
    """Merge a compact verifier response into source-first facts, failing closed."""
    if len(expected_ids) != len(set(expected_ids)):
        raise ValueError("Expected result IDs must be unique")
    fact_ids = [fact.result_id for fact in facts]
    if len(fact_ids) != len(set(fact_ids)) or set(fact_ids) != set(expected_ids):
        raise ValueError("Source-first facts must cover each expected result exactly once")
    if len(verification.reviewed_result_ids) != len(set(verification.reviewed_result_ids)) or set(
        verification.reviewed_result_ids
    ) != set(expected_ids):
        raise ValueError("Verifier reviewed_result_ids must cover each expected ID exactly once")
    decision_ids = [decision.result_id for decision in verification.decisions]
    if len(decision_ids) != len(set(decision_ids)) or set(decision_ids) != set(expected_ids):
        raise ValueError("Verifier decisions must cover each expected result exactly once")

    source_lines = source.splitlines()
    fact_by_id = {fact.result_id: fact.model_dump(mode="json") for fact in facts}
    seen_fields: set[tuple[int, str]] = set()
    applied_fact_patches = 0
    applied_repair_patches = 0
    applied_candidate_patches = 0
    added_candidates = 0
    no_op_patches = 0

    def check_patch_evidence(evidence, reason: str, label: str) -> None:
        if not evidence or not reason.strip():
            raise ValueError(f"{label} require source evidence and a reason")
        if any(
            span.start_line < 1
            or span.end_line < span.start_line
            or span.end_line > len(source_lines)
            for span in evidence
        ):
            raise ValueError("Patch evidence is outside the source line range")

    for patch in verification.fact_patches:
        if patch.result_id not in fact_by_id:
            raise ValueError(f"Fact patch references unknown result {patch.result_id}")
        key = (patch.result_id, patch.field)
        if key in seen_fields:
            raise ValueError(f"Duplicate fact patch for result {patch.result_id}: {patch.field}")
        seen_fields.add(key)
        check_patch_evidence(patch.evidence, patch.reason, "Fact patches")
        target = fact_by_id[patch.result_id]
        if target[patch.field] == patch.new_value:
            no_op_patches += 1
            continue
        target[patch.field] = deepcopy(patch.new_value)
        applied_fact_patches += 1

    seen_repair_ids: set[int] = set()
    for patch in verification.repair_patches:
        if patch.result_id not in fact_by_id:
            raise ValueError(f"Repair patch references unknown result {patch.result_id}")
        if patch.result_id in seen_repair_ids:
            raise ValueError(f"Duplicate repair patch for result {patch.result_id}")
        seen_repair_ids.add(patch.result_id)
        check_patch_evidence(patch.evidence, patch.reason, "Repair patches")
        target = fact_by_id[patch.result_id]
        new_value = None if patch.new_value is None else patch.new_value.model_dump(mode="json")
        if target["repair"] == new_value:
            no_op_patches += 1
            continue
        target["repair"] = deepcopy(new_value)
        applied_repair_patches += 1

    seen_candidate_fields: set[tuple[int, int, str]] = set()
    for patch in verification.candidate_patches:
        if patch.result_id not in fact_by_id:
            raise ValueError(f"Candidate patch references unknown result {patch.result_id}")
        key = (patch.result_id, patch.candidate_index, patch.field)
        if key in seen_candidate_fields:
            raise ValueError(
                "Duplicate candidate patch for result "
                f"{patch.result_id}, candidate {patch.candidate_index}: {patch.field}"
            )
        seen_candidate_fields.add(key)
        check_patch_evidence(patch.evidence, patch.reason, "Candidate patches")
        target = fact_by_id[patch.result_id]
        candidates = target["candidates"]
        if patch.candidate_index >= len(candidates):
            raise ValueError(
                f"Candidate patch index {patch.candidate_index} is out of range "
                f"for result {patch.result_id}"
            )
        candidate = candidates[patch.candidate_index]
        if candidate[patch.field] == patch.new_value:
            no_op_patches += 1
            continue
        updated = deepcopy(candidate)
        updated[patch.field] = deepcopy(patch.new_value)
        candidates[patch.candidate_index] = MappingCandidate.model_validate(updated).model_dump(
            mode="json"
        )
        applied_candidate_patches += 1

    for addition in verification.candidate_additions:
        if addition.result_id not in fact_by_id:
            raise ValueError(f"Candidate addition references unknown result {addition.result_id}")
        if not addition.reason.strip():
            raise ValueError("Candidate additions require a reason")
        evidence = [
            addition.candidate.row_evidence,
            addition.candidate.column_evidence,
            addition.candidate.cell_evidence,
            *addition.candidate.protocol.evidence,
            *addition.candidate.protocol.scope_evidence,
            *addition.candidate.identity_evidence,
        ]
        check_patch_evidence(evidence, addition.reason, "Candidate additions")
        target = fact_by_id[addition.result_id]
        target["candidates"].append(addition.candidate.model_dump(mode="json"))
        added_candidates += 1

    decisions = {decision.result_id: decision for decision in verification.decisions}
    verdicts = []
    for result_id in expected_ids:
        fact = MappingFact.model_validate(fact_by_id[result_id])
        decision = decisions[result_id]
        verdicts.append(
            MappingVerdict(
                result_id=result_id,
                corrected_fact=fact,
                verified_candidate_indices=decision.verified_candidate_indices,
                selected_candidate_index=decision.selected_candidate_index,
                origin_supported=decision.origin_supported,
                execution_supported=decision.execution_supported,
                protocol_supported=decision.protocol_supported,
                repair_supported=decision.repair_supported,
                setting_status=decision.setting_status,
                eligibility=decision.eligibility,
                presentations=decision.presentations,
                protocol_scope_review=decision.protocol_scope_review,
                explanation=decision.explanation,
            )
        )
    return MappingVerdicts(verdicts=verdicts), {
        "applied_fact_patches": applied_fact_patches,
        "applied_repair_patches": applied_repair_patches,
        "applied_candidate_patches": applied_candidate_patches,
        "added_candidates": added_candidates,
        "ignored_no_op_patches": no_op_patches,
    }


def compact_verification_prompt(full_prompt: str) -> str:
    """Keep maintained review rules while requesting compact, typed source-grounded patches."""
    _, _, review_rules = full_prompt.partition("\n\n")
    if not review_rules:
        raise ValueError("Full verification prompt has no review-rule section")
    review_rules = review_rules.replace(
        "corrected_fact", "source-first fact after applying all patches"
    )
    contract = (
        "Independently verify EVERY stored row against the primary numbered LaTeX. "
        "Input contains source-first facts from a fallible initial model. Return one compact "
        "decision per result_id and list every reviewed ID exactly once. Do NOT re-emit the "
        "complete fact or candidate objects. Return fact_patches only for source-grounded "
        "changes to origin, origin_evidence, or execution_evidence. Return repair_patches "
        "for old-to-corrected row metadata; each new_value must match the typed Repair object "
        "in the schema, or null to remove an unsupported repair. For candidate "
        "corrections to an existing candidate, return candidate_patches with result_id, candidate_index, one candidate "
        "field, native-JSON new_value, source evidence, and a short reason. When validation "
        "feedback names a wrong candidate field, emit a patch for that field; explanatory prose "
        "alone is not a correction. For a source-grounded result presentation absent from the "
        "input candidates (including a distinct same-experiment table presentation), return a "
        "candidate_additions entry containing result_id, a complete typed candidate object, "
        "and a short reason. Additions are appended after existing candidates in listed order; "
        "verified/selected candidate indices in decisions refer to this final combined list. "
        "Use additions only for genuinely absent candidates, not to duplicate an existing one. "
        "On a feedback round, preserve valid prior patches and candidate additions; repeat them "
        "in the response unless the supplied feedback specifically shows they are incorrect. "
        "Never replace the whole candidate list. "
        "No old stored number or unverified initial fact is ground truth. Empty patch lists "
        "mean the initial facts were checked and retained. In decisions, include every field "
        "needed to build the final verdict: verified_candidate_indices, selected_candidate_index, "
        "support flags, setting_status, eligibility, presentations, protocol_scope_review, and a "
        "brief explanation. Keep the supplied result IDs exact.\n\n"
    )
    return contract + review_rules
