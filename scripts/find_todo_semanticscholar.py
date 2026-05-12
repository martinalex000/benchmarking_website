#!/usr/bin/env python3
"""Crawl Semantic Scholar to seed `todo_papers` in the SQLite DB.

Always writes discoveries into the SQLite database (default: data/benchmarks.db).
Creates helper tables if missing: `s2_crawl_state`, `missing_papers`, `local_corpus`.

Rate limit: minimum 1s between Semantic Scholar requests.

API key is read from (in priority order):
  1. --s2-key CLI argument
  2. SEMANTIC_SCHOLAR_API_KEY env var (loaded from .env if present)
  3. S2_API_KEY env var

When --seed is omitted the script crawls ALL papers already in the `papers` table
that have not yet been fully crawled (i.e. not present in `s2_crawl_state`).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import requests
from rich.console import Console
from rich.table import Table

# Load .env from project root (silently skip if python-dotenv is not installed)
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
try:
    from dotenv import load_dotenv as _load_dotenv

    _load_dotenv(_PROJECT_ROOT / ".env", override=False)
except ImportError:
    pass

console = Console()

ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class S2Client:
    def __init__(self, api_key: str | None = None, min_delay: float = 1.0):
        self.sess = requests.Session()
        key = api_key or os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or os.environ.get("S2_API_KEY")
        if key:
            self.sess.headers["x-api-key"] = key
        self.min_delay = float(min_delay)
        self._last_request_at: float = 0.0

    def _wait(self) -> None:
        elapsed = time.time() - self._last_request_at
        if elapsed < self.min_delay:
            time.sleep(self.min_delay - elapsed)

    def _get(
        self, url: str, params: Dict[str, Any] | None = None, max_retries: int = 5
    ) -> Optional[requests.Response]:
        for attempt in range(max_retries):
            self._wait()
            try:
                resp = self.sess.get(url, params=params, timeout=30)
            except requests.RequestException as exc:
                console.print(f"[red]Request error: {exc} — retrying[/red]")
                time.sleep(2**attempt)
                continue

            self._last_request_at = time.time()
            if resp.status_code == 429:
                wait = (2**attempt) * 1.0
                console.print(f"[yellow]S2 rate limited (429). Backing off {wait}s[/yellow]")
                time.sleep(wait)
                continue
            if resp.status_code >= 400:
                console.print(f"[red]S2 HTTP {resp.status_code} for {url}[/red]")
                return None
            return resp
        return None

    def paper_id_for_arxiv(self, arxiv_id: str) -> Optional[str]:
        url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}"
        resp = self._get(url, {"fields": "paperId,title,externalIds"})
        if resp is None:
            return None
        data = resp.json()
        return data.get("paperId")

    def fetch_paginated(self, base_url: str, fields: str, limit: int) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        offset = 0
        page = min(limit, 500)
        while True:
            params = {"fields": fields, "limit": page, "offset": offset}
            resp = self._get(base_url, params)
            if resp is None:
                break
            data = resp.json()
            batch = data.get("data") or []
            for entry in batch:
                # citations endpoint wraps the paper under 'citingPaper'
                if "citingPaper" in entry:
                    results.append(entry.get("citingPaper") or {})
                else:
                    # references endpoint returns paper objects directly
                    results.append(entry.get("citedPaper") or entry.get("reference") or entry)

            if len(results) >= limit:
                return results[:limit]

            next_offset = data.get("next")
            if not next_offset or len(batch) == 0:
                break
            offset = next_offset
        return results

    def fetch_citations(self, paper_id: str, limit: int) -> List[Dict[str, Any]]:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations"
        return self.fetch_paginated(
            url, "paperId,title,authors,year,externalIds,publicationVenue,abstract,url", limit
        )

    def fetch_references(self, paper_id: str, limit: int) -> List[Dict[str, Any]]:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references"
        return self.fetch_paginated(
            url, "paperId,title,authors,year,externalIds,publicationVenue,abstract,url", limit
        )


def infer_arxiv_id_from_s2(paper: Dict[str, Any]) -> Optional[str]:
    # Try externalIds
    ext = paper.get("externalIds") or {}
    for k in ("ArXiv", "arXiv", "arxiv"):
        v = ext.get(k)
        if v:
            m = ARXIV_RE.search(str(v))
            if m:
                return m.group(1)

    # Try url
    for field in ("url", "publicationVenue", "title", "abstract"):
        txt = str(paper.get(field) or "")
        m = ARXIV_RE.search(txt)
        if m:
            return m.group(1)

    return None


def ensure_tables(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS s2_crawl_state (
            paper_id           TEXT PRIMARY KEY,
            arxiv_id           TEXT,
            seed_arxiv         TEXT,
            crawled_at         TEXT,
            citations_fetched  INTEGER NOT NULL DEFAULT 0,
            references_fetched INTEGER NOT NULL DEFAULT 0,
            citations_capped   INTEGER NOT NULL DEFAULT 0,
            references_capped  INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    # Migrate old s2_crawl_state that may lack the new columns
    cur.execute("PRAGMA table_info(s2_crawl_state)")
    crawl_cols = {r[1] for r in cur.fetchall()}
    for col, defn in [
        ("citations_fetched", "INTEGER NOT NULL DEFAULT 0"),
        ("references_fetched", "INTEGER NOT NULL DEFAULT 0"),
        ("citations_capped", "INTEGER NOT NULL DEFAULT 0"),
        ("references_capped", "INTEGER NOT NULL DEFAULT 0"),
    ]:
        if col not in crawl_cols:
            cur.execute(f"ALTER TABLE s2_crawl_state ADD COLUMN {col} {defn}")

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS missing_papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            observed_in TEXT,
            payload TEXT,
            first_seen_at TEXT
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS local_corpus (
            arxiv_id TEXT PRIMARY KEY,
            meta TEXT
        )
        """
    )
    # Ensure todo_papers has the extra columns added during development
    cur.execute("PRAGMA table_info(todo_papers)")
    todo_cols = {r[1] for r in cur.fetchall()}
    for col, defn in [
        ("seen_count", "INTEGER NOT NULL DEFAULT 0"),
        ("seen_from", "TEXT"),
        ("first_seen_at", "TEXT"),
    ]:
        if col not in todo_cols:
            cur.execute(f"ALTER TABLE todo_papers ADD COLUMN {col} {defn}")
    conn.commit()


