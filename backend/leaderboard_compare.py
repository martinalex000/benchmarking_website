"""Shared leaderboard value comparison and proposed-model selection."""

from __future__ import annotations

from typing import Any

from backend.models import Result


def has_paper_value_difference(
    paper_value: float | None,
    true_value: float | None,
) -> bool:
    if paper_value is None or true_value is None:
        return False
    return abs(paper_value - true_value) > 1e-12


def gap_magnitude(
    paper_value: float | None,
    reference_value: float | None,
) -> float | None:
    if not has_paper_value_difference(paper_value, reference_value):
        return None
    return abs(float(paper_value) - float(reference_value))


def is_value_worse_than(
    value: float,
    reference: float,
    higher_is_better: bool,
    value_std: float | None = None,
    reference_std: float | None = None,
) -> bool:
    """True when *value* is strictly worse than *reference* (outside combined std)."""
    worse = (value < reference) if higher_is_better else (value > reference)
    if not worse:
        return False
    delta = abs(value - reference)
    combined_std = float(value_std or 0.0) + float(reference_std or 0.0)
    if combined_std and delta <= combined_std:
        return False
    return delta > 1e-12


def is_value_better_than(
    value: float,
    reference: float,
    higher_is_better: bool,
    value_std: float | None = None,
    reference_std: float | None = None,
) -> bool:
    """True when *value* is strictly better than *reference* (outside combined std)."""
    return is_value_worse_than(reference, value, higher_is_better, reference_std, value_std)


def is_value_directionally_better(
    value: float,
    reference: float,
    higher_is_better: bool,
) -> bool:
    return (value > reference) if higher_is_better else (value < reference)


def primary_proposed_from_results(
    results: list[Result],
    proposed_models: list[str],
) -> str | None:
    """Pick the main proposed model from DB rows (no extraction YAML)."""
    if not proposed_models:
        return None
    if len(proposed_models) == 1:
        return proposed_models[0]

    counts: dict[str, int] = {}
    for result in results:
        if not result.model or not result.model.canonical_name:
            continue
        cname = result.model.canonical_name
        if cname not in proposed_models:
            continue
        dv = result.dataset_variant
        if not dv or not dv.dataset:
            continue
        primary_metric = dv.dataset.primary_metric or result.metric_name
        if result.metric_name != primary_metric:
            continue
        counts[cname] = counts.get(cname, 0) + 1
    if counts:
        return max(counts, key=counts.get)
    return proposed_models[0]


def global_best_entry_at_publication(
    truth_map: dict[str, dict[str, Any]],
    *,
    higher_is_better: bool,
) -> dict[str, Any] | None:
    """Directionally best entry from a preloaded at-publication truth map."""
    best: dict[str, Any] | None = None
    for entry in truth_map.values():
        value = entry.get("value")
        if value is None:
            continue
        if best is None or is_value_directionally_better(
            float(value), float(best["value"]), higher_is_better
        ):
            best = entry
    return best
