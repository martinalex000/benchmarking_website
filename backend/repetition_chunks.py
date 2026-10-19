"""Persistent table-chunk scheduler for repetition-number extraction.

The existing paper-level extractor remains unchanged. This runner reuses its prompts,
schemas, validation and database application while scheduling source-table groups as
independent jobs, with a durable SQLite queue for resume and overview.
"""

from __future__ import annotations

import hashlib
import json
import logging
import sqlite3
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from dataclasses import asdict
from datetime import UTC, datetime, timedelta
from pathlib import Path
from threading import Event, Lock
from uuid import uuid4

from backend.config import cfg
from backend.db import session_scope
from backend.llm_model_options import extra_body_for_model
from backend.llm_tasks import LLMExtractor
from backend.models import Paper, RepetitionAssessment, Result
from backend.repetition_batch import RequestGate, backup_database, write_json
from backend.repetition_extractor import (
    DEFAULT_MODEL,
    MAX_REPETITION_TOTAL_TOKENS,
    _response_schema,
    external_glm_route,
    preflight_external_glm,
    repetition_input,
)
from backend.repetition_metadata import (
    RepetitionFacts,
    Verification,
    table_inventory,
    validate_repetitions,
)
from backend.repetition_storage import apply_assessment

logger = logging.getLogger(__name__)
FACTS_PROMPT = "repetition_metadata.txt"
VERIFY_PROMPT = "repetition_verification.txt"
MAX_COMPLETION_TOKENS = 24_000
MAX_TOTAL_TOKENS = MAX_REPETITION_TOTAL_TOKENS
REQUEST_TIMEOUT_SECONDS = 600
LEASE_SECONDS = REQUEST_TIMEOUT_SECONDS + 120


@contextmanager
def connect(database: Path) -> Iterator[sqlite3.Connection]:
    database.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database, timeout=30)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA busy_timeout=30000")
    connection.execute("PRAGMA foreign_keys=ON")
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()


def queue_database_path(root: Path) -> Path:
    """Keep scheduler bookkeeping beside the primary benchmarks database."""
    return cfg.db_path.with_name(f"{root.name}.sqlite3")


