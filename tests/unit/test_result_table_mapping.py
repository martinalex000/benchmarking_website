"""Safety gates for the read-only mixed-protocol mapping experiment."""

import pytest

from experiments.table_provenance_experiment.verify_stored_mapping import (
    Mapping,
    Span,
    Verdict,
    exact_coverage,
    proposal,
)


def example():
    source = "\\begin{table}\nMethod & Cora & CiteSeer \\\\\nOwn & 80.0 & 70.0 \\\\\n\\end{table}"
    row = {"result_id": 1, "value": 0.8}
    mapping = Mapping(
        result_id=1,
        decision="match",
        table_id=1,
        displayed_mean=80.0,
        divisor=100,
        table_method="Own",
        table_dataset="Cora",
        table_metric="Accuracy",
        metadata_method="Own",
        row_evidence=Span(start_line=3, end_line=3),
        column_evidence=Span(start_line=2, end_line=2),
        cell_evidence=Span(start_line=3, end_line=3),
        explanation="Cora column.",
    )
    verdict = Verdict(
        result_id=1,
        decision_supported=True,
        cell_supported=True,
        row_identity_supported=True,
        numeric_supported=True,
        metadata_link_supported=True,
        explanation="Verified.",
    )
    metadata = {
        "validated": {
            "accepted": [{"table_id": 1, "name": "Own", "repetitions": 10}],
            "table_outcomes": [{"table_id": 1, "outcome": "count"}],
        }
    }
    return source, row, mapping, verdict, metadata


def test_verified_cell_proposes_without_mutating_input():
    source, row, mapping, verdict, metadata = example()
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["proposed_num_runs"] == 10
    assert "proposed_num_runs" not in row


@pytest.mark.parametrize("field", ["cell_supported", "row_identity_supported", "numeric_supported"])
def test_disagreed_cell_never_gets_count(field):
    source, row, mapping, verdict, metadata = example()
    setattr(verdict, field, False)
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["proposed_num_runs"] is None


def test_wrong_dataset_column_is_rejected_even_when_number_present():
    source, row, mapping, verdict, metadata = example()
    mapping.table_dataset = "CiteSeer"
    verdict.row_identity_supported = False
    assert proposal(row, mapping, verdict, metadata, source)["action"] == "propose_quarantine"


def test_unknown_method_link_cannot_inherit_proposed_count():
    source, row, mapping, verdict, metadata = example()
    verdict.metadata_link_supported = False
    assert proposal(row, mapping, verdict, metadata, source)["proposed_num_runs"] is None


def test_span_outside_table_and_wrong_mean_are_withheld():
    source, row, mapping, verdict, metadata = example()
    mapping.cell_evidence = Span(start_line=1, end_line=100)
    assert proposal(row, mapping, verdict, metadata, source)["proposed_num_runs"] is None
    mapping.cell_evidence = Span(start_line=3, end_line=3)
    mapping.displayed_mean = 81
    assert proposal(row, mapping, verdict, metadata, source)["proposed_num_runs"] is None


def test_special_and_excluded_tables_never_get_counts():
    source, row, mapping, verdict, metadata = example()
    for outcome in ("special", "excluded", "unknown"):
        metadata["validated"]["table_outcomes"][0]["outcome"] = outcome
        assert proposal(row, mapping, verdict, metadata, source)["proposed_num_runs"] is None


def test_missing_or_duplicate_outputs_fail_coverage():
    _, row, mapping, _, _ = example()
    exact_coverage([mapping], [row])
    with pytest.raises(ValueError):
        exact_coverage([], [row])
    with pytest.raises(ValueError):
        exact_coverage([mapping, mapping], [row])


def test_null_method_link_is_unknown_even_if_judge_says_true():
    source, row, mapping, verdict, metadata = example()
    mapping.metadata_method = None
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["action"] == "matched_origin_or_count_unknown"
    assert result["proposed_num_runs"] is None


def test_competing_benchmark_and_ablation_locations_withhold_exclusion():
    source, row, mapping, verdict, metadata = example()
    row.update(model="Own", dataset="Cora")
    source += "\n" + source
    metadata["validated"]["table_outcomes"][0]["outcome"] = "excluded"
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["action"] == "ambiguous_table_candidates"
    assert result["presence_candidate_ids"] == [1, 2]
    assert result["proposed_num_runs"] is None


def test_old_style_tex_bold_touching_number_remains_grounded():
    source, row, mapping, verdict, metadata = example()
    source = source.replace("80.0", r"{\bf80.0}")
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["proposed_num_runs"] == 10


def test_verified_stored_protocol_conflict_proposes_quarantine():
    source, row, mapping, verdict, metadata = example()
    verdict.row_identity_supported = False
    verdict.explanation = "Stored split disagrees with the source protocol."
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["action"] == "propose_quarantine"
    assert result["quarantine_kind"] == "stored_protocol_or_identity_unfitting"
    assert result["proposed_num_runs"] is None


def test_verified_excluded_table_proposes_quarantine_not_deletion():
    source, row, mapping, verdict, metadata = example()
    metadata["validated"]["table_outcomes"][0].update(outcome="excluded", reason="Ablation")
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["action"] == "propose_quarantine"
    assert result["quarantine_reason"] == "Ablation"
    assert result["quarantine_kind"] == "excluded_source_table"


def test_ungrounded_mismatch_does_not_propose_quarantine():
    source, row, mapping, verdict, metadata = example()
    mapping.decision = "mismatch"
    mapping.cell_evidence = Span(start_line=100, end_line=100)
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["action"] == "unresolved_mismatch"


def test_supported_mismatch_can_quarantine_without_a_positive_match_verdict():
    source, row, mapping, verdict, metadata = example()
    mapping.decision = "mismatch"
    verdict.cell_supported = False
    verdict.numeric_supported = False
    verdict.row_identity_supported = False
    verdict.explanation = "Value exists but belongs to a different method."
    result = proposal(row, mapping, verdict, metadata, source)
    assert result["action"] == "propose_quarantine"
    assert result["quarantine_kind"] == "stored_identity_mismatch"
