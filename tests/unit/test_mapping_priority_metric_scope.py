from types import SimpleNamespace as NS

from experiments.table_provenance_experiment.check_priority_metric_scope import (
    priority_with_metric_target,
)


def candidate(metric, column, table=5):
    return NS(
        main_experiment=True,
        eligibility="benchmark",
        table_id=table,
        cell_evidence=(591, 591),
        cell_column_index=column,
        dataset="PCQM-Contact",
        method="GINE",
        metric=metric,
        configuration_axes={"layers": "5"},
    )


def test_requested_mrr_may_correct_first_column_hits_fact():
    row = {"result_id": 1, "variant": "Standard split", "dataset": "PCQM-Contact", "metric": "MRR"}
    fact = NS(candidates=[candidate("Hits@1", 2)])
    verdict = NS(selected_candidate_index=0, corrected_fact=NS(candidates=[candidate("MRR", 5)]))
    assert priority_with_metric_target(row, verdict, fact) is None


def test_metric_target_does_not_authorize_an_appendix_configuration():
    row = {"result_id": 1, "variant": "Standard split", "dataset": "PCQM-Contact", "metric": "MRR"}
    fact = NS(candidates=[candidate("Hits@1", 2)])
    verdict = NS(
        selected_candidate_index=0, corrected_fact=NS(candidates=[candidate("MRR", 5, table=9)])
    )
    assert priority_with_metric_target(row, verdict, fact)
