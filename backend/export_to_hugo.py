"""Export DB contents to Hugo markdown content files.

Generates:
  site/content/papers/{arxiv_id}/index.md
  site/content/datasets/{dataset_slug}/index.md
  site/data/benchmarks.json

Also copies main figures to site/static/figures/{arxiv_id}/

Usage::
    python -m backend.export_to_hugo
    python -m backend.export_to_hugo --paper 2206.08164
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
import statistics
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import yaml
from sqlalchemy.orm import Session, joinedload

from backend.baseline_aggregator import get_best_results_over_time
from backend.config import cfg
from backend.db import init_db, session_scope
from backend.export_helpers import has_paper_value_gap as _has_paper_value_gap
from backend.export_helpers import plain_model as _plain_model
from backend.export_helpers import rank_for_value as _rank_for_value
from backend.export_helpers import sanitize_model as _sanitize_model_text
from backend.export_helpers import sanitize_title as _sanitize_title
from backend.model_metadata import architecture_label, architecture_title
from backend.models import (
    Benchmark,
    Dataset,
    DatasetVariant,
    Paper,
    Result,
)
from backend.override_handler import get_model_renames, load_overrides
from backend.paper_storage import PaperStorage
from backend.text_cleanup import clean_extracted_text

logger = logging.getLogger(__name__)

_SITE_DIR = cfg.base_dir / "site"
_CONTENT = _SITE_DIR / "content"
_DATA_DIR = _SITE_DIR / "data"
_STATIC = _SITE_DIR / "static"
_DATASET_OVERRIDES_FILE = cfg.base_dir / "config" / "dataset_overrides.yaml"

_MODEL_RENAME_CACHE: dict[str, dict[str, str]] = {}
_DATASET_OVERRIDE_CACHE: dict[str, dict[str, Any]] = {}
_GLOBAL_RANKS_CACHE: dict[
    tuple[str, str, bool], tuple[dict[str, int], list[dict], dict[str, dict[str, Any]]]
] = {}
_AT_PUB_MODEL_CACHE: dict[tuple[str, str, bool, str], dict[str, dict[str, Any]]] = {}
_DATASET_EXPORT_META_CACHE: dict[int, dict[str, Any]] = {}
_BENCHMARK_EXPORTABLE_TOTALS: dict[str, int] | None = None
_DATASET_PAPER_COUNT_CACHE: dict[tuple[str, str], int] = {}

RECENT_RESULTS_YEARS = 2


def _recent_results_cutoff_iso() -> str:
    """ISO date for leaderboard rows counted as recent (paper publication date)."""
    return (date.today() - timedelta(days=365 * RECENT_RESULTS_YEARS)).isoformat()


def _count_recent_leaderboard_rows(rows: list[dict[str, Any]]) -> int:
    cutoff = _recent_results_cutoff_iso()
    return sum(1 for row in rows if (row.get("date_iso") or "") >= cutoff)


def clear_export_caches() -> None:
    """Reset per-export-run caches (call at the start of a full or partial export)."""
    global _BENCHMARK_EXPORTABLE_TOTALS
    _MODEL_RENAME_CACHE.clear()
    _DATASET_OVERRIDE_CACHE.clear()
    _GLOBAL_RANKS_CACHE.clear()
    _AT_PUB_MODEL_CACHE.clear()
    _DATASET_EXPORT_META_CACHE.clear()
    _BENCHMARK_EXPORTABLE_TOTALS = None
    _DATASET_PAPER_COUNT_CACHE.clear()


_CONFERENCE_ALIASES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("NeurIPS", ("neurips", "nips", "neural information processing systems")),
    ("ICLR", ("iclr", "international conference on learning representations")),
    (
        "TMLR",
        ("tmlr", "transactions on machine learning research", "trans. mach. learn. res."),
    ),
    ("ICML", ("icml", "international conference on machine learning")),
    (
        "LoG",
        (
            "learning on graphs and geometry",
            "learning on graphs conference",
            "graph learning conference",
        ),
    ),
    ("AAAI", ("aaai", "association for the advancement of artificial intelligence")),
    ("KDD", ("kdd", "sigkdd", "knowledge discovery and data mining")),
)
_SHORT_CONFERENCE_ALIASES = frozenset(
    alias for _label, aliases in _CONFERENCE_ALIASES for alias in aliases if len(alias) <= 5
)
_BOUNDED_METRIC_SUBSTRINGS: tuple[str, ...] = (
    "accuracy",
    "acc",
    "f1",
    "ap",
    "auc",
    "auroc",
    "mrr",
    "hits@",
)


# ── Helpers ───────────────────────────────────────────────────────────────────


def _slug(name: str) -> str:
    """Convert a string to a URL-safe slug."""
    return re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")


def _normalize_conference(venue: str | None) -> str:
    raw = " ".join(str(venue or "").split()).strip()
    if not raw:
        return ""
    lowered = raw.lower()
    for label, aliases in _CONFERENCE_ALIASES:
        for alias in aliases:
            if alias in _SHORT_CONFERENCE_ALIASES:
                if re.search(rf"\b{re.escape(alias)}\b", lowered):
                    return label
            elif alias in lowered:
                return label
    return ""


def _publication_year(published_date: str | None) -> str:
    raw = (published_date or "").strip()
    if len(raw) >= 4 and raw[:4].isdigit():
        year = int(raw[:4])
        if 1990 <= year <= 2100:
            return str(year)
    return ""


def _conference_export_fields(venue: str | None, published_date: str | None) -> dict[str, str]:
    short = _normalize_conference(venue)
    if not short:
        return {
            "published_conference": "",
            "published_conference_short": "",
            "published_conference_slug": "",
        }
    year = _publication_year(published_date)
    label = f"{short} {year}" if year else short
    return {
        "published_conference": label,
        "published_conference_short": short,
        "published_conference_slug": _slug(short),
    }


def _query_exportable_papers(session: Any, arxiv_ids: list[str] | None = None) -> list[Paper]:
    from sqlalchemy import or_

    query = (
        session.query(Paper)
        .join(Paper.results)
        .filter(or_(Result.is_problematic.is_(None), Result.is_problematic == 0))
        .distinct()
    )
    if arxiv_ids:
        query = query.filter(Paper.arxiv_id.in_(arxiv_ids))
    return query.all()


def _is_bounded_metric(metric_name: str | None) -> bool:
    key = (metric_name or "").strip().lower()
    return any(sub in key for sub in _BOUNDED_METRIC_SUBSTRINGS)


def _normalize_model_family(model_name: str | None) -> str:
    raw = (model_name or "").strip().lower()
    if re.match(r"^gated[\s-]?gcn(?:\s|\(|$)", raw):
        return "gatedgcn"
    if re.match(r"^gcn(?:\s|\(|$)", raw):
        return "gcn"
    if re.match(r"^gin(?:\s|\(|$)", raw):
        return "gin"
    if re.match(r"^(?:graphsage|sage)(?:\s|\(|$)", raw):
        return "sage"
    if re.match(r"^mlp(?:\s|\(|$)", raw):
        return "mlp"
    return ""


def _plain_core_baseline_kind(model_name: str | None) -> str:
    """Return core family only for plain baseline names (exact GCN/GIN/SAGE/MLP/GatedGCN)."""
    key = _plain_model(model_name).strip().lower()
    if not key:
        return ""
    if key == "mlp":
        return "mlp"
    if key == "gcn":
        return "gcn"
    if key == "gin":
        return "gin"
    if key in ("graphsage", "sage"):
        return "sage"
    if re.fullmatch(r"gated[\s-]?gcn", key):
        return "gatedgcn"
    return ""


def _row_metric_value(row: dict) -> float | None:
    value = row.get("sort_value")
    if value is None:
        value = row.get("value")
    if value is None:
        return None
    return float(value)


def _row_is_better(candidate: dict, incumbent: dict | None, *, higher_is_better: bool) -> bool:
    if incumbent is None:
        return True
    cand_v = _row_metric_value(candidate)
    inc_v = _row_metric_value(incumbent)
    if cand_v is None:
        return False
    if inc_v is None:
        return True
    return cand_v > inc_v if higher_is_better else cand_v < inc_v


def _paper_model_renames(arxiv_id: str | None) -> dict[str, str]:
    if not arxiv_id:
        return {}
    if arxiv_id in _MODEL_RENAME_CACHE:
        return _MODEL_RENAME_CACHE[arxiv_id]
    overrides = load_overrides(arxiv_id)
    mapping = get_model_renames(overrides)
    normalized = {
        str(k).strip().lower(): str(v).strip()
        for k, v in mapping.items()
        if str(k).strip() and str(v).strip()
    }
    _MODEL_RENAME_CACHE[arxiv_id] = normalized
    return normalized


def _sanitize_model(model_name: str | None, arxiv_id: str | None = None) -> str:
    return _sanitize_model_text(model_name, remap=_paper_model_renames(arxiv_id))


def _model_key(model_name: str | None) -> str:
    return _plain_model(model_name).lower()


def _paper_site_link(arxiv_id: str | None, label: str | None = None) -> str:
    paper_id = (arxiv_id or "").strip()
    if not paper_id:
        return label or ""
    text = (label or paper_id).replace("[", "\\[").replace("]", "\\]")
    return f"[{text}](/papers/{paper_id}/)"


def _truncate_words(text: str | None, limit: int) -> str:
    value = " ".join(str(text or "").split())
    if not value:
        return ""
    words = value.split()
    if len(words) <= limit:
        return value
    return " ".join(words[:limit]) + "..."


def _has_paper_value_difference(
    paper_value: float | None,
    true_value: float | None,
) -> bool:
    if paper_value is None or true_value is None:
        return False
    return abs(paper_value - true_value) > 1e-12


def _is_value_worse_than(
    value: float,
    reference: float,
    higher_is_better: bool,
    value_std: float | None = None,
    reference_std: float | None = None,
) -> bool:
    """True when *value* is strictly worse than *reference* (outside combined std)."""
    worse = (value < reference) if higher_is_better else (value > reference)
    if not worse:
        return False
    delta = abs(value - reference)
    if value_std is not None and delta <= float(value_std):
        return False
    if reference_std is not None and delta <= float(reference_std):
        return False
    return delta > 1e-12


def _resolve_global_rank(
    row: dict,
    model_to_rank: dict[str, int],
    global_top_all: list[dict],
    higher_is_better: bool,
) -> int | None:
    """Leaderboard rank for a row on the dataset primary metric.

    Uses the cached best-per-model rank when the model appears on the global
    leaderboard. Otherwise ranks the row's displayed value (``sort_value`` or
    ``value``) as if it were inserted into that leaderboard — needed when the
    paper only reported a different metric name or the model has no stored best
    yet for the primary metric.
    """
    model_key = row.get("model_key", "")
    if model_key:
        rank = model_to_rank.get(model_key)
        if rank is not None:
            return rank

    sort_value = row.get("sort_value")
    if sort_value is None:
        sort_value = row.get("value")
    if sort_value is None:
        metric_values = row.get("metric_values")
        if metric_values:
            sort_value = metric_values[0]
    return _rank_for_value(global_top_all, model_key, sort_value, higher_is_better)


def _higher_is_better_for_metric(rows: list[dict], metric: str, fallback: bool = True) -> bool:
    for row in rows:
        if row.get("metric") == metric and row.get("higher_is_better") is not None:
            return bool(row["higher_is_better"])
    return fallback


def _paper_metric_global_caches(
    session: Any,
    ds_name: str,
    paper_metrics: list[str],
    rows: list[dict],
    default_higher: bool,
) -> dict[str, tuple[dict[str, int], list[dict], dict[str, dict[str, Any]], bool]]:
    caches: dict[str, tuple[dict[str, int], list[dict], dict[str, dict[str, Any]], bool]] = {}
    for metric in paper_metrics:
        higher = _higher_is_better_for_metric(rows, metric, default_higher)
        try:
            model_to_rank, global_top_all, truth_map = _global_ranks_cached(
                session, ds_name, metric, higher
            )
        except Exception as exc:
            logger.debug("Global rank lookup failed for %r/%r: %s", ds_name, metric, exc)
            model_to_rank, global_top_all, truth_map = {}, [], {}
        caches[metric] = (model_to_rank, global_top_all, truth_map, higher)
    return caches


def _enrich_paper_result_row(
    row: dict,
    *,
    truth_map: dict[str, dict[str, Any]],
    model_to_rank: dict[str, int],
    global_top_all: list[dict],
    arxiv_id: str,
    higher_is_better: bool,
    at_pub_map: dict[str, dict[str, Any]] | None = None,
) -> None:
    """Attach global-rank and leaderboard comparison fields for ``row['metric']``."""
    row["at_pub_value"] = None
    row["at_pub_std"] = None
    row["at_pub_source_arxiv"] = ""
    row["at_pub_source_title"] = ""
    row["at_pub_source_date_iso"] = ""
    row["value_gap_source_date_iso"] = ""
    row["gap_vs_at_pub"] = None
    row["worse_than_at_pub"] = False
    row["surpassed_since_pub"] = False

    truth = truth_map.get(row.get("model_key", ""))
    if not truth:
        row["sort_value"] = row.get("value")
        row["sort_std"] = row.get("std")
        row["global_rank"] = _resolve_global_rank(
            row, model_to_rank, global_top_all, higher_is_better
        )
        row["has_value_gap"] = False
        row["has_value_note"] = False
        row["value_gap"] = None
        row["value_note"] = ""
        row["paper_rank"] = None
        row["rank_delta"] = None
        row["rank_delta_abs"] = None
        row["rank_delta_direction"] = None
        row["comparison_type"] = None
        row["comparison_source_title"] = ""
        row["comparison_source_arxiv"] = ""
        return

    true_val = truth.get("value")
    true_std = truth.get("std")
    row["true_value"] = true_val
    row["true_std"] = true_std
    row["value_gap_source_arxiv"] = truth.get("arxiv_id", "")
    row["value_gap_source_title"] = truth.get("title", "")
    row["value_gap_source_date_iso"] = truth.get("date_iso", "")
    row["value_gap_source_is_current_paper"] = truth.get("arxiv_id", "") == arxiv_id
    row["value_gap"] = (
        abs(row["paper_value"] - true_val)
        if _has_paper_value_difference(row.get("paper_value"), true_val)
        and row.get("paper_value") is not None
        and true_val is not None
        else None
    )
    row["has_value_note"] = False
    row["value_note"] = ""
    row["sort_value"] = true_val
    row["sort_std"] = true_std
    row["global_rank"] = _resolve_global_rank(row, model_to_rank, global_top_all, higher_is_better)
    row["paper_rank"] = _rank_for_value(
        global_top_all,
        row.get("model_key", ""),
        row.get("paper_value"),
        higher_is_better,
    )
    row["rank_delta"] = (
        row["paper_rank"] - row["global_rank"]
        if row.get("paper_rank") is not None and row.get("global_rank") is not None
        else None
    )
    row["rank_delta_abs"] = abs(row["rank_delta"]) if row.get("rank_delta") is not None else None
    if row.get("rank_delta") is not None:
        if row["rank_delta"] < 0:
            row["rank_delta_direction"] = "better"
        elif row["rank_delta"] > 0:
            row["rank_delta_direction"] = "worse"
        else:
            row["rank_delta_direction"] = "same"
    else:
        row["rank_delta_direction"] = None

    paper_val = row.get("paper_value")
    paper_std = row.get("paper_std")
    at_pub = (at_pub_map or {}).get(row.get("model_key", ""), {})
    at_pub_val = at_pub.get("value")
    at_pub_std = at_pub.get("std")
    row["at_pub_value"] = at_pub_val
    row["at_pub_std"] = at_pub_std
    row["at_pub_source_arxiv"] = at_pub.get("arxiv_id", "")
    row["at_pub_source_title"] = at_pub.get("title", "")
    row["at_pub_source_date_iso"] = at_pub.get("date_iso", "")

    worse_than_at_pub = False
    surpassed_since_pub = False
    if row.get("is_baseline") and paper_val is not None:
        if at_pub_val is not None:
            worse_than_at_pub = _is_value_worse_than(
                float(paper_val),
                float(at_pub_val),
                higher_is_better,
                paper_std,
                at_pub_std,
            )
            if worse_than_at_pub:
                row["gap_vs_at_pub"] = abs(float(paper_val) - float(at_pub_val))
        if true_val is not None and not worse_than_at_pub:
            surpassed_since_pub = _is_value_worse_than(
                float(paper_val),
                float(true_val),
                higher_is_better,
                paper_std,
                true_std,
            )

    row["worse_than_at_pub"] = worse_than_at_pub
    row["surpassed_since_pub"] = surpassed_since_pub
    row["has_value_gap"] = bool(
        row.get("is_baseline")
        and (
            _has_paper_value_gap(paper_val, paper_std, true_val, true_std)
            or worse_than_at_pub
            or surpassed_since_pub
        )
    )

    if row.get("is_global_top"):
        row["comparison_type"] = "global_top"
        row["comparison_source_title"] = ""
        row["comparison_source_arxiv"] = ""
    elif worse_than_at_pub:
        row["comparison_type"] = "behind"
        row["comparison_source_title"] = row["at_pub_source_title"]
        row["comparison_source_arxiv"] = row["at_pub_source_arxiv"]
    elif row.get("is_baseline") and paper_val is not None and true_val is not None:
        better_than_today = (higher_is_better and paper_val > true_val) or (
            not higher_is_better and paper_val < true_val
        )
        if better_than_today:
            row["comparison_type"] = "improved"
            row["comparison_source_title"] = truth.get("title", "")
            row["comparison_source_arxiv"] = truth.get("arxiv_id", "")
        else:
            row["comparison_type"] = None
            row["comparison_source_title"] = ""
            row["comparison_source_arxiv"] = ""
    else:
        row["comparison_type"] = None
        row["comparison_source_title"] = ""
        row["comparison_source_arxiv"] = ""


def _paper_dataset_export_meta(
    dataset_primary_metric: str,
    paper_metrics: list[str],
    display_metric: str,
) -> dict[str, Any]:
    return {
        "dataset_primary_metric": dataset_primary_metric,
        "paper_metrics": paper_metrics,
        "metric": display_metric,
        "uses_non_primary_metric": display_metric != dataset_primary_metric,
        "paper_has_primary_metric": dataset_primary_metric in paper_metrics,
    }


def _result_params_millions(result: Result | None) -> float | None:
    if result is not None and result.params_millions is not None:
        return float(result.params_millions)
    return None


def _copy_main_figure_if_newer(src: Path, dest: Path) -> None:
    """Copy paper main figure to Hugo static dir when missing or source is newer."""
    if dest.exists() and dest.stat().st_mtime >= src.stat().st_mtime:
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def _primary_proposed_from_results(
    results: list[Result],
    proposed_models: list[str],
) -> str | None:
    """Pick the main proposed model from DB rows (no extraction YAML)."""
    if not proposed_models:
        return None
    if len(proposed_models) == 1:
        return proposed_models[0]

    counts: dict[str, int] = {}
    for r in results:
        if not r.model or not r.model.canonical_name:
            continue
        cname = r.model.canonical_name
        if cname not in proposed_models:
            continue
        dv = r.dataset_variant
        if not dv or not dv.dataset:
            continue
        primary_metric = dv.dataset.primary_metric or r.metric_name
        if r.metric_name != primary_metric:
            continue
        counts[cname] = counts.get(cname, 0) + 1
    if counts:
        return max(counts, key=counts.get)
    return proposed_models[0]


_PAPER_RESULT_LOAD_OPTIONS = (
    joinedload(Result.model),
    joinedload(Result.dataset_variant).joinedload(DatasetVariant.dataset),
)
_DATASET_RESULT_LOAD_OPTIONS = (
    joinedload(Result.model),
    joinedload(Result.paper),
    joinedload(Result.dataset_variant).joinedload(DatasetVariant.dataset),
)


def _result_architecture_fields(result: Result | None) -> dict[str, Any]:
    model_type = result.model.model_type if result and result.model else None
    return {
        "architecture_type": model_type,
        "architecture_label": architecture_label(model_type),
        "architecture_title": architecture_title(model_type) or "",
    }


def _load_dataset_overrides() -> dict[str, dict[str, Any]]:
    """Load optional dataset-level display overrides from config/dataset_overrides.yaml."""
    cache_key = "_all"
    cached = _DATASET_OVERRIDE_CACHE.get(cache_key)
    if cached is not None:
        return cached

    if not _DATASET_OVERRIDES_FILE.exists():
        _DATASET_OVERRIDE_CACHE[cache_key] = {}
        return {}

    try:
        raw = yaml.safe_load(_DATASET_OVERRIDES_FILE.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        logger.warning("Failed to read dataset overrides file %s: %s", _DATASET_OVERRIDES_FILE, exc)
        _DATASET_OVERRIDE_CACHE[cache_key] = {}
        return {}

    datasets_raw = raw.get("datasets") if isinstance(raw, dict) else None
    if not isinstance(datasets_raw, dict):
        _DATASET_OVERRIDE_CACHE[cache_key] = {}
        return {}

    normalized: dict[str, dict[str, Any]] = {}
    for ds_name, ds_cfg in datasets_raw.items():
        if not isinstance(ds_cfg, dict):
            continue
        key = str(ds_name).strip().lower()
        if not key:
            continue
        normalized[key] = ds_cfg

    _DATASET_OVERRIDE_CACHE[cache_key] = normalized
    return normalized


def _dataset_display_metrics(dataset_name: str) -> list[str] | None:
    """Return optional ordered metric list to display for the dataset page."""
    ds_cfg = _load_dataset_overrides().get(dataset_name.strip().lower(), {})
    if not isinstance(ds_cfg, dict):
        return None
    metrics = ds_cfg.get("display_metrics")
    if not isinstance(metrics, list):
        return None
    cleaned = [str(m).strip() for m in metrics if str(m).strip()]
    return cleaned or None


def _dataset_force_export(dataset_name: str) -> bool:
    """Return whether the dataset page should be emitted even without results."""
    ds_cfg = _load_dataset_overrides().get(dataset_name.strip().lower(), {})
    if not isinstance(ds_cfg, dict):
        return False
    return bool(ds_cfg.get("export_without_results"))


_CLASS_TARGET_COUNT_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"\b(\d+)\s+(?:subject\s+areas?|subjects?|classes?|targets?|tasks?|labels?)\b", re.I
    ),
    re.compile(r"\b(\d+)\s+(?:venue|community|go)\s+labels?\b", re.I),
    re.compile(r"\b(\d+)\s+categories?\b", re.I),
)


def _description_class_target_count(description: str | None) -> int | None:
    text = " ".join(str(description or "").split())
    if not text:
        return None

    for pattern in _CLASS_TARGET_COUNT_PATTERNS:
        match = pattern.search(text)
        if match:
            try:
                count = int(match.group(1))
            except (TypeError, ValueError):
                continue
            if count > 0:
                return count
    return None


def _summary_num_classes(dataset: Dataset) -> int | None:
    raw_count = dataset.num_classes
    desc_count = _description_class_target_count(dataset.description)
    if desc_count is None:
        return raw_count
    if raw_count is None or raw_count <= 1:
        return desc_count
    return raw_count


def _dataset_page_export_metadata(session: Any, dataset_id: int) -> dict[str, Any]:
    """Return whether a dataset page exports and the aligned overview result count."""
    ds = session.get(Dataset, dataset_id)
    if ds is None:
        return {"exportable": False, "result_count": 0, "recent_result_count": 0}

    variants = (
        session.query(DatasetVariant)
        .filter_by(dataset_id=dataset_id)
        .order_by(DatasetVariant.is_standard.desc(), DatasetVariant.name)
        .all()
    )
    if not variants:
        return {"exportable": False, "result_count": 0, "recent_result_count": 0}

    force_export = _dataset_force_export(ds.name)
    variant_counts: list[tuple[bool, int]] = []
    exportable = False
    primary_metric = ds.primary_metric or ""

    for v in variants:
        all_results = (
            session.query(Result)
            .filter_by(dataset_variant_id=v.id)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .all()
        )

        if not all_results:
            if force_export:
                exportable = True
            continue

        exportable = True
        available_metrics = {r.metric_name for r in all_results}
        if primary_metric and primary_metric in available_metrics:
            metric = primary_metric
        else:
            from collections import Counter

            metric = Counter(r.metric_name for r in all_results).most_common(1)[0][0]
            if not primary_metric:
                primary_metric = metric

        metrics_ordered, _hib, rows = _build_multi_metric_rows(all_results, metric)
        display_metrics = _dataset_display_metrics(ds.name)
        _metrics_ordered, rows, _metric = _apply_display_metrics_filter(
            metrics_ordered,
            rows,
            display_metrics,
            metric,
        )
        variant_counts.append(
            (bool(v.is_standard), len(rows), _count_recent_leaderboard_rows(rows))
        )

    if not exportable:
        return {"exportable": False, "result_count": 0, "recent_result_count": 0}

    std_entry = next((entry for entry in variant_counts if entry[0]), None)
    if std_entry is None:
        std_entry = variant_counts[0]
    result_count = std_entry[1]
    recent_result_count = std_entry[2]
    return {
        "exportable": True,
        "result_count": result_count,
        "recent_result_count": recent_result_count,
    }


def _paper_experiment_scope(task_type: str | None) -> str | None:
    task_key = (task_type or "").strip().lower()
    if task_key.startswith("node_"):
        return "node-level"
    if task_key.startswith("graph_"):
        return "graph-level"
    if task_key.startswith("edge_") or task_key == "link_prediction":
        return "edge-level"
    return None


_PAPER_SCOPE_ORDER = ("node-level", "graph-level", "edge-level")
_PAPER_SCOPE_LABELS = {
    "node-level": "Node-level",
    "graph-level": "Graph-level",
    "edge-level": "Edge-level",
}


def _datasets_by_scope_for_paper(grouped_results: list[dict]) -> list[dict]:
    """Group paper datasets by experiment scope for the single-page hero nav."""
    out: list[dict] = []
    for scope in _PAPER_SCOPE_ORDER:
        bm_entries: dict[str, list[dict]] = {}
        for bm_group in grouped_results:
            bm_name = bm_group.get("benchmark", "")
            for ds_group in bm_group.get("datasets", []):
                if ds_group.get("experiment_scope") != scope:
                    continue
                ds_name = ds_group.get("dataset", "")
                bm_entries.setdefault(bm_name, []).append(
                    {"dataset": ds_name, "dataset_slug": _slug(ds_name)}
                )
        if not bm_entries:
            continue
        benchmarks = [
            {
                "benchmark": bm_name,
                "benchmark_slug": _slug(bm_name),
                "datasets": ds_list,
            }
            for bm_name, ds_list in bm_entries.items()
        ]
        out.append(
            {
                "scope": scope,
                "label": _PAPER_SCOPE_LABELS[scope],
                "benchmarks": benchmarks,
            }
        )
    return out


def _benchmark_totals_exportable(session: Any, benchmarks: list[Benchmark]) -> dict[str, int]:
    """Count exportable datasets per benchmark group (aligned with benchmarks.json).

    Cached for the export run; uses ``_dataset_export_metadata`` so dataset pages
    do not recompute row pivots on every paper.
    """
    global _BENCHMARK_EXPORTABLE_TOTALS
    if _BENCHMARK_EXPORTABLE_TOTALS is not None:
        return _BENCHMARK_EXPORTABLE_TOTALS

    totals: dict[str, int] = {}
    for benchmark in benchmarks:
        count = sum(
            1
            for ds in benchmark.datasets
            if _dataset_export_metadata(session, ds.id).get("exportable")
        )
        if count:
            totals[benchmark.name] = count
    _BENCHMARK_EXPORTABLE_TOTALS = totals
    return totals


def _dataset_paper_count_for_metric(session: Any, ds_name: str, primary_metric: str) -> int:
    """Distinct papers with results on a dataset/metric (cached per export run)."""
    cache_key = (ds_name, primary_metric)
    if cache_key in _DATASET_PAPER_COUNT_CACHE:
        return _DATASET_PAPER_COUNT_CACHE[cache_key]

    from sqlalchemy import func as _sqla_func

    paper_count = (
        session.query(_sqla_func.count(Result.paper_id.distinct()))
        .join(Result.dataset_variant)
        .join(DatasetVariant.dataset)
        .filter(Dataset.name == ds_name)
        .filter(Result.metric_name == primary_metric)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .scalar()
    ) or 0
    _DATASET_PAPER_COUNT_CACHE[cache_key] = int(paper_count)
    return int(paper_count)


def _benchmark_coverage_entries(
    grouped_results: list[dict],
    benchmark_totals: dict[str, int],
) -> list[dict[str, int | str]]:
    """Per-benchmark evaluated/total dataset counts for the papers overview."""
    entries: list[dict[str, int | str]] = []
    for group in grouped_results:
        bm_name = group["benchmark"]
        evaluated = len(group.get("datasets") or [])
        total = benchmark_totals.get(bm_name, evaluated)
        entries.append(
            {
                "benchmark": bm_name,
                "benchmark_slug": _slug(bm_name),
                "evaluated": evaluated,
                "total": total,
            }
        )
    return entries


def _apply_display_metrics_filter(
    metrics_ordered: list[str],
    rows: list[dict],
    display_metrics: list[str] | None,
    primary_metric: str,
) -> tuple[list[str], list[dict], str]:
    """Filter metric columns in dataset pages according to display_metrics list."""
    if not display_metrics:
        return metrics_ordered, rows, primary_metric

    filtered_metrics = [m for m in display_metrics if m in metrics_ordered]
    if not filtered_metrics:
        logger.warning(
            "display_metrics=%s contains no metrics present in exported metrics=%s; keeping all",
            display_metrics,
            metrics_ordered,
        )
        return metrics_ordered, rows, primary_metric

    idx_map = {m: i for i, m in enumerate(metrics_ordered)}
    new_rows: list[dict] = []
    for r in rows:
        new_r = dict(r)
        metric_values = r.get("metric_values") or []
        metric_stds = r.get("metric_stds") or []
        new_r["metric_values"] = [metric_values[idx_map[m]] for m in filtered_metrics]
        new_r["metric_stds"] = [metric_stds[idx_map[m]] for m in filtered_metrics]
        new_rows.append(new_r)

    new_primary = primary_metric if primary_metric in filtered_metrics else filtered_metrics[0]
    return filtered_metrics, new_rows, new_primary


def _mark_is_best(
    rows: list[dict],
    primary_metric_key: str,
    higher_is_better: bool,
    val_getter: callable,
    std_getter: callable,
) -> None:
    """Mutate rows in-place adding is_best flag.

    A row is "best" when its confidence interval overlaps with the top performer's CI,
    using the heuristic: |best_val - row_val| <= best_std + row_std.
    Rows with no value are never best.
    """
    best_val: float | None = None
    best_std: float | None = None
    for r in rows:
        v = val_getter(r)
        if v is not None:
            best_val = v
            best_std = std_getter(r)
            break

    for r in rows:
        v = val_getter(r)
        if v is None or best_val is None:
            r["is_best"] = False
            continue
        s = std_getter(r) or 0.0
        bs = best_std or 0.0
        if higher_is_better:
            r["is_best"] = v + s >= best_val - bs
        else:
            r["is_best"] = v - s <= best_val + bs


def _mark_std_outliers(rows: list[dict], std_getter: callable) -> None:
    """Flag rows whose std is >10x the dataset median std."""
    std_values = []
    for row in rows:
        std = std_getter(row)
        if std is None:
            continue
        std_f = float(std)
        if std_f > 0:
            std_values.append(std_f)

    if not std_values:
        for row in rows:
            row["is_std_outlier"] = False
        return

    median_std = statistics.median(std_values)
    if median_std <= 0:
        for row in rows:
            row["is_std_outlier"] = False
        return

    threshold = median_std * 10.0
    for row in rows:
        std = std_getter(row)
        row["is_std_outlier"] = std is not None and float(std) > threshold


def _fmt_date(date_str: str | None) -> str:
    """Format date strings consistently for public display."""
    if not date_str:
        return ""
    try:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            return datetime.fromisoformat(date_str).strftime("%b %d, %Y").replace(" 0", " ")
        if re.match(r"^\d{4}-\d{2}$", date_str):
            return datetime.fromisoformat(date_str + "-01").strftime("%b %Y")
        return datetime.fromisoformat(date_str[:10]).strftime("%b %d, %Y").replace(" 0", " ")
    except ValueError:
        return date_str


def _fmt_month_year(date_str: str | None) -> str:
    """Format a date string as Mon YYYY for table display."""
    if not date_str:
        return ""
    try:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            return datetime.fromisoformat(date_str[:10]).strftime("%b %Y")
        if re.match(r"^\d{4}-\d{2}$", date_str):
            return datetime.fromisoformat(date_str + "-01").strftime("%b %Y")
        return _fmt_date(date_str)
    except ValueError:
        return date_str


def _yaml_dump_front_matter(front_matter: dict) -> str:
    try:
        from yaml import CSafeDumper as _Dumper
    except ImportError:
        from yaml import SafeDumper as _Dumper

    return yaml.dump(
        front_matter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        Dumper=_Dumper,
    )


def _write_md(path: Path, front_matter: dict, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_str = _yaml_dump_front_matter(front_matter)
    path.write_text(f"---\n{fm_str}---\n\n{body}", encoding="utf-8")


def _sanitize_abstract(text: str | None) -> str:
    """Light cleanup for public-facing abstracts exported from extraction artifacts."""
    if not text:
        return ""
    cleaned = str(text)
    cleaned = cleaned.replace("~https://", " https://").replace("~http://", " http://")
    cleaned = cleaned.replace("~", " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"\s+([,.;:])", r"\1", cleaned)
    return cleaned


def _dedup_result_rows(rows: list[dict], signature_fields: tuple[str, ...]) -> list[dict]:
    """Remove exact duplicate exported rows while preserving first-seen order."""
    unique_rows: list[dict] = []
    seen: set[tuple[Any, ...]] = set()
    for row in rows:
        signature: list[Any] = []
        for field in signature_fields:
            value = row.get(field)
            if isinstance(value, (list, dict)):
                signature.append(json.dumps(value, sort_keys=True, ensure_ascii=False))
            else:
                signature.append(value)
        signature_tuple = tuple(signature)
        if signature_tuple in seen:
            continue
        seen.add(signature_tuple)
        unique_rows.append(row)
    return unique_rows


# ── Paper export ──────────────────────────────────────────────────────────────


def _pivot_paper_rows(rows: list[dict], primary_metric: str | None) -> dict:
    """Pivot flat per-metric paper rows into multi-metric format (like dataset pages).

    Input rows have fields: model, value, std, metric, is_baseline, params_millions, …
    Output has each model once with metric_values / metric_stds parallel arrays.
    """
    # Collect metrics in order of first appearance; primary goes first
    seen_metrics: list[str] = list(dict.fromkeys(r["metric"] for r in rows if r.get("metric")))
    if primary_metric and primary_metric in seen_metrics or primary_metric:
        seen_metrics = [primary_metric] + [m for m in seen_metrics if m != primary_metric]
    elif not primary_metric and seen_metrics:
        primary_metric = seen_metrics[0]

    # Group by model (first appearance determines metadata)
    seen_models: list[str] = []
    model_first: dict[str, dict] = {}
    model_vals: dict[str, dict[str, tuple]] = {}  # model -> {metric -> (val, std)}
    for r in rows:
        model = r.get("model") or ""
        if model not in model_first:
            seen_models.append(model)
            model_first[model] = r
            model_vals[model] = {}
        m = r.get("metric") or ""
        if m and m not in model_vals[model]:
            model_vals[model][m] = (r.get("value"), r.get("std"))

    # Sort by primary metric value
    higher = bool(rows[0].get("higher_is_better", True)) if rows else True

    def _sort_key(model: str) -> tuple:
        primary_row = next(
            (
                r
                for r in rows
                if (r.get("model") or "") == model and r.get("metric") == primary_metric
            ),
            model_first[model],
        )
        pval = primary_row.get("sort_value")
        if pval is None:
            pval = model_vals[model].get(primary_metric or "", (None, None))[0]
        if pval is None:
            return (1, 0.0)
        return (0, -pval if higher else pval)

    seen_models.sort(key=_sort_key)

    pivoted: list[dict] = []
    for model in seen_models:
        first = model_first[model]
        primary_row = next(
            (
                r
                for r in rows
                if (r.get("model") or "") == model and r.get("metric") == primary_metric
            ),
            first,
        )
        metric_values = [model_vals[model].get(m, (None, None))[0] for m in seen_metrics]
        metric_stds = [model_vals[model].get(m, (None, None))[1] for m in seen_metrics]
        pivoted.append(
            {
                "model": model,
                "model_key": first.get("model_key", _model_key(model)),
                "model_plain": first.get("model_plain", _plain_model(model)),
                "metric_values": metric_values,
                "metric_stds": metric_stds,
                "is_baseline": first.get("is_baseline", False),
                "is_overridden": first.get("is_overridden", False),
                "override_reason": first.get("override_reason", ""),
                "params_millions": first.get("params_millions"),
                "architecture_type": first.get("architecture_type"),
                "architecture_label": first.get("architecture_label"),
                "architecture_title": first.get("architecture_title", ""),
                "sort_value": primary_row.get("sort_value"),
                "sort_std": primary_row.get("sort_std"),
                "true_value": primary_row.get("true_value"),
                "true_std": primary_row.get("true_std"),
                "paper_value": primary_row.get("paper_value"),
                "paper_std": primary_row.get("paper_std"),
                "has_value_gap": primary_row.get("has_value_gap", False),
                "has_value_note": primary_row.get("has_value_note", False),
                "value_gap": primary_row.get("value_gap"),
                "value_gap_source_arxiv": primary_row.get("value_gap_source_arxiv", ""),
                "value_gap_source_title": primary_row.get("value_gap_source_title", ""),
                "value_note": primary_row.get("value_note", ""),
                "at_pub_value": primary_row.get("at_pub_value"),
                "at_pub_std": primary_row.get("at_pub_std"),
                "at_pub_source_arxiv": primary_row.get("at_pub_source_arxiv", ""),
                "at_pub_source_title": primary_row.get("at_pub_source_title", ""),
                "at_pub_source_date_iso": primary_row.get("at_pub_source_date_iso", ""),
                "value_gap_source_date_iso": primary_row.get("value_gap_source_date_iso", ""),
                "gap_vs_at_pub": primary_row.get("gap_vs_at_pub"),
                "worse_than_at_pub": primary_row.get("worse_than_at_pub", False),
                "surpassed_since_pub": primary_row.get("surpassed_since_pub", False),
                "arxiv_id": first.get("arxiv_id", ""),
                "title": first.get("title", ""),
                "published_venue": first.get("published_venue", ""),
                "date": first.get("date", ""),
                "date_display": first.get("date_display", ""),
                "date_iso": first.get("date_iso", ""),
                "codebase_url": first.get("codebase_url", ""),
                "uses_external_data": first.get("uses_external_data"),
                "comparison_type": first.get("comparison_type"),
                "comparison_source_title": first.get("comparison_source_title", ""),
                "comparison_source_arxiv": first.get("comparison_source_arxiv", ""),
            }
        )

    _mark_is_best(
        pivoted,
        primary_metric or "",
        higher,
        lambda r: (
            r.get("sort_value")
            if r.get("sort_value") is not None
            else (r["metric_values"][0] if r["metric_values"] else None)
        ),
        lambda r: (
            r.get("sort_std")
            if r.get("sort_std") is not None
            else (r["metric_stds"][0] if r["metric_stds"] else None)
        ),
    )

    _mark_std_outliers(
        pivoted,
        lambda r: (
            r.get("sort_std")
            if r.get("sort_std") is not None
            else (r["metric_stds"][0] if r.get("metric_stds") else None)
        ),
    )
    return {"rows": pivoted, "metrics": seen_metrics, "primary_metric": primary_metric}


def _global_ranks_for_dataset(
    session: Any,
    ds_name: str,
    primary_metric: str,
    higher_is_better: bool,
) -> tuple[dict[str, int], list[dict], dict[str, dict[str, Any]]]:
    """Return (model_to_rank, sorted_rows, model_truth_map) for *ds_name* on *primary_metric*.

    Deduplicates by canonical model name (keeps the best result per model across
    all papers).  The returned rows are sorted best-first and already have
    ``is_global_top=True`` and ``global_rank`` set — callers filter to models
    not already in the paper before adding them to the display list.
    """
    all_res = (
        session.query(Result)
        .options(
            joinedload(Result.model),
            joinedload(Result.paper),
            joinedload(Result.dataset_variant).joinedload(DatasetVariant.dataset),
        )
        .join(Result.dataset_variant)
        .join(DatasetVariant.dataset)
        .filter(Dataset.name == ds_name)
        .filter(Result.metric_name == primary_metric)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )

    # Keep the best value per canonical model name
    model_best: dict[str, tuple[float, Any]] = {}
    for r in all_res:
        model_key = _model_key(r.model.canonical_name if r.model else "")
        if not model_key:
            continue
        v = float(r.display_value) if r.display_value is not None else None
        if v is None:
            continue
        prev = model_best.get(model_key)
        if (
            prev is None
            or (higher_is_better and v > prev[0])
            or (not higher_is_better and v < prev[0])
        ):
            model_best[model_key] = (v, r)

    sorted_items = sorted(
        model_best.items(),
        key=lambda kv: -kv[1][0] if higher_is_better else kv[1][0],
    )
    model_to_rank: dict[str, int] = {m: i + 1 for i, (m, _) in enumerate(sorted_items)}

    rows: list[dict] = []
    truth_map: dict[str, dict[str, Any]] = {}
    for model_key, (val, r) in sorted_items:
        p = r.paper
        ued = r.uses_external_data
        rendered_name = _sanitize_model(
            (r.model.canonical_name if r.model else "") or "",
            p.arxiv_id if p else None,
        )
        row = {
            "model": rendered_name,
            "model_key": model_key,
            "model_plain": _plain_model(rendered_name),
            "value": val,
            "std": float(r.display_std) if r.display_std is not None else None,
            "metric": primary_metric,
            "higher_is_better": bool(r.higher_is_better),
            "is_baseline": bool(r.is_baseline),
            "is_overridden": bool(r.is_overridden),
            "override_reason": r.override_reason or "",
            "params_millions": (
                float(r.params_millions) if r.params_millions is not None else None
            ),
            **_result_architecture_fields(r),
            "arxiv_id": p.arxiv_id if p else "",
            "title": _sanitize_title(p.title if p else ""),
            "date": _fmt_date(p.published_date) if p else "",
            "date_display": _fmt_month_year(p.published_date) if p else "",
            "date_iso": (p.published_date[:10] if p and p.published_date else ""),
            "codebase_url": p.codebase_url or "" if p else "",
            "uses_external_data": (True if ued == 1 else (False if ued == 0 else None)),
            "is_global_top": True,
            "global_rank": model_to_rank.get(model_key),
            "sort_value": val,
            "sort_std": float(r.display_std) if r.display_std is not None else None,
            "comparison_type": "global_top",
            "comparison_source_title": "",
            "comparison_source_arxiv": "",
        }
        rows.append(row)
        truth_map[model_key] = row

    return model_to_rank, rows, truth_map


def _global_ranks_cached(
    session: Any,
    ds_name: str,
    primary_metric: str,
    higher_is_better: bool,
) -> tuple[dict[str, int], list[dict], dict[str, dict[str, Any]]]:
    """Like ``_global_ranks_for_dataset``, with a per-export-run module cache."""
    cache_key = (ds_name, primary_metric, higher_is_better)
    if cache_key not in _GLOBAL_RANKS_CACHE:
        _GLOBAL_RANKS_CACHE[cache_key] = _global_ranks_for_dataset(
            session, ds_name, primary_metric, higher_is_better
        )
    return _GLOBAL_RANKS_CACHE[cache_key]


def _global_best_per_model_as_of_date(
    session: Any,
    ds_name: str,
    metric: str,
    higher_is_better: bool,
    cutoff_iso: str,
) -> dict[str, dict[str, Any]]:
    """Best result per model on *metric* from papers published on or before *cutoff_iso*."""
    cache_key = (ds_name, metric, higher_is_better, cutoff_iso or "")
    if cache_key in _AT_PUB_MODEL_CACHE:
        return _AT_PUB_MODEL_CACHE[cache_key]

    all_res = (
        session.query(Result)
        .options(
            joinedload(Result.model),
            joinedload(Result.paper),
            joinedload(Result.dataset_variant).joinedload(DatasetVariant.dataset),
        )
        .join(Result.dataset_variant)
        .join(DatasetVariant.dataset)
        .filter(Dataset.name == ds_name)
        .filter(Result.metric_name == metric)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )

    model_best: dict[str, tuple[float, Any]] = {}
    for r in all_res:
        p = r.paper
        if cutoff_iso:
            pub = p.published_date[:10] if p and p.published_date else ""
            if not pub or pub > cutoff_iso:
                continue
        model_key = _model_key(r.model.canonical_name if r.model else "")
        if not model_key:
            continue
        v = float(r.display_value) if r.display_value is not None else None
        if v is None:
            continue
        prev = model_best.get(model_key)
        if (
            prev is None
            or (higher_is_better and v > prev[0])
            or (not higher_is_better and v < prev[0])
        ):
            model_best[model_key] = (v, r)

    truth_map: dict[str, dict[str, Any]] = {}
    for model_key, (val, r) in model_best.items():
        p = r.paper
        rendered_name = _sanitize_model(
            (r.model.canonical_name if r.model else "") or "",
            p.arxiv_id if p else None,
        )
        truth_map[model_key] = {
            "model": rendered_name,
            "model_key": model_key,
            "value": val,
            "std": float(r.display_std) if r.display_std is not None else None,
            "arxiv_id": p.arxiv_id if p else "",
            "title": _sanitize_title(p.title if p else ""),
            "date_iso": (p.published_date[:10] if p and p.published_date else ""),
        }

    _AT_PUB_MODEL_CACHE[cache_key] = truth_map
    return truth_map


def _dataset_export_metadata(session: Any, dataset_id: int) -> dict[str, Any]:
    """Dataset page metadata, using cache populated by ``export_dataset`` when available."""
    cached = _DATASET_EXPORT_META_CACHE.get(dataset_id)
    if cached is not None:
        return cached
    return _dataset_page_export_metadata(session, dataset_id)


def _select_global_context_rows(
    global_top_all: list[dict],
    paper_model_keys: set[str],
    *,
    top_n: int = 3,
) -> list[dict]:
    """Pick global-top rows for paper display: dataset ranks 1..top_n plus plain core baselines."""
    extras: list[dict] = []
    seen_keys = set(paper_model_keys)

    def _add(gr: dict) -> None:
        model_key = gr.get("model_key", "")
        if not model_key or model_key in seen_keys:
            return
        seen_keys.add(model_key)
        extras.append(gr)

    for gr in global_top_all[:top_n]:
        _add(gr)

    higher_is_better = (
        bool(global_top_all[0].get("higher_is_better", True)) if global_top_all else True
    )
    best_plain_gnn_global: dict | None = None
    best_gnn_extra: dict | None = None
    gated_row: dict | None = None
    mlp_row: dict | None = None

    for gr in global_top_all:
        model_key = gr.get("model_key", "")
        if not model_key:
            continue
        kind = _plain_core_baseline_kind(gr.get("model"))
        if kind in ("gcn", "gin", "sage"):
            if _row_is_better(gr, best_plain_gnn_global, higher_is_better=higher_is_better):
                best_plain_gnn_global = gr
            if model_key not in seen_keys and _row_is_better(
                gr, best_gnn_extra, higher_is_better=higher_is_better
            ):
                best_gnn_extra = gr
        elif kind == "gatedgcn" and gated_row is None and model_key not in seen_keys:
            gated_row = gr
        elif kind == "mlp" and mlp_row is None and model_key not in seen_keys:
            mlp_row = gr

    if best_gnn_extra is not None:
        _add(best_gnn_extra)
    if gated_row is not None and _row_is_better(
        gated_row, best_plain_gnn_global, higher_is_better=higher_is_better
    ):
        _add(gated_row)
    if mlp_row is not None:
        _add(mlp_row)

    return extras


def _global_row_to_pivoted_extra(gr: dict, n_metrics: int) -> dict:
    return {
        "model": gr["model"],
        "model_key": gr["model_key"],
        "model_plain": gr.get("model_plain") or _plain_model(gr["model"]),
        "metric_values": [gr["value"] if i == 0 else None for i in range(n_metrics)],
        "metric_stds": [gr["std"] if i == 0 else None for i in range(n_metrics)],
        "is_baseline": gr["is_baseline"],
        "is_overridden": False,
        "override_reason": "",
        "params_millions": gr["params_millions"],
        "architecture_type": gr.get("architecture_type"),
        "architecture_label": gr.get("architecture_label"),
        "architecture_title": gr.get("architecture_title", ""),
        "arxiv_id": gr["arxiv_id"],
        "title": gr["title"],
        "published_venue": gr.get("published_venue", ""),
        "date": gr["date"],
        "date_display": gr.get("date_display", ""),
        "date_iso": gr.get("date_iso", ""),
        "codebase_url": gr["codebase_url"],
        "uses_external_data": gr.get("uses_external_data"),
        "is_global_top": True,
        "global_rank": gr["global_rank"],
        "is_best": False,
        "sort_value": gr.get("sort_value", gr.get("value")),
        "sort_std": gr.get("sort_std", gr.get("std")),
        "has_value_gap": False,
        "has_value_note": False,
        "paper_rank": None,
        "rank_delta": None,
        "rank_delta_abs": None,
        "value_note": "",
        "comparison_type": gr.get("comparison_type", "global_top"),
        "comparison_source_title": gr.get("comparison_source_title", ""),
        "comparison_source_arxiv": gr.get("comparison_source_arxiv", ""),
    }


def _compute_paper_mrr(
    session: Any,
    paper: Paper,
) -> tuple[float | None, float | None, int, list[str]]:
    """Return (raw_mrr, adjusted_mrr, dataset_count, proposed_model_names) for *paper*.

    MRR is the mean reciprocal rank of the paper's *primary* proposed model on
    each dataset's primary metric, ranked against ALL models globally (baselines
    included).  Only datasets that have ≥10 global entries count toward MRR.

    "Primary proposed model" = the model named in the LLM extraction's
    ``proposed_model.name`` field (read from llm_output artifact). Falls back to
    the first non-baseline model found if the artifact is unavailable.

    Adjusted MRR uses a three-dataset floor, i.e. it divides the reciprocal-rank
    sum by ``max(dataset_count, 3)``. This penalizes papers evaluated on very few
    datasets without distorting the underlying per-dataset ranks.

    Returns ``(None, None, 0, [])`` for pure benchmarking papers.
    Returns ``(0.0, 0.0, 0, names)`` when the paper has proposed models but none qualify.
    """
    results = (
        session.query(Result)
        .options(*_PAPER_RESULT_LOAD_OPTIONS)
        .filter_by(paper_id=paper.id, is_baseline=False)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )
    if not results:
        return None, None, 0, []

    proposed_models: list[str] = list(
        dict.fromkeys(r.model.canonical_name for r in results if r.model and r.model.canonical_name)
    )

    primary_proposed = _primary_proposed_from_results(results, proposed_models)

    if primary_proposed is None:
        return 0.0, 0.0, 0, proposed_models

    # Collect per-dataset best values for the primary proposed model only.
    ds_info: dict[str, dict] = {}
    for r in results:
        dv = r.dataset_variant
        if not dv or not dv.dataset:
            continue
        ds = dv.dataset
        primary_metric = ds.primary_metric or r.metric_name
        if r.metric_name != primary_metric:
            continue
        model = r.model.canonical_name if r.model else None
        if model != primary_proposed:
            continue  # only track the primary proposed model
        val = float(r.display_value) if r.display_value is not None else None
        if val is None:
            continue
        hib = bool(r.higher_is_better)
        key = ds.name
        if key not in ds_info:
            ds_info[key] = {"primary_metric": primary_metric, "hib": hib, "best": val}
        else:
            prev = ds_info[key]["best"]
            if (hib and val > prev) or (not hib and val < prev):
                ds_info[key]["best"] = val

    reciprocal_ranks: list[float] = []
    for ds_name, info in ds_info.items():
        try:
            model_to_rank, global_rows, _ = _global_ranks_cached(
                session, ds_name, info["primary_metric"], info["hib"]
            )
        except Exception:
            continue
        if len(global_rows) < 10:
            continue
        if _dataset_paper_count_for_metric(session, ds_name, info["primary_metric"]) < 3:
            continue
        rank = model_to_rank.get(_model_key(primary_proposed))
        if rank is not None:
            reciprocal_ranks.append(1.0 / rank)

    dataset_count = len(reciprocal_ranks)
    mrr = round(sum(reciprocal_ranks) / dataset_count, 4) if reciprocal_ranks else 0.0
    adjusted_mrr = (
        round(sum(reciprocal_ranks) / max(dataset_count, 3), 4) if reciprocal_ranks else 0.0
    )
    return mrr, adjusted_mrr, dataset_count, proposed_models


def _collect_result_anomalies(session: Any) -> list[dict[str, Any]]:
    """Return suspicious stored results for a development report."""
    results = (
        session.query(Result)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )

    grouped: dict[tuple[str, str], list[Result]] = {}
    for result in results:
        dv = result.dataset_variant
        ds = dv.dataset if dv else None
        if not ds:
            continue
        grouped.setdefault((ds.name, result.metric_name), []).append(result)

    medians: dict[tuple[str, str], float] = {}
    for key, items in grouped.items():
        values = [float(r.display_value) for r in items if r.display_value is not None]
        if len(values) >= 5:
            medians[key] = statistics.median(values)

    anomalies: list[dict[str, Any]] = []
    for result in results:
        dv = result.dataset_variant
        ds = dv.dataset if dv else None
        paper = result.paper
        model = result.model
        if not ds or not paper or not model or result.display_value is None:
            continue

        value = float(result.display_value)
        metric = result.metric_name or ""
        reasons: list[str] = []
        median = medians.get((ds.name, metric))

        if _is_bounded_metric(metric) and value > 1.0:
            reasons.append("bounded metric above 1")

        if median and median > 0:
            if value == 0:
                reasons.append("zero value against positive dataset median")
            else:
                ratio = value / median
                if ratio >= 20:
                    reasons.append(f"{ratio:.1f}x above dataset median")
                elif ratio <= 0.05:
                    reasons.append(f"{(median / value):.1f}x below dataset median")

        if not reasons:
            continue

        anomalies.append(
            {
                "arxiv_id": paper.arxiv_id,
                "title": _sanitize_title(paper.title),
                "dataset": ds.name,
                "metric": metric,
                "model": model.canonical_name,
                "value": value,
                "median": median,
                "reasons": reasons,
            }
        )

    anomalies.sort(
        key=lambda item: (item["arxiv_id"], item["dataset"], item["metric"], item["model"])
    )
    return anomalies


def _collect_model_value_mismatches(session: Any) -> list[dict[str, Any]]:
    """Return paper rows whose reported primary-metric model value materially disagrees with the global best."""
    results = (
        session.query(Result)
        .join(Result.paper)
        .join(Result.dataset_variant)
        .join(DatasetVariant.dataset)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )

    truth_cache: dict[
        tuple[str, str, bool], tuple[dict[str, int], list[dict], dict[str, dict[str, Any]]]
    ] = {}
    at_pub_cache: dict[tuple[str, str, bool, str], dict[str, dict[str, Any]]] = {}
    mismatches: list[dict[str, Any]] = []

    for result in results:
        paper = result.paper
        dv = result.dataset_variant
        ds = dv.dataset if dv else None
        model = result.model
        if not paper or not ds or not model:
            continue

        primary_metric = ds.primary_metric or result.metric_name
        if result.metric_name != primary_metric:
            continue

        higher = bool(result.higher_is_better)
        cache_key = (ds.name, primary_metric, higher)
        if cache_key not in truth_cache:
            truth_cache[cache_key] = _global_ranks_cached(session, ds.name, primary_metric, higher)
        model_to_rank, global_rows, truth_map = truth_cache[cache_key]

        model_key = _model_key(model.canonical_name)
        truth = truth_map.get(model_key)
        if not truth:
            continue

        paper_value = float(result.display_value) if result.display_value is not None else None
        paper_std = float(result.display_std) if result.display_std is not None else None
        true_value = truth.get("value")
        if not _has_paper_value_gap(paper_value, paper_std, true_value, truth.get("std")):
            continue

        global_rank = model_to_rank.get(model_key)
        paper_rank = _rank_for_value(global_rows, model_key, paper_value, higher)
        rank_delta = (
            paper_rank - global_rank if paper_rank is not None and global_rank is not None else None
        )
        paper_date_iso = paper.published_date[:10] if paper.published_date else ""
        source_arxiv_id = truth.get("arxiv_id", "")
        source_date_iso = truth.get("date_iso", "")
        if source_arxiv_id and source_arxiv_id == paper.arxiv_id:
            source_timing = "same-paper"
        elif source_date_iso and paper_date_iso:
            source_timing = (
                "already-known" if source_date_iso <= paper_date_iso else "published-later"
            )
        else:
            source_timing = "unknown"

        at_pub_key = (ds.name, primary_metric, higher, paper_date_iso)
        if at_pub_key not in at_pub_cache:
            at_pub_cache[at_pub_key] = _global_best_per_model_as_of_date(
                session, ds.name, primary_metric, higher, paper_date_iso
            )
        at_pub = at_pub_cache[at_pub_key].get(model_key, {})
        at_pub_value = at_pub.get("value")
        at_pub_std = at_pub.get("std")
        at_pub_arxiv = at_pub.get("arxiv_id", "")
        at_pub_date_iso = at_pub.get("date_iso", "")

        worse_than_at_pub = False
        surpassed_since_pub = False
        gap_vs_at_pub = None
        if paper_value is not None and at_pub_value is not None:
            worse_than_at_pub = _is_value_worse_than(
                float(paper_value),
                float(at_pub_value),
                higher,
                paper_std,
                at_pub_std,
            )
            if worse_than_at_pub:
                gap_vs_at_pub = abs(float(paper_value) - float(at_pub_value))
        if paper_value is not None and true_value is not None and not worse_than_at_pub:
            surpassed_since_pub = _is_value_worse_than(
                float(paper_value),
                float(true_value),
                higher,
                paper_std,
                truth.get("std"),
            )

        at_pub_arxiv_norm = (at_pub_arxiv or "").strip()
        today_arxiv_norm = (source_arxiv_id or "").strip()
        at_pub_differs_from_today = bool(
            at_pub_arxiv_norm and today_arxiv_norm and at_pub_arxiv_norm != today_arxiv_norm
        )
        if at_pub_arxiv_norm and at_pub_arxiv_norm == paper.arxiv_id:
            at_pub_timing = "same-paper"
        elif at_pub_date_iso and paper_date_iso:
            at_pub_timing = (
                "already-known" if at_pub_date_iso <= paper_date_iso else "published-later"
            )
        else:
            at_pub_timing = "unknown"

        mismatches.append(
            {
                "arxiv_id": paper.arxiv_id,
                "title": _sanitize_title(paper.title),
                "paper_date_iso": paper_date_iso,
                "dataset": ds.name,
                "metric": primary_metric,
                "model": _sanitize_model(model.canonical_name, paper.arxiv_id),
                "is_baseline": bool(result.is_baseline),
                "paper_value": paper_value,
                "paper_std": paper_std,
                "true_value": true_value,
                "true_std": truth.get("std"),
                "at_pub_value": at_pub_value,
                "at_pub_std": at_pub_std,
                "at_pub_source_arxiv": at_pub_arxiv,
                "at_pub_source_title": at_pub.get("title", ""),
                "at_pub_source_date_iso": at_pub_date_iso,
                "at_pub_timing": at_pub_timing,
                "worse_than_at_pub": worse_than_at_pub,
                "surpassed_since_pub": surpassed_since_pub,
                "gap_vs_at_pub": gap_vs_at_pub,
                "at_pub_differs_from_today": at_pub_differs_from_today,
                "source_arxiv_id": source_arxiv_id,
                "source_title": truth.get("title", ""),
                "source_date_iso": source_date_iso,
                "source_timing": source_timing,
                "global_rank": global_rank,
                "paper_rank": paper_rank,
                "rank_delta": rank_delta,
                "value_gap": (
                    abs(paper_value - true_value)
                    if paper_value is not None and true_value is not None
                    else None
                ),
            }
        )

    mismatches.sort(
        key=lambda item: (
            -(abs(item.get("rank_delta") or 0)),
            -(item.get("value_gap") or 0.0),
            item.get("arxiv_id") or "",
            item.get("dataset") or "",
            item.get("model") or "",
        )
    )
    return mismatches


def _collect_missing_baselines(session: Any) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Return datasets missing core GNN baselines and datasets missing MLP baselines."""
    core_missing: list[dict[str, Any]] = []
    mlp_missing: list[dict[str, Any]] = []

    for ds in session.query(Dataset).all():
        families: set[str] = set()
        result_count = 0
        for variant in ds.variants:
            for result in variant.results:
                if result.is_problematic:
                    continue
                result_count += 1
                family = _normalize_model_family(
                    result.model.canonical_name if result.model else ""
                )
                if family:
                    families.add(family)

        item = {
            "benchmark": ds.benchmark.name if ds.benchmark else "Other",
            "dataset": ds.name,
            "task_type": ds.task_type or "",
            "primary_metric": ds.primary_metric or "",
            "result_count": result_count,
            "present_families": ", ".join(sorted(families)) or "—",
        }
        if not any(f in families for f in ("gcn", "gin", "sage")):
            core_missing.append(item)
        if "mlp" not in families:
            mlp_missing.append(item)

    core_missing.sort(key=lambda item: (item["benchmark"], item["dataset"]))
    mlp_missing.sort(key=lambda item: (item["benchmark"], item["dataset"]))
    return core_missing, mlp_missing


