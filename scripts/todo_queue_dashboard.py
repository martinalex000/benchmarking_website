#!/usr/bin/env python3
"""Live multi-worker dashboard for todo queue processing.

Runs multiple queue workers in parallel (without duplicate paper processing) and
shows one persistent row per worker with live status updates.

Example:
    uv run python scripts/todo_queue_dashboard.py --workers 10 --model primary
"""

from __future__ import annotations

import argparse
import select
import re
import subprocess
import sys
import termios
import threading
import time
import tty
from collections import deque
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from sqlalchemy import func
import yaml

from backend.db import session_scope
from backend.models import TodoPaper
from backend.todo_queue import TodoQueueRunResult, process_queue

ANSI_RE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
EXTRACT_DATASET_RE = re.compile(r"extract_dataset:([^\s]+)")
CONFIDENCE_RE = re.compile(r"Confidence:\s*([^\s]+)")
RESULTS_RE = re.compile(r"Results:\s*(\d+)")
PROPOSED_RE = re.compile(r"Proposed:\s*([^\n]+)$")
NEW_RESULTS_RE = re.compile(r"(\d+)\s+new result row")
UPDATED_RESULTS_RE = re.compile(r"(\d+)\s+existing result row\(s\) updated")
DRAINED_ROW_TTL_S = 30.0
STALE_UPDATE_SECONDS = 10.0
EMPTY_CLAIM_RETRIES = 12
EMPTY_CLAIM_RETRY_SLEEP_S = 0.5


@dataclass
class WorkerState:
    worker_id: int
    arxiv_id: str = "-"
    title: str = ""
    status: str = "idle"
    dataset_current: str = ""
    dataset_index: int = 0
    dataset_total: int = 0
    confidence: str = ""
    results_count: int | None = None
    proposed_model: str = ""
    dataset_breakdown: str = ""
    refs_at_start: int = 0
    new_results: int = 0
    updated_results: int = 0
    started_at: float = 0.0
    last_update_at: float | None = None
    completed: int = 0
    failed: int = 0
    drained_at: float | None = None
    last_line: str = ""

    def elapsed_s(self) -> float:
        if self.started_at <= 0:
            return 0.0
        return max(0.0, time.time() - self.started_at)

    def title_short(self, max_len: int = 30) -> str:
        text = (self.title or "").strip()
        if not text:
            return ""
        if len(text) <= max_len:
            return text
        return text[: max_len - 3] + "..."

    def summary_short(self) -> str:
        bits: list[str] = []
        if self.refs_at_start:
            bits.append(f"refs={self.refs_at_start}")
        if self.dataset_breakdown:
            bits.append(f"datasets={self.dataset_breakdown}")
        elif self.dataset_total:
            bits.append(f"datasets={self.dataset_total}")
        if self.results_count is not None:
            bits.append(f"results={self.results_count}")
        if self.proposed_model:
            bits.append(f"proposed={self.proposed_model[:22]}")
        if self.new_results or self.updated_results:
            bits.append(f"new={self.new_results} upd={self.updated_results}")
        return " | ".join(bits)


def _strip_ansi(text: str) -> str:
    return ANSI_RE.sub("", text).strip()


