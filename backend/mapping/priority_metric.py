from backend.mapping.decisions import metric_key
from backend.mapping.priority import priority_error


def priority_with_metric_target(row, verdict, fact):
    error = priority_error(row, verdict, fact)
    index = verdict.selected_candidate_index
    if not error or index is None:
        return error
    chosen = verdict.corrected_fact.candidates[index]
    for original in fact.candidates:
        if (
            original.main_experiment
            and original.eligibility == "benchmark"
            and chosen.main_experiment
            and chosen.table_id == original.table_id
            and chosen.cell_evidence == original.cell_evidence
            and chosen.dataset == original.dataset
            and chosen.method == original.method
            and metric_key(chosen.metric) == metric_key(row["metric"])
            and metric_key(original.metric) != metric_key(row["metric"])
        ):
            # Cell grounding/header semantics must still be verified by the caller.
            # Only the requested quantity changes, not method/dataset/configuration.
            return None
    return error