def export_paper(arxiv_id: str, *, session: Session | None = None) -> bool:
    """Export a single paper's page to Hugo content."""
    if session is not None:
        return _export_paper_impl(session, arxiv_id)
    with session_scope() as scoped:
        return _export_paper_impl(scoped, arxiv_id)


def _export_paper_impl(session: Session, arxiv_id: str) -> bool:
    paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
    if paper is None:
        logger.warning("Paper arXiv:%s not found in DB", arxiv_id)
        return False

    results = (
        session.query(Result)
        .options(*_PAPER_RESULT_LOAD_OPTIONS)
        .filter_by(paper_id=paper.id)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )
    out_path = _CONTENT / "papers" / arxiv_id / "index.md"
    if not results:
        if out_path.exists():
            out_path.unlink()
        return False

    conference_fields = _conference_export_fields(paper.venue, paper.published_date)

    # Group results by dataset name, tracking metric/direction per group
    result_groups: dict[str, list[dict]] = {}
    result_group_meta: dict[str, dict] = {}
    for r in results:
        dv = r.dataset_variant
        ds_name = dv.dataset.name if dv else "Unknown"
        if ds_name not in result_group_meta:
            # Prefer the dataset's declared primary_metric over the first result's metric
            primary = (
                dv.dataset.primary_metric
                if dv and dv.dataset and dv.dataset.primary_metric
                else r.metric_name
            )
            result_group_meta[ds_name] = {
                "metric": primary,
                "higher_is_better": bool(r.higher_is_better),
            }
        rendered_model = _sanitize_model(
            r.model.canonical_name if r.model else "",
            paper.arxiv_id,
        )
        display_value = float(r.display_value) if r.display_value is not None else None
        display_std = float(r.display_std) if r.display_std is not None else None
        result_groups.setdefault(ds_name, []).append(
            {
                "model": rendered_model,
                "model_key": _model_key(r.model.canonical_name if r.model else rendered_model),
                "model_plain": _plain_model(rendered_model),
                "value": display_value,
                "std": display_std,
                "paper_value": display_value,
                "paper_std": display_std,
                "metric": r.metric_name,
                "higher_is_better": bool(r.higher_is_better),
                "is_baseline": bool(r.is_baseline),
                "is_overridden": bool(r.is_overridden),
                "override_reason": r.override_reason or "",
                "params_millions": _result_params_millions(r),
                **_result_architecture_fields(r),
                "uses_external_data": r.uses_external_data,
                "table_ref": r.table_ref or "",
                "source_ref": r.source_ref or "",
                "variant_inference_reason": r.variant_inference_reason or "",
                "date": _fmt_date(paper.published_date) if paper else "",
                "date_display": _fmt_month_year(paper.published_date) if paper else "",
                "date_iso": (paper.published_date[:10] if paper and paper.published_date else ""),
                "published_venue": paper.venue if paper else "",
                "published_conference": conference_fields["published_conference"],
            }
        )

    dataset_task_type: dict[str, str] = {}
    for r in results:
        dv = r.dataset_variant
        if dv and dv.dataset:
            dataset_task_type[dv.dataset.name] = dv.dataset.task_type or ""

    results_for_fm: list[dict] = []
    for ds, rows in sorted(result_groups.items()):
        meta = result_group_meta[ds]
        dataset_primary_metric = meta["metric"]
        default_higher = meta["higher_is_better"]
        paper_metrics = list(dict.fromkeys(r["metric"] for r in rows if r.get("metric")))
        metric_caches = _paper_metric_global_caches(
            session, ds, paper_metrics, rows, default_higher
        )
        paper_date_iso = paper.published_date[:10] if paper.published_date else ""
        at_pub_maps = {
            metric: _global_best_per_model_as_of_date(
                session,
                ds,
                metric,
                _higher_is_better_for_metric(rows, metric, default_higher),
                paper_date_iso,
            )
            for metric in paper_metrics
        }

        for row in rows:
            metric = row.get("metric") or ""
            model_to_rank, global_top_all, truth_map, higher = metric_caches.get(
                metric, ({}, [], {}, default_higher)
            )
            _enrich_paper_result_row(
                row,
                truth_map=truth_map,
                model_to_rank=model_to_rank,
                global_top_all=global_top_all,
                arxiv_id=arxiv_id,
                higher_is_better=higher,
                at_pub_map=at_pub_maps.get(metric, {}),
            )

        rows = _dedup_result_rows(
            rows,
            (
                "model_key",
                "model",
                "metric",
                "value",
                "std",
                "paper_value",
                "paper_std",
                "true_value",
                "true_std",
                "sort_value",
                "sort_std",
                "is_baseline",
                "has_value_gap",
                "has_value_note",
                "value_gap_source_arxiv",
                "worse_than_at_pub",
                "surpassed_since_pub",
                "rank_delta",
                "comparison_type",
                "comparison_source_title",
                "comparison_source_arxiv",
            ),
        )

        rank_metric = (
            dataset_primary_metric if dataset_primary_metric in paper_metrics else paper_metrics[0]
        )
        rank_model_to_rank, rank_global_top, _, rank_higher = metric_caches.get(
            rank_metric, ({}, [], {}, default_higher)
        )

        if len(paper_metrics) > 1:
            pivoted = _pivot_paper_rows(rows, dataset_primary_metric)
            pv_rows = pivoted["rows"]
            metrics_list = pivoted["metrics"]

            paper_models: set[str] = {pr.get("model_key", "") for pr in pv_rows}
            for pr in pv_rows:
                pr["global_rank"] = _resolve_global_rank(
                    pr, rank_model_to_rank, rank_global_top, rank_higher
                )

            extra_rows = [
                _global_row_to_pivoted_extra(gr, len(metrics_list))
                for gr in _select_global_context_rows(rank_global_top, paper_models)
            ]

            if extra_rows:
                combined = pv_rows + extra_rows

                def _pv_sort(r: dict, _hib: bool = rank_higher) -> tuple:
                    v = r.get("sort_value")
                    if v is None:
                        v = r["metric_values"][0] if r.get("metric_values") else None
                    if v is None:
                        return (1, 0.0)
                    return (0, -v if _hib else v)

                combined.sort(key=_pv_sort)
                _mark_is_best(
                    combined,
                    rank_metric,
                    rank_higher,
                    lambda r: (
                        r.get("sort_value")
                        if r.get("sort_value") is not None
                        else (r["metric_values"][0] if r.get("metric_values") else None)
                    ),
                    lambda r: (
                        r.get("sort_std")
                        if r.get("sort_std") is not None
                        else (r["metric_stds"][0] if r.get("metric_stds") else None)
                    ),
                )
                _mark_std_outliers(
                    combined,
                    lambda r: (
                        r.get("sort_std")
                        if r.get("sort_std") is not None
                        else (r["metric_stds"][0] if r.get("metric_stds") else None)
                    ),
                )
                pv_rows = combined

            pv_rows = _dedup_result_rows(
                pv_rows,
                (
                    "model_key",
                    "model",
                    "metric_values",
                    "metric_stds",
                    "sort_value",
                    "sort_std",
                    "is_baseline",
                    "is_global_top",
                    "has_value_gap",
                    "has_value_note",
                    "rank_delta",
                    "value_gap_source_arxiv",
                    "comparison_type",
                    "comparison_source_title",
                    "comparison_source_arxiv",
                ),
            )

            group_meta = _paper_dataset_export_meta(
                dataset_primary_metric, paper_metrics, rank_metric
            )
            results_for_fm.append(
                {
                    "dataset": ds,
                    "is_multi_metric": True,
                    "rows": pv_rows,
                    "metrics": metrics_list,
                    "primary_metric": pivoted["primary_metric"],
                    "rank_metric": rank_metric,
                    "higher_is_better": rank_higher,
                    "experiment_scope": _paper_experiment_scope(dataset_task_type.get(ds)),
                    **group_meta,
                }
            )
        else:
            display_metric = paper_metrics[0]
            display_model_to_rank, display_global_top, _, display_higher = metric_caches[
                display_metric
            ]
            rows = [r for r in rows if r.get("metric") == display_metric]

            def _row_sort_key(r: dict, _hib: bool = display_higher) -> tuple:
                v = r.get("sort_value")
                if v is None:
                    v = r.get("value")
                if v is None:
                    return (1, 0.0)
                return (0, -float(v) if _hib else float(v))

            rows.sort(key=_row_sort_key)

            paper_models = {r.get("model_key", "") for r in rows}

            extra_rows = _select_global_context_rows(display_global_top, paper_models)

            if extra_rows:
                rows = rows + extra_rows
                rows = _dedup_result_rows(
                    rows,
                    (
                        "model_key",
                        "model",
                        "metric",
                        "value",
                        "std",
                        "paper_value",
                        "paper_std",
                        "true_value",
                        "true_std",
                        "sort_value",
                        "sort_std",
                        "is_baseline",
                        "is_global_top",
                        "has_value_gap",
                        "has_value_note",
                        "rank_delta",
                        "value_gap_source_arxiv",
                        "comparison_type",
                        "comparison_source_title",
                        "comparison_source_arxiv",
                    ),
                )
                rows.sort(key=_row_sort_key)

            _mark_is_best(
                rows,
                display_metric,
                display_higher,
                lambda r: (
                    r.get("sort_value") if r.get("sort_value") is not None else r.get("value")
                ),
                lambda r: r.get("sort_std") if r.get("sort_std") is not None else r.get("std"),
            )
            _mark_std_outliers(
                rows,
                lambda r: r.get("sort_std") if r.get("sort_std") is not None else r.get("std"),
            )
            group_meta = _paper_dataset_export_meta(
                dataset_primary_metric, paper_metrics, display_metric
            )
            results_for_fm.append(
                {
                    "dataset": ds,
                    "rows": rows,
                    "rank_metric": display_metric,
                    "higher_is_better": display_higher,
                    "experiment_scope": _paper_experiment_scope(dataset_task_type.get(ds)),
                    **group_meta,
                }
            )

    # Group paper results by benchmark first, using the same benchmark/dataset ordering
    # strategy as the dataset overview page (result-count driven).
    from sqlalchemy import func

    ds_result_counts: dict[int, int] = dict(
        session.query(Dataset.id, func.count(Result.id))
        .join(Dataset.variants)
        .join(DatasetVariant.results)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .group_by(Dataset.id)
        .all()
    )

    benchmarks = session.query(Benchmark).all()

    def _bm_total(b: Benchmark) -> int:
        return sum(ds_result_counts.get(ds.id, 0) for ds in b.datasets)

    benchmarks = sorted(benchmarks, key=_bm_total, reverse=True)
    benchmark_rank: dict[str, int] = {}
    dataset_rank: dict[tuple[str, str], int] = {}
    dataset_to_benchmark: dict[str, str] = {}
    for bi, b in enumerate(benchmarks):
        benchmark_rank[b.name] = bi
        sorted_datasets = sorted(b.datasets, key=lambda ds: -ds_result_counts.get(ds.id, 0))
        for di, ds in enumerate(sorted_datasets):
            dataset_rank[(b.name, ds.name)] = di
            dataset_to_benchmark[ds.name] = b.name

    grouped_tmp: dict[str, list[dict]] = {}
    for group in results_for_fm:
        ds_name = group.get("dataset", "")
        bm_name = dataset_to_benchmark.get(ds_name, "Other")
        grouped_tmp.setdefault(bm_name, []).append(group)

    grouped_results: list[dict] = []
    for bm_name, ds_groups in sorted(
        grouped_tmp.items(),
        key=lambda kv: benchmark_rank.get(kv[0], 10_000),
    ):
        ds_groups = sorted(
            ds_groups,
            key=lambda g: dataset_rank.get((bm_name, g.get("dataset", "")), 10_000),
        )
        grouped_results.append({"benchmark": bm_name, "datasets": ds_groups})

    datasets_by_scope = _datasets_by_scope_for_paper(grouped_results)

    # Main figure
    storage = PaperStorage(arxiv_id)
    paper_metadata = storage.read_metadata()
    main_figure_hugo: str | None = None
    if storage.main_figure_path and storage.main_figure_path.exists():
        dest = _STATIC / "figures" / arxiv_id / storage.main_figure_path.name
        _copy_main_figure_if_newer(storage.main_figure_path, dest)
        main_figure_hugo = f"/figures/{arxiv_id}/{storage.main_figure_path.name}"

    mrr, adjusted_mrr, mrr_dataset_count, proposed_models = _compute_paper_mrr(session, paper)
    has_results = bool(results_for_fm)

    # Single proposed model: if all proposed results come from the same canonical name
    single_proposed_model: str | None = None
    if len(proposed_models) == 1:
        single_proposed_model = proposed_models[0]

    benchmark_categories = [group["benchmark"] for group in grouped_results]
    benchmark_totals = _benchmark_totals_exportable(session, benchmarks)
    benchmark_coverage = _benchmark_coverage_entries(grouped_results, benchmark_totals)
    task_categories = sorted(
        {
            dv.dataset.task_type
            for r in results
            for dv in [r.dataset_variant]
            if dv and dv.dataset and dv.dataset.task_type
        }
    )
    experiment_scopes = sorted(
        {
            scope
            for scope in (_paper_experiment_scope(task_type) for task_type in task_categories)
            if scope
        }
    )
    paper_type = "method" if proposed_models else "dataset"

    front_matter: dict[str, Any] = {
        "title": _sanitize_title(paper.title) or arxiv_id,
        "arxiv_id": arxiv_id,
        "source_url": paper_metadata.get("paper_url") or paper_metadata.get("source_url") or "",
        "authors": paper.authors or [],
        "published_date": _fmt_date(paper.published_date),
        "published_date_iso": (paper.published_date[:10] if paper.published_date else ""),
        "published_venue": paper.venue or "",
        **conference_fields,
        "abstract": _sanitize_abstract(clean_extracted_text(paper.abstract)),
        "codebase_url": paper.codebase_url or "",
        "extraction_model": paper.extraction_model or "",
        "has_results": has_results,
        "paper_type": paper_type,
        "proposed_models": proposed_models,
        "mrr": mrr,
        "adjusted_mrr": adjusted_mrr,
        "mrr_dataset_count": mrr_dataset_count,
        "benchmark_categories": benchmark_categories,
        "benchmark_coverage": benchmark_coverage,
        "task_categories": task_categories,
        "experiment_scopes": experiment_scopes,
        "results": results_for_fm,
        "results_grouped": grouped_results,
        "datasets_by_scope": datasets_by_scope,
    }
    if single_proposed_model:
        front_matter["single_proposed_model"] = single_proposed_model
    if main_figure_hugo:
        front_matter["main_figure"] = main_figure_hugo

    _write_md(out_path, front_matter)
    return True


