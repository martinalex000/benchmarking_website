import json

from experiments.table_provenance_experiment.supervise_assignment_retries import (
    progress,
    reset_timeouts,
    timeout_failure,
)


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


def test_timeout_retry_does_not_loop_on_exhausted_reasoning_budget():
    assessment = {"state": "failed", "errors": [{"error": "Request timed out."}]}
    assert timeout_failure(assessment)
    assessment["errors"].append({"error": "Reasoning exhausted the completion budget"})
    assert not timeout_failure(assessment)
    assert not timeout_failure({"state": "complete", "errors": []})


def test_retry_progress_excludes_previously_successful_papers(tmp_path):
    save(
        tmp_path / "papers/failed/assessment.json",
        {
            "state": "failed",
            "errors": [{"error": "Request timed out."}],
        },
    )
    states = progress(
        tmp_path,
        {"retry_paper_ids": ["failed", "active"]},
        {
            "active_papers": ["active"],
        },
    )
    assert states == {"failed": "pending_timeout_retry", "active": "running"}
    assert json.loads((tmp_path / "retry_status.json").read_text())["completed"] == 0


def test_reset_preserves_failed_assessment_and_valid_chunk_cache(tmp_path):
    folder = tmp_path / "papers/failed"
    save(folder / "assessment.json", {"state": "failed"})
    save(folder / "chunks/001/facts.json", {"valid": True})
    save(
        tmp_path / "status.json",
        {
            "completed": 50,
            "pipeline_terminal": True,
            "results": {"failed": {"state": "failed"}},
        },
    )
    reset_timeouts(tmp_path, ["failed"], 1)
    assert not (folder / "assessment.json").exists()
    assert (tmp_path / "attempt_history/round_001/failed/assessment.json").exists()
    assert (folder / "chunks/001/facts.json").exists()
    status = json.loads((tmp_path / "status.json").read_text())
    assert status["completed"] == 49
    assert status["pipeline_terminal"] is False