class DashboardState:
    def __init__(self, workers: int, event_lines: int = 16) -> None:
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.worker_states = [WorkerState(worker_id=i + 1) for i in range(workers)]
        self.next_worker_id = workers + 1
        self.desired_workers = workers
        self.drain_requests = 0
        self.scale_up_requests = 0
        self.events: deque[str] = deque(maxlen=event_lines)
        self.finished_lines: list[str] = []
        self.finished_scroll: int = 0
        self.total_done = 0
        self.total_failed = 0
        self.queue_total: int = 0
        self.queue_max_refs: int = 0
        self._render_cache: dict = {
            "snapshot": [],
            "events": [],
            "finished_lines": [],
            "finished_scroll": 0,
            "total_done": 0,
            "total_failed": 0,
            "desired_workers": workers,
            "drain_requests": 0,
            "queue_total": 0,
            "queue_max_refs": 0,
        }

    def add_event(self, message: str) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.events.append(message)
            finally:
                self.lock.release()

    def add_finished_line(self, line: str) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.finished_lines.append(line)
            finally:
                self.lock.release()

    def scroll_finished(self, delta: int) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                max_scroll = max(0, len(self.finished_lines) - 1)
                self.finished_scroll = max(0, min(max_scroll, self.finished_scroll + delta))
            finally:
                self.lock.release()

    def request_scale_up(self) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.scale_up_requests += 1
                self.desired_workers += 1
                self.events.append("scale up requested (+1 worker)")
            finally:
                self.lock.release()

    def request_scale_down(self) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                if self.desired_workers <= 0:
                    self.events.append("scale down ignored (already at 0 workers)")
                    return
                self.desired_workers -= 1
                self.drain_requests += 1
                self.events.append("scale down requested (drain 1 worker)")
            finally:
                self.lock.release()

    def consume_scale_up_requests(self) -> int:
        if self.lock.acquire(timeout=0.05):
            try:
                requested = self.scale_up_requests
                self.scale_up_requests = 0
                return requested
            finally:
                self.lock.release()
        return 0

    def reserve_new_worker_id(self) -> int:
        if self.lock.acquire(timeout=0.05):
            try:
                worker_id = self.next_worker_id
                self.next_worker_id += 1
                self.worker_states.append(WorkerState(worker_id=worker_id))
                return worker_id
            finally:
                self.lock.release()
        return -1

    def consume_drain_slot(self) -> bool:
        if self.lock.acquire(timeout=0.05):
            try:
                if self.drain_requests <= 0:
                    return False
                self.drain_requests -= 1
                return True
            finally:
                self.lock.release()
        return False

    def snapshot_counts(self) -> tuple[int, int]:
        if self.lock.acquire(timeout=0.05):
            try:
                return self.desired_workers, self.drain_requests
            finally:
                self.lock.release()
        cache = self._render_cache
        return int(cache.get("desired_workers", 0)), int(cache.get("drain_requests", 0))

    def snapshot_for_render(self, now: float) -> tuple[dict, bool]:
        """Return a safe render snapshot without ever blocking the UI thread."""
        if self.lock.acquire(timeout=0.05):
            try:
                snapshot = [
                    WorkerState(**vars(s))
                    for s in self.worker_states
                    if not (
                        s.status == "drained"
                        and s.drained_at is not None
                        and (now - s.drained_at) >= DRAINED_ROW_TTL_S
                    )
                ]
                data = {
                    "snapshot": snapshot,
                    "events": list(self.events),
                    "finished_lines": list(self.finished_lines),
                    "finished_scroll": self.finished_scroll,
                    "total_done": self.total_done,
                    "total_failed": self.total_failed,
                    "desired_workers": self.desired_workers,
                    "drain_requests": self.drain_requests,
                    "queue_total": self.queue_total,
                    "queue_max_refs": self.queue_max_refs,
                }
                self._render_cache = data
                return data, False
            finally:
                self.lock.release()
        return self._render_cache, True


def _trim(text: str, max_len: int) -> str:
    text = (text or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def _dataset_breakdown_from_output(arxiv_id: str) -> str:
    """Return datasets sorted by extracted row count (descending)."""
    output_path = (
        Path(__file__).resolve().parents[1] / "papers" / arxiv_id / "extracted" / "llm_output.yaml"
    )
    if not output_path.exists():
        return ""

    try:
        raw = yaml.safe_load(output_path.read_text(encoding="utf-8")) or {}
        rows = raw.get("results", {}).get("results", [])
        if not isinstance(rows, list):
            return ""

        counts: dict[str, int] = {}
        for row in rows:
            if not isinstance(row, dict):
                continue
            ds = str(row.get("dataset") or "").strip()
            if not ds:
                continue
            counts[ds] = counts.get(ds, 0) + 1

        if not counts:
            return ""

        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0].lower()))
        return ", ".join(f"{name}({count})" for name, count in ranked)
    except Exception:
        return ""


