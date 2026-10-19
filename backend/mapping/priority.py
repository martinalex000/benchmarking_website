from backend.mapping.source import name_key


def default_configuration(row: dict) -> bool:
    # Full describes the full model, not an instruction to switch to ZINC-Full.
    return name_key(row["variant"]) in {"", "standard", "standardsplit", "default", "full"}


def priority_error(row: dict, verdict, fact) -> str | None:
    index = verdict.selected_candidate_index
    if not default_configuration(row) or index is None:
        return None
    mains = [
        c
        for c in fact.candidates
        if c.main_experiment
        and c.eligibility == "benchmark"
        and name_key(c.dataset) == name_key(row["dataset"])
    ]
    if not mains:
        return None
    chosen = verdict.corrected_fact.candidates[index]
    if any(
        chosen.table_id == c.table_id
        and chosen.cell_column_index == c.cell_column_index
        and chosen.cell_evidence == c.cell_evidence
        for c in mains
    ):
        return None
    return (
        f"Row {row['result_id']}: selected cell replaces the source-first main benchmark "
        "with another configuration. Stored numbers, table_ref, protocol_note and setting "
        "notes are FALLIBLE, not independent configuration authority. For this unspecified "
        "target retain a grounded source-first main cell and compute old-to-source repair. "
        "If that main cell is unsupported, abstain rather than silently substitute an "
        "appendix configuration."
    )


def repair_echo_errors(row: dict, verdict) -> list[str]:
    repair = verdict.corrected_fact.repair
    if repair is None:
        return []
    errors = []
    for field in ("value", "std", "model", "variant"):
        if getattr(repair, f"old_{field}") != row[field]:
            errors.append(
                f"Row {row['result_id']}: old_{field} must echo EXACT stored {field} "
                f"{row[field]!r}, including spelling/spaces; do not normalize old fields. "
                "Normalization or correction belongs only in corrected_* fields."
            )
    if repair.old_metric is not None and repair.old_metric != row["metric"]:
        errors.append(f"Row {row['result_id']}: old_metric must echo exact stored metric.")
    return errors