# ── Dataset export ────────────────────────────────────────────────────────────


def _dedup_shared_results(groups: list[dict], primary_metric: str) -> list[dict]:
    """Remove duplicate baseline entries — keep only the oldest paper per (model, value-cluster).

    When multiple papers cite the same baseline result (same model, overlapping value
    within std), only the oldest paper's entry is shown. Entries with no primary-metric
    value are always kept unchanged.

    Args:
        groups: list of group dicts, each containing ``_vals`` and ``date_iso``.
        primary_metric: the metric name used to compare values.

    Returns:
        Deduplicated list in original order (dates resolved, then re-sorted by caller).
    """
    # Sort oldest-first so the first occurrence of a (model, value-cluster) wins.
    date_sorted = sorted(
        enumerate(groups),
        key=lambda t: (t[1].get("date_iso") or "9999", t[1].get("arxiv_id", "")),
    )

    keep_indices: set[int] = set()
    seen_model_vals: dict[str, list[tuple[float, float]]] = {}  # model → [(val, std), …]

    for orig_idx, g in date_sorted:
        model = g["model"]
        val, std = g["_vals"].get(primary_metric, (None, None))
        if val is None:
            keep_indices.add(orig_idx)
            continue
        std_f: float = std or 0.0
        prev = seen_model_vals.get(model, [])
        if any(abs(val - pv) <= std_f + ps for pv, ps in prev):
            continue  # duplicate — skip this paper's entry
        keep_indices.add(orig_idx)
        seen_model_vals.setdefault(model, []).append((val, std_f))

    return [g for i, g in enumerate(groups) if i in keep_indices]


