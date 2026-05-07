"""Override handler — loads and applies per-paper human corrections.

All corrections live in  papers/{arxiv_id}/overrides.yaml  which is
tracked in git and NEVER overwritten by the pipeline.

The pipeline calls apply_overrides() after every extraction run.
Overridden results in the DB cannot be re-extracted (is_overridden=1 guard).
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import yaml

from backend.config import cfg

logger = logging.getLogger(__name__)


# ── Loading ───────────────────────────────────────────────────────────────────

def load_overrides(arxiv_id: str, papers_root: Path | None = None) -> dict:
    """Read overrides.yaml for the given paper.

    Returns empty dict if the file does not exist or has no content.
    """
    root = (papers_root or cfg.papers_dir) / arxiv_id
    path = root / "overrides.yaml"
    if not path.exists():
        return {}
    try:
        content = path.read_text(encoding="utf-8")
        data = yaml.safe_load(content) or {}
        if not isinstance(data, dict):
            logger.warning("overrides.yaml for %s is not a mapping — ignoring", arxiv_id)
            return {}
        return data
    except Exception as exc:
        logger.error("Failed to parse overrides.yaml for %s: %s", arxiv_id, exc)
        return {}


# ── Application ───────────────────────────────────────────────────────────────

def apply_overrides_to_results(
    results: list[dict],
    overrides: dict,
    override_source: str = "",
) -> list[dict]:
    """Apply overrides to a list of result dicts (in-place modifications).

    Each result dict is expected to have keys:
      model, dataset, metric, value, std, is_baseline, is_proposed
    """
    if not overrides:
        return results

    # Build lookup maps
    problematic_set = _build_lookup(overrides.get("problematic_results", []))
    override_map = _build_override_map(overrides.get("result_overrides", []))

    for r in results:
        key = _result_key(r.get("model", ""), r.get("dataset", ""), r.get("metric", ""))

        if key in problematic_set:
            r["is_problematic"] = True
            r["problematic_reason"] = problematic_set[key]

        if key in override_map:
            ov = override_map[key]
            r["is_overridden"] = True
            r["override_value"] = ov.get("correct_value")
            r["override_std"] = ov.get("correct_std")
            r["override_reason"] = ov.get("reason", "")
            r["override_source"] = override_source

    return results


def get_metadata_overrides(overrides: dict) -> dict:
    """Extract metadata_overrides dict (codebase_url, etc.)."""
    return overrides.get("metadata_overrides") or {}


def get_split_notes(overrides: dict) -> list[dict]:
    """Extract dataset_split_notes list."""
    return overrides.get("dataset_split_notes") or []


# ── DB application ────────────────────────────────────────────────────────────

def apply_overrides_to_db(arxiv_id: str) -> int:
    """Load overrides.yaml and update matching Result rows in the database.

    Returns number of rows affected.
    """
    from backend.db import session_scope
    from backend.models import Paper, Result

    overrides = load_overrides(arxiv_id)
    if not overrides:
        return 0

    override_source = str(cfg.papers_dir / arxiv_id / "overrides.yaml")
    problematic_set = _build_lookup(overrides.get("problematic_results", []))
    override_map = _build_override_map(overrides.get("result_overrides", []))

    affected = 0

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            logger.warning("Paper arXiv:%s not found in DB — cannot apply overrides", arxiv_id)
            return 0

        results = session.query(Result).filter_by(paper_id=paper.id).all()

        for result in results:
            key = _result_key(
                result.model.name if result.model else "",
                result.dataset_variant.dataset.name if result.dataset_variant else "",
                result.metric_name,
            )

            changed = False

            if key in problematic_set:
                result.is_problematic = 1
                result.problematic_reason = problematic_set[key]
                changed = True

            if key in override_map:
                ov = override_map[key]
                result.is_overridden = 1
                result.override_value = ov.get("correct_value")
                result.override_std = ov.get("correct_std")
                result.override_reason = ov.get("reason", "")
                result.override_source = override_source
                changed = True

            if changed:
                affected += 1

        # Apply metadata overrides to the paper itself
        meta_ov = get_metadata_overrides(overrides)
        if meta_ov.get("codebase_url") and not paper.codebase_url:
            paper.codebase_url = meta_ov["codebase_url"]

    logger.info("Applied overrides for arXiv:%s — %d results affected", arxiv_id, affected)
    return affected


# ── Helpers ───────────────────────────────────────────────────────────────────

def _result_key(model: str, dataset: str, metric: str) -> tuple[str, str, str]:
    return model.strip().lower(), dataset.strip().lower(), metric.strip().lower()


def _build_lookup(items: list[Any]) -> dict[tuple, str]:
    """Build a {(model, dataset, metric) → reason} dict from a list of dicts."""
    result: dict[tuple, str] = {}
    if not isinstance(items, list):
        return result
    for item in items:
        if not isinstance(item, dict):
            continue
        key = _result_key(
            item.get("model", ""),
            item.get("dataset", ""),
            item.get("metric", ""),
        )
        result[key] = item.get("reason", "")
    return result


def _build_override_map(items: list[Any]) -> dict[tuple, dict]:
    """Build a {(model, dataset, metric) → override_dict} map."""
    result: dict[tuple, dict] = {}
    if not isinstance(items, list):
        return result
    for item in items:
        if not isinstance(item, dict):
            continue
        key = _result_key(
            item.get("model", ""),
            item.get("dataset", ""),
            item.get("metric", ""),
        )
        result[key] = item
    return result
