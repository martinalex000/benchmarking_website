#!/usr/bin/env python3
"""find_citing_papers.py — discover papers that cite a given dataset/benchmark paper.

Queries the Semantic Scholar API to find all papers that cite the given arXiv paper,
extracts their arXiv IDs, shows processing status vs our database, then lets you
interactively select which papers to process via run_manual.py.

Usage::
    uv run python scripts/find_citing_papers.py 2206.08164
    uv run python scripts/find_citing_papers.py 2206.08164 --limit 100
    uv run python scripts/find_citing_papers.py 2206.08164 --show-all
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent.parent))

import os

import requests
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

_S2_BASE = "https://api.semanticscholar.org/graph/v1"
_ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5})")


def _s2_session() -> requests.Session:
    """Build a requests session with optional API key from S2_API_KEY env var."""
    sess = requests.Session()
    key = os.environ.get("S2_API_KEY", "").strip()
    if key:
        sess.headers["x-api-key"] = key
    return sess


def _s2_get(
    sess: requests.Session, url: str, params: dict, *, max_retries: int = 5
) -> requests.Response | None:
    """GET with automatic retry/backoff on 429 rate-limit responses."""
    delay = 5
    for attempt in range(max_retries):
        resp = sess.get(url, params=params, timeout=30)
        if resp.status_code == 429:
            wait = delay * (2**attempt)
            console.print(f"[yellow]Rate limited — waiting {wait} s…[/yellow]")
            time.sleep(wait)
            continue
        return resp
    console.print("[red]Max retries exceeded after repeated 429 responses.[/red]")
    return None


# ── Semantic Scholar helpers ──────────────────────────────────────────────────


def _s2_paper_id(sess: requests.Session, arxiv_id: str) -> str | None:
    """Return the Semantic Scholar paperId for a given arXiv ID."""
    url = f"{_S2_BASE}/paper/arXiv:{arxiv_id}"
    resp = _s2_get(sess, url, {"fields": "paperId,title"})
    if resp is None:
        return None
    if resp.status_code == 200:
        return resp.json().get("paperId")
    console.print(f"[red]S2 lookup failed for arXiv:{arxiv_id}: HTTP {resp.status_code}[/red]")
    if resp.status_code == 404:
        console.print("  [dim]Tip: the paper may not yet be indexed by Semantic Scholar.[/dim]")
    return None


def _fetch_citations(sess: requests.Session, s2_id: str, limit: int) -> list[dict[str, Any]]:
    """Fetch all citing papers from Semantic Scholar (handles pagination)."""
    results: list[dict[str, Any]] = []
    fields = "paperId,title,authors,year,externalIds,publicationDate"
    offset = 0
    page_size = min(limit, 500)

    with console.status("[dim]Fetching citations from Semantic Scholar…[/dim]"):
        while True:
            url = f"{_S2_BASE}/paper/{s2_id}/citations"
            resp = _s2_get(
                sess,
                url,
                {"fields": fields, "limit": page_size, "offset": offset},
            )
            if resp is None or resp.status_code != 200:
                if resp is not None:
                    console.print(f"[red]Citations fetch failed: HTTP {resp.status_code}[/red]")
                break

            data = resp.json()
            batch = data.get("data", [])
            for entry in batch:
                citing = entry.get("citingPaper", {})
                results.append(citing)

            if len(results) >= limit:
                results = results[:limit]
                break

            next_offset = data.get("next")
            if next_offset is None or len(batch) == 0:
                break
            offset = next_offset
            time.sleep(1)  # be polite

    return results


def _extract_arxiv_id(paper: dict[str, Any]) -> str | None:
    """Extract arXiv ID from a Semantic Scholar paper dict."""
    ext = paper.get("externalIds") or {}
    arxiv_raw = ext.get("ArXiv") or ext.get("arxiv") or ""
    if arxiv_raw:
        m = _ARXIV_RE.search(arxiv_raw)
        if m:
            return m.group(1)
    return None


# ── DB status helpers ─────────────────────────────────────────────────────────


def _get_processed_ids() -> dict[str, str]:
    """Return {arxiv_id: extraction_status} for all papers in the DB."""
    from backend.db import init_db, session_scope
    from backend.models import Paper

    init_db()
    with session_scope() as session:
        rows = session.query(Paper.arxiv_id, Paper.extraction_status).all()
        return {r.arxiv_id: r.extraction_status for r in rows if r.arxiv_id}


def _has_local_extraction(arxiv_id: str) -> bool:
    """True if the paper has an llm_output.json on disk (even if not in DB yet)."""
    from backend.paper_storage import PaperStorage

    return PaperStorage(arxiv_id).llm_output_path.exists()


# ── Interactive selection ─────────────────────────────────────────────────────


def _pick_papers(candidates: list[dict]) -> list[str]:
    """Prompt the user to select papers to process. Returns list of arXiv IDs."""
    console.print(
        "\nEnter numbers to select (space/comma-separated), [bold]a[/bold] for all, or [bold]q[/bold] to quit:"
    )
    raw = input("> ").strip()
    if not raw or raw.lower() == "q":
        return []
    if raw.lower() == "a":
        return [c["arxiv_id"] for c in candidates]

    selected: list[str] = []
    for token in re.split(r"[\s,]+", raw):
        token = token.strip()
        if not token:
            continue
        try:
            idx = int(token) - 1
            if 0 <= idx < len(candidates):
                selected.append(candidates[idx]["arxiv_id"])
            else:
                console.print(f"[yellow]  Index {token} out of range — skipped[/yellow]")
        except ValueError:
            console.print(f"[yellow]  Not a number: {token!r} — skipped[/yellow]")
    return selected


def _run_paper(arxiv_id: str, run_manual_args: list[str]) -> None:
    """Call run_manual.py for the given arXiv ID."""
    cmd = [sys.executable, str(Path(__file__).parent / "run_manual.py"), arxiv_id]
    cmd += run_manual_args
    console.rule(f"[bold]Processing {arxiv_id}[/bold]")
    subprocess.run(cmd, check=False)


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find papers citing a benchmark paper, check status, and process them.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "arxiv_id",
        help="arXiv ID of the benchmark/dataset paper (e.g. 2206.08164)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Max number of citing papers to fetch (default: 200)",
    )
    parser.add_argument(
        "--show-all",
        action="store_true",
        help="Show all citing papers, including those without arXiv IDs",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="primary",
        help="Model tier to pass to run_manual (default: primary)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Pass --force to run_manual (re-run extraction)",
    )
    args = parser.parse_args()

    # Normalise arXiv ID
    raw = args.arxiv_id.strip()
    m = re.match(r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", raw)
    if m:
        raw = m.group(1)
    arxiv_id = raw.lstrip("arXiv:").split("v")[0]

    console.rule(f"[bold]Citations of arXiv:{arxiv_id}[/bold]")

    sess = _s2_session()

    # ── Step 1: Semantic Scholar lookup ──────────────────────────────────
    console.print("\n[bold]1. Looking up paper on Semantic Scholar…[/bold]")
    s2_id = _s2_paper_id(sess, arxiv_id)
    if not s2_id:
        console.print("[red]Could not find paper on Semantic Scholar. Aborting.[/red]")
        sys.exit(1)

    console.print(f"  Found S2 ID: [cyan]{s2_id}[/cyan]")

    key_hint = (
        ""
        if os.environ.get("S2_API_KEY")
        else " [dim](set S2_API_KEY env var for higher rate limits)[/dim]"
    )
    # ── Step 2: Fetch citations ───────────────────────────────────────────
    console.print(f"\n[bold]2. Fetching up to {args.limit} citing papers…[/bold]{key_hint}")
    citations = _fetch_citations(sess, s2_id, args.limit)
    console.print(f"  Retrieved [cyan]{len(citations)}[/cyan] citing papers.")

    # ── Step 3: Extract arXiv IDs & check DB ─────────────────────────────
    console.print("\n[bold]3. Checking processing status…[/bold]")
    processed = _get_processed_ids()

    arxiv_papers: list[dict] = []
    no_arxiv: list[dict] = []

    for paper in citations:
        aid = _extract_arxiv_id(paper)
        if aid:
            has_extraction = _has_local_extraction(aid)
            db_status = processed.get(aid)

            if db_status:
                status = db_status  # "done", "pending", "failed", etc.
            elif has_extraction:
                status = "extracted (not in DB)"
            else:
                status = "new"

            arxiv_papers.append(
                {
                    "arxiv_id": aid,
                    "title": paper.get("title") or "",
                    "year": paper.get("year") or "",
                    "status": status,
                }
            )
        else:
            no_arxiv.append(paper)

    # Sort: new first, then by year desc
    def _sort_key(p: dict) -> tuple:
        is_new = p["status"] == "new"
        year = p.get("year") or 0
        return (0 if is_new else 1, -int(year) if year else 0)

    arxiv_papers.sort(key=_sort_key)

    # ── Step 4: Display table ─────────────────────────────────────────────
    new_count = sum(1 for p in arxiv_papers if p["status"] == "new")
    done_count = sum(1 for p in arxiv_papers if p["status"] in ("done", "extracted (not in DB)"))

    console.print(
        f"\n  [green]{len(arxiv_papers)}[/green] with arXiv IDs  "
        f"([yellow]{new_count}[/yellow] new, "
        f"[green]{done_count}[/green] already processed, "
        f"[dim]{len(no_arxiv)}[/dim] without arXiv ID)"
    )

    table = Table(show_header=True, header_style="bold", box=box.SIMPLE, show_edge=False)
    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("arXiv ID", style="cyan", width=13)
    table.add_column("Year", width=6)
    table.add_column("Status", width=24)
    table.add_column("Title")

    candidates: list[dict] = []  # only unprocessed papers get a number
    all_rows = arxiv_papers

    for paper in all_rows:
        status = paper["status"]
        is_done = status in ("done", "extracted (not in DB)")

        # Assign sequential index only to unprocessed papers
        if not is_done:
            candidates.append(paper)
            num = str(len(candidates))
        else:
            num = "–"

        if status == "new":
            status_str = "[bold green]new[/bold green]"
        elif status == "done":
            status_str = "[dim]done[/dim]"
        elif status == "extracted (not in DB)":
            status_str = "[yellow]extracted (not in DB)[/yellow]"
        elif status == "failed":
            status_str = "[red]failed[/red]"
        elif status == "pending":
            status_str = "[yellow]pending[/yellow]"
        else:
            status_str = f"[dim]{status}[/dim]"

        title = paper["title"]
        if len(title) > 72:
            title = title[:69] + "…"

        table.add_row(num, paper["arxiv_id"], str(paper["year"]), status_str, title)

    console.print(table)

    if args.show_all and no_arxiv:
        console.print(f"\n[dim]Papers without arXiv IDs ({len(no_arxiv)}):[/dim]")
        for p in no_arxiv[:20]:
            console.print(f"  [dim]• {(p.get('title') or 'untitled')[:80]}[/dim]")
        if len(no_arxiv) > 20:
            console.print(f"  [dim]… and {len(no_arxiv) - 20} more[/dim]")

    if not candidates:
        console.print("[green]All arXiv-indexed citing papers are already processed.[/green]")
        return

    # ── Step 5: Interactive selection ────────────────────────────────────
    console.print(
        f"\n[bold]{len(candidates)}[/bold] unprocessed paper(s) available."
        f" Enter indices to process (e.g. [bold]1 3 5[/bold]), "
        f"[bold]a[/bold] for all, or [bold]q[/bold] to quit:"
    )
    selected_ids = _pick_papers(candidates)

    if not selected_ids:
        console.print("[dim]No papers selected. Exiting.[/dim]")
        return

    # ── Step 6: Process selected papers ──────────────────────────────────
    run_args: list[str] = ["--model", args.model]
    if args.force:
        run_args.append("--force")

    for i, aid in enumerate(selected_ids, 1):
        console.print(f"\n[dim]({i}/{len(selected_ids)})[/dim]")
        _run_paper(aid, run_args)

    console.rule("[green]All selected papers processed[/green]")


if __name__ == "__main__":
    main()
