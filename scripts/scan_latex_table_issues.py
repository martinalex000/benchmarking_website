#!/usr/bin/env python3
"""Scan local LaTeX sources for table-parser blind spots.

Writes:
  - site/data/problematic_latex_papers.json  (development page input)
  - config/reextract_latex_papers.txt        (server re-extraction queue list)

Usage::

    uv run python scripts/scan_latex_table_issues.py
    uv run python scripts/scan_latex_table_issues.py --paper 2411.05274
    uv run python scripts/scan_latex_table_issues.py --write-list --export-json
    uv run python scripts/scan_latex_table_issues.py --mark --requeue
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rich.console import Console
from rich.table import Table

from backend.config import cfg, normalize_arxiv_id
from backend.db import init_db, session_scope
from backend.latex_source import diagnose_latex_table_coverage
from backend.models import Paper
from backend.todo_queue import add_todo_paper

console = Console()

_DEFAULT_JSON = cfg.site_dir / "data" / "problematic_latex_papers.json"
_DEFAULT_LIST = cfg.config_dir / "reextract_latex_papers.txt"


def _iter_paper_dirs(only: list[str] | None = None) -> list[Path]:
    papers_root = cfg.papers_dir
    if not papers_root.is_dir():
        return []
    dirs = sorted(path for path in papers_root.iterdir() if path.is_dir())
    if only:
        wanted = {normalize_arxiv_id(item) for item in only}
        dirs = [path for path in dirs if path.name in wanted]
    return dirs


def _paper_title(arxiv_id: str) -> str:
    init_db()
    with session_scope() as session:
        row = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        return row.title if row and row.title else ""


def scan_papers(only: list[str] | None = None) -> dict:
    scanned_at = datetime.now(UTC).isoformat()
    entries: list[dict] = []
    for paper_dir in _iter_paper_dirs(only):
        arxiv_id = paper_dir.name
        tex_path = paper_dir / "latex" / "expanded.tex"
        if not tex_path.is_file():
            continue
        tex = tex_path.read_text(encoding="utf-8", errors="replace")
        diagnostics = diagnose_latex_table_coverage(tex)
        if not diagnostics:
            continue
        entries.append(
            {
                "arxiv_id": arxiv_id,
                "title": _paper_title(arxiv_id),
                "latex_path": str(tex_path.relative_to(cfg.project_root)),
                "issues": [
                    {
                        "kind": item.kind,
                        "detail": item.detail,
                        "sample_lines": item.sample_lines,
                    }
                    for item in diagnostics
                ],
            }
        )

    entries.sort(key=lambda item: item["arxiv_id"])
    return {
        "scanned_at": scanned_at,
        "paper_count": len(entries),
        "papers": entries,
    }


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_reextract_list(path: Path, payload: dict) -> int:
    lines = [
        "# Papers that need full LLM re-extraction after LaTeX table-parser fixes.",
        "# One arXiv ID per line. Used by scripts/mark_reextract_papers.py.",
        "#",
        "# Regenerate with:",
        "#   uv run python scripts/scan_latex_table_issues.py --write-list",
        "#",
        f"# Last scan: {payload.get('scanned_at', 'unknown')}",
        "",
    ]
    for entry in payload.get("papers", []):
        arxiv_id = entry["arxiv_id"]
        title = entry.get("title") or ""
        kinds = ", ".join(sorted({issue["kind"] for issue in entry.get("issues", [])}))
        suffix = f"  # {title}" if title else ""
        lines.append(f"{arxiv_id}  # {kinds}{suffix}" if kinds else f"{arxiv_id}{suffix}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(payload.get("papers", []))


def _print_summary(payload: dict) -> None:
    papers = payload.get("papers", [])
    if not papers:
        console.print("[green]No problematic LaTeX table coverage issues found.[/green]")
        return

    table = Table(title="Problematic LaTeX papers", show_header=True, header_style="bold")
    table.add_column("arXiv", style="cyan")
    table.add_column("Issues")
    table.add_column("Title")
    for entry in papers:
        kinds = ", ".join(sorted({issue["kind"] for issue in entry.get("issues", [])}))
        title = (entry.get("title") or "")[:48]
        table.add_row(entry["arxiv_id"], kinds, title)
    console.print(table)


def _mark_for_reextract(payload: dict, *, requeue: bool, dry_run: bool) -> None:
    arxiv_ids = [entry["arxiv_id"] for entry in payload.get("papers", [])]
    if not arxiv_ids:
        console.print("[yellow]No papers to mark.[/yellow]")
        return

    if dry_run:
        console.print(f"[dim]Dry-run — would mark {len(arxiv_ids)} paper(s) important.[/dim]")
        for arxiv_id in arxiv_ids:
            console.print(f"  {arxiv_id}")
        return

    for arxiv_id in arxiv_ids:
        _created, message = add_todo_paper(
            arxiv_id,
            title=_paper_title(arxiv_id) or None,
            reason="latex_table_issues",
            added_by="scan_latex_table_issues.py",
            is_manually_important=True,
            requeue=requeue,
        )
        console.print(message)

    console.print(
        f"\n[green]Marked {len(arxiv_ids)} paper(s) for LLM re-extraction.[/green] "
        "Run workers with --force (see config/latex_table_reextract_server.txt)."
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scan papers for LaTeX table-parser blind spots.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--paper",
        nargs="*",
        metavar="ARXIV_ID",
        help="Limit scan to specific arXiv IDs",
    )
    parser.add_argument(
        "--export-json",
        action="store_true",
        help=f"Write JSON report (default: {_DEFAULT_JSON}; always on unless --write-list only)",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        default=_DEFAULT_JSON,
        help=f"JSON output path (default: {_DEFAULT_JSON})",
    )
    parser.add_argument(
        "--write-list",
        action="store_true",
        help=f"Write re-extract list to this path (default: {_DEFAULT_LIST})",
    )
    parser.add_argument(
        "--list-output",
        type=Path,
        default=_DEFAULT_LIST,
        help=f"Write re-extract list path (default: {_DEFAULT_LIST})",
    )
    parser.add_argument(
        "--mark",
        action="store_true",
        help="Mark scanned papers as manually important in todo_papers",
    )
    parser.add_argument(
        "--requeue",
        action="store_true",
        help="With --mark, reset done/failed/rejected rows back to pending",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview --mark without changing the DB",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    payload = scan_papers(args.paper)
    _print_summary(payload)

    _write_json(args.json_output, payload)
    console.print(f"[green]Wrote {args.json_output}[/green]")

    if args.write_list:
        count = _write_reextract_list(args.list_output, payload)
        console.print(f"[green]Wrote {count} row(s) to {args.list_output}[/green]")

    if args.mark:
        _mark_for_reextract(payload, requeue=args.requeue, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