def initialize(root: Path, *, chunk_tables: int = 4, venue_set_only: bool = False) -> dict:
    """Create a new queue and snapshot the currently unassessed paper cohort."""
    if chunk_tables < 1:
        raise ValueError("chunk_tables must be at least one")
    _assert_no_legacy_batch_running()
    database = queue_database_path(root)
    if database.exists():
        raise FileExistsError(f"Queue already exists at {database}; resume it or choose a new root")

    prompts = root / "prompts"
    prompts.mkdir(parents=True, exist_ok=True)
    prompt_source = Path(__file__).with_name("prompts")
    for name in (FACTS_PROMPT, VERIFY_PROMPT):
        text = (prompt_source / name).read_text()
        if name == FACTS_PROMPT:
            coverage_instruction = (
                "Return EXACTLY ONE output for EVERY inventory table, including excluded tables."
            )
            if coverage_instruction not in text:
                raise ValueError(
                    "The repetition prompt changed; review the chunk-specific adaptation"
                )
            text = text.replace(
                coverage_instruction,
                "Return exactly one output for every assigned table ID listed at the end of the "
                "input. Do not return tables outside those assigned IDs. The full source and "
                "inventory are context; the final chunk scope defines output coverage.",
            )
        (prompts / name).write_text(text)
    prompt_hashes = {
        "facts": _sha256((prompts / FACTS_PROMPT).read_bytes()),
        "verification": _sha256((prompts / VERIFY_PROMPT).read_bytes()),
    }
    legacy_prompt_hashes = {
        "facts": _sha256((prompt_source / FACTS_PROMPT).read_bytes()),
        "verification": _sha256((prompt_source / VERIFY_PROMPT).read_bytes()),
    }
    legacy_roots = sorted(cfg.papers_dir.glob("repetition_backfill*"))

    with session_scope() as session:
        assessed = {row[0] for row in session.query(RepetitionAssessment.paper_id).distinct()}
        papers = (
            session.query(Paper.id, Paper.arxiv_id, Paper.title, Paper.venue)
            .filter(Paper.arxiv_id.is_not(None))
            .order_by(Paper.arxiv_id)
            .all()
        )
        cohort = [
            paper
            for paper in papers
            if paper.id not in assessed
            and (not venue_set_only or bool(paper.venue and paper.venue.strip()))
        ]
        hints_by_id = {}
        for paper in cohort:
            hints_by_id[paper.arxiv_id] = sorted(
                {
                    result.model_name_override or result.model.name
                    for result in session.query(Result).filter_by(paper_id=paper.id).all()
                }
            )

    root.mkdir(parents=True, exist_ok=True)
    cached_legacy = 0
    with connect(database) as db:
        db.execute("PRAGMA journal_mode=WAL")
        db.executescript(
            """
            CREATE TABLE run_meta (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            CREATE TABLE papers (
                paper_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                venue TEXT,
                source_sha256 TEXT,
                status TEXT NOT NULL,
                chunk_count INTEGER NOT NULL DEFAULT 0,
                analysis_path TEXT,
                error TEXT,
                updated_at TEXT NOT NULL,
                route_label TEXT,
                route_model TEXT
            );
            CREATE TABLE chunks (
                paper_id TEXT NOT NULL REFERENCES papers(paper_id),
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
            CREATE INDEX idx_chunks_queue ON chunks(status, lease_until, paper_id);
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
                PRIMARY KEY (paper_id, chunk_index, phase),
                FOREIGN KEY (paper_id, chunk_index)
                    REFERENCES chunks(paper_id, chunk_index)
            );
            CREATE INDEX idx_phase_queue ON phase_tasks(status, phase, paper_id);
            CREATE TABLE throughput_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                completed_at TEXT NOT NULL,
                endpoint TEXT NOT NULL,
                model_id TEXT NOT NULL,
                phase INTEGER NOT NULL,
                paper_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                prompt_tokens INTEGER NOT NULL,
                completion_tokens INTEGER NOT NULL
            );
            """
        )
        now = _now()
        values = {
            "run_id": str(uuid4()),
            "created_at": now,
            "chunk_tables": str(chunk_tables),
            "cohort_filter": "venue_set" if venue_set_only else "all_unassessed",
            "model": DEFAULT_MODEL,
            "prompt_hashes": json.dumps(prompt_hashes, sort_keys=True),
            "papers_dir": str(cfg.papers_dir),
        }
        db.executemany("INSERT INTO run_meta(key, value) VALUES (?, ?)", values.items())

        paper_root = root / "papers"
        paper_root.mkdir(exist_ok=True)
        for paper in cohort:
            pid = paper.arxiv_id
            source_path = cfg.papers_dir / pid / "latex" / "expanded.tex"
            folder = paper_root / pid
            folder.mkdir(parents=True, exist_ok=True)
            if not source_path.is_file():
                db.execute(
                    "INSERT INTO papers VALUES (?, ?, ?, NULL, 'missing_source', 0, NULL, ?, ?, NULL, NULL)",
                    (pid, paper.title, paper.venue, "Missing expanded LaTeX source", now),
                )
                continue
            source = source_path.read_text()
            source_hash = _sha256(source.encode())
            cached_path = None
            for legacy_root in legacy_roots:
                candidate = legacy_root / "papers" / pid
                reusable = _reusable_legacy_analysis(
                    candidate, source_hash, legacy_prompt_hashes, pid
                )
                if reusable is not None:
                    cached_path = reusable
                    break
            if cached_path is not None:
                db.execute(
                    "INSERT INTO papers VALUES (?, ?, ?, ?, 'ready', 0, ?, NULL, ?, NULL, NULL)",
                    (pid, paper.title, paper.venue, source_hash, str(cached_path), now),
                )
                cached_legacy += 1
                continue
            write_json(folder / "hints.json", hints_by_id[pid])
            (folder / "source.tex").write_text(source)
            tables = table_inventory(source)
            groups = [tables[i : i + chunk_tables] for i in range(0, len(tables), chunk_tables)]
            if not groups:
                groups = [[]]
            db.execute(
                "INSERT INTO papers VALUES (?, ?, ?, ?, 'queued', ?, NULL, NULL, ?, NULL, NULL)",
                (pid, paper.title, paper.venue, source_hash, len(groups), now),
            )
            for index, group in enumerate(groups):
                db.execute(
                    "INSERT INTO chunks(paper_id, chunk_index, table_ids_json, status, updated_at) "
                    "VALUES (?, ?, ?, 'queued', ?)",
                    (pid, index, json.dumps([table["table_id"] for table in group]), now),
                )
                db.execute(
                    "INSERT INTO phase_tasks VALUES (?, ?, 1, 'queued', 0, NULL, NULL, NULL, NULL, NULL, NULL, ?)",
                    (pid, index, now),
                )
                db.execute(
                    "INSERT INTO phase_tasks VALUES (?, ?, 2, 'blocked', 0, NULL, NULL, NULL, NULL, NULL, NULL, ?)",
                    (pid, index, now),
                )

    from backend.repetition_batch import _result_snapshot

    eligible_ids = [
        paper.arxiv_id
        for paper in cohort
        if (cfg.papers_dir / paper.arxiv_id / "latex" / "expanded.tex").is_file()
    ]
    write_json(
        root / "database_rows_snapshot.json",
        _result_snapshot(set(eligible_ids), include_papers=True),
    )
    write_json(
        root / "manifest.json",
        {
            "run_id": values["run_id"],
            "cohort_size": len(cohort),
            "source_ready": len(eligible_ids),
            "missing_source": len(cohort) - len(eligible_ids),
            "cohort_filter": "venue_set" if venue_set_only else "all_unassessed",
            "venue_set_only": venue_set_only,
            "cached_legacy_analyses": cached_legacy,
            "chunk_tables": chunk_tables,
            "model": DEFAULT_MODEL,
            "model_route": "selected by each endpoint worker",
            "workers": "configured per endpoint-model process",
            "phase2_ready_buffer": 30,
            "prompt_sha256": prompt_hashes,
            "chunk_input": (
                "Full source is a shared prefix; assigned table IDs are appended at the end."
            ),
        },
    )
    return overview(root)


