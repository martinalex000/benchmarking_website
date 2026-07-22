"""Semantic Scholar Graph API helpers."""

from __future__ import annotations

import json
import logging
import re
import sqlite3
import time
from typing import Any

import requests

from backend.config import cfg
from backend.models import AuthorRecord, author_display_name, normalize_author_entry
from backend.venue import (
    is_arxiv_only_venue,
    is_untrusted_s2_publication_venue,
    is_untrusted_venue,
    resolve_canonical_venue,
    venue_from_arxiv_comment,
    venue_from_openreview_fields,
    venue_needs_resolution,
)

logger = logging.getLogger(__name__)

_S2_BASE = "https://api.semanticscholar.org/graph/v1"
_S2_FIELDS = "title,abstract,year,publicationDate,venue,publicationVenue,journal,externalIds"
_ORCID_RE = re.compile(r"(\d{4}-\d{4}-\d{4}-\d{3}[\dX])")
_ARXIV_DATE_RE = re.compile(r"^(\d{2})(\d{2})\.\d+")


def _s2_headers() -> dict[str, str]:
    headers = {"Accept": "application/json"}
    if cfg.semantic_scholar_api_key:
        headers["x-api-key"] = cfg.semantic_scholar_api_key
    return headers


def _s2_request(
    url: str,
    payload: dict[str, Any] | None = None,
    *,
    is_batch: bool = False,
    max_retries: int = 5,
) -> dict[str, Any] | list[dict[str, Any]] | None:
    """Send a request to the Semantic Scholar API with retries."""
    for attempt in range(max_retries):
        try:
            if is_batch:
                resp = requests.post(url, json=payload, headers=_s2_headers(), timeout=30)
            else:
                resp = requests.get(url, headers=_s2_headers(), params=payload, timeout=30)
        except requests.RequestException as exc:
            logger.warning("Semantic Scholar request error for %s: %s — retrying", url, exc)
            time.sleep(2**attempt)
            continue

        if resp.status_code == 429:
            wait = 2**attempt
            logger.warning("Semantic Scholar rate-limited for %s — backing off %ss", url, wait)
            time.sleep(wait)
            continue
        if resp.status_code >= 400:
            logger.debug("Semantic Scholar HTTP error %s for %s", resp.status_code, url)
            return None
        body = resp.text
        return json.loads(body) if body else None
    return None


def _parse_orcid(raw: object) -> str | None:
    if raw is None:
        return None
    match = _ORCID_RE.search(str(raw))
    return match.group(1) if match else None


def _published_date_from_arxiv_id(arxiv_id: str) -> str:
    match = _ARXIV_DATE_RE.match(arxiv_id)
    if not match:
        return ""
    year, month = int(match.group(1)) + 2000, int(match.group(2))
    if 1 <= month <= 12:
        return f"{year}-{month:02d}"
    return ""


def _named_object_field(value: object, *keys: str) -> str:
    if isinstance(value, dict):
        for key in keys:
            text = str(value.get(key) or "").strip()
            if text:
                return text
    elif isinstance(value, str):
        return value.strip()
    return ""


def _resolve_venue_from_s2(data: dict[str, Any]) -> str:
    """Prefer a real publication venue over arXiv-only labels from Semantic Scholar."""
    pub_venue_obj = data.get("publicationVenue")
    if is_untrusted_s2_publication_venue(pub_venue_obj):
        return ""

    top_venue = str(data.get("venue") or "").strip()
    pub_venue = _named_object_field(pub_venue_obj, "name", "venue")
    journal_venue = _named_object_field(data.get("journal"), "name")

    if (
        is_untrusted_venue(top_venue)
        or is_untrusted_venue(pub_venue)
        or is_untrusted_venue(journal_venue)
    ):
        return ""

    if pub_venue and (not top_venue or is_arxiv_only_venue(top_venue)):
        return resolve_canonical_venue(pub_venue)
    if top_venue and not is_arxiv_only_venue(top_venue):
        return resolve_canonical_venue(top_venue)
    if pub_venue:
        return resolve_canonical_venue(pub_venue)
    if journal_venue:
        return resolve_canonical_venue(journal_venue)
    return ""


