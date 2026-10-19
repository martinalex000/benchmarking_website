"""Resumable compact mapping with frozen inputs and selectable database application."""

from __future__ import annotations

import csv
import fcntl
import hashlib
import json
import os
import random
import shutil
import sqlite3
import time
from collections import Counter, deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import UTC, datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from threading import Condition, Lock
from zoneinfo import ZoneInfo

from backend.config import cfg
from backend.mapping.audit import write_override_log
from backend.mapping.client import (
    GLM_MODEL,
    SECOND_GLM_FLASH_MODEL,
    SECOND_GLM_FLASH_ROUTE,
    SUPPORTED_MODELS,
    mapping_endpoint_pool,
    preflight_glm,
)
from backend.mapping.client import (
    preflight_model as preflight_mapping_model,
)
from backend.mapping.compact_verification import compact_verification_prompt
from backend.mapping.datasets import load_reviews, reviewed_dataset
from backend.mapping.plan import read_json, validate_proposal
from backend.mapping.schema import stored_rows
from backend.mapping.source import compact_protocols, earlier_matches
from backend.mapping.worker import analyze_chunk, optional_json
from backend.repetition_batch import RequestGate, write_json
from backend.repetition_extractor import DEFAULT_MODEL
from backend.repetition_metadata import (
    RepetitionFacts,
    Verification,
    table_inventory,
    validate_repetitions,
)
from backend.venue import conference_export_fields

PROMPTS = ("result_mapping.txt", "result_mapping_verification.txt")
DELTA_VERIFICATION_PROMPT = "result_mapping_delta_verification.txt"
REQUEST_WINDOWS = {
    # Latest Key 2 response: burst 30/reset 14s, then 30/min, 200/hour,
    # 1000/day, and 3000/month. Keep the burst window separate from minute quota.
    SECOND_GLM_FLASH_ROUTE: ((30, 14), (30, 60), (200, 3600), (1000, 86400), (3000, 2592000))
}
_THROUGHPUT_LOCK = Lock()


class MappingGate(RequestGate):
    """Per-endpoint concurrency caps with per-model adaptation and cooldowns."""

    def __init__(
        self,
        maximum,
        daytime_streams=None,
        now=None,
        models=None,
        persisted_state=None,
        state_path: Path | None = None,
        attempt_journal_path: Path | None = None,
        second_key_maximum=50,
        full_glm_daytime=False,
        minimum_model_limits=None,
    ):
        daytime_streams = maximum if daytime_streams is None else daytime_streams
        if not 1 <= daytime_streams <= maximum <= 20:
            raise ValueError("Require 1 <= daytime streams <= maximum <= 20")
        if not 1 <= second_key_maximum <= 50:
            raise ValueError("Require 1 <= second-key maximum <= 50")
        self.maximum = maximum
        self.daytime_streams = daytime_streams
        self.second_key_maximum = second_key_maximum
        self.full_glm_daytime = full_glm_daytime
        self.now = now or (lambda: datetime.now(ZoneInfo("Europe/Berlin")))
        self.models = set(models or SUPPORTED_MODELS)
        self._endpoint_by_model = {model: mapping_endpoint_pool(model) for model in self.models}
        self._models_by_endpoint = {}
        for model, endpoint in self._endpoint_by_model.items():
            self._models_by_endpoint.setdefault(endpoint, set()).add(model)
        persisted_state = persisted_state or {}
        minimum_model_limits = minimum_model_limits or {}
        for model, minimum in minimum_model_limits.items():
            if model not in self.models or not 1 <= minimum <= self._model_ceiling(model):
                raise ValueError(f"Invalid minimum concurrency for model {model}: {minimum}")
        self._minimum_model_limits = minimum_model_limits
        self._limits = {
            model: min(
                self._model_ceiling(model),
                max(
                    minimum_model_limits.get(model, 1),
                    persisted_state.get("model_limits", {}).get(
                        model,
                        min(
                            2 if model == SECOND_GLM_FLASH_ROUTE else 4,
                            self._model_ceiling(model),
                        ),
                    ),
                ),
            )
            for model in self.models
        }
        self._successes = {
            model: persisted_state.get("successes_by_model", {}).get(model, 0)
            for model in self.models
        }
        self._rate_limits = {
            model: persisted_state.get("rate_limits_by_model", {}).get(model, 0)
            for model in self.models
        }
        self._last_429_at_by_model = dict(persisted_state.get("last_429_at_by_model", {}))
        now_utc = datetime.now(UTC)
        monotonic_now = time.monotonic()
        cooldowns = persisted_state.get("cooldown_until_utc_by_model", {})
        self._cooldowns = {}
        for model in self.models:
            deadline = cooldowns.get(model)
            if deadline:
                try:
                    remaining = max(
                        0.0,
                        (datetime.fromisoformat(deadline) - now_utc).total_seconds(),
                    )
                except (TypeError, ValueError):
                    remaining = 0.0
            else:
                remaining = 0.0
            self._cooldowns[model] = monotonic_now + remaining
        saved_requests = persisted_state.get("request_starts_by_model", {})
        self.state_path = state_path
        self.attempt_journal_path = attempt_journal_path
        self._request_starts = {
            model: deque(
                float(stamp)
                for stamp in saved_requests.get(model, [])
                if isinstance(stamp, (int, float))
            )
            for model in self.models
        }
        self._active_by_model = dict.fromkeys(self.models, 0)
        self._active_by_endpoint = dict.fromkeys(self._models_by_endpoint, 0)
        self.active = 0
        self.condition = Condition()
        self._phase1_pending = 0
        self._phase2_pending = 0

    def _model_ceiling(self, model):
        return self.second_key_maximum if model == SECOND_GLM_FLASH_ROUTE else self.maximum

    def set_phase1_pending(self, count):
        with self.condition:
            self._phase1_pending = max(0, count)
            self.condition.notify_all()

    def phase1_finished(self):
        with self.condition:
            self._phase1_pending = max(0, self._phase1_pending - 1)
            self._phase2_pending += 1
            self.condition.notify_all()

    def phase2_finished(self):
        with self.condition:
            self._phase2_pending = max(0, self._phase2_pending - 1)
            self.condition.notify_all()

    def phase1_pending(self):
        with self.condition:
            return self._phase1_pending

    def phase2_pending(self):
        with self.condition:
            return self._phase2_pending

    def phase2_model(self, preferred_model, fact_model=None):
        """Spend key 2 on verification only after all queued fact work is done."""
        if fact_model == SECOND_GLM_FLASH_ROUTE:
            return preferred_model
        if self.phase1_pending() == 0 and self.can_schedule(SECOND_GLM_FLASH_ROUTE):
            return SECOND_GLM_FLASH_ROUTE
        if self.phase2_pending() > 30 and self.can_schedule(DEFAULT_MODEL):
            return DEFAULT_MODEL
        if preferred_model == GLM_MODEL:
            return GLM_MODEL
        if self.can_schedule(DEFAULT_MODEL):
            return DEFAULT_MODEL
        return preferred_model

    def for_model(self, model):
        if model not in self.models:
            raise ValueError(f"Model is not configured for this run: {model}")
        return _ModelGate(self, model)

    def _model_enabled(self, model):
        if model != GLM_MODEL or self.full_glm_daytime:
            return True
        hour = self.now().astimezone(ZoneInfo("Europe/Berlin")).hour
        return hour >= 18 or hour < 8

    def model_enabled(self, model):
        return model in self.models and self._model_enabled(model)

    def can_schedule(self, model):
        with self.condition:
            return (
                self._model_enabled(model)
                and self._active_by_model[model] < self._limits[model]
                and self._active_by_endpoint[self._endpoint_by_model[model]]
                < self._current_endpoint_limit(self._endpoint_by_model[model])
                and time.monotonic() >= self._cooldowns[model]
                and self._request_wait_seconds(model, time.time()) == 0
            )

    def model_limit(self, model):
        with self.condition:
            return min(
                self._limits[model],
                self._current_endpoint_limit(self._endpoint_by_model[model]),
            )

    def paper_task_limit(self, model, fact_model=None):
        """Allow key-2 fact work to queue ahead of the separately gated verifier."""
        limit = self.model_limit(model)
        if fact_model == SECOND_GLM_FLASH_ROUTE:
            return limit + self.second_key_maximum
        return limit

    def _current_endpoint_limit(self, endpoint):
        if endpoint == "second-key":
            return self.second_key_maximum
        if not any(self._model_enabled(model) for model in self._models_by_endpoint[endpoint]):
            return 0
        hour = self.now().astimezone(ZoneInfo("Europe/Berlin")).hour
        if 8 <= hour < 23:
            return min(self.maximum, self.daytime_streams)
        return self.maximum

    @property
    def limit(self):
        with self.condition:
            return sum(
                self._current_endpoint_limit(endpoint) for endpoint in self._models_by_endpoint
            )

    @property
    def rate_limits(self):
        return sum(self._rate_limits.values())

    @property
    def rate_limits_by_model(self):
        return dict(self._rate_limits)

    @property
    def last_429_at(self):
        return max(self._last_429_at_by_model.values(), default=None)

    @property
    def last_429_at_by_model(self):
        return dict(self._last_429_at_by_model)

    @property
    def cooldowns_by_model(self):
        return {
            model: max(0.0, deadline - time.monotonic())
            for model, deadline in self._cooldowns.items()
        }

    @property
    def cooldown_until_utc_by_model(self):
        now_utc = datetime.now(UTC)
        monotonic_now = time.monotonic()
        return {
            model: (now_utc + timedelta(seconds=max(0.0, deadline - monotonic_now))).isoformat()
            for model, deadline in self._cooldowns.items()
            if deadline > monotonic_now
        }

    @property
    def limits_by_model(self):
        return dict(self._limits)

    @property
    def active_by_endpoint(self):
        return dict(self._active_by_endpoint)

    @property
    def limits_by_endpoint(self):
        return {
            endpoint: self._current_endpoint_limit(endpoint)
            for endpoint in self._models_by_endpoint
        }

    @property
    def endpoint_count(self):
        return len(self._models_by_endpoint)

    @property
    def maximum_workers(self):
        return sum(
            self.second_key_maximum if endpoint == "second-key" else self.maximum
            for endpoint in self._models_by_endpoint
        )

    @property
    def paper_worker_capacity(self):
        """Keep fact-stage workers available while other papers await verification."""
        return sum(
            self.paper_task_limit(model, SECOND_GLM_FLASH_ROUTE)
            for model in self.models
            if model != SECOND_GLM_FLASH_ROUTE and self._model_enabled(model)
        )

    @property
    def successes_by_model(self):
        return dict(self._successes)

    @property
    def request_starts_by_model(self):
        now = time.time()
        history = {}
        for model, starts in self._request_starts.items():
            windows = REQUEST_WINDOWS.get(model, ())
            retention = max((window for _limit, window in windows), default=0)
            history[model] = [stamp for stamp in starts if now - stamp < retention]
        return history

    @property
    def cooldown_until(self):
        return max(self._cooldowns.values(), default=0.0)

    def _enter(self, model, context=None):
        with self.condition:
            while True:
                if (
                    not self._model_enabled(model)
                    or self._active_by_model[model] >= self._limits[model]
                    or self._active_by_endpoint[self._endpoint_by_model[model]]
                    >= self._current_endpoint_limit(self._endpoint_by_model[model])
                    or time.monotonic() < self._cooldowns[model]
                ):
                    self.condition.wait(timeout=1)
                    continue
                delay = self._request_wait_seconds(model, time.time())
                if delay > 0:
                    self.condition.wait(timeout=min(delay, 1))
                    continue
                self.active += 1
                self._active_by_model[model] += 1
                self._active_by_endpoint[self._endpoint_by_model[model]] += 1
                if model in REQUEST_WINDOWS:
                    started_at = time.time()
                    self._request_starts[model].append(started_at)
                    self._persist_request_start(model, started_at)
                else:
                    started_at = time.time()
                self._persist_request_attempt(model, started_at, context or {})
                break

    def _persist_request_start(self, model, started_at):
        if self.state_path is None:
            return
        with self.state_path.open("a") as journal:
            journal.write(f"{model}\t{started_at:.6f}\n")
            journal.flush()
            os.fsync(journal.fileno())

    def _persist_request_attempt(self, model, started_at, context):
        if self.attempt_journal_path is None:
            return
        event = {
            "model_route": model,
            "started_at_epoch": started_at,
            **context,
        }
        with self.attempt_journal_path.open("a") as journal:
            journal.write(json.dumps(event, ensure_ascii=False) + "\n")
            journal.flush()

    def _request_wait_seconds(self, model, now):
        windows = REQUEST_WINDOWS.get(model, ())
        if not windows:
            return 0.0
        starts = self._request_starts[model]
        retention = max(window for _limit, window in windows)
        while starts and now - starts[0] >= retention:
            starts.popleft()
        active = list(starts)
        waits = []
        for limit, window in windows:
            recent = [stamp for stamp in active if now - stamp < window]
            if len(recent) >= limit:
                waits.append(recent[-limit] + window - now)
        return max(waits, default=0.0)

    def _exit(self, model, exc):
        with self.condition:
            self.active -= 1
            self._active_by_model[model] -= 1
            self._active_by_endpoint[self._endpoint_by_model[model]] -= 1
            if getattr(exc, "status_code", None) == 429:
                self._rate_limits[model] += 1
                self._last_429_at_by_model[model] = datetime.now(UTC).isoformat()
                self._successes[model] = 0
                self._limits[model] = max(
                    self._minimum_model_limits.get(model, 1), self._limits[model] - 1
                )
                response = getattr(exc, "response", None)
                retry_after = (
                    response.headers.get("retry-after", "60") if response is not None else "60"
                )
                try:
                    delay = max(1.0, float(retry_after))
                except (TypeError, ValueError):
                    try:
                        delay = max(
                            1.0,
                            (
                                parsedate_to_datetime(retry_after) - datetime.now(UTC)
                            ).total_seconds(),
                        )
                    except (TypeError, ValueError):
                        delay = 60.0
                self._cooldowns[model] = max(self._cooldowns[model], time.monotonic() + delay)
            elif exc is None:
                self._successes[model] += 1
                if self._successes[model] >= 2 * max(1, self._limits[model]):
                    self._limits[model] = min(self._model_ceiling(model), self._limits[model] + 2)
                    self._successes[model] = 0
            self.condition.notify_all()


