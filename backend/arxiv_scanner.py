"""ArXiv scanner — finds graph learning papers with benchmarking results.

Two-stage LLM filter:
  Stage 1 (cheap, small model):  Is this paper about graph learning?
  Stage 2 (primary model):       Does it report benchmark results or introduce a benchmark?

Papers passing both stages are stored in the database.

Usage::
    python -m backend.arxiv_scanner --days 7
    python -m backend.arxiv_scanner --days 14 --categories cs.LG cs.AI
    python -m backend.arxiv_scanner --days 3 --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

import arxiv  # type: ignore[import-untyped]
from openai import OpenAI
from rich.console import Console
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn, TimeElapsedColumn
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Paper, PipelineRun

logger = logging.getLogger(__name__)
console = Console()

DEFAULT_CATEGORIES = ["cs.LG", "cs.AI", "stat.ML", "cs.SI"]


@dataclass
class ScanResult:
    arxiv_id: str
    title: str
    authors: list[str] = field(default_factory=list)
    abstract: str = ""
    published: str = ""  # YYYY-MM-DD
    categories: list[str] = field(default_factory=list)
    # Stage results
    is_graph_learning: bool = False
    has_benchmark_results: bool = False
    has_new_benchmark: bool = False
    datasets_mentioned: list[str] = field(default_factory=list)
    stage1_confidence: float = 0.0
    stage2_confidence: float = 0.0


def _make_llm_client(model_tier: str = "small") -> tuple[OpenAI, str]:
    """Return (OpenAI client, model_name) for the given tier."""
    model_name = cfg.model_for_tier(model_tier)
    client = OpenAI(
        api_key=cfg.llm_api_key or "none",
        base_url=cfg.llm_endpoint or None,
        timeout=cfg.llm_timeout,
    )
    return client, model_name


def _read_prompt(filename: str) -> str:
    path = cfg.prompts_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=5, max=30), reraise=True)
def _call_llm(client: OpenAI, model: str, system_prompt: str, user_content: str) -> dict:
    """Call the LLM and parse JSON from the response."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        max_tokens=512,
        temperature=cfg.llm_temperature,
    )
    raw = response.choices[0].message.content or ""
    # Strip accidental markdown fences
    raw = raw.strip().lstrip("```json").lstrip("```").rstrip("```").strip()
    return json.loads(raw)


def stage1_relevance(result: ScanResult, client: OpenAI, model: str, prompt: str) -> bool:
    """Return True if the paper is about graph learning."""
    user_content = f"Title: {result.title}\n\nAbstract: {result.abstract}"
    try:
        parsed = _call_llm(client, model, prompt, user_content)
        result.is_graph_learning = bool(parsed.get("is_graph_learning", False))
        result.stage1_confidence = float(parsed.get("confidence", 0.0))
        return result.is_graph_learning
    except Exception as exc:
        logger.warning("Stage-1 LLM error for %s: %s", result.arxiv_id, exc)
        return False


def stage2_benchmark_check(result: ScanResult, client: OpenAI, model: str, prompt: str) -> bool:
    """Return True if the paper has benchmark results or a new benchmark."""
    user_content = f"Title: {result.title}\n\nAbstract: {result.abstract}"
    try:
        parsed = _call_llm(client, model, prompt, user_content)
        result.has_benchmark_results = bool(parsed.get("has_benchmark_results", False))
        result.has_new_benchmark = bool(parsed.get("has_new_benchmark", False))
        result.datasets_mentioned = parsed.get("datasets_mentioned", [])
        result.stage2_confidence = float(parsed.get("confidence", 0.0))
        return result.has_benchmark_results or result.has_new_benchmark
    except Exception as exc:
        logger.warning("Stage-2 LLM error for %s: %s", result.arxiv_id, exc)
        return False


