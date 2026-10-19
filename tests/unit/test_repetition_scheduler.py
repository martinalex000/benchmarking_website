import csv
import json

from backend.repetition_chunks import connect
from backend.repetition_scheduler import _claim_phase, _update_throughput_graph


def make_queue(path, ready_chunks, phase1_queued=False):
    with connect(path) as db:
        db.executescript(
            """
            CREATE TABLE papers (
                paper_id TEXT PRIMARY KEY,
                status TEXT,
                updated_at TEXT,
                route_label TEXT,
                route_model TEXT
            );
            CREATE TABLE chunks (
                paper_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                table_ids_json TEXT NOT NULL,
                status TEXT NOT NULL,
                attempts INTEGER NOT NULL DEFAULT 0,
                worker_id TEXT,
                lease_until TEXT,
                output_path TEXT,
                error TEXT,
                updated_at TEXT NOT NULL,
                PRIMARY KEY (paper_id, chunk_index)
            );
            CREATE TABLE phase_tasks (
                paper_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                phase INTEGER NOT NULL,
                status TEXT NOT NULL,
                attempts INTEGER NOT NULL DEFAULT 0,
                worker_id TEXT,
                lease_until TEXT,
                output_path TEXT,
                route_label TEXT,
                model_id TEXT,
                error TEXT,
                updated_at TEXT NOT NULL,
                PRIMARY KEY (paper_id, chunk_index, phase)
            );
            CREATE TABLE scheduler_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            """
        )
        for index in range(ready_chunks + int(phase1_queued)):
            phase1_status = "complete" if index < ready_chunks else "queued"
            phase2_status = "queued" if index < ready_chunks else "blocked"
            db.execute(
                "INSERT INTO papers VALUES (?, 'queued', 'now', NULL, NULL)",
                (f"paper-{index}",),
            )
            db.execute(
                "INSERT INTO chunks VALUES (?, 0, ?, 'queued', 0, NULL, NULL, NULL, NULL, 'now')",
                (f"paper-{index}", json.dumps([index + 1])),
            )
            for phase, status in ((1, phase1_status), (2, phase2_status)):
                db.execute(
                    "INSERT INTO phase_tasks VALUES (?, 0, ?, ?, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'now')",
                    (f"paper-{index}", phase, status),
                )


def ready_phase2_count(path):
    with connect(path) as db:
        return db.execute(
            "SELECT COUNT(*) FROM phase_tasks WHERE phase=2 AND status='queued'"
        ).fetchone()[0]


def test_phase2_preserve_keeps_thirty_ready_chunks_while_phase1_runs(tmp_path):
    database = tmp_path / "queue.sqlite3"
    make_queue(database, ready_chunks=31, phase1_queued=True)

    first = _claim_phase(database, "worker-a", "phase2", 4)
    assert first["phase"] == 2
    assert ready_phase2_count(database) == 30

    second = _claim_phase(database, "worker-b", "phase2", 4)
    assert second["phase"] == 1
    assert ready_phase2_count(database) == 30

    assert _claim_phase(database, "worker-c", "phase2", 4) is None
    assert ready_phase2_count(database) == 30


def test_phase2_aggressive_waits_for_thirty_then_can_spend_reserve(tmp_path):
    database = tmp_path / "queue.sqlite3"
    make_queue(database, ready_chunks=29, phase1_queued=True)

    first = _claim_phase(database, "worker-a", "phase2-aggressive", 4)
    assert first["phase"] == 1
    assert ready_phase2_count(database) == 29

    with connect(database) as db:
        db.execute("UPDATE phase_tasks SET status='complete' WHERE paper_id='paper-29' AND phase=1")
        db.execute("UPDATE phase_tasks SET status='queued' WHERE paper_id='paper-29' AND phase=2")
    first_phase2 = _claim_phase(database, "worker-b", "phase2-aggressive", 4)
    assert first_phase2["phase"] == 2
    assert ready_phase2_count(database) == 29

    next_phase2 = _claim_phase(database, "worker-c", "phase2-aggressive", 4)
    assert next_phase2["phase"] == 2
    with connect(database) as db:
        assert (
            db.execute("SELECT value FROM scheduler_meta WHERE key='phase2_unlocked'").fetchone()[0]
            == "1"
        )


