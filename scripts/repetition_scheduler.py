#!/usr/bin/env python3
"""Run the whole-paper repetition extractor with a selected GLM endpoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.config import cfg
from backend.repetition_batch import run_batch

V5_COMPLETED_ROOT = (
    Path(__file__).resolve().parents[1]
    / "experiments/table_provenance_experiment/run_2026-10-14_full_mapping_recovery_v5/papers"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("worker", "status"))
    parser.add_argument(
        "--root",
        type=Path,
        default=cfg.papers_dir / "repetition_scheduler",
        help="whole-paper run directory (default: papers/repetition_scheduler)",
    )
    parser.add_argument("--endpoint", choices=("primary", "second"), default="primary")
    parser.add_argument("--concurrency", type=int, default=1)
    parser.add_argument("--paper", nargs="+", help="limit work to these arXiv IDs")
    parser.add_argument("--include-nonconference", action="store_true")
    parser.add_argument("--reuse-root", type=Path)
    parser.add_argument(
        "--exclude-root",
        type=Path,
        default=V5_COMPLETED_ROOT,
        help="exclude papers with assessment.json under this experiment's papers directory",
    )
    parser.add_argument(
        "--include-v5-completed",
        action="store_true",
        help="include papers already assessed by the v5 experiment",
    )
    parser.add_argument("--force", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.concurrency < 1:
        raise SystemExit("--concurrency must be positive")
    status_path = args.root / "status.json"
    if args.command == "status":
        if not status_path.exists():
            print(f"No run status at {status_path}")
            return 1
        print(json.dumps(json.loads(status_path.read_text()), indent=2, ensure_ascii=False))
        return 0

    result = run_batch(
        root=args.root,
        arxiv_ids=args.paper,
        force=args.force,
        night_max=args.concurrency,
        day_streams=args.concurrency,
        reuse_root=args.reuse_root,
        endpoint=args.endpoint,
        include_nonconference=args.include_nonconference,
        exclude_root=None if args.include_v5_completed else args.exclude_root,
    )
    print(
        f"Whole-paper repetition run: {result.get('completed', 0)}/{result.get('total', 0)} "
        f"papers; state={result.get('state')}; database_applied="
        f"{result.get('database_applied', False)}"
    )
    print(f"Report: {args.root / 'report.md'}")
    return 0 if result.get("state") == "finished" else 1


if __name__ == "__main__":
    raise SystemExit(main())
