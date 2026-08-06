from pathlib import Path

from backend import todo_queue
from backend.process_env import project_subprocess_env


def test_project_subprocess_env_puts_checkout_first(monkeypatch):
    root = Path("/tmp/benchmarking-checkout")
    monkeypatch.setenv("PYTHONPATH", "/opt/old-backend:/opt/other")

    env = project_subprocess_env(root)

    assert env["PYTHONPATH"].split(":") == [str(root.resolve()), "/opt/old-backend", "/opt/other"]


def test_project_subprocess_env_deduplicates_checkout(monkeypatch):
    root = Path("/tmp/benchmarking-checkout").resolve()
    monkeypatch.setenv("PYTHONPATH", f"/opt/old:{root}:/opt/other")

    env = project_subprocess_env(root)

    assert env["PYTHONPATH"].split(":") == [str(root), "/opt/old", "/opt/other"]


def test_queue_runner_pins_project_import_environment(monkeypatch):
    captured = {}

    def fake_run(command, **kwargs):
        captured["command"] = command
        captured["kwargs"] = kwargs
        return todo_queue.subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.setattr(todo_queue.subprocess, "run", fake_run)

    result = todo_queue.run_manual_subprocess("2206.08164", model="primary", force=False)

    project_root = Path(__file__).resolve().parents[2]
    assert result.returncode == 0
    assert captured["kwargs"]["cwd"] == str(project_root)
    assert captured["kwargs"]["env"]["PYTHONPATH"].split(":")[0] == str(project_root)