class _ModelGate:
    def __init__(self, parent, model):
        self.parent = parent
        self.model = model
        self.context = {}

    def set_context(self, **context):
        self.context = dict(context)

    def __enter__(self):
        self.parent._enter(self.model, self.context)
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.parent._exit(self.model, exc)

    @property
    def limit(self):
        return self.parent.model_limit(self.model)


def readonly(database: Path):
    db = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
    db.execute("PRAGMA query_only=ON")
    return db


def read_request_journal(path: Path) -> dict[str, list[float]]:
    history = {}
    if not path.exists():
        return history
    for line in path.read_text().splitlines():
        try:
            model, timestamp = line.split("\t", 1)
            history.setdefault(model, []).append(float(timestamp))
        except ValueError:
            continue
    return history


def implementation_files():
    backend = Path(__file__).resolve().parent.parent
    return list((backend / "mapping").glob("*.py")) + [
        backend / name
        for name in (
            "repetition_metadata.py",
            "repetition_consistency.py",
            "repetition_storage.py",
            "repetition_batch.py",
            "repetition_extractor.py",
            "result_mapping_checks.py",
            "llm_tasks.py",
            "llm_client.py",
            "llm_types.py",
            "llm_model_options.py",
            "llm_backends.py",
            "latex_source.py",
            "config.py",
            "pipeline.py",
        )
    ]