def _queue_stats_snapshot() -> tuple[int, int]:
    """Return (total rows in queue, max seen_count)."""
    try:
        with session_scope() as session:
            total_rows = int(session.query(func.count(TodoPaper.id)).scalar() or 0)
            max_refs = int(session.query(func.max(TodoPaper.seen_count)).scalar() or 0)
        return total_rows, max_refs
    except Exception:
        return 0, 0


def _detect_status_from_line(line: str) -> str | None:
    low = line.lower()
    if "1. download" in low:
        return "downloading"
    if "2. preliminaries" in low:
        return "pre-screening"
    if "pre-screen pass" in low:
        return "pre-screen passed"
    if "pre-screen reject" in low:
        return "rejected pre-screen"
    if "3. dataset discovery" in low:
        return "discovering datasets"
    if "4. per-dataset result extraction" in low:
        return "extracting datasets"
    if "5. parse results" in low:
        return "parsing"
    if "6. build hugo pages" in low:
        return "exporting"
    if "done" == low or low.endswith(" done"):
        return "done"
    return None


def _parse_discovered_datasets(line: str) -> list[str]:
    if "datasets:" not in line.lower():
        return []
    payload = line.split(":", 1)[1].strip()
    if not payload or payload == "-":
        return []
    if "," in payload:
        names = [part.strip() for part in payload.split(",") if part.strip()]
        return names
    names = [part.strip() for part in re.split(r"\s{2,}", payload) if part.strip()]
    if len(names) <= 1:
        names = [part.strip() for part in payload.split() if part.strip()]
    return names


def _update_state_from_line(state: WorkerState, line: str) -> None:
    state.last_line = line

    status = _detect_status_from_line(line)
    if status is not None:
        state.status = status

    if "confidence:" in line.lower():
        match = CONFIDENCE_RE.search(line)
        if match:
            state.confidence = match.group(1)

        res_match = RESULTS_RE.search(line)
        if res_match:
            state.results_count = int(res_match.group(1))

        prop_match = PROPOSED_RE.search(line)
        if prop_match:
            state.proposed_model = prop_match.group(1).strip()

    if "new result row" in line.lower():
        match = NEW_RESULTS_RE.search(line)
        if match:
            state.new_results = int(match.group(1))

    if "existing result row(s) updated" in line.lower():
        match = UPDATED_RESULTS_RE.search(line)
        if match:
            state.updated_results = int(match.group(1))

    datasets = _parse_discovered_datasets(line)
    if datasets:
        state.dataset_total = max(state.dataset_total, len(datasets))

    match = EXTRACT_DATASET_RE.search(line)
    if match:
        ds_name = match.group(1)
        if ds_name and ds_name != state.dataset_current:
            state.dataset_index += 1
            state.dataset_current = ds_name
        if state.dataset_total > 0:
            state.status = (
                f"dataset {state.dataset_index}/{state.dataset_total}: "
                f"{state.dataset_current[:22]}"
            )
        else:
            state.status = f"dataset {state.dataset_index}: {state.dataset_current[:22]}"