def run(
    root: Path,
    *,
    workers: int = 10,
    max_attempts: int = 4,
) -> dict:
    """Process queued table chunks through the primary GLM endpoint."""
    if workers < 1 or max_attempts < 1:
        raise ValueError("workers and max_attempts must be positive")
    database = queue_database_path(root)
    if not database.exists():
        raise FileNotFoundError(f"No queue found at {database}; run the prepare command first")
    with connect(database) as db:
        has_phases = db.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='phase_tasks'"
        ).fetchone()
    if has_phases:
        raise RuntimeError(
            "This queue uses the phase scheduler; start workers with scripts/repetition_scheduler.py"
        )
    lock_path = root / "scheduler.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    import fcntl

    with lock_path.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("A scheduler is already running for this queue") from None
        _release_orphaned(database, max_attempts)
        with connect(database) as db:
            has_work = db.execute(
                "SELECT 1 FROM chunks WHERE status IN ('queued','failed') AND attempts < ? LIMIT 1",
                (max_attempts,),
            ).fetchone()
        if has_work is None:
            _mark_papers_with_failed_chunks(database)
            _aggregate_ready_papers(root)
            write_json(
                root / "scheduler_state.json",
                {"state": "finished", "at": datetime.now(UTC).isoformat()},
            )
            return overview(root)
        route = external_glm_route()
        gate = RequestGate(maximum=workers, daytime_streams=workers)
        try:
            preflight = preflight_external_glm(
                gate,
                max_total_tokens=MAX_TOTAL_TOKENS,
                timeout=REQUEST_TIMEOUT_SECONDS,
                model_route=route,
            )
        except Exception as exc:
            write_json(
                root / "preflight.json",
                {"status": "failed", "error": f"{type(exc).__name__}: {exc}"},
            )
            write_json(
                root / "scheduler_state.json",
                {"state": "preflight_failed", "at": datetime.now(UTC).isoformat()},
            )
            raise
        write_json(root / "preflight.json", preflight)
        write_json(
            root / "scheduler_state.json",
            {"state": "running", "started_at": datetime.now(UTC).isoformat()},
        )
        counts_lock = Lock()
        aggregation_lock = Lock()
        completed = 0

        stop = Event()

        def stoppable_worker(worker_index: int) -> None:
            nonlocal completed
            worker_id = f"{route.backend.label}-{worker_index + 1:02d}"
            while not stop.is_set():
                task = _claim(database, worker_id, max_attempts)
                if task is None:
                    return
                try:
                    output = _analyze_chunk(root, task, route, gate)
                    output_path = (
                        _chunk_path(root, task["paper_id"], task["chunk_index"]) / "chunk.json"
                    )
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    write_json(output_path, output)
                    _finish_chunk(database, task, str(output_path), None, max_attempts)
                    with aggregation_lock:
                        _aggregate_ready_papers(root, [task["paper_id"]])
                    with counts_lock:
                        completed += 1
                        logger.info(
                            "Completed %d chunks; latest %s/%03d",
                            completed,
                            task["paper_id"],
                            task["chunk_index"] + 1,
                        )
                except Exception as exc:
                    _finish_chunk(
                        database, task, None, f"{type(exc).__name__}: {exc}", max_attempts
                    )
                    logger.exception(
                        "Chunk failed for %s/%03d",
                        task["paper_id"],
                        task["chunk_index"] + 1,
                    )

        pool = ThreadPoolExecutor(max_workers=workers)
        futures = [pool.submit(stoppable_worker, index) for index in range(workers)]
        try:
            for future in as_completed(futures):
                future.result()
        except KeyboardInterrupt:
            stop.set()
            pool.shutdown(wait=True, cancel_futures=True)
            _release_orphaned(database, max_attempts)
            write_json(
                root / "scheduler_state.json",
                {"state": "interrupted", "at": datetime.now(UTC).isoformat()},
            )
            raise
        else:
            pool.shutdown(wait=True)
    _mark_papers_with_failed_chunks(database)
    _aggregate_ready_papers(root)
    write_json(
        root / "scheduler_state.json",
        {"state": "finished", "at": datetime.now(UTC).isoformat()},
    )
    return overview(root)


