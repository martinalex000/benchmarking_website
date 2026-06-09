"""Match paper-reported dataset statistics against canonical DB values."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from backend.dataset_stats_parsing import parse_extra_stats, values_compatible

_CORE_FIELDS = ("num_graphs", "avg_nodes", "avg_edges", "num_classes")
_INTEGER_FIELDS = {"num_graphs", "num_classes"}


@dataclass
class StatsObservation:
    num_graphs: int | None = None
    avg_nodes: float | None = None
    avg_edges: float | None = None
    num_classes: int | None = None
    extra_stats: dict[str, float | int] = field(default_factory=dict)
    raw_values: dict[str, str] = field(default_factory=dict)
    precision_hints: dict[str, str] = field(default_factory=dict)


@dataclass
class CanonicalStats:
    num_graphs: int | None = None
    avg_nodes: float | None = None
    avg_edges: float | None = None
    num_classes: int | None = None
    extra_stats: dict[str, float | int] = field(default_factory=dict)


@dataclass
class MatchResult:
    status: str  # matched | mismatch | pending
    mismatch_fields: list[str] = field(default_factory=list)
    match_details: dict[str, str] = field(default_factory=dict)


def _coerce_int(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return int(round(float(value)))
    except (TypeError, ValueError):
        return None


def _coerce_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def observation_from_dict(data: dict[str, Any]) -> StatsObservation:
    return StatsObservation(
        num_graphs=_coerce_int(data.get("num_graphs")),
        avg_nodes=_coerce_float(data.get("avg_nodes")),
        avg_edges=_coerce_float(data.get("avg_edges")),
        num_classes=_coerce_int(data.get("num_classes")),
        extra_stats=parse_extra_stats(data.get("extra_stats")),
        raw_values={str(k): str(v) for k, v in (data.get("raw_values") or {}).items()},
        precision_hints={str(k): str(v) for k, v in (data.get("precision_hints") or {}).items()},
    )


def canonical_from_dataset(ds: Any, variant: Any | None = None) -> CanonicalStats:
    source = variant or ds
    extra_raw = getattr(source, "extra_stats", None) or getattr(ds, "extra_stats", None)
    extra: dict[str, float | int] = {}
    if extra_raw:
        try:
            extra = parse_extra_stats(json.loads(extra_raw))
        except (json.JSONDecodeError, TypeError):
            extra = {}
    return CanonicalStats(
        num_graphs=getattr(source, "num_graphs", None) or getattr(ds, "num_graphs", None),
        avg_nodes=getattr(source, "avg_nodes", None) or getattr(ds, "avg_nodes", None),
        avg_edges=getattr(source, "avg_edges", None) or getattr(ds, "avg_edges", None),
        num_classes=getattr(ds, "num_classes", None),
        extra_stats=extra,
    )


def classify_match(observation: StatsObservation, canonical: CanonicalStats) -> MatchResult:
    mismatch_fields: list[str] = []
    match_details: dict[str, str] = {}
    comparable = 0

    for field_name in _CORE_FIELDS:
        paper_val = getattr(observation, field_name)
        canon_val = getattr(canonical, field_name)
        if paper_val is None or canon_val is None:
            if paper_val is not None and canon_val is None:
                match_details[field_name] = "paper_only"
            continue

        comparable += 1
        compatible, tier = values_compatible(
            paper_val,
            canon_val,
            raw_value=observation.raw_values.get(field_name),
            precision_hint=observation.precision_hints.get(field_name),
            is_integer_field=field_name in _INTEGER_FIELDS,
        )
        if compatible:
            raw = observation.raw_values.get(field_name)
            if raw:
                match_details[field_name] = f"{raw} ↔ {canon_val} via {tier}"
            else:
                match_details[field_name] = f"{paper_val} ↔ {canon_val} via {tier}"
        else:
            mismatch_fields.append(field_name)
            raw = observation.raw_values.get(field_name, str(paper_val))
            match_details[field_name] = f"{raw} ↔ {canon_val} ({tier})"

    if comparable == 0:
        return MatchResult(status="pending", match_details=match_details)
    if mismatch_fields:
        return MatchResult(
            status="mismatch",
            mismatch_fields=mismatch_fields,
            match_details=match_details,
        )
    return MatchResult(status="matched", match_details=match_details)


def merge_stats(canonical: CanonicalStats, observation: StatsObservation) -> CanonicalStats:
    """Fill gaps + extend extra_stats; never overwrite existing canonical values."""
    merged = CanonicalStats(
        num_graphs=canonical.num_graphs,
        avg_nodes=canonical.avg_nodes,
        avg_edges=canonical.avg_edges,
        num_classes=canonical.num_classes,
        extra_stats=dict(canonical.extra_stats),
    )
    for field_name in _CORE_FIELDS:
        if getattr(merged, field_name) is None:
            setattr(merged, field_name, getattr(observation, field_name))
    for key, value in observation.extra_stats.items():
        if key not in merged.extra_stats:
            merged.extra_stats[key] = value
    return merged


def apply_canonical_to_orm(ds: Any, variant: Any | None, merged: CanonicalStats) -> None:
    target = variant or ds
    if merged.num_graphs is not None and getattr(target, "num_graphs", None) is None:
        target.num_graphs = merged.num_graphs
    if merged.avg_nodes is not None and getattr(target, "avg_nodes", None) is None:
        target.avg_nodes = merged.avg_nodes
    if merged.avg_edges is not None and getattr(target, "avg_edges", None) is None:
        target.avg_edges = merged.avg_edges
    if merged.num_classes is not None and getattr(ds, "num_classes", None) is None:
        ds.num_classes = merged.num_classes

    existing_extra: dict[str, Any] = {}
    raw_extra = getattr(target, "extra_stats", None)
    if raw_extra:
        try:
            existing_extra = json.loads(raw_extra)
        except (json.JSONDecodeError, TypeError):
            existing_extra = {}
    for key, value in merged.extra_stats.items():
        if key not in existing_extra:
            existing_extra[key] = value
    if existing_extra:
        target.extra_stats = json.dumps(existing_extra, sort_keys=True)
