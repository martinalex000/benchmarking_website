#!/usr/bin/env python3
"""repopulate_db.py — Re-extract and re-parse all existing papers.

Walks every paper directory under papers/ and re-runs the full extraction +
parse pipeline.  Downloads are never touched.

Typical use-case: after a major update to the extraction pipeline you want to
refresh all results without re-downloading anything.

Usage::
    # Full clean slate — wipe DB, delete all previous LLM outputs, re-extract everything
    uv run python scripts/repopulate_db.py --clean

    # Same but use the fallback model for every paper
    uv run python scripts/repopulate_db.py --clean --model fallback

    # Clean slate for specific papers only
    uv run python scripts/repopulate_db.py --clean --paper 2206.08164 2309.00367

    # Re-extract without wiping DB (upserts results, keeps overrides)
    uv run python scripts/repopulate_db.py

    # Re-parse only (skip LLM calls, re-read existing llm_output artifacts)
    uv run python scripts/repopulate_db.py --skip-extract

    # Extract only, don't touch the DB yet
    uv run python scripts/repopulate_db.py --skip-parse

    # Also regenerate Hugo content files at the end
    uv run python scripts/repopulate_db.py --clean --export

    # Preview what would happen without doing anything
    uv run python scripts/repopulate_db.py --clean --dry-run
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.table import Table

from backend.config import cfg
from backend.db import init_db

console = Console()
logging.basicConfig(level=logging.INFO, format="%(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)


def _discover_arxiv_ids(only: list[str] | None = None) -> list[str]:
    """Return all arXiv IDs that have a downloaded paper directory."""
    papers_dir = cfg.papers_dir
    ids: list[str] = []
    for d in sorted(papers_dir.iterdir()):
        if not d.is_dir():
            continue
        arxiv_id = d.name
        # Skip directories that don't look like arXiv IDs
        if not arxiv_id or arxiv_id.startswith("."):
            continue
        if only and arxiv_id not in only:
            continue
        ids.append(arxiv_id)
    return ids


def _has_download(arxiv_id: str) -> bool:
    from backend.paper_storage import PaperStorage

    s = PaperStorage(arxiv_id)
    return s.pdf_path.exists() or s.html_index_path.exists()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Re-extract and re-parse all existing papers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--paper",
        nargs="+",
        metavar="ARXIV_ID",
        help="Limit to specific arXiv IDs (default: all papers/)",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="primary",
        help="Model tier for extraction (default: primary).  Use 'fallback' to force the "
        "fallback model even for papers that already have fallback results.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help=(
            "Start from a clean slate: delete the database and all previous llm_output*.yaml/json "
            "files before re-running.  Downloads (PDF/HTML/LaTeX) are kept.  The DB is "
            "re-seeded from config/seed_data.yaml after the wipe."
        ),
    )
    parser.add_argument(
        "--skip-extract",
        action="store_true",
        help="Skip LLM extraction; only re-parse existing llm_output artifacts",
    )
    parser.add_argument(
        "--skip-parse",
        action="store_true",
        help="Run extraction but skip storing results back into the DB",
    )
    parser.add_argument(
        "--export",
        action="store_true",
        help="Re-export Hugo content files after all papers are processed",
    )
    parser.add_argument(
        "--skip-screen",
        action="store_true",
        help="Skip abstract screening (stage 1) for every paper",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without actually running anything",
    )
    args = parser.parse_args()

    arxiv_ids = _discover_arxiv_ids(only=args.paper)
    if not arxiv_ids:
        console.print("[yellow]No paper directories found under papers/[/yellow]")
        sys.exit(0)

    model_name = cfg.model_for_tier(args.model)
    console.rule("[bold]Repopulate DB[/bold]")
    console.print(f"  Papers     : {len(arxiv_ids)}")
    console.print(f"  Model      : [cyan]{model_name}[/cyan]  (tier={args.model})")
    console.print(
        f"  Clean      : {'[bold red]YES — wipe DB + llm_output files[/bold red]' if args.clean else '[dim]no[/dim]'}"
    )
    console.print(
        f"  Extract    : {'[dim]skipped[/dim]' if args.skip_extract else '[green]yes[/green]'}"
    )
    console.print(
        f"  Parse      : {'[dim]skipped[/dim]' if args.skip_parse else '[green]yes[/green]'}"
    )
    console.print(f"  Export     : {'[green]yes[/green]' if args.export else '[dim]no[/dim]'}")
    console.print(
        f"  Dry-run    : {'[yellow]YES — nothing will be changed[/yellow]' if args.dry_run else 'no'}"
    )
    console.print()

    if args.dry_run:
        if args.clean:
            console.print("[bold yellow]Would delete:[/bold yellow]")
            console.print(f"  • {cfg.db_path}")
            from backend.paper_storage import PaperStorage

            for aid in arxiv_ids:
                s = PaperStorage(aid)
                for f in list(s.extracted_dir.glob("llm_output*.yaml")) + list(
                    s.extracted_dir.glob("llm_output*.json")
                ):
                    console.print(f"  • {f.relative_to(cfg.project_root)}")
            console.print()

        t = Table(show_header=True, header_style="bold")
        t.add_column("arXiv ID")
        t.add_column("Downloaded")
        t.add_column("Has extraction")
        t.add_column("Action")
        from backend.paper_storage import PaperStorage

        for aid in arxiv_ids:
            s = PaperStorage(aid)
            has_dl = "✓" if _has_download(aid) else "✗"
            has_ext = "✓" if s.llm_output_path.exists() else "—"
            if not _has_download(aid):
                action = "[red]skip — no download[/red]"
            elif args.skip_extract:
                action = "parse only"
            else:
                action = "extract + parse" if not args.skip_parse else "extract only"
            t.add_row(aid, has_dl, has_ext, action)
        console.print(t)
        return

    # ── Clean slate ───────────────────────────────────────────────────────
    if args.clean:
        console.print("[bold red]Wiping database and previous extraction outputs…[/bold red]")

        # Delete the SQLite database file
        if cfg.db_path.exists():
            cfg.db_path.unlink()
            console.print(f"  Deleted [dim]{cfg.db_path}[/dim]")

        # Delete all llm_output artifacts for the affected papers
        from backend.paper_storage import PaperStorage

        for aid in arxiv_ids:
            s = PaperStorage(aid)
            for f in sorted(
                list(s.extracted_dir.glob("llm_output*.yaml"))
                + list(s.extracted_dir.glob("llm_output*.json"))
            ):
                f.unlink()
                console.print(f"  Deleted [dim]{f.relative_to(cfg.project_root)}[/dim]")

        # Re-create and re-seed the DB
        console.print("\n  Re-seeding database from config/seed_data.yaml…")
        from backend.seed_db import seed

        init_db()
        seed()
        console.print("  [green]Database re-seeded.[/green]\n")
    else:
        init_db()

    from backend.llm_extractor import run_extraction
    from backend.results_parser import parse_and_store

    ok_count = fail_count = skip_count = 0
    processed_ids: list[str] = []

    for aid in arxiv_ids:
        console.rule(f"[dim]{aid}[/dim]", style="dim")

        if not _has_download(aid):
            console.print("  [yellow]Skip[/yellow] — no downloaded content (run download first)")
            skip_count += 1
            continue

        # ── Extract ───────────────────────────────────────────────────────
        if not args.skip_extract:
            ok = run_extraction(
                aid,
                model_tier=args.model,
                screen_first=not args.skip_screen,
                fallback_on_failure=(args.model == "primary"),
                extraction_strategy="two-step",
                verbose=True,
            )
            if not ok:
                console.print(f"  [red]Extraction failed for {aid}[/red]")
                fail_count += 1
                continue

        # ── Parse ─────────────────────────────────────────────────────────
        if not args.skip_parse:
            from backend.paper_storage import PaperStorage

            s = PaperStorage(aid)
            if not s.llm_output_path.exists():
                console.print("  [yellow]Skip parse[/yellow] — no llm_output artifact")
                skip_count += 1
                continue
            try:
                n = parse_and_store(aid)
                console.print(f"  [green]{n} result(s) stored[/green]")
            except Exception as exc:
                console.print(f"  [red]Parse failed: {exc}[/red]")
                fail_count += 1
                continue

        ok_count += 1
        processed_ids.append(aid)

    # ── Export ────────────────────────────────────────────────────────────
    if args.export and processed_ids:
        console.rule("[bold]Exporting Hugo files[/bold]")
        from backend.export_to_hugo import export_all

        export_all(arxiv_ids=processed_ids)
        console.print("  [green]Export complete[/green]")

    console.rule("[bold]Done[/bold]")
    console.print(
        f"  [green]{ok_count} ok[/green]  "
        f"[red]{fail_count} failed[/red]  "
        f"[dim]{skip_count} skipped[/dim]"
    )
    if fail_count:
        sys.exit(1)


if __name__ == "__main__":
    main()
