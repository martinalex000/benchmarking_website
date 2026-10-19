import pytest

from backend.repetition_metadata import RepetitionFacts, table_outcomes
from experiments.table_provenance_experiment.evaluate_six_runs import score_claims

SOURCE = "We propose OwnNet.\n\\begin{table}\n\\caption{Dataset statistics}\n\\end{table}"


def test_excluded_table_has_explicit_reason_and_grounded_evidence():
    facts = RepetitionFacts.model_validate(
        {
            "proposed_methods": [],
            "tables": [
                {
                    "table_id": 1,
                    "role": "excluded",
                    "decision": "excluded",
                    "role_evidence": [{"start_line": 3, "end_line": 3}],
                    "complication": "Dataset statistics, not benchmark results.",
                    "methods": [],
                }
            ],
        }
    )
    result = table_outcomes(facts, SOURCE, {})
    assert result[0]["outcome"] == "excluded"
    assert result[0]["reason"]
    assert result[0]["evidence"][0]["quote"] == r"\caption{Dataset statistics}"


def test_call_failure_is_not_mislabeled_as_paper_unknown():
    result = table_outcomes(None, SOURCE, {}, error="timeout")
    assert result[0]["outcome"] == "special"
    assert result[0]["special_kind"] == "call_failure"
    assert result[0]["reason"] == "timeout"


@pytest.mark.parametrize("expected, correct", [(5, 1), (10, 0), (None, 0)])
def test_precision_collapses_variants_to_a_table_and_does_not_count_unknowns(expected, correct):
    claims = [{"table_id": 1, "role": "proposed", "repetitions": 5}] * 3
    result = score_claims(claims, {"1": expected, "2": 10})
    assert result == {"assigned": 1, "correct": correct, "wrong": 1 - correct}
    assert score_claims([], {"1": None}) == {"assigned": 0, "correct": 0, "wrong": 0}