def test_phase_affinity_is_independent_and_tail_chunks_can_be_stolen(tmp_path):
    database = tmp_path / "queue.sqlite3"
    make_queue(database, ready_chunks=1)
    with connect(database) as db:
        db.execute("UPDATE phase_tasks SET status='queued' WHERE paper_id='paper-0' AND phase=1")
        db.execute("UPDATE phase_tasks SET status='blocked' WHERE paper_id='paper-0' AND phase=2")
        db.execute(
            "INSERT INTO chunks VALUES ('paper-0', 1, '[2]', 'queued', 0, NULL, NULL, NULL, NULL, 'now')"
        )
        for phase, status in ((1, "queued"), (2, "blocked")):
            db.execute(
                "INSERT INTO phase_tasks VALUES ('paper-0', 1, ?, ?, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'now')",
                (phase, status),
            )

    first = _claim_phase(database, "worker-a", "phase1", 4, "primary", "model-a")
    assert (first["paper_id"], first["chunk_index"], first["phase"]) == ("paper-0", 0, 1)
    with connect(database) as db:
        affinity = db.execute(
            "SELECT endpoint,model_id FROM phase_routes WHERE paper_id='paper-0' AND phase=1"
        ).fetchone()
    assert tuple(affinity) == ("primary", "model-a")
    assert _claim_phase(database, "worker-b", "phase1", 4, "second", "model-b") is None

    # Once one task is left in the active tail, a different route may help clear it.
    tail = _claim_phase(
        database,
        "worker-b",
        "phase1",
        4,
        "second",
        "model-b",
        active_worker_slots=2,
    )
    assert (tail["paper_id"], tail["chunk_index"], tail["phase"]) == ("paper-0", 1, 1)

    with connect(database) as db:
        db.execute("UPDATE phase_tasks SET status='complete' WHERE paper_id='paper-0' AND phase=1")
        db.execute("UPDATE phase_tasks SET status='queued' WHERE paper_id='paper-0' AND phase=2")
    phase2 = _claim_phase(database, "worker-c", "phase2-aggressive", 4, "second", "model-b")
    assert (phase2["paper_id"], phase2["phase"]) == ("paper-0", 2)
    with connect(database) as db:
        routes = {
            row["phase"]: (row["endpoint"], row["model_id"])
            for row in db.execute(
                "SELECT phase,endpoint,model_id FROM phase_routes WHERE paper_id='paper-0'"
            )
        }
    assert routes == {1: ("primary", "model-a"), 2: ("second", "model-b")}


def test_throughput_graph_uses_wall_clock_bins_per_endpoint(tmp_path):
    database = tmp_path / "queue.sqlite3"
    with connect(database) as db:
        db.execute(
            """CREATE TABLE throughput_events (
                id INTEGER PRIMARY KEY,
                completed_at TEXT,
                endpoint TEXT,
                model_id TEXT,
                phase INTEGER,
                paper_id TEXT,
                chunk_index INTEGER,
                prompt_tokens INTEGER,
                completion_tokens INTEGER
            )"""
        )
        db.executemany(
            """INSERT INTO throughput_events VALUES (?, ?, ?, 'glm', 1, 'paper', 0, ?, ?)""",
            [
                (1, "2026-10-16T10:00:10+00:00", "primary", 60, 60),
                (2, "2026-10-16T10:02:10+00:00", "second", 30, 30),
            ],
        )

    _update_throughput_graph(tmp_path, database)

    with (tmp_path / "throughput.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert [row["endpoint"] for row in rows] == [
        "primary",
        "second",
        "primary",
        "second",
        "primary",
        "second",
    ]
    assert [float(row["tokens_per_second"]) for row in rows] == [2, 0, 0, 0, 0, 1]
    assert (tmp_path / "throughput.png").is_file()
    report = (tmp_path / "throughput.md").read_text()
    assert "Throughput by endpoint and model" in report
    assert "| primary | glm | 1 | 60 | 60 |" in report
    assert "| second | glm | 1 | 30 | 30 |" in report
