"""Tests for conservative per-result run-count extraction."""

from backend.llm_postprocessing import _expand_compact_result_entry
from backend.models import Result
from backend.results_parser import _update_result, _validated_run_metadata


def test_accepts_run_count_for_explicit_author_trained_row():
    entry = {
        "num_runs": 10,
        "trained_by_paper": True,
        "num_runs_evidence": "We report mean and std over 10 independent runs.",
        "source_ref": "this paper",
    }

    assert _validated_run_metadata(entry) == (
        10,
        1,
        "We report mean and std over 10 independent runs.",
    )


def test_rejects_count_for_cited_row_even_with_numeric_evidence():
    entry = {
        "num_runs": 10,
        "trained_by_paper": False,
        "num_runs_evidence": "The cited work used 10 runs.",
        "source_ref": "Smith 2024",
    }

    assert _validated_run_metadata(entry) == (None, 0, None)


def test_rejects_count_when_evidence_does_not_contain_same_number():
    entry = {
        "num_runs": 4,
        "trained_by_paper": True,
        "num_runs_evidence": "We average repeated experiments.",
        "source_ref": "this paper",
    }

    assert _validated_run_metadata(entry) == (None, 1, None)


def test_update_result_clears_unsubstantiated_run_count():
    result = Result(
        metric_value=0.8,
        num_runs=10,
        trained_by_paper=1,
        num_runs_evidence="10 independent runs",
    )

    changed = _update_result(
        result,
        {
            "value": 0.8,
            "num_runs": 4,
            "trained_by_paper": False,
            "num_runs_evidence": "A cited paper used 4 runs.",
            "source_ref": "Smith 2024",
        },
        "extractor",
    )

    assert changed is True
    assert result.num_runs is None
    assert result.trained_by_paper == 0
    assert result.num_runs_evidence is None


def test_compact_run_metadata_expands_to_full_fields():
    expanded = _expand_compact_result_entry(
        {"m": "Ours", "d": "ZINC", "k": "MAE", "v": 0.1, "j": 4, "a": True, "g": "4 seeds"}
    )

    assert expanded["num_runs"] == 4
    assert expanded["trained_by_paper"] is True
    assert expanded["num_runs_evidence"] == "4 seeds"
