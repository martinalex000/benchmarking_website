"""CV structure, total-model units, repair guards and ranking regressions."""

import pytest
from pydantic import ValidationError

from experiments.table_provenance_experiment.verify_stored_mapping_v3 import (
    Candidate,
    CompleteRetryVerdict,
    Fact,
    Protocol,
    Repair,
    Span,
    Verdict,
    grounded_protocol,
    normalized_scale,
    propose,
    rank,
    total_models,
)


def protocol(**changes):
    return Protocol.model_validate(
        {
            "design": "repeated_training",
            "training_repetitions": 5,
            "cv_folds": None,
            "cv_repetitions": None,
            "dataset_splits": None,
            "repetitions_per_split": None,
            "reported_runs": 5,
            "variability_scope": "unknown",
            "evidence": [{"start_line": 5, "end_line": 5}],
            "scope_evidence": [{"start_line": 5, "end_line": 5}],
            "explanation": "Explicit scoped protocol",
            **changes,
        }
    )


@pytest.mark.parametrize(
    "design,folds,repeats,expected",
    [
        ("single_cv", 10, 1, 10),
        ("repeated_cv", 10, 10, 100),
        ("repeated_cv", 10, 5, 50),
        ("repeated_cv", 10, None, None),
    ],
)
def test_cv_uses_total_models_but_retains_outer_repeats(design, folds, repeats, expected):
    p = protocol(design=design, training_repetitions=None, cv_folds=folds, cv_repetitions=repeats)
    assert total_models(p) == expected
    assert p.cv_repetitions == repeats


def fixture():
    source = "\\begin{table}\nMethod & Cora \\\\\nOwn & 80.0 $\\pm$ 0.2 \\\\\n\\end{table}\nWe evaluate Own with 5 runs.\n"
    row = {"result_id": 1, "value": 0.8, "std": 0.002, "model": "Own", "variant": "fixed"}
    span = Span(start_line=3, end_line=3)
    candidate = Candidate(
        table_id=1,
        displayed_mean=80,
        displayed_std=0.2,
        divisor=100,
        method="Own",
        dataset="Cora",
        metric="Accuracy",
        configuration="Own",
        eligibility="benchmark",
        main_experiment=True,
        row_evidence=span,
        column_evidence=Span(start_line=2, end_line=2),
        cell_evidence=span,
        protocol=protocol(),
    )
    fact = Fact(
        result_id=1,
        candidates=[candidate],
        origin="self_evaluated",
        origin_evidence=[Span(start_line=5, end_line=5)],
        execution_evidence=[Span(start_line=5, end_line=5)],
        repair=None,
        explanation="Explicit",
    )
    verdict = Verdict(
        result_id=1,
        corrected_fact=fact,
        verified_candidate_indices=[0],
        origin_supported=True,
        execution_supported=True,
        protocol_supported=True,
        repair_supported=False,
        setting_status="supported",
        eligibility="benchmark",
        explanation="Verified",
    )
    return row, verdict, source


def test_fractional_bounded_cell_is_not_divided_by_100_again():
    _, verdict, source = fixture()
    candidate = verdict.corrected_fact.candidates[0].model_copy(
        update={"displayed_mean": 0.8, "displayed_std": 0.002, "divisor": 100}
    )
    result = normalized_scale(candidate, source)
    assert result.divisor == 1
    assert result.displayed_mean == 0.8
    assert result.displayed_std == 0.002


def test_explicit_percentage_caption_preserves_small_percentage_result():
    _, verdict, source = fixture()
    source = source.replace(r"\begin{table}", r"\begin{table}" + "\n" + r"\caption{Accuracy (\%)}")
    candidate = verdict.corrected_fact.candidates[0].model_copy(
        update={"displayed_mean": 0.8, "displayed_std": 0.002, "divisor": 100}
    )
    assert normalized_scale(candidate, source).divisor == 100


def test_unbounded_error_metric_does_not_get_percentage_conversion():
    _, verdict, source = fixture()
    candidate = verdict.corrected_fact.candidates[0].model_copy(
        update={"metric": "MAE", "displayed_mean": 20.5, "divisor": 1}
    )
    assert normalized_scale(candidate, source).divisor == 1


