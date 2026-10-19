"""v2 origin semantics and exact numerical/unit guard regressions."""

import pytest

from experiments.table_provenance_experiment.verify_stored_mapping_v2 import (
    Location,
    RowFact,
    RowVerdict,
    Span,
    VerifiedCorrection,
    printed_matches,
    propose,
)


def fixture():
    source = "\\begin{table}\nMethod & Cora \\\\\nOwn & 80.0 $\\pm$ 0.2 \\\\\n\\end{table}\nWe evaluate Own with 10 runs.\nThese values are copied from Smith."
    row = {"result_id": 1, "value": 0.8, "std": 0.002}
    location = Location(
        table_id=1,
        displayed_mean=80,
        displayed_std=0.2,
        divisor=100,
        method="Own",
        dataset="Cora",
        metric="Accuracy",
        configuration="Own",
        eligibility="benchmark",
        row_evidence=Span(start_line=3, end_line=3),
        column_evidence=Span(start_line=2, end_line=2),
        cell_evidence=Span(start_line=3, end_line=3),
    )
    fact = RowFact(
        result_id=1,
        decision="match",
        locations=[location],
        configuration="Own",
        origin="self_evaluated",
        origin_evidence=[Span(start_line=5, end_line=5)],
        execution_evidence=[Span(start_line=5, end_line=5)],
        count_evidence=[Span(start_line=5, end_line=5)],
        protocol_evidence=[Span(start_line=5, end_line=5)],
        eligibility="benchmark",
        protocol="repeated_training",
        repetitions=10,
        metadata_method="Own",
        explanation="Supported",
    )
    verdict = RowVerdict(
        result_id=1,
        verified_location_indices=[0],
        decision_supported=True,
        identity_supported=True,
        mean_supported=True,
        std_supported=True,
        origin_classification_supported=True,
        current_evaluation_supported=True,
        count_supported=True,
        unit_correct=True,
        evidence_supported=True,
        duplicates_compatible=True,
        eligibility="benchmark",
        explanation="Verified",
    )
    return row, fact, verdict, {"verification": {"methods": []}}, source


def test_explicit_self_evaluation_count():
    row, fact, verdict, metadata, source = fixture()
    assert propose(row, fact, verdict, metadata, source)["proposed_num_runs"] == 10


def test_normalized_display_fields_require_literal_source_conversion():
    row, fact, verdict, metadata, source = fixture()
    fact.locations[0].displayed_mean = 0.8
    fact.locations[0].displayed_std = 0.002
    result = propose(row, fact, verdict, metadata, source)
    assert result["proposed_num_runs"] == 10
    assert result["representation_corrections"] == [0]
    fact.locations[0].displayed_std = 0.003
    assert propose(row, fact, verdict, metadata, source)["action"] == "ungrounded_mean"


def test_printed_table_number_resolved_only_by_unique_containing_spans():
    row, fact, verdict, metadata, source = fixture()
    fact.locations[0].table_id = 4
    result = propose(row, fact, verdict, metadata, source)
    assert result["proposed_num_runs"] == 10
    assert result["table_id_corrections"][0]["resolved"] == 1
    fact.locations[0].cell_evidence = Span(start_line=5, end_line=5)
    assert propose(row, fact, verdict, metadata, source)["action"] == "ungrounded_cell"


def test_copied_origin_valid_without_current_execution():
    row, fact, verdict, metadata, source = fixture()
    fact.origin = "copied"
    fact.origin_evidence = [Span(start_line=6, end_line=6)]
    verdict.current_evaluation_supported = False
    result = propose(row, fact, verdict, metadata, source)
    assert result["action"] == "copied_excluded"
    assert result["include_as_independent_result"] is False
    assert result["proposed_num_runs"] is None


def test_copied_source_conflict_still_excludes_independent_count():
    row, fact, verdict, metadata, source = fixture()
    fact.origin = "copied"
    fact.origin_evidence = [Span(start_line=6, end_line=6)]
    verdict.duplicates_compatible = False
    result = propose(row, fact, verdict, metadata, source)
    assert result["action"] == "copied_excluded"
    assert result["source_presentations_conflict"] is True


def test_prior_coincidence_without_source_evidence_cannot_prove_copy():
    row, fact, verdict, metadata, source = fixture()
    fact.origin = "copied"
    fact.origin_evidence = []
    assert propose(row, fact, verdict, metadata, source)["action"] == "origin_unresolved"


