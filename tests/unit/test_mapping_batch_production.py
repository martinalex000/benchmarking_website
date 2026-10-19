import hashlib
import json
import sqlite3
import time
from datetime import UTC, datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

from backend.mapping import batch
from tests.unit.test_mapping_plan import prepared


def test_request_limits_follow_berlin_hours_and_configurable_pool():
    berlin = ZoneInfo("Europe/Berlin")
    models = {batch.DEFAULT_MODEL, batch.SECOND_GLM_FLASH_ROUTE}
    gate = batch.MappingGate(
        maximum=10,
        daytime_streams=5,
        now=lambda: datetime(2026, 10, 9, 12, tzinfo=berlin),
        models=models,
    )
    assert gate.limit == 55  # Five primary streams plus the second-key cap.
    gate = batch.MappingGate(
        maximum=10,
        daytime_streams=1,
        now=lambda: datetime(2026, 10, 9, 12, tzinfo=berlin),
        models=models,
    )
    assert gate.limit == 51
    gate.now = lambda: datetime(2026, 10, 9, 23, tzinfo=berlin)
    assert gate.limit == 60
    with pytest.raises(ValueError, match="maximum <= 20"):
        batch.MappingGate(maximum=250)


@pytest.mark.xfail(
    strict=True,
    reason="A shared Retry-After deadline must survive process restarts",
)
def test_resume_restores_persisted_retry_after_deadline(tmp_path, monkeypatch):
    _, root, _ = prepare_run(tmp_path, monkeypatch)
    status_path = root / "status.json"
    status = batch.read_json(status_path)
    status["retry_after_until_utc"] = (datetime.now(UTC) + timedelta(seconds=120)).isoformat()
    batch.write_json(status_path, status)
    restored_cooldowns = []

    def check_cooldown(gate):
        restored_cooldowns.append(gate.cooldown_until - time.monotonic())
        return {"status": "passed", "model": "zai-org/GLM-5.3-Flash"}

    monkeypatch.setattr(batch, "preflight_glm", check_cooldown)
    monkeypatch.setattr(
        batch,
        "analyze_chunk",
        lambda _folder, _pid, rows, *_args: [
            {**row, "action": "origin_unresolved", "proposed_num_runs": None} for row in rows
        ],
    )

    status = batch.run(root)

    assert restored_cooldowns and restored_cooldowns[0] > 0
    assert status["successful"] == 1


def prepare_run(tmp_path, monkeypatch):
    database, parent, papers, _ = prepared(tmp_path)
    monkeypatch.setattr(batch, "earlier_matches", lambda *_: [])
    (parent / "papers" / "one" / "protocol_keys.json").write_text("[]")
    root = tmp_path / "maintained_run"
    batch.prepare(root, database, papers, parent=parent, maximum=5, daytime_streams=5)
    return database, root, papers


def test_prepare_freezes_compact_verifier_prompt_and_mode(tmp_path, monkeypatch):
    database, parent, papers, _ = prepared(tmp_path)
    monkeypatch.setattr(batch, "earlier_matches", lambda *_: [])
    (parent / "papers" / "one" / "protocol_keys.json").write_text("[]")
    root = tmp_path / "compact_run"

    batch.prepare(
        root,
        parent=parent,
        database=database,
        papers=papers,
        maximum=5,
        daytime_streams=5,
        compact_verifier=True,
    )

    manifest = batch.read_json(root / "manifest.json")
    assert manifest["compact_verifier"] is True
    assert "result_mapping_delta_verification.txt" in manifest["prompt_sha256"]
    prompt = (root / "prompts" / "result_mapping_delta_verification.txt").read_text()
    assert "Do NOT re-emit the complete fact or candidate objects" in prompt
    batch.check_revision(manifest, root)


