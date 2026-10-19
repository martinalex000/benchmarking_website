"""Coverage failures need fresh outputs and must retain their failed attempts."""

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from experiments.table_provenance_experiment.protocol_review_coverage import complete_call


def output(ids):
    return SimpleNamespace(verdicts=[SimpleNamespace(result_id=i) for i in ids])


def test_incomplete_output_gets_full_coverage_feedback():
    with patch(
        "experiments.table_provenance_experiment.protocol_review_coverage.call",
        side_effect=[output([1]), output([1, 2])],
    ) as call:
        result = complete_call(
            None, "prompt", "source", None, "review", None, [{"result_id": 1}, {"result_id": 2}]
        )
    assert len(result.verdicts) == 2
    assert "ENTIRE corrected output" in call.call_args_list[1].args[2]
    assert call.call_args_list[0].args[4] != call.call_args_list[1].args[4]


def test_persistent_missing_or_duplicate_ids_remain_a_failed_call():
    with (
        patch(
            "experiments.table_provenance_experiment.protocol_review_coverage.call",
            return_value=output([1, 1]),
        ),
        pytest.raises(ValueError, match="after 3 attempts"),
    ):
        complete_call(
            None, "prompt", "source", None, "review", None, [{"result_id": 1}, {"result_id": 2}]
        )


def test_api_error_is_not_transformed_into_unknown():
    with (
        patch(
            "experiments.table_provenance_experiment.protocol_review_coverage.call",
            side_effect=TimeoutError("transport failed"),
        ),
        pytest.raises(TimeoutError),
    ):
        complete_call(None, "prompt", "source", None, "review", None, [{"result_id": 1}])
