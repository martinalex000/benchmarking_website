#!/usr/bin/env python3
"""Live multi-worker dashboard for todo queue processing.

Runs multiple queue workers in parallel (without duplicate paper processing) and
shows one persistent row per worker with live status updates.

Example:
    uv run python scripts/todo_queue_dashboard.py --workers 10 --model primary
"""

from __future__ import annotations

import argparse
import faulthandler
import logging
import os
import random
import re
import select
import shutil
import subprocess
import sys
import termios
import threading
import time
import tty
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml
from rich.align import Align
from rich.console import Group
from rich.layout import Layout
from rich.live import Live
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from sqlalchemy import func

from backend.db import session_scope
from backend.models import TodoPaper, TodoPaperStatus
from backend.process_env import project_subprocess_env
from backend.todo_queue import TodoQueueRunResult, process_queue

ANSI_RE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
EXTRACT_DATASET_RE = re.compile(r"extract_dataset:([^\s]+)")
EXTRACT_DATASET_VARIANT_RE = re.compile(
    r"^(?P<name>.+?):(?:(?:g|table)\d+|tables_only|tables_first)$",
    re.IGNORECASE,
)
CONFIDENCE_RE = re.compile(r"Confidence:\s*([^\s]+)")
RESULTS_RE = re.compile(r"Results:\s*(\d+)")
PROPOSED_RE = re.compile(r"Proposed:\s*([^\n]+)$")
NEW_RESULTS_RE = re.compile(r"(\d+)\s+new result row")
UPDATED_RESULTS_RE = re.compile(r"(\d+)\s+existing result row\(s\) updated")
MOUSE_SGR_RE = re.compile(r"\[<(\d+);(\d+);(\d+)([Mm])")
ARROW_SEQ_RE = re.compile(r"\x1b(?:O|\[[\d;]*)([ABCD])$")
DONE_RULE_RE = re.compile(r"(?:^|─+|\s)done(?:\s|─+|$)", re.IGNORECASE)
PEEK_OUTPUT_MAX_LINES = 60
WORKER_OUTPUT_MAX_LINES = 800
INPUT_ESCAPE_DEADLINE_S = 0.12
# Screen row (1-based) of first worker row: header + keys + Workers + table header.
WORKER_TABLE_FIRST_ROW = 5
FINISHED_WINDOW_LINES = 12
LOG_WINDOW_LINES = 16
OVERLAY_HEIGHT_RATIO = 2 / 3
OVERLAY_WIDTH_RATIO = 2 / 3
DRAINED_ROW_TTL_S = 30.0
STALE_UPDATE_SECONDS = 10.0
EMPTY_CLAIM_RETRIES = 12
EMPTY_CLAIM_RETRY_SLEEP_S = 0.5

LOGGER = logging.getLogger("todo_queue_dashboard")


