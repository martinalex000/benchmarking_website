from copy import deepcopy

import pytest
from pydantic import ValidationError

from backend.repetition_extractor import repetition_input
from backend.repetition_metadata import (
    Evidence,
    RepetitionFacts,
    Verification,
    grounded,
    has_execution_evidence,
    supports_repeat_count,
    table_inventory,
    validate_repetitions,
)

SOURCE = "\n".join(
    [
        "We propose OwnNet for this task.",
        r"\begin{table}",
        r"\caption{Benchmark accuracy (\%) for OwnNet and Baseline.}",
        r"OwnNet & 80 \\ Baseline & 70 \\",
        r"\end{table}",
        "We train all methods on both datasets and repeat 10-fold cross-validation for five trials.",
    ]
)


def evidence(line):
    return {"start_line": line, "end_line": line, "quote": SOURCE.splitlines()[line - 1]}


def payload():
    return {
        "proposed_methods": [{"name": "OwnNet", "evidence": [evidence(1)]}],
        "tables": [
            {
                "table_id": 1,
                "role": "benchmark",
                "role_evidence": [evidence(3)],
                "complication": "",
                "methods": [
                    {
                        "name": "OwnNet",
                        "role": "proposed",
                        "origin": "self_evaluated",
                        "origin_evidence": [evidence(6)],
                        "status": "simple",
                        "repetitions": 5,
                        "cv_folds": 10,
                        "design": "repeated_cv",
                        "count_evidence": [evidence(6)],
                        "scope_evidence": [evidence(6)],
                        "explanation": "five outer trials",
                    }
                ],
            }
        ],
    }


def verdict(**overrides):
    result = {
        "table_id": 1,
        "name": "OwnNet",
        "benchmark_supported": True,
        "origin_supported": True,
        "count_supported": True,
        "unit_correct": True,
        "uniform_datasets": True,
        "explanation": "source supports all datasets",
    }
    return Verification.model_validate({"methods": [{**result, **overrides}]})


def test_repeated_cv_accepts_outer_trials_not_product():
    result = validate_repetitions(RepetitionFacts.model_validate(payload()), verdict(), SOURCE)
    assert result["accepted"][0]["repetitions"] == 5
    assert result["accepted"][0]["cv_folds"] == 10
    assert not result["withheld"]


def test_explicit_repetition_count_is_kept_even_when_table_displays_no_stds():
    raw = payload()
    raw["tables"][0]["decision"] = "count"
    raw["tables"][0]["complication"] = "No standard deviations displayed."
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), SOURCE)
    assert result["table_outcomes"][0]["outcome"] == "count"
    assert result["table_outcomes"][0]["count"] == 5


def test_no_stds_without_stated_repeats_is_unknown_not_zero_or_one():
    source = SOURCE.replace(SOURCE.splitlines()[5], "We train all methods on both datasets.")
    raw = payload()
    table = raw["tables"][0]
    table["decision"] = "unknown"
    table["complication"] = "no_standard_deviations_reported"
    method = table["methods"][0]
    method.update(
        status="unstated",
        repetitions=None,
        cv_folds=None,
        design="unknown",
        count_evidence=[],
        origin_evidence=[{"start_line": 6, "end_line": 6}],
        scope_evidence=[{"start_line": 6, "end_line": 6}],
        explanation="No standard deviations displayed; repetition count not stated.",
    )
    result = validate_repetitions(
        RepetitionFacts.model_validate(raw), verdict(count_supported=False), source
    )
    outcome = result["table_outcomes"][0]
    assert outcome["outcome"] == "unknown"
    assert outcome["count"] is None
    assert "No standard deviations displayed" in outcome["reason"]


@pytest.mark.parametrize("training", ["", " We train each model five times per split."])
def test_reported_split_variability_remains_special_even_with_known_trainings_per_split(training):
    source = SOURCE.replace(
        SOURCE.splitlines()[5],
        "We train all methods on both datasets using ten random train/test splits. "
        "We report the mean and standard deviation across the ten splits." + training,
    )
    raw = payload()
    table = raw["tables"][0]
    table["decision"] = "special"
    table["complication"] = "split_variability: reported standard deviation is across data splits."
    method = table["methods"][0]
    method.update(
        status="complex",
        repetitions=None,
        cv_folds=None,
        design="nested" if training else "unknown",
        count_evidence=[{"start_line": 6, "end_line": 6}],
        origin_evidence=[{"start_line": 6, "end_line": 6}],
        scope_evidence=[{"start_line": 6, "end_line": 6}],
        explanation="Ten random splits; std over split-level results, not initialization seeds.",
    )
    result = validate_repetitions(
        RepetitionFacts.model_validate(raw),
        verdict(count_supported=False, unit_correct=False),
        source,
    )
    assert not result["accepted"]
    outcome = result["table_outcomes"][0]
    assert outcome["outcome"] == "special"
    assert outcome["count"] is None
    assert "split_variability" in outcome["reason"]


