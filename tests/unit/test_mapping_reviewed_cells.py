from experiments.table_provenance_experiment.recheck_reviewed_cells import (
    fix_literal_column,
    source_repair,
)
from tests.unit.test_mapping_cell_identity import fixture


def test_unique_mean_std_cell_can_repair_only_the_column_index():
    _, verdict, source = fixture()
    candidate = verdict.corrected_fact.candidates[0].model_copy(update={"cell_column_index": 2})
    repaired = fix_literal_column(candidate, source)
    assert repaired.cell_column_index == 1
    assert repaired.cell_evidence == candidate.cell_evidence
    assert repaired.dataset == candidate.dataset


def test_ambiguous_cell_location_does_not_guess():
    _, verdict, source = fixture()
    candidate = verdict.corrected_fact.candidates[0].model_copy(update={"cell_column_index": 9})
    source = source.replace("90.0", "80.0").replace("0.3", "0.2")
    assert fix_literal_column(candidate, source).cell_column_index == 9


def test_source_repair_echoes_exact_old_fields_and_normalizes_both_numbers():
    row, verdict, _ = fixture()
    row.update(model="Graph ViT", metric="ROC-AUC")
    candidate = verdict.corrected_fact.candidates[0]
    repair = source_repair(row, candidate)
    assert repair.old_model == repair.corrected_model == "Graph ViT"
    assert repair.old_metric == "ROC-AUC"
    assert repair.corrected_metric == "Accuracy"
    assert repair.corrected_value == 0.8
    assert repair.corrected_std == 0.002
    assert repair.old_variant == repair.corrected_variant == row["variant"]