@dataclass
class WorkerState:
    worker_id: int
    arxiv_id: str = "-"
    title: str = ""
    status: str = "idle"
    dataset_current: str = ""
    dataset_names: list[str] = field(default_factory=list)
    dataset_index: int = 0
    dataset_total: int = 0
    confidence: str = ""
    results_count: int | None = None
    proposed_model: str = ""
    dataset_breakdown: str = ""
    refs_at_start: int = 0
    manually_important: bool = False
    new_results: int = 0
    updated_results: int = 0
    started_at: float = 0.0
    last_update_at: float | None = None
    completed: int = 0
    failed: int = 0
    drained_at: float | None = None
    last_line: str = ""
    output_log: list[str] = field(default_factory=list)

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
        if self.manually_important:
            bits.append("imp!")
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
        self.queue_failed_total: int = 0
        self.lock_contention_drops: int = 0
        self.ui_last_render_at: float = time.monotonic()
        self.ui_loop_iterations: int = 0
        self.render_cache_uses: int = 0
        self.peek_worker_id: int | None = None
        self.selected_worker_index: int = 0
        self.peek_tail_offset: int = 0
        self.peek_follow_tail: bool = True
        self.ui_focus: str = "workers"
        self.worker_row_map: dict[int, int] = {}
        self.worker_table_first_row: int = WORKER_TABLE_FIRST_ROW
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
            "queue_failed_total": 0,
            "lock_contention_drops": 0,
            "peek_worker_id": None,
            "selected_worker_index": 0,
        }

    def set_peek_worker(self, worker_id: int) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.peek_worker_id = worker_id
                self.peek_tail_offset = 0
                self.peek_follow_tail = True
            finally:
                self.lock.release()

    def clear_peek_worker(self) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.peek_worker_id = None
                self.peek_tail_offset = 0
                self.peek_follow_tail = True
            finally:
                self.lock.release()

    def scroll_peek_older(self, lines: int = 3) -> None:
        """Scroll peek output toward older lines (away from tail)."""
        if self.lock.acquire(timeout=0.05):
            try:
                self.peek_tail_offset += lines
                self.peek_follow_tail = False
            finally:
                self.lock.release()

    def scroll_peek_toward_tail(self, lines: int = 3) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.peek_tail_offset = max(0, self.peek_tail_offset - lines)
                if self.peek_tail_offset == 0:
                    self.peek_follow_tail = True
            finally:
                self.lock.release()

    def reset_peek_to_tail(self) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.peek_tail_offset = 0
                self.peek_follow_tail = True
            finally:
                self.lock.release()

    def peek_worker_id_snapshot(self) -> int | None:
        if self.lock.acquire(timeout=0.05):
            try:
                return self.peek_worker_id
            finally:
                self.lock.release()
        cache = self._render_cache
        peek = cache.get("peek_worker_id")
        return int(peek) if peek is not None else None

    def move_worker_selection(self, delta: int, worker_count: int) -> None:
        if worker_count <= 0:
            return
        if self.lock.acquire(timeout=0.05):
            try:
                idx = self.selected_worker_index + delta
                if idx < 0:
                    idx = worker_count - 1
                elif idx >= worker_count:
                    idx = 0
                self.selected_worker_index = idx
                self.ui_focus = "workers"
            finally:
                self.lock.release()

    def select_worker_index(self, index: int, worker_count: int) -> None:
        if worker_count <= 0:
            return
        if self.lock.acquire(timeout=0.05):
            try:
                self.selected_worker_index = max(0, min(worker_count - 1, index))
                self.ui_focus = "workers"
            finally:
                self.lock.release()

    def select_first_worker(self, worker_count: int) -> None:
        self.select_worker_index(0, worker_count)

    def select_last_worker(self, worker_count: int) -> None:
        if worker_count <= 0:
            return
        self.select_worker_index(worker_count - 1, worker_count)

    def set_ui_focus(self, focus: str) -> None:
        if focus not in {"workers", "finished"}:
            return
        if self.lock.acquire(timeout=0.05):
            try:
                self.ui_focus = focus
            finally:
                self.lock.release()

    def ui_focus_snapshot(self) -> str:
        if self.lock.acquire(timeout=0.05):
            try:
                return self.ui_focus
            finally:
                self.lock.release()
        return str(self._render_cache.get("ui_focus", "workers"))

    def open_peek_for_selected_worker(self, snapshot: list[WorkerState]) -> None:
        if not snapshot:
            return
        if self.lock.acquire(timeout=0.05):
            try:
                idx = min(self.selected_worker_index, len(snapshot) - 1)
                self.selected_worker_index = idx
                self.peek_worker_id = snapshot[idx].worker_id
                self.peek_tail_offset = 0
                self.peek_follow_tail = True
            finally:
                self.lock.release()

    def add_event(self, message: str) -> None:
        if self.lock.acquire(timeout=0.05):
            try:
                self.events.append(message)
            finally:
                self.lock.release()

    def mutate(self, fn, timeout: float = 0.05) -> bool:
        """Best-effort shared-state update that never blocks callers indefinitely."""
        if self.lock.acquire(timeout=timeout):
            try:
                fn()
                return True
            finally:
                self.lock.release()
        # Keep this lock-free so a wedged lock never blocks the caller path.
        self.lock_contention_drops += 1
        return False

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

    def _visible_worker_states(self, now: float) -> list[WorkerState]:
        return [
            s
            for s in self.worker_states
            if not (
                s.status == "drained"
                and s.drained_at is not None
                and (now - s.drained_at) >= DRAINED_ROW_TTL_S
            )
        ]

    def snapshot_for_render(self, now: float) -> tuple[dict, bool]:
        """Return a safe render snapshot without ever blocking the UI thread."""
        if self.lock.acquire(timeout=0.05):
            try:
                visible = self._visible_worker_states(now)
                if visible:
                    self.selected_worker_index = min(self.selected_worker_index, len(visible) - 1)
                else:
                    self.selected_worker_index = 0
                snapshot = [WorkerState(**vars(s)) for s in visible]
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
                    "queue_failed_total": self.queue_failed_total,
                    "lock_contention_drops": self.lock_contention_drops,
                    "peek_worker_id": self.peek_worker_id,
                    "selected_worker_index": self.selected_worker_index,
                    "peek_tail_offset": self.peek_tail_offset,
                    "peek_follow_tail": self.peek_follow_tail,
                    "ui_focus": self.ui_focus,
                }
                self._render_cache = data
                return data, False
            finally:
                self.lock.release()
        return self._render_cache, True


def _configure_logger(log_path: str) -> logging.Logger:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("todo_queue_dashboard")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s [%(threadName)s] %(message)s")
    )
    logger.addHandler(handler)
    return logger


def _dump_all_thread_stacks(log_path: str, reason: str) -> None:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fp:
        fp.write("\n")
        fp.write(f"===== THREAD DUMP ({reason}) =====\n")
        faulthandler.dump_traceback(file=fp, all_threads=True)
        fp.write("===== END THREAD DUMP =====\n")
        fp.write("\n")


