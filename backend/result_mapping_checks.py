"""Deterministic bookkeeping checks independent of the model and database."""

import math
import re


def equivalent_number(old: float | None, new: float | None) -> bool:
    if old is None or new is None:
        return old is new
    return (
        math.isfinite(old)
        and math.isfinite(new)
        and math.isclose(old, new, abs_tol=1e-9, rel_tol=0)
    )


def same_dataset(stored: str, source: str) -> bool:
    """The stored ZINC benchmark means the 12K subset, never ZINC-Full."""

    def key(value):
        return re.sub(r"[^a-z0-9]", "", value.casefold())

    left, right = key(stored), key(source)
    zinc_subset = {"zinc", "zinc12k", "zincsubset", "zincsubset12k"}
    return left == right or left in zinc_subset and right in zinc_subset


def sole_verified_selection(verdict):
    """No semantic choice is needed when exactly one candidate was verified."""
    if verdict.selected_candidate_index is not None or len(verdict.verified_candidate_indices) != 1:
        return verdict
    index = verdict.verified_candidate_indices[0]
    if not 0 <= index < len(verdict.corrected_fact.candidates):
        return verdict
    return verdict.model_copy(update={"selected_candidate_index": index}, deep=True)
