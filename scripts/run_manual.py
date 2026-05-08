#!/usr/bin/env python3
"""run_manual.py — process a single paper end-to-end.

Downloads the paper (PDF + HTML if available), runs two-stage LLM extraction,
parses results into the database, and re-exports the Hugo site.

Usage::
    uv run python scripts/run_manual.py 2206.08164
    uv run python scripts/run_manual.py 2206.08164 --model fallback
    uv run python scripts/run_manual.py 2206.08164 --force           # re-run extraction
    uv run python scripts/run_manual.py 2206.08164 --force-download  # re-download files
    uv run python scripts/run_manual.py 2206.08164 --skip-download
    uv run python scripts/run_manual.py 2206.08164 --skip-extract
    uv run python scripts/run_manual.py 2206.08164 --compare-models  # run all 3 tiers

Extraction is two-stage:
  Stage 1 (small model): screens title+abstract from arXiv API to confirm
    the paper has benchmark results before spending tokens on full extraction.
  Stage 2 (chosen model): sends the complete paper text to the LLM.

If a model is not found at the endpoint, run:
    uv run python scripts/list_models.py
to see what is available.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.table import Table

from backend.config import cfg
from backend.llm_extractor import fetch_arxiv_metadata, run_extraction

console = Console()

logging.basicConfig(level=logging.INFO, format="%(levelname)-8s %(message)s")


def _fmt_bytes(n: int) -> str:
    if n >= 1_048_576:
        return f"{n / 1_048_576:.1f} MB"
    if n >= 1_024:
        return f"{n / 1_024:.0f} KB"
    return f"{n} B"


# ── Download ──────────────────────────────────────────────────────────────────


def _do_download(arxiv_id: str, force: bool) -> None:
    from backend.arxiv_downloader import download_paper
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)

    if not force and storage.pdf_path.exists():
        size = storage.pdf_path.stat().st_size
        html_note = " + HTML" if storage.html_index_path.exists() else " (no HTML version)"
        console.print(
            f"  [dim]Already downloaded ({_fmt_bytes(size)}{html_note})"
            f" — use --force-download to re-download[/dim]"
        )
        return

    ok = download_paper(arxiv_id, force=force)
    if not ok:
        console.print(f"  [red]Download failed for arXiv:{arxiv_id}[/red]")
        sys.exit(1)

    storage = PaperStorage(arxiv_id)
    if storage.pdf_path.exists():
        console.print(f"  [green]PDF saved[/green]  {_fmt_bytes(storage.pdf_path.stat().st_size)}")
    if storage.html_index_path.exists():
        console.print(
            f"  [green]HTML version available[/green]"
            f"  {_fmt_bytes(storage.html_index_path.stat().st_size)}"
        )
    else:
        console.print("  [yellow]No HTML version on arXiv — will use PDF text extraction[/yellow]")


# ── Extraction ────────────────────────────────────────────────────────────────


def _show_existing_extraction(arxiv_id: str, requested_model: str) -> bool:
    """Print info about any existing extraction. Returns True if one exists."""
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)
    if not storage.llm_output_path.exists():
        return False
    try:
        with storage.llm_output_path.open() as f:
            data = json.load(f)
        existing_model = data.get("model_used", "unknown")
        extracted_at = (data.get("extracted_at") or "")[:10]
        n_results = len(data.get("results", {}).get("results", []))
        confidence = data.get("results", {}).get("extraction_confidence", "?")
        if existing_model == requested_model:
            console.print(
                f"  [dim]Already extracted with [cyan]{existing_model}[/cyan]"
                f" on {extracted_at} ({n_results} results, conf={confidence})"
                f" — use --force to re-run[/dim]"
            )
        else:
            console.print(
                f"  [yellow]Existing extraction:[/yellow] [cyan]{existing_model}[/cyan]"
                f" on {extracted_at} ({n_results} results, conf={confidence})"
            )
            console.print(
                f"  Requesting [cyan]{requested_model}[/cyan]"
                f" — use [bold]--force[/bold] to re-run with new model"
            )
        return True
    except Exception:
        return False


def _print_extraction_summary(path: Path) -> None:
    """Pretty-print results from an llm_output.json file."""
    if not path.exists():
        console.print("  [red]No output file found.[/red]")
        return
    try:
        with path.open() as f:
            data = json.load(f)
        results = data.get("results", {})
        rows = results.get("results", [])
        confidence = results.get("extraction_confidence", "?")
        proposed = results.get("proposed_model")
        baselines = results.get("baseline_models", [])
        notes = results.get("extraction_notes", "")

        console.print(
            f"  Confidence: [bold]{confidence}[/bold]  Results: {len(rows)}"
            + (f"  Proposed: [green]{proposed['name']}[/green]" if proposed else "")
        )
        if baselines:
            names = ", ".join(b["name"] for b in baselines[:8])
            console.print(f"  Baselines: {names}" + (" ..." if len(baselines) > 8 else ""))

        if rows:
            t = Table(show_header=True, header_style="bold", show_lines=False)
            t.add_column("Dataset", style="cyan", max_width=20)
            t.add_column("Model", max_width=25)
            t.add_column("Metric")
            t.add_column("Value", justify="right")
            t.add_column("Table")
            for r in rows[:25]:
                val = f"{r['value']:.4f}"
                if r.get("std"):
                    val += f" ±{r['std']:.4f}"
                t.add_row(
                    r.get("dataset", ""),
                    r.get("model", ""),
                    r.get("metric", ""),
                    val,
                    r.get("table_ref") or "",
                )
            if len(rows) > 25:
                console.print(f"  [dim](showing 25 of {len(rows)} rows)[/dim]")
            console.print(t)
        else:
            console.print("  [yellow]No result rows extracted.[/yellow]")
            if notes:
                console.print(f"  [dim]{notes[:400]}[/dim]")
    except Exception as exc:
        console.print(f"  [dim]Could not parse output: {exc}[/dim]")


def _do_extract(arxiv_id: str, model_tier: str, force: bool, screen: bool) -> bool:
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)
    model_name = cfg.model_for_tier(model_tier)

    # Describe text source
    if storage.html_index_path.exists():
        console.print(
            f"  Text source: [green]HTML[/green]"
            f"  {_fmt_bytes(storage.html_index_path.stat().st_size)}"
        )
    elif storage.pdf_path.exists():
        console.print(
            f"  Text source: [yellow]PDF (no HTML)[/yellow]"
            f"  {_fmt_bytes(storage.pdf_path.stat().st_size)}"
        )
    else:
        console.print("  [red]No downloaded content — run without --skip-download[/red]")
        sys.exit(1)

    # Check for existing extraction
    if not force and _show_existing_extraction(arxiv_id, model_name):
        return True  # use existing

    console.print(f"  Model: [cyan]{model_name}[/cyan]  (tier={model_tier})")
    if screen:
        console.print("  [dim]Stage 1: screening abstract via arXiv API...[/dim]")
    else:
        console.print("  [dim]Stage 1 screening skipped (--skip-screen)[/dim]")

    ok = run_extraction(arxiv_id, model_tier=model_tier, screen_first=screen)
    if not ok:
        console.print(
            f"\n[red]Extraction failed or stage-1 rejected.[/red]\n"
            f"  • Stage 1 may have determined no benchmark results in abstract\n"
            f"    → run with [bold]--skip-screen[/bold] to bypass\n"
            f"  • Or check that [cyan]{model_name}[/cyan] is available:\n"
            f"    [bold]uv run python scripts/list_models.py[/bold]\n"
            f"  • Try: [bold]--model fallback[/bold]  or  [bold]--model small[/bold]"
        )
        return False
    return True


# ── Compare-models helper ─────────────────────────────────────────────────────


def _run_for_tier(arxiv_id: str, model_tier: str, force: bool) -> None:
    """Extract with one model tier and save to a tier-specific file."""
    import shutil
    from backend.paper_storage import PaperStorage

    model_name = cfg.model_for_tier(model_tier)
    console.print(f"\n[bold]── {model_name} (tier={model_tier}) ──[/bold]")

    storage = PaperStorage(arxiv_id)
    tier_out = storage.llm_output_path.parent / f"llm_output_{model_tier}.json"

    if not force and tier_out.exists():
        console.print("  [dim]Cached — showing existing result[/dim]")
        _print_extraction_summary(tier_out)
        return

    ok = run_extraction(
        arxiv_id, model_tier=model_tier, screen_first=False, fallback_on_failure=False
    )

    # Copy main llm_output.json to tier-specific file so runs don't overwrite each other
    if ok and storage.llm_output_path.exists():
        shutil.copy2(storage.llm_output_path, tier_out)
        _print_extraction_summary(tier_out)
    else:
        console.print(f"  [red]Extraction failed for {model_name}[/red]")


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Process a single arXiv paper manually end-to-end",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "arxiv_id",
        help="arXiv ID (e.g. 2206.08164) or full URL (e.g. https://arxiv.org/abs/2206.08164)",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="primary",
        help="Model tier: primary/fallback/small (default: primary)",
    )
    parser.add_argument("--skip-download", action="store_true", help="Skip download step")
    parser.add_argument("--skip-extract", action="store_true", help="Skip LLM extraction step")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-run extraction even if results already exist (does NOT re-download)",
    )
    parser.add_argument(
        "--force-download",
        action="store_true",
        help="Re-download PDF/HTML even if already present (implies --force for extraction too)",
    )
    parser.add_argument(
        "--compare-models",
        action="store_true",
        help="Run extraction with all three tiers (primary/fallback/small) and compare results",
    )
    parser.add_argument(
        "--skip-screen",
        action="store_true",
        help="Skip stage 1 abstract screening and always run full extraction",
    )
    args = parser.parse_args()

    # Normalise: accept full arXiv URLs like https://arxiv.org/abs/2206.08164
    raw = args.arxiv_id.strip()
    m = re.match(r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", raw)
    if m:
        raw = m.group(1)
    arxiv_id = raw.lstrip("arXiv:").split("v")[0]
    force_extract = args.force or args.force_download
    force_download = args.force_download
    do_screen = not args.skip_screen

    console.rule(f"[bold]Processing arXiv:{arxiv_id}[/bold]")

    # ── Download ──────────────────────────────────────────────────────────
    if not args.skip_download:
        console.print("\n[bold]1. Download[/bold]")
        _do_download(arxiv_id, force=force_download)
    else:
        console.print("\n[dim]1. Download — skipped[/dim]")

    # ── Compare-models mode ───────────────────────────────────────────────
    if args.compare_models:
        console.rule("[bold]Comparing all 3 model tiers[/bold]")
        for tier in ("primary", "fallback", "small"):
            _run_for_tier(arxiv_id, tier, force=force_extract)
        console.rule("[green]Comparison done[/green]")
        return

    # ── Extract ───────────────────────────────────────────────────────────
    if not args.skip_extract:
        console.print("\n[bold]2. LLM Extraction[/bold]")
        ok = _do_extract(arxiv_id, model_tier=args.model, force=force_extract, screen=do_screen)
        if ok:
            console.print("  [green]Extraction complete.[/green]")
            from backend.paper_storage import PaperStorage

            _print_extraction_summary(PaperStorage(arxiv_id).llm_output_path)
        else:
            sys.exit(1)
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
