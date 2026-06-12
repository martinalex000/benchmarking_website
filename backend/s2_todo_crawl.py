"""Semantic Scholar helpers for seeding and maintaining the todo_papers queue."""

from __future__ import annotations

import json
import logging
import os
import re
import sqlite3
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests

from backend.config import cfg

logger = logging.getLogger(__name__)

ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")


def utcnow_iso() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


class S2Client:
    def __init__(self, min_delay: float = 1.0):
        self.sess = requests.Session()
        key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or os.environ.get("S2_API_KEY")
        if key:
            self.sess.headers["x-api-key"] = key
        self.min_delay = float(min_delay)
        self._last_request_at: float = 0.0

    def _wait(self) -> None:
        elapsed = time.time() - self._last_request_at
        if elapsed < self.min_delay:
            time.sleep(self.min_delay - elapsed)

    def _get(
        self, url: str, params: dict[str, Any] | None = None, max_retries: int = 5
    ) -> requests.Response | None:
        for attempt in range(max_retries):
            self._wait()
            try:
                resp = self.sess.get(url, params=params, timeout=30)
            except requests.RequestException as exc:
                logger.warning("S2 request error for %s: %s — retrying", url, exc)
                time.sleep(2**attempt)
                continue

            self._last_request_at = time.time()
            if resp.status_code == 429:
                wait = (2**attempt) * 1.0
                logger.warning("S2 rate limited (429). Backing off %ss", wait)
                time.sleep(wait)
                continue
            if resp.status_code >= 400:
                logger.error("S2 HTTP %s for %s", resp.status_code, url)
                return None
            return resp
        return None

    def paper_id_for_arxiv(self, arxiv_id: str) -> str | None:
        url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}"
        resp = self._get(url, {"fields": "paperId,title,externalIds"})
        if resp is None:
            return None
        data = resp.json()
        return data.get("paperId")

    def fetch_paginated(self, base_url: str, fields: str, limit: int) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
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
                if "citingPaper" in entry:
                    results.append(entry.get("citingPaper") or {})
                else:
                    results.append(entry.get("citedPaper") or entry.get("reference") or entry)

            if len(results) >= limit:
                return results[:limit]

            next_offset = data.get("next")
            if not next_offset or len(batch) == 0:
                break
            offset = next_offset
        return results

    def fetch_citations(self, paper_id: str, limit: int) -> list[dict[str, Any]]:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations"
        return self.fetch_paginated(
            url, "paperId,title,authors,year,externalIds,publicationVenue,abstract,url", limit
        )

    def fetch_references(self, paper_id: str, limit: int) -> list[dict[str, Any]]:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references"
        return self.fetch_paginated(
            url, "paperId,title,authors,year,externalIds,publicationVenue,abstract,url", limit
        )


def infer_arxiv_id_from_s2(paper: dict[str, Any]) -> str | None:
    ext = paper.get("externalIds") or {}
    for key in ("ArXiv", "arXiv", "arxiv"):
        value = ext.get(key)
        if value:
            match = ARXIV_RE.search(str(value))
            if match:
                return match.group(1)

    for field in ("url", "publicationVenue", "title", "abstract"):
        match = ARXIV_RE.search(str(paper.get(field) or ""))
        if match:
            return match.group(1)

    return None


def ensure_s2_tables(conn: sqlite3.Connection) -> None:
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
    cur.execute("PRAGMA table_info(s2_crawl_state)")
    crawl_cols = {row[1] for row in cur.fetchall()}
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
    cur.execute("PRAGMA table_info(todo_papers)")
    todo_cols = {row[1] for row in cur.fetchall()}
    for col, defn in [
        ("seen_count", "INTEGER NOT NULL DEFAULT 0"),
        ("seen_from", "TEXT"),
        ("first_seen_at", "TEXT"),
        ("is_manually_important", "INTEGER NOT NULL DEFAULT 0"),
    ]:
        if col not in todo_cols:
            cur.execute(f"ALTER TABLE todo_papers ADD COLUMN {col} {defn}")
    conn.commit()