def _trim(text: str, max_len: int) -> str:
    text = (text or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def _dataset_breakdown_from_output(arxiv_id: str) -> str:
    """Return datasets sorted by extracted row count (descending)."""
    try:
        from backend.paper_storage import PaperStorage

        output_path = PaperStorage(arxiv_id).llm_output_yaml_path
    except ValueError:
        return ""
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


def _queue_stats_snapshot() -> tuple[int, int, int]:
    """Return (open rows, max seen_count among open rows, total failed rows)."""
    try:
        with session_scope() as session:
            open_statuses = [
                TodoPaperStatus.PENDING.value,
                TodoPaperStatus.PROCESSING.value,
            ]
            failed_statuses = [
                TodoPaperStatus.FAILED.value,
                TodoPaperStatus.REJECTED.value,
            ]
            open_query = session.query(TodoPaper).filter(TodoPaper.status.in_(open_statuses))
            open_rows = int(open_query.count())
            max_refs = int(
                session.query(func.max(TodoPaper.seen_count))
                .filter(TodoPaper.status.in_(open_statuses))
                .scalar()
                or 0
            )
            failed_total = int(
                session.query(func.count(TodoPaper.id))
                .filter(TodoPaper.status.in_(failed_statuses))
                .scalar()
                or 0
            )
        return open_rows, max_refs, failed_total
    except Exception:
        return 0, 0, 0


def _pending_ready_count() -> int:
    """Return number of currently claimable pending rows."""
    try:
        with session_scope() as session:
            return int(
                session.query(func.count(TodoPaper.id))
                .filter(
                    TodoPaper.status == "pending",
                )
                .scalar()
                or 0
            )
    except Exception:
        return 0


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
    if "exporting datasets" in low:
        return "exporting datasets"
    if "exporting papers" in low:
        return "exporting papers"
    if "6. build hugo pages" in low:
        if "skipped" in low:
            if "skip-export" in low:
                return "export skipped (--skip-export)"
            return "export skipped (no changes)"
        return "exporting hugo"
    if DONE_RULE_RE.search(line) or low == "done" or low.endswith(" done"):
        return "done"
    return None


def _worker_id_at_screen_row(row_map: dict[int, int], screen_row: int) -> int | None:
    """Map a terminal row (1-based) to a worker id using the latest render map."""
    if screen_row in row_map:
        return row_map[screen_row]
    for offset in (-1, 1, -2, 2):
        candidate = row_map.get(screen_row + offset)
        if candidate is not None:
            return candidate
    return None


def _terminal_size() -> tuple[int, int]:
    try:
        size = shutil.get_terminal_size(fallback=(80, 24))
        return max(40, size.columns), max(15, size.lines)
    except OSError:
        return 80, 24


def _overlay_dimensions() -> tuple[int, int, int]:
    """Return (overlay_width, overlay_height, main_visible_height)."""
    term_w, term_h = _terminal_size()
    overlay_h = max(8, int(term_h * OVERLAY_HEIGHT_RATIO))
    overlay_w = max(40, int(term_w * OVERLAY_WIDTH_RATIO))
    main_h = max(6, term_h - overlay_h)
    return overlay_w, overlay_h, main_h


def _build_worker_row_map(snapshot: list[WorkerState]) -> dict[int, int]:
    return _build_worker_row_map_at(snapshot, WORKER_TABLE_FIRST_ROW)


def _build_worker_row_map_at(snapshot: list[WorkerState], first_row: int) -> dict[int, int]:
    row_map: dict[int, int] = {}
    for i, st in enumerate(snapshot):
        row_map[first_row + i] = st.worker_id
    return row_map


def _append_worker_output(state: WorkerState, line: str) -> None:
    state.output_log.append(line)
    overflow = len(state.output_log) - WORKER_OUTPUT_MAX_LINES
    if overflow > 0:
        del state.output_log[:overflow]


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


def _unique_dataset_names(names: list[str]) -> list[str]:
    unique: list[str] = []
    seen: set[str] = set()
    for name in names:
        normalized = name.strip()
        key = normalized.casefold()
        if normalized and key not in seen:
            seen.add(key)
            unique.append(normalized)
    return unique


def _normalize_extracted_dataset(raw_name: str) -> str:
    """Strip retry, group, and per-table suffixes from an extraction call name."""
    name = raw_name.strip()
    while True:
        match = EXTRACT_DATASET_VARIANT_RE.match(name)
        if match is None:
            return name
        name = match.group("name")


def _dataset_position(state: WorkerState, dataset_name: str) -> int:
    key = dataset_name.casefold()
    for index, known_name in enumerate(state.dataset_names, start=1):
        if known_name.casefold() == key:
            return index

    state.dataset_names.append(dataset_name)
    return len(state.dataset_names)


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
        state.dataset_names = _unique_dataset_names(state.dataset_names + datasets)
        state.dataset_total = len(state.dataset_names)

    match = EXTRACT_DATASET_RE.search(line)
    if match:
        ds_name = _normalize_extracted_dataset(match.group(1))
        if ds_name:
            state.dataset_index = _dataset_position(state, ds_name)
            state.dataset_current = ds_name
            state.dataset_total = max(state.dataset_total, len(state.dataset_names))
        if state.dataset_total > 0:
            state.status = (
                f"dataset {state.dataset_index}/{state.dataset_total}: {state.dataset_current[:22]}"
            )
        else:
            state.status = f"dataset {state.dataset_index}: {state.dataset_current[:22]}"


def _format_elapsed(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def _format_header_line(snap: dict) -> Text:
    """Single stable status line (fixed layout; no per-frame counters that change width)."""
    total_done = int(snap.get("total_done", 0))
    total_failed = int(snap.get("total_failed", 0))
    queue_total = int(snap.get("queue_total", 0))
    queue_max_refs = int(snap.get("queue_max_refs", 0))
    queue_failed_total = int(snap.get("queue_failed_total", 0))
    desired_workers = int(snap.get("desired_workers", 0))
    drain = int(snap.get("drain_requests", 0))
    line = (
        f"todo_queue  ok={total_done:4d} fail={total_failed:3d}/{queue_failed_total:4d} "
        f"q={queue_total:4d} refs={queue_max_refs:3d} "
        f"w={desired_workers:2d} drain={drain:2d}"
    )
    return Text(line, style="bold")


def _format_keys_hint_line() -> Text:
    """Static shortcuts line; never changes length."""
    return Text(
        "keys: w/f focus  arrows/n/p  1-9 enter peek  j/k scroll  +/- workers",
        style="dim",
    )


def _dashboard_render_fingerprint(snap: dict, now: float) -> str:
    """Fingerprint for throttling redraws; clocks bucketed to 1 Hz."""
    clock_sec = int(now)
    worker_bits: list[tuple] = []
    for s in snap.get("snapshot", []):
        started = float(getattr(s, "started_at", 0) or 0)
        elapsed_bucket = clock_sec - int(started) if started > 0 else 0
        last_upd = getattr(s, "last_update_at", None)
        age_bucket = clock_sec - int(last_upd) if last_upd else -1
        worker_bits.append(
            (
                getattr(s, "worker_id", 0),
                getattr(s, "status", ""),
                getattr(s, "arxiv_id", ""),
                elapsed_bucket,
                age_bucket,
            )
        )
    events = snap.get("events", [])
    last_event = events[-1] if events else ""
    return repr(
        (
            clock_sec,
            snap.get("total_done"),
            snap.get("total_failed"),
            snap.get("queue_total"),
            snap.get("queue_max_refs"),
            snap.get("queue_failed_total"),
            snap.get("desired_workers"),
            snap.get("drain_requests"),
            snap.get("selected_worker_index"),
            snap.get("ui_focus"),
            snap.get("peek_worker_id"),
            snap.get("peek_tail_offset"),
            snap.get("peek_follow_tail"),
            snap.get("finished_scroll"),
            len(snap.get("finished_lines", [])),
            last_event,
            tuple(worker_bits),
        )
    )


def _format_age(seconds: float | None) -> str:
    if seconds is None or seconds < 0:
        return "--:--"
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def _render_peek_overlay_panel(
    snapshot: list[WorkerState],
    worker_id: int,
    overlay_w: int,
    overlay_h: int,
    *,
    tail_offset: int = 0,
    follow_tail: bool = True,
) -> Panel:
    worker = next((s for s in snapshot if s.worker_id == worker_id), None)
    viewport_lines = max(3, overlay_h - 3)
    if worker is None:
        body = "(worker not found)"
        title = f"Worker {worker_id}"
    else:
        lines = list(worker.output_log[-PEEK_OUTPUT_MAX_LINES:])
        if not lines:
            lines = ["(no output captured yet)"]
        if worker.last_line and (not lines or lines[-1] != worker.last_line):
            lines.append(f"— last: {worker.last_line}")

        offset = 0 if follow_tail else tail_offset
        end = max(0, len(lines) - offset)
        start = max(0, end - viewport_lines)
        visible = lines[start:end]
        if start > 0:
            visible.insert(0, f"… {start} older lines (j/k scroll) …")
        if end < len(lines):
            visible.append(f"… {len(lines) - end} newer …")

        body = "\n".join(visible)
        title = (
            f"Worker {worker.worker_id}  {worker.arxiv_id}  [{worker.status}]"
            "  esc/q close  j/k scroll"
        )
    return Panel(
        Text(body),
        title=title,
        border_style="yellow on grey23",
        width=overlay_w,
        height=overlay_h,
    )


def _render_main_dashboard(
    dash: DashboardState,
    snap: dict,
    now: float,
) -> Group:
    snapshot = snap["snapshot"]
    selected_worker_index = int(snap.get("selected_worker_index", 0))
    ui_focus = snap.get("ui_focus", "workers")
    events = snap["events"]
    finished_lines = snap["finished_lines"]
    finished_scroll = snap["finished_scroll"]
    dash.worker_table_first_row = WORKER_TABLE_FIRST_ROW
    dash.worker_row_map = _build_worker_row_map(snapshot)

    table = Table(expand=True, box=None)
    table.add_column("W", width=3, justify="right", no_wrap=True)
    table.add_column("arXiv", width=12, no_wrap=True)
    table.add_column("Title", width=30, no_wrap=True)
    table.add_column("Status", width=40, no_wrap=True)
    table.add_column("Elapsed", width=8, justify="right", no_wrap=True)
    table.add_column("Upd", width=7, justify="right", no_wrap=True)
    table.add_column("Summary", ratio=1, min_width=20)

    for i, st in enumerate(snapshot):
        status_text = st.status
        if st.status == "idle":
            status_text = "idle / waiting"

        summary_text = st.summary_short() or st.last_line[:60]
        age_s = None
        if st.last_update_at is not None:
            age_s = max(0.0, now - st.last_update_at)
        age_text = _format_age(age_s)
        age_style: str | None = None
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
                "export skipped (--skip-export)",
                "export skipped (no changes)",
            }
        ):
            age_style = "yellow"

        status_cell = Text(status_text)
        if st.status == "drained":
            status_cell.stylize("grey62")
        age_cell = Text(age_text, style=age_style)

        row_style = "reverse" if i == selected_worker_index and ui_focus == "workers" else None
        marker = ">" if i == selected_worker_index else " "

        table.add_row(
            f"{marker}{st.worker_id}",
            escape(st.arxiv_id),
            escape(_trim(st.title_short(), 30)),
            status_cell,
            _format_elapsed(st.elapsed_s()),
            age_cell,
            Text(summary_text),
            style=row_style,
        )

    header = _format_header_line(snap)
    keys_hint = _format_keys_hint_line()

    finished_end = max(0, len(finished_lines) - finished_scroll)
    finished_start = max(0, finished_end - FINISHED_WINDOW_LINES)
    visible_finished = finished_lines[finished_start:finished_end]
    if not visible_finished:
        visible_finished = ["(no finished papers yet)"]
    finished_title = f"Finished papers ({len(finished_lines)})  scroll={finished_scroll}"
    finished_border = "bold green" if ui_focus == "finished" else "green"
    finished_panel = Panel(
        Text("\n".join(visible_finished)),
        title=finished_title,
        border_style=finished_border,
    )

    log_lines = events[-LOG_WINDOW_LINES:] if events else ["(no worker log lines yet)"]
    log_panel = Panel(
        Text("\n".join(log_lines)),
        title="Recent worker output",
        border_style="cyan",
    )

    workers_title = Text("Workers", style="bold")
    return Group(header, keys_hint, workers_title, table, finished_panel, log_panel)


