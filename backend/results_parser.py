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
from dataclasses import dataclass, field
from typing import Any

from thefuzz import fuzz as fuzz_lib
from thefuzz import process as fuzz_process

from backend.db import init_db, session_scope
from backend.method_name_audit import audit_extraction_payload

# Patterns like "(ours)", "(base)", "(baseline)" are author annotations, not part
# of the model name.  Strip them so "IPR-MPNN (ours)" and "IPR-MPNN" resolve to
# the same canonical model.
_ROLE_SUFFIX_RE = re.compile(
    r"\s*\(\s*(?:ours?|base(?:line)?|our\s+model|our\s+method|proposed)\s*\)\s*$",
    re.IGNORECASE,
)
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

# ── Metric normalisation ──────────────────────────────────────────────────────

# Metrics that should be in [0, 1] but are sometimes reported as percentages
# (e.g. 44.2 instead of 0.442).  Matched as a substring of the metric name,
# case-insensitively.  MAE/RMSE/loss intentionally excluded.
_PERCENTAGE_METRIC_SUBSTRINGS: tuple[str, ...] = (
    "accuracy",
    "acc",
    "f1",
    "ap",
    "auc",  # covers AUC, ROC-AUC, AUC-ROC
    "auroc",  # AUROC
    "mrr",
    "hits@",
)

_ZINC_SUBSET_ALIASES: tuple[str, ...] = (
    "zinc",
    "zinc subset",
    "zinc subset (12k)",
    "zinc 12k",
    "zinc-12k",
    "zinc12k",
)
_ZINC_FULL_ALIASES: tuple[str, ...] = (
    "zinc full",
    "full zinc",
    "zinc-full",
    "zinc 250k",
    "zinc full dataset",
)
_ZINC_SUBSET_CUE_RE = re.compile(
    r"(?:zinc[^\n]{0,120}(?:12k|12,000|12000|subset)|"
    r"(?:12k|12,000|12000)[^\n]{0,120}zinc|"
    r"benchmarking graph neural networks|"
    r"arxiv:?\s*2003\.00982)",
    re.IGNORECASE,
)
_ZINC_FULL_CUE_RE = re.compile(
    r"(?:zinc[^\n]{0,120}(?:249,456|249456|250,000|250000|full)|"
    r"(?:249,456|249456|250,000|250000)[^\n]{0,120}zinc|"
    r"tab[:_ -]*zinc[_ -]*full)",
    re.IGNORECASE,
)
_ZINC_FULL_MAX_MAE = 0.06
_ZINC_SUBSET_MIN_MAE = 0.07
# token_sort_ratio >= 88 matched the current model set well enough to reuse
# obvious variants like punctuation or spacing changes without collapsing short
# families such as GCN into unrelated names like GatedGCN.
_MODEL_FUZZY_MATCH_MIN_SCORE = 88


@dataclass
class ParseStoreSummary:
    arxiv_id: str
    extraction_model: str = "unknown"
    new_results: int = 0
    updated_results: int = 0
    skipped_unknown_datasets: list[str] = field(default_factory=list)
    skipped_invalid_values: list[str] = field(default_factory=list)
    created_models: list[str] = field(default_factory=list)
    created_stub_paper: bool = False
    metadata_changed: bool = False
    overrides_applied: int = 0
    quarantined: bool = False
    quarantine_reasons: list[str] = field(default_factory=list)
    quarantine_model_names: list[str] = field(default_factory=list)


def _is_percentage_metric(metric_name: str) -> bool:
    key = metric_name.strip().lower()
    return any(sub in key for sub in _PERCENTAGE_METRIC_SUBSTRINGS)


def normalize_percentage_metric(
    metric_name: str,
    value: float,
    std: float | None,
) -> tuple[float, float | None]:
    """Convert percentage-scale metrics from [0, 100] to [0, 1].

    If *value* > 1.0 and the metric is a known percentage-type metric,
    divides both value and std by 100.  Returns unchanged values otherwise.
    """
    if value <= 1.0 or not _is_percentage_metric(metric_name):
        return value, std
    if value > 100.0:
        logger.warning(
            "Metric %r value %.4f is outside [0, 100] — skipping normalisation",
            metric_name,
            value,
        )
        return value, std
    normalized = value / 100.0
    normalized_std = std / 100.0 if std is not None else None
    logger.debug(
        "Normalised %r: %.4f±%s → %.6f±%s",
        metric_name,
        value,
        std,
        normalized,
        normalized_std,
    )
    return normalized, normalized_std