def _format_elapsed(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def _format_age(seconds: float | None) -> str:
    if seconds is None or seconds < 0:
        return "--:--"
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def _render_dashboard(dash: DashboardState) -> Group:
    now = time.time()
    snap, using_cache = dash.snapshot_for_render(now)
    snapshot = snap["snapshot"]
    events = snap["events"]
    finished_lines = snap["finished_lines"]
    finished_scroll = snap["finished_scroll"]
    total_done = snap["total_done"]
    total_failed = snap["total_failed"]
    desired_workers = snap["desired_workers"]
    drain_requests = snap["drain_requests"]
    queue_total = snap["queue_total"]
    queue_max_refs = snap["queue_max_refs"]

    table = Table(expand=True)
    table.add_column("W", width=3, justify="right", no_wrap=True)
    table.add_column("arXiv", width=12, no_wrap=True)
    table.add_column("Title", width=30, no_wrap=True)
    table.add_column("Status", width=40, no_wrap=True)
    table.add_column("Elapsed", width=8, justify="right", no_wrap=True)
    table.add_column("Upd", width=7, justify="right", no_wrap=True)
    table.add_column("Summary", ratio=1, min_width=20)

    for st in snapshot:
        status_text = st.status
        if st.status == "idle":
            status_text = "idle / waiting"
        elif st.status == "drained":
            status_text = "[grey62]drained[/grey62]"
        summary_text = st.summary_short() or st.last_line[:60]
        age_s = None
        if st.last_update_at is not None:
            age_s = max(0.0, now - st.last_update_at)
        age_text = _format_age(age_s)
        if (
            age_s is not None
            and age_s >= STALE_UPDATE_SECONDS
            and st.status
            not in {
                "idle",
                "drained",
                "done",
                "failed",
                "rejected",
            }
        ):
            age_text = f"[yellow]{age_text}[/yellow]"
        table.add_row(
            str(st.worker_id),
            st.arxiv_id,
            _trim(st.title_short(), 30),
            status_text,
            _format_elapsed(st.elapsed_s()),
            age_text,
            summary_text,
        )

    ui_tick = time.strftime("%H:%M:%S", time.localtime(now))
    stale_note = "  [snapshot cached]" if using_cache else ""
    header = Text(
        "todo_queue dashboard   "
        f"ui_tick={ui_tick}{stale_note}   "
        f"done={total_done}   failed={total_failed}   "
        f"queue_total={queue_total}   queue_max_refs={queue_max_refs}   "
        f"target_workers={desired_workers}   draining={drain_requests}   "
        "ctrl+c stop   arrows/j,k scroll finished   +/- scale workers",
        style="bold",
    )

    finished_window_lines = 12
    finished_end = max(0, len(finished_lines) - finished_scroll)
    finished_start = max(0, finished_end - finished_window_lines)
    visible_finished = finished_lines[finished_start:finished_end]
    if not visible_finished:
        visible_finished = ["(no finished papers yet)"]
    finished_title = f"Finished papers ({len(finished_lines)})" f"  scroll={finished_scroll}"
    finished_panel = Panel(
        "\n".join(visible_finished),
        title=finished_title,
        border_style="green",
    )

    log_lines = events[-16:] if events else ["(no worker log lines yet)"]
    log_panel = Panel("\n".join(log_lines), title="Recent worker output", border_style="cyan")

    workers_title = Text("Workers", style="bold")
    return Group(header, workers_title, table, finished_panel, log_panel)


def _keyboard_listener(dash: DashboardState) -> None:
    """Listen for arrow key input and scroll the finished-paper window.

    Keeps focus on the finished pane only; other panels ignore key input.
    """
    if not sys.stdin.isatty():
        return

    fd = sys.stdin.fileno()
    old_attrs = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        while not dash.stop_event.is_set():
            ready, _, _ = select.select([sys.stdin], [], [], 0.2)
            if not ready:
                continue

            ch = sys.stdin.read(1)
            if ch == "\x1b":
                seq = sys.stdin.read(2)
                if seq == "[A":
                    dash.scroll_finished(+1)
                elif seq == "[B":
                    dash.scroll_finished(-1)
            elif ch in {"k", "K"}:
                dash.scroll_finished(+1)
            elif ch in {"j", "J"}:
                dash.scroll_finished(-1)
            elif ch in {"+", "="}:
                dash.request_scale_up()
            elif ch in {"-", "_"}:
                dash.request_scale_down()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_attrs)