def _render_dashboard(dash: DashboardState) -> Group | Layout:
    now = time.time()
    snap, _ = dash.snapshot_for_render(now)
    peek_worker_id = snap.get("peek_worker_id")
    peek_tail_offset = int(snap.get("peek_tail_offset", 0))
    peek_follow_tail = bool(snap.get("peek_follow_tail", True))

    main = _render_main_dashboard(dash, snap, now)

    if peek_worker_id is None:
        return main

    overlay_w, overlay_h, main_h = _overlay_dimensions()
    peek_panel = _render_peek_overlay_panel(
        snap["snapshot"],
        int(peek_worker_id),
        overlay_w,
        overlay_h,
        tail_offset=peek_tail_offset,
        follow_tail=peek_follow_tail,
    )

    overlay_row = Layout(name="overlay_row")
    overlay_row.split_row(
        Layout(name="margin_left", ratio=1),
        Layout(Align.center(peek_panel, vertical="middle"), name="peek", ratio=2),
        Layout(name="margin_right", ratio=1),
    )

    root = Layout(name="root")
    root.split_column(
        Layout(main, name="main", size=main_h),
        Layout(overlay_row, name="overlay", size=overlay_h),
    )
    return root


def _enable_mouse_tracking() -> None:
    if sys.stdout.isatty():
        # 1000=click, 1002=drag, 1006=SGR coordinates, 1003=any-event (some terminals).
        sys.stdout.write("\x1b[?1000h\x1b[?1002h\x1b[?1003h\x1b[?1006h")
        sys.stdout.flush()


