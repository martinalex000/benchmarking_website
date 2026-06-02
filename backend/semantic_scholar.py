"""Semantic Scholar Graph API helpers."""

from __future__ import annotations

import json
import logging
from typing import Any

import requests

from backend.config import cfg

logger = logging.getLogger(__name__)

_S2_BASE = "https://api.semanticscholar.org/graph/v1"
_S2_FIELDS = "title,abstract,year,publicationDate,venue,publicationVenue,journal,externalIds"


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
) -> dict[str, Any] | list[dict[str, Any]] | None:
    """Send a request to the Semantic Scholar API.

    For paper/*endpoints* use GET with *fields* as query params.
    For the batch endpoint /paper/batch *must* use POST with JSON body.
    """
    try:
        if is_batch:
            resp = requests.post(url, json=payload, headers=_s2_headers(), timeout=30)
        else:
            resp = requests.get(url, headers=_s2_headers(), params=payload, timeout=30)
        if resp.status_code == 429:
            logger.warning("Semantic Scholar rate-limited for %s", url)
            return None
        if resp.status_code >= 400:
            logger.debug("Semantic Scholar HTTP error %s for %s", resp.status_code, url)
            return None
        body = resp.text
    except requests.RequestException as exc:
        logger.debug("Semantic Scholar request failed for %s: %s", url, exc)
        return None
    return json.loads(body) if body else None


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

    venue = str(data.get("venue") or "").strip()
    if not venue:
        pub_venue = data.get("publicationVenue")
        if isinstance(pub_venue, dict):
            venue = str(pub_venue.get("name") or "").strip()
            if not venue:
                venue = str(pub_venue.get("venue") or "").strip()
        elif isinstance(pub_venue, str):
            venue = pub_venue.strip()
    if not venue:
        journal = data.get("journal")
        if isinstance(journal, dict):
            venue = str(journal.get("name") or "").strip()
        elif isinstance(journal, str):
            venue = journal.strip()
    if venue:
        meta["venue"] = venue
    return meta


def fetch_paper_metadata(arxiv_id: str) -> dict[str, str]:
    url = f"{_S2_BASE}/paper/ARXIV:{arxiv_id}"
    data = _s2_request(url, {"fields": _S2_FIELDS})
    return _paper_fields(data if isinstance(data, dict) else None)


def fetch_paper_metadata_batch(arxiv_ids: list[str]) -> dict[str, dict[str, str]]:
    """Fetch metadata individually for each arXiv ID.

    The /paper/batch endpoint only returns paperId + title for API keys
    without batch/Pro permissions, so we fall back to individual requests.
    """
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