def test_repeated_cv_proposal_assigns_100_not_10():
    row, verdict, source = fixture()
    source = source.replace("5 runs", "10 repetitions of 10-fold CV")
    verdict.corrected_fact.candidates[0].protocol = protocol(
        design="repeated_cv", training_repetitions=None, cv_folds=10, cv_repetitions=10
    )
    assert grounded_protocol(verdict.corrected_fact.candidates[0].protocol, source)
    result = propose(row, verdict, source)
    assert result["proposed_num_runs"] == 100
    assert result["protocol"]["cv_repetitions"] == 10


def test_executed_experiments_opt_in_preserves_original_guard():
    row, verdict, source = fixture()
    source = source.replace("We evaluate Own with 5 runs.", "We run $5$ experiments.")
    assert propose(row, verdict, source)["proposed_num_runs"] is None
    assert propose(row, verdict, source, allow_experiments=True)["proposed_num_runs"] == 5
    source = source.replace("We run $5$ experiments.", "We select from 5 experiments for tuning.")
    assert propose(row, verdict, source, allow_experiments=True)["proposed_num_runs"] is None


def test_explicit_random_seed_trials_are_counted_not_tuning_trials():
    row, verdict, source = fixture()
    row["metric"] = "Accuracy"
    verdict.corrected_fact.candidates[0].metric = "Accuracy"
    source = source.replace(
        "We evaluate Own with 5 runs.", "We run experiments with random seeds over 5 trials."
    )
    assert propose(row, verdict, source, allow_experiments=True)["proposed_num_runs"] == 5
    source = source.replace("random seeds", "hyperparameters")
    assert propose(row, verdict, source, allow_experiments=True)["proposed_num_runs"] is None


def test_metric_mismatch_cannot_accept_count_without_actual_metric_repair():
    row, verdict, source = fixture()
    row["metric"] = "Accuracy"
    verdict.corrected_fact.candidates[0].metric = "F1-macro"
    assert propose(row, verdict, source, allow_experiments=True)["action"] == "metric_unresolved"
    verdict.corrected_fact.repair = Repair(
        old_value=row["value"],
        old_std=row["std"],
        old_model=row["model"],
        old_variant=row["variant"],
        corrected_value=row["value"],
        corrected_std=row["std"],
        corrected_model=row["model"],
        corrected_variant=row["variant"],
        old_metric="Accuracy",
        corrected_metric="F1-macro",
        evidence=[Span(start_line=3, end_line=3)],
        explanation="Metric header verified",
    )
    verdict.repair_supported = True
    result = propose(row, verdict, source, allow_experiments=True)
    assert result["correction"]["corrected"]["metric"] == "F1-macro"
    assert result["proposed_num_runs"] == 5


def test_repetitions_within_folds_do_not_assert_outer_cv_or_std_scope():
    row, verdict, source = fixture()
    source = source.replace(
        "5 runs",
        "10-fold cross validation. In each partition, experiments are repeated for 10 times",
    )
    verdict.corrected_fact.candidates[0].protocol = protocol(
        design="repeated_cv",
        training_repetitions=None,
        cv_folds=10,
        cv_repetitions=10,
        variability_scope="cv_runs",
    )
    result = propose(row, verdict, source, allow_experiments=True)
    assert result["proposed_num_runs"] == 100
    assert result["protocol"]["cv_repeat_unit"] == "within_fold"
    assert result["protocol"]["variability_scope"] == "unknown"


def test_retry_schema_rejects_dropped_candidates_without_forcing_verification():
    row, verdict, source = fixture()
    payload = verdict.model_dump()
    payload["verified_candidate_indices"] = []
    assert CompleteRetryVerdict.model_validate(payload).verified_candidate_indices == []
    payload["corrected_fact"]["candidates"] = []
    with pytest.raises(ValidationError):
        CompleteRetryVerdict.model_validate(payload)


def test_single_cv_accepts_spelled_folds_as_total_models():
    row, verdict, source = fixture()
    source = source.replace("5 runs", "ten-fold cross-validation")
    verdict.corrected_fact.candidates[0].protocol = protocol(
        design="single_cv", training_repetitions=None, cv_folds=10, cv_repetitions=1
    )
    result = propose(row, verdict, source)
    assert result["proposed_num_runs"] == 10
    assert result["count_unit"] == "models_trained"


def test_cv_fold_number_requires_source_not_only_stored_label():
    row, verdict, source = fixture()
    verdict.corrected_fact.candidates[0].protocol = protocol(
        design="single_cv", training_repetitions=None, cv_folds=10, cv_repetitions=1
    )
    assert propose(row, verdict, source)["action"] == "self_evaluated_protocol_unresolved"


