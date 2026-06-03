"""Pre-commit entrypoint: checkpoint benchmarks.db and block SQLite sidecar commits."""

from __future__ import annotations

import subprocess
import sys

from backend.benchmarks_db_checkpoint import (
    BENCHMARKS_DB_REL,
    is_benchmarks_db_sidecar,
    wal_checkpoint_truncate,
)
from backend.config import cfg


def _staged_paths() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=cfg.project_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def _restage_benchmarks_db() -> None:
    subprocess.run(
        ["git", "add", "--", BENCHMARKS_DB_REL],
        cwd=cfg.project_root,
        check=True,
    )


def main() -> int:
    staged = _staged_paths()
    sidecars = [path for path in staged if is_benchmarks_db_sidecar(path)]
    if sidecars:
        print(
            "Cannot commit SQLite sidecar files; only data/benchmarks.db belongs in git:",
            file=sys.stderr,
        )
        for path in sidecars:
            print(f"  {path}", file=sys.stderr)
        print(
            "Remove them from the index: git restore --staged <file>",
            file=sys.stderr,
        )
        return 1

    db_path = cfg.db_path
    if not db_path.is_file():
        return 0

    wal_checkpoint_truncate(db_path)
    if BENCHMARKS_DB_REL in staged:
        _restage_benchmarks_db()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
