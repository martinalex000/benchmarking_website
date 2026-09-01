#!/usr/bin/env python3
"""Create exploratory figures for stale baselines inside and outside LRGB."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from backend.stale_baselines_analysis import load_analysis_rows, run, write_outputs, write_report


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

    peer_reviewed_dir = args.output_dir / "peer_reviewed"
    peer_reviewed_rows, peer_reviewed_metadata = load_analysis_rows(
        args.db, peer_reviewed_only=True
    )
    peer_reviewed_paths = write_outputs(
        peer_reviewed_rows, peer_reviewed_metadata, peer_reviewed_dir
    )
    peer_reviewed_paths.append(
        write_report(
            peer_reviewed_rows,
            peer_reviewed_metadata,
            peer_reviewed_dir,
            peer_reviewed_paths,
        )
    )
    for path in peer_reviewed_paths:
        print(path)

    conference_dir = args.output_dir / "conference_only"
    conference_rows, conference_metadata = load_analysis_rows(args.db, conference_only=True)
    conference_paths = write_outputs(conference_rows, conference_metadata, conference_dir)
    conference_paths.append(
        write_report(conference_rows, conference_metadata, conference_dir, conference_paths)
    )
    for path in conference_paths:
        print(path)


if __name__ == "__main__":
    main()
