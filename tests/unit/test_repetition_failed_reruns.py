import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, BoundedSemaphore, Lock

from experiments.table_provenance_experiment import rerun_failed_cases
from experiments.table_provenance_experiment.rerun_failed_cases import failed_record


def test_reruns_transport_failure_and_wrong_accepted_claim():
    assert failed_record({"state": "call_failure"})
    assert failed_record({"state": "complete", "stage_scores": {"current_guards": {"wrong": 1}}})


def test_reruns_missing_supported_count_and_uncredited_coverage_case():
    assert failed_record(
        {
            "state": "complete",
            "targets": [{"correct_positive": False, "supported_abstention": False}],
        }
    )


def test_does_not_rerun_an_already_successful_paper():
    assert not failed_record(
        {
            "state": "complete",
            "targets": [
                {"correct_positive": True, "supported_abstention": False},
                {"correct_positive": False, "supported_abstention": True},
            ],
        }
    )


def test_thinking_variants_share_two_slots_while_other_model_runs_concurrently(
    tmp_path, monkeypatch
):
    source = tmp_path / "source.tex"
    source.write_text("Test source")
    papers = {pid: {"path": source} for pid in ("one", "two")}
    shared = Barrier(4)
    lock = Lock()
    active = {"model-a": 0, "model-b": 0}
    started = {"model-a": 0, "model-b": 0}
    maxima = {"model-a": 0, "model-b": 0, "total": 0}

    def fake_run_paper(*args, model, **kwargs):
        with lock:
            active[model] += 1
            started[model] += 1
            wait = started[model] <= 2
            maxima[model] = max(maxima[model], active[model])
            maxima["total"] = max(maxima["total"], sum(active.values()))
        if wait:
            shared.wait(timeout=5)
        with lock:
            active[model] -= 1
        return {"error": None}

    monkeypatch.setattr(rerun_failed_cases, "run_paper", fake_run_paper)
    slots = {model: BoundedSemaphore(2) for model in active}
    jobs = []
    for label, model in (("a-low", "model-a"), ("a-thinking", "model-a"), ("b", "model-b")):
        previous = tmp_path / f"{label}.json"
        previous.write_text(
            json.dumps(
                {
                    "provenance": {
                        "model": model,
                        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                    }
                }
            )
        )
        jobs.append((label, dict.fromkeys(papers, previous)))
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [
            pool.submit(rerun_failed_cases.run_configuration, label, old, papers, tmp_path, slots)
            for label, old in jobs
        ]
        results = [future.result() for future in futures]
    assert all(not result["worker_errors"] for result in results)
    assert maxima == {"model-a": 2, "model-b": 2, "total": 4}