@pytest.mark.xfail(
    strict=True,
    reason="Preparing from a parent must preserve its verified scoped-out papers",
)
def test_prepare_parent_preserves_scoped_out_rows(tmp_path, monkeypatch):
    database, parent, papers, _ = prepared(tmp_path)
    monkeypatch.setattr(batch, "earlier_matches", lambda *_: [])
    (parent / "papers" / "one" / "protocol_keys.json").write_text("[]")
    parent_run = tmp_path / "parent_run"
    batch.prepare(parent_run, database, papers, parent=parent)

    with sqlite3.connect(database) as db:
        db.execute("INSERT INTO papers VALUES(2,'omitted','ICLR','2025-01-01')")
        db.execute(
            "INSERT INTO results(id,paper_id,model_id,dataset_variant_id,"
            "model_name_override,metric_name,metric_value,metric_std,table_ref,source_ref,"
            "evaluation_task,protocol_decision,protocol_note,num_runs,is_overridden) "
            "VALUES(2,2,1,1,NULL,'Accuracy',0.7,0.01,'Table 1','this paper',"
            "'node classification','standard',NULL,NULL,0)"
        )
        rows = batch.stored_rows(db, "omitted")

    source = "No result tables in the local paper."
    source_path = papers / "omitted" / "latex" / "expanded.tex"
    source_path.parent.mkdir(parents=True)
    source_path.write_text(source)
    scope_path = parent_run / "scope.json"
    scope = batch.read_json(scope_path)
    scope["candidate_papers"] += 1
    scope["excluded_papers"] = [
        {
            "paper_id": "omitted",
            "reason": "no_detected_result_tables",
            "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "rows": rows,
        }
    ]
    batch.write_json(scope_path, scope)

    child = tmp_path / "child_run"
    batch.prepare(child, database, papers, parent=parent_run)

    child_scope = batch.read_json(child / "scope.json")
    assert child_scope["candidate_papers"] == 2
    assert child_scope["excluded_papers"] == scope["excluded_papers"]


def test_batch_is_read_only_and_resume_reuses_completed_assessments(tmp_path, monkeypatch):
    database, root, _ = prepare_run(tmp_path, monkeypatch)
    before = database.read_bytes()
    calls = []
    preflights = []

    def preflight(gate):
        preflights.append(gate)
        return {"status": "passed", "model": "zai-org/GLM-5.3-Flash"}

    def analyze(folder, pid, rows, source, prompts, gate, **_options):
        calls.append(pid)
        return [
            {**r, "action": "origin_unresolved", "proposed_num_runs": None, "correction": None}
            for r in rows
        ]

    monkeypatch.setattr(batch, "preflight_glm", preflight)
    monkeypatch.setattr(batch, "analyze_chunk", analyze)
    status = batch.run(root)
    assert status["pipeline_terminal"] and status["selected_rows_unchanged"]
    assert status["successful"] == 1
    assert status["failed"] == 0
    assert database.read_bytes() == before
    assert batch.run(root)["successful"] == 1
    assert calls == ["one"]
    assert len(preflights) == 1
    assert (root / "override_counts.log").exists()


def test_assigned_deepseek_paper_uses_the_run_shared_gate(tmp_path, monkeypatch):
    _, root, _ = prepare_run(tmp_path, monkeypatch)
    manifest = batch.read_json(root / "manifest.json")
    model = "deepseek-ai/DeepSeek-V4.1-Flash"
    manifest["papers"][0]["model"] = model
    manifest["models"] = [model]
    batch.write_json(root / "manifest.json", manifest)
    preflight_gates = []
    analysis_gates = []

    def preflight(gate, selected_model):
        assert selected_model == model
        preflight_gates.append(gate)
        return {"status": "passed", "model": selected_model}

    def analyze(_folder, _pid, rows, _source, _prompts, gate, *, model, **_options):
        assert model == "deepseek-ai/DeepSeek-V4.1-Flash"
        analysis_gates.append(gate)
        return [
            {
                **row,
                "action": "origin_unresolved",
                "proposed_num_runs": None,
                "correction": None,
            }
            for row in rows
        ]

    monkeypatch.setattr(batch, "preflight_mapping_model", preflight)
    monkeypatch.setattr(batch, "analyze_chunk", analyze)

    status = batch.run(root)

    assert status["successful"] == 1
    assert status["results"]["one"]["model"] == model
    assert analysis_gates[0] is preflight_gates[0]


