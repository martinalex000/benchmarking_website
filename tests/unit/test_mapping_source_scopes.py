from backend.mapping.source_scopes import (
    competing_old_value_lines,
    fractional_percentage_column_lines,
    uncertainty_context,
    uncertainty_review_hints,
)
from backend.repetition_metadata import table_inventory


def test_genuine_low_percentage_conversion_is_not_another_configuration():
    source = "\n".join(
        [
            r"\begin{table}",
            r"\caption{Accuracy in percent}",
            r"Method & Cora \\",
            r"Own & 0.9 $\pm$ 0.03 \\",
            r"Baseline & 80.0 $\pm$ 0.2 \\",
            r"\end{table}",
        ]
    )
    row = {
        "model": "Own",
        "dataset": "Cora",
        "value": 0.9,
        "std": 0.03,
        "selected_candidate": {"cell_column_index": 1, "cell_evidence": {"start_line": 4}},
    }
    assert competing_old_value_lines(row, source, table_inventory(source)[0]) == []


def test_alternate_configuration_still_blocks_replacement():
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
        "model": "Own",
        "dataset": "Cora",
        "value": 0.9,
        "std": 0.003,
        "selected_candidate": {"cell_column_index": 1, "cell_evidence": {"start_line": 3}},
    }
    assert competing_old_value_lines(row, source, table_inventory(source)[0]) == [4]


def test_dataset_row_other_backbone_still_blocks_default_backbone_repair():
    source = "\n".join(
        [
            r"\begin{table}",
            r"Dataset & GCN ProtGNN & GIN ProtGNN+ \\",
            r"MUTAG & 76.7 $\pm$ 6.4 & 91.7 $\pm$ 2.9 \\",
            r"\end{table}",
        ]
    )
    row = {
        "model": "ProtGNN",
        "dataset": "MUTAG",
        "value": 0.917,
        "std": 0.029,
        "selected_candidate": {"cell_column_index": 1, "cell_evidence": {"start_line": 3}},
    }
    assert competing_old_value_lines(row, source, table_inventory(source)[0]) == [3]


def test_previous_tables_confidence_intervals_do_not_leak_into_std_table():
    source = "\n".join(
        [
            r"\begin{table}",
            r"\caption{95 percent confidence intervals}",
            r"Old & 1.0 \\",
            r"\end{table}",
            "Next we report standard deviations over five seeds.",
            r"\begin{table}",
            r"\caption{Mean and standard deviation}",
            r"Own & 80.0 $\pm$ 0.2 \\",
            r"\end{table}",
        ]
    )
    context, first = uncertainty_context(source, table_inventory(source)[1])
    assert first == 5
    assert "confidence intervals" not in context
    assert "standard deviations" in context


def test_current_tables_interval_statement_is_retained():
    source = "\n".join(
        [
            "We report 95 percent confidence intervals.",
            r"\begin{table}",
            r"Own & 80.0 $\pm$ 0.2 \\",
            r"\end{table}",
        ]
    )
    context, first = uncertainty_context(source, table_inventory(source)[0])
    assert first == 1
    assert "confidence intervals" in context


def test_fractional_percentage_column_requests_review_without_choosing_units():
    source = "\n".join(
        [
            r"\begin{table}",
            r"\caption{Classification accuracy in percent}",
            r"Method & Accuracy & Runtime \\",
            r"A & 0.844 $\pm$ 0.141 & 30 $\pm$ 2 \\",
            r"B & 0.747 $\pm$ 0.044 & 40 $\pm$ 2 \\",
            r"C & 0.732 $\pm$ 0.087 & 50 $\pm$ 2 \\",
            r"\end{table}",
        ]
    )
    table = table_inventory(source)[0]
    assert fractional_percentage_column_lines(source, table, 1) == [4, 5, 6]
    assert fractional_percentage_column_lines(source, table, 2) == []


def test_genuine_low_percentage_cell_does_not_overrule_percent_units():
    source = "\n".join(
        [
            r"\begin{table}",
            r"\caption{Accuracy in percent}",
            r"A & 0.9 $\pm$ 0.03 \\",
            r"B & 80 $\pm$ 2 \\",
            r"C & 90 $\pm$ 1 \\",
            r"\end{table}",
        ]
    )
    assert fractional_percentage_column_lines(source, table_inventory(source)[0], 1) == []


def test_global_standard_error_setup_survives_subsection_via_protocol_evidence():
    source = "\n".join(
        [
            "We report the mean and standard error of the mean over 5 to 10 runs.",
            r"\subsection{Long-range tasks}",
            r"\begin{table}",
            r"Own & 72.16 $\pm$ 0.41 \\",
            r"\end{table}",
        ]
    )
    table = table_inventory(source)[0]
    assert uncertainty_review_hints(source, table, []) == []
    hints = uncertainty_review_hints(source, table, [{"start_line": 1, "end_line": 1}])
    assert hints == [
        {"kind": "standard_error", "start_line": 1, "end_line": 1, "requires_scope_review": True}
    ]


def test_non_std_hints_are_scoped_and_do_not_read_commented_claims():
    source = "\n".join(
        [
            r"\begin{table}",
            r"\caption{Confidence intervals}",
            r"Old & 10 \\",
            r"\end{table}",
            "% We report standard errors.",
            "We report mean and variance.",
            r"\begin{table}",
            r"Own & 80 $\pm$ 2 \\",
            r"\end{table}",
        ]
    )
    hints = uncertainty_review_hints(source, table_inventory(source)[1], [])
    assert [h["kind"] for h in hints] == ["variance"]
    assert hints[0]["start_line"] == 6