def _venue_from_local_metadata(arxiv_id: str) -> str:
    from backend.paper_storage import PaperStorage

    meta = PaperStorage(arxiv_id).read_metadata()
    if not meta:
        return ""
    for key in ("openreview_venue", "venue", "arxiv_comment", "journal_ref"):
        raw = str(meta.get(key) or "").strip()
        if not raw:
            continue
        venue = venue_from_openreview_fields(raw) or venue_from_arxiv_comment(raw)
        if venue:
            return venue
    return ""


def _venue_from_openreview_for_paper(arxiv_id: str) -> str:
    if not (cfg.openreview_token or (cfg.openreview_username and cfg.openreview_password)):
        return ""
    from backend.db import session_scope
    from backend.models import Paper
    from backend.openreview_client import OpenReviewClient, OpenReviewError
    from backend.paper_matching import author_last_names, author_overlap_score, titles_match

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None or not paper.title:
            return ""
        title = paper.title
        authors = [author_display_name(author) for author in paper.authors or []]

    try:
        client = OpenReviewClient.from_config()
    except OpenReviewError:
        return ""

    for year in (2025, 2024, 2023, 2022):
        venue_group = f"logconference.io/LOG/{year}/Conference"
        try:
            candidates = client.search_submissions_by_title(venue_group, title)
        except OpenReviewError as exc:
            logger.debug("OpenReview title search failed for %s: %s", venue_group, exc)
            continue
        for candidate in candidates:
            if not titles_match(title, candidate.title):
                continue
            if authors and candidate.authors:
                from backend.paper_matching import author_last_names, author_overlap_score

                overlap = author_overlap_score(
                    author_last_names(authors), author_last_names(candidate.authors)
                )
                if overlap < 0.34:
                    continue
            venue = venue_from_openreview_fields(candidate.venue, candidate.venueid)
            if venue:
                _cache_venue_metadata(arxiv_id, venue, candidate.venue, candidate.venueid)
                return venue
    return ""


def _cache_venue_metadata(
    arxiv_id: str,
    canonical_venue: str,
    openreview_venue: str = "",
    openreview_venueid: str = "",
) -> None:
    from backend.paper_storage import PaperStorage

    updates: dict[str, str] = {"venue": canonical_venue}
    if openreview_venue:
        updates["openreview_venue"] = openreview_venue
    if openreview_venueid:
        updates["openreview_venueid"] = openreview_venueid
    try:
        PaperStorage(arxiv_id).update_metadata(updates)
    except Exception as exc:
        logger.debug("Could not cache venue metadata for %s: %s", arxiv_id, exc)


def _venue_from_arxiv_metadata(arxiv_id: str) -> str:
    if cfg.skip_arxiv_metadata_api:
        return ""
    from backend.llm_metadata import fetch_arxiv_metadata

    arxiv_meta = fetch_arxiv_metadata(arxiv_id)
    cache_updates: dict[str, str] = {}
    resolved = ""
    for key in ("arxiv_comment", "journal_ref"):
        raw = str(arxiv_meta.get(key) or "").strip()
        if raw:
            cache_updates[key] = raw
        venue = venue_from_arxiv_comment(raw)
        if venue:
            resolved = venue
            break
    if cache_updates or resolved:
        cache_updates.update({"venue": resolved} if resolved else {})
        try:
            from backend.paper_storage import PaperStorage

            PaperStorage(arxiv_id).update_metadata(cache_updates)
        except Exception as exc:
            logger.debug("Could not cache arXiv metadata for %s: %s", arxiv_id, exc)
    return resolved


def resolve_paper_venue(arxiv_id: str, ss_meta: dict[str, str] | None = None) -> str:
    """Resolve a canonical venue string from S2 metadata with local/OpenReview fallbacks."""
    meta = ss_meta if ss_meta is not None else fetch_paper_metadata(arxiv_id)
    s2_venue = str(meta.get("venue") or "").strip()
    if s2_venue and not is_untrusted_venue(s2_venue):
        canonical = resolve_canonical_venue(s2_venue)
        if canonical:
            return canonical
    for resolver in (
        _venue_from_local_metadata,
        _venue_from_openreview_for_paper,
        _venue_from_arxiv_metadata,
    ):
        venue = resolver(arxiv_id)
        if venue:
            return venue
    return ""


