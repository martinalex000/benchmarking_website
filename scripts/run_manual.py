#!/usr/bin/env python3
"""run_manual.py — process a single paper end-to-end.

Downloads the paper (LaTeX source + PDF), runs two-stage LLM extraction,
parses results into the database, and re-exports the Hugo site.

Usage::
    uv run python scripts/run_manual.py 2206.08164
    uv run python scripts/run_manual.py 2206.08164 --model fallback
    uv run python scripts/run_manual.py 2206.08164 --force           # re-run extraction
    uv run python scripts/run_manual.py 2206.08164 --force-download  # re-download files
    uv run python scripts/run_manual.py 2206.08164 --skip-download
    uv run python scripts/run_manual.py 2206.08164 --skip-extract    uv run python scripts/run_manual.py 2206.08164 --oneshot   # legacy single-shot extraction    uv run python scripts/run_manual.py 2206.08164 --compare-models  # run all 3 tiers
    uv run python scripts/run_manual.py --import-pending            # review pending datasets

Extraction is two-stage:
  Stage 1 (small model): screens title+abstract from arXiv API to confirm
    the paper has benchmark results before spending tokens on full extraction.
  Stage 2 (chosen model): sends the complete paper text to the LLM.

Unknown datasets found during extraction are queued in the pending_datasets DB
table for later review. Use --import-pending to interactively add them to
seed_data.yaml and reseed the DB.

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
from backend.llm_model_options import extra_body_for_model
from backend.llm_extractor import fetch_arxiv_metadata, run_extraction, run_figure_detection

console = Console()

# Only show WARNING+ from backend modules; rich console handles all user-facing output.
logging.basicConfig(level=logging.WARNING, format="%(levelname)-8s %(message)s")


def _fmt_bytes(n: int) -> str:
    if n >= 1_048_576:
        return f"{n / 1_048_576:.1f} MB"
    if n >= 1_024:
        return f"{n / 1_024:.0f} KB"
    return f"{n} B"


# ── Download ──────────────────────────────────────────────────────────────────


def _is_paper_downloaded(arxiv_id: str) -> bool:
    """Return True if the paper already has local downloaded content."""
    from backend.paper_storage import PaperStorage

    s = PaperStorage(arxiv_id)
    return (
        s.pdf_path.exists() or s.html_index_path.exists() or (s.latex_dir / "expanded.tex").exists()
    )


def _record_candidate(
    arxiv_id: str,
    title: str,
    abstract: str,
    stage1_passed: int,
    stage1_confidence: float,
    stage1_reason: str,
    discovery_source: str = "manual",
) -> None:
    """Upsert a paper_candidates row so every paper run through screening is tracked."""
    from backend.db import session_scope as _ss
    from backend.models import PaperCandidate as _PC

    with _ss() as _s:
        cand = _s.query(_PC).filter_by(arxiv_id=arxiv_id).first()
        if cand is None:
            cand = _PC(
                arxiv_id=arxiv_id,
                title=title or f"arXiv:{arxiv_id}",
                abstract=abstract,
                discovery_source=discovery_source,
                discovery_detail="run_manual.py",
            )
            _s.add(cand)
        cand.stage1_passed = stage1_passed
        cand.stage1_confidence = stage1_confidence
        cand.stage1_reason = stage1_reason
        if stage1_passed == 0:
            cand.final_status = "rejected_stage1"
        elif stage1_passed == 1 and cand.final_status in (None, "rejected_stage1"):
            cand.final_status = "accepted"


def _pre_screen(arxiv_id: str) -> bool:
    """Fetch abstract from DB/local/arXiv API and run stage-1 screening.

    Returns True if the paper passes screening (or if screening cannot be run),
    False if the paper is rejected.  Prints status to console.

    Always writes a paper_candidates row so the result is visible in the dev page.
    """
    from backend.db import session_scope as _ss
    from backend.models import Paper as _Paper

    title = abstract = ""
    with _ss() as _s:
        p = _s.query(_Paper).filter_by(arxiv_id=arxiv_id).first()
        if p:
            title = p.title or ""
            abstract = p.abstract or ""

    if not abstract or title.startswith("arXiv:"):
        # Try local LaTeX cache before hitting the network
        from backend.paper_storage import PaperStorage

        storage = PaperStorage(arxiv_id)
        if storage.latex_dir.exists():
            try:
                from backend.llm_extractor import _extract_metadata_from_latex_cache

                meta = _extract_metadata_from_latex_cache(storage.latex_dir)
                if meta.get("title"):
                    title = meta["title"]
                if meta.get("abstract"):
                    abstract = meta["abstract"]
            except Exception:
                pass

    if not abstract or title.startswith("arXiv:"):
        console.print("  [dim]Fetching abstract from arXiv API for pre-screen…[/dim]")
        from backend.llm_extractor import fetch_arxiv_metadata

        meta = fetch_arxiv_metadata(arxiv_id)
        title = meta.get("title", title)
        abstract = meta.get("abstract", abstract)

    if not abstract:
        console.print(
            "  [yellow]Could not fetch abstract — skipping pre-screen, will download[/yellow]"
        )
        return True  # can't screen, proceed with download

    from backend.llm_extractor import LLMExtractor

    screener = LLMExtractor(model_tier="small")
    screen = screener.screen_paper(title, abstract)
    if screen.has_benchmark_results or screen.has_new_benchmark:
        datasets_str = ", ".join(screen.datasets_mentioned) if screen.datasets_mentioned else "—"
        console.print(
            f"  [green]Pre-screen PASS[/green] (conf={screen.confidence:.2f})"
            f" — datasets: {datasets_str}"
        )
        _record_candidate(
            arxiv_id,
            title,
            abstract,
            stage1_passed=1,
            stage1_confidence=screen.confidence,
            stage1_reason=screen.notes or "",
        )
        return True
    else:
        console.print(
            f"  [yellow]Pre-screen REJECT[/yellow] (conf={screen.confidence:.2f}):"
            f" no benchmark results detected in abstract.\n"
            f"  Notes: {screen.notes or 'none'}\n"
            f"  Use [bold]--skip-screen[/bold] to force download anyway."
        )
        _record_candidate(
            arxiv_id,
            title,
            abstract,
            stage1_passed=0,
            stage1_confidence=screen.confidence,
            stage1_reason=screen.notes or "",
        )
        return False


def _do_download(arxiv_id: str, force: bool) -> None:
    from backend.arxiv_downloader import download_paper
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)

    if not force and storage.pdf_path.exists():
        latex_note = ""
        expanded = storage.latex_dir / "expanded.tex"
        if expanded.exists():
            latex_note = f" + LaTeX ({_fmt_bytes(expanded.stat().st_size)})"
        console.print(
            f"  [dim]Already downloaded ({_fmt_bytes(storage.pdf_path.stat().st_size)}{latex_note})"
            f" — use --force-download to re-download[/dim]"
        )
        return

    ok = download_paper(arxiv_id, force=force)
    if not ok:
        console.print(f"  [red]Download failed for arXiv:{arxiv_id}[/red]")
        sys.exit(1)

    storage = PaperStorage(arxiv_id)
    expanded = storage.latex_dir / "expanded.tex"
    if expanded.exists():
        console.print(f"  [green]LaTeX[/green]  {_fmt_bytes(expanded.stat().st_size)}")
    else:
        console.print("  [yellow]No LaTeX source on arXiv — will use PDF text extraction[/yellow]")
    if storage.pdf_path.exists():
        console.print(f"  [green]PDF[/green]   {_fmt_bytes(storage.pdf_path.stat().st_size)}")


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
        fallback_model = cfg.model_for_tier("fallback")
        is_fallback = existing_model == fallback_model
        if existing_model == requested_model:
            console.print(
                f"  [dim]Already extracted with [cyan]{existing_model}[/cyan]"
                f" on {extracted_at} ({n_results} results, conf={confidence})"
                f" — use --force to re-run[/dim]"
            )
        elif is_fallback:
            console.print(
                f"  [green]Fallback results present:[/green] [cyan]{existing_model}[/cyan]"
                f" on {extracted_at} ({n_results} results, conf={confidence})"
            )
            console.print(
                "  [dim]Fallback results are protected — re-run with "
                "[bold]--model fallback[/bold] to replace them.[/dim]"
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


def _do_extract(
    arxiv_id: str, model_tier: str, force: bool, screen: bool, two_step: bool = True
) -> bool:
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)
    model_name = cfg.model_for_tier(model_tier)

    # Describe text source (LaTeX preferred, PDF fallback)
    expanded_tex = storage.latex_dir / "expanded.tex"
    has_latex = expanded_tex.exists() and expanded_tex.stat().st_size > 100
    if has_latex and storage.pdf_path.exists():
        console.print(
            f"  Source: [bold green]LaTeX[/bold green]  {_fmt_bytes(expanded_tex.stat().st_size)}"
            f"  +  PDF  {_fmt_bytes(storage.pdf_path.stat().st_size)}"
        )
    elif has_latex:
        console.print(
            f"  Source: [bold green]LaTeX[/bold green]  {_fmt_bytes(expanded_tex.stat().st_size)}"
        )
    elif storage.pdf_path.exists():
        console.print(
            f"  Source: [yellow]PDF[/yellow]  {_fmt_bytes(storage.pdf_path.stat().st_size)}"
            f"  [dim](no LaTeX source — may reduce extraction quality)[/dim]"
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
    if not two_step:
        console.print("  [dim]Mode: one-shot (--oneshot)[/dim]")

    ok = run_extraction(arxiv_id, model_tier=model_tier, screen_first=screen, two_step=two_step)
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

    # Show LaTeX source stats (from cache — instant)
    _show_latex_stats(arxiv_id)
    return True


# ── LaTeX stats helper ────────────────────────────────────────────────────────


def _show_latex_stats(arxiv_id: str) -> None:
    """Print LaTeX table/section counts from the cached expanded.tex."""
    from backend.paper_storage import PaperStorage as _PS

    storage = _PS(arxiv_id)
    expanded = storage.latex_dir / "expanded.tex"
    if not expanded.exists():
        return
    try:
        from backend.latex_source import download_and_parse as _latex_load

        lp = _latex_load(arxiv_id, storage.latex_dir)
        if lp:
            n_tables = len(lp.tables)
            n_appendix = sum(1 for t in lp.tables if t.in_appendix)
            n_exp = len(lp.experiment_sections)
            n_sections = len(lp.sections)
            console.print(
                f"  [dim]LaTeX: {n_tables} tables ({n_appendix} appendix),"
                f" {n_sections} sections, {n_exp} experiment section(s) in RAG[/dim]"
            )
    except Exception:
        pass


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


# ── New-dataset prompt ────────────────────────────────────────────────────────


_TASK_TYPES = [
    "graph_classification",
    "graph_regression",
    "node_classification",
    "node_regression",
    "link_prediction",
    "graph_generation",
]


def _llm_suggest_dataset(
    ds_name: str,
    metrics: set[str],
    paper_text: str,
) -> dict:
    """Call the LLM to auto-fill dataset metadata.

    Returns a dict with keys: task_type, primary_metric, higher_is_better,
    description, domain, pyg_class, pyg_url, benchmark_name.
    Returns {} on failure.
    """
    import json as _json
    import re as _re

    from openai import OpenAI

    prompt_path = Path(__file__).parent.parent / "config" / "prompts" / "dataset_autoseed.txt"
    if not prompt_path.exists():
        return {}
    system_prompt = prompt_path.read_text(encoding="utf-8").strip()

    metrics_str = ", ".join(sorted(metrics)) if metrics else "unknown"
    # Use first 8000 chars of paper text for context
    excerpt = paper_text[:8000] if paper_text else ""
    user_content = (
        f"Dataset name: {ds_name}\n"
        f"Metrics observed in results: {metrics_str}\n\n"
        f"Paper excerpt:\n{excerpt}"
    )

    try:
        model_name = cfg.model_for_tier("small")
        client = OpenAI(
            api_key=cfg.llm_api_key or "none",
            base_url=cfg.llm_endpoint or None,
            timeout=30,
        )
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            max_tokens=512,
            temperature=0.0,
            extra_body=extra_body_for_model(model_name),
        )
        raw = (response.choices[0].message.content or "").strip()
        # Strip markdown fences and thinking tags
        raw = _re.sub(r"<think>.*?</think>", "", raw, flags=_re.DOTALL).strip()
        raw = _re.sub(r"^```(?:json)?\s*", "", raw, flags=_re.MULTILINE)
        raw = _re.sub(r"\s*```$", "", raw, flags=_re.MULTILINE).strip()
        return _json.loads(raw)
    except Exception as exc:
        console.print(f"  [dim]LLM suggestion failed: {exc}[/dim]")
        return {}


def _collect_unknown_datasets(arxiv_id: str, paper_title: str = "") -> int:
    """Find unknown datasets in extraction and queue them in pending_datasets table.

    Runs entirely non-interactively. Unknown datasets are stored in the DB and
    can later be reviewed via --import-pending.

    Returns the number of newly queued DB rows.
    """
    from backend.db import init_db, session_scope
    from backend.models import PendingDataset
    from backend.paper_storage import PaperStorage
    from backend.results_parser import _load_variant_map, resolve_dataset_variant

    storage = PaperStorage(arxiv_id)
    if not storage.llm_output_path.exists():
        return 0

    raw = json.loads(storage.llm_output_path.read_text(encoding="utf-8"))
    result_entries = raw.get("results", {}).get("results", [])
    if not result_entries:
        return 0

    # Collect unique dataset names + their metrics
    seen: dict[str, set[str]] = {}
    for entry in result_entries:
        ds = (entry.get("dataset") or "").strip()
        metric = (entry.get("metric") or "").strip()
        if ds:
            seen.setdefault(ds, set()).add(metric)

    init_db()
    unknown: list[tuple[str, set[str]]] = []
    already_queued: set[tuple[str, str]] = set()
    with session_scope() as session:
        variant_map = _load_variant_map(session)
        for ds_name, metrics in seen.items():
            if resolve_dataset_variant(ds_name, session, variant_map) is None:
                unknown.append((ds_name, metrics))
        already_queued = {
            (row_arxiv_id, row_dataset_name)
            for row_arxiv_id, row_dataset_name in session.query(
                PendingDataset.arxiv_id,
                PendingDataset.dataset_name,
            ).filter(PendingDataset.arxiv_id == arxiv_id)
        }

    if not unknown:
        return 0

    # Load paper text for LLM context
    paper_text = ""
    if storage.text_path.exists():
        paper_text = storage.text_path.read_text(encoding="utf-8")

    candidates_to_add: list[dict] = []
    for ds_name, metrics in unknown:
        if (arxiv_id, ds_name) in already_queued:
            continue  # already tracked

        console.print(f"  [dim]LLM suggestion for '{ds_name}'...[/dim]", end="")
        suggestion = _llm_suggest_dataset(ds_name, metrics, paper_text)
        console.print(" [green]done[/green]" if suggestion else " [yellow]unavailable[/yellow]")

        metrics_seen = sorted(m for m in metrics if m)
        entry: dict = {
            "arxiv_id": arxiv_id,
            "paper_title": paper_title,
            "dataset_name": ds_name,
            "metrics_seen": metrics_seen,
            "suggestion": {
                "task_type": suggestion.get("task_type", "graph_classification"),
                "primary_metric": (
                    suggestion.get("primary_metric")
                    or (metrics_seen[0] if metrics_seen else "Accuracy")
                ),
                "higher_is_better": bool(suggestion.get("higher_is_better", True)),
                "description": suggestion.get("description", ""),
                "domain": suggestion.get("domain", ""),
                "pyg_class": suggestion.get("pyg_class", ""),
                "pyg_url": suggestion.get("pyg_url", ""),
                "benchmark_name": suggestion.get("benchmark_name", ""),
            },
            "status": "pending",
        }
        candidates_to_add.append(entry)
        already_queued.add((arxiv_id, ds_name))

    added = 0
    if candidates_to_add:
        with session_scope() as session:
            for entry in candidates_to_add:
                exists = (
                    session.query(PendingDataset.id)
                    .filter_by(
                        arxiv_id=entry["arxiv_id"],
                        dataset_name=entry["dataset_name"],
                    )
                    .first()
                )
                if exists is not None:
                    continue
                row = PendingDataset(
                    arxiv_id=entry["arxiv_id"],
                    paper_title=entry["paper_title"],
                    dataset_name=entry["dataset_name"],
                    status=entry["status"],
                )
                row.metrics_seen_list = entry["metrics_seen"]
                row.suggestion_obj = entry["suggestion"]
                session.add(row)
                added += 1

    if added:
        console.print(
            f"\n  [yellow]⚠  {len(unknown)} unknown dataset(s) found —"
            f" {added} new entr{'y' if added == 1 else 'ies'} queued in"
            " [bold]pending_datasets[/bold] (DB table)[/yellow]"
        )
        console.print(
            "  Results for unknown datasets are [dim]skipped during parsing[/dim].\n"
            "  Review and import with: "
            "[bold]uv run python scripts/run_manual.py --import-pending[/bold]"
        )
    elif unknown:
        console.print(
            f"  [dim]{len(unknown)} unknown dataset(s) already in pending_datasets — skipped.[/dim]"
        )

    return added


def _import_pending_datasets() -> None:
    """Interactively review pending_datasets DB rows and import approved entries."""
    import yaml
    from rich.table import Table as _RTable

    from backend.db import init_db, session_scope
    from backend.models import PendingDataset

    init_db()
    with session_scope() as session:
        pending = (
            session.query(PendingDataset)
            .filter(PendingDataset.status == "pending")
            .order_by(PendingDataset.created_at.asc(), PendingDataset.id.asc())
            .all()
        )

        if not pending:
            console.print("[green]No pending datasets to review.[/green]")
            return

        console.print(f"\n[bold]{len(pending)} pending dataset(s) to review:[/bold]\n")

        # Overview table
        overview = _RTable(show_header=True, header_style="bold", show_lines=True)
        overview.add_column("#", style="dim", width=3)
        overview.add_column("Dataset", style="cyan")
        overview.add_column("Paper (arXiv ID)", style="dim", max_width=45)
        overview.add_column("Metrics seen")
        overview.add_column("Suggested benchmark", style="green")
        for i, row in enumerate(pending, 1):
            overview.add_row(
                str(i),
                row.dataset_name or "",
                row.paper_title or row.arxiv_id or "",
                ", ".join(row.metrics_seen_list),
                row.suggestion_obj.get("benchmark_name", "?"),
            )
        console.print(overview)

        # Load seed_data.yaml
        seed_path = Path(__file__).parent.parent / "config" / "seed_data.yaml"
        with seed_path.open(encoding="utf-8") as f:
            seed_data = yaml.safe_load(f)
        benchmarks: list[dict] = seed_data.get("benchmarks", [])
        bm_names = [bm["name"] for bm in benchmarks]

        approved_datasets: list[str] = []
        approved_arxiv_ids: set[str] = set()

        for row in pending:
            ds_name = row.dataset_name or ""
            arxiv_id_e = row.arxiv_id or ""
            sug = row.suggestion_obj

            console.print(f"\n  [bold cyan]{ds_name}[/bold cyan]  [dim](arXiv:{arxiv_id_e})[/dim]")
            console.print(f"    task_type:        [cyan]{sug.get('task_type', '?')}[/cyan]")
            console.print(f"    primary_metric:   [cyan]{sug.get('primary_metric', '?')}[/cyan]")
            console.print(f"    higher_is_better: [cyan]{sug.get('higher_is_better', True)}[/cyan]")
            if sug.get("description"):
                console.print(f"    description:      [dim]{sug['description']}[/dim]")
            if sug.get("benchmark_name"):
                bm_marker = (
                    "[green](in DB)[/green]"
                    if sug["benchmark_name"] in bm_names
                    else "[yellow](new)[/yellow]"
                )
                console.print(
                    f"    benchmark:        [green]{sug['benchmark_name']}[/green] {bm_marker}"
                )
            if sug.get("pyg_url"):
                console.print(f"    pyg_url:          [dim]{sug['pyg_url']}[/dim]")

            ans = (
                console.input("  [a]pprove / [s]kip / [b]enchmark list? [a/s/b]: ").strip().lower()
            )
            if ans == "s":
                row.status = "skipped"
                continue

            # Determine benchmark assignment
            suggested_bm = sug.get("benchmark_name", "")
            if ans == "b" or (suggested_bm and suggested_bm not in bm_names and ans != "a"):
                # Show benchmark list
                console.print("  Benchmarks:")
                for i, name in enumerate(bm_names, 1):
                    console.print(f"    [{i}] {name}")
                console.print("    [N] Create new")
                bm_choice = console.input("  Choice: ").strip()
                bm_idx: int | None = None
                new_bm_name: str | None = None
                try:
                    idx = int(bm_choice) - 1
                    if 0 <= idx < len(bm_names):
                        bm_idx = idx
                except ValueError:
                    pass
                if bm_idx is None:
                    new_bm_name = console.input("  New benchmark name: ").strip()
                    if not new_bm_name:
                        console.print("  [yellow]Skipped.[/yellow]")
                        row.status = "skipped"
                        continue
            elif suggested_bm in bm_names:
                bm_idx = bm_names.index(suggested_bm)
                new_bm_name = None
            else:
                # Auto-create benchmark from suggestion
                bm_idx = None
                new_bm_name = suggested_bm or f"Paper {arxiv_id_e}"

            # Build dataset entry
            new_dataset: dict = {
                "name": ds_name,
                "task_type": sug.get("task_type", "graph_classification"),
                "primary_metric": sug.get("primary_metric", "Accuracy"),
                "higher_is_better": bool(sug.get("higher_is_better", True)),
                "variants": [{"name": "Standard split", "is_standard": True}],
            }
            if sug.get("description"):
                new_dataset["description"] = sug["description"]
            if sug.get("pyg_url"):
                new_dataset["pyg_url"] = sug["pyg_url"]
            if sug.get("domain"):
                new_dataset["domain"] = sug["domain"]

            if bm_idx is not None:
                benchmarks[bm_idx].setdefault("datasets", []).append(new_dataset)
            else:
                benchmarks.append(
                    {
                        "name": new_bm_name,
                        "arxiv_id": arxiv_id_e,
                        "url": f"https://arxiv.org/abs/{arxiv_id_e}",
                        "description": f"Benchmark introduced in arXiv:{arxiv_id_e}.",
                        "datasets": [new_dataset],
                    }
                )
                bm_names.append(new_bm_name)

            row.status = "approved"
            row.resolved_dataset_id = None
            approved_datasets.append(ds_name)
            if arxiv_id_e:
                approved_arxiv_ids.add(arxiv_id_e)
            console.print(f"  [green]✓ {ds_name} approved.[/green]")

    if not approved_datasets:
        console.print("[dim]No datasets approved.[/dim]")
        return

    # Write updated seed_data.yaml and reseed DB
    seed_data["benchmarks"] = benchmarks
    with seed_path.open("w", encoding="utf-8") as f:
        yaml.dump(seed_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    console.print(
        f"\n  [green]Wrote {len(approved_datasets)} dataset(s) to seed_data.yaml — seeding DB...[/green]"
    )
    init_db()
    from backend.seed_db import seed

    seed()
    console.print("  [green]DB seeded.[/green]")

    # Re-parse and re-export all affected papers
    affected = sorted(approved_arxiv_ids)
    if affected:
        console.print(f"\n  Re-parsing {len(affected)} paper(s) and exporting...")
        from backend.export_to_hugo import export_all
        from backend.results_parser import parse_and_store

        for aid in affected:
            n = parse_and_store(aid)
            console.print(f"    [dim]{aid}[/dim]: {n} result row(s) stored")
        export_all(arxiv_ids=affected)
        console.print("  [green]Export complete.[/green]")


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Process a single arXiv paper manually end-to-end",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "arxiv_id",
        nargs="?",
        help="arXiv ID (e.g. 2206.08164) or full URL — omit when using --import-pending",
    )
    parser.add_argument(
        "--import-pending",
        action="store_true",
        help="Interactively review and import datasets from the pending_datasets DB table",
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
        help="Re-download LaTeX/PDF even if already present (implies --force for extraction too)",
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
    parser.add_argument(
        "--force-rescreen",
        action="store_true",
        help="Re-screen even if the paper was previously rejected (overrides rejection guard)",
    )
    parser.add_argument(
        "--oneshot",
        action="store_true",
        help="Use legacy single-shot extraction (no dataset discovery step)",
    )
    parser.add_argument(
        "--figure-only",
        action="store_true",
        help="Re-run figure detection only (requires existing extraction); skips all other steps",
    )
    args = parser.parse_args()

    # ── Import-pending mode (no paper required) ───────────────────────────
    if args.import_pending:
        console.rule("[bold]Import Pending Datasets[/bold]")
        _import_pending_datasets()
        console.rule("[green]Done[/green]")
        return

    if not args.arxiv_id:
        parser.error("arxiv_id is required unless --import-pending is used")

    # Normalise: accept full arXiv URLs like https://arxiv.org/abs/2206.08164
    raw = args.arxiv_id.strip()
    m = re.match(r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", raw)
    if m:
        raw = m.group(1)
    arxiv_id = raw.lstrip("arXiv:").split("v")[0]
    force_extract = args.force or args.force_download
    force_download = args.force_download
    do_screen = not args.skip_screen
    do_two_step = not args.oneshot

    console.rule(f"[bold]Processing arXiv:{arxiv_id}[/bold]")

    # Ensure DB schema exists and seed benchmarks/datasets if the DB is fresh.
    from backend.db import init_db
    from backend.models import Benchmark, PaperCandidate
    from backend.db import session_scope as _ss

    init_db()
    with _ss() as _s:
        _needs_seed = _s.query(Benchmark).count() == 0
    if _needs_seed:
        console.print("  [dim]Fresh database — seeding benchmarks from seed_data.yaml...[/dim]")
        from backend.seed_db import seed as _seed

        _seed()

    # ── Rejection guard ───────────────────────────────────────────────────
    # If the paper was previously rejected by screening (and we're not forcing
    # a re-screen), abort early to avoid wasting LLM calls.
    if not args.force_rescreen and not args.skip_screen and not args.figure_only:
        with _ss() as _s:
            _cand = _s.query(PaperCandidate).filter_by(arxiv_id=arxiv_id).first()
            if _cand and _cand.final_status in ("rejected_stage1", "rejected_stage2"):
                stage = "stage 1" if _cand.final_status == "rejected_stage1" else "stage 2"
                reason = (_cand.stage1_reason or _cand.stage2_reason or "no reason recorded")[:200]
                console.print(
                    f"  [yellow]Previously rejected at {stage}[/yellow]: {reason}\n"
                    f"  Use [bold]--force-rescreen[/bold] to process anyway."
                )
                console.rule("[yellow]Skipped (previously rejected)[/yellow]")
                sys.exit(2)

    # Print title as early as possible — check DB first, then LaTeX cache.
    def _resolve_title() -> str:
        from backend.db import init_db, session_scope
        from backend.models import Paper
        from backend.paper_storage import PaperStorage

        init_db()
        with session_scope() as session:
            p = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
            if p and p.title and not p.title.startswith("arXiv:"):
                return p.title
        # Try LaTeX metadata cache
        s = PaperStorage(arxiv_id)
        if s.latex_dir.exists():
            try:
                from backend.llm_extractor import _extract_metadata_from_latex_cache

                meta = _extract_metadata_from_latex_cache(s.latex_dir)
                if meta.get("title"):
                    return meta["title"]
            except Exception:
                pass
        return ""

    paper_title = _resolve_title()
    if paper_title:
        console.print(f"  [bold magenta]{paper_title}[/bold magenta]")

    # ── Figure-only mode ──────────────────────────────────────────────────
    if args.figure_only:
        console.print("\n[bold]Figure detection[/bold]")
        model_name = cfg.model_for_tier(args.model)
        console.print(f"  Model: [cyan]{model_name}[/cyan]  (tier={args.model})")
        ok = run_figure_detection(arxiv_id, model_tier=args.model)
        if ok:
            console.print("  [green]Figure detection complete.[/green]")
            console.print("\n[bold]Exporting to Hugo[/bold]")
            from backend.export_to_hugo import export_all

            export_all(arxiv_ids=[arxiv_id])
        else:
            console.print("  [red]Figure detection failed.[/red]")
            sys.exit(1)
        console.rule("[green]Done[/green]")
        return

    # ── Download (with pre-screen for papers not yet local) ──────────────
    if not args.skip_download:
        console.print("\n[bold]1. Download[/bold]")
        already_downloaded = _is_paper_downloaded(arxiv_id)
        if already_downloaded:
            # Paper is already local — re-use it, no need to hit arxiv.
            _do_download(arxiv_id, force=force_download)
        elif do_screen:
            # Paper not yet local — screen the abstract BEFORE downloading.
            screen_passed = _pre_screen(arxiv_id)
            if screen_passed:
                _do_download(arxiv_id, force=force_download)
                # Abstract screening already done; skip it inside run_extraction.
                do_screen = False
            else:
                console.rule("[yellow]Rejected[/yellow]")
                sys.exit(2)
        else:
            # --skip-screen: download unconditionally.
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
        ok = _do_extract(
            arxiv_id,
            model_tier=args.model,
            force=force_extract,
            screen=do_screen,
            two_step=do_two_step,
        )
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

    # Collect unknown datasets non-interactively; user reviews later
    _collect_unknown_datasets(arxiv_id, paper_title)

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
