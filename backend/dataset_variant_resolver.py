"""Shared helpers for resolving dataset names to canonical variants."""

from __future__ import annotations

from typing import Any

from thefuzz import process as fuzz_process

from backend.models import DatasetVariant


def build_dataset_variant_lookup(session: Any) -> dict[str, DatasetVariant]:
    """Build a case-insensitive lookup for variant and dataset display names."""
    lookup: dict[str, DatasetVariant] = {}
    for variant in session.query(DatasetVariant).all():
        lookup.setdefault(variant.name.lower(), variant)
        if variant.dataset:
            lookup.setdefault(variant.dataset.name.lower(), variant)
    return lookup


def resolve_dataset_variant_quiet(
    dataset_name: str,
    dataset_lookup: dict[str, DatasetVariant],
) -> DatasetVariant | None:
    """Resolve a dataset name by exact or fuzzy match without logging."""
    key = dataset_name.strip().lower()
    if not key:
        return None
    if key in dataset_lookup:
        return dataset_lookup[key]
    if dataset_lookup:
        min_score = 85 if len(key) <= 6 else 75
        best_match, score = fuzz_process.extractOne(key, list(dataset_lookup.keys()))
        if score >= min_score:
            return dataset_lookup[best_match]
    return None
