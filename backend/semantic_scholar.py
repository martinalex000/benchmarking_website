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
    url: str, payload: dict[str, Any] | None = None
) -> dict[str, Any] | list[dict[str, Any]] | None:
    try:
        resp = (
            requests.post(url, json=payload, headers=_s2_headers(), timeout=30)
            if payload is not None
            else requests.get(url, headers=_s2_headers(), timeout=30)
        )
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
    ids = [f"ARXIV:{arxiv_id}" for arxiv_id in arxiv_ids if arxiv_id.strip()]
    if not ids:
        return {}
    url = f"{_S2_BASE}/paper/batch"
    payload = {"ids": ids, "fields": _S2_FIELDS}
    data = _s2_request(url, payload)
    results: dict[str, dict[str, str]] = {}
    if not isinstance(data, list):
        return results
    for arxiv_id, paper in zip(arxiv_ids, data, strict=False):
        meta = _paper_fields(paper)
        if meta:
            results[arxiv_id] = meta
    return results
