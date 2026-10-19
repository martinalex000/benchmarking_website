import hashlib
import json
from datetime import UTC, datetime, timedelta
from email.utils import format_datetime
from types import SimpleNamespace
from zoneinfo import ZoneInfo

import pytest

from backend.db import init_db, session_scope
from backend.models import Dataset, DatasetVariant, Model, Paper, RepetitionAssessment, Result
from backend.repetition_batch import RequestGate, cohort
from backend.repetition_extractor import DEFAULT_MODEL
from backend.repetition_storage import apply_assessment, paper_protocol


def analysis(counts=(10,), extra=None):
    accepted = [
        {"table_id": i, "repetitions": n, "cv_folds": None, "design": "repeated_training"}
        for i, n in enumerate(counts, 1)
    ]
    return {
        "validated": {
            "accepted": accepted,
            "coverage": {},
            "withheld": [],
            "table_outcomes": [
                {"table_id": i, "outcome": "count"} for i in range(1, len(counts) + 1)
            ]
            + (extra or []),
        }
    }


def test_uniform_and_mixed_protocols():
    assert paper_protocol(analysis((10, 10))) == ("uniform", 10)
    assert paper_protocol(analysis((10, 5))) == ("table_dependent", None)
    assert paper_protocol(analysis(extra=[{"outcome": "special"}])) == ("table_dependent", None)
    assert paper_protocol(analysis(extra=[{"outcome": "excluded"}])) == ("uniform", 10)
    assert paper_protocol({"error": "timeout"}) == ("failed", None)


@pytest.mark.parametrize(
    "design,repetitions,folds,expected",
    [
        ("repeated_cv", 10, 10, 100),
        ("single_cv", 1, 10, 10),
        ("repeated_training", 5, None, 5),
        ("nested", 10, 10, None),
    ],
)
def test_uniform_num_runs_counts_models_trained(design, repetitions, folds, expected):
    data = analysis()
    item = data["validated"]["accepted"][0]
    item.update(design=design, repetitions=repetitions, cv_folds=folds)
    assert paper_protocol(data) == ("uniform", expected)


def test_missing_table_never_uniform():
    data = analysis()
    data["validated"]["coverage"] = {"missing_table_ids": [2]}
    assert paper_protocol(data) == ("table_dependent", None)


@pytest.mark.parametrize("hour,limit", [(7, 100), (8, 4), (22, 4), (23, 100)])
def test_berlin_day_night_boundary(hour, limit):
    gate = RequestGate(
        100, now=lambda: datetime(2026, 10, 6, hour, tzinfo=ZoneInfo("Europe/Berlin"))
    )
    assert gate.limit == limit


def test_night_limit_matches_requested_worker_count():
    gate = RequestGate(10, now=lambda: datetime(2026, 10, 6, 23, tzinfo=ZoneInfo("Europe/Berlin")))
    assert gate.limit == 10


def test_rate_limit_has_shared_cooldown_and_configurable_stream_pool():
    gate = RequestGate(100, now=lambda: datetime(2026, 10, 6, 23, tzinfo=ZoneInfo("Europe/Berlin")))
    assert gate.maximum == 100
    gate.__enter__()
    error = SimpleNamespace(
        status_code=429, response=SimpleNamespace(headers={"retry-after": "90"})
    )
    gate.__exit__(None, error, None)
    assert gate.limit == 50
    assert gate.rate_limits == 1
    assert gate.active == 0
    assert gate.cooldown_until > 0


def test_default_stream_ceiling_tracks_available_papers(tmp_path, monkeypatch):
    import backend.repetition_batch as batch

    papers = [{"paper_id": f"p{i}", "title": "paper", "venue": "ICLR"} for i in range(3)]
    route = SimpleNamespace(model_id=DEFAULT_MODEL, backend=SimpleNamespace(label="primary"))
    monkeypatch.setattr(batch, "cohort", lambda _ids: papers)
    (tmp_path / "repetition_metadata.txt").write_text("facts")
    (tmp_path / "repetition_verification.txt").write_text("verify")
    monkeypatch.setattr(batch, "prepare_prompts", lambda _root: tmp_path)
    monkeypatch.setattr(batch, "external_glm_routes", lambda: {"primary": route})
    monkeypatch.setattr(
        batch,
        "preflight_external_glm",
        lambda *_args, **_kwargs: {"status": "passed", "checked_at": "now"},
    )
    observed = []

    def analyze(_paper, _root, _prompts, gate, model_route, _reuse_root, _force):
        observed.append(gate.maximum)
        assert model_route == route
        return {"status": "failed", "error": "test-only failure"}

    monkeypatch.setattr(batch, "analyze_paper", analyze)
    root = tmp_path / "batch"
    root.mkdir()

    status = batch._run_locked(root, None, False, None, None)

    assert set(observed) == {3}
    assert status["state"] == "finished_with_failures"
    assert status["completed"] == 3
    assert status["preflight_status"] == "passed"