def normalize_dataset_scaled_metric(
    dataset_name: str,
    metric_name: str,
    value: float,
    std: float | None,
) -> tuple[float, float | None]:
    """Correct known dataset-specific scale conventions omitted by extraction.

    Some papers report Peptides-struct MAE on a x100 scale while the benchmark
    leaderboard and the rest of the repo store the native decimal value.
    """
    dataset_key = dataset_name.strip().lower()
    metric_key = metric_name.strip().lower()
    if dataset_key == "peptides-struct" and metric_key == "mae" and value > 2.0:
        return value / 100.0, std / 100.0 if std is not None else None
    return value, std


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
    zinc_variants: dict[str, int] = {}
    for v in session.query(DatasetVariant).all():
        mapping[v.name.lower()] = v.id
        dataset_key = v.dataset.name.lower()
        mapping[dataset_key] = v.id
        if dataset_key == "zinc":
            variant_key = v.name.lower()
            zinc_variants[variant_key] = v.id
            mapping[f"zinc {variant_key}"] = v.id

    zinc_subset_id = zinc_variants.get("subset (12k)")
    zinc_full_id = zinc_variants.get("full")
    if zinc_subset_id is not None:
        for alias in _ZINC_SUBSET_ALIASES:
            mapping[alias] = zinc_subset_id
    if zinc_full_id is not None:
        for alias in _ZINC_FULL_ALIASES:
            mapping[alias] = zinc_full_id
    if zinc_subset_id is not None:
        mapping["zinc"] = zinc_subset_id
    elif zinc_full_id is not None:
        mapping["zinc"] = zinc_full_id
    return mapping


def _zinc_variant_id(kind: str, variant_map: dict[str, int]) -> int | None:
    if kind == "subset":
        return variant_map.get("zinc subset") or variant_map.get("subset (12k)")
    if kind == "full":
        return variant_map.get("zinc full") or variant_map.get("full")
    return None


def _collect_zinc_context(entry: dict[str, Any]) -> str:
    parts = [
        str(entry.get("dataset") or ""),
        str(entry.get("table_ref") or ""),
        str(entry.get("source_ref") or ""),
        str(entry.get("notes") or ""),
    ]
    return " ".join(part for part in parts if part).strip().lower()


def _extract_numeric_value(raw: Any) -> float | None:
    value, _std = parse_value_std(raw)
    return value


def _infer_zinc_variant(
    entry: dict[str, Any],
    variant_map: dict[str, int],
    paper_text: str | None = None,
) -> tuple[int | None, str]:
    context = _collect_zinc_context(entry)

    if _ZINC_FULL_CUE_RE.search(context):
        return _zinc_variant_id("full", variant_map), "zinc: entry cue matched full"
    if _ZINC_SUBSET_CUE_RE.search(context):
        return _zinc_variant_id("subset", variant_map), "zinc: entry cue matched subset"

    paper_text_lower = (paper_text or "").lower()
    if paper_text_lower:
        has_subset_cue = _ZINC_SUBSET_CUE_RE.search(paper_text_lower) is not None
        has_full_cue = _ZINC_FULL_CUE_RE.search(paper_text_lower) is not None
        if has_subset_cue and not has_full_cue:
            return _zinc_variant_id("subset", variant_map), "zinc: paper text matched subset"
        if has_full_cue and not has_subset_cue:
            return _zinc_variant_id("full", variant_map), "zinc: paper text matched full"

    metric_key = str(entry.get("metric") or "").strip().lower()
    if metric_key == "mae":
        value = _extract_numeric_value(entry.get("value"))
        if value is not None:
            if value <= _ZINC_FULL_MAX_MAE:
                return (
                    _zinc_variant_id("full", variant_map),
                    f"zinc: mae fallback <= {_ZINC_FULL_MAX_MAE:.2f}",
                )
            if value >= _ZINC_SUBSET_MIN_MAE:
                return (
                    _zinc_variant_id("subset", variant_map),
                    f"zinc: mae fallback >= {_ZINC_SUBSET_MIN_MAE:.2f}",
                )

    return _zinc_variant_id("subset", variant_map), "zinc: default subset fallback"