def load_local_corpus_from_papers_table(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    # If papers table exists, copy arxiv_id into local_corpus
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='papers'")
    if cur.fetchone():
        console.print("Loading local corpus from existing `papers` table…")
        cur.execute("SELECT arxiv_id FROM papers WHERE arxiv_id IS NOT NULL")
        rows = cur.fetchall()
        for (aid,) in rows:
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO local_corpus(arxiv_id, meta) VALUES (?, ?)",
                    (aid, None),
                )
            except Exception:
                pass
        conn.commit()


def upsert_todo(conn: sqlite3.Connection, arxiv_id: str, title: str | None, seen_from: str) -> None:
    """Insert or update a todo_papers row, incrementing seen_count on each observation."""
    cur = conn.cursor()
    now = _utcnow_iso()
    cur.execute(
        "INSERT OR IGNORE INTO todo_papers"
        "(arxiv_id, title, reason, added_by, status, created_at, seen_count, seen_from, first_seen_at)"
        " VALUES (?, ?, 'semanticscholar', 'find_todo_s2', 'pending', ?, 0, ?, ?)",
        (arxiv_id, title or "", now, json.dumps([seen_from]), now),
    )
    # Fetch current state and increment
    cur.execute(
        "SELECT seen_count, seen_from, title FROM todo_papers WHERE arxiv_id = ?", (arxiv_id,)
    )
    row = cur.fetchone()
    if row:
        count = row[0] or 0
        seen_list: list[str] = []
        if row[1]:
            try:
                seen_list = json.loads(row[1])
            except Exception:
                seen_list = [row[1]]
        seen_list.append(seen_from)
        # Keep existing title if new one is absent; set title if row had none
        effective_title = title or row[2] or ""
        cur.execute(
            "UPDATE todo_papers SET seen_count = ?, seen_from = ?, title = COALESCE(NULLIF(?, ''), title)"
            " WHERE arxiv_id = ?",
            (count + 1, json.dumps(seen_list), effective_title, arxiv_id),
        )
    conn.commit()