def _build_multi_metric_rows(
    all_results: list,
    primary_metric: str,
) -> tuple[list[str], bool, list[dict]]:
    """Pivot results by (canonical_model_name, arxiv_id) to produce a multi-metric table.

    Returns:
        metrics_ordered  – metric names, primary metric first then alphabetically
        higher_is_better – derived from primary metric rows
        rows             – one dict per (model, paper) with parallel metric_values / metric_stds
    """
    # Discover all distinct metrics; primary goes first
    metric_set: set[str] = {r.metric_name for r in all_results}
    metrics_ordered = sorted(metric_set - {primary_metric})
    if primary_metric in metric_set:
        metrics_ordered = [primary_metric] + metrics_ordered

    # higher_is_better from the primary metric rows
    hib = True
    for r in all_results:
        if r.metric_name == primary_metric and r.higher_is_better is not None:
            hib = bool(r.higher_is_better)
            break

    # Group by (canonical_model_name, arxiv_id)
    groups: dict[tuple, dict] = {}
    for r in all_results:
        model_name = _sanitize_model(
            r.model.canonical_name if r.model else "",
            r.paper.arxiv_id if r.paper else None,
        )
        paper = r.paper
        arxiv_id = paper.arxiv_id if paper else ""
        key = (model_name, arxiv_id)
        if key not in groups:
            conference_fields = _conference_export_fields(
                paper.venue if paper else None,
                paper.published_date if paper else None,
            )
            groups[key] = {
                "model": model_name,
                "model_plain": _plain_model(model_name),
                "is_baseline": bool(r.is_baseline),
                "is_overridden": bool(r.is_overridden),
                "override_reason": r.override_reason or "",
                "params_millions": _result_params_millions(r),
                **_result_architecture_fields(r),
                "arxiv_id": arxiv_id,
                "title": _sanitize_title(paper.title if paper else ""),
                "date": _fmt_date(paper.published_date) if paper else "",
                "date_iso": (paper.published_date[:10] if paper and paper.published_date else ""),
                "date_display": _fmt_month_year(paper.published_date) if paper else "",
                "codebase_url": paper.codebase_url or "",
                "published_conference": conference_fields["published_conference"],
                "uses_external_data": None,
                "_vals": {},
            }
        # uses_external_data: prefer True > False > None across metrics for this (model, paper)
        ued = r.uses_external_data
        if ued == 1:
            groups[key]["uses_external_data"] = True
        elif ued == 0 and groups[key]["uses_external_data"] is None:
            groups[key]["uses_external_data"] = False
        val = float(r.display_value) if r.display_value is not None else None
        std = float(r.metric_std) if r.metric_std is not None else None
        groups[key]["_vals"][r.metric_name] = (val, std)

    # Sort by primary metric value
    def _sort_key(g: dict) -> tuple:
        pval = g["_vals"].get(primary_metric, (None, None))[0]
        if pval is None:
            return (1, 0.0)
        return (0, -pval if hib else pval)

    # Deduplicate: when multiple papers report the same model with an overlapping
    # primary-metric value (within std), keep only the oldest paper's entry.
    unique_groups = _dedup_shared_results(list(groups.values()), primary_metric)

    sorted_groups = sorted(unique_groups, key=_sort_key)

    _mark_is_best(
        sorted_groups,
        primary_metric,
        hib,
        lambda g: g["_vals"].get(primary_metric, (None, None))[0],
        lambda g: g["_vals"].get(primary_metric, (None, None))[1],
    )
    _mark_std_outliers(
        sorted_groups,
        lambda g: g["_vals"].get(primary_metric, (None, None))[1],
    )

    rows: list[dict] = []
    for g in sorted_groups:
        metric_values = []
        metric_stds = []
        for m in metrics_ordered:
            val, std = g["_vals"].get(m, (None, None))
            metric_values.append(val)
            metric_stds.append(std)
        row = {k: v for k, v in g.items() if k != "_vals"}
        row["metric_values"] = metric_values
        row["metric_stds"] = metric_stds
        rows.append(row)  # is_best already set by _mark_is_best above

    return metrics_ordered, hib, rows


