"""Citation-based paper discovery using Google Scholar.

Finds papers that cite known benchmark papers (LRGB, GraphBench) and stores
them in the database for downstream downloading and extraction.

Usage::
    python -m backend.citation_finder --benchmark lrgb
    python -m backend.citation_finder --benchmark lrgb --benchmark graphbench
    python -m backend.citation_finder --all
"""

from __future__ import annotations

import argparse
import logging
import re
import time
from dataclasses import dataclass, field

from rich.console import Console
from tenacity import retry, stop_after_attempt, wait_exponential
from tqdm import tqdm

from backend.db import init_db, session_scope
from backend.models import Paper, PaperCandidate, PipelineRun

logger = logging.getLogger(__name__)
console = Console()

# ── Known benchmark papers ────────────────────────────────────────────────────
BENCHMARKS: dict[str, dict] = {
    "lrgb": {
        "arxiv_id": "2206.08164",
        "title": "Long Range Graph Benchmark",
        "discovery_source": "lrgb_citation",
    },
    "graphbench": {
        "arxiv_id": "2512.04475",
        "title": "GraphBench",
        "discovery_source": "graphbench_citation",
    },
}

ARXIV_ID_RE = re.compile(r"\b(\d{4}\.\d{4,5})(v\d+)?\b")


@dataclass
class DiscoveredPaper:
    title: str
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    arxiv_id: str | None = None
    url: str | None = None
    venue: str | None = None
    discovery_source: str = "unknown"


def _extract_arxiv_id(text: str) -> str | None:
    """Try to extract an arXiv ID from a URL or free-form text."""
    if not text:
        return None
    m = ARXIV_ID_RE.search(text)
    return m.group(1) if m else None


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=10, max=60),
    reraise=True,
)
def _fetch_citing_papers(benchmark_arxiv_id: str) -> list[DiscoveredPaper]:
    """Use scholarly to retrieve papers that cite the given arXiv paper."""
    try:
        from scholarly import scholarly as _scholarly  # type: ignore[import-untyped]
    except ImportError as exc:
        raise RuntimeError("scholarly is not installed. Run: uv add scholarly") from exc

    results: list[DiscoveredPaper] = []

    # Search for the benchmark paper itself first
    console.print(f"  [dim]Searching Google Scholar for arXiv:{benchmark_arxiv_id}…[/dim]")
    query = f"arxiv {benchmark_arxiv_id}"
    search_results = list(_scholarly.search_pubs(query))

    if not search_results:
        logger.warning("Could not find benchmark paper arXiv:%s on Scholar", benchmark_arxiv_id)
        return results

    benchmark_pub = search_results[0]

    # Fetch citing papers
    time.sleep(5)  # polite delay before citation crawl
    try:
        citing_gen = _scholarly.citedby(benchmark_pub)
        for pub in citing_gen:
            bib = pub.get("bib", {})
            title = bib.get("title", "").strip()
            if not title:
                continue

            # Try to detect arXiv ID from eprint, url, or abstract
            eprint = bib.get("eprint", "") or ""
            url = pub.get("pub_url", "") or ""
            arxiv_id = _extract_arxiv_id(eprint) or _extract_arxiv_id(url)

            authors_raw = bib.get("author", "")
            if isinstance(authors_raw, str):
                authors = [a.strip() for a in authors_raw.split(" and ") if a.strip()]
            else:
                authors = list(authors_raw)

            year_raw = bib.get("pub_year") or bib.get("year")
            try:
                year = int(year_raw) if year_raw else None
            except (ValueError, TypeError):
                year = None

            results.append(
                DiscoveredPaper(
                    title=title,
                    authors=authors,
                    year=year,
                    arxiv_id=arxiv_id,
                    url=url or None,
                    venue=bib.get("venue") or bib.get("journal") or None,
                )
            )
            time.sleep(2)  # be polite to Scholar
    except Exception as exc:
        logger.warning("Error crawling citations for %s: %s", benchmark_arxiv_id, exc)

    return results


