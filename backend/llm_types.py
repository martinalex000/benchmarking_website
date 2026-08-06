"""Shared data types for LLM extraction and inspection workflows."""

from __future__ import annotations

import re
from dataclasses import dataclass
from dataclasses import field as dc_field
from typing import Any

from pydantic import BaseModel, Field, field_validator

from backend.model_metadata import normalize_architecture_type

INPUT_FEATURE_SOURCE_VALUES = frozenset(
    {
        "raw_features",
        "llm_features",
        "other_external_features",
        "mixed",
        "unknown",
    }
)


def normalize_input_feature_source(value: Any) -> str | None:
    """Normalize the feature provenance emitted by an extraction model."""
    if value is None:
        return None
    normalized = str(value).strip().casefold().replace("-", "_").replace(" ", "_")
    aliases = {
        "raw": "raw_features",
        "dataset_features": "raw_features",
        "llm": "llm_features",
        "lm_features": "llm_features",
        "plm_features": "llm_features",
        "slm_features": "llm_features",
        "external_features": "other_external_features",
        "other_external": "other_external_features",
        "unclear": "unknown",
    }
    normalized = aliases.get(normalized, normalized)
    return normalized if normalized in INPUT_FEATURE_SOURCE_VALUES else "unknown"


@dataclass
class CallRecord:
    """One LLM request/response exchange, captured for verbose inspection."""

    call_type: str
    system_prompt: str
    user_content: str
    raw_response: str = ""
    input_chars: int = 0
    output_chars: int = 0
    duration_s: float = 0.0
    ttft_s: float | None = None
    tokens_per_sec: float | None = None
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    success: bool = False
    parse_error: str | None = None
    parsed_result: Any = dc_field(default=None, repr=False)
    extra: dict = dc_field(default_factory=dict)


class ProposedModel(BaseModel):
    name: str
    supporting_sentence: str | None = None
    params_millions: float | None = None
    params_exact: int | None = None
    model_type: str | None = None

    @field_validator("model_type", mode="before")
    @classmethod
    def _normalize_model_type(cls, value: Any) -> str | None:
        return normalize_architecture_type(value if value is not None else None)


class BaselineModelInfo(BaseModel):
    name: str
    params_millions: float | None = None
    params_exact: int | None = None
    model_type: str | None = None
    original_paper_hint: str | None = None

    @field_validator("model_type", mode="before")
    @classmethod
    def _normalize_model_type(cls, value: Any) -> str | None:
        return normalize_architecture_type(value if value is not None else None)


class ResultEntry(BaseModel):
    model: str
    is_proposed: bool = False
    dataset: str
    metric: str
    value: float
    std: float | None = None
    higher_is_better: bool = True
    uses_external_data: bool | None = None
    input_feature_source: str | None = None
    feature_source_evidence: str | None = None
    table_ref: str | None = None
    source_ref: str | None = "this paper"
    evaluation_task: str | None = None
    protocol_decision: str | None = None
    uses_standard_protocol: bool | None = None
    protocol_note: str | None = None

    @field_validator("input_feature_source", mode="before")
    @classmethod
    def _normalize_input_feature_source(cls, value: Any) -> str | None:
        return normalize_input_feature_source(value)

    @field_validator("value", "std", mode="before")
    @classmethod
    def _coerce_numeric(cls, value: Any) -> Any:
        if value is None:
            return value
        if isinstance(value, str):
            value = re.sub(r"[^\d.\-]", "", value)
            if not value:
                return None
        return float(value)


class ScreenResult(BaseModel):
    has_benchmark_results: bool = False
    has_new_benchmark: bool = False
    datasets_mentioned: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    notes: str = ""


