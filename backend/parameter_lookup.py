"""Parameter-count lookup helpers shared by extraction and backfill code."""

from __future__ import annotations

import contextlib
from typing import Any

from backend.model_metadata import normalize_architecture_type


def build_metadata_lookups(
    extraction: dict[str, Any],
    model_sizes: list[Any] | None = None,
) -> tuple[dict[str, float | None], dict[str, str | None]]:
    """Build global parameter and architecture lookups keyed by model name."""
    sizes_lookup: dict[str, float | None] = {}
    type_lookup: dict[str, str | None] = {}

    def _add(name: str | None, params: Any, model_type: Any) -> None:
        if not name:
            return
        key = name.strip().lower()
        sizes_lookup[key] = None
        if params is not None:
            with contextlib.suppress(TypeError, ValueError):
                sizes_lookup[key] = float(params)
        normalized_type = normalize_architecture_type(
            str(model_type) if model_type is not None else None
        )
        if normalized_type is not None:
            type_lookup[key] = normalized_type

    proposed = extraction.get("proposed_model") or {}
    if isinstance(proposed, dict):
        _add(proposed.get("name"), proposed.get("params_millions"), proposed.get("model_type"))

    for baseline in extraction.get("baseline_models") or []:
        if isinstance(baseline, dict):
            _add(baseline.get("name"), baseline.get("params_millions"), baseline.get("model_type"))

    for item in model_sizes or []:
        if not isinstance(item, dict) or item.get("dataset"):
            continue
        name = item.get("matched_result_name") or item.get("model_name")
        _add(name, item.get("params_millions"), None)

    return sizes_lookup, type_lookup


def build_dataset_param_lookup(
    model_sizes: list[Any] | None = None,
) -> dict[tuple[str, str], float]:
    """Build dataset-specific parameter counts without collapsing model variants."""
    lookup: dict[tuple[str, str], float] = {}
    for item in model_sizes or []:
        if not isinstance(item, dict):
            continue
        dataset = str(item.get("dataset") or "").strip().casefold()
        name = str(item.get("matched_result_name") or item.get("model_name") or "")
        if not dataset or not name:
            continue
        params = item.get("params_millions")
        if params is None:
            continue
        try:
            lookup[(dataset, name.strip().casefold())] = float(params)
        except (TypeError, ValueError):
            continue
    return lookup