def _run_manual_streaming(
    *,
    arxiv_id: str,
    model: str,
    force: bool,
    inactivity_timeout_s: float | None,
    worker_state: WorkerState,
    dash: DashboardState,
) -> TodoQueueRunResult:
    cmd = [
        sys.executable,
        str(Path(__file__).resolve().parents[1] / "scripts" / "run_manual.py"),
        arxiv_id,
        "--model",
        model,
        "--skip-export",
    ]
    if force:
        cmd.append("--force")

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True,
    )

    output_lines: list[str] = []
    assert proc.stdout is not None
    stdout_fd = proc.stdout.fileno()
    last_activity = time.monotonic()

    while True:
        if proc.poll() is not None:
            break

        ready, _, _ = select.select([stdout_fd], [], [], 0.25)
        if ready:
            raw_line = proc.stdout.readline()
            if not raw_line:
                continue
            line = _strip_ansi(raw_line)
            if not line:
                continue
            last_activity = time.monotonic()
            output_lines.append(line)

            with dash.lock:
                _update_state_from_line(worker_state, line)
                worker_state.last_update_at = time.time()
                dash.events.append(f"w{worker_state.worker_id} {arxiv_id}: {line[:180]}")
            continue

        if inactivity_timeout_s and (time.monotonic() - last_activity) > inactivity_timeout_s:
            with dash.lock:
                dash.events.append(
                    f"w{worker_state.worker_id} {arxiv_id}: timed out after "
                    f"{int(inactivity_timeout_s)}s of inactivity"
                )
                worker_state.status = "timed out"
                worker_state.last_update_at = time.time()

            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=5)

            return TodoQueueRunResult(
                returncode=1,
                stdout="\n".join(output_lines),
                stderr=f"Timed out after {int(inactivity_timeout_s)}s of inactivity",
            )

    # Drain any remaining buffered output after process exit.
    for raw_line in proc.stdout:
        line = _strip_ansi(raw_line)
        if not line:
            continue
        output_lines.append(line)
        with dash.lock:
            _update_state_from_line(worker_state, line)
            worker_state.last_update_at = time.time()
            dash.events.append(f"w{worker_state.worker_id} {arxiv_id}: {line[:180]}")

    stdout = "\n".join(output_lines)
    return TodoQueueRunResult(returncode=proc.returncode or 0, stdout=stdout, stderr="")


