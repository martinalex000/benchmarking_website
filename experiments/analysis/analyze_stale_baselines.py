#!/usr/bin/env python3
"""Create exploratory figures for stale baselines inside and outside LRGB."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.stale_baselines_analysis import run


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=Path("data/benchmarks.db"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/stale_baselines"),
    )
    args = parser.parse_args()
    for path in run(args.db, args.output_dir):
        print(path)


if __name__ == "__main__":
    main()
