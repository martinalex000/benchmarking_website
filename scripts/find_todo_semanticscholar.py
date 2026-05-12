#!/usr/bin/env python3
"""Crawl Semantic Scholar to seed `todo_papers` in the SQLite DB.

Always writes discoveries into the SQLite database (default: data/benchmarks.db).
Creates helper tables if missing: `s2_crawl_state`, `missing_papers`, `local_corpus`.

Rate limit: minimum 1s between Semantic Scholar requests.
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
            paper_id TEXT PRIMARY KEY,
            arxiv_id TEXT,
            crawled_at TEXT,
            seed_arxiv TEXT
        )
        """
    )
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
    # Ensure todo_papers has seen_count and seen_from columns
    cur.execute("PRAGMA table_info(todo_papers)")
    cols = {r[1] for r in cur.fetchall()}
    if "seen_count" not in cols:
        cur.execute("ALTER TABLE todo_papers ADD COLUMN seen_count INTEGER NOT NULL DEFAULT 0")
    if "seen_from" not in cols:
        cur.execute("ALTER TABLE todo_papers ADD COLUMN seen_from TEXT")
    if "first_seen_at" not in cols:
        cur.execute("ALTER TABLE todo_papers ADD COLUMN first_seen_at TEXT")
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
    cur = conn.cursor()
    now = _utcnow_iso()
    # Insert if missing
    cur.execute(
        "INSERT OR IGNORE INTO todo_papers(arxiv_id, title, reason, added_by, status, created_at, seen_count, seen_from, first_seen_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            arxiv_id,
            title or "",
            "semanticscholar",
            "find_todo_s2",
            "pending",
            now,
            0,
            json.dumps([seen_from]),
            now,
        ),
    )
    # Increment seen_count and append seen_from
    cur.execute("SELECT seen_count, seen_from FROM todo_papers WHERE arxiv_id = ?", (arxiv_id,))
    row = cur.fetchone()
    if row:
        count = row[0] or 0
        seen_list = []
        if row[1]:
            try:
                seen_list = json.loads(row[1])
            except Exception:
                seen_list = [row[1]]
        seen_list.append(seen_from)
        cur.execute(
            "UPDATE todo_papers SET seen_count = ?, seen_from = ?, title = COALESCE(NULLIF(title, ''), ?), updated_at = ? WHERE arxiv_id = ?",
            (
                count + 1,
                json.dumps(seen_list),
                title or row[2] if len(row) > 2 else title or "",
                now,
                arxiv_id,
            ),
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
    conn: sqlite3.Connection, paper_id: str, arxiv_id: str | None, seed_arxiv: str
) -> None:
    cur = conn.cursor()
    now = _utcnow_iso()
    cur.execute(
        "INSERT OR REPLACE INTO s2_crawl_state(paper_id, arxiv_id, crawled_at, seed_arxiv) VALUES (?, ?, ?, ?)",
        (paper_id, arxiv_id, now, seed_arxiv),
    )
    conn.commit()


def already_crawled(conn: sqlite3.Connection, paper_id: str) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM s2_crawl_state WHERE paper_id = ?", (paper_id,))
    return cur.fetchone() is not None


def process_seed(
    s2: S2Client, conn: sqlite3.Connection, seed_arxiv: str, limit: int, force: bool
) -> None:
    console.print(f"\n[bold]Processing seed {seed_arxiv} (limit={limit})[/bold]")
    pid = s2.paper_id_for_arxiv(seed_arxiv)
    if not pid:
        console.print(f"[red]Could not resolve seed arXiv:{seed_arxiv} on Semantic Scholar[/red]")
        return

    # Crawl citations
    if not force and already_crawled(conn, pid):
        console.print(f"[dim]Seed paperId {pid} already crawled — skipping[/dim]")
        return

    citations = s2.fetch_citations(pid, limit)
    console.print(f"  Found {len(citations)} citations")
    for c in citations:
        aid = infer_arxiv_id_from_s2(c)
        if aid:
            upsert_todo(conn, aid, c.get("title"), f"cited_by:{seed_arxiv}")
        else:
            insert_missing(conn, c.get("title"), seed_arxiv, c)

    # Crawl references
    references = s2.fetch_references(pid, limit)
    console.print(f"  Found {len(references)} references")
    for r in references:
        aid = infer_arxiv_id_from_s2(r)
        if aid:
            upsert_todo(conn, aid, r.get("title"), f"references_from:{seed_arxiv}")
        else:
            insert_missing(conn, r.get("title"), seed_arxiv, r)

    mark_crawled(conn, pid, seed_arxiv, seed_arxiv)


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
    p = argparse.ArgumentParser(description="Seed todo_papers via Semantic Scholar crawl")
    p.add_argument(
        "--seed", "-s", action="append", required=True, help="Seed arXiv ID (repeatable)"
    )
    p.add_argument(
        "--limit", "-n", type=int, default=5000, help="Max papers per seed (default: 5000)"
    )
    p.add_argument(
        "--db-path", default=None, help="Path to SQLite DB (defaults to data/benchmarks.db)"
    )
    p.add_argument("--s2-key", default=None, help="Semantic Scholar API key")
    p.add_argument("--force", action="store_true", help="Re-crawl seeds even if already crawled")
    p.add_argument("--top", type=int, default=20, help="Show top-N after run")
    args = p.parse_args(list(argv) if argv is not None else None)

    project_root = Path(__file__).resolve().parent.parent
    db_path = Path(args.db_path) if args.db_path else project_root / "data" / "benchmarks.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    s2 = S2Client(api_key=args.s2_key, min_delay=1.0)

    console.print(f"Using DB: [cyan]{db_path}[/cyan]")
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")

    ensure_tables(conn)
    load_local_corpus_from_papers_table(conn)

    for seed in args.seed:
        process_seed(s2, conn, seed, args.limit, args.force)

    console.print("\n[green]Crawl complete.[/green]")
    top_report(conn, args.top)


if __name__ == "__main__":
    main()
