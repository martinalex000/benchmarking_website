#!/usr/bin/env python3
"""Compatibility wrapper for the unified todo queue CLI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console

from backend.models import todo_paper_status_from_exit_code
from scripts.todo_queue import main as todo_queue_main

console = Console()


def _run_paper(arxiv_id: str, model: str, dry_run: bool) -> str:
    cmd = [
        sys.executable,
        str(Path(__file__).parent / "run_manual.py"),
        arxiv_id,
        "--model",
        model,
    ]
    if dry_run:
        console.print(f"[dim][dry-run] would run: {' '.join(cmd)}[/dim]")
        return "dry-run"

    result = subprocess.run(cmd, capture_output=False)
    return todo_paper_status_from_exit_code(result.returncode).value


def main() -> None:
    todo_queue_main(["process", *sys.argv[1:]])


if __name__ == "__main__":
    main()