def file_hash(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_revision(manifest: dict, root: Path):
    for path, sha in manifest["implementation_sha256"].items():
        if file_hash(Path(path)) != sha:
            raise ValueError(f"Implementation changed while run is frozen: {path}")
    for name, sha in manifest["prompt_sha256"].items():
        if file_hash(root / "prompts" / name) != sha:
            raise ValueError(f"Frozen prompt changed: {name}")


def check_inputs(manifest: dict, root: Path, paper: dict):
    folder = root / "papers" / paper["paper_id"]
    for name, sha in paper["input_sha256"].items():
        if file_hash(folder / name) != sha:
            raise ValueError(f"Immutable paper input changed: {paper['paper_id']}/{name}")
    source = Path(manifest["papers_dir"]) / paper["paper_id"] / "latex" / "expanded.tex"
    if file_hash(source) != paper["source_sha256"]:
        raise ValueError(f"Local LaTeX changed: {paper['paper_id']}")


def prior_protocols(pid: str, source: str):
    for name in (
        "repetition_backfill_all_stored_results",
        "repetition_backfill_large_budget_retry",
        "repetition_backfill",
    ):
        path = cfg.papers_dir / name / "papers" / pid / "analysis.json"
        if not path.exists():
            continue
        metadata = read_json(path)
        provenance = metadata.get("provenance", {})
        if (
            metadata.get("error")
            or provenance.get("model") != DEFAULT_MODEL
            or provenance.get("source_sha256") != hashlib.sha256(source.encode()).hexdigest()
        ):
            continue
        try:
            facts = RepetitionFacts.model_validate(metadata["facts"])
            verification = Verification.model_validate(metadata["verification"])
            metadata["validated"] = validate_repetitions(facts, verification, source)
            return compact_protocols(metadata)
        except (ValueError, KeyError):
            continue
    return []


def prepare(
    root: Path,
    database: Path,
    papers: Path,
    *,
    parent=None,
    ids=None,
    count=None,
    seed=20261009,
    chunk_size=15,
    daytime_streams=None,
    maximum=None,
    review_roots=(),
    model_assignments=None,
    preferred_fact_model: str | None = None,
    exclusions=None,
    compact_verifier=False,
    full_glm_daytime=False,
    database_mode="apply",
    include_nonconference=False,
    second_key_only=False,
):
    if root.exists():
        raise ValueError("Preparation never overwrites an existing run; resume it instead")
    if chunk_size < 1:
        raise ValueError("Chunk size must be positive")
    if database_mode not in {"apply", "collect-only"}:
        raise ValueError("database_mode must be 'apply' or 'collect-only'")
    model_assignments = dict(model_assignments or {})
    exclusions = dict(exclusions or {})
    if set(model_assignments.values()) - SUPPORTED_MODELS:
        raise ValueError("A paper is assigned to an unsupported mapping model")
    if preferred_fact_model is not None and preferred_fact_model not in SUPPORTED_MODELS:
        raise ValueError("Unsupported phase-1 facts model")
    with readonly(database) as db:
        db.execute("BEGIN")
        cohort = []
        scoped_out = []
        if parent:
            selected = read_json(parent / "manifest.json")["papers"]
        else:
            selected = [
                dict(zip(("paper_id", "title", "venue", "published_date"), row, strict=True))
                for row in db.execute(
                    "SELECT p.arxiv_id,p.title,p.venue,p.published_date FROM papers p "
                    "WHERE p.arxiv_id IS NOT NULL AND EXISTS(SELECT 1 FROM results r WHERE r.paper_id=p.id) ORDER BY p.arxiv_id"
                )
            ]
        for paper in selected:
            pid = paper["paper_id"]
            if ids and pid not in ids:
                continue
            if (
                not parent
                and not include_nonconference
                and not conference_export_fields(paper.get("venue"), paper.get("published_date"))[
                    "published_conference"
                ]
            ):
                continue
            rows = stored_rows(db, pid)
            if pid in exclusions:
                scoped_out.append({**paper, "reason": exclusions[pid], "rows": rows})
                continue
            source_path = papers / pid / "latex" / "expanded.tex"
            if not source_path.exists():
                if parent:
                    raise ValueError(f"Missing local source for frozen cohort: {pid}")
                scoped_out.append(
                    {
                        **paper,
                        "reason": "missing_expanded_latex",
                        "rows": rows,
                    }
                )
                continue
            source = source_path.read_text()
            tables = table_inventory(source)
            if not tables:
                scoped_out.append(
                    {
                        **paper,
                        "reason": "no_detected_result_tables",
                        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
                        "rows": rows,
                    }
                )
                continue
            if parent and (
                rows != read_json(parent / "papers" / pid / "rows.json")
                or source != (parent / "papers" / pid / "source.tex").read_text()
            ):
                raise ValueError(f"Frozen cohort changed: {pid}")
            if rows:
                cohort.append((paper, rows, source, tables))
        if ids and (set(ids) - set(exclusions)) != {p[0]["paper_id"] for p in cohort}:
            raise ValueError("Requested papers are not all eligible or locally available")
        if set(exclusions) - {paper["paper_id"] for paper in selected}:
            raise ValueError("An exclusion is outside the selected cohort")
        if set(model_assignments) - {paper[0]["paper_id"] for paper in cohort}:
            raise ValueError("A model assignment is outside the included cohort")
        if count is not None:
            cohort = random.Random(seed).sample(cohort, count)
        if not cohort:
            raise ValueError("No eligible papers")
        maximum = len(cohort) if maximum is None else maximum
        daytime_streams = maximum if daytime_streams is None else daytime_streams
        MappingGate(maximum, daytime_streams)
        root.mkdir(parents=True)
        (root / "prompts").mkdir()
        prompt_names = PROMPTS + ((DELTA_VERIFICATION_PROMPT,) if compact_verifier else ())
        for name in PROMPTS:
            shutil.copy2(
                Path(__file__).resolve().parent.parent / "prompts" / name, root / "prompts" / name
            )
        if compact_verifier:
            full_prompt = (root / "prompts" / "result_mapping_verification.txt").read_text()
            (root / "prompts" / DELTA_VERIFICATION_PROMPT).write_text(
                compact_verification_prompt(full_prompt)
            )
        manifest = {
            "model": DEFAULT_MODEL,
            "models": sorted(
                {model_assignments.get(paper["paper_id"], DEFAULT_MODEL) for paper, *_ in cohort}
                | ({preferred_fact_model} if preferred_fact_model else set())
            ),
            "preferred_fact_model": preferred_fact_model,
            "reasoning": True,
            "compact_verifier": compact_verifier,
            "database_mode": database_mode,
            "include_nonconference": include_nonconference,
            "second_key_only": second_key_only,
            "database": str(database.resolve()),
            "papers_dir": str(papers.resolve()),
            "chunk_size": chunk_size,
            "daytime_streams": daytime_streams,
            "full_glm_daytime": full_glm_daytime,
            "maximum": maximum,
            "seed": seed,
            "parent": str(parent.resolve()) if parent else None,
            "papers": [],
            "implementation_sha256": {
                str(p.resolve()): file_hash(p) for p in implementation_files()
            },
            "prompt_sha256": {name: file_hash(root / "prompts" / name) for name in prompt_names},
        }
        implementation = root / "implementation"
        implementation.mkdir()
        backend = Path(__file__).resolve().parent.parent
        for source_file in implementation_files():
            target = implementation / source_file.relative_to(backend)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, target)
        imported_reviews = {"protocols": 0, "datasets": 0}
        for paper, rows, source, tables in cohort:
            pid = paper["paper_id"]
            folder = root / "papers" / pid
            folder.mkdir(parents=True)
            (folder / "source.tex").write_text(source)
            keys = []
            reviews = []
            dataset_records = []
            if parent:
                old = parent / "papers" / pid
                keys = read_json(old / "protocol_keys.json")
                reviews = optional_json(old, "reviewed_protocols.json", [])
                dataset_records = optional_json(old, "reviewed_datasets.json", [])
            else:
                keys = prior_protocols(pid, source)
                reviews = []
                dataset_records = []
                for review_root in review_roots:
                    old = Path(review_root) / "papers" / pid
                    for filename, target in (
                        ("reviewed_protocols.json", reviews),
                        ("reviewed_datasets.json", dataset_records),
                    ):
                        review_file = old / filename
                        if not review_file.exists():
                            continue
                        for record in read_json(review_file):
                            if record.get("reviewer") == "human_user" and record not in target:
                                target.append(record)
                imported_reviews["protocols"] += len(reviews)
                imported_reviews["datasets"] += len(dataset_records)
            if {record.get("result_id") for record in dataset_records} - {
                row["result_id"] for row in rows
            }:
                raise ValueError("Dataset review contains out-of-cohort result IDs")
            hint_rows = []
            for row in rows:
                record = reviewed_dataset(row, source, dataset_records)
                if record:
                    target = db.execute(
                        "SELECT name FROM datasets WHERE id=?", (record["corrected_dataset_id"],)
                    ).fetchone()
                    if target is None or target[0] != record["corrected_dataset"]:
                        raise ValueError("Approved target dataset is not uniquely registered")
                    hint_rows.append({**row, "dataset": record["corrected_dataset"]})
                else:
                    hint_rows.append(row)
            for name, value in (
                ("rows.json", rows),
                ("protocol_keys.json", keys),
                ("reviewed_protocols.json", reviews),
                ("reviewed_datasets.json", dataset_records),
                ("earlier_matches.json", earlier_matches(db, pid, hint_rows)),
            ):
                write_json(folder / name, value)
            manifest["papers"].append(
                {
                    **paper,
                    "model": model_assignments.get(pid, DEFAULT_MODEL),
                    "preferred_fact_model": preferred_fact_model,
                    "rows": len(rows),
                    "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
                    "table_count": len(tables),
                    "input_sha256": {p.name: file_hash(p) for p in folder.iterdir() if p.is_file()},
                }
            )
        write_json(
            root / "scope.json",
            {
                "definition": "Published-conference papers with stored results and local expanded LaTeX",
                "candidate_papers": len(cohort) + len(scoped_out),
                "included_papers": [
                    {"paper_id": paper["paper_id"], "rows": len(rows), "tables": len(tables)}
                    for paper, rows, _source, tables in cohort
                ],
                "excluded_papers": scoped_out,
                "human_reviews_imported": imported_reviews,
            },
        )
    write_json(root / "manifest.json", manifest)
    write_json(
        root / "status.json",
        {
            "state": "prepared",
            "phase": "mapping",
            "completed": 0,
            "total": len(cohort),
            "database_modified": False,
            "scope_unchanged": None,
        },
    )
    refresh_throughput_report(root)
    return manifest


