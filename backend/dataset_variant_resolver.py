"""Shared helpers for resolving dataset names to canonical variants."""

from __future__ import annotations

from typing import Any

from thefuzz import fuzz as fuzz_lib
from thefuzz import process as fuzz_process

from backend.model_name_resolution import ogb_dataset_families_compatible
from backend.models import DatasetVariant
from backend.results_parser import normalize_dataset_alias


def build_dataset_variant_lookup(session: Any) -> dict[str, DatasetVariant]:
    """Build a case-insensitive lookup for variant and dataset display names."""
    lookup: dict[str, DatasetVariant] = {}
    for variant in session.query(DatasetVariant).all():
        lookup.setdefault(variant.name.lower(), variant)
        if variant.dataset:
            dataset_key = variant.dataset.name.lower()
            existing = lookup.get(dataset_key)
            if existing is None or (
                getattr(variant, "is_standard", False)
                and not getattr(existing, "is_standard", False)
            ):
                lookup[dataset_key] = variant
    return lookup


def resolve_dataset_variant_quiet(
    dataset_name: str,
    dataset_lookup: dict[str, DatasetVariant],
) -> DatasetVariant | None:
    """Resolve a dataset name by exact or fuzzy match without logging."""
    dataset_name = normalize_dataset_alias(dataset_name)
    key = dataset_name.strip().lower()
    if not key:
        return None
    if key in dataset_lookup:
        return dataset_lookup[key]
    if dataset_lookup:
        min_score = 85 if len(key) <= 6 else 75
        best_match, score = fuzz_process.extractOne(
            key,
            list(dataset_lookup.keys()),
            scorer=fuzz_lib.token_sort_ratio,
        )
        if score >= min_score and ogb_dataset_families_compatible(key, best_match):
            return dataset_lookup[best_match]
    return None