def _worker_loop(
    *,
    worker_id: int,
    dash: DashboardState,
    model: str,
    force: bool,
    max_attempts: int,
    max_papers: int,
    inactivity_timeout_s: float | None,
) -> None:
    state = dash.worker_states[worker_id - 1]

    handled = 0
    empty_claims = 0
    while not dash.stop_event.is_set():
        # Draining happens only between jobs so active work finishes gracefully.
        if dash.consume_drain_slot():
            with dash.lock:
                state.status = "drained"
                state.started_at = 0.0
                state.drained_at = time.time()
                state.last_update_at = time.time()
                dash.events.append(f"w{worker_id} drained and exited")
            return

        if max_papers > 0 and handled >= max_papers:
            with dash.lock:
                state.status = "done (limit reached)"
            return

        def _on_start(entry, _index, _total):
            queue_total, queue_max_refs = _queue_stats_snapshot()
            with dash.lock:
                dash.queue_total = queue_total
                dash.queue_max_refs = queue_max_refs
                state.arxiv_id = entry.arxiv_id
                state.title = entry.title or ""
                state.status = "claimed"
                state.started_at = time.time()
                state.last_update_at = state.started_at
                state.dataset_current = ""
                state.dataset_index = 0
                state.dataset_total = 0
                state.confidence = ""
                state.results_count = None
                state.proposed_model = ""
                state.dataset_breakdown = ""
                state.refs_at_start = entry.seen_count or 0
                state.new_results = 0
                state.updated_results = 0
                state.drained_at = None
                state.last_line = ""
                dash.events.append(f"w{worker_id} claimed {entry.arxiv_id}")

        def _runner(arxiv_id: str, *, model: str, force: bool) -> TodoQueueRunResult:
            return _run_manual_streaming(
                arxiv_id=arxiv_id,
                model=model,
                force=force,
                inactivity_timeout_s=inactivity_timeout_s,
                worker_state=state,
                dash=dash,
            )

        def _on_finish(_entry, status, _result, _index, _total):
            dataset_breakdown = _dataset_breakdown_from_output(state.arxiv_id)
            with dash.lock:
                if status == "done":
                    dash.total_done += 1
                    state.completed += 1
                    state.status = "done"
                else:
                    dash.total_failed += 1
                    state.failed += 1
                    state.status = status
                state.dataset_breakdown = dataset_breakdown
                state.last_update_at = time.time()
                dash.events.append(f"w{worker_id} finished {state.arxiv_id} => {status}")
                finished_summary = state.summary_short() or _trim(state.last_line, 80)
                status_prefix = ""
                if status == "rejected":
                    status_prefix = "[yellow]REJECTED[/yellow] "
                elif status == "failed":
                    status_prefix = "[red]FAILED[/red] "
                finished_line = f"{state.arxiv_id:<12}  {(_trim(state.title, 30) or '-'):30}  {status_prefix}{finished_summary}"
                dash.finished_lines.append(finished_line)

        summary = process_queue(
            limit=1,
            model=model,
            force=force,
            max_attempts=max_attempts,
            dry_run=False,
            refresh_dev_exports=False,
            runner=_runner,
            on_start=_on_start,
            on_finish=_on_finish,
        )

        if summary.total_selected == 0:
            empty_claims += 1
            with dash.lock:
                state.status = "waiting for claim"
                state.started_at = 0.0
                state.last_update_at = time.time()

            if empty_claims >= EMPTY_CLAIM_RETRIES:
                with dash.lock:
                    state.status = "idle (queue empty)"
                    state.last_update_at = time.time()
                return

            time.sleep(EMPTY_CLAIM_RETRY_SLEEP_S)
            continue

        empty_claims = 0

        handled += summary.total_selected


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run many todo_queue workers with a live dashboard. "
            "Each worker claims one paper at a time and updates a persistent status row."
        )
    )
    parser.add_argument(
        "--workers", type=int, default=10, metavar="N", help="Parallel workers (default: 10)"
    )
    parser.add_argument(
        "--model",
        default="primary",
        metavar="TIER",
        help="LLM tier for run_manual.py (default: primary)",
    )
    parser.add_argument("--force", action="store_true", help="Pass --force to run_manual.py")
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=3,
        metavar="N",
        help="Skip papers already attempted N times (default: 3)",
    )
    parser.add_argument(
        "--max-papers-per-worker",
        type=int,
        default=0,
        metavar="N",
        help="Stop each worker after N papers (0 = until queue empty)",
    )
    parser.add_argument(
        "--inactivity-timeout-min",
        type=float,
        default=20.0,
        metavar="MIN",
        help="Terminate a worker's run_manual subprocess after MIN minutes without output (0 disables)",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    if args.workers <= 0:
        raise SystemExit("--workers must be >= 1")

    inactivity_timeout_s: float | None = None
    if args.inactivity_timeout_min and args.inactivity_timeout_min > 0:
        inactivity_timeout_s = args.inactivity_timeout_min * 60.0

    dash = DashboardState(workers=args.workers)

    threads: list[threading.Thread] = []

    def _spawn_worker(worker_id: int) -> None:
        t = threading.Thread(
            target=_worker_loop,
            kwargs={
                "worker_id": worker_id,
                "dash": dash,
                "model": args.model,
                "force": args.force,
                "max_attempts": args.max_attempts,
                "max_papers": args.max_papers_per_worker,
                "inactivity_timeout_s": inactivity_timeout_s,
            },
            daemon=True,
            name=f"todo-worker-{worker_id}",
        )
        threads.append(t)
        t.start()

    for idx in range(1, args.workers + 1):
        _spawn_worker(idx)

    key_thread = threading.Thread(
        target=_keyboard_listener,
        kwargs={"dash": dash},
        daemon=True,
        name="todo-dashboard-keys",
    )
    key_thread.start()

    try:
        with Live(_render_dashboard(dash), refresh_per_second=4, screen=True) as live:
            while True:
                for _ in range(dash.consume_scale_up_requests()):
                    new_worker_id = dash.reserve_new_worker_id()
                    if new_worker_id < 0:
                        continue
                    _spawn_worker(new_worker_id)
                    dash.add_event(f"w{new_worker_id} spawned")

                threads[:] = [t for t in threads if t.is_alive()]

                live.update(_render_dashboard(dash))

                desired_workers, _ = dash.snapshot_counts()
                if not threads and desired_workers <= 0:
                    break
                if not threads and desired_workers > 0:
                    break

                time.sleep(0.25)
            live.update(_render_dashboard(dash))
    except KeyboardInterrupt:
        dash.stop_event.set()
        for t in threads:
            t.join(timeout=1.0)
    finally:
        dash.stop_event.set()
        key_thread.join(timeout=0.5)


if __name__ == "__main__":
    main()
