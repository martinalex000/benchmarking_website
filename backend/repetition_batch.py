"""Resumable GLM-only backfill with one daytime stream and adaptive night throughput."""

from __future__ import annotations

import csv
import hashlib
import json
import logging
import os
import shutil
import sqlite3
import time
from collections import Counter, defaultdict, deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from threading import Condition, Lock
from zoneinfo import ZoneInfo

from backend.config import cfg
from backend.db import session_scope
from backend.models import Paper, RepetitionAssessment, Result
from backend.repetition_extractor import (
    DEFAULT_MODEL,
    MAX_REPETITION_TOTAL_TOKENS,
    external_glm_routes,
    extract_repetition_metadata,
    preflight_external_glm,
)
from backend.repetition_storage import apply_assessment
from backend.venue import conference_export_fields

logger = logging.getLogger(__name__)
BERLIN = ZoneInfo("Europe/Berlin")
PRODUCTION_ROOT = cfg.papers_dir / "repetition_backfill"
_DATABASE_APPLY_LOCK = Lock()


def write_json(path: Path, payload) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


class RequestGate:
    """Shared API-key gate; provider 429s reduce concurrency and impose cooldown."""

    _WINDOW_SECONDS = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "month": 30 * 86400,
    }

    def __init__(
        self,
        maximum: int,
        now=None,
        daytime_streams: int | None = None,
        *,
        enforce_rate_limits: bool = False,
        shared_rate_path: Path | None = None,
        last_429_path: Path | None = None,
    ):
        daytime_streams = maximum if daytime_streams is None else daytime_streams
        if maximum < 1 or not 1 <= daytime_streams <= maximum:
            raise ValueError("Require 1 <= daytime streams <= maximum")
        self.maximum = maximum
        self.daytime_maximum = daytime_streams
        self.daytime_limit = daytime_streams
        self.now = now or (lambda: datetime.now(BERLIN))
        self.condition = Condition()
        self.active = 0
        self.rate_limits = 0
        self.successes = 0
        self.cooldown_until = 0.0
        self.enforce_rate_limits = enforce_rate_limits
        self.shared_rate_path = shared_rate_path
        self.last_429_path = last_429_path
        self.request_windows: dict[int, int] = {}
        self.request_starts: deque[float] = deque()

    def observe_rate_limit_headers(self, headers: dict[str, str]) -> None:
        """Learn request quotas from provider response headers, when they include windows."""
        parsed: dict[int, int] = {}
        for name, value in headers.items():
            parts = name.lower().removeprefix("x-ratelimit-").split("-")
            if len(parts) == 2 and parts[0] == "limit":
                unit = parts[1]
            elif len(parts) == 3 and parts[0] == "limit" and parts[1] == "requests":
                unit = parts[2]
            elif len(parts) == 3 and parts[1] == "limit" and parts[2] == "requests":
                unit = ""
            else:
                continue
            seconds = self._WINDOW_SECONDS.get(unit)
            if seconds is None:
                continue
            try:
                limit = int(value)
            except (TypeError, ValueError):
                continue
            if limit > 0:
                parsed[seconds] = min(parsed.get(seconds, limit), limit)
        if parsed:
            with self.condition:
                self.request_windows.update(parsed)
                self.condition.notify_all()

    @property
    def rate_limit_summary(self) -> dict[str, int]:
        return {
            next(name for name, seconds in self._WINDOW_SECONDS.items() if seconds == window): limit
            for window, limit in sorted(self.request_windows.items())
        }

    def recommended_maximum(self, *, timeout_seconds: int, fallback: int = 10) -> int:
        """Choose enough worker slots to fill the tightest advertised request window."""
        if not self.request_windows:
            return fallback
        requests_per_second = min(limit / window for window, limit in self.request_windows.items())
        return max(1, min(100, int(requests_per_second * timeout_seconds)))

    def set_maximum(self, maximum: int) -> None:
        if maximum < 1:
            raise ValueError("maximum must be positive")
        with self.condition:
            self.maximum = maximum
            self.daytime_maximum = maximum
            self.daytime_limit = maximum
            self.condition.notify_all()

    def _rate_window_wait(self, now: float) -> float:
        if not self.enforce_rate_limits:
            return 0.0
        longest_window = max(self.request_windows, default=0)
        while self.request_starts and self.request_starts[0] <= now - longest_window:
            self.request_starts.popleft()
        wait_for = 0.0
        for seconds, limit in self.request_windows.items():
            starts_in_window = sum(started > now - seconds for started in self.request_starts)
            if starts_in_window >= limit:
                oldest = next(started for started in self.request_starts if started > now - seconds)
                wait_for = max(wait_for, oldest + seconds - now)
        return max(0.0, wait_for)

    def _reserve_shared_request(self) -> float:
        """Reserve one request under a file lock shared by workers using this API key."""
        if (
            not self.enforce_rate_limits
            or not self.request_windows
            or self.shared_rate_path is None
        ):
            return 0.0
        import fcntl

        path = self.shared_rate_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.with_suffix(path.suffix + ".lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                state = json.loads(path.read_text()) if path.exists() else {"starts": []}
            except (OSError, json.JSONDecodeError):
                state = {"starts": []}
            now = time.time()
            longest_window = max(self.request_windows)
            starts = [float(value) for value in state.get("starts", [])]
            starts = [value for value in starts if value > now - longest_window]
            wait_for = 0.0
            for seconds, limit in self.request_windows.items():
                in_window = [value for value in starts if value > now - seconds]
                if len(in_window) >= limit:
                    wait_for = max(wait_for, min(in_window) + seconds - now)
            if wait_for <= 0:
                starts.append(now)
            write_json(path, {"updated_at": datetime.now(UTC).isoformat(), "starts": starts})
            return max(0.0, wait_for)

    @property
    def limit(self) -> int:
        return self.daytime_limit

    def __enter__(self):
        with self.condition:
            while True:
                now = time.monotonic()
                rate_wait = self._rate_window_wait(now)
                cooldown_wait = max(0.0, self.cooldown_until - now)
                shared_wait = 0.0
                if self.active < self.limit and rate_wait <= 0 and cooldown_wait <= 0:
                    shared_wait = self._reserve_shared_request()
                    if shared_wait <= 0:
                        break
                waits = [1.0]
                waits.extend(wait for wait in (rate_wait, cooldown_wait, shared_wait) if wait > 0)
                self.condition.wait(timeout=max(0.05, min(waits)))
            self.active += 1
            self.request_starts.append(time.monotonic())
        return self

    def __exit__(self, exc_type, exc, traceback):
        with self.condition:
            self.active -= 1
            if getattr(exc, "status_code", None) == 429:
                self.rate_limits += 1
                self.successes = 0
                if self.last_429_path is not None:
                    import fcntl

                    self.last_429_path.parent.mkdir(parents=True, exist_ok=True)
                    lock_path = self.last_429_path.with_suffix(".lock")
                    try:
                        with lock_path.open("a") as lock:
                            fcntl.flock(lock, fcntl.LOCK_EX)
                            write_json(
                                self.last_429_path,
                                {"occurred_at": datetime.now(UTC).isoformat()},
                            )
                    except OSError:
                        logger.exception("Could not record the most recent 429 timestamp")
                self.daytime_limit = max(1, self.daytime_limit - 1)
                response = getattr(exc, "response", None)
                retry_after = (
                    response.headers.get("retry-after", "60") if response is not None else "60"
                )
                try:
                    delay = max(1, float(retry_after))
                except ValueError:
                    try:
                        delay = max(
                            1,
                            (
                                parsedate_to_datetime(retry_after) - datetime.now(UTC)
                            ).total_seconds(),
                        )
                    except (TypeError, ValueError):
                        delay = 60
                self.cooldown_until = max(self.cooldown_until, time.monotonic() + delay)
            elif exc is None:
                self.successes += 1
                if self.successes >= 2 * self.limit:
                    self.daytime_limit = min(self.daytime_maximum, self.daytime_limit + 2)
                    self.successes = 0
            self.condition.notify_all()


def cohort(
    arxiv_ids: list[str] | None = None,
    *,
    include_nonconference: bool = False,
    include_assessed: bool = False,
    excluded_paper_ids: set[str] | None = None,
) -> list[dict]:
    with session_scope() as session:
        query = session.query(Paper).filter(Paper.results.any())
        if not include_assessed:
            assessed = (
                session.query(RepetitionAssessment.paper_id)
                .filter(RepetitionAssessment.status != "failed")
                .distinct()
            )
            query = query.filter(~Paper.id.in_(assessed))
        if not include_nonconference:
            query = query.filter(Paper.venue.is_not(None), Paper.venue != "")
        if arxiv_ids:
            query = query.filter(Paper.arxiv_id.in_(arxiv_ids))
        return [
            {"paper_id": p.arxiv_id, "title": p.title, "venue": p.venue}
            for p in query.order_by(Paper.arxiv_id)
            if p.arxiv_id
            and p.arxiv_id not in (excluded_paper_ids or set())
            and (
                include_nonconference
                or conference_export_fields(p.venue, p.published_date)["published_conference"]
            )
        ]


def prepare_prompts(root: Path) -> Path:
    folder = root / "prompts"
    folder.mkdir(parents=True, exist_ok=True)
    for name in ("repetition_metadata.txt", "repetition_verification.txt"):
        src = Path(__file__).with_name("prompts") / name
        dst = folder / name
        if not dst.exists():
            shutil.copy2(src, dst)
        elif dst.read_bytes() != src.read_bytes():
            raise ValueError("Prompts changed; use a new batch directory rather than mix revisions")
    return folder


def _reusable_analysis(
    folder: Path,
    source_sha256: str,
    prompt_hashes: dict[str, str],
) -> Path | None:
    path = folder / "analysis.json"
    if not path.exists():
        return None
    try:
        analysis = json.loads(path.read_text())
        provenance = analysis["provenance"]
        if (
            analysis.get("error")
            or provenance["source_sha256"] != source_sha256
            or provenance["prompt_sha256"] != prompt_hashes
            or provenance["model"] not in {DEFAULT_MODEL, "glm-5.3-flash"}
            or not all((folder / f"call_{i}.json").exists() for i in (1, 2))
        ):
            return None
        for index in (1, 2):
            call = json.loads((folder / f"call_{index}.json").read_text())
            if call.get("error") or call.get("success") is False:
                return None
        return path
    except (OSError, KeyError, TypeError, json.JSONDecodeError):
        return None


def analyze_paper(
    paper: dict,
    root: Path,
    prompts: Path,
    gate: RequestGate,
    model_route,
    reuse_root: Path | None = None,
    force=False,
) -> dict:
    pid = paper["paper_id"]
    source_path = cfg.papers_dir / pid / "latex/expanded.tex"
    folder = root / "papers" / pid
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "analysis.json"
    if not source_path.exists():
        return {"paper_id": pid, "status": "failed", "error": "Missing expanded LaTeX source"}
    source = source_path.read_text()
    source_hash = hashlib.sha256(source.encode()).hexdigest()
    prompt_hashes = {
        "facts": hashlib.sha256((prompts / "repetition_metadata.txt").read_bytes()).hexdigest(),
        "verification": hashlib.sha256(
            (prompts / "repetition_verification.txt").read_bytes()
        ).hexdigest(),
    }
    if not force:
        for candidate in (folder, (reuse_root / "papers" / pid) if reuse_root else None):
            if candidate is None:
                continue
            reusable = _reusable_analysis(candidate, source_hash, prompt_hashes)
            if reusable is not None:
                return {"paper_id": pid, "analysis": str(reusable), "cached": True}
    if path.exists():
        archive = folder / "history" / datetime.now(UTC).strftime("%Y%m%dT%H%M%S%f")
        archive.mkdir(parents=True)
        for existing in folder.iterdir():
            if existing.is_file():
                shutil.copy2(existing, archive / existing.name)
    with session_scope() as session:
        p = session.query(Paper).filter_by(arxiv_id=pid).one()
        hints = sorted(
            {
                r.model_name_override or r.model.name
                for r in session.query(Result).filter_by(paper_id=p.id)
            }
        )
    (folder / "source.tex").write_text(source)
    analysis = extract_repetition_metadata(
        source,
        paper_id=pid,
        hints=hints,
        model=model_route.model_id,
        enable_reasoning=True,
        max_tokens=24_000,
        max_total_tokens=MAX_REPETITION_TOTAL_TOKENS,
        request_timeout_seconds=600,
        prompt_directory=prompts,
        request_gate=gate,
        model_route=model_route,
    )
    for i, call in enumerate(analysis.pop("calls"), 1):
        write_json(
            folder / f"call_{i}.json",
            {
                **call,
                "endpoint": model_route.backend.label,
                "model": model_route.model_id,
                "completed_at_utc": datetime.now(UTC).isoformat(),
            },
        )
    write_json(path, analysis)
    return {"paper_id": pid, "analysis": str(path), "cached": False}


def save_progress(root: Path, state: dict, gate: RequestGate | dict[str, RequestGate]) -> None:
    categories = Counter(r.get("status", "ready") for r in state["results"].values())
    state.update(
        updated_at=datetime.now(UTC).isoformat(),
        completed=len(state["results"]),
        categories=dict(categories),
        current_stream_limit=sum(g.limit for g in gate.values())
        if isinstance(gate, dict)
        else gate.limit,
        rate_limits=sum(g.rate_limits for g in gate.values())
        if isinstance(gate, dict)
        else gate.rate_limits,
        active_by_endpoint={name: g.active for name, g in gate.items()}
        if isinstance(gate, dict)
        else {"primary": gate.active},
        limits_by_endpoint={name: g.limit for name, g in gate.items()}
        if isinstance(gate, dict)
        else {"primary": gate.limit},
    )
    write_json(root / "status.json", state)
    assigned = sum(r.get("assigned", 0) for r in state["results"].values())
    text = [
        "# GLM repetition backfill",
        "",
        f"Updated {datetime.now(BERLIN).strftime('%Y-%m-%d %H:%M %Z')}; state: {state['state']}.",
        f"Completed {state['completed']}/{state['total']} papers; {state['active']} active. Categories: {dict(categories)}.",
        f"Assigned verified counts to {assigned} result rows; table-dependent papers are linked but not remapped or deleted.",
        "API endpoints: "
        + ", ".join(
            f"{name}={g.active}/{g.limit} active/limit, {g.rate_limits} 429s"
            for name, g in gate.items()
        )
        if isinstance(gate, dict)
        else f"API streams: {gate.limit}; observed 429 responses: {gate.rate_limits}.",
        *([f"Preflight error: {state['preflight_error']}"] if state.get("preflight_error") else []),
        "",
        "Both extraction and verification use only configured GLM-5.3-Flash endpoints with reasoning enabled. Raw calls and exact source snapshots are under papers/. No statistics or result deletion are performed.",
    ]
    (root / "report.md").write_text("\n".join(text) + "\n")
    if state.get("_throughput_completed") != state["completed"]:
        refresh_throughput_report(root, state)
        state["_throughput_completed"] = state["completed"]
        write_json(root / "status.json", state)


def refresh_throughput_report(root: Path, state: dict) -> None:
    calls = []
    for path in sorted((root / "papers").glob("*/call_*.json")):
        try:
            record = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if record.get("success") and record.get("completed_at_utc"):
            calls.append(record)

    per_route: dict[tuple[str, str], list[dict]] = defaultdict(list)
    per_phase: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    minute_tokens: dict[tuple[int, str, str], int] = defaultdict(int)
    for call in calls:
        try:
            finished = datetime.fromisoformat(call["completed_at_utc"])
            endpoint = call.get("endpoint", "unknown")
            model = call.get("model", "unknown")
            tokens = int(call.get("completion_tokens") or 0)
            minute = int(finished.timestamp() // 60)
        except (KeyError, TypeError, ValueError):
            continue
        per_route[(endpoint, model)].append(call)
        per_phase[(endpoint, model, call.get("call_type", "unknown"))].append(call)
        minute_tokens[(minute, endpoint, model)] += tokens

    csv_path = root / "throughput.csv"
    with csv_path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(
            ("minute_utc", "endpoint", "model", "output_tokens", "output_tokens_per_second")
        )
        for (minute, endpoint, model), tokens in sorted(minute_tokens.items()):
            writer.writerow(
                (
                    datetime.fromtimestamp(minute * 60, UTC).isoformat(),
                    endpoint,
                    model,
                    tokens,
                    tokens / 60,
                )
            )

    lines = [
        "# Repetition scheduler throughput",
        "",
        f"Updated {datetime.now(UTC).isoformat()}; papers {state.get('completed', 0)}/{state.get('total', 0)} complete; "
        f"{state.get('active', 0)} whole-paper tasks active.",
        "",
        "## Output throughput by endpoint and model",
        "",
        "| Endpoint | Model | Calls | Output tokens | Mean call tokens/s | Mean duration | Last-10 mean duration |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for (endpoint, model), route_calls in sorted(per_route.items()):
        durations = [float(call.get("duration_s") or 0) for call in route_calls]
        total_tokens = sum(int(call.get("completion_tokens") or 0) for call in route_calls)
        elapsed = sum(durations)
        lines.append(
            f"| {endpoint} | {model} | {len(route_calls)} | {total_tokens} | "
            f"{total_tokens / elapsed if elapsed else 0:.2f} | "
            f"{sum(durations) / len(durations):.2f}s | "
            f"{sum(durations[-10:]) / len(durations[-10:]):.2f}s |"
        )
    if not per_route:
        lines.append("| — | — | 0 | 0 | — | — | — |")
    lines.extend(
        (
            "",
            "## Call durations by phase",
            "",
            "| Endpoint | Model | Phase | Calls | Mean duration | Last-10 mean duration |",
            "|---|---|---|---:|---:|---:|",
        )
    )
    for (endpoint, model, phase), phase_calls in sorted(per_phase.items()):
        durations = [float(call.get("duration_s") or 0) for call in phase_calls]
        lines.append(
            f"| {endpoint} | {model} | {phase} | {len(durations)} | "
            f"{sum(durations) / len(durations):.2f}s | "
            f"{sum(durations[-10:]) / len(durations[-10:]):.2f}s |"
        )
    if not per_phase:
        lines.append("| — | — | — | 0 | — | — |")
    lines.extend(
        ("", "Per-minute output tokens/s are in `throughput.csv` and plotted in `throughput.png`.")
    )
    (root / "throughput.md").write_text("\n".join(lines) + "\n")

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return
    figure, axis = plt.subplots(figsize=(12, 6))
    if minute_tokens:
        for endpoint, model in sorted(per_route):
            points = sorted(
                (minute, tokens / 60)
                for (minute, point_endpoint, point_model), tokens in minute_tokens.items()
                if point_endpoint == endpoint and point_model == model
            )
            axis.plot(
                [datetime.fromtimestamp(minute * 60, UTC) for minute, _ in points],
                [rate for _, rate in points],
                label=f"{endpoint}/{model}",
            )
        axis.legend(title="Endpoint/model")
    else:
        axis.text(0.5, 0.5, "No completed model calls yet", ha="center", va="center")
    axis.set_title("Output-token throughput by endpoint and model")
    axis.set_xlabel("Call completion minute (UTC)")
    axis.set_ylabel("Output tokens/s")
    axis.grid(True, alpha=0.25)
    figure.autofmt_xdate()
    figure.tight_layout()
    figure.savefig(root / "throughput.png", dpi=150)
    plt.close(figure)


def save_preflight(root: Path, result: dict) -> None:
    path = root / "preflight.json"
    history = json.loads(path.read_text()) if path.exists() else {"attempts": []}
    history["attempts"].append(result)
    write_json(path, history)


def run_batch(
    root: Path = PRODUCTION_ROOT,
    arxiv_ids=None,
    force=False,
    night_max=None,
    day_streams=None,
    reuse_root: Path | None = None,
    endpoint: str | None = None,
    include_nonconference: bool = False,
    exclude_root: Path | None = None,
) -> dict:
    """Snapshot the cohort; resume completed work and serialize database application."""
    root.mkdir(parents=True, exist_ok=True)
    # Only one writer/backfill supervisor for this batch directory.
    import fcntl

    lock = (root / "batch.lock").open("a")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock.close()
        raise RuntimeError("A repetition backfill is already running in this directory") from None
    try:
        return _run_locked(
            root,
            arxiv_ids,
            force,
            night_max,
            day_streams,
            reuse_root,
            endpoint,
            include_nonconference,
            exclude_root,
        )
    finally:
        lock.close()


def _run_locked(
    root: Path,
    arxiv_ids,
    force: bool,
    night_max: int | None,
    day_streams: int | None,
    reuse_root: Path | None = None,
    endpoint: str | None = None,
    include_nonconference: bool = False,
    exclude_root: Path | None = None,
) -> dict:
    prompts = prepare_prompts(root)
    excluded_paper_ids = (
        {path.parent.name for path in exclude_root.glob("*/assessment.json")}
        if exclude_root and exclude_root.is_dir()
        else set()
    )
    papers = cohort(
        arxiv_ids,
        include_nonconference=include_nonconference,
        # Existing DB assessments may come from other runs; the exclusion root is
        # the explicit record of papers completed by the source experiment.
        include_assessed=True,
        excluded_paper_ids=excluded_paper_ids,
    )
    if not papers:
        raise ValueError("No eligible papers found after applying the cohort filters")
    routes = external_glm_routes()
    if endpoint is not None:
        if endpoint not in routes:
            raise ValueError(f"Endpoint {endpoint!r} is not configured")
        routes = {endpoint: routes[endpoint]}
    night_max = max(1, len(papers)) if night_max is None else night_max
    day_streams = night_max if day_streams is None else day_streams
    if night_max < 1 or not 1 <= day_streams <= night_max:
        raise ValueError("Require 1 <= daytime streams <= the eligible paper count")
    row_snapshot = _result_snapshot({paper["paper_id"] for paper in papers})
    write_json(root / "database_rows_snapshot.json", row_snapshot)
    write_json(
        root / "manifest.json",
        {
            "model": DEFAULT_MODEL,
            "model_routes": {name: route.model_id for name, route in routes.items()},
            "papers": papers,
            "timezone": "Europe/Berlin",
            "day_streams": day_streams,
            "night_max": night_max,
            "endpoint_filter": endpoint,
            "include_nonconference": include_nonconference,
        },
    )
    state = {
        "state": "running",
        "pid": os.getpid(),
        "total": len(papers),
        "active": 0,
        "results": {},
        "started_at": datetime.now(UTC).isoformat(),
    }
    gates = {name: RequestGate(night_max, daytime_streams=day_streams) for name in routes}
    if papers:
        preflights = []
        for name, route in routes.items():
            try:
                preflight = preflight_external_glm(
                    gates[name],
                    max_total_tokens=MAX_REPETITION_TOTAL_TOKENS,
                    timeout=600,
                    model_route=route,
                )
            except Exception as exc:
                preflight = {
                    "status": "failed",
                    "checked_at": datetime.now(UTC).isoformat(),
                    "model": route.model_id,
                    "endpoint": route.backend.label,
                    "error": f"{type(exc).__name__}: {exc}",
                    "paper_calls_started": False,
                }
                save_preflight(root, preflight)
                state.update(
                    state="preflight_failed",
                    preflight_error=preflight["error"],
                    preflight_status="failed",
                    failed_endpoint=name,
                    pipeline_terminal=True,
                    selected_rows_unchanged=True,
                )
                save_progress(root, state, gates)
                return state
            preflights.append({**preflight, "paper_calls_started": False})
            save_preflight(root, preflights[-1])
        state["preflight_status"] = "passed"
        state["preflight_finished_at"] = preflights[-1]["checked_at"]
    else:
        state["preflight_status"] = "skipped_empty_cohort"
    prompt_hashes = (
        {
            "facts": hashlib.sha256((prompts / "repetition_metadata.txt").read_bytes()).hexdigest(),
            "verification": hashlib.sha256(
                (prompts / "repetition_verification.txt").read_bytes()
            ).hexdigest(),
        }
        if papers
        else {}
    )
    fresh_papers = []
    if papers:
        for paper in papers:
            source_path = cfg.papers_dir / paper["paper_id"] / "latex/expanded.tex"
            if not source_path.exists():
                fresh_papers.append(paper)
                continue
            source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
            cached = _reusable_analysis(
                root / "papers" / paper["paper_id"], source_hash, prompt_hashes
            ) or (
                _reusable_analysis(
                    reuse_root / "papers" / paper["paper_id"], source_hash, prompt_hashes
                )
                if reuse_root
                else None
            )
            if cached is None:
                fresh_papers.append(paper)
    route_names = list(routes)
    route_assignment = {
        paper["paper_id"]: route_names[index % len(route_names)]
        for index, paper in enumerate(fresh_papers)
    }
    state["model_assignments"] = {
        name: sum(1 for route_name in route_assignment.values() if route_name == name)
        for name in route_names
    }
    write_json(root / "route_assignments.json", route_assignment)
    backup_path = (
        cfg.data_dir
        / "backups"
        / (f"benchmarks_before_repetition_{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}.sqlite")
    )
    database_backup = None
    applied_papers = set()
    queue = deque(papers)
    futures = {}
    max_workers = max(1, night_max * max(1, len(gates)))
    save_progress(root, state, gates)
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        while queue or futures:
            stream_limit = max(1, sum(g.limit for g in gates.values()))
            while queue and len(futures) < stream_limit:
                paper = queue.popleft()
                route_name = route_assignment.get(paper["paper_id"], route_names[0])
                futures[
                    pool.submit(
                        analyze_paper,
                        paper,
                        root,
                        prompts,
                        gates[route_name],
                        routes[route_name],
                        reuse_root,
                        force,
                    )
                ] = paper
            state["active"] = len(futures)
            save_progress(root, state, gates)
            completed, _ = wait(futures, timeout=5, return_when=FIRST_COMPLETED)
            for future in completed:
                paper = futures.pop(future)
                pid = paper["paper_id"]
                try:
                    result = future.result()
                    if "analysis" in result:
                        analysis = json.loads(Path(result["analysis"]).read_text())
                        if analysis.get("error"):
                            result.update(status="failed", error=analysis["error"])
                        else:
                            result["status"] = "ready"
                            source_path = cfg.papers_dir / pid / "latex/expanded.tex"
                            with _DATABASE_APPLY_LOCK:
                                if database_backup is None:
                                    backup_database(backup_path)
                                    database_backup = str(backup_path)
                                    state["database_backup"] = database_backup
                                with session_scope() as db_session:
                                    current = _result_snapshot({pid}, session=db_session)
                                    if current != row_snapshot["papers"].get(pid):
                                        raise RuntimeError(
                                            "Stored result rows changed while this paper was being processed"
                                        )
                                    applied = apply_assessment(
                                        pid,
                                        analysis,
                                        source_path.read_text(),
                                        Path(result["analysis"]),
                                        session=db_session,
                                    )
                            result.update(applied)
                            result["database_application"] = "applied"
                            applied_papers.add(pid)
                    state["results"][pid] = result
                except Exception as exc:
                    logger.exception("Repetition backfill failed for %s", pid)
                    state["results"][pid] = {"status": "failed", "error": str(exc)}
                logger.info("Repetitions %s: %s", pid, state["results"][pid].get("status", "ready"))
                state["active"] = len(futures)
                save_progress(root, state, gates)
    failures = [
        pid
        for pid, result in state["results"].items()
        if result.get("status") == "failed" or "analysis" not in result
    ]
    state.update(state="finished_with_failures" if failures else "finished", active=0)
    if failures:
        state["database_applied"] = bool(applied_papers)
        state["database_application_complete"] = False
        state["failed_papers"] = failures
        save_progress(root, state, gates)
        return state
    state.update(
        database_applied=bool(applied_papers),
        database_application_complete=True,
        selected_rows_unchanged=True,
    )
    save_progress(root, state, gates)
    return state


def _result_snapshot(paper_ids: set[str], *, include_papers: bool = False, session=None) -> dict:
    """Hash repetition-relevant result fields to prevent applying stale assessments."""
    if session is None:
        with session_scope() as active_session:
            return _result_snapshot(
                paper_ids, include_papers=include_papers, session=active_session
            )
    papers = session.query(Paper).filter(Paper.arxiv_id.in_(paper_ids)).all()
    paper_by_id = {paper.id: paper.arxiv_id for paper in papers}
    rows = session.query(Result).filter(Result.paper_id.in_(paper_by_id)).order_by(Result.id).all()
    values = [
        [
            row.id,
            paper_by_id[row.paper_id],
            row.model_id,
            row.dataset_variant_id,
            row.metric_name,
            row.metric_value,
            row.metric_std,
            row.source_paper_id,
            row.source_ref,
            row.table_ref,
            row.model_name_override,
            row.num_runs,
            row.trained_by_paper,
            row.num_runs_evidence,
            row.repetition_assessment_id,
            row.repetition_status,
            row.is_overridden,
        ]
        for row in rows
    ]

    def digest(items: list[list]) -> dict:
        encoded = json.dumps(items, ensure_ascii=False, separators=(",", ":")).encode()
        return {"rows": len(items), "sha256": hashlib.sha256(encoded).hexdigest()}

    if include_papers:
        by_paper = {paper_id: [] for paper_id in paper_by_id.values()}
        for value in values:
            by_paper[value[1]].append(value)
        return {
            "all": digest(values),
            "papers": {paper_id: digest(items) for paper_id, items in by_paper.items()},
        }
    return digest(values)


def backup_database(destination: Path) -> None:
    """Consistent SQLite backup includes any existing WAL; do not overwrite backups."""
    if destination.exists():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with (
        sqlite3.connect(f"file:{cfg.db_path}?mode=ro", uri=True) as src,
        sqlite3.connect(destination) as dst,
    ):
        src.backup(dst)
