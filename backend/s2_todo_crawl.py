"""Semantic Scholar helpers for seeding and maintaining the todo_papers queue."""

from __future__ import annotations

import json
import logging
import os
import re
import sqlite3
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests

from backend.config import cfg
from backend.sqlite_retry import (
    configure_sqlite_connection,
    is_sqlite_lock_error,
    run_db_transaction,
)

logger = logging.getLogger(__name__)

ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")
_CITATION_FRESHNESS_SECONDS = 30 * 24 * 60 * 60
_is_sqlite_lock_error = is_sqlite_lock_error


@dataclass(frozen=True)
class PaginatedFetchResult:
    papers: list[dict[str, Any]]
    complete: bool


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

    def fetch_paginated(self, base_url: str, fields: str, limit: int) -> PaginatedFetchResult:
        results: list[dict[str, Any]] = []
        offset = 0
        page = min(limit, 500)
        while True:
            params = {"fields": fields, "limit": page, "offset": offset}
            resp = self._get(base_url, params)
            if resp is None:
                return PaginatedFetchResult(results, complete=False)
            data = resp.json()
            batch = data.get("data") or []
            for entry in batch:
                if "citingPaper" in entry:
                    results.append(entry.get("citingPaper") or {})
                else:
                    results.append(entry.get("citedPaper") or entry.get("reference") or entry)

            if len(results) >= limit:
                return PaginatedFetchResult(results[:limit], complete=True)

            next_offset = data.get("next")
            if not next_offset or len(batch) == 0:
                return PaginatedFetchResult(results, complete=True)
            offset = next_offset

    def fetch_citations(self, paper_id: str, limit: int) -> PaginatedFetchResult:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations"
        return self.fetch_paginated(
            url, "paperId,title,authors,year,externalIds,publicationVenue,abstract,url", limit
        )

    def fetch_references(self, paper_id: str, limit: int) -> PaginatedFetchResult:
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
    def _write(cur: sqlite3.Cursor) -> None:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS s2_crawl_state (
                paper_id           TEXT PRIMARY KEY,
                arxiv_id           TEXT,
                seed_arxiv         TEXT,
                crawled_at         TEXT,
                citations_fetched  INTEGER NOT NULL DEFAULT 0,
                references_fetched INTEGER NOT NULL DEFAULT 0,
                citations_capped   INTEGER NOT NULL DEFAULT 0,
                references_capped  INTEGER NOT NULL DEFAULT 0,
                crawl_complete     INTEGER NOT NULL DEFAULT 0,
                citations_fetched_at TEXT,
                references_fetched_at TEXT,
                citations_complete INTEGER NOT NULL DEFAULT 0,
                references_complete INTEGER NOT NULL DEFAULT 0
            )
            """)
        cur.execute("PRAGMA table_info(s2_crawl_state)")
        crawl_cols = {row[1] for row in cur.fetchall()}
        for col, defn in [
            ("citations_fetched", "INTEGER NOT NULL DEFAULT 0"),
            ("references_fetched", "INTEGER NOT NULL DEFAULT 0"),
            ("citations_capped", "INTEGER NOT NULL DEFAULT 0"),
            ("references_capped", "INTEGER NOT NULL DEFAULT 0"),
            ("crawl_complete", "INTEGER NOT NULL DEFAULT 0"),
            ("citations_fetched_at", "TEXT"),
            ("references_fetched_at", "TEXT"),
            ("citations_complete", "INTEGER NOT NULL DEFAULT 0"),
            ("references_complete", "INTEGER NOT NULL DEFAULT 0"),
        ]:
            if col not in crawl_cols:
                cur.execute(f"ALTER TABLE s2_crawl_state ADD COLUMN {col} {defn}")

        cur.execute(
            "UPDATE s2_crawl_state SET crawl_complete = 1"
            " WHERE crawl_complete = 0"
            " AND citations_fetched > 0 AND references_fetched > 0"
        )
        # Historical rows only recorded a successful crawl as a single event.
        # A completed legacy crawl therefore represents both complete directions.
        cur.execute(
            "UPDATE s2_crawl_state SET citations_complete = 1, references_complete = 1,"
            " citations_fetched_at = COALESCE(citations_fetched_at, crawled_at),"
            " references_fetched_at = COALESCE(references_fetched_at, crawled_at)"
            " WHERE crawl_complete = 1"
        )

        cur.execute("""
            CREATE TABLE IF NOT EXISTS missing_papers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                observed_in TEXT,
                payload TEXT,
                first_seen_at TEXT
            )
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS local_corpus (
                arxiv_id TEXT PRIMARY KEY,
                meta TEXT
            )
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS s2_metadata_cache (
                arxiv_id TEXT PRIMARY KEY,
                metadata TEXT NOT NULL,
                fetched_at TEXT NOT NULL
            )
            """)
        cur.execute("PRAGMA table_info(todo_papers)")
        todo_cols = {row[1] for row in cur.fetchall()}
        if todo_cols:
            for col, defn in [
                ("seen_count", "INTEGER NOT NULL DEFAULT 0"),
                ("seen_from", "TEXT"),
                ("first_seen_at", "TEXT"),
                ("is_manually_important", "INTEGER NOT NULL DEFAULT 0"),
            ]:
                if col not in todo_cols:
                    cur.execute(f"ALTER TABLE todo_papers ADD COLUMN {col} {defn}")

    run_db_transaction(conn, _write)


def cache_s2_metadata(conn: sqlite3.Connection, arxiv_id: str, metadata: dict[str, Any]) -> None:
    """Persist normalized S2 metadata for reuse by extraction and maintenance paths."""
    if not arxiv_id or not metadata:
        return
    ensure_s2_tables(conn)
    conn.execute(
        "INSERT INTO s2_metadata_cache(arxiv_id, metadata, fetched_at) VALUES (?, ?, ?)"
        " ON CONFLICT(arxiv_id) DO UPDATE SET metadata = excluded.metadata,"
        " fetched_at = excluded.fetched_at",
        (arxiv_id, json.dumps(metadata, ensure_ascii=False), utcnow_iso()),
    )
    conn.commit()


def load_cached_s2_metadata(conn: sqlite3.Connection, arxiv_id: str) -> dict[str, Any] | None:
    """Load cached S2 metadata without applying a freshness policy."""
    ensure_s2_tables(conn)
    row = conn.execute(
        "SELECT metadata FROM s2_metadata_cache WHERE arxiv_id = ?", (arxiv_id,)
    ).fetchone()
    if row is None:
        return None
    try:
        value = json.loads(row[0])
    except (TypeError, ValueError):
        return None
    return value if isinstance(value, dict) else None


def load_local_corpus_from_papers_table(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='papers'")
    if not cur.fetchone():
        return

    logger.info("Loading local corpus from existing papers table")
    rows = conn.execute("SELECT arxiv_id FROM papers WHERE arxiv_id IS NOT NULL").fetchall()

    def _write(cur: sqlite3.Cursor) -> None:
        for (arxiv_id,) in rows:
            cur.execute(
                "INSERT OR IGNORE INTO local_corpus(arxiv_id, meta) VALUES (?, ?)",
                (arxiv_id, None),
            )

    run_db_transaction(conn, _write)


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
    now = utcnow_iso()

    def _write(cur: sqlite3.Cursor) -> None:
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

    run_db_transaction(conn, _write)


def repair_todo_counts(conn: sqlite3.Connection) -> None:
    rows = conn.execute("SELECT arxiv_id, seen_from FROM todo_papers").fetchall()

    def _write(cur: sqlite3.Cursor) -> None:
        for arxiv_id, seen_from in rows:
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

    run_db_transaction(conn, _write)


def sync_todo_status_with_local_corpus(conn: sqlite3.Connection) -> None:
    def _write(cur: sqlite3.Cursor) -> None:
        cur.execute(
            "UPDATE todo_papers SET status = 'done'"
            " WHERE arxiv_id IN (SELECT arxiv_id FROM local_corpus)"
            " AND status IN ('pending', 'processing', 'failed')"
        )

    run_db_transaction(conn, _write)


def insert_missing(
    conn: sqlite3.Connection, title: str | None, observed_in: str, payload: dict[str, Any]
) -> None:
    def _write(cur: sqlite3.Cursor) -> None:
        cur.execute(
            "INSERT INTO missing_papers(title, observed_in, payload, first_seen_at) VALUES (?, ?, ?, ?)",
            (title or "", observed_in, json.dumps(payload, ensure_ascii=False), utcnow_iso()),
        )

    run_db_transaction(conn, _write)


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
    citations_complete: bool = True,
    references_complete: bool = True,
    citations_fetched_at: str | None = None,
    references_fetched_at: str | None = None,
) -> None:
    def _write(cur: sqlite3.Cursor) -> None:
        now = utcnow_iso()
        citation_timestamp = (
            citations_fetched_at
            if citations_fetched_at is not None
            else (now if citations_complete else None)
        )
        reference_timestamp = (
            references_fetched_at
            if references_fetched_at is not None
            else (now if references_complete else None)
        )
        cur.execute(
            "INSERT INTO s2_crawl_state"
            "(paper_id, arxiv_id, seed_arxiv, crawled_at,"
            " citations_fetched, references_fetched, citations_capped, references_capped,"
            " crawl_complete, citations_fetched_at, references_fetched_at,"
            " citations_complete, references_complete)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            " ON CONFLICT(paper_id) DO UPDATE SET"
            " arxiv_id = excluded.arxiv_id, seed_arxiv = excluded.seed_arxiv,"
            " crawled_at = excluded.crawled_at, citations_fetched = excluded.citations_fetched,"
            " references_fetched = excluded.references_fetched,"
            " citations_capped = excluded.citations_capped,"
            " references_capped = excluded.references_capped,"
            " crawl_complete = excluded.crawl_complete,"
            " citations_fetched_at = excluded.citations_fetched_at,"
            " references_fetched_at = excluded.references_fetched_at,"
            " citations_complete = excluded.citations_complete,"
            " references_complete = excluded.references_complete",
            (
                paper_id,
                arxiv_id,
                seed_arxiv,
                now,
                citations_fetched,
                references_fetched,
                int(citations_capped),
                int(references_capped),
                int(citations_complete and references_complete),
                citation_timestamp,
                reference_timestamp,
                int(citations_complete),
                int(references_complete),
            ),
        )

    run_db_transaction(conn, _write)


def _crawl_state_for_arxiv(conn: sqlite3.Connection, arxiv_id: str) -> dict[str, Any] | None:
    cur = conn.execute(
        "SELECT * FROM s2_crawl_state WHERE arxiv_id = ? OR seed_arxiv = ?"
        " ORDER BY crawled_at DESC LIMIT 1",
        (arxiv_id, arxiv_id),
    )
    row = cur.fetchone()
    if row is None:
        return None
    return dict(zip((column[0] for column in cur.description), row, strict=True))


def _citation_is_fresh(fetched_at: str | None) -> bool:
    if not fetched_at:
        return False
    try:
        fetched = datetime.fromisoformat(fetched_at.replace("Z", "+00:00"))
    except ValueError:
        return False
    return (datetime.now(UTC) - fetched).total_seconds() < _CITATION_FRESHNESS_SECONDS


def _s2_fetch_plan(state: dict[str, Any] | None, *, force: bool) -> tuple[bool, bool]:
    """Return (fetch_citations, fetch_references) for one S2 crawl."""
    if force or state is None:
        return True, True
    if not state["citations_complete"] or not state["references_complete"]:
        return True, True
    return not _citation_is_fresh(state["citations_fetched_at"]), False


def already_crawled(conn: sqlite3.Connection, paper_id: str) -> bool:
    cur = conn.cursor()
    cur.execute(
        "SELECT crawl_complete FROM s2_crawl_state WHERE paper_id = ?",
        (paper_id,),
    )
    row = cur.fetchone()
    return bool(row and row[0])


def get_uncrawled_seeds(conn: sqlite3.Connection) -> list[str]:
    """Return DB papers needing an incomplete crawl or a citation refresh."""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='papers'")
    if not cur.fetchone():
        return []
    cur.execute("SELECT arxiv_id FROM papers WHERE arxiv_id IS NOT NULL ORDER BY created_at")
    seeds: list[str] = []
    for (arxiv_id,) in cur.fetchall():
        if any(_s2_fetch_plan(_crawl_state_for_arxiv(conn, arxiv_id), force=False)):
            seeds.append(arxiv_id)
    return seeds


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
        "marked_complete": 0,
        "metadata_filled": {"published_date": False, "venue": False, "authors": False},
    }
    state = _crawl_state_for_arxiv(conn, seed_arxiv)
    paper_id = str(state["paper_id"]) if state else s2.paper_id_for_arxiv(seed_arxiv)
    if not paper_id:
        logger.warning("Could not resolve seed arXiv:%s on Semantic Scholar", seed_arxiv)
        return stats

    try:
        from backend.semantic_scholar import ensure_paper_metadata, normalize_s2_metadata

        stats["metadata_filled"] = ensure_paper_metadata(seed_arxiv)
    except Exception as exc:
        logger.warning("Paper metadata backfill failed for arXiv:%s: %s", seed_arxiv, exc)

    fetch_citations, fetch_references = _s2_fetch_plan(state, force=force)
    if not fetch_citations and not fetch_references:
        logger.info(
            "Seed paperId %s has fresh citations and complete references — skipping", paper_id
        )
        return stats

    citation_result = s2.fetch_citations(paper_id, limit) if fetch_citations else None
    reference_result = s2.fetch_references(paper_id, limit) if fetch_references else None
    stats["citations"] = len(citation_result.papers) if citation_result else 0
    stats["references"] = len(reference_result.papers) if reference_result else 0

    for paper in citation_result.papers if citation_result and citation_result.complete else []:
        arxiv_id = infer_arxiv_id_from_s2(paper)
        if arxiv_id:
            cache_s2_metadata(conn, arxiv_id, normalize_s2_metadata(paper))
            if not is_in_local_corpus(conn, arxiv_id):
                upsert_todo(conn, arxiv_id, paper.get("title"), f"cited_by:{seed_arxiv}")
                stats["cite_added"] += 1
        else:
            insert_missing(conn, paper.get("title"), seed_arxiv, paper)
            stats["cite_missing"] += 1

    for paper in reference_result.papers if reference_result and reference_result.complete else []:
        arxiv_id = infer_arxiv_id_from_s2(paper)
        if arxiv_id:
            cache_s2_metadata(conn, arxiv_id, normalize_s2_metadata(paper))
            if not is_in_local_corpus(conn, arxiv_id):
                upsert_todo(conn, arxiv_id, paper.get("title"), f"references_from:{seed_arxiv}")
                stats["ref_added"] += 1
        else:
            insert_missing(conn, paper.get("title"), seed_arxiv, paper)
            stats["ref_missing"] += 1

    citations_complete = (
        citation_result.complete if citation_result else bool(state and state["citations_complete"])
    )
    references_complete = (
        reference_result.complete
        if reference_result
        else bool(state and state["references_complete"])
    )
    if not citations_complete or not references_complete:
        logger.warning("Incomplete Semantic Scholar crawl for arXiv:%s", seed_arxiv)

    mark_crawled(
        conn,
        paper_id,
        seed_arxiv,
        seed_arxiv,
        citations_fetched=(
            len(citation_result.papers) if citation_result else int(state["citations_fetched"])
        ),
        references_fetched=(
            len(reference_result.papers) if reference_result else int(state["references_fetched"])
        ),
        citations_capped=(
            len(citation_result.papers) >= limit
            if citation_result
            else bool(state["citations_capped"])
        ),
        references_capped=(
            len(reference_result.papers) >= limit
            if reference_result
            else bool(state["references_capped"])
        ),
        citations_complete=citations_complete,
        references_complete=references_complete,
        citations_fetched_at=(
            utcnow_iso()
            if citation_result and citation_result.complete
            else (state["citations_fetched_at"] if state else None)
        ),
        references_fetched_at=(
            utcnow_iso()
            if reference_result and reference_result.complete
            else (state["references_fetched_at"] if state else None)
        ),
    )
    stats["marked_complete"] = int(citations_complete and references_complete)
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
    configure_sqlite_connection(conn)
    try:
        ensure_s2_tables(conn)
        load_local_corpus_from_papers_table(conn)

        state = _crawl_state_for_arxiv(conn, arxiv_id)
        s2 = S2Client(min_delay=1.0)
        paper_id = str(state["paper_id"]) if state else s2.paper_id_for_arxiv(arxiv_id)
        if not paper_id:
            logger.info("Semantic Scholar has no paperId for arXiv:%s", arxiv_id)
            return None

        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM todo_papers")
        before_todo = int(cur.fetchone()[0])

        def _todo_exists(aid: str) -> bool:
            cur.execute("SELECT 1 FROM todo_papers WHERE arxiv_id = ?", (aid,))
            return cur.fetchone() is not None

        fetch_citations, fetch_references = _s2_fetch_plan(state, force=False)
        citation_result = s2.fetch_citations(paper_id, limit) if fetch_citations else None
        reference_result = s2.fetch_references(paper_id, limit) if fetch_references else None

        incoming_added = incoming_no_arxiv = incoming_known = 0
        for paper in citation_result.papers if citation_result and citation_result.complete else []:
            aid = infer_arxiv_id_from_s2(paper)
            if not aid:
                incoming_no_arxiv += 1
                continue
            from backend.semantic_scholar import normalize_s2_metadata

            cache_s2_metadata(conn, aid, normalize_s2_metadata(paper))
            if is_in_local_corpus(conn, aid):
                incoming_known += 1
                continue
            existed = _todo_exists(aid)
            upsert_todo(conn, aid, paper.get("title"), f"cited_by:{arxiv_id}")
            if not existed:
                incoming_added += 1

        outgoing_added = outgoing_no_arxiv = outgoing_known = 0
        for paper in (
            reference_result.papers if reference_result and reference_result.complete else []
        ):
            aid = infer_arxiv_id_from_s2(paper)
            if not aid:
                outgoing_no_arxiv += 1
                continue
            cache_s2_metadata(conn, aid, normalize_s2_metadata(paper))
            if is_in_local_corpus(conn, aid):
                outgoing_known += 1
                continue
            existed = _todo_exists(aid)
            upsert_todo(conn, aid, paper.get("title"), f"references_from:{arxiv_id}")
            if not existed:
                outgoing_added += 1

        citations_complete = (
            citation_result.complete
            if citation_result
            else bool(state and state["citations_complete"])
        )
        references_complete = (
            reference_result.complete
            if reference_result
            else bool(state and state["references_complete"])
        )
        mark_crawled(
            conn,
            paper_id,
            arxiv_id,
            arxiv_id,
            citations_fetched=(
                len(citation_result.papers) if citation_result else int(state["citations_fetched"])
            ),
            references_fetched=(
                len(reference_result.papers)
                if reference_result
                else int(state["references_fetched"])
            ),
            citations_capped=(
                len(citation_result.papers) >= limit
                if citation_result
                else bool(state["citations_capped"])
            ),
            references_capped=(
                len(reference_result.papers) >= limit
                if reference_result
                else bool(state["references_capped"])
            ),
            citations_complete=citations_complete,
            references_complete=references_complete,
            citations_fetched_at=(
                utcnow_iso()
                if citation_result and citation_result.complete
                else (state["citations_fetched_at"] if state else None)
            ),
            references_fetched_at=(
                utcnow_iso()
                if reference_result and reference_result.complete
                else (state["references_fetched_at"] if state else None)
            ),
        )

        cur.execute("SELECT COUNT(*) FROM todo_papers")
        after_todo = int(cur.fetchone()[0])
        return {
            "incoming_citations": len(citation_result.papers) if citation_result else 0,
            "incoming_added": incoming_added,
            "incoming_known": incoming_known,
            "incoming_no_arxiv": incoming_no_arxiv,
            "outgoing_references": len(reference_result.papers) if reference_result else 0,
            "outgoing_added": outgoing_added,
            "outgoing_known": outgoing_known,
            "outgoing_no_arxiv": outgoing_no_arxiv,
            "new_papers_queued": max(0, after_todo - before_todo),
        }
    finally:
        conn.close()


__all__ = [
    "PaginatedFetchResult",
    "S2Client",
    "_is_sqlite_lock_error",
    "already_crawled",
    "configure_sqlite_connection",
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
    "run_db_transaction",
    "sync_todo_status_with_local_corpus",
    "upsert_todo",
]