def test_failed_preflight_stops_before_paper_calls(tmp_path, monkeypatch):
    import backend.repetition_batch as batch

    papers = [{"paper_id": "p1", "title": "paper", "venue": "ICLR"}]
    route = SimpleNamespace(model_id=DEFAULT_MODEL, backend=SimpleNamespace(label="primary"))
    monkeypatch.setattr(batch, "cohort", lambda _ids: papers)
    monkeypatch.setattr(batch, "prepare_prompts", lambda _root: tmp_path)
    monkeypatch.setattr(batch, "external_glm_routes", lambda: {"primary": route})
    monkeypatch.setattr(
        batch,
        "preflight_external_glm",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(ConnectionError("endpoint down")),
    )
    monkeypatch.setattr(
        batch,
        "analyze_paper",
        lambda *_args, **_kwargs: pytest.fail("No paper request may start after preflight failure"),
    )
    root = tmp_path / "preflight_failure"
    root.mkdir()

    state = batch._run_locked(root, None, False, None, None)

    preflight = json.loads((root / "preflight.json").read_text())["attempts"][-1]
    assert state["state"] == "preflight_failed"
    assert state["pipeline_terminal"] is True
    assert state["selected_rows_unchanged"] is True
    assert preflight["paper_calls_started"] is False
    assert "endpoint down" in preflight["error"]


def test_fresh_papers_are_split_across_independent_glm_endpoints(tmp_path, monkeypatch):
    import backend.repetition_batch as batch

    papers = [
        {"paper_id": "a", "title": "A", "venue": "ICLR"},
        {"paper_id": "b", "title": "B", "venue": "ICLR"},
    ]
    routes = {
        "primary": SimpleNamespace(
            model_id=DEFAULT_MODEL, backend=SimpleNamespace(label="primary")
        ),
        "second": SimpleNamespace(
            model_id="glm-5.3-flash", backend=SimpleNamespace(label="second")
        ),
    }
    (tmp_path / "repetition_metadata.txt").write_text("facts")
    (tmp_path / "repetition_verification.txt").write_text("verify")
    monkeypatch.setattr(batch, "cohort", lambda _ids: papers)
    monkeypatch.setattr(batch, "prepare_prompts", lambda _root: tmp_path)
    monkeypatch.setattr(batch, "external_glm_routes", lambda: routes)
    monkeypatch.setattr(
        batch,
        "preflight_external_glm",
        lambda *_args, model_route, **_kwargs: {
            "status": "passed",
            "checked_at": "now",
            "model": model_route.model_id,
        },
    )
    observed = []
    monkeypatch.setattr(
        batch,
        "analyze_paper",
        lambda paper, _root, _prompts, gate, route, _reuse, _force: (
            observed.append((paper["paper_id"], gate, route.model_id))
            or {"paper_id": paper["paper_id"], "status": "failed", "error": "test"}
        ),
    )
    root = tmp_path / "two_routes"
    root.mkdir()
    state = batch._run_locked(root, None, False, 2, 1)

    assert {item[2] for item in observed} == {DEFAULT_MODEL, "glm-5.3-flash"}
    assert observed[0][1] is not observed[1][1]
    assert state["model_assignments"] == {"primary": 1, "second": 1}
    assert state["database_applied"] is False


def test_empty_cohort_finishes_without_a_zero_stream_gate(tmp_path, monkeypatch):
    import backend.repetition_batch as batch

    monkeypatch.setattr(batch, "cohort", lambda _ids: [])
    monkeypatch.setattr(batch, "prepare_prompts", lambda _root: tmp_path)
    root = tmp_path / "empty_batch"
    root.mkdir()

    state = batch._run_locked(root, None, False, None, None)

    assert state["state"] == "finished"
    assert state["total"] == 0


def test_database_migration_and_cohort(tmp_path):
    init_db(str(tmp_path / "test.db"))
    with session_scope() as s:
        a = Paper(arxiv_id="one", title="A", venue="ICLR")
        b = Paper(arxiv_id="two", title="B", venue=" ")
        d = Dataset(name="Cora")
        v = DatasetVariant(dataset=d, name="standard")
        m = Model(name="GCN", canonical_name="gcn")
        s.add_all([a, b, v, m])
        s.flush()
        s.add_all(
            [
                Result(
                    paper_id=p.id,
                    model_id=m.id,
                    dataset_variant_id=v.id,
                    metric_name="accuracy",
                    metric_value=80,
                )
                for p in [a, b]
            ]
        )
    assert [p["paper_id"] for p in cohort()] == ["one"]
    with session_scope() as s:
        assert s.query(RepetitionAssessment).count() == 0


