#!/usr/bin/env python3
"""run_manual.py — process a single paper end-to-end.

Downloads the paper (PDF + HTML if available), runs LLM extraction, parses
results into the database, and re-exports the Hugo site.

Usage::
    uv run python scripts/run_manual.py 2206.08164
    uv run python scripts/run_manual.py 2206.08164 --model fallback
    uv run python scripts/run_manual.py 2206.08164 --skip-download
    uv run python scripts/run_manual.py 2206.08164 --skip-extract

Model names are resolved from config/llm_config.yaml / .env.
If a model is not found at the endpoint, run:
    uv run python scripts/list_models.py
to see what is available.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Ensure project root is on the path when run directly
sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.rule import Rule

console = Console()


def _fmt_bytes(n: int) -> str:
    if n >= 1_048_576:
        return f"{n / 1_048_576:.1f} MB"
    if n >= 1_024:
        return f"{n / 1_024:.0f} KB"
    return f"{n} B"


def _do_download(arxiv_id: str, force: bool) -> None:
    from backend.arxiv_downloader import download_paper
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)

    # Already downloaded?
    if not force and storage.pdf_path.exists():
        size = storage.pdf_path.stat().st_size
        html_note = " + HTML" if storage.html_index_path.exists() else " (no HTML version)"
        console.print(
            f"  [dim]Already downloaded ({_fmt_bytes(size)}{html_note}) — use --force to re-download[/dim]"
        )
        return

    ok = download_paper(arxiv_id, force=force)
    if not ok:
        console.print(f"  [red]Download failed for arXiv:{arxiv_id}[/red]")
        sys.exit(1)

    # Print post-download summary
    if storage.pdf_path.exists():
        console.print(f"  [green]PDF saved[/green]  {_fmt_bytes(storage.pdf_path.stat().st_size)}")
    if storage.html_index_path.exists():
        console.print(
            f"  [green]HTML version available[/green]  {_fmt_bytes(storage.html_index_path.stat().st_size)}"
        )
    else:
        console.print("  [yellow]No HTML version on arXiv — will use PDF text extraction[/yellow]")


def _do_extract(arxiv_id: str, model_tier: str) -> None:
    from backend.llm_extractor import run_extraction
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)

    # Describe text source
    if storage.html_index_path.exists():
        console.print(
            f"  Text source: [green]HTML[/green]  {_fmt_bytes(storage.html_index_path.stat().st_size)}"
        )
    elif storage.pdf_path.exists():
        console.print(
            f"  Text source: [yellow]PDF (no HTML)[/yellow]  {_fmt_bytes(storage.pdf_path.stat().st_size)}"
        )
    else:
        console.print("  [red]No downloaded content found — run without --skip-download[/red]")
        sys.exit(1)

    model_name = cfg.model_for_tier(model_tier)
    console.print(f"  Model: [cyan]{model_name}[/cyan]  (tier={model_tier})")

    ok = run_extraction(arxiv_id, model_tier=model_tier)
    if not ok:
        console.print(
            f"\n[red]Extraction failed.[/red]\n"
            f"  • Check that [cyan]{model_name}[/cyan] is available at your endpoint:\n"
            f"    [bold]uv run python scripts/list_models.py[/bold]\n"
            f"  • Try a different tier:  [bold]--model fallback[/bold]  or  [bold]--model small[/bold]\n"
            f"  • Check logs above for the full error message."
        )
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Process a single arXiv paper manually end-to-end")
    parser.add_argument("arxiv_id", help="arXiv ID, e.g. 2206.08164")
    parser.add_argument(
        "--model",
        "-m",
        default="primary",
        help="Model tier (primary/fallback/small) or explicit model name (default: primary)",
    )
    parser.add_argument("--skip-download", action="store_true", help="Skip download step")
    parser.add_argument("--skip-extract", action="store_true", help="Skip LLM extraction step")
    parser.add_argument("--force", action="store_true", help="Re-run even if already processed")
    args = parser.parse_args()

    arxiv_id = args.arxiv_id.strip().lstrip("arXiv:").split("v")[0]

    console.rule(f"[bold]Processing arXiv:{arxiv_id}[/bold]")

    # ── Download ──────────────────────────────────────────────────────────
    if not args.skip_download:
        console.print("\n[bold]1. Download[/bold]")
        _do_download(arxiv_id, force=args.force)
    else:
        console.print("\n[dim]1. Download — skipped[/dim]")

    # ── Extract ───────────────────────────────────────────────────────────
    if not args.skip_extract:
        console.print("\n[bold]2. LLM Extraction[/bold]")
        _do_extract(arxiv_id, model_tier=args.model)
        console.print("  [green]Extraction complete.[/green]")
    else:
        console.print("\n[dim]2. LLM Extraction — skipped[/dim]")

    # ── Parse ─────────────────────────────────────────────────────────────
    console.print("\n[bold]3. Parse results into DB[/bold]")
    from backend.results_parser import parse_and_store

    n = parse_and_store(arxiv_id)
    console.print(f"  [green]{n}[/green] result row(s) stored.")

    # ── Export ────────────────────────────────────────────────────────────
    console.print("\n[bold]4. Export to Hugo[/bold]")
    from backend.export_to_hugo import export_all

    export_all(arxiv_ids=[arxiv_id])

    console.rule("[green]Done[/green]")
    console.print("Preview: [bold]cd site && /snap/bin/hugo server[/bold]")


if __name__ == "__main__":
    main()