def load_local_corpus_from_papers_table(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='papers'")
    if not cur.fetchone():
        return

    logger.info("Loading local corpus from existing papers table")
    cur.execute("SELECT arxiv_id FROM papers WHERE arxiv_id IS NOT NULL")
    for (arxiv_id,) in cur.fetchall():
        cur.execute(
            "INSERT OR IGNORE INTO local_corpus(arxiv_id, meta) VALUES (?, ?)",
            (arxiv_id, None),
        )
    conn.commit()


def _load_seen_sources(raw: str | None) -> list[str]:
    if not raw:
        return []
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            return [str(item) for item in data if item]
    except Exception:
        pass
    return [raw]


def _unique_seen_sources(sources: list[str]) -> list[str]:
    unique: list[str] = []
    seen: set[str] = set()
    for source in sources:
        source = str(source).strip()
        if not source or source in seen:
            continue
        seen.add(source)
        unique.append(source)
    return unique


def _directional_counts(seen_sources: list[str]) -> tuple[int, int]:
    cited_by = 0
    cites_existing = 0
    for source in seen_sources:
        if source.startswith("references_from:"):
            cited_by += 1
        elif source.startswith("cited_by:"):
            cites_existing += 1
    return cited_by, cites_existing


def upsert_todo(conn: sqlite3.Connection, arxiv_id: str, title: str | None, seen_from: str) -> None:
    """Insert or update a todo_papers row from a unique citation/reference observation."""
    cur = conn.cursor()
    now = utcnow_iso()
    cur.execute(
        "INSERT OR IGNORE INTO todo_papers"
        "(arxiv_id, title, reason, added_by, status, attempts, cited_by_count,"
        " cites_existing_count, created_at, seen_count, seen_from, first_seen_at)"
        " VALUES (?, ?, 'semanticscholar', 's2_todo_crawl', 'pending', 0, 0, 0, ?, 1, ?, ?)",
        (arxiv_id, title or "", now, json.dumps([seen_from]), now),
    )
    cur.execute("SELECT seen_from, title FROM todo_papers WHERE arxiv_id = ?", (arxiv_id,))
    row = cur.fetchone()
    if row:
        seen_list = _unique_seen_sources(_load_seen_sources(row[0]) + [seen_from])
        seen_count = len(seen_list)
        cited_by_count, cites_existing_count = _directional_counts(seen_list)
        effective_title = title or row[1] or ""
        cur.execute(
            "UPDATE todo_papers SET seen_count = ?, seen_from = ?, title = COALESCE(NULLIF(?, ''), title),"
            " cited_by_count = ?, cites_existing_count = ?"
            " WHERE arxiv_id = ?",
            (
                seen_count,
                json.dumps(seen_list),
                effective_title,
                cited_by_count,
                cites_existing_count,
                arxiv_id,
            ),
        )
    conn.commit()


def repair_todo_counts(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute("SELECT arxiv_id, seen_from FROM todo_papers")
    for arxiv_id, seen_from in cur.fetchall():
        seen_list = _unique_seen_sources(_load_seen_sources(seen_from))
        seen_count = len(seen_list)
        cited_by_count, cites_existing_count = _directional_counts(seen_list)
        cur.execute(
            "UPDATE todo_papers SET seen_count = ?, seen_from = ?, cited_by_count = ?, cites_existing_count = ?"
            " WHERE arxiv_id = ?",
            (
                seen_count,
                json.dumps(seen_list),
                cited_by_count,
                cites_existing_count,
                arxiv_id,
            ),
        )
    conn.commit()


def sync_todo_status_with_local_corpus(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute(
        "UPDATE todo_papers SET status = 'done'"
        " WHERE arxiv_id IN (SELECT arxiv_id FROM local_corpus)"
        " AND status IN ('pending', 'processing', 'failed')"
    )
    conn.commit()


def insert_missing(
    conn: sqlite3.Connection, title: str | None, observed_in: str, payload: dict[str, Any]
) -> None:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO missing_papers(title, observed_in, payload, first_seen_at) VALUES (?, ?, ?, ?)",
        (title or "", observed_in, json.dumps(payload, ensure_ascii=False), utcnow_iso()),
    )
    conn.commit()


def mark_crawled(
    conn: sqlite3.Connection,
    paper_id: str,
    arxiv_id: str | None,
    seed_arxiv: str,
    *,
    citations_fetched: int = 0,
    references_fetched: int = 0,
    citations_capped: bool = False,
    references_capped: bool = False,
) -> None:
    cur = conn.cursor()
    cur.execute(
        "INSERT OR REPLACE INTO s2_crawl_state"
        "(paper_id, arxiv_id, seed_arxiv, crawled_at,"
        " citations_fetched, references_fetched, citations_capped, references_capped)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            paper_id,
            arxiv_id,
            seed_arxiv,
            utcnow_iso(),
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


def get_uncrawled_seeds(conn: sqlite3.Connection) -> list[str]:
    cur = conn.cursor()
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
    return [row[0] for row in cur.fetchall()]


def is_in_local_corpus(conn: sqlite3.Connection, arxiv_id: str) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM local_corpus WHERE arxiv_id = ?", (arxiv_id,))
    return cur.fetchone() is not None


def fetch_top_todo_rows(conn: sqlite3.Connection, top_n: int = 20) -> list[tuple[str, str, int]]:
    cur = conn.cursor()
    cur.execute(
        "SELECT arxiv_id, title, seen_count FROM todo_papers"
        " ORDER BY is_manually_important DESC, seen_count DESC LIMIT ?",
        (top_n,),
    )
    return [(row[0] or "", row[1] or "", int(row[2] or 0)) for row in cur.fetchall()]


def crawl_seed(
    s2: S2Client,
    conn: sqlite3.Connection,
    seed_arxiv: str,
    limit: int,
    force: bool,
) -> dict[str, int]:
    """Crawl one seed paper and upsert linked arXiv papers into todo_papers."""
    stats = {
        "citations": 0,
        "references": 0,
        "cite_added": 0,
        "ref_added": 0,
        "cite_missing": 0,
        "ref_missing": 0,
    }
    paper_id = s2.paper_id_for_arxiv(seed_arxiv)
    if not paper_id:
        logger.warning("Could not resolve seed arXiv:%s on Semantic Scholar", seed_arxiv)
        return stats

    if not force and already_crawled(conn, paper_id):
        logger.info("Seed paperId %s already crawled — skipping", paper_id)
        return stats

    citations = s2.fetch_citations(paper_id, limit)
    stats["citations"] = len(citations)
    for paper in citations:
        arxiv_id = infer_arxiv_id_from_s2(paper)
        if arxiv_id:
            if not is_in_local_corpus(conn, arxiv_id):
                upsert_todo(conn, arxiv_id, paper.get("title"), f"cited_by:{seed_arxiv}")
                stats["cite_added"] += 1
        else:
            insert_missing(conn, paper.get("title"), seed_arxiv, paper)
            stats["cite_missing"] += 1

    references = s2.fetch_references(paper_id, limit)
    stats["references"] = len(references)
    for paper in references:
        arxiv_id = infer_arxiv_id_from_s2(paper)
        if arxiv_id:
            if not is_in_local_corpus(conn, arxiv_id):
                upsert_todo(conn, arxiv_id, paper.get("title"), f"references_from:{seed_arxiv}")
                stats["ref_added"] += 1
        else:
            insert_missing(conn, paper.get("title"), seed_arxiv, paper)
            stats["ref_missing"] += 1

    mark_crawled(
        conn,
        paper_id,
        seed_arxiv,
        seed_arxiv,
        citations_fetched=len(citations),
        references_fetched=len(references),
        citations_capped=len(citations) >= limit,
        references_capped=len(references) >= limit,
    )
    return stats


def enrich_todo_from_semantic_scholar(
    arxiv_id: str,
    *,
    limit: int = 5000,
    db_path: Path | None = None,
) -> dict[str, int] | None:
    """Seed todo_papers from one paper's S2 citations and references.

    Returns count stats, or None when enrichment was skipped.
    """
    api_key = cfg.semantic_scholar_api_key
    if not api_key:
        logger.info("Semantic Scholar key missing — skipping citation expansion for %s", arxiv_id)
        return None

    path = db_path or cfg.db_path
    conn = sqlite3.connect(str(path))
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        ensure_s2_tables(conn)
        load_local_corpus_from_papers_table(conn)

        s2 = S2Client(min_delay=1.0)
        paper_id = s2.paper_id_for_arxiv(arxiv_id)
        if not paper_id:
            logger.info("Semantic Scholar has no paperId for arXiv:%s", arxiv_id)
            return None

        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM todo_papers")
        before_todo = int(cur.fetchone()[0])

        def _todo_exists(aid: str) -> bool:
            cur.execute("SELECT 1 FROM todo_papers WHERE arxiv_id = ?", (aid,))
            return cur.fetchone() is not None

        citations = s2.fetch_citations(paper_id, limit)
        references = s2.fetch_references(paper_id, limit)

        incoming_added = incoming_no_arxiv = incoming_known = 0
        for paper in citations:
            aid = infer_arxiv_id_from_s2(paper)
            if not aid:
                incoming_no_arxiv += 1
                continue
            if is_in_local_corpus(conn, aid):
                incoming_known += 1
                continue
            existed = _todo_exists(aid)
            upsert_todo(conn, aid, paper.get("title"), f"cited_by:{arxiv_id}")
            if not existed:
                incoming_added += 1

        outgoing_added = outgoing_no_arxiv = outgoing_known = 0
        for paper in references:
            aid = infer_arxiv_id_from_s2(paper)
            if not aid:
                outgoing_no_arxiv += 1
                continue
            if is_in_local_corpus(conn, aid):
                outgoing_known += 1
                continue
            existed = _todo_exists(aid)
            upsert_todo(conn, aid, paper.get("title"), f"references_from:{arxiv_id}")
            if not existed:
                outgoing_added += 1

        mark_crawled(
            conn,
            paper_id,
            arxiv_id,
            arxiv_id,
            citations_fetched=len(citations),
            references_fetched=len(references),
            citations_capped=len(citations) >= limit,
            references_capped=len(references) >= limit,
        )

        cur.execute("SELECT COUNT(*) FROM todo_papers")
        after_todo = int(cur.fetchone()[0])
        return {
            "incoming_citations": len(citations),
            "incoming_added": incoming_added,
            "incoming_known": incoming_known,
            "incoming_no_arxiv": incoming_no_arxiv,
            "outgoing_references": len(references),
            "outgoing_added": outgoing_added,
            "outgoing_known": outgoing_known,
            "outgoing_no_arxiv": outgoing_no_arxiv,
            "new_papers_queued": max(0, after_todo - before_todo),
        }
    finally:
        conn.close()


__all__ = [
    "S2Client",
    "already_crawled",
    "crawl_seed",
    "enrich_todo_from_semantic_scholar",
    "ensure_s2_tables",
    "fetch_top_todo_rows",
    "get_uncrawled_seeds",
    "infer_arxiv_id_from_s2",
    "is_in_local_corpus",
    "load_local_corpus_from_papers_table",
    "mark_crawled",
    "repair_todo_counts",
    "sync_todo_status_with_local_corpus",
    "upsert_todo",
]