def test_application_preserves_copied_unknown_and_overridden_rows(tmp_path, monkeypatch):
    import backend.repetition_storage as storage

    init_db(str(tmp_path / "rows.db"))
    source = "We train OwnNet for 10 runs."
    accepted = {
        "table_id": 1,
        "name": "OwnNet",
        "role": "proposed",
        "origin": "self_evaluated",
        "repetitions": 10,
        "cv_folds": None,
        "design": "repeated_training",
        "evidence_by_purpose": {"count": [{"quote": source}]},
    }
    validated = analysis()["validated"]
    validated["accepted"] = [accepted]
    raw = {
        "provenance": {
            "model": DEFAULT_MODEL,
            "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "prompt_sha256": {"facts": "test", "verification": "test"},
        },
        "facts": {"proposed_methods": [], "tables": []},
        "verification": {"methods": []},
        "validated": validated,
    }
    monkeypatch.setattr(storage, "validate_repetitions", lambda *args: validated)
    with session_scope() as s:
        p = Paper(arxiv_id="test", title="Test", venue="ICLR")
        s.add(p)
        s.flush()
        d = Dataset(name="Cora")
        s.add(d)
        s.flush()
        for i, (name, origin, overridden) in enumerate(
            [
                ("OwnNet", "this paper", 0),
                ("CopiedNet", "Smith 2020", 0),
                ("UnknownNet", "this paper", 0),
                ("OwnNet variant", "this paper", 1),
            ]
        ):
            m = Model(name=name, canonical_name=name.lower())
            v = DatasetVariant(dataset_id=d.id, name=str(i))
            s.add_all([m, v])
            s.flush()
            s.add(
                Result(
                    paper_id=p.id,
                    model_id=m.id,
                    dataset_variant_id=v.id,
                    metric_name="acc",
                    metric_value=80,
                    source_ref=origin,
                    num_runs=3 if overridden else None,
                    is_overridden=overridden,
                )
            )
    result = apply_assessment("test", raw, source, tmp_path / "analysis.json")
    assert result["assigned"] == 1
    assert result["linked"] == 4
    with session_scope() as s:
        rows = s.query(Result).order_by(Result.id).all()
        assert [r.num_runs for r in rows] == [10, None, None, 3]
        assert [r.repetition_status for r in rows[:3]] == ["count", "copied", "unknown"]
        assert all(r.repetition_assessment_id for r in rows)
        snapshot = json.loads(s.query(RepetitionAssessment).one().payload)
        assert len(snapshot["row_update_audit"]) == 4


def test_gate_can_ramp_up_again_after_rate_limiting():
    gate = RequestGate(100, now=lambda: datetime(2026, 10, 6, 23, tzinfo=ZoneInfo("Europe/Berlin")))
    gate.night_limit = 1
    for _ in range(2):
        gate.__enter__()
        gate.__exit__(None, None, None)
    assert gate.limit == 3


def test_retry_after_blocks_the_shared_key_until_reset(monkeypatch):
    import backend.repetition_batch as batch

    clock = [100.0]
    monkeypatch.setattr(batch.time, "monotonic", lambda: clock[0])
    gate = RequestGate(100, now=lambda: datetime(2026, 10, 6, 12, tzinfo=ZoneInfo("Europe/Berlin")))
    gate.__enter__()
    error = SimpleNamespace(
        status_code=429, response=SimpleNamespace(headers={"retry-after": "90"})
    )
    gate.__exit__(None, error, None)
    assert gate.cooldown_until == 190
    assert gate.limit == 2

    def advance_to_reset(timeout):
        assert clock[0] < gate.cooldown_until
        clock[0] = gate.cooldown_until

    monkeypatch.setattr(gate.condition, "wait", advance_to_reset)
    gate.__enter__()
    assert clock[0] == 190
    gate.__exit__(None, None, None)


def test_retry_after_accepts_http_date(monkeypatch):
    import backend.repetition_batch as batch

    monkeypatch.setattr(batch.time, "monotonic", lambda: 100.0)
    retry_after = format_datetime(datetime.now(UTC) + timedelta(seconds=75))
    gate = RequestGate(100, now=lambda: datetime(2026, 10, 6, 12, tzinfo=ZoneInfo("Europe/Berlin")))
    gate.__enter__()
    error = SimpleNamespace(
        status_code=429, response=SimpleNamespace(headers={"retry-after": retry_after})
    )
    gate.__exit__(None, error, None)

    assert 160 <= gate.cooldown_until <= 180
