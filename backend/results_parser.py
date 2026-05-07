"""Results parser — converts LLM extraction output into DB records.

Handles:
  - Fuzzy dataset variant resolution (exact → thefuzz)
  - Model canonical name lookup + alias matching; creates new models if unseen
  - Numeric value normalisation ("mean±std", parenthetical std)
  - Skips rows where is_overridden=1 already exists in DB
  - Calls apply_overrides_to_db after writing new records

Usage::
    python -m backend.results_parser 2206.08164
"""

from __future__ import annotations

import argparse
import json
import logging
import re
from typing import Any

from thefuzz import process as fuzz_process

from backend.db import init_db, session_scope
from backend.models import (
    DatasetVariant,
    Model,
    ModelAlias,
    Paper,
    Result,
)
from backend.override_handler import apply_overrides_to_db
from backend.paper_storage import PaperStorage

logger = logging.getLogger(__name__)

# ── Value parsing ─────────────────────────────────────────────────────────────

_PLUSMINUS_RE = re.compile(r"([\d.]+)\s*[±]\s*([\d.]+)")
_PAREN_STD_RE = re.compile(r"([\d.]+)\s*\(\s*([\d.]+)\s*\)")
_PM_AFTER_RE = re.compile(r"([\d.]+)\s*±\s*([\d.]+)")


def parse_value_std(raw: Any) -> tuple[float | None, float | None]:
    """Parse a raw value into (value, std). Returns (None, None) on failure."""
    if raw is None:
        return None, None
    if isinstance(raw, (int, float)):
        return float(raw), None
    s = str(raw).strip()

    # "0.653 ± 0.004" or "0.653±0.004"
    m = _PM_AFTER_RE.search(s)
    if m:
        return float(m.group(1)), float(m.group(2))

    # "0.653 (0.004)"
    m = _PAREN_STD_RE.match(s)
    if m:
        return float(m.group(1)), float(m.group(2))

    # plain number
    try:
        return float(re.sub(r"[^\d.\-]", "", s)), None
    except (ValueError, TypeError):
        return None, None


# ── Dataset variant resolution ────────────────────────────────────────────────


def _load_variant_map(session) -> dict[str, int]:
    """Build {name.lower() → variant_id} for all variants + their dataset names."""
    mapping: dict[str, int] = {}
    for v in session.query(DatasetVariant).all():
        mapping[v.name.lower()] = v.id
        mapping[v.dataset.name.lower()] = v.id
    return mapping


def resolve_dataset_variant(
    dataset_name: str,
    session,
    variant_map: dict[str, int] | None = None,
) -> int | None:
    """Return the DatasetVariant.id best matching dataset_name.

    Falls back to thefuzz similarity (threshold 75%) if exact match fails.
    Returns None if no match found.
    """
    if variant_map is None:
        variant_map = _load_variant_map(session)

    key = dataset_name.strip().lower()

    # Exact match
    if key in variant_map:
        return variant_map[key]

    # thefuzz fallback
    if variant_map:
        best_match, score = fuzz_process.extractOne(key, list(variant_map.keys()))
        if score >= 75:
            logger.debug(
                "Fuzzy-matched dataset '%s' → '%s' (score=%d)", dataset_name, best_match, score
            )
            return variant_map[best_match]

    logger.warning("Could not resolve dataset variant '%s'", dataset_name)
    return None


# ── Model resolution ──────────────────────────────────────────────────────────


def _load_model_map(session) -> tuple[dict[str, int], dict[str, int]]:
    """Returns (canonical_map, alias_map) both keyed on lowercased name → model_id."""
    canonical: dict[str, int] = {}
    aliases: dict[str, int] = {}
    for m in session.query(Model).all():
        canonical[m.canonical_name.lower()] = m.id
    for a in session.query(ModelAlias).all():
        aliases[a.alias.lower()] = a.model_id
    return canonical, aliases


def resolve_or_create_model(
    model_name: str,
    is_proposed: bool,
    params_millions: float | None,
    session,
    canonical_map: dict[str, int],
    alias_map: dict[str, int],
) -> int:
    """Find or create a Model record. Returns model_id."""
    key = model_name.strip().lower()

    if key in canonical_map:
        return canonical_map[key]
    if key in alias_map:
        return alias_map[key]

    # thefuzz against canonical names
    all_names = list(canonical_map.keys()) + list(alias_map.keys())
    if all_names:
        best_match, score = fuzz_process.extractOne(key, all_names)
        if score >= 88:
            logger.debug(
                "Fuzzy-matched model '%s' → '%s' (score=%d)", model_name, best_match, score
            )
            match_id = canonical_map.get(best_match) or alias_map.get(best_match)
            if match_id:
                return match_id

    # Create new model
    new_model = Model(
        canonical_name=model_name.strip(),
        size_params=int(params_millions * 1_000_000) if params_millions else None,
    )
    session.add(new_model)
    session.flush()  # get the new id
    canonical_map[key] = new_model.id
    logger.info("Created new model: '%s' (id=%d)", model_name, new_model.id)
    return new_model.id


