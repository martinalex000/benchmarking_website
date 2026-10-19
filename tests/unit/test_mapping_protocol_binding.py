"""Count attachment cannot silently contradict the table-level protocol input."""

import pytest

from experiments.table_provenance_experiment.check_protocol_binding import (
    check_binding,
    input_total,
)


def key(**changes):
    return {
        "table_id": 1,
        "method": {
            "name": "Own",
            "origin": "self_evaluated",
            "status": "simple",
            "design": "repeated_training",
            "repetitions": 10,
            "cv_folds": None,
            "count_evidence": [],
            **changes,
        },
        "previous_verdict": dict.fromkeys(
            (
                "benchmark_supported",
                "origin_supported",
                "count_supported",
                "unit_correct",
                "uniform_datasets",
            ),
            True,
        ),
    }


def row():
    return {
        "result_id": 1,
        "action": "propose_count",
        "proposed_num_runs": 10,
        "selected_candidate": {"table_id": 1, "method": "Own"},
    }


def test_matching_table_method_retains_count_without_reextracting():
    assert check_binding(row(), [key()])["proposed_num_runs"] == 10


def test_table_level_unknown_cannot_be_overridden_for_some_rows():
    prior = key()
    prior["previous_verdict"]["count_supported"] = False
    result = check_binding(row(), [prior])
    assert result["action"] == "protocol_input_unresolved"
    assert result["proposed_num_runs"] is None
    assert row()["proposed_num_runs"] == 10


@pytest.mark.parametrize("folds,repetitions,expected", [(10, 1, 10), (10, 10, 100), (5, 3, 15)])
def test_cv_input_total_uses_agreed_model_fit_convention(folds, repetitions, expected):
    assert (
        input_total(key(design="repeated_cv", cv_folds=folds, repetitions=repetitions)) == expected
    )


def test_other_table_or_baseline_needs_explicit_scope_binding():
    previous = key()
    previous["table_id"] = 2
    assert check_binding(row(), [previous])["action"] == "protocol_binding_unresolved"
    previous["table_id"] = 1
    previous["method"]["name"] = "Baseline"
    assert check_binding(row(), [previous])["action"] == "protocol_binding_unresolved"


def test_conflicting_keys_or_counts_are_not_resolved_by_order():
    assert (
        check_binding(row(), [key(), key(repetitions=5)])["action"] == "protocol_input_unresolved"
    )
    assert check_binding(row(), [key(repetitions=5)])["action"] == "protocol_input_conflict"


def test_copied_and_special_keys_do_not_supply_simple_counts():
    assert input_total(key(origin="copied")) is None
    assert input_total(key(status="special")) is None
    previous = key()
    previous["previous_verdict"]["uniform_datasets"] = False
    assert input_total(previous) is None


def test_descriptive_expansion_resolves_via_actual_source_method_not_database_label():
    current = row()
    current["selected_candidate"].update(
        method="Long descriptive kernel name", row_evidence={"start_line": 1, "end_line": 1}
    )
    previous = key()
    previous["method"]["name"] = "p--RW"
    source = r"\m{p}--RW & 80.33 (\pm 1.35)"
    assert check_binding(current, [previous], source)["proposed_num_runs"] == 10
    assert (
        check_binding(current, [previous], r"Other & 80.33")["action"]
        == "protocol_binding_unresolved"
    )


def test_parenthetical_description_does_not_change_exact_method_identity():
    current = row()
    current["selected_candidate"]["method"] = "Own (proposed kernel)"
    assert check_binding(current, [key()])["protocol_binding"]["status"] == "matched"
