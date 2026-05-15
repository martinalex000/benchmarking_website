"""Main pipeline CLI.

Subcommands:
  discover   – find new papers via citation and/or ArXiv scanner
  download   – download HTML + PDF for pending papers
  extract    – run LLM extraction on downloaded papers
  parse      – store LLM output as DB records
  aggregate  – (re-)compute baseline aggregation stats
  export     – write Hugo content files from DB
  build      – run `hugo` to produce site/public/
  run-all    – run all stages end-to-end

Usage examples::

    python -m backend.pipeline discover --all
    python -m backend.pipeline download
    python -m backend.pipeline extract --model primary
    python -m backend.pipeline extract --model fallback --paper 2206.08164
    python -m backend.pipeline run-all --since 7d
    python -m backend.pipeline run-all --force
"""

from __future__ import annotations

import argparse
import logging
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Paper
from backend.pipeline_state import record_run, should_process

console = Console()
logger = logging.getLogger(__name__)

HUGO_BIN = (
    str(cfg.base_dir / "bin" / "hugo") if (cfg.base_dir / "bin" / "hugo").exists() else "hugo"
)


# ── Helpers ───────────────────────────────────────────────────────────────────


def _get_papers(
    arxiv_ids: list[str] | None = None,
    status_filter: str | None = None,
    since: timedelta | None = None,
) -> list[Paper]:
    """Load papers from DB, optionally filtered."""
    with session_scope() as session:
        q = session.query(Paper)
        if arxiv_ids:
            q = q.filter(Paper.arxiv_id.in_(arxiv_ids))
        if status_filter:
            q = q.filter_by(extraction_status=status_filter)
        if since:
            cutoff = datetime.now(timezone.utc) - since
            q = q.filter(Paper.created_at >= cutoff)
        return q.all()


def _parse_since(value: str | None) -> timedelta | None:
    if value is None:
        return None
    value = value.strip().lower()
    if value.endswith("d"):
        return timedelta(days=int(value[:-1]))
    if value.endswith("h"):
        return timedelta(hours=int(value[:-1]))
    return timedelta(days=int(value))


# ── Stage runners ─────────────────────────────────────────────────────────────


def stage_discover(args: argparse.Namespace) -> None:
    console.print("[bold]Discover[/bold] — finding new papers…")
    tasks: list[str] = []

    if args.citations or args.all:
        tasks.append("citations")
    if args.arxiv or args.all:
        tasks.append("arxiv")

    if not tasks:
        console.print("[yellow]Specify --citations, --arxiv, or --all[/yellow]")
        return

    if "citations" in tasks:
        from backend.citation_finder import discover_citations

        benchmarks = args.benchmark or ["lrgb", "graphbench"]
        console.print(f"  Citation search for benchmarks: {benchmarks}")
        discover_citations(benchmarks)

    if "arxiv" in tasks:
        from backend.arxiv_scanner import scan

        days = getattr(args, "days", 7)
        dry_run = getattr(args, "dry_run", False)
        console.print(f"  ArXiv scan: last {days} days (dry_run={dry_run})")
        scan(days=days, dry_run=dry_run)