def insert_missing(
    conn: sqlite3.Connection, title: str | None, observed_in: str, payload: Dict[str, Any]
) -> None:
    cur = conn.cursor()
    now = _utcnow_iso()
    cur.execute(
        "INSERT INTO missing_papers(title, observed_in, payload, first_seen_at) VALUES (?, ?, ?, ?)",
        (title or "", observed_in, json.dumps(payload, ensure_ascii=False), now),
    )
    conn.commit()


def mark_crawled(
    conn: sqlite3.Connection,
    paper_id: str,
    arxiv_id: str | None,
    seed_arxiv: str,
    citations_fetched: int = 0,
    references_fetched: int = 0,
    citations_capped: bool = False,
    references_capped: bool = False,
) -> None:
    """Record that we crawled paper_id and how many citations/references we fetched."""
    cur = conn.cursor()
    now = _utcnow_iso()
    cur.execute(
        "INSERT OR REPLACE INTO s2_crawl_state"
        "(paper_id, arxiv_id, seed_arxiv, crawled_at,"
        " citations_fetched, references_fetched, citations_capped, references_capped)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            paper_id,
            arxiv_id,
            seed_arxiv,
            now,
            citations_fetched,
            references_fetched,
            int(citations_capped),
            int(references_capped),
        ),
    )
    conn.commit()


def already_crawled(conn: sqlite3.Connection, paper_id: str) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM s2_crawl_state WHERE paper_id = ?", (paper_id,))
    return cur.fetchone() is not None


def get_uncrawled_seeds(conn: sqlite3.Connection) -> List[str]:
    """Return arxiv_ids from the papers table that have not yet been crawled."""
    cur = conn.cursor()
    # Check papers table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='papers'")
    if not cur.fetchone():
        return []
    cur.execute(
        """
        SELECT p.arxiv_id
        FROM papers p
        WHERE p.arxiv_id IS NOT NULL
          AND NOT EXISTS (
            SELECT 1 FROM s2_crawl_state cs WHERE cs.arxiv_id = p.arxiv_id
          )
        ORDER BY p.created_at
        """
    )
    return [r[0] for r in cur.fetchall()]


def is_in_local_corpus(conn: sqlite3.Connection, arxiv_id: str) -> bool:
    """Return True if the arxiv_id is already in the local corpus (papers table)."""
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM local_corpus WHERE arxiv_id = ?", (arxiv_id,))
    return cur.fetchone() is not None


def process_seed(
    s2: S2Client,
    conn: sqlite3.Connection,
    seed_arxiv: str,
    limit: int,
    force: bool,
) -> None:
    console.print(f"\n[bold]Processing seed {seed_arxiv} (limit={limit})[/bold]")
    pid = s2.paper_id_for_arxiv(seed_arxiv)
    if not pid:
        console.print(f"[red]Could not resolve seed arXiv:{seed_arxiv} on Semantic Scholar[/red]")
        return

    if not force and already_crawled(conn, pid):
        console.print(f"[dim]Seed paperId {pid} already crawled — skipping[/dim]")
        return

    # ── Citations (papers that cite this seed) ───────────────────────────
    citations = s2.fetch_citations(pid, limit)
    citations_capped = len(citations) >= limit
    console.print(
        f"  Citations: {len(citations)}"
        + (" [yellow](capped at limit)[/yellow]" if citations_capped else "")
    )
    cite_added = cite_missing = 0
    for c in citations:
        aid = infer_arxiv_id_from_s2(c)
        if aid:
            if not is_in_local_corpus(conn, aid):
                upsert_todo(conn, aid, c.get("title"), f"cited_by:{seed_arxiv}")
                cite_added += 1
        else:
            insert_missing(conn, c.get("title"), seed_arxiv, c)
            cite_missing += 1
    console.print(f"    → {cite_added} added to todo, {cite_missing} missing arXiv IDs")

    # ── References (papers this seed cites) ─────────────────────────────
    references = s2.fetch_references(pid, limit)
    references_capped = len(references) >= limit
    console.print(
        f"  References: {len(references)}"
        + (" [yellow](capped at limit)[/yellow]" if references_capped else "")
    )
    ref_added = ref_missing = 0
    for r in references:
        aid = infer_arxiv_id_from_s2(r)
        if aid:
            if not is_in_local_corpus(conn, aid):
                upsert_todo(conn, aid, r.get("title"), f"references_from:{seed_arxiv}")
                ref_added += 1
        else:
            insert_missing(conn, r.get("title"), seed_arxiv, r)
            ref_missing += 1
    console.print(f"    → {ref_added} added to todo, {ref_missing} missing arXiv IDs")

    mark_crawled(
        conn,
        pid,
        seed_arxiv,
        seed_arxiv,
        citations_fetched=len(citations),
        references_fetched=len(references),
        citations_capped=citations_capped,
        references_capped=references_capped,
    )


