from backend.mapping.decisions import grounded_column
from backend.mapping.priority_metric import (
    priority_with_metric_target,
)


def priority_with_grounding(row, verdict, fact, source):
    error = priority_with_metric_target(row, verdict, fact)
    index = verdict.selected_candidate_index
    if not error or index is None:
        return error
    chosen = verdict.corrected_fact.candidates[index]
    mains = [c for c in fact.candidates if c.main_experiment and c.eligibility == "benchmark"]
    if not mains or any(grounded_column(c, source) for c in mains):
        return error
    if grounded_column(chosen, source) and any(
        chosen.main_experiment
        and chosen.table_id == c.table_id
        and chosen.cell_evidence == c.cell_evidence
        and chosen.method == c.method
        and chosen.dataset == c.dataset == row["dataset"]
        for c in mains
    ):
        # The verifier repaired an invalid physical-column anchor within the same row.
        return None
    return error