def _paper_fields(data: dict[str, Any] | None) -> dict[str, str]:
    if not isinstance(data, dict):
        return {}
    meta: dict[str, str] = {}
    title = str(data.get("title") or "").strip()
    abstract = str(data.get("abstract") or "").strip()
    if title:
        meta["title"] = title
    if abstract:
        meta["abstract"] = abstract

    published_date = str(data.get("publicationDate") or "").strip()
    if published_date:
        meta["published_date"] = published_date[:10]
    else:
        year = data.get("year")
        if isinstance(year, int) and year > 0:
            meta["published_date"] = f"{year:04d}-01-01"
        elif isinstance(year, str) and year.isdigit():
            meta["published_date"] = f"{int(year):04d}-01-01"

    venue = _resolve_venue_from_s2(data)
    if venue:
        meta["venue"] = venue
    return meta


def normalize_s2_metadata(data: dict[str, Any] | None) -> dict[str, str]:
    """Normalize an S2 API payload for the shared metadata cache."""
    return _paper_fields(data)


def fetch_cached_paper_metadata(arxiv_id: str) -> dict[str, str]:
    """Read immutable S2 metadata from the DB, fetching it only when absent."""
    from backend.s2_todo_crawl import (
        cache_s2_metadata,
        configure_sqlite_connection,
        ensure_s2_tables,
        load_cached_s2_metadata,
    )

    conn = sqlite3.connect(str(cfg.db_path))
    configure_sqlite_connection(conn)
    try:
        ensure_s2_tables(conn)
        cached = load_cached_s2_metadata(conn, arxiv_id)
        if cached:
            return {str(key): str(value) for key, value in cached.items()}
        metadata = fetch_paper_metadata(arxiv_id)
        if metadata:
            cache_s2_metadata(conn, arxiv_id, metadata)
        return metadata
    finally:
        conn.close()


def cache_paper_metadata(arxiv_id: str, metadata: dict[str, str]) -> None:
    """Write normalized S2 metadata to the shared database cache."""
    from backend.s2_todo_crawl import (
        cache_s2_metadata,
        configure_sqlite_connection,
        ensure_s2_tables,
    )

    conn = sqlite3.connect(str(cfg.db_path))
    configure_sqlite_connection(conn)
    try:
        ensure_s2_tables(conn)
        cache_s2_metadata(conn, arxiv_id, metadata)
    finally:
        conn.close()


def fetch_paper_metadata(arxiv_id: str) -> dict[str, str]:
    url = f"{_S2_BASE}/paper/ARXIV:{arxiv_id}"
    data = _s2_request(url, {"fields": _S2_FIELDS})
    return _paper_fields(data if isinstance(data, dict) else None)


def fetch_paper_metadata_batch(arxiv_ids: list[str]) -> dict[str, dict[str, str]]:
    """Fetch metadata individually for each arXiv ID."""
    results: dict[str, dict[str, str]] = {}
    for i, arxiv_id in enumerate(arxiv_ids):
        if i and i % 50 == 0:
            logger.info("Batch progress: %d/%d papers fetched", i, len(arxiv_ids))
        try:
            meta = fetch_paper_metadata(arxiv_id)
            if meta:
                results[arxiv_id] = meta
        except Exception:
            logger.debug("S2 request failed for arXiv:%s", arxiv_id)
    logger.info("S2 individual results: %d/%d papers with metadata", len(results), len(arxiv_ids))
    return results


def fetch_paper_author_ids(arxiv_id: str) -> list[dict[str, str]]:
    url = f"{_S2_BASE}/paper/ARXIV:{arxiv_id}"
    data = _s2_request(url, {"fields": "authors"})
    if not isinstance(data, dict):
        return []
    authors: list[dict[str, str]] = []
    for entry in data.get("authors") or []:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("name") or "").strip()
        author_id = str(entry.get("authorId") or "").strip()
        if name:
            authors.append({"author_id": author_id, "name": name})
    return authors