def _dataset_page_result_count(session: Any, dataset_id: int) -> int:
    """Compute dataset result_count exactly as used on dataset pages.

    This keeps landing-page counts aligned with per-dataset pages.
    """
    return int(_dataset_page_export_metadata(session, dataset_id)["result_count"])


def export_dataset(dataset_id: int, *, session: Session | None = None) -> bool:
    """Export a dataset page with all variants and leaderboard data."""
    if session is not None:
        return _export_dataset_impl(session, dataset_id)
    with session_scope() as scoped:
        return _export_dataset_impl(scoped, dataset_id)


def _export_dataset_impl(session: Session, dataset_id: int) -> bool:
    ds = (
        session.query(Dataset)
        .options(joinedload(Dataset.benchmark))
        .filter_by(id=dataset_id)
        .first()
    )
    if ds is None:
        return False

    variants = session.query(DatasetVariant).filter_by(dataset_id=dataset_id).all()
    variants = sorted(
        variants,
        key=lambda variant: (
            0 if variant.is_standard else 1,
            variant.num_graphs if variant.num_graphs is not None else 10**18,
            variant.avg_nodes if variant.avg_nodes is not None else 10**18,
            variant.name.lower(),
        ),
    )

    if not variants:
        logger.debug("Dataset %s has no variants — skipping export", ds.name)
        _DATASET_EXPORT_META_CACHE[dataset_id] = {
            "exportable": False,
            "result_count": 0,
            "recent_result_count": 0,
        }
        return False

    force_export = _dataset_force_export(ds.name)

    # Determine primary metric from the first variant that has results.
    # For forced empty exports, fall back to the dataset-level direction.
    primary_metric = ds.primary_metric or ""
    higher_is_better = bool(ds.higher_is_better) if ds.higher_is_better is not None else True

    variant_data: list[dict] = []
    for v in variants:
        all_results = (
            session.query(Result)
            .options(*_DATASET_RESULT_LOAD_OPTIONS)
            .filter_by(dataset_variant_id=v.id)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .all()
        )

        if not all_results and not force_export:
            continue

        if not all_results:
            variant_data.append(
                {
                    "slug": _slug(v.name),
                    "name": v.name,
                    "notes": v.notes or "",
                    "is_standard": bool(v.is_standard),
                    "primary_metric": primary_metric,
                    "higher_is_better": bool(ds.higher_is_better),
                    "stats": {
                        "num_graphs": v.num_graphs,
                        "avg_nodes": v.avg_nodes,
                        "avg_edges": v.avg_edges,
                    },
                    "metrics": [primary_metric] if primary_metric else [],
                    "rows": [],
                    "milestones": [],
                }
            )
            continue

        # Determine which metric to display: prefer primary_metric if it exists in results
        available_metrics = {r.metric_name for r in all_results}
        if primary_metric and primary_metric in available_metrics:
            metric = primary_metric
        else:
            # Fall back to the most-common metric among results
            from collections import Counter

            metric = Counter(r.metric_name for r in all_results).most_common(1)[0][0]
            if not primary_metric:
                primary_metric = metric

        # Build pivoted multi-metric rows (primary metric first, then sorted)
        metrics_ordered, higher_is_better, rows = _build_multi_metric_rows(all_results, metric)

        # Optional dataset-level display metric filtering (e.g. Texas -> Accuracy only)
        display_metrics = _dataset_display_metrics(ds.name)
        metrics_ordered, rows, metric = _apply_display_metrics_filter(
            metrics_ordered,
            rows,
            display_metrics,
            metric,
        )

        milestones = get_best_results_over_time(v.id, metric, session=session)

        variant_data.append(
            {
                "slug": _slug(v.name),
                "name": v.name,
                "notes": v.notes or "",
                "is_standard": bool(v.is_standard),
                "primary_metric": metric,
                "higher_is_better": higher_is_better,
                "stats": {
                    "num_graphs": v.num_graphs,
                    "avg_nodes": v.avg_nodes,
                    "avg_edges": v.avg_edges,
                },
                "metrics": metrics_ordered,
                "rows": rows,
                "milestones": milestones,
            }
        )

    if not variant_data:
        _DATASET_EXPORT_META_CACHE[dataset_id] = {
            "exportable": False,
            "result_count": 0,
            "recent_result_count": 0,
        }
        return False

    # Compute overview stats from the standard (or first) variant
    std_vd = next((v for v in variant_data if v["is_standard"]), variant_data[0])
    result_count = len(std_vd["rows"])
    recent_result_count = _count_recent_leaderboard_rows(std_vd["rows"])
    best_row = std_vd["rows"][0] if std_vd["rows"] else None
    best_model_info: dict | None = None
    if best_row:
        primary_val = (
            best_row["metric_values"][0] if best_row.get("metric_values") else best_row.get("value")
        )
        best_model_info = {
            "model": best_row["model"],
            "value": primary_val,
            "metric": std_vd["primary_metric"],
            "arxiv_id": best_row.get("arxiv_id") or "",
            "paper_title": best_row.get("title") or "",
        }

    # Dataset-level stats are often missing; fall back to the standard variant stats.
    std_variant = next((v for v in variants if v.is_standard), variants[0])
    stats_num_graphs = ds.num_graphs if ds.num_graphs is not None else std_variant.num_graphs
    stats_avg_nodes = ds.avg_nodes if ds.avg_nodes is not None else std_variant.avg_nodes
    stats_avg_edges = ds.avg_edges if ds.avg_edges is not None else std_variant.avg_edges
    stats_num_classes = _summary_num_classes(ds)

    benchmark_name = ds.benchmark.name if ds.benchmark else ""
    front_matter: dict[str, Any] = {
        "title": ds.name,
        "slug": _slug(ds.name),
        "benchmark": benchmark_name,
        "task_type": ds.task_type or "",
        "description": ds.description or "",
        "primary_metric": primary_metric,
        "higher_is_better": higher_is_better,
        "pyg_url": ds.pyg_url or "",
        "stats": (
            {
                "num_graphs": stats_num_graphs,
                "avg_nodes": round(stats_avg_nodes, 2) if stats_avg_nodes is not None else None,
                "avg_edges": round(stats_avg_edges, 2) if stats_avg_edges is not None else None,
                "num_classes": stats_num_classes,
            }
            if any(
                x is not None
                for x in [stats_num_graphs, stats_avg_nodes, stats_avg_edges, stats_num_classes]
            )
            else None
        ),
        "result_count": result_count,
        "best_model": best_model_info,
        "variants": variant_data,
    }

    out_path = _CONTENT / "datasets" / _slug(ds.name) / "index.md"
    _write_md(out_path, front_matter)
    _DATASET_EXPORT_META_CACHE[dataset_id] = {
        "exportable": True,
        "result_count": result_count,
        "recent_result_count": recent_result_count,
    }
    return True