def test_unverified_cv_label_is_not_quarantined_or_multiplied():
    row, verdict, source = fixture()
    verdict.setting_status = "unverified"
    verdict.protocol_supported = False
    verdict.corrected_fact.candidates[0].protocol = protocol(
        design="unknown", training_repetitions=None, reported_runs=10
    )
    assert propose(row, verdict, source)["action"] == "self_evaluated_protocol_unresolved"


def test_ambiguous_runs_do_not_override_unverified_cv_setting():
    row, verdict, source = fixture()
    row["variant"] = "10-fold CV"
    verdict.setting_status = "unverified"
    assert propose(row, verdict, source)["action"] == "self_evaluated_protocol_unresolved"
    verdict.setting_status = "supported"
    result = propose(row, verdict, source)
    assert result["action"] == "self_evaluated_protocol_unresolved"
    assert result["protocol"]["design"] == "unknown"
    assert result["protocol"]["reported_runs"] == 5


def test_partial_std_normalization_can_be_repaired_with_old_and_new_values():
    row, verdict, source = fixture()
    row["std"] = 0.2
    verdict.corrected_fact.repair = Repair(
        old_value=0.8,
        old_std=0.2,
        old_model="Own",
        old_variant="fixed",
        corrected_value=0.8,
        corrected_std=0.002,
        corrected_model="Own",
        corrected_variant="fixed",
        evidence=[Span(start_line=3, end_line=3)],
        explanation="Normalize both fields",
    )
    verdict.repair_supported = True
    result = propose(row, verdict, source)
    assert result["proposed_num_runs"] == 5
    assert result["correction"]["old"]["std"] == 0.2
    assert result["correction"]["corrected"]["std"] == 0.002
    verdict.setting_status = "unverified"
    verdict.corrected_fact.repair.corrected_variant = "unspecified split"
    result = propose(row, verdict, source)
    assert result["correction"]["corrected"]["variant"] == "fixed"
    assert result["correction"]["corrected"]["std"] == 0.002
    verdict.corrected_fact.repair.old_std = 0.3
    assert propose(row, verdict, source)["action"] == "repair_unverified"


def test_copied_cv_does_not_receive_current_paper_count():
    row, verdict, source = fixture()
    verdict.corrected_fact.origin = "copied"
    assert propose(row, verdict, source)["action"] == "copied_excluded"
    assert propose(row, verdict, source)["proposed_num_runs"] is None


def test_previous_trusted_ablation_exclusion_cannot_be_revived():
    row, verdict, source = fixture()
    result = propose(row, verdict, source, prior_eligibility="ablation")
    assert result["action"] == "propose_quarantine"
    assert result["proposed_num_runs"] is None
    assert result["reason"] == "prior_verifier_excluded"


def test_source_order_is_final_tiebreak_and_main_body_beats_appendix():
    row, verdict, source = fixture()
    first = verdict.corrected_fact.candidates[0]
    second = first.model_copy(update={"cell_evidence": Span(start_line=10, end_line=10)})
    source += "\\appendix\n" + "extra\n" * 5
    assert rank(first, source) < rank(second, source)


def test_split_hierarchy_counts_all_trained_models():
    p = protocol(
        design="split_training",
        training_repetitions=100,
        dataset_splits=20,
        repetitions_per_split=5,
        reported_runs=100,
    )
    assert total_models(p) == 100


def test_split_training_requires_a_consistent_total():
    p = protocol(
        design="split_training",
        training_repetitions=99,
        dataset_splits=20,
        repetitions_per_split=5,
        reported_runs=99,
    )
    assert total_models(p) is None


def test_source_grounded_split_training_is_countable():
    source = (
        "We selected 5 random train/valid/test splits.\n"
        "We ran 10 turns with different seeds in each split.\n"
        "Table 1 reports Own on Cora."
    )
    p = protocol(
        design="split_training",
        training_repetitions=50,
        dataset_splits=5,
        repetitions_per_split=10,
        reported_runs=50,
        variability_scope="splits",
        evidence=[{"start_line": 1, "end_line": 2}],
        scope_evidence=[{"start_line": 3, "end_line": 3}],
    )
    assert total_models(p) == 50
    assert grounded_protocol(p, source)