def fetch_author_external_ids(author_ids: list[str]) -> dict[str, dict[str, str | None]]:
    ids = [author_id for author_id in author_ids if author_id]
    if not ids:
        return {}
    url = f"{_S2_BASE}/author/batch"
    data = _s2_request(url, {"ids": ids}, is_batch=True)
    if not isinstance(data, list):
        return {}

    results: dict[str, dict[str, str | None]] = {}
    for entry in data:
        if not isinstance(entry, dict):
            continue
        author_id = str(entry.get("authorId") or "").strip()
        if not author_id:
            continue
        external_ids = entry.get("externalIds") or {}
        orcid = None
        if isinstance(external_ids, dict):
            orcid = _parse_orcid(external_ids.get("ORCID") or external_ids.get("orcid"))
        results[author_id] = {
            "orcid": orcid,
            "url": str(entry.get("url") or "").strip() or None,
        }
    return results


def authors_from_s2_only(s2_authors: list[dict[str, str]]) -> list[AuthorRecord]:
    author_ids = [author["author_id"] for author in s2_authors if author.get("author_id")]
    external = fetch_author_external_ids(author_ids)
    records: list[AuthorRecord] = []
    for author in s2_authors:
        author_id = author.get("author_id") or ""
        ext = external.get(author_id, {})
        records.append(
            normalize_author_entry(
                {
                    "name": author.get("name") or "",
                    "orcid": ext.get("orcid"),
                    "s2_author_id": author_id or None,
                    "s2_url": ext.get("url"),
                }
            )
        )
    return records


def merge_latex_authors_with_s2(
    latex_names: list[str],
    s2_authors: list[dict[str, str]],
    s2_external: dict[str, dict[str, str | None]],
) -> list[AuthorRecord]:
    """Legacy merge helper — prefer Semantic Scholar names when available."""
    if s2_authors:
        return authors_from_s2_only(s2_authors)

    merged: list[AuthorRecord] = []
    for name in latex_names:
        merged.append(normalize_author_entry(name))
    return merged


def enrich_authors_from_latex_and_s2(
    arxiv_id: str,
    latex_names: list[str],
) -> list[AuthorRecord]:
    return resolve_paper_authors(arxiv_id, latex_names=latex_names)


def resolve_paper_authors(
    arxiv_id: str,
    *,
    latex_names: list[str] | None = None,
) -> list[AuthorRecord]:
    """Resolve authors with Semantic Scholar first, then arXiv API, then LaTeX."""
    try:
        s2_authors = fetch_paper_author_ids(arxiv_id)
        if s2_authors:
            return authors_from_s2_only(s2_authors)
    except Exception as exc:
        logger.warning("S2 author fetch failed for arXiv:%s: %s", arxiv_id, exc)

    try:
        from backend.llm_metadata import fetch_arxiv_authors

        arxiv_names = fetch_arxiv_authors(arxiv_id)
        if arxiv_names:
            return [normalize_author_entry(name) for name in arxiv_names]
    except Exception as exc:
        logger.debug("arXiv author fetch failed for arXiv:%s: %s", arxiv_id, exc)

    if latex_names:
        return [
            normalize_author_entry(name)
            for name in latex_names
            if str(name).strip() and not _looks_like_latex_author_fallback(name)
        ]
    return []


def _looks_like_latex_author_fallback(name: str) -> bool:
    from backend.text_cleanup import author_name_looks_broken

    return author_name_looks_broken(name)


def _resolve_authors(arxiv_id: str, storage) -> list[AuthorRecord]:
    latex_names: list[str] | None = None
    if storage.latex_dir.exists():
        from backend.llm_metadata import _extract_metadata_from_latex_cache

        latex_meta = _extract_metadata_from_latex_cache(storage.latex_dir)
        raw_names = latex_meta.get("authors")
        if isinstance(raw_names, list) and raw_names:
            latex_names = [str(name) for name in raw_names if str(name).strip()]

    return resolve_paper_authors(arxiv_id, latex_names=latex_names)


