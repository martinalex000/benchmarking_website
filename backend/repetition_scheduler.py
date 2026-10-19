"""Multi-process, two-phase repetition scheduler backed by the chunk SQLite queue."""

from __future__ import annotations

import csv
import hashlib
import json
import logging
import os
import signal
import sqlite3
import sys
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import asdict
from datetime import UTC, datetime, timedelta
from pathlib import Path
from threading import Event, Lock, Thread
from uuid import uuid4

from backend.llm_backends import ModelRoute
from backend.llm_tasks import LLMExtractor
from backend.repetition_batch import RequestGate, write_json
from backend.repetition_chunks import (
    FACTS_PROMPT,
    LEASE_SECONDS,
    MAX_COMPLETION_TOKENS,
    MAX_TOTAL_TOKENS,
    REQUEST_TIMEOUT_SECONDS,
    VERIFY_PROMPT,
    _aggregate_ready_papers,
    _chunk_path,
    _now,
    connect,
    overview,
    queue_database_path,
)
from backend.repetition_extractor import preflight_external_glm, repetition_input
from backend.repetition_metadata import RepetitionFacts, Verification, table_inventory

logger = logging.getLogger(__name__)
PHASE_STRATEGIES = ("phase1", "phase2", "phase2-aggressive")
PHASE2_RESERVE = 30