def test_contradicted_cv_label_repairs_to_explicit_split_training():
    source = (
        "\\begin{table}\n"
        "Method & Cora \\\\\n"
        "Own & 80.0 $\\pm$ 0.2 \\\\\n"
        "\\end{table}\n"
        "We select 5 random train/valid/test splits.\n"
        "We run 10 turns with different random seeds in each split.\n"
    )
    row = {
        "result_id": 1,
        "value": 0.8,
        "std": 0.002,
        "model": "Own",
        "variant": "Random 10-fold",
    }
    cell = Span(start_line=3, end_line=3)
    p = protocol(
        design="split_training",
        training_repetitions=50,
        dataset_splits=5,
        repetitions_per_split=10,
        reported_runs=50,
        variability_scope="splits",
        evidence=[Span(start_line=5, end_line=6)],
        scope_evidence=[Span(start_line=2, end_line=2)],
    )
    candidate = Candidate(
        table_id=1,
        displayed_mean=80,
        displayed_std=0.2,
        divisor=100,
        method="Own",
        dataset="Cora",
        metric="Accuracy",
        configuration="Own",
        eligibility="benchmark",
        main_experiment=True,
        row_evidence=cell,
        column_evidence=Span(start_line=2, end_line=2),
        cell_evidence=cell,
        protocol=p,
    )
    repair = Repair(
        old_value=0.8,
        old_std=0.002,
        old_model="Own",
        old_variant="Random 10-fold",
        corrected_value=0.8,
        corrected_std=0.002,
        corrected_model="Own",
        corrected_variant="5 random splits x 10 seeds (split_training, no CV)",
        evidence=[Span(start_line=5, end_line=6)],
        explanation="The table value is reported over five splits and ten seeds per split.",
    )
    fact = Fact(
        result_id=1,
        candidates=[candidate],
        origin="self_evaluated",
        origin_evidence=[Span(start_line=6, end_line=6)],
        execution_evidence=[Span(start_line=6, end_line=6)],
        repair=repair,
        explanation="Author-run baseline under the controlled experiment.",
    )
    verdict = Verdict(
        result_id=1,
        corrected_fact=fact,
        verified_candidate_indices=[0],
        origin_supported=True,
        execution_supported=True,
        protocol_supported=True,
        repair_supported=True,
        setting_status="contradicted",
        eligibility="benchmark",
        explanation="Cell and explicit split-training protocol verified.",
    )

    result = propose(row, verdict, source)

    assert result["action"] == "propose_count"
    assert result["proposed_num_runs"] == 50
    assert result["correction"]["corrected"]["variant"] == repair.corrected_variant


def test_cv_fields_cannot_be_ignored_by_training_design():
    assert total_models(protocol(cv_folds=10)) is None
    assert total_models(protocol(design="single_cv", cv_folds=10)) is None
    assert total_models(protocol(dataset_splits=20)) is None


def test_more_grounded_repetitions_before_source_order_but_after_main_experiment():
    row, verdict, source = fixture()
    source += "We evaluate Own with 10 runs.\n"
    first = verdict.corrected_fact.candidates[0]
    second = first.model_copy(
        update={
            "cell_evidence": Span(start_line=6, end_line=6),
            "protocol": protocol(
                training_repetitions=10, evidence=[{"start_line": 6, "end_line": 6}]
            ),
        }
    )
    assert rank(second, source) < rank(first, source)
    second.main_experiment = False
    assert rank(first, source) < rank(second, source)


def test_origin_only_reclassification_is_not_counted_as_a_value_repair():
    row, verdict, source = fixture()
    verdict.corrected_fact.repair = Repair(
        old_value=0.8,
        old_std=0.002,
        old_model="Own",
        old_variant="fixed",
        corrected_value=0.8,
        corrected_std=0.002,
        corrected_model="Own",
        corrected_variant="fixed",
        evidence=[Span(start_line=3, end_line=3)],
        explanation="Only origin changes",
    )
    verdict.repair_supported = True
    assert propose(row, verdict, source)["correction"] is None
    verdict.corrected_fact.repair.corrected_model = "OWN"
    assert propose(row, verdict, source)["correction"] is None
    verdict.corrected_fact.repair.corrected_variant = "Transductive: training on all nodes"
    assert propose(row, verdict, source)["correction"] is None
    row["variant"] = "Standard split"
    verdict.corrected_fact.repair.old_variant = "Standard split"
    verdict.corrected_fact.repair.corrected_variant = "20 train / 2 val / 2 test graphs"
    assert propose(row, verdict, source)["correction"] is None
    row["model"] = "Own-PNA"
    verdict.corrected_fact.repair.old_model = "Own-PNA"
    verdict.corrected_fact.repair.corrected_model = "Own (PNA extractor)"
    assert propose(row, verdict, source)["correction"] is None