def _disable_mouse_tracking() -> None:
    if sys.stdout.isatty():
        sys.stdout.write("\x1b[?1000l\x1b[?1002l\x1b[?1003l\x1b[?1006l")
        sys.stdout.flush()


def _read_terminal_input(fd: int, timeout: float = 0) -> str | None:
    ready, _, _ = select.select([fd], [], [], timeout)
    if not ready:
        return None

    first = os.read(fd, 1)
    if not first:
        return None

    if first != b"\x1b":
        return first.decode("utf-8", errors="replace")

    seq = first
    deadline = time.monotonic() + INPUT_ESCAPE_DEADLINE_S
    while time.monotonic() < deadline:
        ready, _, _ = select.select([fd], [], [], 0.02)
        if not ready:
            break
        chunk = os.read(fd, 32)
        if not chunk:
            break
        seq += chunk
        text = seq.decode("utf-8", errors="replace")
        if MOUSE_SGR_RE.search(text):
            return text
        if _arrow_direction(text) is not None:
            return text
        if _special_key(text) is not None:
            return text
        if "~" in text and "[" in text:
            return text
        if len(seq) > 48:
            break
    return seq.decode("utf-8", errors="replace")


def _arrow_direction(inp: str) -> str | None:
    if not inp.startswith("\x1b"):
        return None
    if inp in ("\x1bOA", "\x1b[A"):
        return "arrow_up"
    if inp in ("\x1bOB", "\x1b[B"):
        return "arrow_down"
    if inp in ("\x1bOC", "\x1b[C"):
        return "arrow_right"
    if inp in ("\x1bOD", "\x1b[D"):
        return "arrow_left"
    match = ARROW_SEQ_RE.search(inp)
    if match is None:
        return None
    direction = match.group(1)
    return {
        "A": "arrow_up",
        "B": "arrow_down",
        "C": "arrow_right",
        "D": "arrow_left",
    }.get(direction)


def _normalize_input(inp: str) -> str:
    direction = _arrow_direction(inp)
    if direction is not None:
        return direction
    return inp


def _should_close_peek(inp: str) -> bool:
    if inp in {"q", "Q"}:
        return True
    if inp == "\x1b":
        return True
    if inp in ("\x1b[", "\x1b\\"):
        return True
    return inp.startswith("\x1b[") and inp.endswith("Z")


def _special_key(inp: str) -> str | None:
    if inp in ("\x1b[H", "\x1bOH", "\x1b[1~"):
        return "home"
    if inp in ("\x1b[F", "\x1bOF", "\x1b[4~"):
        return "end"
    return None


def _handle_mouse_press(dash: DashboardState, seq: str) -> None:
    if dash.peek_worker_id_snapshot() is not None:
        return
    match = MOUSE_SGR_RE.search(seq)
    if match is None:
        return
    btn, _col, row, action = (
        match.group(1),
        int(match.group(2)),
        int(match.group(3)),
        match.group(4),
    )
    if action not in {"M", "m"} or btn not in {"0", "32"}:
        return

    worker_id = _worker_id_at_screen_row(dash.worker_row_map, row)
    if worker_id is not None:
        dash.set_ui_focus("workers")
        dash.set_peek_worker(worker_id)


