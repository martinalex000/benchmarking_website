"""Source intervals and alternate backbone cells must not become std repairs."""

import copy

from experiments.table_provenance_experiment.mapping_presentation_safety import presentation_safety


def fixture():
    source = "\n".join(
        [
            r"\begin{table}",
            r"Method & Cora \\",
            r"Own & 80.0 $\pm$ 0.2 \\",
            r"Own & 90.0 $\pm$ 0.3 \\",
            r"\end{table}",
        ]
    )
    row = {
        "result_id": 1,
        "model": "Own",
        "dataset": "Cora",
        "value": 0.9,
        "std": 0.003,
        "action": "propose_count",
        "proposed_num_runs": 5,
        "correction": {"old": {"value": 0.9}, "corrected": {"value": 0.8}},
        "selected_candidate": {
            "table_id": 1,
            "cell_column_index": 1,
            "cell_evidence": {"start_line": 3, "end_line": 3},
            "displayed_std": 0.2,
        },
    }
    return row, source


def test_alternate_source_configuration_blocks_score_replacement():
    row, source = fixture()
    before = copy.deepcopy(row)
    result = presentation_safety(row, source)
    assert result["action"] == "configuration_scope_unresolved"
    assert result["competing_old_value_lines"] == [4]
    assert result["correction"] is None
    assert row == before


def test_actual_wrong_number_without_an_alternative_cell_can_be_repaired():
    row, source = fixture()
    row["value"] = 0.99
    assert presentation_safety(row, source)["action"] == "propose_count"


def test_confidence_interval_is_not_stored_as_a_standard_deviation():
    row, source = fixture()
    source = source.replace(
        r"Method & Cora", r"\caption{95 percent confidence intervals} Method & Cora"
    )
    result = presentation_safety(row, source)
    assert result["action"] == "special_uncertainty"
    assert result["proposed_num_runs"] is None
    assert result["correction"] is None


def test_other_backbone_column_cannot_replace_a_matching_old_dataset_cell():
    row, source = fixture()
    source = source.replace(r"Own & 80.0 $\pm$ 0.2", r"Cora & 80.0 $\pm$ 0.2 & 90.0 $\pm$ 0.3")
    assert presentation_safety(row, source)["action"] == "configuration_scope_unresolved"
