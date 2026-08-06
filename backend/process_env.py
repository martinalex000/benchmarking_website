"""Helpers for launching project-owned subprocesses."""

from __future__ import annotations

import os
from pathlib import Path


def project_subprocess_env(project_root: Path) -> dict[str, str]:
    """Return an environment that resolves imports from this checkout first."""
    root = str(project_root.resolve())
    env = os.environ.copy()
    existing = [entry for entry in env.get("PYTHONPATH", "").split(os.pathsep) if entry]
    env["PYTHONPATH"] = os.pathsep.join([root, *[entry for entry in existing if entry != root]])
    return env
