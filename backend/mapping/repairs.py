from backend.mapping.decisions import (
    Repair,
    grounded_column,
    metric_key,
    normalized_scale,
)


def adapt_verified_repair(row, verdict, source):
    """Keep semantic decisions intact; derive numeric/metric fields from verified cells."""
    adapted = verdict.model_copy(deep=True)
    index = adapted.selected_candidate_index
    repair = adapted.corrected_fact.repair
    if (
        index is None
        or index not in adapted.verified_candidate_indices
        or (repair is not None and not adapted.repair_supported)
    ):
        return adapted
    candidate = adapted.corrected_fact.candidates[index]
    if not grounded_column(candidate, source):
        return adapted
    candidate = normalized_scale(candidate, source)
    adapted.corrected_fact.candidates[index] = candidate
    value = candidate.displayed_mean / candidate.divisor
    std = None if candidate.displayed_std is None else candidate.displayed_std / candidate.divisor
    if repair is None:
        changed = any(
            old != new and (old is None or new is None or abs(old - new) > 1e-9)
            for old, new in ((row["value"], value), (row["std"], std))
        ) or metric_key(row["metric"]) != metric_key(candidate.metric)
        if not changed:
            return adapted
        repair = Repair(
            old_value=row["value"],
            old_std=row["std"],
            old_model=row["model"],
            old_variant=row["variant"],
            old_metric=row["metric"],
            corrected_value=value,
            corrected_std=std,
            corrected_model=row["model"],
            corrected_variant=row["variant"],
            corrected_metric=candidate.metric,
            evidence=[candidate.cell_evidence, candidate.column_evidence],
            explanation="Deterministic numeric/metric bookkeeping from the independently verified literal cell. Model/variant, origin, protocol and count are not inferred by this adapter.",
        )
        adapted.corrected_fact.repair = repair
        adapted.repair_supported = True
    for field in ("value", "std", "model", "variant", "metric"):
        setattr(repair, f"old_{field}", row[field])
    repair.corrected_value = value
    repair.corrected_std = std
    repair.corrected_metric = candidate.metric
    # Model/variant changes remain semantic judgments: never generate aliases here.
    return adapted