def stage_download(args: argparse.Namespace) -> None:
    from backend.arxiv_downloader import download_paper
    from backend.llm_extractor import LLMExtractor, fetch_arxiv_metadata
    from backend.paper_storage import PaperStorage
    from tqdm import tqdm

    force = getattr(args, "force", False)
    arxiv_ids = getattr(args, "paper", None)
    screen_first = not getattr(args, "skip_screen", False)
    papers = _get_papers(arxiv_ids=arxiv_ids, status_filter="pending" if not arxiv_ids else None)

    console.print(f"[bold]Download[/bold] — {len(papers)} paper(s) to process")
    if not papers:
        console.print("  Nothing to download.")
        return

    ok = fail = skip = rejected = 0
    screener = LLMExtractor(model_tier="small") if screen_first else None

    for p in tqdm(papers, desc="Downloading", unit="paper", leave=True):
        if not should_process(p.id, "download", force=force):
            tqdm.write(f"  skip  {p.arxiv_id}  (already downloaded)")
            skip += 1
            continue
        try:
            storage = PaperStorage(p.arxiv_id)
            already_local = (
                storage.pdf_path.exists()
                or storage.html_index_path.exists()
                or (storage.latex_dir / "expanded.tex").exists()
            )

            # Screen abstract BEFORE downloading if paper is not yet local.
            if screen_first and not already_local:
                title = p.title or ""
                abstract = p.abstract or ""
                if not abstract or title.startswith("arXiv:"):
                    meta = fetch_arxiv_metadata(p.arxiv_id)
                    title = meta.get("title", title)
                    abstract = meta.get("abstract", abstract)
                if abstract:
                    screen = screener.screen_paper(title, abstract)
                    if not screen.has_benchmark_results and not screen.has_new_benchmark:
                        tqdm.write(
                            f"  ✗  {p.arxiv_id}  REJECTED by pre-screen"
                            f" (conf={screen.confidence:.2f})"
                        )
                        record_run(p.id, "download", "rejected")
                        rejected += 1
                        continue

            result = download_paper(p.arxiv_id, force=force)
            status = "success" if result else "failed"
        except Exception as exc:
            logger.error("Download failed for %s: %s", p.arxiv_id, exc)
            status = "failed"
        record_run(p.id, "download", status)
        if status == "success":
            tqdm.write(f"  ✓  {p.arxiv_id}  {p.title[:70]!r}")
            ok += 1
        else:
            tqdm.write(f"  ✗  {p.arxiv_id}  FAILED")
            fail += 1

    console.print(
        f"  Done — [green]{ok} ok[/green], [red]{fail} failed[/red],"
        f" [yellow]{rejected} rejected[/yellow], [dim]{skip} skipped[/dim]"
    )


def stage_extract(args: argparse.Namespace) -> None:
    from backend.llm_extractor import run_extraction
    from tqdm import tqdm

    model_tier = getattr(args, "model", "primary")
    force = getattr(args, "force", False)
    arxiv_ids = getattr(args, "paper", None)
    papers = _get_papers(arxiv_ids=arxiv_ids, status_filter="downloaded" if not arxiv_ids else None)

    model_name = cfg.model_for_tier(model_tier)
    console.print(f"[bold]Extract[/bold] — {len(papers)} paper(s), model=[cyan]{model_name}[/cyan]")
    if not papers:
        console.print("  Nothing to extract.")
        return

    ok = fail = skip = 0
    for p in tqdm(papers, desc="Extracting", unit="paper", leave=True):
        if not should_process(p.id, "extract", force=force):
            tqdm.write(f"  skip  {p.arxiv_id}  (already extracted)")
            skip += 1
            continue
        try:
            result = run_extraction(p.arxiv_id, model_tier=model_tier, verbose=False)
            status = "success" if result else "failed"
        except Exception as exc:
            logger.error("Extraction failed for %s: %s", p.arxiv_id, exc)
            status = "failed"
        record_run(p.id, "extract", status, model_used=model_name)
        if status == "success":
            tqdm.write(f"  ✓  {p.arxiv_id}  {p.title[:70]!r}")
            ok += 1
        else:
            tqdm.write(f"  ✗  {p.arxiv_id}  FAILED")
            fail += 1

    console.print(
        f"  Done — [green]{ok} ok[/green], [red]{fail} failed[/red], [dim]{skip} skipped[/dim]"
    )


def stage_parse(args: argparse.Namespace) -> None:
    from backend.results_parser import parse_and_store
    from tqdm import tqdm

    force = getattr(args, "force", False)
    arxiv_ids = getattr(args, "paper", None)
    papers = _get_papers(arxiv_ids=arxiv_ids, status_filter="extracted" if not arxiv_ids else None)

    console.print(f"[bold]Parse[/bold] — {len(papers)} paper(s)")
    if not papers:
        console.print("  Nothing to parse.")
        return

    ok = fail = skip = 0
    for p in tqdm(papers, desc="Parsing", unit="paper", leave=True):
        if not should_process(p.id, "parse", force=force):
            tqdm.write(f"  skip  {p.arxiv_id}  (already parsed)")
            skip += 1
            continue
        try:
            n = parse_and_store(p.arxiv_id)
            status = "success"
            tqdm.write(f"  ✓  {p.arxiv_id}  {n} results stored  {p.title[:55]!r}")
        except Exception as exc:
            logger.error("Parse failed for %s: %s", p.arxiv_id, exc)
            status = "failed"
            n = 0
            tqdm.write(f"  ✗  {p.arxiv_id}  FAILED: {exc}")
        record_run(p.id, "parse", status)
        if status == "success":
            ok += 1
        else:
            fail += 1

    console.print(
        f"  Done — [green]{ok} ok[/green], [red]{fail} failed[/red], [dim]{skip} skipped[/dim]"
    )


