from types import SimpleNamespace as NS

from experiments.table_provenance_experiment.iterate_mapping_assignment7 import (
    priority_error,
    repair_echo_errors,
)


def candidate(table, line, column, *, main=True):
    return NS(
        table_id=table,
        cell_evidence=(line, line),
        cell_column_index=column,
        main_experiment=main,
        eligibility="benchmark",
        dataset="PascalVOC-SP",
    )


def test_old_numeric_match_cannot_replace_unspecified_main_cell():
    row = {"result_id": 1, "variant": "Standard split", "dataset": "PascalVOC-SP"}
    fact = NS(candidates=[candidate(3, 513, 3)])
    verdict = NS(
        selected_candidate_index=0,
        corrected_fact=NS(candidates=[candidate(8, 883, 5, main=False)]),
    )
    assert priority_error(row, verdict, fact)


def test_same_main_cell_is_allowed():
    row = {"result_id": 1, "variant": "Standard split", "dataset": "PascalVOC-SP"}
    main = candidate(3, 513, 3)
    assert (
        priority_error(
            row,
            NS(selected_candidate_index=0, corrected_fact=NS(candidates=[main])),
            NS(candidates=[main]),
        )
        is None
    )


def test_explicit_variant_is_not_forced_to_default():
    row = {"result_id": 1, "variant": "SLIC 10 coo", "dataset": "PascalVOC-SP"}
    verdict = NS(
        selected_candidate_index=0, corrected_fact=NS(candidates=[candidate(8, 883, 5, main=False)])
    )
    assert priority_error(row, verdict, NS(candidates=[candidate(3, 513, 3)])) is None


def test_graph_vit_old_spelling_must_be_echoed_exactly():
    row = {
        "result_id": 2,
        "value": 0.035,
        "std": 0.005,
        "model": "Graph ViT",
        "variant": "Full",
        "metric": "MAE",
    }
    repair = NS(
        old_value=0.035, old_std=0.005, old_model="GraphViT", old_variant="Full", old_metric=None
    )
    verdict = NS(corrected_fact=NS(repair=repair))
    assert len(repair_echo_errors(row, verdict)) == 1
    repair.old_model = "Graph ViT"
    assert not repair_echo_errors(row, verdict)


def test_abstention_does_not_force_a_count_or_candidate():
    row = {"result_id": 1, "variant": "Full", "dataset": "PascalVOC-SP"}
    assert priority_error(row, NS(selected_candidate_index=None), NS(candidates=[])) is None
