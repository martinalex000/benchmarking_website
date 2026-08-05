"""Persist unresolved dataset observations from extraction discovery."""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from typing import Any

from backend.dataset_discovery import classify_dataset_infos, discovery_payload
from backend.db import init_db, session_scope
from backend.llm_types import DatasetInfo
from backend.models import Paper, PendingDataset

logger = logging.getLogger(__name__)


def _discovered_infos(raw_output: dict[str, Any]) -> list[DatasetInfo]:
    results = raw_output.get("results") or {}
    if not isinstance(results, dict):
        return []
    infos: list[DatasetInfo] = []
    for value in results.get("discovered_datasets") or []:
        try:
            infos.append(
                DatasetInfo.model_validate(value if isinstance(value, dict) else {"name": value})
            )
        except (TypeError, ValueError) as exc:
            logger.warning("Ignoring malformed discovered dataset payload: %s", exc)
    return infos


def collect_pending_datasets(arxiv_id: str, raw_output: dict[str, Any]) -> int:
    """Upsert unresolved discovery observations without making an LLM request."""
    infos = _discovered_infos(raw_output)
    if not infos:
        return 0

    init_db()
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        title = paper.title if paper else raw_output.get("paper_title") or f"arXiv:{arxiv_id}"
        resolutions = classify_dataset_infos(session, infos, arxiv_id=arxiv_id)
        unresolved = [
            resolution
            for resolution in resolutions
            if resolution.status in {"unknown_dataset", "unknown_variant"}
        ]
        for resolution in unresolved:
            info = resolution.dataset_info
            row = (
                session.query(PendingDataset)
                .filter_by(arxiv_id=arxiv_id, dataset_name=info.name)
                .first()
            )
            if row is None:
                row = PendingDataset(arxiv_id=arxiv_id, dataset_name=info.name)
                session.add(row)
            row.paper_title = title
            row.metrics_seen_list = list(
                info.metrics_seen or ([info.primary_metric] if info.primary_metric else [])
            )
            row.discovery_payload = discovery_payload(info)
            row.updated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
            # Human review status, resolved assignment, and legacy suggestion
            # are intentionally left untouched on repeated observations.
        return len(unresolved)


def discovery_payload_dict(row: PendingDataset) -> dict[str, Any]:
    """Read a pending row's new payload, with a safe legacy fallback."""
    payload = row.discovery_payload_obj
    if payload:
        return payload
    return {
        "name": row.dataset_name,
        "metrics_seen": row.metrics_seen_list,
    }