def prepare_phase_queue(root: Path) -> dict:
    """Add durable phase tasks to a prepared or existing chunk queue."""
    database = queue_database_path(root)
    if not database.is_file():
        raise FileNotFoundError(f"No chunk queue at {database}; prepare it first")
    legacy_lock_path = root / "scheduler.lock"
    if legacy_lock_path.is_file():
        import fcntl

        with legacy_lock_path.open("a") as legacy_lock:
            try:
                fcntl.flock(legacy_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise RuntimeError("The paper-chunk scheduler is still using this queue") from None
            fcntl.flock(legacy_lock, fcntl.LOCK_UN)
    now = _now()
    with connect(database) as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS phase_tasks (
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
                PRIMARY KEY (paper_id, chunk_index, phase),
                FOREIGN KEY (paper_id, chunk_index)
                    REFERENCES chunks(paper_id, chunk_index)
            );
            CREATE INDEX IF NOT EXISTS idx_phase_queue ON phase_tasks(status, phase, paper_id);
            CREATE TABLE IF NOT EXISTS phase_routes (
                paper_id TEXT NOT NULL,
                phase INTEGER NOT NULL,
                endpoint TEXT NOT NULL,
                model_id TEXT NOT NULL,
                assigned_at TEXT NOT NULL,
                PRIMARY KEY (paper_id, phase)
            );
            CREATE TABLE IF NOT EXISTS throughput_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                completed_at TEXT NOT NULL,
                endpoint TEXT NOT NULL,
                model_id TEXT NOT NULL,
                phase INTEGER NOT NULL,
                paper_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                prompt_tokens INTEGER NOT NULL,
                completion_tokens INTEGER NOT NULL,
                started_at TEXT,
                duration_seconds REAL
            );
            CREATE TABLE IF NOT EXISTS scheduler_meta (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            """
        )
        event_columns = {row["name"] for row in db.execute("PRAGMA table_info(throughput_events)")}
        for name, sql_type in (("started_at", "TEXT"), ("duration_seconds", "REAL")):
            if name not in event_columns:
                db.execute(f"ALTER TABLE throughput_events ADD COLUMN {name} {sql_type}")
        db.execute("BEGIN IMMEDIATE")
        db.execute(
            """INSERT OR IGNORE INTO phase_routes
               (paper_id,phase,endpoint,model_id,assigned_at)
               SELECT paper_id,phase,route_label,model_id,MIN(updated_at)
               FROM phase_tasks
               WHERE route_label IS NOT NULL AND model_id IS NOT NULL
               GROUP BY paper_id,phase"""
        )
        paper_columns = {row["name"] for row in db.execute("PRAGMA table_info(papers)")}
        if "route_label" not in paper_columns:
            db.execute("ALTER TABLE papers ADD COLUMN route_label TEXT")
        if "route_model" not in paper_columns:
            db.execute("ALTER TABLE papers ADD COLUMN route_model TEXT")
        chunks = db.execute("SELECT * FROM chunks").fetchall()
        for chunk in chunks:
            exists = db.execute(
                "SELECT 1 FROM phase_tasks WHERE paper_id=? AND chunk_index=? LIMIT 1",
                (chunk["paper_id"], chunk["chunk_index"]),
            ).fetchone()
            if exists:
                continue
            complete = chunk["status"] == "complete"
            db.execute(
                "INSERT INTO phase_tasks VALUES (?, ?, 1, ?, 0, NULL, NULL, ?, NULL, NULL, NULL, ?)",
                (
                    chunk["paper_id"],
                    chunk["chunk_index"],
                    "complete" if complete else "queued",
                    chunk["output_path"] if complete else None,
                    now,
                ),
            )
            db.execute(
                "INSERT INTO phase_tasks VALUES (?, ?, 2, ?, 0, NULL, NULL, ?, NULL, NULL, NULL, ?)",
                (
                    chunk["paper_id"],
                    chunk["chunk_index"],
                    "complete" if complete else "blocked",
                    chunk["output_path"] if complete else None,
                    now,
                ),
            )
        db.execute(
            "UPDATE phase_tasks SET status='queued',worker_id=NULL,lease_until=NULL,updated_at=? "
            "WHERE status='running' AND (lease_until IS NULL OR lease_until < ?)",
            (now, now),
        )
        db.execute(
            "UPDATE chunks SET status='queued',worker_id=NULL,lease_until=NULL,updated_at=? "
            "WHERE status='running' AND (lease_until IS NULL OR lease_until < ?)",
            (now, now),
        )
    _update_throughput_graph(root, database)
    return overview(root)


def run_endpoint(
    root: Path,
    *,
    endpoint: str,
    route: ModelRoute,
    concurrency: int | str,
    strategy: str,
    max_attempts: int = 4,
) -> dict:
    """Run one endpoint/model process; sibling processes share the SQLite queue."""
    if endpoint not in {"primary", "second"}:
        raise ValueError("endpoint must be primary or second")
    auto_max = concurrency == "max"
    if not auto_max and (not isinstance(concurrency, int) or concurrency < 1):
        raise ValueError("concurrency must be a positive integer or 'max'")
    if auto_max and endpoint != "second":
        raise ValueError("--concurrency max is currently supported for endpoint=second only")
    if max_attempts < 1:
        raise ValueError("concurrency and max_attempts must be positive")
    if strategy not in PHASE_STRATEGIES:
        raise ValueError(f"strategy must be one of {', '.join(PHASE_STRATEGIES)}")
    prepare_phase_queue(root)
    database = queue_database_path(root)
    import fcntl

    lock_name = hashlib.sha256(f"{endpoint}\0{route.model_id}".encode()).hexdigest()[:20]
    route_lock_path = root / "route_locks" / f"{lock_name}.lock"
    route_lock_path.parent.mkdir(parents=True, exist_ok=True)
    route_lock = route_lock_path.open("a")
    try:
        fcntl.flock(route_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        route_lock.close()
        raise RuntimeError(
            f"A worker already runs for endpoint={endpoint}, model={route.model_id}"
        ) from None
    maximum = 100 if auto_max else concurrency
    gate = RequestGate(
        maximum=maximum,
        daytime_streams=maximum,
        enforce_rate_limits=auto_max,
        shared_rate_path=root / "key2_request_starts.json" if auto_max else None,
        last_429_path=root / "last_429.json",
    )
    preflight = preflight_external_glm(
        gate,
        max_total_tokens=MAX_TOTAL_TOKENS,
        timeout=REQUEST_TIMEOUT_SECONDS,
        model_route=route,
    )
    if auto_max:
        concurrency = gate.recommended_maximum(timeout_seconds=REQUEST_TIMEOUT_SECONDS)
        gate.set_maximum(concurrency)
        if gate.rate_limit_summary:
            thread_label = "thread" if concurrency == 1 else "threads"
            logger.info(
                "Rate-aware concurrency for %s/%s: %s %s; advertised request limits %s",
                endpoint,
                route.model_id,
                concurrency,
                thread_label,
                gate.rate_limit_summary,
            )
        else:
            logger.warning(
                "No request-per-time-window limits were reported for key2; using %s threads "
                "with adaptive 429 backoff",
                concurrency,
            )
    worker_id = f"{endpoint}-{route.model_id}-{os.getpid()}-{uuid4().hex[:8]}"
    state_path = root / "workers" / f"{worker_id}.json"
    drain_path = state_path.with_suffix(".drain")
    state_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(
        state_path,
        {
            "state": "running",
            "worker_id": worker_id,
            "pid": os.getpid(),
            "endpoint": endpoint,
            "model": route.model_id,
            "concurrency": concurrency,
            "strategy": strategy,
            "concurrency_mode": "max" if auto_max else "fixed",
            "rate_window_limits": gate.rate_limit_summary,
            "rate_limits": gate.rate_limits,
            "preflight": preflight,
            "started_at": datetime.now(UTC).isoformat(),
        },
    )
    stop = Event()
    drain_requested = Event()
    aggregation_lock = Lock()
    finished = Lock()
    active_lock = Lock()
    progress_lock = Lock()
    active_chunks = 0
    finished_count = 0
    failed_count = 0

    def worker(index: int) -> None:
        nonlocal active_chunks, finished_count, failed_count
        thread_id = f"{worker_id}-{index + 1:02d}"
        while not stop.is_set():
            if drain_path.exists():
                drain_requested.set()
                return
            task = _claim_phase(
                database,
                thread_id,
                strategy,
                max_attempts,
                endpoint,
                route.model_id,
                active_worker_slots=_active_worker_slots(root),
            )
            if task is None:
                if not _has_pending_or_active_work(database):
                    return
                stop.wait(1)
                continue
            task_started = time.monotonic()
            with active_lock:
                active_chunks += 1
            lease_stop = Event()
            lease_heartbeat = Thread(
                target=_renew_phase_lease,
                args=(database, task, thread_id, lease_stop),
                daemon=True,
            )
            lease_heartbeat.start()
            outcome = "complete"
            prompt_tokens = completion_tokens = None
            try:
                result = _process_phase(root, task, route, gate)
                calls = result.get("calls", [])
                prompt_tokens = sum(int(call.get("prompt_tokens") or 0) for call in calls)
                completion_tokens = sum(int(call.get("completion_tokens") or 0) for call in calls)
                output_path = _chunk_path(root, task["paper_id"], task["chunk_index"])
                output_path.mkdir(parents=True, exist_ok=True)
                phase_path = output_path / f"phase{task['phase']}.json"
                write_json(phase_path, result)
                _complete_phase(
                    root,
                    database,
                    task,
                    phase_path,
                    endpoint,
                    route.model_id,
                    result.get("calls", []),
                )
                if task["phase"] == 2:
                    with aggregation_lock:
                        _aggregate_papers_across_processes(root, [task["paper_id"]])
                with finished:
                    finished_count += 1
                    write_json(
                        state_path,
                        {
                            "state": "draining" if stop.is_set() else "running",
                            "worker_id": worker_id,
                            "pid": os.getpid(),
                            "endpoint": endpoint,
                            "model": route.model_id,
                            "concurrency": concurrency,
                            "concurrency_mode": "max" if auto_max else "fixed",
                            "rate_window_limits": gate.rate_limit_summary,
                            "strategy": strategy,
                            "completed_tasks": finished_count,
                            "active_requests": gate.active,
                            "request_limit": gate.limit,
                            "rate_limits": gate.rate_limits,
                            "updated_at": datetime.now(UTC).isoformat(),
                        },
                    )
                _update_throughput_graph(root, database)
            except Exception as exc:
                outcome = "failed"
                _fail_phase(
                    database,
                    task,
                    f"{type(exc).__name__}: {exc}",
                    max_attempts,
                )
                with finished:
                    failed_count += 1
                    write_json(
                        state_path,
                        {
                            "state": "draining" if stop.is_set() else "running",
                            "worker_id": worker_id,
                            "pid": os.getpid(),
                            "endpoint": endpoint,
                            "model": route.model_id,
                            "concurrency": concurrency,
                            "concurrency_mode": "max" if auto_max else "fixed",
                            "rate_window_limits": gate.rate_limit_summary,
                            "strategy": strategy,
                            "completed_tasks": finished_count,
                            "failed_attempts": failed_count,
                            "active_requests": gate.active,
                            "request_limit": gate.limit,
                            "rate_limits": gate.rate_limits,
                            "updated_at": datetime.now(UTC).isoformat(),
                        },
                    )
                logger.exception(
                    "Phase %s failed for %s/%03d",
                    task["phase"],
                    task["paper_id"],
                    task["chunk_index"] + 1,
                )
            finally:
                lease_stop.set()
                lease_heartbeat.join()
                with active_lock:
                    active_chunks -= 1
                _log_task_completion(
                    root,
                    database,
                    endpoint,
                    route.model_id,
                    task,
                    outcome,
                    prompt_tokens,
                    completion_tokens,
                    time.monotonic() - task_started,
                    gate.rate_limit_summary if auto_max else None,
                    progress_lock,
                )

    pool = ThreadPoolExecutor(max_workers=concurrency)
    futures = [pool.submit(worker, index) for index in range(concurrency)]
    pending = set(futures)
    draining = False
    interrupt_count = 0

    def handle_interrupt(_signum, _frame) -> None:
        nonlocal interrupt_count
        interrupt_count += 1
        if interrupt_count == 1:
            drain_requested.set()
            os.write(
                2,
                b"\nCtrl+C received: draining active chunks. Press Ctrl+C again to hard-exit.\n",
            )
            return
        os.write(
            2,
            b"\nSecond Ctrl+C: hard exit. Active chunk leases remain until they expire.\n",
        )
        os._exit(130)

    previous_sigint_handler = signal.signal(signal.SIGINT, handle_interrupt)
    try:
        while pending:
            if drain_path.exists():
                drain_requested.set()
            if drain_requested.is_set() and not draining:
                draining = True
                stop.set()
                logger.info(
                    "Draining %s/%s: no new chunks will be claimed", endpoint, route.model_id
                )
                with active_lock:
                    active_count = active_chunks
                with finished:
                    write_json(
                        state_path,
                        {
                            "state": "draining",
                            "worker_id": worker_id,
                            "pid": os.getpid(),
                            "endpoint": endpoint,
                            "model": route.model_id,
                            "concurrency": concurrency,
                            "concurrency_mode": "max" if auto_max else "fixed",
                            "strategy": strategy,
                            "rate_window_limits": gate.rate_limit_summary,
                            "completed_tasks": finished_count,
                            "active_chunks": active_count,
                            "started_at": datetime.now(UTC).isoformat(),
                        },
                    )
            completed_futures, pending = wait(pending, timeout=1, return_when=FIRST_COMPLETED)
            for future in completed_futures:
                future.result()
            if draining:
                with active_lock:
                    remaining = active_chunks
                progress = (
                    f"Draining {endpoint}/{route.model_id}: {remaining} chunk(s) still running"
                )
                with progress_lock:
                    if sys.stdout.isatty():
                        sys.stdout.write(f"\r{progress}")
                        sys.stdout.flush()
                    else:
                        print(progress, flush=True)
                with finished:
                    write_json(
                        state_path,
                        {
                            "state": "draining",
                            "worker_id": worker_id,
                            "pid": os.getpid(),
                            "endpoint": endpoint,
                            "model": route.model_id,
                            "concurrency": concurrency,
                            "concurrency_mode": "max" if auto_max else "fixed",
                            "strategy": strategy,
                            "rate_window_limits": gate.rate_limit_summary,
                            "completed_tasks": finished_count,
                            "active_chunks": remaining,
                            "updated_at": datetime.now(UTC).isoformat(),
                        },
                    )
        if draining:
            with progress_lock:
                if sys.stdout.isatty():
                    sys.stdout.write("\r\033[K")
                print("Draining complete: 0 chunk(s) still running.", flush=True)
    except KeyboardInterrupt:
        stop.set()
        pool.shutdown(wait=True, cancel_futures=True)
        _release_phase_leases(database, worker_id)
        write_json(state_path, {"state": "interrupted", "worker_id": worker_id})
        raise
    else:
        pool.shutdown(wait=True)
    finally:
        signal.signal(signal.SIGINT, previous_sigint_handler)
    write_json(
        state_path,
        {
            "state": "drained" if draining else "finished",
            "worker_id": worker_id,
            "endpoint": endpoint,
            "model": route.model_id,
            "concurrency_mode": "max" if auto_max else "fixed",
            "rate_window_limits": gate.rate_limit_summary,
            "completed_tasks": finished_count,
            "finished_at": datetime.now(UTC).isoformat(),
        },
    )
    drain_path.unlink(missing_ok=True)
    return overview(root)


def _has_pending_or_active_work(database: Path) -> bool:
    with connect(database) as db:
        return (
            db.execute(
                "SELECT 1 FROM phase_tasks WHERE status IN ('queued','running') LIMIT 1"
            ).fetchone()
            is not None
        )


def _log_task_completion(
    root: Path,
    database: Path,
    endpoint: str,
    model_id: str,
    task: sqlite3.Row,
    outcome: str,
    prompt_tokens: int | None,
    completion_tokens: int | None,
    duration_seconds: float,
    request_limits: dict[str, int] | None,
    output_lock: Lock,
) -> None:
    """Print one compact cross-process queue snapshot after each finished phase task."""
    try:
        with connect(database) as db:
            paper_chunks = db.execute(
                "SELECT COUNT(*) FROM chunks WHERE paper_id=?", (task["paper_id"],)
            ).fetchone()[0]
            phase_statuses = {
                (row["phase"], row["status"]): row["count"]
                for row in db.execute(
                    "SELECT phase,status,COUNT(*) AS count FROM phase_tasks GROUP BY phase,status"
                )
            }
        phase_open = {
            phase: sum(
                count
                for (task_phase, status), count in phase_statuses.items()
                if task_phase == phase and status != "complete"
            )
            for phase in (1, 2)
        }
        open_tasks = sum(phase_open.values())
        active_processes = _active_process_count(root)
        age = _time_since_last_429(root / "last_429.json")
        state = "finished" if outcome == "complete" else "failed"
        input_tokens = _format_token_count(prompt_tokens) if prompt_tokens is not None else "n/a"
        output_tokens = (
            _format_token_count(completion_tokens) if completion_tokens is not None else "n/a"
        )
        output_rate = (
            _format_token_count(round(completion_tokens / duration_seconds))
            if completion_tokens is not None and duration_seconds > 0
            else "n/a"
        )
        token_usage = f"input={input_tokens:>5} output={output_tokens:>5} output/s={output_rate:>5}"
        limits_summary = f"; request limits={request_limits}" if request_limits else ""
        message = (
            f"[{endpoint}/{model_id}] {state} phase {task['phase']} "
            f"{task['paper_id']}/{task['chunk_index'] + 1:03d} "
            f"({paper_chunks} chunks in paper); time={_format_duration(duration_seconds):>8}; "
            f"{token_usage}; "
            f"open phase tasks={open_tasks} (P1 {phase_open[1]}, P2 {phase_open[2]}); "
            f"active processes={active_processes}; last 429={age}{limits_summary}"
        )
        with output_lock:
            if sys.stdout.isatty():
                sys.stdout.write("\r\033[K")
            print(message, flush=True)
    except Exception:
        logger.exception("Could not write task completion progress line")


def _format_token_count(count: int) -> str:
    if count >= 1_000_000:
        value = f"{count / 1_000_000:.1f}".removesuffix(".0")
        return f"{value}M"
    if count >= 1_000:
        value = f"{count / 1_000:.1f}".removesuffix(".0")
        return f"{value}k"
    return str(count)


def _format_duration(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes, remaining_seconds = divmod(seconds, 60)
    if minutes < 60:
        return f"{int(minutes)}m{remaining_seconds:02.0f}s"
    hours, remaining_minutes = divmod(minutes, 60)
    return f"{int(hours)}h{int(remaining_minutes):02d}m"


def _active_process_count(root: Path) -> int:
    pids = set()
    for state_path in (root / "workers").glob("*.json"):
        try:
            state = json.loads(state_path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if state.get("state") not in {"running", "draining"} or not _worker_process_alive(state):
            continue
        pids.add(state.get("pid", state.get("worker_id", state_path.name)))
    return len(pids)


def _time_since_last_429(path: Path) -> str:
    try:
        occurred_at = datetime.fromisoformat(json.loads(path.read_text())["occurred_at"])
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return "never"
    seconds = max(0, int((datetime.now(UTC) - occurred_at.astimezone(UTC)).total_seconds()))
    if seconds < 60:
        return f"{seconds}s ago"
    minutes, seconds = divmod(seconds, 60)
    if minutes < 60:
        return f"{minutes}m {seconds}s ago"
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m ago"


def _active_worker_slots(root: Path) -> int:
    """Count configured thread slots for endpoint/model processes currently running."""
    total = 0
    for state_path in (root / "workers").glob("*.json"):
        try:
            state = json.loads(state_path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if state.get("state") in {"running", "draining"} and _worker_process_alive(state):
            total += max(0, int(state.get("concurrency", 0)))
    return total


def _worker_process_alive(state: dict) -> bool:
    """Ignore stale worker status files left behind by terminated processes."""
    pid = state.get("pid")
    if pid is None:
        parts = str(state.get("worker_id", "")).rsplit("-", 2)
        pid = parts[-2] if len(parts) == 3 else None
    try:
        os.kill(int(pid), 0)
    except (TypeError, ValueError, ProcessLookupError):
        return False
    except PermissionError:
        return True
    return True


def _aggregate_papers_across_processes(root: Path, paper_ids: list[str]) -> None:
    import fcntl

    with (root / "aggregate.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        _aggregate_ready_papers(root, paper_ids)


def _claim_phase(
    database: Path,
    worker_id: str,
    strategy: str,
    max_attempts: int,
    endpoint: str = "primary",
    model_id: str = "model",
    active_worker_slots: int = 0,
) -> sqlite3.Row | None:
    now = datetime.now(UTC)
    lease_until = (now + timedelta(seconds=LEASE_SECONDS)).isoformat()
    with connect(database) as db:
        db.execute("BEGIN IMMEDIATE")
        db.execute(
            """CREATE TABLE IF NOT EXISTS phase_routes (
                paper_id TEXT NOT NULL,
                phase INTEGER NOT NULL,
                endpoint TEXT NOT NULL,
                model_id TEXT NOT NULL,
                assigned_at TEXT NOT NULL,
                PRIMARY KEY (paper_id, phase)
            )"""
        )
        phase1 = db.execute(
            """SELECT t.* FROM phase_tasks t
               LEFT JOIN phase_routes r ON r.paper_id=t.paper_id AND r.phase=t.phase
               WHERE t.phase=1 AND t.status IN ('queued','failed') AND t.attempts < ?
                 AND (r.paper_id IS NULL OR (r.endpoint=? AND r.model_id=?))
               ORDER BY t.paper_id,t.chunk_index LIMIT 1""",
            (max_attempts, endpoint, model_id),
        ).fetchone()
        phase1_active = db.execute(
            """SELECT 1 FROM phase_tasks WHERE phase=1
               AND (status='running' OR (status='queued' AND attempts < ?)) LIMIT 1""",
            (max_attempts,),
        ).fetchone()
        ready_buffer = db.execute(
            """SELECT COUNT(*) FROM phase_tasks p2
               JOIN phase_tasks p1 USING(paper_id,chunk_index)
               WHERE p1.phase=1 AND p1.status='complete'
                 AND p2.phase=2 AND p2.status='queued' AND p2.attempts < ?""",
            (max_attempts,),
        ).fetchone()[0]
        unlocked = db.execute(
            "SELECT value FROM scheduler_meta WHERE key='phase2_unlocked'"
        ).fetchone()
        if unlocked is None and (ready_buffer >= PHASE2_RESERVE or phase1_active is None):
            db.execute("INSERT INTO scheduler_meta(key,value) VALUES ('phase2_unlocked','1')")
            unlocked = ("1",)
        phase2 = db.execute(
            """SELECT p2.* FROM phase_tasks p2
               JOIN phase_tasks p1 USING(paper_id,chunk_index)
               LEFT JOIN phase_routes r ON r.paper_id=p2.paper_id AND r.phase=p2.phase
               WHERE p1.phase=1 AND p1.status='complete' AND p2.phase=2
                 AND p2.status IN ('queued','failed') AND p2.attempts < ?
                 AND (r.paper_id IS NULL OR (r.endpoint=? AND r.model_id=?))
               ORDER BY p2.paper_id,p2.chunk_index LIMIT 1""",
            (max_attempts, endpoint, model_id),
        ).fetchone()

        phase1_total = db.execute(
            "SELECT COUNT(*) FROM phase_tasks WHERE phase=1 "
            "AND status IN ('queued','failed') AND attempts < ?",
            (max_attempts,),
        ).fetchone()[0]
        phase2_total = db.execute(
            """SELECT COUNT(*) FROM phase_tasks p2
               JOIN phase_tasks p1 USING(paper_id,chunk_index)
               WHERE p1.phase=1 AND p1.status='complete' AND p2.phase=2
                 AND p2.status IN ('queued','failed') AND p2.attempts < ?""",
            (max_attempts,),
        ).fetchone()[0]
        if active_worker_slots > 0 and phase1_total <= active_worker_slots and phase1 is None:
            phase1 = db.execute(
                """SELECT * FROM phase_tasks WHERE phase=1
                   AND status IN ('queued','failed') AND attempts < ?
                   ORDER BY paper_id,chunk_index LIMIT 1""",
                (max_attempts,),
            ).fetchone()
        if active_worker_slots > 0 and phase2_total <= active_worker_slots and phase2 is None:
            phase2 = db.execute(
                """SELECT p2.* FROM phase_tasks p2
                   JOIN phase_tasks p1 USING(paper_id,chunk_index)
                   WHERE p1.phase=1 AND p1.status='complete' AND p2.phase=2
                     AND p2.status IN ('queued','failed') AND p2.attempts < ?
                   ORDER BY p2.paper_id,p2.chunk_index LIMIT 1""",
                (max_attempts,),
            ).fetchone()

        if strategy == "phase1":
            selected = phase1 or (phase2 if not phase1_active and phase2 else None)
        elif strategy == "phase2":
            drain_at_end = phase1_active is None
            selected = (
                phase2 if phase2 and (ready_buffer > PHASE2_RESERVE or drain_at_end) else phase1
            )
        else:
            selected = (phase2 if unlocked and unlocked[0] == "1" else None) or phase1
        if selected is None:
            db.commit()
            return None
        phase = selected["phase"]
        db.execute(
            """UPDATE phase_tasks SET status='running',attempts=attempts+1,
               worker_id=?,lease_until=?,error=NULL,updated_at=?
               WHERE paper_id=? AND chunk_index=? AND phase=?""",
            (
                worker_id,
                lease_until,
                now.isoformat(),
                selected["paper_id"],
                selected["chunk_index"],
                phase,
            ),
        )
        db.execute(
            "UPDATE chunks SET status='running',worker_id=?,lease_until=?,updated_at=? "
            "WHERE paper_id=? AND chunk_index=?",
            (
                worker_id,
                lease_until,
                now.isoformat(),
                selected["paper_id"],
                selected["chunk_index"],
            ),
        )
        db.execute(
            "UPDATE papers SET status='running',updated_at=? WHERE paper_id=? AND status='queued'",
            (now.isoformat(), selected["paper_id"]),
        )
        db.execute(
            """INSERT OR IGNORE INTO phase_routes
               (paper_id,phase,endpoint,model_id,assigned_at) VALUES (?,?,?,?,?)""",
            (selected["paper_id"], phase, endpoint, model_id, now.isoformat()),
        )
        db.commit()
        return db.execute(
            "SELECT * FROM phase_tasks WHERE paper_id=? AND chunk_index=? AND phase=?",
            (selected["paper_id"], selected["chunk_index"], phase),
        ).fetchone()


def _process_phase(root: Path, task: sqlite3.Row, route: ModelRoute, gate: RequestGate) -> dict:
    from backend.repetition_chunks import _response_schema

    folder = root / "papers" / task["paper_id"]
    source = (folder / "source.tex").read_text()
    hints = json.loads((folder / "hints.json").read_text())
    ids = json.loads(_table_ids(queue_database_path(root), task["paper_id"], task["chunk_index"]))
    inventory = table_inventory(source)
    selected = [table for table in inventory if table["table_id"] in ids]
    if len(selected) != len(ids):
        raise ValueError("Chunk table IDs do not match the frozen source")
    content = repetition_input(source, paper_id=task["paper_id"], hints=hints)
    content += "\nCHUNK SCOPE (apply only after reading the full source above):\n"
    content += json.dumps(
        {
            "assigned_table_ids": ids,
            "assigned_tables": [
                {key: value for key, value in table.items() if key != "body"} for table in selected
            ],
            "instruction": "Return facts only for assigned table IDs. Never return another table ID.",
        },
        ensure_ascii=False,
    )
    client = LLMExtractor(
        model_tier=route.model_id,
        streaming=True,
        result_output_format="json",
        enable_reasoning=True,
        max_total_tokens=MAX_TOTAL_TOKENS,
        model_route=route,
    )
    client.request_timeout_seconds = REQUEST_TIMEOUT_SECONDS
    client.request_gate = gate
    client._client.max_retries = 0
    prompts = root / "prompts"
    if task["phase"] == 1:
        raw = client._call_structured(
            (prompts / FACTS_PROMPT).read_text(),
            content,
            call_type="repetition_chunk_facts",
            output_format="json",
            max_tokens=MAX_COMPLETION_TOKENS,
            response_format=_response_schema(RepetitionFacts, "repetition_facts"),
        )
        if client._call_log[-1].finish_reason == "length":
            raise ValueError("Chunk facts were truncated")
        facts = RepetitionFacts.model_validate(raw)
        unexpected = {table.table_id for table in facts.tables} - set(ids)
        if unexpected:
            raise ValueError(f"Chunk returned unassigned tables: {sorted(unexpected)}")
        return {"facts": facts.model_dump(), "calls": [asdict(c) for c in client._call_log]}

    phase1_path = _chunk_path(root, task["paper_id"], task["chunk_index"]) / "phase1.json"
    phase1 = json.loads(phase1_path.read_text())
    facts = RepetitionFacts.model_validate(phase1["facts"])
    verification_content = content + "\nUNTRUSTED METADATA (not source evidence):\n"
    verification_content += facts.model_dump_json()
    verification_content += "\nREQUIRED VERDICT KEYS (copy exactly; do not expand variants):\n"
    verification_content += json.dumps(
        [{"table_id": t.table_id, "name": m.name} for t in facts.tables for m in t.methods]
    )
    raw = client._call_structured(
        (prompts / VERIFY_PROMPT).read_text(),
        verification_content,
        call_type="repetition_chunk_verification",
        output_format="json",
        max_tokens=MAX_COMPLETION_TOKENS,
        response_format=_response_schema(Verification, "repetition_verification"),
    )
    if client._call_log[-1].finish_reason == "length":
        raise ValueError("Chunk verification was truncated")
    verification = Verification.model_validate(raw)
    if any(verdict.table_id not in ids for verdict in verification.methods):
        raise ValueError("Chunk verifier returned a table outside its assignment")
    return {
        "verification": verification.model_dump(),
        "calls": [asdict(c) for c in client._call_log],
    }


def _table_ids(database: Path, paper_id: str, chunk_index: int) -> str:
    with connect(database) as db:
        row = db.execute(
            "SELECT table_ids_json FROM chunks WHERE paper_id=? AND chunk_index=?",
            (paper_id, chunk_index),
        ).fetchone()
    if row is None:
        raise KeyError(f"Unknown chunk {paper_id}/{chunk_index}")
    return row[0]


def _complete_phase(
    root: Path,
    database: Path,
    task: sqlite3.Row,
    output_path: Path,
    endpoint: str,
    model_id: str,
    calls: list[dict],
) -> None:
    completed = datetime.now(UTC)
    now = completed.isoformat()
    started = datetime.fromisoformat(task["updated_at"])
    duration_seconds = max(0.0, (completed - started).total_seconds())
    phase = task["phase"]
    with connect(database) as db:
        db.execute(
            """UPDATE phase_tasks SET status='complete',output_path=?,route_label=?,model_id=?,
               lease_until=NULL,updated_at=? WHERE paper_id=? AND chunk_index=? AND phase=?""",
            (
                str(output_path),
                endpoint,
                model_id,
                now,
                task["paper_id"],
                task["chunk_index"],
                phase,
            ),
        )
        if phase == 1:
            db.execute(
                "UPDATE phase_tasks SET status='queued',updated_at=? "
                "WHERE paper_id=? AND chunk_index=? AND phase=2 AND status='blocked'",
                (now, task["paper_id"], task["chunk_index"]),
            )
            db.execute(
                "UPDATE chunks SET status='queued',lease_until=NULL,updated_at=? "
                "WHERE paper_id=? AND chunk_index=?",
                (now, task["paper_id"], task["chunk_index"]),
            )
        else:
            phase1_path = _chunk_path(root, task["paper_id"], task["chunk_index"]) / "phase1.json"
            first = json.loads(phase1_path.read_text())
            second = json.loads(output_path.read_text())
            combined = {
                "paper_id": task["paper_id"],
                "chunk_index": task["chunk_index"],
                "table_ids": json.loads(
                    db.execute(
                        "SELECT table_ids_json FROM chunks WHERE paper_id=? AND chunk_index=?",
                        (task["paper_id"], task["chunk_index"]),
                    ).fetchone()[0]
                ),
                "facts": first["facts"],
                "verification": second["verification"],
                "calls": first.get("calls", []) + second.get("calls", []),
            }
            combined_path = _chunk_path(root, task["paper_id"], task["chunk_index"]) / "chunk.json"
            write_json(combined_path, combined)
            db.execute(
                "UPDATE chunks SET status='complete',output_path=?,lease_until=NULL,updated_at=? "
                "WHERE paper_id=? AND chunk_index=?",
                (str(combined_path), now, task["paper_id"], task["chunk_index"]),
            )
        prompt_tokens = sum(int(call.get("prompt_tokens") or 0) for call in calls)
        completion_tokens = sum(int(call.get("completion_tokens") or 0) for call in calls)
        db.execute(
            """INSERT INTO throughput_events
               (completed_at,endpoint,model_id,phase,paper_id,chunk_index,prompt_tokens,
                completion_tokens,started_at,duration_seconds)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (
                now,
                endpoint,
                model_id,
                phase,
                task["paper_id"],
                task["chunk_index"],
                prompt_tokens,
                completion_tokens,
                started.isoformat(),
                duration_seconds,
            ),
        )