def discover_citations(benchmark_keys: list[str]) -> list[DiscoveredPaper]:
    """Discover papers citing the given benchmarks and store new ones in the DB.

    Returns the list of newly inserted papers.
    """
    init_db()
    inserted: list[DiscoveredPaper] = []

    for key in benchmark_keys:
        bm = BENCHMARKS.get(key)
        if not bm:
            console.print(f"[red]Unknown benchmark key: {key}[/red]")
            continue

        console.print(
            f"\n[bold]Fetching citations for {bm['title']} (arXiv:{bm['arxiv_id']})[/bold]"
        )
        try:
            papers = _fetch_citing_papers(bm["arxiv_id"])
        except Exception as exc:
            console.print(f"[red]Failed to fetch citations: {exc}[/red]")
            continue

        console.print(f"  Found [cyan]{len(papers)}[/cyan] citing papers")
        discovery_detail = f"cited by {bm['title']} (arXiv:{bm['arxiv_id']})"

        new_count = dup_count = 0
        for disc in tqdm(papers, desc=f"  Storing {key} citations", unit="paper", leave=True):
            disc.discovery_source = bm["discovery_source"]
            tqdm.write(f"    → {disc.arxiv_id or '(no arXiv)':>15}  {disc.title[:70]!r}")
            status = _upsert_paper(disc, discovery_detail=discovery_detail)
            if status == "inserted":
                inserted.append(disc)
                new_count += 1
            else:
                dup_count += 1

        console.print(
            f"  [green]{new_count} new[/green] papers stored, "
            f"[dim]{dup_count} already known[/dim]"
        )

    return inserted


def _upsert_paper(disc: DiscoveredPaper, discovery_detail: str = "") -> str:
    """Insert a discovered paper if not already in the DB. Returns 'inserted' or 'duplicate'."""
    with session_scope() as session:
        # Deduplicate by arxiv_id (preferred) or exact title match
        existing = None
        if disc.arxiv_id:
            existing = session.query(Paper).filter_by(arxiv_id=disc.arxiv_id).first()
        if existing is None:
            existing = session.query(Paper).filter_by(title=disc.title).first()

        if existing is not None:
            # Record as duplicate in paper_candidates
            _upsert_candidate(
                disc, discovery_detail, final_status="duplicate", paper_id=existing.id
            )
            return "duplicate"

        paper = Paper(
            title=disc.title,
            arxiv_id=disc.arxiv_id,
            published_date=f"{disc.year}-01-01" if disc.year else None,
            venue=disc.venue,
            codebase_url=None,
            extraction_status="pending",
            discovery_source=disc.discovery_source,
            is_benchmark_paper=0,
        )
        paper.authors = disc.authors
        session.add(paper)

        run = PipelineRun(
            stage="discover",
            status="success",
            model_used=None,
        )
        session.add(run)
        # paper_id will be set after flush
        session.flush()
        run.paper_id = paper.id
        paper_id = paper.id

    _upsert_candidate(disc, discovery_detail, final_status="accepted", paper_id=paper_id)
    logger.info("Discovered paper: %s (arXiv:%s)", disc.title, disc.arxiv_id)
    return "inserted"


def _upsert_candidate(
    disc: DiscoveredPaper,
    discovery_detail: str,
    final_status: str,
    paper_id: int | None = None,
) -> None:
    """Create or update a PaperCandidate row for a citation-discovered paper."""
    with session_scope() as session:
        cand = None
        if disc.arxiv_id:
            cand = session.query(PaperCandidate).filter_by(arxiv_id=disc.arxiv_id).first()
        if cand is None and disc.title:
            cand = session.query(PaperCandidate).filter_by(title=disc.title).first()

        if cand is None:
            cand = PaperCandidate(
                arxiv_id=disc.arxiv_id,
                title=disc.title,
                published_date=f"{disc.year}-01-01" if disc.year else None,
                discovery_source=disc.discovery_source,
                discovery_detail=discovery_detail,
            )
            cand.authors = disc.authors
            session.add(cand)

        cand.final_status = final_status
        if paper_id is not None:
            cand.paper_id = paper_id


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Discover papers citing known benchmarks via Google Scholar"
    )
    group = p.add_mutually_exclusive_group()
    group.add_argument(
        "--benchmark",
        "-b",
        action="append",
        dest="benchmarks",
        choices=list(BENCHMARKS.keys()),
        metavar="NAME",
        help="Benchmark to crawl (may be repeated). Choices: " + ", ".join(BENCHMARKS),
    )
    group.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Crawl all configured benchmarks",
    )
    return p


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)

    keys = list(BENCHMARKS.keys()) if args.all else (args.benchmarks or list(BENCHMARKS.keys()))
    inserted = discover_citations(keys)
    console.print(f"\n[green]Done.[/green] Stored [bold]{len(inserted)}[/bold] new papers.")


if __name__ == "__main__":
    main()