@pytest.mark.parametrize("role", ["proposed", "baseline"])
def test_ablation_variant_is_ineligible_regardless_of_method_role(role):
    raw = payload()
    method = raw["tables"][0]["methods"][0]
    method["role"] = role
    method["explanation"] = "Ablation variant shown alongside benchmark methods."
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), SOURCE)
    assert not result["accepted"]
    assert "ablation_variant_not_eligible" in result["withheld"][0]["flags"]


def test_mention_of_excluded_other_ablation_variant_does_not_reject_main_method():
    raw = payload()
    raw["tables"][0]["methods"][0]["explanation"] = (
        "OwnNet evaluated with five trials. OwnNet-minus is an ablation variant excluded."
    )
    assert validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), SOURCE)["accepted"]


def test_ambiguous_splits_over_initializations_is_not_per_split_even_if_judge_agrees():
    source = SOURCE.replace(
        SOURCE.splitlines()[5],
        "We evaluate with 20 dataset splits over 5 random weight initializations.",
    )
    raw = payload()
    method = raw["tables"][0]["methods"][0]
    method["design"] = "repeated_training"
    method["cv_folds"] = None
    for field in ("origin_evidence", "count_evidence", "scope_evidence"):
        method[field] = [{"start_line": 6, "end_line": 6}]
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), source)
    assert "split_initialization_relationship_unresolved" in result["withheld"][0]["flags"]


def test_other_protocol_each_split_clause_does_not_resolve_unsupervised_ambiguity():
    source = SOURCE.replace(
        SOURCE.splitlines()[5],
        "We evaluate with 20 dataset splits over 5 random weight initializations. "
        "For supervised experiments we use one initialization for each split.",
    )
    raw = payload()
    method = raw["tables"][0]["methods"][0]
    method["design"] = "repeated_training"
    method["cv_folds"] = None
    for field in ("origin_evidence", "count_evidence", "scope_evidence"):
        method[field] = [{"start_line": 6, "end_line": 6}]
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), source)
    assert "split_initialization_relationship_unresolved" in result["withheld"][0]["flags"]


def test_nested_encoder_and_clustering_repeats_are_rejected_when_judge_agrees():
    source = SOURCE.replace(
        SOURCE.splitlines()[5],
        "We train each model with 5 random weight initializations, "
        "perform k-means 5 times on each trained encoder, and report the averaged results.",
    )
    raw = payload()
    method = raw["tables"][0]["methods"][0]
    method["design"] = "repeated_training"
    method["cv_folds"] = None
    for field in ("origin_evidence", "count_evidence", "scope_evidence"):
        method[field] = [{"start_line": 6, "end_line": 6}]
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), source)
    assert "nested_training_clustering_protocol" in result["withheld"][0]["flags"]


def test_unknown_has_explicit_table_outcome_without_inventing_one_run():
    source = SOURCE.replace(
        SOURCE.splitlines()[5], "We train all models with 10-fold cross-validation."
    )
    raw = payload()
    method = raw["tables"][0]["methods"][0]
    method.update(status="unstated", repetitions=None, design="single_cv")
    for field in ("origin_evidence", "count_evidence", "scope_evidence"):
        method[field] = [{"start_line": 6, "end_line": 6}]
    result = validate_repetitions(
        RepetitionFacts.model_validate(raw),
        verdict(count_supported=False, unit_correct=False),
        source,
    )
    assert result["table_outcomes"][0]["outcome"] == "unknown"
    assert result["table_outcomes"][0]["count"] is None


def test_parenthetical_definition_does_not_hide_proposed_family():
    raw = payload()
    raw["proposed_methods"][0]["name"] = "OwnNet (including small variants)"
    assert validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), SOURCE)["accepted"]


def test_baseline_count_caption_is_not_execution_evidence():
    raw = payload()
    method = raw["tables"][0]["methods"][0]
    method["role"] = "baseline"
    method["origin_evidence"] = [evidence(3)]
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), SOURCE)
    assert "baseline_execution_evidence_missing" in result["withheld"][0]["flags"]


def test_explicit_baseline_execution_does_not_inherit_proposed_only_count():
    source = SOURCE.replace(
        SOURCE.splitlines()[5], "We train Baseline and repeat our model five times."
    )
    raw = payload()
    method = raw["tables"][0]["methods"][0]
    method["role"] = "baseline"
    method["design"] = "repeated_training"
    for field in ("origin_evidence", "count_evidence", "scope_evidence"):
        method[field] = [{"start_line": 6, "end_line": 6}]
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), source)
    assert "baseline_count_scope_is_proposed_only" in result["withheld"][0]["flags"]


@pytest.mark.parametrize("count", [10, 50])
def test_cv_fold_count_or_product_is_rejected_even_when_verifier_agrees(count):
    raw = payload()
    raw["tables"][0]["methods"][0]["repetitions"] = count
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), SOURCE)
    assert not result["accepted"]
    assert "count_or_unit_not_supported" in result["withheld"][0]["flags"]
    assert result["withheld"][0]["repetitions"] is None


