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

from backend.todo_queue import TodoQueueRunResult, process_queue

ANSI_RE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
EXTRACT_DATASET_RE = re.compile(r"extract_dataset:([^\s]+)")
CONFIDENCE_RE = re.compile(r"Confidence:\s*([^\s]+)")
RESULTS_RE = re.compile(r"Results:\s*(\d+)")
PROPOSED_RE = re.compile(r"Proposed:\s*([^\n]+)$")
NEW_RESULTS_RE = re.compile(r"(\d+)\s+new result row")
UPDATED_RESULTS_RE = re.compile(r"(\d+)\s+existing result row\(s\) updated")


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
    new_results: int = 0
    updated_results: int = 0
    started_at: float = 0.0
    completed: int = 0
    failed: int = 0
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
        if self.dataset_total:
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
        self.events: deque[str] = deque(maxlen=event_lines)
        self.finished_lines: list[str] = []
        self.finished_scroll: int = 0
        self.total_done = 0
        self.total_failed = 0

    def add_event(self, message: str) -> None:
        with self.lock:
            self.events.append(message)

    def add_finished_line(self, line: str) -> None:
        with self.lock:
            self.finished_lines.append(line)

    def scroll_finished(self, delta: int) -> None:
        with self.lock:
            max_scroll = max(0, len(self.finished_lines) - 1)
            self.finished_scroll = max(0, min(max_scroll, self.finished_scroll + delta))


def _trim(text: str, max_len: int) -> str:
    text = (text or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


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


def _render_dashboard(dash: DashboardState) -> Group:
    with dash.lock:
        snapshot = [s for s in dash.worker_states]
        events = list(dash.events)
        finished_lines = list(dash.finished_lines)
        finished_scroll = dash.finished_scroll
        total_done = dash.total_done
        total_failed = dash.total_failed

    table = Table(expand=True)
    table.add_column("W", width=3, justify="right", no_wrap=True)
    table.add_column("arXiv", width=12, no_wrap=True)
    table.add_column("Title", width=30, no_wrap=True)
    table.add_column("Status", width=40, no_wrap=True)
    table.add_column("Elapsed", width=8, justify="right", no_wrap=True)
    table.add_column("Summary")

    for st in snapshot:
        status_text = st.status
        if st.status == "idle":
            status_text = "idle / waiting"
        summary_text = st.summary_short() or st.last_line[:60]
        table.add_row(
            str(st.worker_id),
            st.arxiv_id,
            _trim(st.title_short(), 30),
            status_text,
            _format_elapsed(st.elapsed_s()),
            summary_text,
        )

    header = Text(
        "todo_queue dashboard   "
        f"done={total_done}   failed={total_failed}   "
        "ctrl+c to stop   arrows/j,k scroll finished papers",
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

    return Group(header, table, finished_panel, log_panel)


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
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_attrs)


def _run_manual_streaming(
    *,
    arxiv_id: str,
    model: str,
    force: bool,
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
    for raw_line in proc.stdout:
        line = _strip_ansi(raw_line)
        if not line:
            continue
        output_lines.append(line)

        with dash.lock:
            _update_state_from_line(worker_state, line)
            dash.events.append(f"w{worker_state.worker_id} {arxiv_id}: {line[:180]}")

    proc.wait()
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
) -> None:
    state = dash.worker_states[worker_id - 1]

    handled = 0
    while not dash.stop_event.is_set():
        if max_papers > 0 and handled >= max_papers:
            with dash.lock:
                state.status = "done (limit reached)"
            return

        def _on_start(entry, _index, _total):
            with dash.lock:
                state.arxiv_id = entry.arxiv_id
                state.title = entry.title or ""
                state.status = "claimed"
                state.started_at = time.time()
                state.dataset_current = ""
                state.dataset_index = 0
                state.dataset_total = 0
                state.confidence = ""
                state.results_count = None
                state.proposed_model = ""
                state.new_results = 0
                state.updated_results = 0
                state.last_line = ""
                dash.events.append(f"w{worker_id} claimed {entry.arxiv_id}")

        def _runner(arxiv_id: str, *, model: str, force: bool) -> TodoQueueRunResult:
            return _run_manual_streaming(
                arxiv_id=arxiv_id,
                model=model,
                force=force,
                worker_state=state,
                dash=dash,
            )

        def _on_finish(_entry, status, _result, _index, _total):
            with dash.lock:
                if status == "done":
                    dash.total_done += 1
                    state.completed += 1
                    state.status = "done"
                else:
                    dash.total_failed += 1
                    state.failed += 1
                    state.status = status
                dash.events.append(f"w{worker_id} finished {state.arxiv_id} => {status}")
                finished_summary = state.summary_short() or _trim(state.last_line, 80)
                finished_line = (
                    f"{state.arxiv_id:<12}  {(_trim(state.title, 30) or '-'):30}  "
                    f"{status:<8}  {finished_summary}"
                )
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
            with dash.lock:
                state.status = "idle (queue empty)"
                state.started_at = 0.0
            return

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
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    if args.workers <= 0:
        raise SystemExit("--workers must be >= 1")

    dash = DashboardState(workers=args.workers)

    threads: list[threading.Thread] = []
    for idx in range(1, args.workers + 1):
        t = threading.Thread(
            target=_worker_loop,
            kwargs={
                "worker_id": idx,
                "dash": dash,
                "model": args.model,
                "force": args.force,
                "max_attempts": args.max_attempts,
                "max_papers": args.max_papers_per_worker,
            },
            daemon=True,
            name=f"todo-worker-{idx}",
        )
        threads.append(t)
        t.start()

    key_thread = threading.Thread(
        target=_keyboard_listener,
        kwargs={"dash": dash},
        daemon=True,
        name="todo-dashboard-keys",
    )
    key_thread.start()

    try:
        with Live(_render_dashboard(dash), refresh_per_second=4, screen=True) as live:
            while any(t.is_alive() for t in threads):
                live.update(_render_dashboard(dash))
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