def _fail_phase(database: Path, task: sqlite3.Row, error: str, max_attempts: int) -> None:
    status = "queued" if task["attempts"] < max_attempts else "failed"
    now = _now()
    with connect(database) as db:
        db.execute(
            """UPDATE phase_tasks SET status=?,error=?,lease_until=NULL,updated_at=?
               WHERE paper_id=? AND chunk_index=? AND phase=?""",
            (status, error, now, task["paper_id"], task["chunk_index"], task["phase"]),
        )
        db.execute(
            "UPDATE chunks SET status=?,error=?,lease_until=NULL,updated_at=? "
            "WHERE paper_id=? AND chunk_index=?",
            (
                "queued" if status == "queued" else "failed",
                error,
                now,
                task["paper_id"],
                task["chunk_index"],
            ),
        )
        if status == "failed":
            db.execute(
                "UPDATE papers SET status='failed',error=?,updated_at=? WHERE paper_id=?",
                (error, now, task["paper_id"]),
            )


def _release_phase_leases(database: Path, worker_id: str) -> None:
    with connect(database) as db:
        db.execute(
            "UPDATE phase_tasks SET status='queued',worker_id=NULL,lease_until=NULL,updated_at=? "
            "WHERE status='running' AND worker_id LIKE ?",
            (_now(), f"{worker_id}%"),
        )
        db.execute(
            "UPDATE chunks SET status='queued',worker_id=NULL,lease_until=NULL,updated_at=? "
            "WHERE status='running' AND worker_id LIKE ?",
            (_now(), f"{worker_id}%"),
        )