def resolve_dataset_variant_with_reason(
    dataset_name: str,
    session,
    variant_map: dict[str, int] | None = None,
    entry: dict[str, Any] | None = None,
    paper_text: str | None = None,
) -> tuple[int | None, str]:
    if variant_map is None:
        variant_map = _load_variant_map(session)

    key = dataset_name.strip().lower()

    if key == "zinc":
        return _infer_zinc_variant(entry or {"dataset": dataset_name}, variant_map, paper_text)

    if key in variant_map:
        return variant_map[key], "dataset: exact match"

    if variant_map:
        min_score = 85 if len(key) <= 6 else 75
        best_match, score = fuzz_process.extractOne(key, list(variant_map.keys()))
        if score >= min_score:
            logger.debug(
                "Fuzzy-matched dataset '%s' → '%s' (score=%d)", dataset_name, best_match, score
            )
            return variant_map[best_match], f"dataset: fuzzy match to {best_match} (score={score})"

    logger.warning("Could not resolve dataset variant '%s'", dataset_name)
    return None, "dataset: unresolved"


def resolve_dataset_variant(
    dataset_name: str,
    session,
    variant_map: dict[str, int] | None = None,
    entry: dict[str, Any] | None = None,
    paper_text: str | None = None,
) -> int | None:
    """Return the DatasetVariant.id best matching dataset_name.

    Falls back to thefuzz similarity (threshold 75%) if exact match fails.
    Returns None if no match found.
    """
    variant_id, _reason = resolve_dataset_variant_with_reason(
        dataset_name,
        session,
        variant_map,
        entry=entry,
        paper_text=paper_text,
    )
    return variant_id


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
) -> tuple[int, bool]:
    """Find or create a Model record. Returns ``(model_id, created_new)``."""
    # Strip author-role annotations before lookup/creation
    model_name = _ROLE_SUFFIX_RE.sub("", model_name).strip()
    key = model_name.strip().lower()

    if key in canonical_map:
        return canonical_map[key], False
    if key in alias_map:
        return alias_map[key], False

    # thefuzz against canonical names — use token_sort_ratio to avoid
    # partial-substring false positives (e.g. "GCN" ⊂ "GatedGCN" scores 90
    # with the default WRatio scorer because partial_ratio=100).
    all_names = list(canonical_map.keys()) + list(alias_map.keys())
    if all_names:
        best_match, score = fuzz_process.extractOne(
            key, all_names, scorer=fuzz_lib.token_sort_ratio
        )
        if score >= _MODEL_FUZZY_MATCH_MIN_SCORE:
            logger.debug(
                "Fuzzy-matched model '%s' → '%s' (score=%d)", model_name, best_match, score
            )
            match_id = canonical_map.get(best_match) or alias_map.get(best_match)
            if match_id:
                return match_id, False

    # Create new model
    new_model = Model(
        name=model_name.strip(),
        canonical_name=model_name.strip(),
    )
    session.add(new_model)
    session.flush()  # get the new id
    canonical_map[key] = new_model.id
    logger.info("Created new model: '%s' (id=%d)", model_name, new_model.id)
    return new_model.id, True


# ── Metadata enrichment ───────────────────────────────────────────────────────

# GitHub URLs to skip — known ML/graph libraries, not project repos
_GH_SKIP = re.compile(
    r"github\.com/(pytorch|pyg-team|dmlc|rusty1s|facebookresearch|google|"
    r"microsoft|openai|shelhamer|snap-stanford|benedekrozemberczki|"
    r"diningphil|asappresearch)/"
)


def _extract_github_url(text: str) -> str | None:
    """Return the first project-specific GitHub URL found in text, or None."""
    urls = re.findall(r"https?://github\.com/([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)", text)
    for path in urls:
        if not _GH_SKIP.search("github.com/" + path):
            return "https://github.com/" + path.rstrip("/.")
    return None


