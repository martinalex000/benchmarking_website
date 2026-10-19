from types import SimpleNamespace as NS

from experiments.table_provenance_experiment.check_priority_grounding import priority_with_grounding
from experiments.table_provenance_experiment.verify_stored_mapping import Span


def candidate(column, mean=62.7, table=1):
    return NS(
        table_id=table,
        cell_evidence=Span(start_line=1, end_line=1),
        cell_column_index=column,
        main_experiment=True,
        eligibility="benchmark",
        method="GCN",
        dataset="Deezer",
        metric="Accuracy",
        displayed_mean=mean,
        displayed_std=0.7,
        configuration_axes={"split": "50/25/25"},
        identity_evidence=[Span(start_line=1, end_line=1)],
    )


def check(original, chosen):
    row = {"result_id": 1, "variant": "Standard split", "dataset": "Deezer", "metric": "ROC-AUC"}
    verdict = NS(selected_candidate_index=0, corrected_fact=NS(candidates=[chosen]))
    source = "GCN & 63.10±0.70 & 62.70±0.70"
    return priority_with_grounding(row, verdict, NS(candidates=[original]), source)


def test_wrong_initial_numeric_column_may_be_repaired_in_same_source_row():
    assert check(candidate(1), candidate(2)) is None


def test_grounded_initial_column_does_not_grant_free_configuration_changes():
    assert check(candidate(1, mean=63.1), candidate(2))


def test_anchor_repair_cannot_move_to_another_table():
    assert check(candidate(1), candidate(2, table=8))