class DatasetInfo(BaseModel):
    name: str
    description: str | None = None
    task_type: str | None = None
    table_refs: list[str] = Field(default_factory=list)
    primary_metric: str | None = None
    metrics_seen: list[str] = Field(default_factory=list)
    expected_model_count: int | None = None
    variant_hint: str | None = None
    num_graphs: int | None = None
    avg_nodes: float | None = None
    avg_edges: float | None = None
    num_classes: int | None = None
    statistics_mentioned: bool = False
    statistics_sources: list[str] = Field(default_factory=list)

    @field_validator("expected_model_count", "num_graphs", "num_classes", mode="before")
    @classmethod
    def _coerce_integer(cls, value: Any) -> int | None:
        if value is None or value == "":
            return None
        try:
            return int(round(float(value)))
        except (TypeError, ValueError):
            return None

    @field_validator("avg_nodes", "avg_edges", mode="before")
    @classmethod
    def _coerce_float(cls, value: Any) -> float | None:
        if value is None or value == "":
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None


class DatasetList(BaseModel):
    datasets: list[DatasetInfo] = Field(default_factory=list)
    notes: str = ""


class DatasetStatisticsEntry(BaseModel):
    name: str
    variant: str | None = None
    num_graphs: int | None = None
    avg_nodes: float | None = None
    avg_edges: float | None = None
    num_classes: int | None = None
    raw_values: dict[str, str] = Field(default_factory=dict)
    precision_hints: dict[str, str] = Field(default_factory=dict)
    extra_stats: dict[str, float | int] = Field(default_factory=dict)
    source_ref: str | None = None
    confidence: str = "medium"


class DatasetStatisticsOutput(BaseModel):
    datasets: list[DatasetStatisticsEntry] = Field(default_factory=list)
    notes: str = ""


class SotaClaimRestriction(BaseModel):
    type: str = "other"
    description: str = ""


class SotaClaimEntry(BaseModel):
    raw_sentence: str
    claim_summary: str = ""
    datasets: list[str] = Field(default_factory=list)
    metrics: list[str] = Field(default_factory=list)
    claim_type: str = "other"
    scope: str = "unclear"
    restrictions: list[SotaClaimRestriction] = Field(default_factory=list)
    source_ref: str | None = None
    confidence: str = "medium"


class SotaClaimOutput(BaseModel):
    claims: list[SotaClaimEntry] = Field(default_factory=list)
    notes: str = ""


class ModelMetadataEnrichmentEntry(BaseModel):
    name: str
    model_type: str | None = None
    uses_external_data: bool | None = None

    @field_validator("model_type", mode="before")
    @classmethod
    def _normalize_model_type(cls, value: Any) -> str | None:
        return normalize_architecture_type(value if value is not None else None)


class ModelMetadataEnrichmentOutput(BaseModel):
    models: list[ModelMetadataEnrichmentEntry] = Field(default_factory=list)
    notes: str = ""


class ExtractionOutput(BaseModel):
    proposed_model: ProposedModel | None = None
    baseline_models: list[BaselineModelInfo] = Field(default_factory=list)
    results: list[ResultEntry] = Field(default_factory=list)
    extraction_confidence: str = "LOW"
    extraction_notes: str = ""
    coverage_assessment: str = "unknown"
    task_mismatch: bool = False
    discovered_datasets: list[DatasetInfo] = Field(default_factory=list)
    paper_has_statistics: bool = False

    @field_validator("proposed_model", mode="before")
    @classmethod
    def _require_model_name(cls, value: Any) -> Any:
        """Discard proposed_model when the LLM returns name=null or name='' ."""
        if value is None:
            return None
        if isinstance(value, dict) and not value.get("name"):
            return None
        return value


class FigureInfo(BaseModel):
    figure_id: str | None = None
    figure_number: int | None = None
    caption_snippet: str | None = None
    img_src: str | None = None
    page_number: int | None = None
    reason: str | None = None


class ModelSizeEntry(BaseModel):
    model_name: str
    matched_result_name: str | None = None
    dataset: str | None = None
    params_millions: float | None = None
    params_exact: int | None = None
    source_text: str | None = None