def test_real_quote_with_wrong_dataset_scope_is_rejected_by_verifier():
    result = validate_repetitions(
        RepetitionFacts.model_validate(payload()), verdict(uniform_datasets=False), SOURCE
    )
    assert not result["accepted"]


@pytest.mark.parametrize("origin", ["copied", "mixed", "unclear"])
def test_non_author_or_mixed_origin_does_not_receive_count(origin):
    raw = payload()
    raw["tables"][0]["methods"][0]["origin"] = origin
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), SOURCE)
    assert not result["accepted"]


def test_missing_table_coverage_does_not_refute_other_supported_facts():
    extra = SOURCE + "\n" + r"\begin{wraptable}{r}{4cm}\caption{Setup}\end{wraptable}"
    result = validate_repetitions(RepetitionFacts.model_validate(payload()), verdict(), extra)
    assert len(result["table_outcomes"]) == 2
    assert result["table_outcomes"][0]["outcome"] == "count"
    assert result["table_outcomes"][0]["count"] == 5
    missing = result["table_outcomes"][1]
    assert missing["outcome"] == "special"
    assert missing["special_kind"] == "missing_output"
    assert "omitted" in missing["reason"]
    result = validate_repetitions(RepetitionFacts.model_validate(payload()), verdict(), extra)
    assert result["accepted"]
    assert result["coverage"]["missing_table_ids"] == [2]


def test_wraptable_caption_inventory_preserves_percent_and_nested_braces():
    source = r"\begin{wraptable}{r}{4cm}\caption[Short]{Accuracy (\%) for \textbf{both} tasks.}\end{wraptable}"
    inventory = table_inventory(source)
    assert inventory[0]["environment"] == "wraptable"
    assert inventory[0]["caption"] == r"Accuracy (\%) for \textbf{both} tasks."
    assert repetition_input(source).startswith("ALL SOURCE TABLE ENVIRONMENTS")


def test_multiple_captions_are_inventoried_and_counts_withheld():
    source = SOURCE.replace(r"\end{table}", r"\caption{Ablation}\end{table}")
    assert len(table_inventory(source)[0]["captions"]) == 2
    result = validate_repetitions(RepetitionFacts.model_validate(payload()), verdict(), source)
    assert not result["accepted"]
    assert "multiple_caption_environment_requires_resolution" in result["withheld"][0]["flags"]


def test_pretrained_embedding_description_is_not_current_execution():
    assert not has_execution_evidence("These methods integrate pre-trained embeddings.")
    assert not has_execution_evidence("We compare performance and training time.")
    assert has_execution_evidence("We used the implementation in the official repository.")
    assert has_execution_evidence("All experiments were conducted using an RTX 8000.")


def test_fold_caption_cannot_be_silently_reinterpreted_as_plain_runs():
    source = SOURCE.replace("Benchmark accuracy", "5-fold benchmark accuracy")
    raw = payload()
    raw["tables"][0]["methods"][0]["design"] = "repeated_training"
    result = validate_repetitions(RepetitionFacts.model_validate(raw), verdict(), source)
    assert "cv_caption_repetition_design_conflict" in result["withheld"][0]["flags"]


def test_made_up_quote_and_bad_line_range_fail_grounding():
    assert not grounded(
        Evidence(start_line=1, end_line=1, quote="We propose some other method."), SOURCE
    )
    assert not grounded(Evidence(start_line=8, end_line=9, quote="We propose OwnNet"), SOURCE)


def test_numeric_strings_and_boolean_counts_are_schema_errors():
    for count in ("5", True):
        raw = deepcopy(payload())
        raw["tables"][0]["methods"][0]["repetitions"] = count
        with pytest.raises(ValidationError):
            RepetitionFacts.model_validate(raw)


@pytest.mark.parametrize(
    "quote,design,count,supported",
    [
        ("We evaluate on ten fixed splits.", "repeated_training", 10, False),
        ("We perform 10-fold cross-validation.", "repeated_cv", 10, False),
        ("We repeat 10-fold cross-validation 5 times.", "repeated_cv", 5, True),
        ("We perform five runs of 10-fold cross-validation.", "repeated_cv", 5, True),
        (r"We use $5$ random seeds.", "repeated_training", 5, True),
        (
            "We used five different random seeds for BenchmarkingGNN datasets and four for others.",
            "repeated_training",
            4,
            True,
        ),
        (
            "We used five different random seeds for BenchmarkingGNN datasets and four for others.",
            "repeated_training",
            5,
            True,
        ),
        (
            "We used five random seeds for dataset A and four for others.",
            "repeated_training",
            6,
            False,
        ),
        (
            "Each configuration is tested for 10 random model initializations and data splits.",
            "repeated_training",
            10,
            True,
        ),
        (
            "We use 100 predetermined random seeds and report results over 100 trials.",
            "repeated_training",
            100,
            True,
        ),
        (r"We run all experiments \textit{five} times.", "repeated_training", 5, True),
    ],
)
def test_repeat_unit_evidence(quote, design, count, supported):
    assert supports_repeat_count(count, quote, design) is supported