def overview(root: Path) -> dict:
    database = queue_database_path(root)
    if not database.exists():
        return {
            "state": "not_prepared",
            "root": str(root),
            "bookkeeping_database": str(database),
        }
    with connect(database) as db:
        paper_rows = db.execute(
            "SELECT status, COUNT(*) AS count FROM papers GROUP BY status"
        ).fetchall()
        chunk_rows = db.execute(
            "SELECT status, COUNT(*) AS count FROM chunks GROUP BY status"
        ).fetchall()
        total_papers = db.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
        total_chunks = db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        filter_row = db.execute(
            "SELECT value FROM run_meta WHERE key='cohort_filter'"
        ).fetchone()
        expired_chunk_leases = db.execute(
            "SELECT COUNT(*) FROM chunks WHERE status='running' AND lease_until < ?", (_now(),)
        ).fetchone()[0]
        failed_chunks = db.execute(
            """SELECT paper_id, chunk_index, attempts, error FROM chunks
               WHERE status='failed' ORDER BY updated_at DESC LIMIT 20"""
        ).fetchall()
    papers = {row["status"]: row["count"] for row in paper_rows}
    chunks = {row["status"]: row["count"] for row in chunk_rows}
    state_path = root / "scheduler_state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {"state": "prepared"}
    return {
        "root": str(root),
        "bookkeeping_database": str(database),
        "scheduler_state": state,
        "papers": papers,
        "paper_total": total_papers,
        "cohort_filter": filter_row[0] if filter_row else "legacy_queue",
        "chunks": chunks,
        "chunk_total": total_chunks,
        "completed_chunks": chunks.get("complete", 0),
        "remaining_chunks": total_chunks - chunks.get("complete", 0),
        "expired_chunk_leases": expired_chunk_leases,
        "failed_chunks": [dict(row) for row in failed_chunks],
    }