def _handle_dashboard_input(dash: DashboardState, inp: str) -> None:
    norm = _normalize_input(inp)
    special = _special_key(inp)
    snap, _ = dash.snapshot_for_render(time.time())
    worker_count = len(snap["snapshot"])
    focus = snap.get("ui_focus", "workers")

    if dash.peek_worker_id_snapshot() is not None:
        if _should_close_peek(inp):
            dash.clear_peek_worker()
        elif norm in {"arrow_up", "k", "K"}:
            dash.scroll_peek_toward_tail(3)
        elif norm in {"arrow_down", "j", "J"}:
            dash.scroll_peek_older(3)
        return

    if MOUSE_SGR_RE.search(inp):
        _handle_mouse_press(dash, inp)
        return

    if inp in {"w", "W"}:
        dash.set_ui_focus("workers")
        return
    if inp in {"f", "F"}:
        dash.set_ui_focus("finished")
        return

    if focus == "finished":
        if norm == "arrow_up" or inp in {"k", "K"}:
            dash.scroll_finished(+1)
        elif norm == "arrow_down" or inp in {"j", "J"}:
            dash.scroll_finished(-1)
        elif inp in {"\r", "\n"}:
            dash.set_ui_focus("workers")
        return

    if special == "home":
        dash.select_first_worker(worker_count)
        return
    if special == "end":
        dash.select_last_worker(worker_count)
        return

    if inp in {"n", "N", "\t"}:
        dash.move_worker_selection(+1, worker_count)
        return
    if inp in {"p", "P"}:
        dash.move_worker_selection(-1, worker_count)
        return
    if inp.isdigit():
        digit = int(inp)
        row_idx = digit - 1 if digit > 0 else 9
        dash.select_worker_index(row_idx, worker_count)
        return

    if norm == "arrow_up":
        dash.move_worker_selection(-1, worker_count)
    elif norm == "arrow_down":
        dash.move_worker_selection(+1, worker_count)
    elif inp in {"\r", "\n", "o", "O", " "}:
        dash.open_peek_for_selected_worker(snap["snapshot"])
    elif inp in {"k", "K"}:
        dash.scroll_finished(+1)
    elif inp in {"j", "J"}:
        dash.scroll_finished(-1)
    elif inp in {"+", "="}:
        dash.request_scale_up()
    elif inp in {"-", "_"}:
        dash.request_scale_down()


def _drain_terminal_input(dash: DashboardState, fd: int) -> None:
    while True:
        inp = _read_terminal_input(fd, timeout=0)
        if inp is None:
            break
        _handle_dashboard_input(dash, inp)


def _configure_terminal_input(fd: int) -> list:
    """Return prior termios attrs; leave terminal in cbreak without echo."""
    old_attrs = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    return old_attrs


def _run_manual_streaming(
    *,
    arxiv_id: str,
    model: str,
    force: bool,
    skip_screen: bool,
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
        "--queue-managed",
    ]
    if force:
        cmd.append("--force")
    if skip_screen:
        cmd.append("--skip-screen")

    project_root = Path(__file__).resolve().parents[1]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True,
        cwd=str(project_root),
        env=project_subprocess_env(project_root),
    )

    output_lines: list[str] = []
    if proc.stdout is None:
        raise RuntimeError("subprocess.Popen did not allocate stdout")
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

            def _on_line(_line: str = line) -> None:
                _append_worker_output(worker_state, _line)
                _update_state_from_line(worker_state, _line)
                worker_state.last_update_at = time.time()
                dash.events.append(f"w{worker_state.worker_id} {arxiv_id}: {_line[:180]}")

            dash.mutate(_on_line)
            LOGGER.debug("worker=%s arxiv=%s line=%s", worker_state.worker_id, arxiv_id, line[:180])
            continue

        if inactivity_timeout_s and (time.monotonic() - last_activity) > inactivity_timeout_s:

            def _on_timeout() -> None:
                dash.events.append(
                    f"w{worker_state.worker_id} {arxiv_id}: timed out after "
                    f"{int(inactivity_timeout_s)}s of inactivity"
                )
                worker_state.status = "timed out"
                worker_state.last_update_at = time.time()

            dash.mutate(_on_timeout)
            LOGGER.warning(
                "worker=%s arxiv=%s timed out after %.1fs inactivity",
                worker_state.worker_id,
                arxiv_id,
                inactivity_timeout_s,
            )

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

        def _on_tail_line(_line: str = line) -> None:
            _append_worker_output(worker_state, _line)
            _update_state_from_line(worker_state, _line)
            worker_state.last_update_at = time.time()
            dash.events.append(f"w{worker_state.worker_id} {arxiv_id}: {_line[:180]}")

        dash.mutate(_on_tail_line)

    def _on_subprocess_exit() -> None:
        if worker_state.status in {
            "done",
            "failed",
            "rejected",
            "timed out",
            "export skipped (--skip-export)",
            "export skipped (no changes)",
        }:
            return
        worker_state.status = "finalizing (subprocess exit)"
        worker_state.last_update_at = time.time()

    dash.mutate(_on_subprocess_exit)

    stdout = "\n".join(output_lines)
    return TodoQueueRunResult(returncode=proc.returncode or 0, stdout=stdout, stderr="")


