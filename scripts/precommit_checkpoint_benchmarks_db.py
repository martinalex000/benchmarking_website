#!/usr/bin/env python3
"""Pre-commit hook wrapper (see backend.benchmarks_db_precommit)."""

from backend.benchmarks_db_precommit import main

if __name__ == "__main__":
    raise SystemExit(main())
