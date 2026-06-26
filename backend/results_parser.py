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
import contextlib
import json
import logging

import yaml
import re
from dataclasses import dataclass, field
from typing import Any

from thefuzz import fuzz as fuzz_lib
from thefuzz import process as fuzz_process

from backend.config import cfg, normalize_arxiv_id
from backend.db import init_db, session_scope
from backend.method_name_audit import audit_extraction_payload
from backend.model_metadata import normalize_architecture_type
from backend.model_metadata_defaults import load_model_metadata_defaults, lookup_model_type
from backend.model_name_resolution import (
    ROLE_SUFFIX_RE,
    model_names_fuzzy_compatible,
    normalize_model_name_for_resolution,
    ogb_dataset_families_compatible,
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
from backend.qm9_targets import is_qm9_dataset, normalize_qm9_metric
from backend.repository_linking import find_verified_repository_link, repository_source_from_storage
from backend.text_cleanup import abstract_has_latex_artifacts, authors_look_broken, clean_extracted_text

logger = logging.getLogger(__name__)

# ── Dataset alias normalisation (post-extraction) ─────────────────────────────

_DATASET_ALIAS_MAP: dict[str, str] | None = None


def _load_dataset_alias_map() -> dict[str, str]:
    """Load the user-facing alias map from ``config/dataset_aliases.yaml``."""
    global _DATASET_ALIAS_MAP
    if _DATASET_ALIAS_MAP is None:
        path = cfg.config_dir / "dataset_aliases.yaml"
        if path.exists():
            with path.open(encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
            raw = data.get("aliases", {})
            _DATASET_ALIAS_MAP = {k.strip().lower(): v.strip() for k, v in raw.items()}
        else:
            _DATASET_ALIAS_MAP = {}
    return _DATASET_ALIAS_MAP


def normalize_dataset_alias(dataset_name: str) -> str:
    """Return the canonical dataset name if an alias is defined, else unchanged."""
    key = dataset_name.strip().lower()
    return _load_dataset_alias_map().get(key, dataset_name)


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

_OGB_DATASET_ALIASES: dict[str, str] = {
    "ogbg-code2": "code",
    "ogbg-code": "code",
    "ogbg-moltox21": "tox21",
}

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
    for alias, canonical in _OGB_DATASET_ALIASES.items():
        target = mapping.get(canonical)
        if target is not None:
            mapping[alias] = target
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

    alias_target = _OGB_DATASET_ALIASES.get(key)
    if alias_target is not None and alias_target in variant_map:
        return variant_map[alias_target], f"dataset: alias to {alias_target}"

    if variant_map:
        min_score = 85 if len(key) <= 6 else 75
        best_match, score = fuzz_process.extractOne(
            key,
            list(variant_map.keys()),
            scorer=fuzz_lib.token_sort_ratio,
        )
        if score >= min_score and ogb_dataset_families_compatible(key, best_match):
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


def _build_metadata_lookups(
    extraction: dict[str, Any],
    model_sizes: list[Any] | None = None,
) -> tuple[dict[str, float | None], dict[str, str | None]]:
    """Build paper-local parameter and architecture lookups keyed by lowercased model name."""
    sizes_lookup: dict[str, float | None] = {}
    type_lookup: dict[str, str | None] = {}

    def _add(name: str | None, params: Any, model_type: Any) -> None:
        if not name:
            return
        key = name.strip().lower()
        if params is not None:
            with contextlib.suppress(TypeError, ValueError):
                sizes_lookup[key] = float(params)
        normalized_type = normalize_architecture_type(
            str(model_type) if model_type is not None else None
        )
        if normalized_type is not None:
            type_lookup[key] = normalized_type

    proposed = extraction.get("proposed_model") or {}
    if isinstance(proposed, dict):
        _add(proposed.get("name"), proposed.get("params_millions"), proposed.get("model_type"))

    for baseline in extraction.get("baseline_models") or []:
        if isinstance(baseline, dict):
            _add(baseline.get("name"), baseline.get("params_millions"), baseline.get("model_type"))

    for item in model_sizes or []:
        if not isinstance(item, dict):
            continue
        name = item.get("matched_result_name") or item.get("model_name")
        _add(name, item.get("params_millions"), None)

    return sizes_lookup, type_lookup


def _update_model_metadata(model: Model, model_type: str | None) -> None:
    normalized_type = normalize_architecture_type(model_type)
    if normalized_type and not model.model_type:
        model.model_type = normalized_type


def _register_model_alias(
    session,
    alias_map: dict[str, int],
    model_id: int,
    alias: str,
) -> None:
    alias_clean = re.sub(r"\s+", " ", alias).strip()
    alias_key = alias_clean.lower()
    if not alias_key or alias_key in alias_map:
        return
    existing = session.query(ModelAlias).filter_by(alias=alias_clean).first()
    if existing is not None:
        alias_map[alias_key] = existing.model_id
        return
    session.add(ModelAlias(model_id=model_id, alias=alias_clean))
    session.flush()
    alias_map[alias_key] = model_id


def resolve_or_create_model(
    model_name: str,
    is_proposed: bool,
    model_type: str | None,
    session,
    canonical_map: dict[str, int],
    alias_map: dict[str, int],
) -> tuple[int, bool]:
    """Find or create a Model record. Returns ``(model_id, created_new)``."""
    raw_name = ROLE_SUFFIX_RE.sub("", model_name).strip()
    normalized = normalize_model_name_for_resolution(raw_name)
    key = normalized.lower()

    if key in canonical_map:
        model = session.query(Model).filter_by(id=canonical_map[key]).first()
        if model is not None:
            _update_model_metadata(model, model_type)
        if raw_name.lower() != key:
            _register_model_alias(session, alias_map, canonical_map[key], raw_name)
        return canonical_map[key], False
    if key in alias_map:
        model = session.query(Model).filter_by(id=alias_map[key]).first()
        if model is not None:
            _update_model_metadata(model, model_type)
        return alias_map[key], False

    # thefuzz against canonical names — use token_sort_ratio to avoid
    # partial-substring false positives (e.g. "GCN" ⊂ "GatedGCN" scores 90
    # with the default WRatio scorer because partial_ratio=100).
    all_names = list(canonical_map.keys()) + list(alias_map.keys())
    if all_names:
        best_match, score = fuzz_process.extractOne(
            key, all_names, scorer=fuzz_lib.token_sort_ratio
        )
        if model_names_fuzzy_compatible(
            normalized, best_match, score, _MODEL_FUZZY_MATCH_MIN_SCORE
        ):
            logger.debug(
                "Fuzzy-matched model '%s' → '%s' (score=%d)", normalized, best_match, score
            )
            match_id = canonical_map.get(best_match) or alias_map.get(best_match)
            if match_id:
                model = session.query(Model).filter_by(id=match_id).first()
                if model is not None:
                    _update_model_metadata(model, model_type)
                if raw_name.lower() != best_match:
                    _register_model_alias(session, alias_map, match_id, raw_name)
                return match_id, False

    # Create new model
    new_model = Model(
        name=normalized,
        canonical_name=normalized,
    )
    _update_model_metadata(new_model, model_type)
    session.add(new_model)
    session.flush()  # get the new id
    canonical_map[key] = new_model.id
    if raw_name.lower() != key:
        _register_model_alias(session, alias_map, new_model.id, raw_name)
    logger.info("Created new model: '%s' (id=%d)", normalized, new_model.id)
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


def _apply_remote_metadata(paper: Paper, meta: dict[str, str]) -> bool:
    """Apply title/abstract/date/venue from a metadata dict. Returns True if abstract changed."""
    abstract_changed = False
    if meta.get("title"):
        paper.title = meta["title"]
    if meta.get("abstract"):
        paper.abstract = meta["abstract"]
        abstract_changed = True
    if meta.get("published_date") and not paper.published_date:
        paper.published_date = meta["published_date"]
    if meta.get("venue") and not paper.venue:
        paper.venue = meta["venue"]
    return abstract_changed


def _enrich_paper_metadata(arxiv_id: str, paper: Paper, storage: PaperStorage) -> bool:
    """Update Paper record from local caches, Semantic Scholar, then arXiv API if needed."""
    abstract_has_artifacts = abstract_has_latex_artifacts(paper.abstract)
    paper.abstract = clean_extracted_text(paper.abstract)
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
            raw_abstract = metadata["abstract"]
            abstract_has_artifacts = abstract_has_artifacts or abstract_has_latex_artifacts(
                raw_abstract
            )
            paper.abstract = clean_extracted_text(raw_abstract)
        if metadata.get("published_date") and not paper.published_date:
            paper.published_date = metadata["published_date"]
        if metadata.get("authors") and not paper.authors:
            from backend.models import author_display_name, normalize_author_entry

            normalized_authors = [
                normalize_author_entry(entry)
                for entry in metadata["authors"]
                if author_display_name(entry)
            ]
            if normalized_authors and not authors_look_broken(normalized_authors):
                paper.authors = normalized_authors
        if metadata.get("venue") and not paper.venue:
            paper.venue = metadata["venue"]
        if metadata.get("codebase_url") and not paper.codebase_url:
            paper.codebase_url = metadata["codebase_url"]
        repo_meta = metadata.get("repository")
        if isinstance(repo_meta, dict) and repo_meta.get("verified_url") and not paper.codebase_url:
            paper.codebase_url = str(repo_meta["verified_url"]).strip()

    if not paper.codebase_url and storage.llm_output_path.exists():
        try:
            raw_output = storage.load_llm_output()
            repository = raw_output.get("repository")
            if isinstance(repository, dict) and repository.get("verified_url"):
                paper.codebase_url = str(repository["verified_url"]).strip()
        except (ValueError, OSError):
            pass

    from backend.llm_extractor import _title_looks_corrupted

    need_meta = not paper.abstract or abstract_has_artifacts or _title_looks_corrupted(paper.title)

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
                    abstract_has_artifacts = abstract_has_latex_artifacts(parsed.abstract)
                need_meta = (
                    not paper.abstract
                    or abstract_has_artifacts
                    or _title_looks_corrupted(paper.title)
                )
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
                    abstract_has_artifacts = abstract_has_latex_artifacts(latex_meta["abstract"])
                need_meta = (
                    not paper.abstract
                    or abstract_has_artifacts
                    or _title_looks_corrupted(paper.title)
                )
            except Exception:
                pass

    need_daily_date = not paper.published_date or len(paper.published_date) < 10
    need_venue = not paper.venue
    if need_meta or need_daily_date or need_venue:
        from backend.semantic_scholar import fetch_paper_metadata

        ss_meta = fetch_paper_metadata(arxiv_id)
        if ss_meta:
            selective_meta = {
                key: value
                for key, value in ss_meta.items()
                if (
                    (key in {"title", "abstract"} and need_meta)
                    or (key == "published_date" and need_daily_date)
                    or (key == "venue" and need_venue)
                )
            }
            if selective_meta and _apply_remote_metadata(paper, selective_meta):
                abstract_has_artifacts = abstract_has_latex_artifacts(paper.abstract)
            need_meta = (
                not paper.abstract or abstract_has_artifacts or _title_looks_corrupted(paper.title)
            )
            need_daily_date = not paper.published_date or len(paper.published_date) < 10
            need_venue = not paper.venue
            storage.update_metadata(
                {
                    **({"published_date": paper.published_date} if paper.published_date else {}),
                    **({"venue": paper.venue} if paper.venue else {}),
                }
            )

        # arXiv Atom API when date/abstract still missing after Semantic Scholar.
        if (need_meta or need_daily_date) and (
            not cfg.semantic_scholar_api_key or need_daily_date
        ):
            from backend.llm_extractor import fetch_arxiv_metadata

            meta = fetch_arxiv_metadata(arxiv_id)
            if meta:
                selective_meta = {
                    key: value
                    for key, value in meta.items()
                    if (
                        (key in {"title", "abstract"} and need_meta)
                        or (key == "published_date" and need_daily_date)
                    )
                }
                if selective_meta and _apply_remote_metadata(paper, selective_meta):
                    abstract_has_artifacts = abstract_has_latex_artifacts(paper.abstract)
                need_meta = (
                    not paper.abstract
                    or abstract_has_artifacts
                    or _title_looks_corrupted(paper.title)
                )
                need_daily_date = not paper.published_date or len(paper.published_date) < 10
                storage.update_metadata(
                    {
                        **(
                            {"published_date": paper.published_date}
                            if paper.published_date
                            else {}
                        ),
                    }
                )

    # Fallback: derive date from arXiv ID (e.g. 2206.08164 → 2022-06)
    if not paper.published_date:
        m = re.match(r"^(\d{2})(\d{2})\.\d+", arxiv_id)
        if m:
            year, month = int(m.group(1)) + 2000, int(m.group(2))
            if 1 <= month <= 12:
                paper.published_date = f"{year}-{month:02d}"

    # Extract GitHub codebase URL from paper text if not already set
    if not paper.codebase_url:
        repo_source_text, repo_source_kind = repository_source_from_storage(storage)
        if repo_source_text:
            try:
                from backend.llm_extractor import LLMExtractor

                verifier = (
                    LLMExtractor(model_tier="small")
                    if cfg.llm_endpoint and cfg.llm_api_key
                    else None
                )
                repository = find_verified_repository_link(
                    llm_verifier=verifier,
                    arxiv_id=arxiv_id,
                    paper_title=paper.title or "",
                    paper_abstract=paper.abstract or "",
                    source_text=repo_source_text,
                    source_kind=repo_source_kind,
                )
                if repository.get("verified_url"):
                    paper.codebase_url = str(repository["verified_url"]).strip()
                    storage.update_metadata(
                        {
                            "codebase_url": paper.codebase_url,
                            "repository": repository,
                        }
                    )
                    logger.info(
                        "Set verified codebase_url=%s for arXiv:%s", paper.codebase_url, arxiv_id
                    )
            except Exception as exc:
                logger.warning("Verified repo extraction failed for arXiv:%s: %s", arxiv_id, exc)

    if not paper.codebase_url and storage.text_path.exists():
        text = storage.text_path.read_text(encoding="utf-8", errors="ignore")
        url = _extract_github_url(text)
        if url:
            paper.codebase_url = url
            logger.info("Set heuristic codebase_url=%s for arXiv:%s", url, arxiv_id)

    if not paper.authors or authors_look_broken(paper.authors):
        try:
            from backend.semantic_scholar import resolve_paper_authors

            latex_names: list[str] | None = None
            if storage.latex_dir.exists():
                from backend.llm_extractor import _extract_metadata_from_latex_cache

                latex_meta = _extract_metadata_from_latex_cache(storage.latex_dir)
                raw_names = latex_meta.get("authors")
                if isinstance(raw_names, list) and raw_names:
                    latex_names = [str(name) for name in raw_names if str(name).strip()]

            resolved_authors = resolve_paper_authors(arxiv_id, latex_names=latex_names)
            if resolved_authors and not authors_look_broken(resolved_authors):
                paper.authors = resolved_authors
                storage.update_metadata({"authors": paper.authors})
        except Exception as exc:
            logger.debug("Author extraction failed for arXiv:%s: %s", arxiv_id, exc)

    after = (
        paper.title,
        paper.abstract,
        paper.published_date,
        json.dumps(paper.authors, ensure_ascii=False),
        paper.venue,
        paper.codebase_url,
    )
    return before != after


# Extraction call types whose parse failures should not block DB ingest.
_NON_FATAL_EXTRACT_CALL_PREFIXES: tuple[str, ...] = ("extract_dataset_statistics",)


def _is_fatal_extraction_parse_failure(entry: str) -> bool:
    call_type = entry.split(":", 1)[0].strip()
    if not call_type.startswith("extract_"):
        return False
    return not any(
        call_type == prefix or call_type.startswith(f"{prefix}:")
        for prefix in _NON_FATAL_EXTRACT_CALL_PREFIXES
    )


def parse_and_store_with_summary(arxiv_id: str) -> ParseStoreSummary:
    """Parse LLM output for a paper and report the side effects explicitly."""
    init_db()
    storage = PaperStorage(arxiv_id)
    summary = ParseStoreSummary(arxiv_id=arxiv_id)

    if not storage.llm_output_path.exists():
        logger.error("No LLM output found for arXiv:%s — run extractor first", arxiv_id)
        return summary

    raw = storage.load_llm_output()
    extraction = raw.get("results", {})
    model_name_used = raw.get("model_used", "unknown")
    summary.extraction_model = model_name_used

    call_log = storage.load_llm_calls()
    parse_failures: list[str] = []
    for call in call_log:
        if not isinstance(call, dict):
            continue
        call_type = str(call.get("call_type") or "")
        parse_error = str(call.get("parse_error") or "").strip()
        if parse_error and (
            call_type.startswith("extract_") or call_type.startswith("extract_dataset")
        ):
            parse_failures.append(f"{call_type}: {parse_error}")

    result_entries: list[dict] = extraction.get("results", [])
    fatal_parse_failures = [f for f in parse_failures if _is_fatal_extraction_parse_failure(f)]

    if fatal_parse_failures and not result_entries:
        with session_scope() as session:
            paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
            if paper is None:
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
            paper.extraction_status = "quarantined_yaml_parse"

        summary.quarantined = True
        summary.quarantine_reasons = fatal_parse_failures[:5]
        logger.warning(
            "Quarantining arXiv:%s due to structured YAML parse failure(s): %s",
            arxiv_id,
            "; ".join(fatal_parse_failures[:2]),
        )
        return summary

    if fatal_parse_failures and result_entries:
        logger.warning(
            "Ignoring non-fatal extraction parse failure(s) for arXiv:%s because "
            "%d result row(s) were recovered: %s",
            arxiv_id,
            len(result_entries),
            "; ".join(fatal_parse_failures[:2]),
        )

    if not result_entries:
        logger.warning("No result entries in LLM output for arXiv:%s", arxiv_id)
        return summary

    paper_text = ""
    if storage.text_path.exists():
        paper_text = storage.text_path.read_text(encoding="utf-8", errors="ignore")

    # Build a sizes lookup from baseline info
    sizes_lookup, type_lookup = _build_metadata_lookups(
        extraction,
        model_sizes=raw.get("model_sizes"),
    )
    metadata_defaults = load_model_metadata_defaults()

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
            except (yaml.YAMLError, OSError) as exc:
                logger.error("Failed to load overrides for %s: %s", arxiv_id, exc)
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
            dataset_name = normalize_dataset_alias(entry.get("dataset", ""))
            model_name = entry.get("model", "")
            metric_name = entry.get("metric", "")
            if is_qm9_dataset(dataset_name):
                normalized_target = normalize_qm9_metric(metric_name)
                if normalized_target is None:
                    logger.warning(
                        "Skipping QM9 result with unknown target metric %r for arXiv:%s model=%s",
                        metric_name,
                        arxiv_id,
                        model_name,
                    )
                    summary.skipped_invalid_values.append(
                        f"{model_name} / {dataset_name} / {metric_name} (unknown QM9 target)"
                    )
                    continue
                metric_name = normalized_target

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
            model_type = lookup_model_type(
                model_name,
                type_lookup,
                defaults=metadata_defaults,
            )
            model_id, created_model = resolve_or_create_model(
                model_name,
                is_proposed=entry.get("is_proposed", False),
                model_type=model_type,
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
                changed = _update_result(existing, entry, model_name_used, params_millions=params)
                existing.variant_inference_reason = variant_reason
                if changed:
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
                params_millions=params,
                table_ref=entry.get("table_ref"),
                source_ref=entry.get("source_ref", "this paper"),
                extraction_model=model_name_used,
                variant_inference_reason=variant_reason,
            )
            session.add(result)
            summary.new_results += 1

        param_lookup = {k: float(v) for k, v in sizes_lookup.items() if v is not None}
        if param_lookup:
            from backend.export_to_hugo import _sanitize_model
            from backend.result_params_backfill import backfill_paper_params_millions

            backfill_paper_params_millions(
                session,
                paper,
                lookup=param_lookup,
                sanitize_model=_sanitize_model,
            )

    logger.info("Stored %d new Result rows for arXiv:%s", summary.new_results, arxiv_id)
    if summary.updated_results:
        logger.info(
            "Updated %d existing Result row(s) for arXiv:%s — usually duplicate model/dataset/metric keys in the extraction output",
            summary.updated_results,
            arxiv_id,
        )

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


def _update_result(
    result: Result,
    entry: dict,
    model_name_used: str,
    params_millions: float | None = None,
) -> bool:
    changed = False
    value, std = _parse_entry_value(entry)
    if value is not None and result.metric_value != value:
        result.metric_value = value
        changed = True
    if std is not None and result.metric_std != std:
        result.metric_std = std
        changed = True
    if "uses_external_data" in entry and result.uses_external_data is None:
        ued = entry["uses_external_data"]
        result.uses_external_data = 1 if ued is True else 0 if ued is False else None
        changed = True
    if params_millions is not None and result.params_millions is None:
        result.params_millions = params_millions
        changed = True
    if result.extraction_model != model_name_used:
        result.extraction_model = model_name_used
        changed = True
    return changed


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
        arxiv_id = normalize_arxiv_id(arxiv_id)
        total_new += parse_and_store(arxiv_id)

    print(f"Total new Result rows created: {total_new}")


if __name__ == "__main__":
    main()