# ── Benchmark data file ───────────────────────────────────────────────────────


def export_benchmarks_data(*, session: Session | None = None) -> None:
    """Write site/data/benchmarks.json for the homepage."""

    _DATA_DIR.mkdir(parents=True, exist_ok=True)

    if session is not None:
        _export_benchmarks_data_impl(session)
        return
    with session_scope() as scoped:
        _export_benchmarks_data_impl(scoped)


def _export_benchmarks_data_impl(session: Session) -> None:
    # Result count per dataset aligned with exported dataset pages.
    dataset_export_metadata: dict[int, dict[str, Any]] = {
        ds.id: _dataset_export_metadata(session, ds.id) for ds in session.query(Dataset).all()
    }
    ds_result_counts: dict[int, int] = {
        dataset_id: int(meta["result_count"])
        for dataset_id, meta in dataset_export_metadata.items()
        if meta["exportable"]
    }
    ds_recent_result_counts: dict[int, int] = {
        dataset_id: int(meta.get("recent_result_count", 0))
        for dataset_id, meta in dataset_export_metadata.items()
        if meta["exportable"]
    }

    benchmarks = session.query(Benchmark).all()

    def _bm_recent_per_dataset(b: Benchmark) -> float:
        exportable = [
            ds for ds in b.datasets if dataset_export_metadata.get(ds.id, {}).get("exportable")
        ]
        if not exportable:
            return 0.0
        total_recent = sum(ds_recent_result_counts.get(ds.id, 0) for ds in exportable)
        return total_recent / len(exportable)

    benchmarks = sorted(benchmarks, key=_bm_recent_per_dataset, reverse=True)

    data: list[dict] = []
    for b in benchmarks:
        # Sort datasets within this benchmark by cumulated result count (descending)
        sorted_datasets = sorted(
            [ds for ds in b.datasets if dataset_export_metadata.get(ds.id, {}).get("exportable")],
            key=lambda ds: -ds_result_counts.get(ds.id, 0),
        )
        if not sorted_datasets:
            continue
        recent_per_dataset = _bm_recent_per_dataset(b)
        datasets_info = []
        for ds in sorted_datasets:
            variants = ds.variants  # all variants (not just standard)
            datasets_info.append(
                {
                    "name": ds.name,
                    "slug": _slug(ds.name),
                    "task_type": ds.task_type or "",
                    "result_count": ds_result_counts.get(ds.id, 0),
                    "recent_result_count": ds_recent_result_counts.get(ds.id, 0),
                    "variants": [{"name": v.name, "slug": _slug(v.name)} for v in variants],
                }
            )
        data.append(
            {
                "name": b.name,
                "slug": _slug(b.name),
                "description": b.description or "",
                "arxiv_id": b.paper.arxiv_id if b.paper else "",
                "paper_title": _sanitize_title(b.paper.title) if b.paper else "",
                "recent_results_per_dataset": round(recent_per_dataset, 1),
                "datasets": datasets_info,
            }
        )

    (_DATA_DIR / "benchmarks.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def export_development_data(*, session: Session | None = None) -> dict[str, int]:
    """Write development data files for debugging/admin purposes."""
    from backend.hugo_dev_exports import export_development_data as _export_development_data

    if session is not None:
        return _export_development_data(session=session)
    with session_scope() as scoped:
        return _export_development_data(session=scoped)


def _create_dev_pages() -> None:
    """Compatibility wrapper for the dedicated dev-export module."""
    from backend.hugo_dev_exports import create_dev_pages

    create_dev_pages()


# ── Full export ───────────────────────────────────────────────────────────────


def _print_export_timing_summary(
    *,
    timings: dict[str, float],
    datasets_ok: int,
    datasets_total: int,
    papers_ok: int,
    papers_total: int,
    skip_development: bool,
    dev_stats: dict[str, int] | None = None,
) -> None:
    from tqdm import tqdm

    total = sum(timings.values())
    tqdm.write("")
    tqdm.write("Export timing summary")
    tqdm.write(
        f"  datasets:     {timings.get('datasets', 0.0):7.1f}s  "
        f"({datasets_ok}/{datasets_total} pages written)"
    )
    tqdm.write(f"  benchmarks:   {timings.get('benchmarks', 0.0):7.1f}s  (homepage JSON)")
    if not skip_development:
        dev_line = f"  development:  {timings.get('development', 0.0):7.1f}s"
        if dev_stats:
            dev_line += (
                f"  ({dev_stats.get('pages', 0)} pages in site/content/dev, "
                f"{dev_stats.get('data_files', 0)} JSON in site/data)"
            )
        tqdm.write(dev_line)
    tqdm.write(
        f"  papers:       {timings.get('papers', 0.0):7.1f}s  "
        f"({papers_ok}/{papers_total} pages written)"
    )
    tqdm.write(f"  total:        {total:7.1f}s")


def export_all(
    arxiv_ids: list[str] | None = None,
    *,
    skip_development: bool = False,
) -> None:
    """Export all papers and datasets (or just the specified papers)."""
    import time

    from tqdm import tqdm

    init_db()
    clear_export_caches()

    with session_scope() as session:
        papers = _query_exportable_papers(session, arxiv_ids=arxiv_ids)
        paper_ids = [p.arxiv_id for p in papers]
        dataset_ids = [ds.id for ds in session.query(Dataset).all()]

    timings: dict[str, float] = {}
    dev_stats: dict[str, int] | None = None

    with session_scope() as session:
        ds_ok = 0
        t0 = time.perf_counter()
        for did in tqdm(dataset_ids, desc="Exporting datasets", unit="dataset", leave=True):
            if export_dataset(did, session=session):
                ds_ok += 1
        timings["datasets"] = time.perf_counter() - t0

        benchmarks = session.query(Benchmark).all()
        _benchmark_totals_exportable(session, benchmarks)

        t0 = time.perf_counter()
        export_benchmarks_data(session=session)
        timings["benchmarks"] = time.perf_counter() - t0

        if not skip_development:
            tqdm.write("Development pages...")
            t0 = time.perf_counter()
            dev_stats = export_development_data(session=session)
            elapsed = time.perf_counter() - t0
            timings["development"] = elapsed
            tqdm.write(
                f"Development pages... done ({elapsed:.1f}s)  "
                f"({dev_stats.get('pages', 0)} pages, {dev_stats.get('data_files', 0)} JSON)"
            )

        papers_ok = 0
        t0 = time.perf_counter()
        for arxiv_id in tqdm(paper_ids, desc="Exporting papers", unit="paper", leave=True):
            if export_paper(arxiv_id, session=session):
                papers_ok += 1
        timings["papers"] = time.perf_counter() - t0

        t0 = time.perf_counter()
        from backend.hugo_dev_exports import create_conferences_page

        create_conferences_page(session=session)
        timings["conferences"] = time.perf_counter() - t0

    _print_export_timing_summary(
        timings=timings,
        datasets_ok=ds_ok,
        datasets_total=len(dataset_ids),
        papers_ok=papers_ok,
        papers_total=len(paper_ids),
        skip_development=skip_development,
        dev_stats=dev_stats,
    )


# ── CLI ───────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Export DB to Hugo content files")
    parser.add_argument(
        "--paper", "-p", nargs="+", metavar="ARXIV_ID", help="Export only specific papers"
    )
    parser.add_argument(
        "--skip-dev",
        action="store_true",
        help="Skip development/admin Hugo data export",
    )
    args = parser.parse_args(argv)
    export_all(arxiv_ids=args.paper, skip_development=args.skip_dev)


if __name__ == "__main__":
    main()