def build_chunk_tasks(papers, root, chunk_size):
    tasks = []
    counts = {}
    for paper in papers:
        pid = paper["paper_id"]
        rows = read_json(root / "papers" / pid / "rows.json")
        count = (len(rows) + chunk_size - 1) // chunk_size
        counts[pid] = count
        for chunk_index in range(count):
            start = chunk_index * chunk_size
            tasks.append(
                {
                    "paper": paper,
                    "chunk_index": chunk_index,
                    "rows": rows[start : start + chunk_size],
                }
            )
    tasks.sort(
        key=lambda task: (
            task["paper"].get("priority_rank", 1),
            task["chunk_index"],
            task["paper"]["paper_id"],
        )
    )
    return tasks, counts


def analyze_paper_chunk(paper, root, manifest, gate, chunk_index):
    pid = paper["paper_id"]
    model = paper.get("model", manifest["model"])
    fact_model = paper.get("fact_model") or model
    folder = root / "papers" / pid
    source = (folder / "source.tex").read_text()
    rows = read_json(folder / "rows.json")
    offset = chunk_index * manifest["chunk_size"]
    subset = rows[offset : offset + manifest["chunk_size"]]
    chunk = folder / "chunks" / f"{chunk_index + 1:03d}"
    if not subset:
        raise ValueError(f"Chunk {chunk_index + 1} has no rows for {pid}")
    dataset_records = load_reviews(folder, paper)
    errors = []

    def analyze(chunk, subset, phase1_finished, phase2_finished):
        options = {"compact_verifier": True} if manifest.get("compact_verifier") else {}
        if model != DEFAULT_MODEL:
            options["model"] = model
        if fact_model != model:
            options["fact_model"] = fact_model
        options["phase1_finished"] = phase1_finished
        options["phase2_finished"] = phase2_finished
        return analyze_chunk(chunk, pid, subset, source, root / "prompts", gate, **options)

    check_revision(manifest, root)
    check_inputs(manifest, root, paper)
    chunk.mkdir(parents=True, exist_ok=True)
    chunk_started_at = datetime.now(UTC)
    chunk_state = "complete"
    phase1_done = False
    phase2_done = False

    def mark_phase1_done():
        nonlocal phase1_done
        if not phase1_done:
            gate.phase1_finished()
            phase1_done = True

    def mark_phase2_done():
        nonlocal phase2_done
        if not phase2_done:
            gate.phase2_finished()
            phase2_done = True

    try:
        path = chunk / "proposals.json"
        if path.exists():
            result = read_json(path)
            try:
                if len(result) != len(subset) or {r["result_id"] for r in result} != {
                    r["result_id"] for r in subset
                }:
                    raise ValueError("Cached chunk has incomplete or duplicate result coverage")
                if any(
                    "same_experiment_candidate_omitted" in row.get("validation_errors", [])
                    for row in result
                ):
                    raise ValueError(
                        "Cached chunk omitted a same-experiment candidate and needs replay"
                    )
                for row in result:
                    validate_proposal(
                        row,
                        source,
                        optional_json(folder, "reviewed_protocols.json", []),
                        dataset_records,
                    )
            except ValueError:
                path.rename(
                    chunk
                    / f"invalid_proposals_{datetime.now(UTC).strftime('%Y%m%dT%H%M%S%f')}.json"
                )
                result = analyze(chunk, subset, mark_phase1_done, mark_phase2_done)
        else:
            result = analyze(chunk, subset, mark_phase1_done, mark_phase2_done)
        for row in result:
            validate_proposal(
                row,
                source,
                optional_json(folder, "reviewed_protocols.json", []),
                dataset_records,
            )
    except Exception as exc:
        chunk_state = "failed"
        errors.append({"chunk": chunk.name, "error": f"{type(exc).__name__}: {exc}"})
        result = [
            {
                **row,
                "action": "call_failed",
                "proposed_num_runs": None,
                "correction": None,
                "error": str(exc),
            }
            for row in subset
        ]
    finally:
        mark_phase1_done()
        mark_phase2_done()
    chunk_finished_at = datetime.now(UTC)
    write_json(
        chunk / "chunk_complete.json",
        {
            "paper_id": pid,
            "chunk": chunk.name,
            "state": chunk_state,
            "started_at_utc": chunk_started_at.isoformat(),
            "completed_at_utc": chunk_finished_at.isoformat(),
        },
    )
    refresh_throughput_report(root, gate=gate)
    return {
        "chunk_index": chunk_index,
        "state": chunk_state,
        "model": model,
        "fact_model": fact_model,
        "errors": errors,
        "proposals": result,
    }


def assemble_paper_result(paper, root, chunk_results):
    pid = paper["paper_id"]
    proposals = []
    errors = []
    for chunk_index in sorted(chunk_results):
        chunk_result = chunk_results[chunk_index]
        proposals.extend(chunk_result["proposals"])
        errors.extend(chunk_result["errors"])
    write_json(root / "papers" / pid / "proposals.json", proposals)
    models = sorted({result["model"] for result in chunk_results.values()})
    fact_models = sorted({result["fact_model"] for result in chunk_results.values()})
    result = {
        "state": "failed" if errors else "complete",
        "completed_at_utc": datetime.now(UTC).isoformat(),
        "model": models[0] if len(models) == 1 else "mixed",
        "fact_model": fact_models[0] if len(fact_models) == 1 else "mixed",
        "models_used": models,
        "fact_models_used": fact_models,
        "errors": errors,
        "rows": len(proposals),
        "actions": dict(Counter(r["action"] for r in proposals)),
    }
    write_json(root / "papers" / pid / "assessment.json", result)
    return result


def _apply_paper_if_enabled(root, manifest, paper, assessment):
    if manifest.get("database_mode", "collect-only") != "apply":
        return assessment
    from backend.mapping.storage import apply_completed_paper

    try:
        receipt = apply_completed_paper(Path(manifest["database"]), root, manifest, paper)
        assessment["database_application"] = {
            "status": "applied",
            "plan_id": receipt["plan_id"],
            "applied_at": receipt["applied_at"],
            "rows_changed": len(receipt["rows"]),
            "already_applied": bool(receipt.get("already_applied")),
        }
    except Exception as exc:
        assessment["database_application"] = {
            "status": "failed",
            "error": f"{type(exc).__name__}: {exc}",
        }
    application = assessment["database_application"]
    print(
        f"{paper['paper_id']} paper database={application['status']} "
        f"rows_changed={application.get('rows_changed', 0)}",
        flush=True,
    )
    write_json(root / "papers" / paper["paper_id"] / "assessment.json", assessment)
    return assessment


def _database_application_ok(assessment):
    return assessment.get("database_application", {}).get("status") == "applied"


def _compact_token_count(value):
    count = int(value or 0)
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}".removesuffix(".0") + "M"
    if count >= 1_000:
        return f"{count / 1_000:.1f}".removesuffix(".0") + "k"
    return str(count)


def _chunk_token_usage(root, paper_id, chunk_index):
    totals = {"prompt": 0, "completion": 0}
    chunk = root / "papers" / paper_id / "chunks" / f"{chunk_index + 1:03d}"
    for path in chunk.rglob("*_call.json"):
        try:
            call = read_json(path)
            totals["prompt"] += int(call.get("prompt_tokens") or 0)
            totals["completion"] += int(call.get("completion_tokens") or 0)
        except (OSError, ValueError, TypeError):
            continue
    return totals


def _since_last_429(value):
    if not value:
        return "--:--:--"
    try:
        last = datetime.fromisoformat(value.replace("Z", "+00:00"))
        seconds = max(0, int((datetime.now(UTC) - last.astimezone(UTC)).total_seconds()))
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    except (AttributeError, ValueError):
        return "??:??:??"