def _resolve_published_date(arxiv_id: str, ss_meta: dict[str, str]) -> str:
    published_date = str(ss_meta.get("published_date") or "").strip()
    if published_date:
        return published_date[:10]

    from backend.llm_metadata import fetch_arxiv_metadata

    arxiv_meta = fetch_arxiv_metadata(arxiv_id)
    published_date = str(arxiv_meta.get("published_date") or "").strip()
    if published_date:
        return published_date[:10]
    return _published_date_from_arxiv_id(arxiv_id)


def ensure_paper_metadata(arxiv_id: str) -> dict[str, bool]:
    """Fill published_date, venue, and authors on a Paper row when missing."""
    from backend.db import session_scope
    from backend.models import Paper
    from backend.paper_storage import PaperStorage

    filled = {"published_date": False, "venue": False, "authors": False}
    storage = PaperStorage(arxiv_id)

    # Read local state before asking S2. Publication date and a real venue are
    # stable once known, and author resolution does not need the metadata endpoint.
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            return filled
        need_date = not paper.published_date or len(paper.published_date) < 10
        need_venue = venue_needs_resolution(paper.venue)

    ss_meta = fetch_cached_paper_metadata(arxiv_id) if need_date or need_venue else {}

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            return filled

        metadata_updates: dict[str, object] = {}

        if need_date:
            resolved_date = _resolve_published_date(arxiv_id, ss_meta)
            if resolved_date:
                paper.published_date = resolved_date
                filled["published_date"] = True
                metadata_updates["published_date"] = resolved_date

        if need_venue:
            resolved_venue = resolve_paper_venue(arxiv_id, ss_meta)
            if resolved_venue:
                paper.venue = resolved_venue
                filled["venue"] = True
                metadata_updates["venue"] = paper.venue

        from backend.text_cleanup import authors_look_broken

        if not paper.authors or authors_look_broken(paper.authors):
            authors = _resolve_authors(arxiv_id, storage)
            if authors and not authors_look_broken(authors):
                paper.authors = authors
                filled["authors"] = True
                metadata_updates["authors"] = authors

        if metadata_updates:
            storage.update_metadata(metadata_updates)

    return filled


def papers_missing_metadata(arxiv_ids: list[str] | None = None) -> list[str]:
    """Return arXiv IDs whose Paper rows are missing date, venue, or authors."""
    from backend.db import init_db, session_scope
    from backend.models import Paper

    init_db()
    with session_scope() as session:
        query = session.query(Paper).filter(Paper.arxiv_id.isnot(None))
        if arxiv_ids is not None:
            query = query.filter(Paper.arxiv_id.in_(arxiv_ids))
        missing: list[str] = []
        for paper in query.all():
            if not paper.arxiv_id:
                continue
            if (
                not paper.published_date
                or len(paper.published_date) < 10
                or not paper.venue
                or venue_needs_resolution(paper.venue)
                or not paper.authors
            ):
                missing.append(paper.arxiv_id)
        return missing


def backfill_missing_paper_metadata(arxiv_ids: list[str] | None = None) -> dict[str, int]:
    """Ensure date, venue, and authors are populated for papers missing them."""
    targets = papers_missing_metadata(arxiv_ids)
    counts = {"processed": 0, "published_date": 0, "venue": 0, "authors": 0}
    for arxiv_id in targets:
        filled = ensure_paper_metadata(arxiv_id)
        counts["processed"] += 1
        for key in ("published_date", "venue", "authors"):
            if filled.get(key):
                counts[key] += 1
    return counts


__all__ = [
    "authors_from_s2_only",
    "backfill_missing_paper_metadata",
    "ensure_paper_metadata",
    "enrich_authors_from_latex_and_s2",
    "fetch_author_external_ids",
    "fetch_paper_author_ids",
    "fetch_paper_metadata",
    "fetch_paper_metadata_batch",
    "merge_latex_authors_with_s2",
    "resolve_paper_authors",
    "resolve_paper_venue",
]