def _worker_loop(
    *,
    worker_id: int,
    dash: DashboardState,
    model: str,
    force: bool,
    skip_screen: bool,
    max_papers: int,
    inactivity_timeout_s: float | None,
) -> None:
    state = dash.worker_states[worker_id - 1]

    handled = 0
    empty_claims = 0
    while not dash.stop_event.is_set():
        # Draining happens only between jobs so active work finishes gracefully.
        if dash.consume_drain_slot():

            def _on_drain() -> None:
                state.status = "drained"
                state.started_at = 0.0
                state.drained_at = time.time()
                state.last_update_at = time.time()
                dash.events.append(f"w{worker_id} drained and exited")

            dash.mutate(_on_drain)
            LOGGER.info("worker=%s drained and exiting", worker_id)
            return

        if max_papers > 0 and handled >= max_papers:
            dash.mutate(lambda: setattr(state, "status", "done (limit reached)"))
            LOGGER.info("worker=%s hit max-papers limit and exited", worker_id)
            return

        def _on_start(entry, _index, _total):
            queue_total, queue_max_refs, queue_failed_total = _queue_stats_snapshot()

            def _start_update() -> None:
                dash.queue_total = queue_total
                dash.queue_max_refs = queue_max_refs
                dash.queue_failed_total = queue_failed_total
                state.arxiv_id = entry.arxiv_id
                state.title = entry.title or ""
                state.status = "claimed"
                state.started_at = time.time()
                state.last_update_at = state.started_at
                state.dataset_current = ""
                state.dataset_names = []
                state.dataset_index = 0
                state.dataset_total = 0
                state.confidence = ""
                state.results_count = None
                state.proposed_model = ""
                state.dataset_breakdown = ""
                state.refs_at_start = entry.seen_count or 0
                state.manually_important = entry.is_manually_important
                state.new_results = 0
                state.updated_results = 0
                state.drained_at = None
                state.last_line = ""
                state.output_log.clear()
                dash.events.append(f"w{worker_id} claimed {entry.arxiv_id}")

            dash.mutate(_start_update)
            LOGGER.info(
                "worker=%s claimed arxiv=%s refs_at_start=%s queue_total=%s queue_max_refs=%s "
                "queue_failed_total=%s",
                worker_id,
                entry.arxiv_id,
                entry.seen_count or 0,
                queue_total,
                queue_max_refs,
                queue_failed_total,
            )

        def _runner(arxiv_id: str, *, model: str, force: bool) -> TodoQueueRunResult:
            result = _run_manual_streaming(
                arxiv_id=arxiv_id,
                model=model,
                force=force,
                skip_screen=skip_screen,
                inactivity_timeout_s=inactivity_timeout_s,
                worker_state=state,
                dash=dash,
            )

            def _on_db_finalize() -> None:
                if state.status.startswith("done"):
                    return
                state.status = "finalizing (db)"
                state.last_update_at = time.time()

            dash.mutate(_on_db_finalize)
            return result

        def _on_finish(_entry, status, _result, _index, _total):
            dataset_breakdown = _dataset_breakdown_from_output(state.arxiv_id)
            queue_total, queue_max_refs, queue_failed_total = _queue_stats_snapshot()

            def _finish_update() -> None:
                if status == "done":
                    dash.total_done += 1
                    state.completed += 1
                    state.status = "done"
                elif status == "pending":
                    state.status = "retrying later"
                else:
                    dash.total_failed += 1
                    state.failed += 1
                    state.status = status
                dash.queue_total = queue_total
                dash.queue_max_refs = queue_max_refs
                dash.queue_failed_total = queue_failed_total
                state.dataset_breakdown = dataset_breakdown
                state.last_update_at = time.time()
                dash.events.append(f"w{worker_id} finished {state.arxiv_id} => {status}")
                finished_summary = state.summary_short() or _trim(state.last_line, 80)
                status_prefix = ""
                if status == "rejected":
                    status_prefix = "REJECTED "
                elif status == "failed":
                    status_prefix = "FAILED "
                elif status == "pending":
                    status_prefix = "RETRY "
                finished_line = f"{state.arxiv_id:<12}  {(_trim(state.title, 30) or '-'):30}  {status_prefix}{finished_summary}"
                dash.finished_lines.append(finished_line)

            dash.mutate(_finish_update)
            LOGGER.info(
                "worker=%s finished arxiv=%s status=%s summary=%s",
                worker_id,
                state.arxiv_id,
                status,
                (state.summary_short() or state.last_line[:120]),
            )

        summary = process_queue(
            limit=1,
            model=model,
            force=force,
            dry_run=False,
            refresh_dev_exports=False,
            runner=_runner,
            on_start=_on_start,
            on_finish=_on_finish,
        )

        if summary.total_selected == 0:
            empty_claims += 1

            pending_ready = _pending_ready_count()

            def _waiting_update(_pending_ready: int = pending_ready) -> None:
                if _pending_ready > 0:
                    state.status = f"waiting for claim ({_pending_ready} ready)"
                else:
                    state.status = "waiting for claim"
                state.started_at = 0.0
                state.last_update_at = time.time()

            dash.mutate(_waiting_update)
            LOGGER.info(
                "worker=%s empty-claim retry=%s pending_ready=%s",
                worker_id,
                empty_claims,
                pending_ready,
            )

            # If pending rows still exist, treat this as transient contention and keep retrying.
            if pending_ready > 0:
                empty_claims = 0
                time.sleep(EMPTY_CLAIM_RETRY_SLEEP_S + random.uniform(0.0, 0.25))
                continue

            if empty_claims >= EMPTY_CLAIM_RETRIES:

                def _idle_update() -> None:
                    state.status = "idle (queue empty)"
                    state.last_update_at = time.time()

                dash.mutate(_idle_update)
                LOGGER.info("worker=%s went idle (queue empty)", worker_id)
                return

            time.sleep(EMPTY_CLAIM_RETRY_SLEEP_S + random.uniform(0.0, 0.25))
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
        "--skip-screen", action="store_true", help="Pass --skip-screen to run_manual.py"
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
    parser.add_argument(
        "--diag-log-path",
        default="logs/todo_queue_dashboard.log",
        metavar="PATH",
        help="Diagnostic log file path (default: logs/todo_queue_dashboard.log)",
    )
    parser.add_argument(
        "--diag-heartbeat-sec",
        type=float,
        default=2.0,
        metavar="SEC",
        help="Diagnostic heartbeat interval in seconds (default: 2)",
    )
    parser.add_argument(
        "--diag-stall-sec",
        type=float,
        default=15.0,
        metavar="SEC",
        help="If UI render loop is inactive for this long, write thread dump (default: 15)",
    )
    return parser