def _log_mapping_chunk(
    root, paper_id, chunk_index, chunk_count, result, elapsed, gate, open_work, active_tasks
):
    usage = _chunk_token_usage(root, paper_id, chunk_index)
    duration = max(0.001, elapsed)
    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    output_rate = usage["completion"] / duration
    state = result.get("state", "failed")
    print(
        f"{paper_id} chunk {chunk_index + 1:03d}/{chunk_count:03d} {state:<8} "
        f"open={open_work:5d} tasks={active_tasks:3d} req={gate.active:3d} "
        f"elapsed={hours:02d}:{minutes:02d}:{seconds:02d} "
        f"in={_compact_token_count(usage['prompt']):>7} "
        f"out={_compact_token_count(usage['completion']):>7} "
        f"out/s={output_rate:8.1f} last429={_since_last_429(gate.last_429_at)}",
        flush=True,
    )


def _utc_datetime(value, fallback_path):
    try:
        moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError):
        moment = datetime.fromtimestamp(fallback_path.stat().st_mtime, UTC)
    return moment.replace(tzinfo=UTC) if moment.tzinfo is None else moment.astimezone(UTC)


def _successful_paper_events(root):
    events = []
    for path in (root / "papers").glob("*/assessment.json"):
        try:
            assessment = read_json(path)
        except (OSError, ValueError):
            continue
        if assessment.get("state") == "complete" and assessment.get("errors") == []:
            completed = _utc_datetime(assessment.get("completed_at_utc"), path)
            events.append((completed, path.parent.name))
    return sorted(events)


