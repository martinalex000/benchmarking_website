"""Human-reviewed CV axes remain scoped in the maintained mapping layer."""

import hashlib

import pytest

from backend.mapping.checks import reviewed_protocol
from backend.mapping.decisions import Protocol, Verdict, total_models
from tests.unit.test_assignment_protocol_refresh import reviewed_fixture


def reviewed_cv_fixture():
    _, previous, source, record = reviewed_fixture()
    raw = previous.model_dump()
    raw.pop("presentations")
    verdict = Verdict.model_validate(raw)
    protocol = Protocol(
        design="repeated_cv",
        training_repetitions=None,
        cv_folds=10,
        cv_repetitions=10,
        dataset_splits=None,
        repetitions_per_split=None,
        reported_runs=10,
        variability_scope="cv_runs",
        evidence=record["evidence"],
        scope_evidence=record["scope_evidence"],
        explanation="Human confirmed ten complete CV repetitions.",
        cv_repeat_unit="full_cv",
    )
    record.update(count=100, protocol=protocol.model_dump(), reviewer="human_user")
    return verdict, source, record


def test_review_preserves_cv_axes_and_does_not_supply_origin_or_identity():
    verdict, source, record = reviewed_cv_fixture()
    reviewed = reviewed_protocol(verdict, [record], source)
    candidate = reviewed.corrected_fact.candidates[0]
    assert total_models(candidate.protocol) == 100
    assert candidate.protocol.cv_folds == 10
    assert candidate.protocol.cv_repetitions == 10
    assert candidate.protocol.reported_runs == 10
    assert candidate.protocol.cv_repeat_unit == "full_cv"
    assert reviewed.corrected_fact.origin == verdict.corrected_fact.origin
    assert candidate.cell_evidence == verdict.corrected_fact.candidates[0].cell_evidence
    assert total_models(verdict.corrected_fact.candidates[0].protocol) == 5


def test_review_rejects_changed_source_or_inconsistent_count():
    verdict, source, record = reviewed_cv_fixture()
    assert record["source_sha256"] == hashlib.sha256(source.encode()).hexdigest()
    with pytest.raises(ValueError, match="source/identity"):
        reviewed_protocol(verdict, [record], source + "Changed source.")
    with pytest.raises(ValueError, match="repetition axes"):
        reviewed_protocol(verdict, [{**record, "count": 10}], source)


@pytest.mark.parametrize("field,value", [("method", "Other"), ("table_id", 2)])
def test_review_does_not_extend_to_other_methods_or_tables(field, value):
    verdict, source, record = reviewed_cv_fixture()
    assert reviewed_protocol(verdict, [{**record, field: value}], source) == verdict