def _renew_phase_lease(
    database: Path,
    task: sqlite3.Row,
    worker_id: str,
    stop: Event,
) -> None:
    """Keep a claimed task leased while its request is active or rate-limited."""
    interval = max(30, LEASE_SECONDS // 3)
    while not stop.wait(interval):
        lease_until = (datetime.now(UTC) + timedelta(seconds=LEASE_SECONDS)).isoformat()
        with connect(database) as db:
            db.execute(
                "UPDATE phase_tasks SET lease_until=? WHERE paper_id=? AND chunk_index=? "
                "AND phase=? AND status='running' AND worker_id=?",
                (
                    lease_until,
                    task["paper_id"],
                    task["chunk_index"],
                    task["phase"],
                    worker_id,
                ),
            )
            db.execute(
                "UPDATE chunks SET lease_until=? WHERE paper_id=? AND chunk_index=? "
                "AND status='running' AND worker_id=?",
                (lease_until, task["paper_id"], task["chunk_index"], worker_id),
            )


def _update_throughput_graph(root: Path, database: Path) -> None:
    import fcntl

    with (root / "throughput.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        with connect(database) as db:
            tables = {
                row["name"]
                for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")
            }
            event_columns = (
                {row["name"] for row in db.execute("PRAGMA table_info(throughput_events)")}
                if "throughput_events" in tables
                else set()
            )
            rows = (
                db.execute(
                    "SELECT completed_at,"
                    + ("started_at" if "started_at" in event_columns else "NULL AS started_at")
                    + ","
                    + (
                        "duration_seconds"
                        if "duration_seconds" in event_columns
                        else "NULL AS duration_seconds"
                    )
                    + ",endpoint,model_id,phase,paper_id,chunk_index,prompt_tokens,completion_tokens "
                    "FROM throughput_events ORDER BY completed_at,id"
                ).fetchall()
                if "throughput_events" in tables
                else []
            )
            phase_counts = {}
            if "phase_tasks" in tables:
                phase_counts = {
                    (row["phase"], row["status"]): row["count"]
                    for row in db.execute(
                        "SELECT phase,status,COUNT(*) AS count FROM phase_tasks GROUP BY phase,status"
                    )
                }
            phase_totals = {
                phase: sum(
                    count for (number, _status), count in phase_counts.items() if number == phase
                )
                for phase in (1, 2)
            }
            phase1_ready = sum(phase_counts.get((1, status), 0) for status in ("queued", "failed"))
            phase2_ready = (
                db.execute(
                    "SELECT COUNT(*) FROM phase_tasks p2 "
                    "JOIN phase_tasks p1 USING(paper_id,chunk_index) "
                    "WHERE p1.phase=1 AND p1.status='complete' AND p2.phase=2 "
                    "AND p2.status IN ('queued','failed')"
                ).fetchone()[0]
                if "phase_tasks" in tables
                else 0
            )
            chunk_counts = (
                {
                    row["status"]: row["count"]
                    for row in db.execute(
                        "SELECT status,COUNT(*) AS count FROM chunks GROUP BY status"
                    )
                }
                if "chunks" in tables
                else {}
            )
            paper_counts = (
                {
                    row["status"]: row["count"]
                    for row in db.execute(
                        "SELECT status,COUNT(*) AS count FROM papers GROUP BY status"
                    )
                }
                if "papers" in tables
                else {}
            )
            chunk_total = (
                db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] if "chunks" in tables else 0
            )
            paper_total = (
                db.execute("SELECT COUNT(*) FROM papers").fetchone()[0] if "papers" in tables else 0
            )
            now = _now()
            expired_chunk_leases = (
                db.execute(
                    "SELECT COUNT(*) FROM chunks WHERE status='running' AND lease_until < ?",
                    (now,),
                ).fetchone()[0]
                if "chunks" in tables
                else 0
            )
            expired_phase_leases = (
                db.execute(
                    "SELECT phase,COUNT(*) AS count FROM phase_tasks "
                    "WHERE status='running' AND lease_until < ? GROUP BY phase",
                    (now,),
                ).fetchall()
                if "phase_tasks" in tables
                else []
            )
        worker_states = []
        for state_path in sorted((root / "workers").glob("*.json")):
            try:
                worker_states.append(json.loads(state_path.read_text()))
            except (OSError, json.JSONDecodeError):
                continue

        buckets: dict[tuple[int, str], int] = {}
        for row in rows:
            minute = int(datetime.fromisoformat(row["completed_at"]).timestamp()) // 60
            tokens = row["prompt_tokens"] + row["completion_tokens"]
            key = (minute, row["endpoint"])
            buckets[key] = buckets.get(key, 0) + tokens
        endpoints = sorted({endpoint for _, endpoint in buckets})
        minutes = [minute for minute, _ in buckets]
        dense = (
            {
                (minute, endpoint): buckets.get((minute, endpoint), 0)
                for endpoint in endpoints
                for minute in range(min(minutes), max(minutes) + 1)
            }
            if minutes
            else {}
        )
        _write_throughput_report(
            root,
            rows,
            phase_counts,
            chunk_counts,
            paper_counts,
            chunk_total,
            paper_total,
            worker_states,
            expired_chunk_leases,
            {row["phase"]: row["count"] for row in expired_phase_leases},
            dense,
            phase_totals,
            phase1_ready,
            phase2_ready,
        )
        with (root / "throughput.csv").open("w", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(("minute_utc", "endpoint", "tokens_per_second"))
            for (minute, endpoint), tokens in sorted(dense.items()):
                writer.writerow(
                    (datetime.fromtimestamp(minute * 60, UTC).isoformat(), endpoint, tokens / 60)
                )
        if not endpoints:
            return
        try:
            import matplotlib

            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            logger.warning(
                "matplotlib is unavailable; wrote throughput.csv but skipped throughput.png"
            )
            return
        figure, axis = plt.subplots(figsize=(10, 5))
        for endpoint in endpoints:
            points = sorted(
                (minute, tokens / 60)
                for (minute, label), tokens in dense.items()
                if label == endpoint
            )
            axis.plot(
                [datetime.fromtimestamp(minute * 60, UTC) for minute, _ in points],
                [rate for _, rate in points],
                marker=".",
                label=endpoint,
            )
        axis.set_title("Repetition extraction throughput")
        axis.set_xlabel("Completion time (UTC)")
        axis.set_ylabel("Tokens per second (60-second bins; prompt + completion)")
        axis.grid(True, alpha=0.25)
        axis.legend(title="Endpoint")
        figure.autofmt_xdate()
        figure.tight_layout()
        figure.savefig(root / "throughput.png", dpi=150)
        plt.close(figure)


def _write_throughput_report(
    root: Path,
    rows: list[sqlite3.Row],
    phase_counts: dict[tuple[int, str], int],
    chunk_counts: dict[str, int],
    paper_counts: dict[str, int],
    chunk_total: int,
    paper_total: int,
    worker_states: list[dict],
    expired_chunk_leases: int,
    expired_phase_leases: dict[int, int],
    minute_bins: dict[tuple[int, str], int],
    phase_totals: dict[int, int],
    phase1_ready: int,
    phase2_ready: int,
) -> None:
    """Write a live queue and model/endpoint performance report."""
    completed_chunks = chunk_counts.get("complete", 0)
    phase1_total = phase_totals.get(1, 0) or chunk_total
    phase2_total = phase_totals.get(2, 0) or chunk_total
    lines = [
        "# Repetition scheduler throughput",
        "",
        f"Updated: {datetime.now(UTC).isoformat()}",
        "",
        "## Queue status",
        "",
        f"- Chunks: **{completed_chunks}/{chunk_total} complete**, "
        f"{chunk_total - completed_chunks} not complete",
        f"- Papers: **{paper_counts.get('ready', 0)}/{paper_total} ready**",
        f"- Chunk statuses: {_format_counts(chunk_counts)}",
        f"- Paper statuses: {_format_counts(paper_counts)}",
        f"- Expired leases awaiting recovery: chunks {expired_chunk_leases}; "
        f"phase 1 {expired_phase_leases.get(1, 0)}, phase 2 {expired_phase_leases.get(2, 0)}",
        "",
        "## Phase queue",
        "",
        "Totals and ready counts in phase 2 are cumulative and include phase 1. Ready means "
        "queued or retryable; a phase-2 chunk counts as ready only after its phase-1 chunk "
        "is complete.",
        "",
        "| Phase | Total counted | Ready |",
        "|---|---:|---:|",
        f"| 1 | {phase1_total} | {phase1_ready} |",
        f"| 2 (cumulative, includes phase 1) | {phase1_total + phase2_total} | "
        f"{phase1_ready + phase2_ready} |",
        "",
        "| Phase | Complete | Running | Queued | Blocked | Failed | Other |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for phase in (1, 2):
        values = {
            status: count for (number, status), count in phase_counts.items() if number == phase
        }
        other = sum(
            count
            for status, count in values.items()
            if status not in {"complete", "running", "queued", "blocked", "failed"}
        )
        lines.append(
            f"| {phase} | {values.get('complete', 0)} | {values.get('running', 0)} | "
            f"{values.get('queued', 0)} | {values.get('blocked', 0)} | "
            f"{values.get('failed', 0)} | {other} |"
        )
    lines.extend(["", "## Workers", ""])
    active = [
        worker
        for worker in worker_states
        if worker.get("state") in {"running", "draining"} and _worker_process_alive(worker)
    ]
    if active:
        lines.extend(
            [
                "| Endpoint | Model | Strategy | Threads | Request caps | Active | Completed | Updated |",
                "|---|---|---|---:|---|---:|---:|---|",
            ]
        )
        for worker in active:
            lines.append(
                f"| {worker.get('endpoint', '?')} | {worker.get('model', '?')} | "
                f"{worker.get('strategy', '?')} | "
                f"{worker.get('concurrency', 0)} ({worker.get('concurrency_mode', 'fixed')}) | "
                f"{worker.get('rate_window_limits', {})} | "
                f"{worker.get('active_requests', 0)} | {worker.get('completed_tasks', 0)} | "
                f"{worker.get('updated_at', 'n/a')} |"
            )
    else:
        lines.append("No workers are currently marked as running.")

    by_route: dict[tuple[str, str], list[sqlite3.Row]] = {}
    for row in rows:
        by_route.setdefault((row["endpoint"], row["model_id"]), []).append(row)
    lines.extend(
        [
            "",
            "## Throughput by endpoint and model",
            "",
            "Tokens/s is total prompt plus completion tokens divided by the wall-clock interval "
            "from the first chunk start to the latest chunk completion; parallel calls are therefore "
            "aggregated rather than averaged.",
            "",
            "| Endpoint | Model | Chunks | Prompt tokens | Completion tokens | Aggregate tokens/s |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for (endpoint, model), route_rows in sorted(by_route.items()):
        prompt = sum(row["prompt_tokens"] for row in route_rows)
        completion = sum(row["completion_tokens"] for row in route_rows)
        starts = [
            datetime.fromisoformat(row["started_at"]) for row in route_rows if row["started_at"]
        ]
        ends = [datetime.fromisoformat(row["completed_at"]) for row in route_rows]
        elapsed = max(1.0, (max(ends) - min(starts or ends)).total_seconds())
        lines.append(
            f"| {endpoint} | {model} | {len(route_rows)} | {prompt} | {completion} | "
            f"{(prompt + completion) / elapsed:.2f} |"
        )
    if not by_route:
        lines.append("No completed phase chunks yet.")

    lines.extend(
        [
            "",
            "## Chunk duration by phase and endpoint/model",
            "",
            "Mean and median use all completed chunks; last 10 uses the 10 most recently completed "
            "chunks for that phase and endpoint/model.",
            "",
            "| Phase | Endpoint | Model | N | Mean (s) | Median (s) | Last 10 mean (s) |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    duration_groups: dict[tuple[int, str, str], list[sqlite3.Row]] = {}
    for row in rows:
        if row["duration_seconds"] is not None:
            duration_groups.setdefault((row["phase"], row["endpoint"], row["model_id"]), []).append(
                row
            )
    import statistics

    for (phase, endpoint, model), group in sorted(duration_groups.items()):
        durations = [float(row["duration_seconds"]) for row in group]
        recent = [float(row["duration_seconds"]) for row in group[-10:]]
        lines.append(
            f"| {phase} | {endpoint} | {model} | {len(durations)} | "
            f"{statistics.mean(durations):.1f} | {statistics.median(durations):.1f} | "
            f"{statistics.mean(recent):.1f} |"
        )
    if not duration_groups:
        lines.append("No duration data yet.")
    lines.extend(
        [
            "",
            "## Per-minute throughput",
            "",
            "Prompt plus completion tokens per second in 60-second UTC bins; zero rows are "
            "included when an endpoint had no completed chunk in that minute.",
            "",
            "| Minute (UTC) | Endpoint | Tokens/s |",
            "|---|---|---:|",
        ]
    )
    if minute_bins:
        for (minute, endpoint), tokens in sorted(minute_bins.items()):
            timestamp = datetime.fromtimestamp(minute * 60, UTC).isoformat()
            lines.append(f"| {timestamp} | {endpoint} | {tokens / 60:.2f} |")
    else:
        lines.append("No completed phase chunks yet.")
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- Graph: `{root / 'throughput.png'}`",
            f"- Per-minute data: `{root / 'throughput.csv'}`",
            f"- Queue database: `{queue_database_path(root)}`",
            "",
        ]
    )
    (root / "throughput.md").write_text("\n".join(lines))


def _format_counts(counts: dict[str, int]) -> str:
    return ", ".join(f"{status}: {count}" for status, count in sorted(counts.items())) or "none"
