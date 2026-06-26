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
from backend.model_metadata import normalize_architecture_type

logger = logging.getLogger(__name__)


# ── Loading ───────────────────────────────────────────────────────────────────


_OVERRIDES_CACHE: dict[str, dict] = {}


def clear_overrides_cache() -> None:
    _OVERRIDES_CACHE.clear()


def load_overrides(arxiv_id: str, papers_root: Path | None = None) -> dict:
    """Read overrides.yaml for the given paper.

    Results are cached in memory for the duration of the process.
    Returns empty dict if the file does not exist or has no content.
    """
    cached = _OVERRIDES_CACHE.get(arxiv_id)
    if cached is not None:
        return cached

    root = (papers_root or cfg.papers_dir) / arxiv_id
    path = root / "overrides.yaml"
    if not path.exists():
        _OVERRIDES_CACHE[arxiv_id] = {}
        return {}
    try:
        content = path.read_text(encoding="utf-8")
        data = yaml.safe_load(content) or {}
        if not isinstance(data, dict):
            logger.warning("overrides.yaml for %s is not a mapping — ignoring", arxiv_id)
            _OVERRIDES_CACHE[arxiv_id] = {}
            return {}
        _OVERRIDES_CACHE[arxiv_id] = data
        return data
    except Exception as exc:
        logger.error("Failed to parse overrides.yaml for %s: %s", arxiv_id, exc)
        _OVERRIDES_CACHE[arxiv_id] = {}
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


def get_model_renames(overrides: dict) -> dict[str, str]:
    """Extract model_renames mapping (raw model name -> cleaned display name)."""
    mapping = overrides.get("model_renames") or {}
    return mapping if isinstance(mapping, dict) else {}


def get_model_metadata_overrides(overrides: dict) -> list[dict]:
    """Extract model_metadata_overrides list (params, architecture, external data)."""
    items = overrides.get("model_metadata_overrides") or []
    return items if isinstance(items, list) else []


def _build_model_metadata_map(items: list[Any]) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        name = str(item.get("model") or "").strip().lower()
        if name:
            mapping[name] = item
    return mapping


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

            if overrides.get("mark_all_as_baseline") and not result.is_baseline:
                result.is_baseline = 1
                changed = True

            if changed:
                affected += 1

        model_meta_map = _build_model_metadata_map(get_model_metadata_overrides(overrides))
        if model_meta_map:
            for result in results:
                model_name = (result.model.name if result.model else "").strip().lower()
                ov = model_meta_map.get(model_name)
                if not ov:
                    continue
                changed_meta = False
                if ov.get("params_millions") is not None:
                    result.params_millions = float(ov["params_millions"])
                    changed_meta = True
                if "uses_external_data" in ov:
                    ued = ov["uses_external_data"]
                    result.uses_external_data = 1 if ued is True else 0 if ued is False else None
                    changed_meta = True
                if result.model is not None:
                    model_type = normalize_architecture_type(ov.get("model_type"))
                    if model_type:
                        result.model.model_type = model_type
                        changed_meta = True
                if changed_meta:
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