def test_wrong_std_scale_quarantined_even_if_mean_matches():
    row, fact, verdict, metadata, source = fixture()
    row["std"] = 0.2
    result = propose(row, fact, verdict, metadata, source)
    assert result["action"] == "propose_quarantine"
    assert result["quarantine_kind"] == "std_mismatch"


def test_verifier_rejecting_match_can_establish_grounded_std_defect():
    row, fact, verdict, metadata, source = fixture()
    row["std"] = 0.2
    verdict.decision_supported = False
    verdict.std_supported = False
    assert propose(row, fact, verdict, metadata, source)["quarantine_kind"] == "std_mismatch"


def test_verifier_rejecting_identity_can_establish_quarantine():
    row, fact, verdict, metadata, source = fixture()
    verdict.identity_supported = False
    verdict.decision_supported = False
    assert (
        propose(row, fact, verdict, metadata, source)["quarantine_kind"]
        == "identity_or_protocol_mismatch"
    )


def test_explicit_verifier_disposition_preserves_unsupported_vs_contradicted():
    row, fact, verdict, metadata, source = fixture()
    verdict.decision_supported = False
    verdict.quarantine_recommended = True
    verdict.setting_status = "unsubstantiated"
    assert (
        propose(row, fact, verdict, metadata, source)["quarantine_kind"]
        == "stored_setting_unsubstantiated"
    )


def test_evidence_backed_origin_correction_can_recover_reproduction():
    row, fact, verdict, metadata, source = fixture()
    fact.origin = "unclear"
    fact.repetitions = None
    verdict.corrected_origin = "self_evaluated"
    verdict.corrected_repetitions = 10
    verdict.correction_evidence = [Span(start_line=5, end_line=5)]
    result = propose(row, fact, verdict, metadata, source)
    assert result["proposed_num_runs"] == 10
    assert result["fact"]["origin"] == "unclear"
    assert result["verifier_corrected_fact"]["origin"] == "self_evaluated"


def test_origin_correction_without_primary_evidence_is_not_applied():
    row, fact, verdict, metadata, source = fixture()
    fact.origin = "unclear"
    verdict.corrected_origin = "self_evaluated"
    verdict.corrected_repetitions = 10
    assert propose(row, fact, verdict, metadata, source)["action"] == "origin_unresolved"


def test_required_correction_judges_replacement_not_discarded_origin():
    row, fact, verdict, metadata, source = fixture()
    fact.origin = "unclear"
    fact.repetitions = None
    verdict.origin_classification_supported = False
    verdict.current_evaluation_supported = False
    verdict.decision_supported = False
    verdict.evidence_supported = False
    verdict.correction = VerifiedCorrection(
        origin="self_evaluated",
        origin_supported=True,
        current_evaluation_supported=True,
        repetitions=10,
        count_supported=True,
        unit_correct=True,
        evidence_supported=True,
        evidence=[Span(start_line=5, end_line=5)],
    )
    assert propose(row, fact, verdict, metadata, source)["proposed_num_runs"] == 10
    verdict.correction.origin_supported = False
    assert propose(row, fact, verdict, metadata, source)["proposed_num_runs"] is None


def test_identical_multiple_cells_not_automatically_ambiguous():
    row, fact, verdict, metadata, source = fixture()
    fact.locations.append(fact.locations[0].model_copy())
    verdict.verified_location_indices = [0, 1]
    assert propose(row, fact, verdict, metadata, source)["proposed_num_runs"] == 10
    verdict.duplicates_compatible = False
    assert (
        propose(row, fact, verdict, metadata, source)["action"]
        == "ambiguous_protocol_or_configuration"
    )


def test_prior_verifier_ablation_is_retained():
    row, fact, verdict, metadata, source = fixture()
    metadata["verification"]["methods"] = [
        {
            "table_id": 1,
            "name": "Own",
            "benchmark_supported": False,
            "explanation": "Component-replacement ablation",
        }
    ]
    result = propose(row, fact, verdict, metadata, source)
    assert result["quarantine_kind"] == "verifier_excluded"


def test_special_split_protocol_never_gets_simple_count():
    row, fact, verdict, metadata, source = fixture()
    fact.protocol = "special"
    fact.repetitions = None
    assert (
        propose(row, fact, verdict, metadata, source)["action"] == "self_evaluated_special_protocol"
    )


@pytest.mark.parametrize("value,std", [(80, 0.2), (80.0, 0.20)])
def test_mean_std_same_percentage_divisor(value, std):
    assert printed_matches(value, 0.8, 100, "80.0 $\\pm$ 0.2")
    assert printed_matches(std, 0.002, 100, "80.0 $\\pm$ 0.2")
