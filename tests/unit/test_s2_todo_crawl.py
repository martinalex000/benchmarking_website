"""Tests for Semantic Scholar todo crawl helpers."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

import pytest

from backend.s2_todo_crawl import (
    PaginatedFetchResult,
    already_crawled,
    configure_sqlite_connection,
    crawl_seed,
    ensure_s2_tables,
    get_uncrawled_seeds,
    infer_arxiv_id_from_s2,
    mark_crawled,
    run_db_transaction,
)


def test_infer_arxiv_id_from_external_ids():
    paper = {"externalIds": {"ArXiv": "2206.08164v2"}}
    assert infer_arxiv_id_from_s2(paper) == "2206.08164"


def test_infer_arxiv_id_from_url_fallback():
    paper = {"url": "https://arxiv.org/abs/2406.08993"}
    assert infer_arxiv_id_from_s2(paper) == "2406.08993"


def _setup_seed_db(conn: sqlite3.Connection, arxiv_id: str = "2206.08164") -> None:
    conn.execute(
        "CREATE TABLE papers (id INTEGER PRIMARY KEY, arxiv_id TEXT, created_at TEXT)"
    )
    conn.execute(
        "CREATE TABLE todo_papers (id INTEGER PRIMARY KEY, arxiv_id TEXT UNIQUE, title TEXT,"
        " reason TEXT, added_by TEXT, status TEXT, attempts INTEGER, cited_by_count INTEGER,"
        " cites_existing_count INTEGER, created_at TEXT)"
    )
    conn.execute(
        "INSERT INTO papers (arxiv_id, created_at) VALUES (?, ?)",
        (arxiv_id, "2024-01-01T00:00:00Z"),
    )
    ensure_s2_tables(conn)


@dataclass
class FakeS2Client:
    paper_id: str = "s2-paper-1"
    citations: PaginatedFetchResult = PaginatedFetchResult([], complete=True)
    references: PaginatedFetchResult = PaginatedFetchResult([], complete=True)
    paper_id_calls: int = 0
    citation_calls: int = 0
    reference_calls: int = 0

    def paper_id_for_arxiv(self, arxiv_id: str) -> str | None:
        self.paper_id_calls += 1
        return self.paper_id

    def fetch_citations(self, paper_id: str, limit: int) -> PaginatedFetchResult:
        self.citation_calls += 1
        return self.citations

    def fetch_references(self, paper_id: str, limit: int) -> PaginatedFetchResult:
        self.reference_calls += 1
        return self.references


def test_get_uncrawled_seeds_includes_never_crawled_and_incomplete_rows():
    conn = sqlite3.connect(":memory:")
    _setup_seed_db(conn)

    assert get_uncrawled_seeds(conn) == ["2206.08164"]

    mark_crawled(
        conn,
        "s2-paper-1",
        "2206.08164",
        "2206.08164",
        citations_fetched=10,
        references_fetched=0,
    )
    conn.execute(
        "UPDATE s2_crawl_state SET crawl_complete = 0, references_complete = 0"
        " WHERE paper_id = 's2-paper-1'"
    )
    conn.commit()

    assert get_uncrawled_seeds(conn) == ["2206.08164"]

    conn.execute(
        "UPDATE s2_crawl_state SET crawl_complete = 1, references_complete = 1"
        " WHERE paper_id = 's2-paper-1'"
    )
    conn.commit()
    assert get_uncrawled_seeds(conn) == []


def test_crawl_seed_does_not_mark_incomplete_fetch():
    conn = sqlite3.connect(":memory:")
    _setup_seed_db(conn)
    s2 = FakeS2Client(
        citations=PaginatedFetchResult([], complete=False),
        references=PaginatedFetchResult([{"externalIds": {"ArXiv": "2406.08993"}}], complete=True),
    )

    stats = crawl_seed(s2, conn, "2206.08164", limit=100, force=False)

    assert stats["marked_complete"] == 0
    assert already_crawled(conn, "s2-paper-1") is False


def test_crawl_seed_marks_complete_fetch():
    conn = sqlite3.connect(":memory:")
    _setup_seed_db(conn)
    s2 = FakeS2Client(
        citations=PaginatedFetchResult(
            [{"externalIds": {"ArXiv": "2406.08993"}, "title": "Citer"}],
            complete=True,
        ),
        references=PaginatedFetchResult([], complete=True),
    )

    stats = crawl_seed(s2, conn, "2206.08164", limit=100, force=False)

    assert stats["marked_complete"] == 1
    assert already_crawled(conn, "s2-paper-1") is True


@pytest.mark.parametrize(
    ("citations_at", "citations_complete", "references_complete", "expected_calls"),
    [
        (None, None, None, (1, 1)),
        (None, True, False, (1, 1)),
        ("fresh", True, True, (0, 0)),
        ("overdue", True, True, (1, 0)),
    ],
)
def test_crawl_seed_uses_directional_freshness_cache(
    citations_at, citations_complete, references_complete, expected_calls
):
    conn = sqlite3.connect(":memory:")
    _setup_seed_db(conn)
    s2 = FakeS2Client()
    if citations_complete is not None:
        timestamp = (
            datetime.now(UTC) - (timedelta(days=31) if citations_at == "overdue" else timedelta(days=1))
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        mark_crawled(
            conn,
            s2.paper_id,
            "2206.08164",
            "2206.08164",
            citations_complete=citations_complete,
            references_complete=references_complete,
            citations_fetched_at=timestamp,
            references_fetched_at=timestamp,
        )

    crawl_seed(s2, conn, "2206.08164", limit=100, force=False)

    assert (s2.citation_calls, s2.reference_calls) == expected_calls
    assert s2.paper_id_calls == (1 if citations_complete is None else 0)


def test_crawl_seed_force_refreshes_both_directions():
    conn = sqlite3.connect(":memory:")
    _setup_seed_db(conn)
    s2 = FakeS2Client()
    mark_crawled(conn, s2.paper_id, "2206.08164", "2206.08164")

    crawl_seed(s2, conn, "2206.08164", limit=100, force=True)

    assert (s2.citation_calls, s2.reference_calls) == (1, 1)
    assert s2.paper_id_calls == 0


def test_run_db_transaction_retries_on_database_locked(monkeypatch):
    conn = sqlite3.connect(":memory:")
    configure_sqlite_connection(conn)
    attempts = {"count": 0}

    def _write(cur: sqlite3.Cursor) -> None:
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise sqlite3.OperationalError("database is locked")
        cur.execute("CREATE TABLE IF NOT EXISTS lock_retry_test (id INTEGER PRIMARY KEY)")

    monkeypatch.setattr("backend.sqlite_retry.time.sleep", lambda _seconds: None)
    run_db_transaction(conn, _write, max_retries=5)

    assert attempts["count"] == 3
    assert conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='lock_retry_test'"
    ).fetchone()