def stage_export(args: argparse.Namespace) -> None:
    from backend.export_to_hugo import export_all

    arxiv_ids = getattr(args, "paper", None)
    n = f"for {len(arxiv_ids)} paper(s)" if arxiv_ids else "all papers + datasets"
    console.print(f"[bold]Export[/bold] — writing Hugo content files ({n})")
    export_all(arxiv_ids=arxiv_ids)


def stage_build(_args: argparse.Namespace) -> None:
    site_dir = cfg.base_dir / "site"
    console.print(f"[bold]Build[/bold] — running Hugo in {site_dir}")
    result = subprocess.run(
        [HUGO_BIN, "--minify"],
        cwd=str(site_dir),
        capture_output=False,
    )
    if result.returncode != 0:
        console.print("[red]Hugo build failed[/red]")
        sys.exit(1)
    console.print("[green]Hugo build complete → site/public/[/green]")


def stage_run_all(args: argparse.Namespace) -> None:
    """Run the full pipeline end-to-end."""
    since = _parse_since(getattr(args, "since", None))

    console.rule("[bold]Pipeline: run-all[/bold]")
    stage_discover(args)
    stage_download(args)
    stage_extract(args)
    stage_parse(args)
    stage_export(args)
    stage_build(args)
    console.rule("[green]Done[/green]")


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python -m backend.pipeline",
        description="Graph benchmark website pipeline",
    )
    p.add_argument("--verbose", "-v", action="store_true", help="Debug logging")

    sub = p.add_subparsers(dest="command", required=True)

    # discover
    d = sub.add_parser("discover", help="Find new papers")
    d.add_argument("--citations", action="store_true")
    d.add_argument("--arxiv", action="store_true")
    d.add_argument("--all", action="store_true")
    d.add_argument("--benchmark", nargs="+", default=["lrgb", "graphbench"])
    d.add_argument("--days", type=int, default=7)
    d.add_argument("--dry-run", action="store_true")

    # download
    dl = sub.add_parser("download", help="Download papers")
    dl.add_argument("--paper", nargs="+", metavar="ARXIV_ID")
    dl.add_argument("--force", action="store_true")
    dl.add_argument(
        "--skip-screen",
        action="store_true",
        help="Skip abstract pre-screen and download all papers unconditionally",
    )

    # extract
    ex = sub.add_parser("extract", help="Run LLM extraction")
    ex.add_argument(
        "--model", "-m", default="primary", help="Model tier (primary/fallback/small) or model name"
    )
    ex.add_argument("--paper", nargs="+", metavar="ARXIV_ID")
    ex.add_argument("--force", action="store_true")

    # parse
    ps = sub.add_parser("parse", help="Store LLM output as DB records")
    ps.add_argument("--paper", nargs="+", metavar="ARXIV_ID")
    ps.add_argument("--force", action="store_true")

    # aggregate (alias for parse + export)
    sub.add_parser("aggregate", help="Recompute aggregates and re-export")

    # export
    ex2 = sub.add_parser("export", help="Write Hugo content files")
    ex2.add_argument("--paper", nargs="+", metavar="ARXIV_ID")

    # build
    sub.add_parser("build", help="Run Hugo static site generator")

    # run-all
    ra = sub.add_parser("run-all", help="Full end-to-end pipeline")
    ra.add_argument(
        "--since",
        metavar="DURATION",
        help="Only process papers added within this window (e.g. 7d, 24h)",
    )
    ra.add_argument("--force", action="store_true", help="Re-process already completed stages")
    ra.add_argument("--model", "-m", default="primary")
    ra.add_argument("--paper", nargs="+", metavar="ARXIV_ID")
    ra.add_argument("--citations", action="store_true")
    ra.add_argument("--arxiv", action="store_true")
    ra.add_argument("--all", action="store_true", dest="all", default=True)
    ra.add_argument("--days", type=int, default=7)
    ra.add_argument("--dry-run", action="store_true")

    return p


def main(argv: list[str] | None = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s %(name)s %(message)s")

    init_db()

    dispatch = {
        "discover": stage_discover,
        "download": stage_download,
        "extract": stage_extract,
        "parse": stage_parse,
        "aggregate": lambda a: (stage_parse(a), stage_export(a)),
        "export": stage_export,
        "build": stage_build,
        "run-all": stage_run_all,
    }
    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        console.print(f"[red]Unknown command: {args.command}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