def _enrich_paper_metadata(arxiv_id: str, paper: Paper, storage: PaperStorage) -> bool:
    """Update Paper record with metadata from local caches, then arXiv API if needed."""
    before = (
        paper.title,
        paper.abstract,
        paper.published_date,
        json.dumps(paper.authors, ensure_ascii=False),
        paper.venue,
        paper.codebase_url,
    )
    metadata = storage.read_metadata()
    if metadata:
        if metadata.get("title"):
            paper.title = metadata["title"]
        if metadata.get("abstract"):
            paper.abstract = metadata["abstract"]
        if metadata.get("published_date") and not paper.published_date:
            paper.published_date = metadata["published_date"]
        if metadata.get("authors") and not paper.authors:
            paper.authors = metadata["authors"]
        if metadata.get("venue") and not paper.venue:
            paper.venue = metadata["venue"]
        if metadata.get("codebase_url") and not paper.codebase_url:
            paper.codebase_url = metadata["codebase_url"]

    from backend.llm_extractor import _title_looks_corrupted

    need_meta = not paper.abstract or _title_looks_corrupted(paper.title)

    if need_meta:
        # 1. Try local HTML — free, no rate limit
        if storage.html_index_path.exists():
            try:
                from backend.html_parser import parse_html_paper

                parsed = parse_html_paper(storage.html_index_path)
                if parsed.title and not _title_looks_corrupted(parsed.title):
                    paper.title = parsed.title
                if parsed.abstract:
                    paper.abstract = parsed.abstract
                need_meta = not paper.abstract or _title_looks_corrupted(paper.title)
            except Exception:
                pass

        # 2. Try cached LaTeX (expanded.tex)
        if need_meta and storage.latex_dir.exists():
            try:
                from backend.llm_extractor import _extract_metadata_from_latex_cache

                latex_meta = _extract_metadata_from_latex_cache(storage.latex_dir)
                if latex_meta.get("title"):
                    paper.title = latex_meta["title"]
                if latex_meta.get("abstract"):
                    paper.abstract = latex_meta["abstract"]
                need_meta = not paper.abstract or _title_looks_corrupted(paper.title)
            except Exception:
                pass

        # 3. Last resort: arXiv API
        if need_meta:
            from backend.llm_extractor import fetch_arxiv_metadata

            meta = fetch_arxiv_metadata(arxiv_id)
            if meta:
                if meta.get("title"):
                    paper.title = meta["title"]
                if meta.get("abstract"):
                    paper.abstract = meta["abstract"]
                if meta.get("published_date") and not paper.published_date:
                    paper.published_date = meta["published_date"]

    # Fallback: derive date from arXiv ID (e.g. 2206.08164 → 2022-06)
    if not paper.published_date:
        m = re.match(r"^(\d{2})(\d{2})\.\d+", arxiv_id)
        if m:
            year, month = int(m.group(1)) + 2000, int(m.group(2))
            if 1 <= month <= 12:
                paper.published_date = f"{year}-{month:02d}"

    # Extract GitHub codebase URL from paper text if not already set
    if not paper.codebase_url and storage.text_path.exists():
        text = storage.text_path.read_text(encoding="utf-8", errors="ignore")
        url = _extract_github_url(text)
        if url:
            paper.codebase_url = url
            logger.info("Set codebase_url=%s for arXiv:%s", url, arxiv_id)

    after = (
        paper.title,
        paper.abstract,
        paper.published_date,
        json.dumps(paper.authors, ensure_ascii=False),
        paper.venue,
        paper.codebase_url,
    )
    return before != after


# ── Main parser ───────────────────────────────────────────────────────────────