def apply_ready(root: Path, *, allow_partial: bool = False) -> dict:
    """Apply fully assembled assessments after source and result snapshots are rechecked."""
    database = queue_database_path(root)
    snapshot_path = root / "database_rows_snapshot.json"
    if not database.is_file() or not snapshot_path.is_file():
        raise FileNotFoundError("Queue or database snapshot is missing")
    with connect(database) as db:
        pending = db.execute(
            "SELECT paper_id, analysis_path FROM papers WHERE status='ready' ORDER BY paper_id"
        ).fetchall()
        incomplete = {
            row["status"]: row["count"]
            for row in db.execute(
                """SELECT status,COUNT(*) AS count FROM papers
                   WHERE status IN ('queued','running','failed','missing_source')
                   GROUP BY status"""
            )
        }
    if pending and incomplete and not allow_partial:
        return {
            "confirmation_required": True,
            "ready_papers": len(pending),
            "incomplete_papers": incomplete,
        }
    if not pending:
        return {"applied": 0, "ready_papers": 0, "incomplete_papers": incomplete}

    ids = {row["paper_id"] for row in pending}
    from backend.repetition_batch import _result_snapshot

    snapshot = json.loads(snapshot_path.read_text())
    if "papers" in snapshot:
        current = _result_snapshot(ids, include_papers=True)["papers"]
        expected = snapshot["papers"]
        changed = [paper_id for paper_id in ids if current.get(paper_id) != expected.get(paper_id)]
        if changed:
            raise RuntimeError(
                "Result rows changed since preparation for "
                f"{', '.join(sorted(changed))}; refusing assessment application"
            )
    else:
        # Upgrade queues prepared before per-paper snapshots were added. Check the
        # whole original cohort before deriving per-paper baselines for partial apply.
        with connect(database) as db:
            cohort_ids = {
                row[0]
                for row in db.execute("SELECT paper_id FROM papers WHERE source_sha256 IS NOT NULL")
            }
        if _result_snapshot(cohort_ids) != snapshot:
            raise RuntimeError(
                "Result rows changed since preparation; refusing assessment application"
            )
        snapshot = _result_snapshot(cohort_ids, include_papers=True)
        write_json(snapshot_path, snapshot)

    backup_path = (
        cfg.data_dir
        / "backups"
        / (
            f"benchmarks_before_repetition_chunks_{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}.sqlite"
        )
    )
    backup_database(backup_path)
    applied = 0
    with session_scope() as session:
        for row in pending:
            analysis_path = Path(row["analysis_path"])
            source = (cfg.papers_dir / row["paper_id"] / "latex" / "expanded.tex").read_text()
            apply_assessment(
                row["paper_id"],
                json.loads(analysis_path.read_text()),
                source,
                analysis_path,
                session=session,
            )
            applied += 1
    with connect(database) as db:
        db.execute(
            "UPDATE papers SET status='applied', updated_at=? WHERE status='ready'", (_now(),)
        )
    return {
        "applied": applied,
        "incomplete_papers": incomplete,
        "backup": str(backup_path),
    }