def _diagnostics_watchdog(
    *,
    dash: DashboardState,
    log_path: str,
    heartbeat_sec: float,
    stall_sec: float,
) -> None:
    """Emit heartbeats and dump stacks when UI render loop appears stalled."""
    last_dump_at = 0.0
    while not dash.stop_event.is_set():
        time.sleep(max(0.2, heartbeat_sec))
        now = time.monotonic()
        last_render_age = now - dash.ui_last_render_at
        desired_workers, drain_requests = dash.snapshot_counts()
        snap, using_cache = dash.snapshot_for_render(time.time())
        active_workers = len(
            [s for s in snap.get("snapshot", []) if str(getattr(s, "status", "")) != "drained"]
        )

        LOGGER.info(
            "heartbeat loop_iter=%s last_render_age=%.2fs active_workers=%s desired=%s draining=%s "
            "queue_total=%s queue_max_refs=%s lock_drops=%s cache_uses=%s using_cache=%s",
            dash.ui_loop_iterations,
            last_render_age,
            active_workers,
            desired_workers,
            drain_requests,
            snap.get("queue_total", 0),
            snap.get("queue_max_refs", 0),
            snap.get("lock_contention_drops", 0),
            dash.render_cache_uses,
            using_cache,
        )

        if last_render_age >= stall_sec and (now - last_dump_at) >= stall_sec:
            reason = f"ui render stalled for {last_render_age:.2f}s"
            LOGGER.error(reason)
            _dump_all_thread_stacks(log_path, reason)
            last_dump_at = now


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    _configure_logger(args.diag_log_path)
    LOGGER.info(
        "starting dashboard workers=%s model=%s inactivity_timeout_min=%s",
        args.workers,
        args.model,
        args.inactivity_timeout_min,
    )

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
                "skip_screen": args.skip_screen,
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

    diag_thread = threading.Thread(
        target=_diagnostics_watchdog,
        kwargs={
            "dash": dash,
            "log_path": args.diag_log_path,
            "heartbeat_sec": args.diag_heartbeat_sec,
            "stall_sec": args.diag_stall_sec,
        },
        daemon=True,
        name="todo-dashboard-diag",
    )
    diag_thread.start()

    stdin_fd: int | None = None
    stdin_old_attrs: list | None = None
    if sys.stdin.isatty():
        stdin_fd = sys.stdin.fileno()
        stdin_old_attrs = _configure_terminal_input(stdin_fd)

    try:
        # Use manual refresh to avoid dependence on Live's internal refresh thread.
        # If that thread wedges under load, the UI can look frozen while work continues.
        with Live(
            _render_dashboard(dash),
            refresh_per_second=2,
            screen=True,
            auto_refresh=False,
        ) as live:
            _enable_mouse_tracking()
            last_fingerprint: str | None = None
            force_redraw = True

            while True:
                user_input = False
                if stdin_fd is not None:
                    inp = _read_terminal_input(stdin_fd, timeout=0.25)
                    if inp is not None:
                        user_input = True
                        _handle_dashboard_input(dash, inp)
                        _drain_terminal_input(dash, stdin_fd)
                else:
                    time.sleep(0.25)

                for _ in range(dash.consume_scale_up_requests()):
                    new_worker_id = dash.reserve_new_worker_id()
                    if new_worker_id < 0:
                        continue
                    _spawn_worker(new_worker_id)
                    dash.add_event(f"w{new_worker_id} spawned")
                    force_redraw = True

                threads[:] = [t for t in threads if t.is_alive()]

                now = time.time()
                snap, _ = dash.snapshot_for_render(now)
                fingerprint = _dashboard_render_fingerprint(snap, now)
                if user_input or force_redraw or fingerprint != last_fingerprint:
                    live.update(_render_dashboard(dash), refresh=True)
                    last_fingerprint = fingerprint
                    force_redraw = False
                    dash.ui_last_render_at = time.monotonic()
                    dash.ui_loop_iterations += 1

                desired_workers, _ = dash.snapshot_counts()
                if not threads and desired_workers <= 0:
                    break
                if not threads and desired_workers > 0:
                    break

            live.update(_render_dashboard(dash), refresh=True)
    except KeyboardInterrupt:
        dash.stop_event.set()
        LOGGER.info("keyboard interrupt received; shutting down")
        for t in threads:
            t.join(timeout=1.0)
    finally:
        dash.stop_event.set()
        diag_thread.join(timeout=0.5)
        _disable_mouse_tracking()
        if stdin_fd is not None and stdin_old_attrs is not None:
            termios.tcsetattr(stdin_fd, termios.TCSADRAIN, stdin_old_attrs)
        LOGGER.info("dashboard stopped")


if __name__ == "__main__":
    main()