def parse_and_store_with_summary(arxiv_id: str) -> ParseStoreSummary:
    """Parse LLM output for a paper and report the side effects explicitly."""
    init_db()
    storage = PaperStorage(arxiv_id)
    summary = ParseStoreSummary(arxiv_id=arxiv_id)

    if not storage.llm_output_path.exists():
        logger.error("No LLM output found for arXiv:%s — run extractor first", arxiv_id)
        return summary

    raw = json.loads(storage.llm_output_path.read_text(encoding="utf-8"))
    extraction = raw.get("results", {})
    model_name_used = raw.get("model_used", "unknown")
    summary.extraction_model = model_name_used

    result_entries: list[dict] = extraction.get("results", [])
    proposed_model_info: dict = extraction.get("proposed_model") or {}
    baseline_models_info: list[dict] = extraction.get("baseline_models") or []

    if not result_entries:
        logger.warning("No result entries in LLM output for arXiv:%s", arxiv_id)
        return summary

    paper_text = ""
    if storage.text_path.exists():
        paper_text = storage.text_path.read_text(encoding="utf-8", errors="ignore")

    # Build a sizes lookup from baseline info
    sizes_lookup: dict[str, float | None] = {}
    if proposed_model_info.get("name"):
        sizes_lookup[proposed_model_info["name"].lower()] = proposed_model_info.get(
            "params_millions"
        )
    for bm in baseline_models_info:
        if bm.get("name"):
            sizes_lookup[bm["name"].lower()] = bm.get("params_millions")

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            logger.warning("Paper arXiv:%s not in DB — creating stub", arxiv_id)
            paper = Paper(
                arxiv_id=arxiv_id,
                title=f"arXiv:{arxiv_id}",
                extraction_status="downloaded",
                discovery_source="manual",
            )
            session.add(paper)
            session.flush()
            summary.created_stub_paper = True

        paper.extraction_model = model_name_used

        summary.metadata_changed = _enrich_paper_metadata(arxiv_id, paper, storage)

        overrides: dict[str, Any] = {}
        if storage.overrides_path.exists():
            try:
                import yaml

                overrides = yaml.safe_load(storage.overrides_path.read_text(encoding="utf-8")) or {}
            except Exception:
                overrides = {}

        finding = audit_extraction_payload(
            arxiv_id=arxiv_id,
            title=paper.title or f"arXiv:{arxiv_id}",
            results_payload=extraction,
            overrides=overrides,
        )
        if finding is not None:
            paper.extraction_status = "quarantined_method_name"
            summary.quarantined = True
            summary.quarantine_reasons = list(finding.reasons)
            summary.quarantine_model_names = [
                name for name in [finding.proposed_name, *finding.suspicious_result_names] if name
            ]
            logger.warning(
                "Quarantining arXiv:%s due to suspicious method names: %s",
                arxiv_id,
                "; ".join(finding.reasons),
            )
            return summary

        paper.extraction_status = "extracted"

        variant_map = _load_variant_map(session)
        canonical_map, alias_map = _load_model_map(session)

        for entry in result_entries:
            dataset_name = entry.get("dataset", "")
            model_name = entry.get("model", "")
            metric_name = entry.get("metric", "")

            variant_id, variant_reason = resolve_dataset_variant_with_reason(
                dataset_name,
                session,
                variant_map,
                entry=entry,
                paper_text=paper_text,
            )
            if variant_id is None:
                logger.warning(
                    "Skipping result (unknown dataset '%s') for arXiv:%s",
                    dataset_name,
                    arxiv_id,
                )
                if dataset_name and dataset_name not in summary.skipped_unknown_datasets:
                    summary.skipped_unknown_datasets.append(dataset_name)
                continue
            if dataset_name.strip().lower() == "zinc":
                logger.info(
                    "Resolved ZINC variant for arXiv:%s model=%s metric=%s via %s",
                    arxiv_id,
                    model_name,
                    metric_name,
                    variant_reason,
                )

            params = sizes_lookup.get(model_name.lower())
            model_id, created_model = resolve_or_create_model(
                model_name,
                is_proposed=entry.get("is_proposed", False),
                params_millions=params,
                session=session,
                canonical_map=canonical_map,
                alias_map=alias_map,
            )
            if created_model and model_name not in summary.created_models:
                summary.created_models.append(model_name)

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
                existing.variant_inference_reason = variant_reason
                summary.updated_results += 1
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
                summary.skipped_invalid_values.append(
                    f"{model_name} / {dataset_name} / {metric_name}"
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
                uses_external_data=(
                    1
                    if entry.get("uses_external_data") is True
                    else 0 if entry.get("uses_external_data") is False else None
                ),
                table_ref=entry.get("table_ref"),
                source_ref=entry.get("source_ref", "this paper"),
                extraction_model=model_name_used,
                variant_inference_reason=variant_reason,
            )
            session.add(result)
            summary.new_results += 1

    logger.info("Stored %d new Result rows for arXiv:%s", summary.new_results, arxiv_id)

    # Always re-apply overrides after inserting fresh results
    overridden = apply_overrides_to_db(arxiv_id)
    summary.overrides_applied = overridden
    if overridden:
        logger.info("Applied %d overrides for arXiv:%s", overridden, arxiv_id)

    return summary


def parse_and_store(arxiv_id: str) -> int:
    """Parse LLM output for a paper and write Result rows to DB.

    Returns number of new Result rows created.
    """
    return parse_and_store_with_summary(arxiv_id).new_results


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
    if value is not None:
        dataset_name = entry.get("dataset", "")
        metric_name = entry.get("metric", "")
        value, std = normalize_percentage_metric(metric_name, float(value), std)
        value, std = normalize_dataset_scaled_metric(dataset_name, metric_name, value, std)
    return value, std


def _update_result(result: Result, entry: dict, model_name_used: str) -> None:
    value, std = _parse_entry_value(entry)
    if value is not None:
        result.metric_value = value
    if std is not None:
        result.metric_std = std
    if "uses_external_data" in entry and result.uses_external_data is None:
        ued = entry["uses_external_data"]
        result.uses_external_data = 1 if ued is True else 0 if ued is False else None
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
