import re

from backend.mapping.decisions import metric_key


def bounded_metric(metric: str) -> bool:
    key = metric_key(metric)
    return key in {"accuracy", "f1", "f1macro", "f1micro", "auc", "ap"} or key.startswith("hits")


def configuration_axis_repair_errors(
    row: dict, candidate: dict, correction: dict | None
) -> list[str]:
    """Catch identity/repair conflicts between model labels and source config axes."""
    axes = candidate.get("configuration_axes") or {}

    def words(text: str | None) -> str:
        return re.sub(r"[^a-z0-9]+", " ", (text or "").casefold()).strip()

    def contains(identity: str | None, value: str) -> bool:
        normalized = words(identity)
        axis = words(value)
        return bool(axis and re.search(rf"(?<!\w){re.escape(axis)}(?!\w)", normalized))

    primary = [
        value
        for name, value in axes.items()
        if name.casefold() in {"model", "backbone", "architecture"} and value
    ]
    method = candidate.get("method")
    identity_errors = []
    for model_axis in primary:
        if contains(method, model_axis):
            continue
        # Pooling/sampling components can themselves name benchmark methods; optimizer
        # names are configuration values, not standalone architectures in this schema.
        misread_axes = [
            f"{name}={value}"
            for name, value in axes.items()
            if name.casefold() == "optimizer" and value and contains(method, value)
        ]
        if misread_axes:
            identity_errors.append(
                f"Selected method {method!r} matches {', '.join(misread_axes)}, while the "
                f"source configuration identifies model/backbone {model_axis!r}. Correct "
                "the candidate method and stored model identity, retaining every other "
                "configuration axis in the variant."
            )

    if not correction:
        return identity_errors
    corrected = correction.get("corrected", {})
    old_identity = (row.get("model"), row.get("variant"))
    new_identity = (
        corrected.get("model", old_identity[0]),
        corrected.get("variant", old_identity[1]),
    )
    lost = [
        f"{axis}={value}"
        for axis, value in axes.items()
        if any(contains(identity, value) for identity in old_identity)
        and not any(contains(identity, value) for identity in new_identity)
    ]
    if lost:
        identity_errors.append(
            "The repair drops configuration axis value(s) already present in the stored "
            "identity: "
            + ", ".join(lost)
            + ". Preserve each distinguishing value in corrected model or variant, or abstain."
        )
    return identity_errors


def repair_feedback(row: dict, verdict) -> list[str]:
    index = verdict.selected_candidate_index
    if index is None:
        return []
    candidate = verdict.corrected_fact.candidates[index]
    errors = []
    candidate_data = candidate.model_dump() if hasattr(candidate, "model_dump") else vars(candidate)
    repair = verdict.corrected_fact.repair
    repair_data = repair.model_dump() if hasattr(repair, "model_dump") else None
    errors.extend(configuration_axis_repair_errors(row, candidate_data, repair_data))
    if (
        bounded_metric(candidate.metric)
        and candidate.displayed_mean > 1
        and candidate.divisor != 100
    ):
        errors.append(
            f"Row {row['result_id']}: bounded metric {candidate.metric} is printed on a "
            "0–100 scale. Set divisor=100, retaining the LITERAL printed mean/std; "
            "database corrected_value and corrected_std must divide BOTH by100 once. "
            "Never expand already fractional stored scores back to percentages."
        )
    repair = verdict.corrected_fact.repair
    metric_changed = metric_key(candidate.metric) != metric_key(row["metric"])
    expected = (
        candidate.displayed_mean / candidate.divisor,
        None if candidate.displayed_std is None else candidate.displayed_std / candidate.divisor,
    )
    numeric_changed = any(
        a != b and (a is None or b is None or abs(a - b) > 1e-9)
        for a, b in zip((row["value"], row["std"]), expected, strict=True)
    )
    if (metric_changed or numeric_changed) and repair is None:
        errors.append(
            f"Row {row['result_id']}: selected source cell differs from old fields; provide "
            "an explicit old-to-corrected repair, even when origin/count remains unknown."
        )
        return errors
    if repair is not None:
        if metric_changed and (
            repair.old_metric != row["metric"]
            or repair.corrected_metric is None
            or metric_key(repair.corrected_metric) != metric_key(candidate.metric)
        ):
            errors.append(
                f"Row {row['result_id']}: actual metric repair fields REQUIRED: "
                f"old_metric={row['metric']!r}, corrected_metric={candidate.metric!r}. "
                "An explanation alone does not repair a metric."
            )
        actual = (repair.corrected_value, repair.corrected_std)
        if any(
            a != b and (a is None or b is None or abs(a - b) > 1e-9)
            for a, b in zip(actual, expected, strict=True)
        ):
            errors.append(
                f"Row {row['result_id']}: corrected mean/std must equal selected literal "
                f"cell divided by divisor ({expected!r}); preserve exact old fields."
            )
    return errors