def _analyze_chunk(root: Path, task: sqlite3.Row, route, gate: RequestGate) -> dict:
    paper_id = task["paper_id"]
    folder = root / "papers" / paper_id
    source = (folder / "source.tex").read_text()
    hints = json.loads((folder / "hints.json").read_text())
    ids = json.loads(task["table_ids_json"])
    inventory = table_inventory(source)
    selected = [table for table in inventory if table["table_id"] in ids]
    if len(selected) != len(ids):
        raise ValueError("Chunk table IDs do not match the frozen source")

    content = repetition_input(source, paper_id=paper_id, hints=hints)
    # Keep source and common metadata byte-identical across a paper's chunks for prefix reuse.
    content += "\nCHUNK SCOPE (apply only after reading the full source above):\n"
    content += json.dumps(
        {
            "assigned_table_ids": ids,
            "assigned_tables": [
                {key: value for key, value in table.items() if key != "body"} for table in selected
            ],
            "instruction": (
                "Return facts only for assigned table IDs. Never return another table ID."
            ),
        },
        ensure_ascii=False,
    )

    client = LLMExtractor(
        model_tier=DEFAULT_MODEL,
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
    facts_prompt = (prompts / FACTS_PROMPT).read_text()
    verify_prompt = (prompts / VERIFY_PROMPT).read_text()
    raw_facts = client._call_structured(
        facts_prompt,
        content,
        call_type="repetition_chunk_facts",
        output_format="json",
        max_tokens=MAX_COMPLETION_TOKENS,
        response_format=_response_schema(RepetitionFacts, "repetition_facts"),
    )
    if client._call_log[-1].finish_reason == "length":
        raise ValueError("Chunk facts were truncated")
    facts = RepetitionFacts.model_validate(raw_facts)
    unexpected = {table.table_id for table in facts.tables} - set(ids)
    if unexpected:
        raise ValueError(f"Chunk returned tables outside its assignment: {sorted(unexpected)}")

    verifier_content = content + "\nUNTRUSTED METADATA (not source evidence):\n"
    verifier_content += facts.model_dump_json()
    verifier_content += "\nREQUIRED VERDICT KEYS (copy exactly; do not expand variants):\n"
    verifier_content += json.dumps(
        [{"table_id": t.table_id, "name": m.name} for t in facts.tables for m in t.methods]
    )
    raw_verification = client._call_structured(
        verify_prompt,
        verifier_content,
        call_type="repetition_chunk_verification",
        output_format="json",
        max_tokens=MAX_COMPLETION_TOKENS,
        response_format=_response_schema(Verification, "repetition_verification"),
    )
    if client._call_log[-1].finish_reason == "length":
        raise ValueError("Chunk verification was truncated")
    verification = Verification.model_validate(raw_verification)
    if any(verdict.table_id not in ids for verdict in verification.methods):
        raise ValueError("Chunk verifier returned a table outside its assignment")
    return {
        "paper_id": paper_id,
        "chunk_index": task["chunk_index"],
        "table_ids": ids,
        "facts": facts.model_dump(),
        "verification": verification.model_dump(),
        "calls": [asdict(call) for call in client._call_log],
    }


def _aggregate_ready_papers(root: Path, paper_ids: list[str] | None = None) -> None:
    database = queue_database_path(root)
    with connect(database) as db:
        query = """SELECT p.* FROM papers p
                   WHERE p.status IN ('queued','running')
                   AND EXISTS (SELECT 1 FROM chunks c WHERE c.paper_id=p.paper_id)
                   AND NOT EXISTS (
                       SELECT 1 FROM chunks c
                       WHERE c.paper_id=p.paper_id AND c.status!='complete'
                   )"""
        parameters: tuple = ()
        if paper_ids:
            placeholders = ",".join("?" for _ in paper_ids)
            query += f" AND p.paper_id IN ({placeholders})"
            parameters = tuple(paper_ids)
        papers = db.execute(query, parameters).fetchall()
    for paper in papers:
        with connect(database) as db:
            chunks = db.execute(
                "SELECT * FROM chunks WHERE paper_id=? ORDER BY chunk_index", (paper["paper_id"],)
            ).fetchall()
        if not chunks or any(chunk["status"] != "complete" for chunk in chunks):
            continue
        chunk_outputs = [json.loads(Path(chunk["output_path"]).read_text()) for chunk in chunks]
        facts = _merge_facts(chunk_outputs)
        verification = _merge_verification(chunk_outputs)
        source = (root / "papers" / paper["paper_id"] / "source.tex").read_text()
        validated = validate_repetitions(facts, verification, source)
        source_hash = paper["source_sha256"]
        prompt_hashes = json.loads(_get_meta(database, "prompt_hashes"))
        analysis = {
            "provenance": {
                "paper_id": paper["paper_id"],
                "model": DEFAULT_MODEL,
                "model_options": extra_body_for_model(DEFAULT_MODEL, enable_reasoning=True),
                "max_completion_tokens": MAX_COMPLETION_TOKENS,
                "max_total_tokens": MAX_TOTAL_TOKENS,
                "request_timeout_seconds": REQUEST_TIMEOUT_SECONDS,
                "source_sha256": source_hash,
                "prompt_sha256": prompt_hashes,
                "table_id_namespace": "source_environment_ordinal",
                "database_writes": False,
                "chunk_tables": int(_get_meta(database, "chunk_tables")),
            },
            "facts": facts.model_dump(),
            "verification": verification.model_dump(),
            "validated": validated,
            "calls": [call for output in chunk_outputs for call in output.get("calls", [])],
        }
        path = root / "papers" / paper["paper_id"] / "analysis.json"
        write_json(path, analysis)
        with connect(database) as db:
            db.execute(
                "UPDATE papers SET status='ready', analysis_path=?, updated_at=? WHERE paper_id=?",
                (str(path), _now(), paper["paper_id"]),
            )


def _merge_facts(outputs: list[dict]) -> RepetitionFacts:
    proposed = {}
    tables = []
    for output in outputs:
        facts = RepetitionFacts.model_validate(output["facts"])
        for method in facts.proposed_methods:
            key = method.name.strip().casefold()
            prior = proposed.setdefault(key, {"name": method.name, "evidence": []})
            seen = {(e.start_line, e.end_line) for e in prior["evidence"]}
            for evidence in method.evidence:
                if (evidence.start_line, evidence.end_line) not in seen:
                    prior["evidence"].append(evidence.model_dump())
                    seen.add((evidence.start_line, evidence.end_line))
        tables.extend(table.model_dump() for table in facts.tables)
    return RepetitionFacts.model_validate(
        {"proposed_methods": list(proposed.values()), "tables": tables}
    )


def _merge_verification(outputs: list[dict]) -> Verification:
    methods = []
    for output in outputs:
        methods.extend(Verification.model_validate(output["verification"]).model_dump()["methods"])
    return Verification.model_validate({"methods": methods})


def _claim(database: Path, worker_id: str, max_attempts: int) -> sqlite3.Row | None:
    now = datetime.now(UTC)
    lease_until = (now + timedelta(seconds=LEASE_SECONDS)).isoformat()
    with connect(database) as db:
        db.execute("BEGIN IMMEDIATE")
        row = db.execute(
            """SELECT c.* FROM chunks c
               WHERE c.attempts < ? AND c.status IN ('queued','failed')
               ORDER BY c.paper_id, c.chunk_index LIMIT 1""",
            (max_attempts,),
        ).fetchone()
        if row is None:
            db.commit()
            return None
        db.execute(
            """UPDATE chunks SET status='running', attempts=attempts+1,
               worker_id=?, lease_until=?, error=NULL, updated_at=?
               WHERE paper_id=? AND chunk_index=?""",
            (worker_id, lease_until, now.isoformat(), row["paper_id"], row["chunk_index"]),
        )
        db.execute(
            "UPDATE papers SET status='running', updated_at=? WHERE paper_id=? AND status='queued'",
            (now.isoformat(), row["paper_id"]),
        )
        db.execute(
            "UPDATE papers SET status='running', error=NULL, updated_at=? "
            "WHERE paper_id=? AND status='failed'",
            (now.isoformat(), row["paper_id"]),
        )
        db.commit()
        return db.execute(
            "SELECT * FROM chunks WHERE paper_id=? AND chunk_index=?",
            (row["paper_id"], row["chunk_index"]),
        ).fetchone()


def _release_orphaned(database: Path, max_attempts: int) -> None:
    """Make interrupted workers' leases immediately resumable under the exclusive lock."""
    now = _now()
    with connect(database) as db:
        db.execute(
            "UPDATE chunks SET status=CASE WHEN attempts >= ? THEN 'failed' ELSE 'queued' END, "
            "worker_id=NULL, lease_until=NULL, updated_at=? WHERE status='running'",
            (max_attempts, now),
        )
        db.execute(
            "UPDATE papers SET status='failed', error='Worker stopped after final attempt', "
            "updated_at=? WHERE status='running' AND paper_id IN "
            "(SELECT paper_id FROM chunks WHERE status='failed')",
            (now,),
        )
        db.execute("UPDATE papers SET status='queued', updated_at=? WHERE status='running'", (now,))


def _mark_papers_with_failed_chunks(database: Path) -> None:
    with connect(database) as db:
        db.execute(
            """UPDATE papers SET status='failed', updated_at=?
               WHERE EXISTS (
                   SELECT 1 FROM chunks c
                   WHERE c.paper_id=papers.paper_id AND c.status='failed'
               )""",
            (_now(),),
        )


def _assert_no_legacy_batch_running() -> None:
    import fcntl

    for path in cfg.papers_dir.glob("repetition_backfill*/batch.lock"):
        with path.open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise RuntimeError(
                    f"A paper-level repetition batch is active ({path.parent}); wait for it to stop"
                ) from None
            fcntl.flock(lock, fcntl.LOCK_UN)


def _finish_chunk(
    database: Path,
    task: sqlite3.Row,
    output_path: str | None,
    error: str | None,
    max_attempts: int,
) -> None:
    status = (
        "complete" if error is None else ("queued" if task["attempts"] < max_attempts else "failed")
    )
    with connect(database) as db:
        db.execute(
            """UPDATE chunks SET status=?, lease_until=NULL, output_path=?, error=?, updated_at=?
               WHERE paper_id=? AND chunk_index=?""",
            (status, output_path, error, _now(), task["paper_id"], task["chunk_index"]),
        )
        if status == "failed":
            db.execute(
                "UPDATE papers SET status='failed', error=?, updated_at=? WHERE paper_id=?",
                (error, _now(), task["paper_id"]),
            )


def _chunk_path(root: Path, paper_id: str, index: int) -> Path:
    return root / "papers" / paper_id / "chunks" / f"{index + 1:03d}"


def _get_meta(database: Path, key: str) -> str:
    with connect(database) as db:
        row = db.execute("SELECT value FROM run_meta WHERE key=?", (key,)).fetchone()
    if row is None:
        raise KeyError(f"Missing run metadata: {key}")
    return row[0]


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _reusable_legacy_analysis(
    folder: Path, source_hash: str, prompt_hashes: dict, paper_id: str
) -> Path | None:
    from backend.repetition_batch import _reusable_analysis

    path = _reusable_analysis(folder, source_hash, prompt_hashes)
    if path is None:
        return None
    try:
        analysis = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return path if analysis.get("provenance", {}).get("paper_id") == paper_id else None


def _now() -> str:
    return datetime.now(UTC).isoformat()
