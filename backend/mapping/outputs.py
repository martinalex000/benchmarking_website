"""Complete per-row outputs for extraction and independent verification."""

from typing import Literal

from pydantic import Field, StrictBool, StrictInt, model_validator

from backend.mapping.decisions import Candidate, Fact, Verdict
from backend.mapping.schema import Span, StrictModel


class PresentationReview(StrictModel):
    table_id: StrictInt
    decision: Literal[
        "same_experiment", "different_configuration", "ablation", "not_matching", "unclear"
    ]
    evidence: list[Span]
    explanation: str


class MappingCandidate(Candidate):
    cell_column_index: StrictInt | None = Field(...)
    configuration_axes: dict[str, str] = Field(...)
    identity_evidence: list[Span] = Field(...)


class MappingFact(Fact):
    candidates: list[MappingCandidate]


class MappingFacts(StrictModel):
    facts: list[MappingFact]


class ProtocolScopeReview(StrictModel):
    prior_reconciled: StrictBool
    scope_supported: StrictBool
    evidence: list[Span]
    explanation: str


class MappingVerdict(Verdict):
    corrected_fact: MappingFact
    presentations: list[PresentationReview]
    selected_candidate_index: StrictInt | None = Field(...)
    protocol_scope_review: ProtocolScopeReview | None = Field(...)

    @model_validator(mode="after")
    def valid_selection(self):
        if self.result_id != self.corrected_fact.result_id:
            raise ValueError("Verdict and fact must have the same result ID")
        indices = self.verified_candidate_indices
        if len(indices) != len(set(indices)) or any(
            not 0 <= index < len(self.corrected_fact.candidates) for index in indices
        ):
            raise ValueError("Verified indices are duplicated or out of range")
        if indices and self.selected_candidate_index not in indices:
            raise ValueError("Explicitly select a verified candidate or abstain with empty indices")
        if not indices and self.selected_candidate_index is not None:
            raise ValueError("Cannot select a candidate that was not verified")
        return self


class MappingVerdicts(StrictModel):
    verdicts: list[MappingVerdict]
