import importlib.util
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[2]
_DASHBOARD_PATH = _ROOT / "scripts" / "todo_queue_dashboard.py"


def _load_dashboard():
    spec = importlib.util.spec_from_file_location("todo_queue_dashboard", _DASHBOARD_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["todo_queue_dashboard"] = module
    spec.loader.exec_module(module)
    return module


def test_detect_status_skip_export_not_exporting():
    dash = _load_dashboard()
    status = dash._detect_status_from_line(
        "6. Build Hugo Pages — skipped (--skip-export)"
    )
    assert status == "export skipped (--skip-export)"


def test_dashboard_forwards_skip_screen_to_manual_runner(monkeypatch):
    dash = _load_dashboard()
    captured = {}

    def _popen(cmd, **_kwargs):
        captured["cmd"] = cmd
        raise RuntimeError("stop after command construction")

    monkeypatch.setattr(dash.subprocess, "Popen", _popen)
    with pytest.raises(RuntimeError, match="stop after command construction"):
        dash._run_manual_streaming(
            arxiv_id="2206.08164",
            model="primary",
            force=False,
            skip_screen=True,
            inactivity_timeout_s=None,
            worker_state=dash.WorkerState(worker_id=1),
            dash=dash.DashboardState(workers=1),
        )
    assert "--skip-screen" in captured["cmd"]


def test_detect_status_real_export():
    dash = _load_dashboard()
    assert dash._detect_status_from_line("6. Build Hugo Pages") == "exporting hugo"
    assert dash._detect_status_from_line("Exporting datasets:  12%|") == "exporting datasets"


def test_detect_status_done_rule():
    dash = _load_dashboard()
    assert dash._detect_status_from_line("──────────────────────── Done ────────────────────────") == "done"


def test_worker_id_at_screen_row():
    dash = _load_dashboard()
    first_row = dash.WORKER_TABLE_FIRST_ROW
    row_map = dash._build_worker_row_map_at(
        [dash.WorkerState(worker_id=1), dash.WorkerState(worker_id=2)],
        first_row,
    )
    assert dash._worker_id_at_screen_row(row_map, first_row) == 1
    assert dash._worker_id_at_screen_row(row_map, first_row + 1) == 2
    assert dash._worker_id_at_screen_row(row_map, 1) is None


def test_special_keys():
    dash = _load_dashboard()
    assert dash._special_key("\x1b[H") == "home"
    assert dash._special_key("\x1b[F") == "end"
    assert dash._special_key("\x1b[1~") == "home"
    assert dash._special_key("\x1b[4~") == "end"


def test_normalize_arrow_keys():
    dash = _load_dashboard()
    assert dash._normalize_input("\x1bOA") == "arrow_up"
    assert dash._normalize_input("\x1b[A") == "arrow_up"
    assert dash._normalize_input("\x1b[1;5A") == "arrow_up"
    assert dash._normalize_input("\x1bOB") == "arrow_down"
    assert dash._normalize_input("\x1b[B") == "arrow_down"


def test_should_close_peek():
    dash = _load_dashboard()
    assert dash._should_close_peek("\x1b")
    assert dash._should_close_peek("q")
    assert not dash._should_close_peek("j")
    assert not dash._should_close_peek("k")
    assert not dash._should_close_peek("\x1b[A")


def test_header_line_stable_width():
    dash = _load_dashboard()
    snap = {
        "total_done": 1,
        "total_failed": 0,
        "queue_total": 10,
        "queue_max_refs": 5,
        "desired_workers": 3,
        "drain_requests": 0,
        "ui_focus": "workers",
    }
    line_a = dash._format_header_line(snap).plain
    snap["total_done"] = 9999
    line_b = dash._format_header_line(snap).plain
    assert len(line_a) == len(line_b)
    dash_mod = _load_dashboard()
    state = dash_mod.DashboardState(workers=3)
    state.select_worker_index(2, 3)
    assert state.selected_worker_index == 2
    assert state.ui_focus == "workers"
    dash_mod = _load_dashboard()
    state = dash_mod.DashboardState(workers=2)
    state.move_worker_selection(+1, 3)
    assert state.selected_worker_index == 1
    state.move_worker_selection(+1, 3)
    assert state.selected_worker_index == 2
    state.move_worker_selection(+1, 3)
    assert state.selected_worker_index == 0
    state.move_worker_selection(-1, 3)
    assert state.selected_worker_index == 2