def fetch_arxiv_papers(
    categories: list[str],
    days: int,
    max_results: int = 500,
) -> list[ScanResult]:
    """Fetch recent arXiv papers from the given categories."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    query = " OR ".join(f"cat:{c}" for c in categories)

    client_arxiv = arxiv.Client(page_size=100, delay_seconds=3)
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    results: list[ScanResult] = []
    for paper in client_arxiv.results(search):
        if paper.published and paper.published.replace(tzinfo=timezone.utc) < cutoff:
            break
        arxiv_id = paper.entry_id.split("/abs/")[-1].split("v")[0]
        results.append(
            ScanResult(
                arxiv_id=arxiv_id,
                title=paper.title.strip(),
                authors=[a.name for a in paper.authors],
                abstract=(paper.summary or "").strip(),
                published=paper.published.strftime("%Y-%m-%d") if paper.published else "",
                categories=paper.categories,
            )
        )
    return results


def scan(
    days: int = 7,
    categories: list[str] | None = None,
    dry_run: bool = False,
    max_results: int = 500,
) -> list[ScanResult]:
    """Run the full two-stage scan. Returns papers that passed both stages."""
    init_db()
    cats = categories or DEFAULT_CATEGORIES

    console.print(
        f"[bold]ArXiv scanner[/bold] — last [cyan]{days}[/cyan] days, categories: {', '.join(cats)}"
    )

    # Fetch from arXiv
    console.print("  Fetching papers from arXiv…")
    candidates = fetch_arxiv_papers(cats, days, max_results)
    console.print(f"  Retrieved [cyan]{len(candidates)}[/cyan] papers")

    # Filter out already-known papers
    with session_scope() as session:
        known_ids = {
            r[0] for r in session.query(Paper.arxiv_id).filter(Paper.arxiv_id.isnot(None)).all()
        }
    candidates = [c for c in candidates if c.arxiv_id not in known_ids]
    console.print(f"  [cyan]{len(candidates)}[/cyan] new (not yet in DB)")

    if not candidates:
        return []

    # Stage 1 — cheap relevance filter
    small_client, small_model = _make_llm_client("small")
    relevance_prompt = _read_prompt("graph_relevance.txt")

    stage1_pass: list[ScanResult] = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Stage 1: relevance filter", total=len(candidates))
        for res in candidates:
            if stage1_relevance(res, small_client, small_model, relevance_prompt):
                stage1_pass.append(res)
            progress.advance(task)
            time.sleep(0.5)  # gentle rate limiting

    console.print(f"  Stage 1 passed: [cyan]{len(stage1_pass)}[/cyan] / {len(candidates)}")

    # Stage 2 — benchmark check
    primary_client, primary_model = _make_llm_client("primary")
    benchmark_prompt = _read_prompt("benchmark_check.txt")

    stage2_pass: list[ScanResult] = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Stage 2: benchmark check", total=len(stage1_pass))
        for res in stage1_pass:
            if stage2_benchmark_check(res, primary_client, primary_model, benchmark_prompt):
                stage2_pass.append(res)
            progress.advance(task)
            time.sleep(1.0)

    console.print(f"  Stage 2 passed: [cyan]{len(stage2_pass)}[/cyan] / {len(stage1_pass)}")

    if not dry_run:
        _store_results(stage2_pass)

    return stage2_pass


def _store_results(results: list[ScanResult]) -> None:
    """Persist passing papers to the database."""
    for res in results:
        with session_scope() as session:
            existing = session.query(Paper).filter_by(arxiv_id=res.arxiv_id).first()
            if existing is not None:
                continue

            paper = Paper(
                arxiv_id=res.arxiv_id,
                title=res.title,
                abstract=res.abstract,
                published_date=res.published or None,
                extraction_status="pending",
                discovery_source="arxiv_scanner",
                is_benchmark_paper=1 if res.has_new_benchmark else 0,
            )
            paper.authors = res.authors
            session.add(paper)
            session.flush()

            run = PipelineRun(
                paper_id=paper.id,
                stage="discover",
                status="success",
                model_used=None,
            )
            session.add(run)

        logger.info(
            "Stored arXiv:%s — '%s' (datasets: %s)",
            res.arxiv_id,
            res.title[:60],
            ", ".join(res.datasets_mentioned) or "none",
        )


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Scan recent arXiv papers for graph learning benchmarks"
    )
    p.add_argument(
        "--days", type=int, default=7, help="Scan papers from the last N days (default: 7)"
    )
    p.add_argument(
        "--categories",
        nargs="+",
        default=DEFAULT_CATEGORIES,
        metavar="CAT",
        help="arXiv categories to scan (default: cs.LG cs.AI stat.ML cs.SI)",
    )
    p.add_argument(
        "--max-results", type=int, default=500, help="Max papers to fetch from arXiv API"
    )
    p.add_argument("--dry-run", action="store_true", help="Run filters but do not write to DB")
    # FUTURE: --update-versions flag (Phase 15)
    return p


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)

    passed = scan(
        days=args.days,
        categories=args.categories,
        dry_run=args.dry_run,
        max_results=args.max_results,
    )

    suffix = " [dim](dry run — not saved)[/dim]" if args.dry_run else ""
    console.print(
        f"\n[green]Done.[/green] [bold]{len(passed)}[/bold] papers queued for download.{suffix}"
    )


if __name__ == "__main__":
    main()