def _write_mapping_plots(root):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    current_events = _successful_paper_events(root)
    parent_path = None
    manifest_path = root / "manifest.json"
    if manifest_path.exists():
        parent = read_json(manifest_path).get("parent")
        if parent:
            parent_path = Path(parent)
    parent_events = (
        _successful_paper_events(parent_path) if parent_path and parent_path.is_dir() else []
    )

    progress_rows = []
    figure, axis = plt.subplots(figsize=(12, 6))
    for label, events, style in (
        ("All verified papers", current_events, "-"),
        ("Parent run completions", parent_events, "--"),
    ):
        if label == "Parent run completions" and not parent_events:
            continue
        if not events:
            continue
        times = [item[0] for item in events]
        counts = list(range(1, len(times) + 1))
        axis.step([times[0], *times], [0, *counts], where="post", linestyle=style, label=label)
        progress_rows.extend(
            {"series": label, "completed_at_utc": timestamp.isoformat(), "cumulative_papers": n}
            for n, (timestamp, _paper_id) in enumerate(events, start=1)
        )
    axis.set_title("Cumulative successful paper completions")
    axis.set_xlabel("Assessment completion time (UTC)")
    axis.set_ylabel("Successfully assessed papers (cumulative count)")
    axis.grid(True, alpha=0.25)
    if current_events or parent_events:
        axis.legend()
    figure.autofmt_xdate()
    figure.tight_layout()
    figure.savefig(root / "completion_progress.png", dpi=150)
    plt.close(figure)
    with (root / "completion_progress.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=("series", "completed_at_utc", "cumulative_papers")
        )
        writer.writeheader()
        writer.writerows(progress_rows)

    manifest = read_json(manifest_path) if manifest_path.exists() else {}
    planned_models = set(manifest.get("models", []))
    planned_models.update(
        model
        for model in (
            manifest.get("phase1_fallback_model"),
            manifest.get("phase2_preferred_model"),
            manifest.get("preferred_fact_model"),
        )
        if model
    )
    for paper in manifest.get("papers", []):
        planned_models.update(
            model
            for model in (
                paper.get("model"),
                paper.get("fact_model"),
                paper.get("preferred_fact_model"),
            )
            if model
        )
    planned_models = {
        SECOND_GLM_FLASH_MODEL if model == SECOND_GLM_FLASH_ROUTE else model
        for model in planned_models
    }
    model_buckets = {}
    for path in (root / "papers").glob("*/chunks/**/*_call.json"):
        try:
            record = read_json(path)
            if not record.get("success") or not record.get("completion_tokens"):
                continue
            finished = _utc_datetime(record.get("finished_at_utc"), path)
            minute = int(finished.timestamp() // 60)
            model = record.get("model") or record.get("model_route") or "unknown"
            model_buckets[(minute, model)] = model_buckets.get((minute, model), 0) + int(
                record["completion_tokens"]
            )
        except (OSError, ValueError, TypeError):
            continue

    models = sorted(planned_models | {model for _minute, model in model_buckets})
    minutes = [minute for minute, _model in model_buckets]
    throughput_rows = []
    if minutes:
        minute_range = range(min(minutes), max(minutes) + 1)
        figure, axis = plt.subplots(figsize=(12, 6))
        for model in models:
            points = [model_buckets.get((minute, model), 0) / 60 for minute in minute_range]
            axis.plot(
                [datetime.fromtimestamp(minute * 60, UTC) for minute in minute_range],
                points,
                label=model,
            )
            throughput_rows.extend(
                {
                    "minute_utc": datetime.fromtimestamp(minute * 60, UTC).isoformat(),
                    "model": model,
                    "output_tokens": model_buckets.get((minute, model), 0),
                    "output_tokens_per_second": model_buckets.get((minute, model), 0) / 60,
                }
                for minute in minute_range
            )
        axis.set_title("Output-token throughput by model")
        axis.set_xlabel("Call completion time (UTC; 60-second bins)")
        axis.set_ylabel("Output tokens per second")
        axis.grid(True, alpha=0.25)
        axis.legend(title="Model")
        figure.autofmt_xdate()
        figure.tight_layout()
        figure.savefig(root / "throughput.png", dpi=150)
        plt.close(figure)
    else:
        figure, axis = plt.subplots(figsize=(12, 6))
        axis.set_title("Output-token throughput by model")
        axis.set_xlabel("Call completion time (UTC; 60-second bins)")
        axis.set_ylabel("Output tokens per second")
        axis.text(0.5, 0.5, "No successful output-token records yet", ha="center", va="center")
        figure.tight_layout()
        figure.savefig(root / "throughput.png", dpi=150)
        plt.close(figure)
    with (root / "throughput.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=("minute_utc", "model", "output_tokens", "output_tokens_per_second"),
        )
        writer.writeheader()
        writer.writerows(throughput_rows)


def progress(root, manifest, results, gate, state="running"):
    completed = len(results)
    failed = sum(
        bool(r.get("errors"))
        or r.get("state") != "complete"
        or r.get("database_application", {}).get("status") == "failed"
        for r in results.values()
    )
    applied = sum(
        result.get("database_application", {}).get("status") == "applied"
        for result in results.values()
    )
    status = {
        "state": state,
        "phase": "mapping",
        "updated_at": datetime.now(UTC).isoformat(),
        "pid": os.getpid(),
        "completed": completed,
        "successful": completed - failed,
        "failed": failed,
        "total": len(manifest["papers"]),
        "model_assignments": dict(
            Counter(paper.get("model", manifest["model"]) for paper in manifest["papers"])
        ),
        "fact_model_assignments": dict(
            Counter(
                paper.get("fact_model")
                or paper.get("preferred_fact_model")
                or paper.get("model", manifest["model"])
                for paper in manifest["papers"]
            )
        ),
        "results": results,
        "active_streams": gate.active,
        "stream_limit": gate.limit,
        "rate_limits": gate.rate_limits,
        "rate_limits_by_model": gate.rate_limits_by_model,
        "last_429_at_by_model": gate.last_429_at_by_model,
        "cooldowns_by_model": gate.cooldowns_by_model,
        "cooldown_until_utc_by_model": gate.cooldown_until_utc_by_model,
        "model_limits": gate.limits_by_model,
        "phase1_pending_chunks": gate.phase1_pending(),
        "phase2_pending_chunks": gate.phase2_pending(),
        "active_by_endpoint": gate.active_by_endpoint,
        "endpoint_limits": gate.limits_by_endpoint,
        "successes_by_model": gate.successes_by_model,
        "throughput_rows_per_second": manifest.get("historical_throughput_rows_per_second", {}),
        "cooldown_remaining_seconds": max(0.0, gate.cooldown_until - time.monotonic()),
        "database_mode": manifest.get("database_mode", "collect-only"),
        "database_modified": applied > 0,
        "database_application_verified": (
            all(
                _database_application_ok(result)
                for result in results.values()
                if result.get("state") == "complete" and not result.get("errors")
            )
            if manifest.get("database_mode") == "apply"
            else None
        ),
        "pipeline_terminal": False,
    }
    write_json(root / "status.json", status)
    (root / "summary.md").write_text(
        "# Result-mapping progress\n\n"
        f"{completed}/{status['total']} papers completed: {status['successful']} successful, {failed} failed.\n\n"
        f"{gate.active} active requests; limit {gate.limit}; {gate.rate_limits} rate-limit responses.\n\n"
        + (
            "Per-paper database application is enabled.\n"
            if manifest.get("database_mode") == "apply"
            else "Collected proposals; the database remains unchanged until apply.\n"
        )
        + "Dispositions are not accuracy; unknowns and failed calls are separate.\n"
    )
    return status


def refresh_throughput_report(root: Path, chunk_window: int = 10, gate=None) -> None:
    """Publish recent per-endpoint request and completion-token throughput."""
    with _THROUGHPUT_LOCK:
        _write_mapping_plots(root)
        markers = []
        for path in (root / "papers").glob("*/chunks/*/chunk_complete.json"):
            try:
                marker = read_json(path)
                if marker.get("state") == "complete":
                    marker["path"] = path.parent
                    markers.append(marker)
            except (OSError, ValueError):
                continue
        markers.sort(key=lambda item: item["completed_at_utc"])
        selected = markers[-chunk_window:]
        lines = [
            "# Recent endpoint throughput",
            "",
            f"Generated: {datetime.now(UTC).isoformat()}.",
            "",
            "Plots: [papers over time](completion_progress.png) · "
            "[output tokens/s by model](throughput.png).",
            "Data: `completion_progress.csv` and `throughput.csv`.",
            "",
        ]
        phase_chunks = {"Phase 1 — facts": {}, "Phase 2 — verifier": {}}
        if selected:
            chunk_paths = {item["path"] for item in selected}
            chunk_ids = {path.relative_to(root).as_posix() for path in chunk_paths}
            start_times = [datetime.fromisoformat(item["started_at_utc"]) for item in selected]
            end_times = [datetime.fromisoformat(item["completed_at_utc"]) for item in selected]
            window_seconds = max(0.001, (max(end_times) - min(start_times)).total_seconds())
            totals = {}

            def bucket(endpoint, model):
                return totals.setdefault(
                    endpoint,
                    {
                        "models": set(),
                        "requests": 0,
                        "tokens": 0,
                        "generation_seconds": 0.0,
                    },
                )

            journal = root / "request_attempts.jsonl"
            if journal.exists():
                for line in journal.read_text().splitlines():
                    try:
                        event = json.loads(line)
                    except ValueError:
                        continue
                    if event.get("chunk") not in chunk_ids:
                        continue
                    started = event.get("started_at_epoch")
                    if (
                        started is not None
                        and not min(start_times).timestamp()
                        <= started
                        <= max(end_times).timestamp()
                    ):
                        continue
                    model_name = event.get("model", event.get("model_route", "unknown"))
                    values = bucket(event.get("endpoint", "unknown"), model_name)
                    values["models"].add(model_name)
                    values["requests"] += 1

            response_records = 0
            for chunk in chunk_paths:
                for path in chunk.rglob("*_call.json"):
                    try:
                        record = read_json(path)
                    except (OSError, ValueError):
                        continue
                    finished_at = record.get("finished_at_utc")
                    try:
                        finished_at = datetime.fromisoformat(finished_at)
                    except (TypeError, ValueError):
                        continue
                    if not min(start_times) <= finished_at <= max(end_times):
                        continue
                    values = bucket(
                        record.get("endpoint", "unknown"), record.get("model", "unknown")
                    )
                    values["models"].add(record.get("model", "unknown"))
                    tokens = int(record.get("completion_tokens") or 0)
                    generation_speed = float(record.get("tokens_per_sec") or 0)
                    values["tokens"] += tokens
                    if tokens and generation_speed > 0:
                        values["generation_seconds"] += tokens / generation_speed
                    response_records += 1

            for marker in markers:
                chunk = marker["path"]
                chunk_id = chunk.relative_to(root).as_posix()
                for path in chunk.rglob("*_call.json"):
                    try:
                        record = read_json(path)
                    except (OSError, ValueError):
                        continue
                    if not record.get("success"):
                        continue
                    stage = record.get("stage") or record.get("call_type") or ""
                    phase = (
                        "Phase 1 — facts"
                        if stage == "mapping_facts"
                        else "Phase 2 — verifier"
                        if stage in {"mapping_delta_verifier", "mapping_verifier"}
                        else None
                    )
                    if phase:
                        endpoint = record.get("endpoint", "unknown")
                        phase_chunks[phase].setdefault(endpoint, set()).add(chunk_id)

            lines.extend(
                [
                    f"Window: latest {len(selected)} completed chunks, "
                    f"{min(start_times).strftime('%Y-%m-%d %H:%M:%S UTC')}–"
                    f"{max(end_times).strftime('%Y-%m-%d %H:%M:%S UTC')}.",
                    "Requests/min includes all transport attempts. Output tok/s is received "
                    "completion tokens over the shared wall-clock window; decode tok/s is "
                    "weighted by reported generation speed.",
                    "",
                    "| Endpoint route | Models used | Requests/min | Requests | Output tokens | "
                    "Output tok/s | Decode tok/s |",
                    "|---|---|---:|---:|---:|---:|---:|",
                ]
            )
            for endpoint, values in sorted(totals.items()):
                decode_seconds = values["generation_seconds"]
                decode_speed = (
                    f"{values['tokens'] / decode_seconds:.2f}" if decode_seconds else "n/a"
                )
                lines.append(
                    f"| {endpoint} | {', '.join(sorted(values['models'])) or '—'} | "
                    f"{values['requests'] * 60 / window_seconds:.2f} | "
                    f"{values['requests']} | {values['tokens']} | "
                    f"{values['tokens'] / window_seconds:.2f} | {decode_speed} |"
                )
            if not totals:
                lines.append("| No endpoint calls recorded | — | 0 | 0 | 0 | 0 | n/a |")
            lines.extend(
                [
                    "",
                    f"Saved response records in this window: {response_records}.",
                    "",
                ]
            )
        else:
            lines.append("No completed chunks yet; throughput metrics are not available.")

        if gate is not None:
            limit_snapshot = {
                "updated_at": datetime.now(UTC).isoformat(),
                "active_streams": gate.active,
                "endpoint_limits": gate.limits_by_endpoint,
                "model_limits": gate.limits_by_model,
                "rate_limits_by_model": gate.rate_limits_by_model,
                "last_429_at_by_model": gate.last_429_at_by_model,
                "cooldown_remaining_seconds": gate.cooldowns_by_model,
                "phase1_pending_chunks": gate.phase1_pending(),
                "phase2_pending_chunks": gate.phase2_pending(),
            }
        else:
            status_path = root / "status.json"
            status = read_json(status_path) if status_path.exists() else {}
            limit_snapshot = {
                "updated_at": status.get("updated_at", "not recorded"),
                "active_streams": status.get("active_streams", "not recorded"),
                "endpoint_limits": status.get("endpoint_limits", {}),
                "model_limits": status.get("model_limits", {}),
                "rate_limits_by_model": status.get("rate_limits_by_model", {}),
                "last_429_at_by_model": status.get("last_429_at_by_model", {}),
                "cooldown_remaining_seconds": status.get("cooldowns_by_model", {}),
                "phase1_pending_chunks": status.get("phase1_pending_chunks", 0),
                "phase2_pending_chunks": status.get("phase2_pending_chunks", 0),
            }

        manifest_path = root / "manifest.json"
        reported_limits = (
            read_json(manifest_path).get("reported_request_limits")
            if manifest_path.exists()
            else None
        )

        lines.extend(("## Cumulative completed chunks by phase and endpoint", ""))
        lines.extend(("| Phase | Endpoint route | Unique chunks |", "|---|---|---:|"))
        for phase, endpoints in phase_chunks.items():
            if endpoints:
                for endpoint, chunks in sorted(endpoints.items()):
                    lines.append(f"| {phase} | {endpoint} | {len(chunks)} |")
            else:
                lines.append(f"| {phase} | — | 0 |")

        limits_lines = [
            "## Current limits snapshot (worker state and recorded provider headers)",
            "",
            f"Recorded: {limit_snapshot['updated_at']}; active streams: "
            f"{limit_snapshot['active_streams']}.",
            f"Remaining chunks: Phase 1 facts {limit_snapshot['phase1_pending_chunks']}; "
            f"Phase 2 verification {limit_snapshot['phase2_pending_chunks']}; total "
            f"{int(limit_snapshot['phase1_pending_chunks']) + int(limit_snapshot['phase2_pending_chunks'])}.",
            "",
            "| Limit type | Current value |",
            "|---|---|",
            f"| Endpoint caps | `{json.dumps(limit_snapshot['endpoint_limits'], sort_keys=True)}` |",
            f"| Adaptive model caps | `{json.dumps(limit_snapshot['model_limits'], sort_keys=True)}` |",
            f"| 429s by model | `{json.dumps(limit_snapshot['rate_limits_by_model'], sort_keys=True)}` |",
            f"| Cooldown seconds by model | `{json.dumps(limit_snapshot['cooldown_remaining_seconds'], sort_keys=True)}` |",
            f"| Provider-reported request quotas | `{json.dumps(reported_limits, sort_keys=True)}` |",
            "",
        ]
        report = "\n".join(lines + [""] + limits_lines)

        target = root / "throughput.md"
        temporary = target.with_suffix(".md.tmp")
        temporary.write_text(report)
        temporary.replace(target)


def save_preflight(root: Path, result: dict) -> None:
    path = root / "preflight.json"
    attempts = read_json(path).get("attempts", []) if path.exists() else []
    attempts.append(result)
    write_json(path, {"attempts": attempts})
    if result["status"] == "failed":
        status_path = root / "status.json"
        status = read_json(status_path) if status_path.exists() else {}
        status.update(
            state="preflight_failed",
            phase="preflight",
            updated_at=result["checked_at"],
            preflight_error=result["error"],
            pipeline_terminal=False,
        )
        write_json(status_path, status)
        (root / "summary.md").write_text(
            "# Result-mapping progress\n\n"
            "Model preflight failed; no paper calls were started. See `preflight.json` "
            "for the recorded failure.\n"
        )


def run(root: Path):
    manifest = read_json(root / "manifest.json")
    check_revision(manifest, root)
    configured_models = set(manifest.get("models", ())) | {
        paper.get("model", manifest["model"]) for paper in manifest["papers"]
    }
    if (
        not configured_models
        or configured_models - SUPPORTED_MODELS
        or manifest["reasoning"] is not True
    ):
        raise ValueError(
            "This runner supports only the configured GLM and DeepSeek models with thinking"
        )
    prior_status = read_json(root / "status.json")
    quota_state_path = root / "request_quota_starts.jsonl"
    journal_history = read_request_journal(quota_state_path)
    if journal_history:
        prior_status["request_starts_by_model"] = journal_history
    with (root / "batch.lock").open("a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        results, pending = {}, []
        database_mode = manifest.get("database_mode", "collect-only")
        if database_mode not in {"apply", "collect-only", "read_only"}:
            raise ValueError(f"Unsupported database mode: {database_mode}")
        with readonly(Path(manifest["database"])) as db:
            for paper in manifest["papers"]:
                check_inputs(manifest, root, paper)
                assessment_path = root / "papers" / paper["paper_id"] / "assessment.json"
                assessment = read_json(assessment_path) if assessment_path.exists() else {}
                previously_applied = (
                    database_mode == "apply"
                    and assessment.get("state") == "complete"
                    and assessment.get("errors") == []
                )
                if not previously_applied and stored_rows(db, paper["paper_id"]) != read_json(
                    root / "papers" / paper["paper_id"] / "rows.json"
                ):
                    raise ValueError(f"Stored rows changed before resume: {paper['paper_id']}")
            scope = read_json(root / "scope.json")
            scope_unchanged = all(
                stored_rows(db, paper["paper_id"]) == paper["rows"]
                for paper in scope["excluded_papers"]
            )
            if not scope_unchanged:
                raise ValueError("A scoped-out paper's stored rows changed before resume")
        for paper in manifest["papers"]:
            path = root / "papers" / paper["paper_id"] / "assessment.json"
            prior = read_json(path) if path.exists() else None
            if prior and prior.get("state") == "complete" and prior.get("errors") == []:
                prior = _apply_paper_if_enabled(root, manifest, paper, prior)
                results[paper["paper_id"]] = prior
            else:
                if path.exists():
                    archive = (
                        path.parent / "history" / datetime.now(UTC).strftime("%Y%m%dT%H%M%S%f")
                    )
                    archive.mkdir(parents=True)
                    for name in ("assessment.json", "proposals.json"):
                        existing = path.parent / name
                        if existing.exists():
                            shutil.copy2(existing, archive / name)
                pending.append(paper)
        second_key_only = manifest.get("second_key_only", False)
        if second_key_only:
            verifier_models = {SECOND_GLM_FLASH_ROUTE}
            models = {SECOND_GLM_FLASH_ROUTE}
        else:
            verifier_models = {paper.get("model", manifest["model"]) for paper in pending}
            models = set(verifier_models)
            for paper in pending:
                preferred = paper.get("preferred_fact_model")
                if preferred:
                    models.add(preferred)
        phase1_fallback_model = manifest.get("phase1_fallback_model")
        phase2_preferred_model = manifest.get("phase2_preferred_model")
        if not second_key_only:
            verifier_models.add(DEFAULT_MODEL)
            models.add(DEFAULT_MODEL)
        if phase1_fallback_model:
            models.add(phase1_fallback_model)
        if phase2_preferred_model:
            models.add(phase2_preferred_model)
            verifier_models.add(phase2_preferred_model)
        if SECOND_GLM_FLASH_ROUTE in models:
            verifier_models.add(SECOND_GLM_FLASH_ROUTE)
        if not verifier_models:
            verifier_models.add(manifest["model"])
        # Completed artifacts may come from models that are no longer configured
        # or reachable. They are provenance, not a reason to preflight/call them.
        if not models:
            models = {manifest["model"]}
        gate = MappingGate(
            manifest["maximum"],
            manifest["daytime_streams"],
            models=models,
            persisted_state=prior_status,
            state_path=quota_state_path,
            attempt_journal_path=root / "request_attempts.jsonl",
            second_key_maximum=manifest.get("second_key_maximum", 50),
            full_glm_daytime=manifest.get("full_glm_daytime", False),
            minimum_model_limits=manifest.get("minimum_model_limits", {}),
        )
        chunk_results = {paper["paper_id"]: {} for paper in pending}
        chunk_tasks, chunk_counts = build_chunk_tasks(pending, root, manifest["chunk_size"])
        # Interleave chunks by ordinal so large papers release worker slots in
        # bounded units instead of monopolizing them until the whole paper ends.
        queued = deque(chunk_tasks)
        phase1_chunks = len(chunk_tasks)
        gate.set_phase1_pending(phase1_chunks)
        progress(root, manifest, results, gate)
        preflighted = set()
        preflight_failures = Counter()
        preflight_retry_at = {}
        preflight_rate_limited = set()

        def ensure_preflight(model):
            if (
                model in preflighted
                or not gate.model_enabled(model)
                or gate.cooldowns_by_model.get(model, 0) > 0
                or time.monotonic() < preflight_retry_at.get(model, 0)
            ):
                return
            # A closed request window must not block preflight of other routes.
            if not gate.can_schedule(model):
                return
            try:
                result = (
                    preflight_glm(gate)
                    if model == DEFAULT_MODEL
                    else preflight_mapping_model(gate, model)
                )
                result["paper_calls_started"] = False
                save_preflight(root, result)
                preflighted.add(model)
            except Exception as exc:
                preflight_failures[model] += 1
                if getattr(exc, "status_code", None) == 429:
                    preflight_rate_limited.add(model)
                save_preflight(
                    root,
                    {
                        "status": "failed",
                        "checked_at": datetime.now(UTC).isoformat(),
                        "model": model,
                        "error": f"{type(exc).__name__}: {exc}",
                        "paper_calls_started": False,
                    },
                )
                cooldown = gate.cooldowns_by_model.get(model, 0)
                if cooldown:
                    preflight_retry_at[model] = time.monotonic() + cooldown
                else:
                    delay = min(300, 5 * (2 ** (preflight_failures[model] - 1)))
                    preflight_retry_at[model] = time.monotonic() + delay

        if pending:
            for model in sorted(models):
                ensure_preflight(model)
            if (
                not preflighted
                and len(preflight_failures) == len(models)
                and not preflight_rate_limited
            ):
                raise RuntimeError(
                    "Every configured model failed preflight; no paper calls were started"
                )
        with ThreadPoolExecutor(max_workers=gate.paper_worker_capacity) as pool:
            futures = {}
            started = {}
            in_flight_work = Counter()
            in_flight_tasks = Counter()
            paper_assignments = {
                paper["paper_id"]: (paper["model"], paper["fact_model"])
                for paper in pending
                if paper.get("model") and paper.get("fact_model")
            }
            dispatch_log_path = root / "dispatch_log.json"
            dispatch_log = (
                read_json(dispatch_log_path)
                if dispatch_log_path.exists()
                else {"policy": "priority-first adaptive throughput", "assignments": []}
            )
            historical_rates = manifest.get("historical_throughput_rows_per_second", {})
            rates = {model: max(0.0001, historical_rates.get(model, 1.0)) for model in models}

            def select_fact_model(paper):
                preferred = paper.get("preferred_fact_model")
                candidates = [
                    preferred,
                    DEFAULT_MODEL,
                    manifest.get("phase1_fallback_model"),
                    paper.get("model", manifest["model"]),
                ]
                candidates = [model for model in dict.fromkeys(candidates) if model]
                for model in candidates:
                    if (
                        model == manifest.get("phase1_fallback_model")
                        and gate.phase2_pending() <= 30
                    ):
                        continue
                    if model in preflighted and gate.can_schedule(model):
                        return model
                return None

            def select_model(paper, fact_model, work):
                if fact_model not in preflighted:
                    return None
                eligible = [
                    model
                    for model in preflighted
                    if model in verifier_models
                    and gate.model_enabled(model)
                    and not (
                        model == SECOND_GLM_FLASH_ROUTE
                        and (
                            gate.phase1_pending() > 0
                            or (
                                fact_model == SECOND_GLM_FLASH_ROUTE
                                and not second_key_only
                            )
                        )
                    )
                ]
                eligible = [
                    model
                    for model in eligible
                    if in_flight_tasks[model] < gate.paper_task_limit(model, fact_model)
                ]
                if not eligible:
                    return None
                # Keep the requested Key 1 Flash worker pool supplied before
                # spending remaining verifier capacity on other models.
                flash_floor = manifest.get("minimum_model_limits", {}).get(DEFAULT_MODEL, 0)
                if (
                    DEFAULT_MODEL in eligible
                    and in_flight_tasks[DEFAULT_MODEL] < flash_floor
                    and gate.model_limit(DEFAULT_MODEL) > 0
                ):
                    return DEFAULT_MODEL
                if phase2_preferred_model in eligible:
                    return phase2_preferred_model
                return min(
                    eligible,
                    key=lambda model: (in_flight_work[model] + work) / rates[model],
                )

            def submit_available():
                if queued:
                    for model in sorted(models):
                        ensure_preflight(model)
                while queued and len(futures) < gate.paper_worker_capacity:
                    selected_index = None
                    selected_model = None
                    selected_fact_model = None
                    for index, task in enumerate(queued):
                        paper = task["paper"]
                        pid = paper["paper_id"]
                        assignment = paper_assignments.get(pid)
                        if assignment:
                            model, fact_model = assignment
                            if in_flight_tasks[model] >= gate.paper_task_limit(model, fact_model):
                                continue
                        else:
                            fact_model = select_fact_model(paper)
                            model = (
                                select_model(paper, fact_model, len(task["rows"]))
                                if fact_model
                                else None
                            )
                        if model is not None:
                            selected_index = index
                            selected_model = model
                            selected_fact_model = fact_model
                            break
                    if selected_index is None:
                        return
                    queued.rotate(-selected_index)
                    task = queued.popleft()
                    queued.rotate(selected_index)
                    paper = task["paper"]
                    pid = paper["paper_id"]
                    if pid not in paper_assignments:
                        paper_assignments[pid] = (selected_model, selected_fact_model)
                        paper["model"] = selected_model
                        paper["fact_model"] = selected_fact_model
                    task_paper = {
                        **paper,
                        "model": selected_model,
                        "fact_model": selected_fact_model,
                    }
                    work = max(1, len(task["rows"]))
                    started_at = time.monotonic()
                    in_flight_work[selected_model] += work
                    in_flight_tasks[selected_model] += 1
                    future = pool.submit(
                        analyze_paper_chunk,
                        task_paper,
                        root,
                        manifest,
                        gate,
                        task["chunk_index"],
                    )
                    futures[future] = task
                    started[future] = (selected_model, work, started_at)
                    dispatch_log["assignments"].append(
                        {
                            "paper_id": pid,
                            "chunk": f"{task['chunk_index'] + 1:03d}",
                            "rows": work,
                            "model": selected_model,
                            "fact_model": selected_fact_model,
                            "priority_rank": paper.get("priority_rank", 1),
                        }
                    )
                    dispatch_log["estimated_rows_per_second"] = dict(rates)
                    write_json(dispatch_log_path, dispatch_log)
                    write_json(root / "manifest.json", manifest)

            submit_available()
            last_throughput_refresh = time.monotonic()
            while futures or queued:
                if futures:
                    finished, _ = wait(futures, timeout=5, return_when=FIRST_COMPLETED)
                else:
                    time.sleep(5)
                    finished = set()
                for future in finished:
                    task = futures.pop(future)
                    paper = task["paper"]
                    pid = paper["paper_id"]
                    chunk_index = task["chunk_index"]
                    selected_model, work, started_at = started.pop(future)
                    in_flight_work[selected_model] -= work
                    in_flight_tasks[selected_model] -= 1
                    elapsed = max(0.001, time.monotonic() - started_at)
                    try:
                        chunk_result = future.result()
                        chunk_results[pid][chunk_index] = chunk_result
                        if chunk_result.get("state") == "complete" and not chunk_result.get(
                            "errors"
                        ):
                            observed = work / elapsed
                            rates[selected_model] = 0.5 * rates[selected_model] + 0.5 * observed
                    except Exception as exc:
                        error = f"{type(exc).__name__}: {exc}"
                        chunk_result = {
                            "chunk_index": chunk_index,
                            "state": "failed",
                            "model": selected_model,
                            "fact_model": paper.get("fact_model", selected_model),
                            "errors": [{"chunk": f"{chunk_index + 1:03d}", "error": error}],
                            "proposals": [
                                {
                                    **row,
                                    "action": "call_failed",
                                    "proposed_num_runs": None,
                                    "correction": None,
                                    "error": error,
                                }
                                for row in task["rows"]
                            ],
                        }
                        gate.phase1_finished()
                        gate.phase2_finished()
                        chunk_results[pid][chunk_index] = chunk_result
                        chunk_path = root / "papers" / pid / "chunks" / f"{chunk_index + 1:03d}"
                        write_json(
                            chunk_path / "chunk_complete.json",
                            {
                                "paper_id": pid,
                                "chunk": f"{chunk_index + 1:03d}",
                                "state": "failed",
                                "started_at_utc": datetime.now(UTC).isoformat(),
                                "completed_at_utc": datetime.now(UTC).isoformat(),
                            },
                        )
                    paper_completed = len(chunk_results[pid]) == chunk_counts[pid]
                    if paper_completed:
                        assessment = assemble_paper_result(paper, root, chunk_results[pid])
                        results[pid] = _apply_paper_if_enabled(root, manifest, paper, assessment)
                    _log_mapping_chunk(
                        root,
                        pid,
                        chunk_index,
                        chunk_counts[pid],
                        chunk_result,
                        elapsed,
                        gate,
                        len(queued) + len(futures),
                        len(futures),
                    )
                    if paper_completed:
                        refresh_throughput_report(root, gate=gate)
                manifest["historical_throughput_rows_per_second"] = rates
                dispatch_log["estimated_rows_per_second"] = dict(rates)
                write_json(dispatch_log_path, dispatch_log)
                write_json(root / "manifest.json", manifest)
                submit_available()
                progress(root, manifest, results, gate)
                if time.monotonic() - last_throughput_refresh >= 30:
                    refresh_throughput_report(root, gate=gate)
                    last_throughput_refresh = time.monotonic()
        with readonly(Path(manifest["database"])) as db:
            included_unchanged = database_mode != "apply" and all(
                stored_rows(db, p["paper_id"])
                == read_json(root / "papers" / p["paper_id"] / "rows.json")
                for p in manifest["papers"]
            )
            scope = read_json(root / "scope.json")
            scope_unchanged = all(
                stored_rows(db, paper["paper_id"]) == paper["rows"]
                for paper in scope["excluded_papers"]
            )
            unchanged = included_unchanged and scope_unchanged
        for paper in manifest["papers"]:
            check_inputs(manifest, root, paper)
        status = progress(root, manifest, results, gate, "finished")
        status.update(
            phase="complete",
            pipeline_terminal=True,
            selected_rows_unchanged=unchanged if database_mode != "apply" else None,
            scope_unchanged=scope_unchanged,
            database_application_verified=(
                status["database_application_verified"] if database_mode == "apply" else None
            ),
        )
        write_json(root / "status.json", status)
        write_override_log(root)
        refresh_throughput_report(root, gate=gate)
        return status