def top_report(conn: sqlite3.Connection, top_n: int = 20) -> None:
    cur = conn.cursor()
    cur.execute(
        "SELECT arxiv_id, title, seen_count FROM todo_papers ORDER BY seen_count DESC LIMIT ?",
        (top_n,),
    )
    rows = cur.fetchall()
    table = Table(show_header=True, header_style="bold")
    table.add_column("#", width=4)
    table.add_column("arXiv", style="cyan", width=14)
    table.add_column("seen_count", width=8)
    table.add_column("title")
    for i, (aid, title, cnt) in enumerate(rows, 1):
        table.add_row(str(i), aid or "", str(cnt or 0), title or "")
    console.print(table)


def main(argv: Iterable[str] | None = None) -> None:
    p = argparse.ArgumentParser(
        description="Seed todo_papers via Semantic Scholar crawl",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "When --seed is omitted, all papers already in the database are used as seeds\n"
            "(except those already crawled). The API key is read from SEMANTIC_SCHOLAR_API_KEY\n"
            "in the environment / .env file."
        ),
    )
    p.add_argument(
        "--seed",
        "-s",
        action="append",
        default=None,
        help="Seed arXiv ID (repeatable). Omit to crawl all DB papers.",
    )
    p.add_argument(
        "--limit",
        "-n",
        type=int,
        default=5000,
        help="Max citations/references fetched per seed (default: 5000)",
    )
    p.add_argument(
        "--db-path", default=None, help="Path to SQLite DB (defaults to data/benchmarks.db)"
    )
    p.add_argument(
        "--s2-key",
        default=None,
        help="Semantic Scholar API key (overrides SEMANTIC_SCHOLAR_API_KEY env var)",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Re-crawl seeds even if already recorded in s2_crawl_state",
    )
    p.add_argument("--top", type=int, default=20, help="Show top-N todo papers after run")
    args = p.parse_args(list(argv) if argv is not None else None)

    project_root = Path(__file__).resolve().parent.parent
    db_path = Path(args.db_path) if args.db_path else project_root / "data" / "benchmarks.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    s2 = S2Client(api_key=args.s2_key, min_delay=1.0)
    key_source = (
        "CLI --s2-key"
        if args.s2_key
        else (
            "SEMANTIC_SCHOLAR_API_KEY env"
            if os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
            else "S2_API_KEY env" if os.environ.get("S2_API_KEY") else "none (rate-limited)"
        )
    )
    console.print(f"API key source: [dim]{key_source}[/dim]")
    console.print(f"Using DB: [cyan]{db_path}[/cyan]")

    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")

    ensure_tables(conn)
    load_local_corpus_from_papers_table(conn)

    seeds = args.seed
    if not seeds:
        seeds = get_uncrawled_seeds(conn)
        if seeds:
            console.print(f"[dim]No --seed given: crawling {len(seeds)} uncrawled DB papers.[/dim]")
        else:
            console.print(
                "[yellow]No seeds given and no uncrawled papers in DB. Nothing to do.[/yellow]"
            )
            return

    for seed in seeds:
        process_seed(s2, conn, seed.strip(), args.limit, args.force)

    console.print("\n[green]Crawl complete.[/green]")
    top_report(conn, args.top)


if __name__ == "__main__":
    main()
