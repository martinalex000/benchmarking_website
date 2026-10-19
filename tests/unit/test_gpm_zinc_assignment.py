import pytest

from experiments.table_provenance_experiment.check_gpm_zinc_assignment import expected_zinc


def source_with_row(method, zinc, full):
    lines = [""] * 875
    lines[853] = "Method & IMDB & COLLAB & R5K & R12K & ZINC & ZINC-Full"
    lines[854] = "Graphs & 1000 & 5000 & 4999 & 11929 & 12,000 & 249,456"
    lines[857] = f"{method} \\small{{\\citep{{example}}}} & - & - & - & - & {zinc} & {full}"
    return "\n".join(lines)


def test_uses_intended_zinc_not_full_or_old_numbers():
    row = {"result_id": 1, "model": "GIN", "value": 0.088, "std": 0.002}
    expected = expected_zinc(row, source_with_row("GIN", "0.526±0.051", "0.088±0.002"))
    assert expected["value"] == 0.526
    assert expected["std"] == 0.051
    assert expected["cell_column_index"] == 5


def test_method_normalization_handles_graph_vit():
    row = {"result_id": 2, "model": "Graph ViT"}
    expected = expected_zinc(row, source_with_row("GraphViT", "0.073±0.001", "0.035±0.005"))
    assert expected["value"] == 0.073


def test_changed_layout_requires_manual_review():
    row = {"result_id": 3, "model": "GIN"}
    source = source_with_row("GIN", "0.526±0.051", "0.088±0.002").replace("12,000", "changed")
    with pytest.raises(ValueError, match="layout changed"):
        expected_zinc(row, source)