# ── Main parser ───────────────────────────────────────────────────────────────


def parse_and_store(arxiv_id: str) -> int:
    """Parse LLM output for a paper and write Result rows to DB.

    Returns number of new Result rows created.
    """
    init_db()
    storage = PaperStorage(arxiv_id)

    if not storage.llm_output_path.exists():
        logger.error("No LLM output found for arXiv:%s — run extractor first", arxiv_id)
        return 0

    raw = json.loads(storage.llm_output_path.read_text(encoding="utf-8"))
    extraction = raw.get("results", {})
    model_name_used = raw.get("model_used", "unknown")

    result_entries: list[dict] = extraction.get("results", [])
    proposed_model_info: dict = extraction.get("proposed_model") or {}
    baseline_models_info: list[dict] = extraction.get("baseline_models") or []

    if not result_entries:
        logger.warning("No result entries in LLM output for arXiv:%s", arxiv_id)
        return 0

    # Build a sizes lookup from baseline info
    sizes_lookup: dict[str, float | None] = {}
    if proposed_model_info.get("name"):
        sizes_lookup[proposed_model_info["name"].lower()] = proposed_model_info.get(
            "params_millions"
        )
    for bm in baseline_models_info:
        if bm.get("name"):
            sizes_lookup[bm["name"].lower()] = bm.get("params_millions")

    new_count = 0

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            logger.error("Paper arXiv:%s not in DB", arxiv_id)
            return 0

        variant_map = _load_variant_map(session)
        canonical_map, alias_map = _load_model_map(session)

        for entry in result_entries:
            dataset_name = entry.get("dataset", "")
            model_name = entry.get("model", "")
            metric_name = entry.get("metric", "")

            variant_id = resolve_dataset_variant(dataset_name, session, variant_map)
            if variant_id is None:
                logger.warning(
                    "Skipping result (unknown dataset '%s') for arXiv:%s",
                    dataset_name,
                    arxiv_id,
                )
                continue

            params = sizes_lookup.get(model_name.lower())
            model_id = resolve_or_create_model(
                model_name,
                is_proposed=entry.get("is_proposed", False),
                params_millions=params,
                session=session,
                canonical_map=canonical_map,
                alias_map=alias_map,
            )

            # Check for duplicate (same paper + variant + model + metric)
            existing = (
                session.query(Result)
                .filter_by(
                    paper_id=paper.id,
                    dataset_variant_id=variant_id,
                    model_id=model_id,
                    metric_name=metric_name,
                )
                .first()
            )
            if existing and existing.is_overridden:
                logger.debug(
                    "Skipping overridden result: %s / %s / %s",
                    model_name,
                    dataset_name,
                    metric_name,
                )
                continue
            if existing:
                # Update in-place
                _update_result(existing, entry, model_name_used)
                continue

            # Parse value/std
            value, std = _parse_entry_value(entry)
            if value is None:
                logger.warning(
                    "Could not parse value for %s / %s / %s — skipping",
                    model_name,
                    dataset_name,
                    metric_name,
                )
                continue

            result = Result(
                paper_id=paper.id,
                dataset_variant_id=variant_id,
                model_id=model_id,
                metric_name=metric_name,
                metric_value=value,
                metric_std=std,
                higher_is_better=entry.get("higher_is_better", True),
                is_baseline=not entry.get("is_proposed", False),
                table_ref=entry.get("table_ref"),
                source_ref=entry.get("source_ref", "this paper"),
                extraction_model=model_name_used,
            )
            session.add(result)
            new_count += 1

    logger.info("Stored %d new Result rows for arXiv:%s", new_count, arxiv_id)

    # Always re-apply overrides after inserting fresh results
    overridden = apply_overrides_to_db(arxiv_id)
    if overridden:
        logger.info("Applied %d overrides for arXiv:%s", overridden, arxiv_id)

    return new_count


def _parse_entry_value(entry: dict) -> tuple[float | None, float | None]:
    value = entry.get("value")
    std = entry.get("std")
    if isinstance(value, str):
        value, parsed_std = parse_value_std(value)
        if std is None:
            std = parsed_std
    if std is not None:
        try:
            std = float(std)
        except (TypeError, ValueError):
            std = None
    return value, std


def _update_result(result: Result, entry: dict, model_name_used: str) -> None:
    value, std = _parse_entry_value(entry)
    if value is not None:
        result.metric_value = value
    if std is not None:
        result.metric_std = std
    result.extraction_model = model_name_used


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Parse LLM output and store results in the DB")
    p.add_argument("arxiv_ids", nargs="+", metavar="ARXIV_ID")
    return p


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)

    total_new = 0
    for arxiv_id in args.arxiv_ids:
        arxiv_id = arxiv_id.strip().lstrip("arXiv:").split("v")[0]
        total_new += parse_and_store(arxiv_id)

    print(f"Total new Result rows created: {total_new}")


if __name__ == "__main__":
    main()
