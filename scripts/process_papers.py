#!/usr/bin/env python3
"""Process one paper directly or process the queue in the live dashboard.

Examples::

    uv run python scripts/process_papers.py 2206.08164
    uv run python scripts/process_papers.py 2206.08164 --force
    uv run python scripts/process_papers.py dashboard
    uv run python scripts/process_papers.py dashboard --workers 4
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _build_parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        description="Process one arXiv paper or papers from the shared queue.",
        usage="%(prog)s ARXIV_ID [OPTIONS]\n       %(prog)s dashboard [OPTIONS]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""examples:
  %(prog)s 2206.08164
  %(prog)s 2206.08164 --model fallback --force
  %(prog)s dashboard
  %(prog)s dashboard --workers 4 --model primary

Run either form with --help to see its available options.
""",
        add_help=False,
    )


def _print_help() -> None:
    parser = _build_parser()
    parser.add_argument("-h", "--help", action="help", help="show this help message and exit")
    parser.print_help()


def _run_paper(argv: list[str]) -> None:
    from scripts.run_manual import main

    main(argv)


def _run_dashboard(argv: list[str]) -> None:
    from scripts.todo_queue_dashboard import main

    main(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """Dispatch to direct-paper processing or the queue dashboard."""
    arguments = list(sys.argv[1:] if argv is None else argv)
    if not arguments or arguments[0] in {"-h", "--help"}:
        _print_help()
        return 0

    if arguments[0] == "dashboard":
        _run_dashboard(arguments[1:])
        return 0

    if arguments[0].startswith("-"):
        parser = _build_parser()
        parser.error("provide an arXiv ID or use the 'dashboard' command")

    _run_paper(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