def test_completed_foreign_model_artifacts_are_reused_without_preflight(tmp_path, monkeypatch):
    database, _, papers, _ = prepared(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("ALTER TABLE papers ADD COLUMN title TEXT")
        db.execute("UPDATE papers SET title='One' WHERE id=1")
        db.execute(
            "INSERT INTO papers(id,arxiv_id,venue,published_date,title) "
            "VALUES(2,'two','ICML','2024-01-01','Two')"
        )
        db.execute(
            "INSERT INTO results VALUES(2,2,1,1,NULL,'Accuracy',0.81,0.003,"
            "'Table 1','this paper','node classification','standard',NULL,NULL,0)"
        )
    source = (papers / "one" / "latex" / "expanded.tex").read_text()
    second_source = papers / "two" / "latex"
    second_source.mkdir(parents=True)
    (second_source / "expanded.tex").write_text(source)

    root = tmp_path / "reused_full_artifacts"
    full_model = "zai-org/GLM-5.3"
    second_key = batch.SECOND_GLM_FLASH_ROUTE
    monkeypatch.setattr(batch, "earlier_matches", lambda *_: [])
    batch.prepare(
        root,
        database,
        papers,
        maximum=5,
        daytime_streams=5,
        model_assignments={"one": full_model},
        preferred_fact_model=second_key,
        compact_verifier=True,
    )
    reused = root / "papers" / "one"
    batch.write_json(
        reused / "assessment.json",
        {"state": "complete", "model": full_model, "errors": []},
    )
    batch.write_json(reused / "proposals.json", [])

    preflighted = []

    def preflight(_gate, model):
        preflighted.append(model)
        return {"status": "passed", "model": model}

    monkeypatch.setattr(batch, "preflight_glm", lambda gate: preflight(gate, batch.DEFAULT_MODEL))
    monkeypatch.setattr(batch, "preflight_mapping_model", preflight)
    monkeypatch.setattr(
        batch,
        "analyze_chunk",
        lambda _folder, _pid, rows, *_args, **_kwargs: [
            {
                **row,
                "action": "origin_unresolved",
                "proposed_num_runs": None,
                "correction": None,
            }
            for row in rows
        ],
    )

    status = batch.run(root)

    assert status["successful"] == 2
    assert set(preflighted) == {batch.DEFAULT_MODEL, second_key}
    assert full_model not in preflighted
    assert status["results"]["one"]["model"] == full_model


def test_default_pool_ceiling_is_the_available_paper_count(tmp_path, monkeypatch):
    database, parent, papers, _ = prepared(tmp_path)
    monkeypatch.setattr(batch, "earlier_matches", lambda *_: [])
    (parent / "papers" / "one" / "protocol_keys.json").write_text("[]")
    root = tmp_path / "default_pool_run"

    batch.prepare(root, database, papers, parent=parent)

    manifest = batch.read_json(root / "manifest.json")
    assert manifest["maximum"] == 1
    assert manifest["daytime_streams"] == 1


def test_second_key_request_budget_matches_reported_limits():
    route = batch.SECOND_GLM_FLASH_ROUTE
    assert batch.REQUEST_WINDOWS[route] == (
        (30, 14),
        (30, 60),
        (200, 3600),
        (1000, 86400),
        (3000, 2592000),
    )


def test_second_key_request_budget_waits_for_minute_quota_after_burst():
    route = batch.SECOND_GLM_FLASH_ROUTE
    gate = batch.MappingGate(maximum=5, models={route})
    gate._request_starts[route].extend([999.9] * 30)

    assert gate._request_wait_seconds(route, 1000.0) == pytest.approx(59.9)


def test_second_key_request_starts_are_saved_before_a_call_and_restored(tmp_path):
    route = batch.SECOND_GLM_FLASH_ROUTE
    state_path = tmp_path / "request_quota_starts.jsonl"
    gate = batch.MappingGate(maximum=5, models={route}, state_path=state_path)

    with gate.for_model(route):
        persisted = batch.read_request_journal(state_path)[route]
        assert len(persisted) == 1

    restored = batch.MappingGate(
        maximum=5,
        models={route},
        persisted_state={"request_starts_by_model": batch.read_request_journal(state_path)},
    )
    assert len(restored.request_starts_by_model[route]) == 1


def test_second_key_is_preferred_for_phase_one_and_available_for_verification(
    tmp_path, monkeypatch
):
    _, root, _ = prepare_run(tmp_path, monkeypatch)
    manifest = batch.read_json(root / "manifest.json")
    second_key = batch.SECOND_GLM_FLASH_ROUTE
    manifest["papers"][0]["preferred_fact_model"] = second_key
    manifest["models"] = [batch.DEFAULT_MODEL, second_key]
    batch.write_json(root / "manifest.json", manifest)
    preflighted = []
    analyzed = []

    def preflight(_gate, model):
        preflighted.append(model)
        return {"status": "passed", "model": model}

    def analyze(_folder, _pid, rows, *_args, model=batch.DEFAULT_MODEL, **options):
        analyzed.append((model, options.get("fact_model", model)))
        return [{**row, "action": "origin_unresolved", "proposed_num_runs": None} for row in rows]

    monkeypatch.setattr(batch, "preflight_glm", lambda _gate: preflight(_gate, batch.DEFAULT_MODEL))
    monkeypatch.setattr(batch, "preflight_mapping_model", preflight)
    monkeypatch.setattr(batch, "analyze_chunk", analyze)

    status = batch.run(root)

    assert status["successful"] == 1
    assert set(preflighted) == {batch.DEFAULT_MODEL, second_key}
    assert len(analyzed) == 1
    assert analyzed[0][1] == second_key
    assert analyzed[0][0] in {batch.DEFAULT_MODEL, second_key}


def test_chunk_scheduler_interleaves_large_papers_by_chunk_ordinal(tmp_path):
    papers = [
        {"paper_id": "large", "priority_rank": 1},
        {"paper_id": "small", "priority_rank": 1},
        {"paper_id": "lower_priority", "priority_rank": 2},
    ]
    rows_by_paper = {"large": 5, "small": 1, "lower_priority": 2}
    for paper in papers:
        folder = tmp_path / "papers" / paper["paper_id"]
        folder.mkdir(parents=True)
        batch.write_json(
            folder / "rows.json",
            [{"result_id": index} for index in range(rows_by_paper[paper["paper_id"]])],
        )

    tasks, counts = batch.build_chunk_tasks(papers, tmp_path, chunk_size=2)

    assert counts == {"large": 3, "small": 1, "lower_priority": 1}
    assert [(task["paper"]["paper_id"], task["chunk_index"]) for task in tasks] == [
        ("large", 0),
        ("small", 0),
        ("large", 1),
        ("large", 2),
        ("lower_priority", 0),
    ]


def test_map_results_cli_exposes_phase_one_second_key_option():
    from backend.pipeline import _build_parser

    args = _build_parser().parse_args(
        ["map-results", "--output-dir", "mapping-run", "--prefer-second-glm-key-phase1"]
    )

    assert args.prefer_second_glm_key_phase1 is True


def test_throughput_report_aggregates_last_completed_chunks_by_endpoint(tmp_path):
    chunk = tmp_path / "papers" / "paper" / "chunks" / "001"
    attempt = chunk / "facts_attempt_001"
    attempt.mkdir(parents=True)
    batch.write_json(
        chunk / "chunk_complete.json",
        {
            "paper_id": "paper",
            "chunk": "001",
            "state": "complete",
            "started_at_utc": "2026-10-14T10:00:00+00:00",
            "completed_at_utc": "2026-10-14T10:00:10+00:00",
        },
    )
    batch.write_json(
        attempt / "mapping_facts_call.json",
        {
            "endpoint": "external-glm-flash-second-key",
            "model": "glm-5.3-flash",
            "stage": "mapping_facts",
            "success": True,
            "started_at_utc": "2026-10-14T10:00:00+00:00",
            "finished_at_utc": "2026-10-14T10:00:05+00:00",
            "completion_tokens": 100,
            "tokens_per_sec": 50,
        },
    )
    batch.write_json(
        attempt / "previous_attempt_call.json",
        {
            "endpoint": "external-glm-flash-second-key",
            "model": "glm-5.3-flash",
            "stage": "mapping_facts",
            "success": True,
            "started_at_utc": "2026-10-14T09:00:00+00:00",
            "finished_at_utc": "2026-10-14T09:01:00+00:00",
            "completion_tokens": 99999,
            "tokens_per_sec": 50,
        },
    )
    (tmp_path / "request_attempts.jsonl").write_text(
        '{"endpoint":"external-glm-flash-second-key","model":"glm-5.3-flash",'
        '"chunk":"papers/paper/chunks/001"}\n'
        '{"endpoint":"external-glm-flash-second-key","model":"glm-5.3-flash",'
        '"chunk":"papers/paper/chunks/001"}\n'
    )

    batch.refresh_throughput_report(tmp_path)

    report = (tmp_path / "throughput.md").read_text()
    assert "glm-5.3-flash" in report
    assert "12.00" in report  # two requests over ten seconds
    assert "10.00" in report  # 100 completion tokens over ten seconds
    assert "50.00" in report  # weighted decode speed
    assert "Phase 1 — facts" in report and "| 1 |" in report
    assert "Saved response records in this window: 1." in report
    assert "Current limits snapshot" in report


def test_timeout_remains_failed_and_resume_preserves_earlier_failure(tmp_path, monkeypatch):
    _, root, _ = prepare_run(tmp_path, monkeypatch)
    monkeypatch.setattr(
        batch,
        "preflight_glm",
        lambda _gate: {"status": "passed", "model": "zai-org/GLM-5.3-Flash"},
    )

    def fail(*args, **_kwargs):
        raise TimeoutError("Provider timed out")

    monkeypatch.setattr(batch, "analyze_chunk", fail)
    status = batch.run(root)
    assert status["failed"] == 1 and status["successful"] == 0
    assert status["results"]["one"]["errors"]
    monkeypatch.setattr(
        batch,
        "analyze_chunk",
        lambda folder, pid, rows, *args, **_kwargs: [
            {**r, "action": "origin_unresolved", "proposed_num_runs": None} for r in rows
        ],
    )
    assert batch.run(root)["successful"] == 1
    assert list((root / "papers" / "one" / "history").glob("*/assessment.json"))


@pytest.mark.xfail(
    strict=True,
    reason="Transient paper failures should be retried within the same batch run",
)
def test_transient_timeout_retried_inside_same_batch(tmp_path, monkeypatch):
    _, root, _ = prepare_run(tmp_path, monkeypatch)
    monkeypatch.setattr(
        batch,
        "preflight_glm",
        lambda _gate: {"status": "passed", "model": "zai-org/GLM-5.3-Flash"},
    )
    calls = 0

    def timeout_once(_folder, _pid, rows, *_args, **_kwargs):
        nonlocal calls
        calls += 1
        if calls == 1:
            raise TimeoutError("Transient provider timeout")
        return [{**row, "action": "origin_unresolved", "proposed_num_runs": None} for row in rows]

    monkeypatch.setattr(batch, "analyze_chunk", timeout_once)
    status = batch.run(root)

    assert calls == 2
    assert status["successful"] == 1
    assert status["failed"] == 0


def test_resume_reuses_chunk_saved_before_paper_assessment(tmp_path, monkeypatch):
    database, root, _ = prepare_run(tmp_path, monkeypatch)
    before = database.read_bytes()
    monkeypatch.setattr(
        batch,
        "preflight_glm",
        lambda _gate: {"status": "passed", "model": "zai-org/GLM-5.3-Flash"},
    )
    calls = []

    def save_then_fail(folder, _pid, rows, *_args, **_kwargs):
        calls.append("interrupted")
        folder.mkdir(parents=True, exist_ok=True)
        proposals = [
            {
                **row,
                "action": "origin_unresolved",
                "proposed_num_runs": None,
                "correction": None,
            }
            for row in rows
        ]
        (folder / "proposals.json").write_text(json.dumps(proposals))
        raise TimeoutError("Power loss after chunk output was saved")

    monkeypatch.setattr(batch, "analyze_chunk", save_then_fail)
    first = batch.run(root)
    assert first["failed"] == 1

    def unexpected_model_call(*_args, **_kwargs):
        calls.append("unexpected retry")
        raise AssertionError("A valid saved chunk should be reused")

    monkeypatch.setattr(batch, "analyze_chunk", unexpected_model_call)
    resumed = batch.run(root)

    assert resumed["successful"] == 1
    assert resumed["failed"] == 0
    assert calls == ["interrupted"]
    assert database.read_bytes() == before


def test_resume_replays_cached_chunk_with_candidate_coverage_failure(tmp_path, monkeypatch):
    _, root, _ = prepare_run(tmp_path, monkeypatch)
    paper = root / "papers" / "one"
    rows = batch.read_json(paper / "rows.json")
    chunk = paper / "chunks" / "001"
    chunk.mkdir(parents=True)
    batch.write_json(
        chunk / "proposals.json",
        [
            {
                **rows[0],
                "action": "targeted_validation_unresolved",
                "proposed_num_runs": None,
                "correction": None,
                "validation_errors": ["same_experiment_candidate_omitted"],
            }
        ],
    )
    monkeypatch.setattr(
        batch,
        "preflight_glm",
        lambda _gate: {"status": "passed", "model": "zai-org/GLM-5.3-Flash"},
    )
    calls = []

    def reanalyze(folder, _pid, subset, *_args, **_kwargs):
        calls.append("replayed")
        result = [
            {
                **row,
                "action": "origin_unresolved",
                "proposed_num_runs": None,
                "correction": None,
            }
            for row in subset
        ]
        batch.write_json(folder / "proposals.json", result)
        return result

    monkeypatch.setattr(batch, "analyze_chunk", reanalyze)
    status = batch.run(root)

    assert calls == ["replayed"]
    assert status["successful"] == 1
    assert list(chunk.glob("invalid_proposals_*.json"))


def test_successful_resume_still_rejects_changed_local_source(tmp_path, monkeypatch):
    _, root, papers = prepare_run(tmp_path, monkeypatch)
    monkeypatch.setattr(
        batch,
        "preflight_glm",
        lambda _gate: {"status": "passed", "model": "zai-org/GLM-5.3-Flash"},
    )
    monkeypatch.setattr(
        batch,
        "analyze_chunk",
        lambda folder, pid, rows, *args, **_kwargs: [
            {**r, "action": "origin_unresolved", "proposed_num_runs": None} for r in rows
        ],
    )
    batch.run(root)
    (papers / "one" / "latex" / "expanded.tex").write_text("Changed source")
    with pytest.raises(ValueError, match="Local LaTeX changed"):
        batch.run(root)


def test_unreachable_glm_stops_before_paper_calls_and_records_failure(tmp_path, monkeypatch):
    database, root, _ = prepare_run(tmp_path, monkeypatch)
    before = database.read_bytes()

    def fail(_gate):
        raise ConnectionError("endpoint unavailable")

    monkeypatch.setattr(batch, "preflight_glm", fail)
    monkeypatch.setattr(
        batch,
        "analyze_chunk",
        lambda *_args: pytest.fail("Paper calls must not start after failed preflight"),
    )

    with pytest.raises(RuntimeError, match="no paper calls were started"):
        batch.run(root)

    preflight = batch.read_json(root / "preflight.json")["attempts"][-1]
    assert preflight["status"] == "failed"
    assert preflight["paper_calls_started"] is False
    assert "endpoint unavailable" in preflight["error"]
    assert batch.read_json(root / "status.json")["state"] == "preflight_failed"
    assert not (root / "papers" / "one" / "assessment.json").exists()
    assert database.read_bytes() == before


def test_map_results_command_never_initializes_database(monkeypatch):
    from backend import pipeline

    monkeypatch.setattr(
        pipeline, "init_db", lambda: pytest.fail("Read-only command initialized DB")
    )
    monkeypatch.setattr(pipeline, "stage_result_mapping", lambda args: True)
    assert pipeline.main(["map-results", "--output-dir", "unused", "--prepare-only"]) == 0
