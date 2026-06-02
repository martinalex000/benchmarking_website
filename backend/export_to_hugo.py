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
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

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
_PAPER_PARAM_CACHE: dict[str, dict[str, float]] = {}
_CONFERENCE_ALIASES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("NeurIPS", ("neurips", "nips")),
    ("ICLR", ("iclr",)),
    ("TMLR", ("tmlr", "transactions on machine learning research")),
    ("ICML", ("icml", "international conference on machine learning")),
    ("LoG", ("log", "learning on graphs", "graph learning")),
    ("AAAI", ("aaai",)),
    ("KDD", ("kdd", "sigkdd")),
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
        if any(alias in lowered for alias in aliases):
            return label
    return raw


def _is_bounded_metric(metric_name: str | None) -> bool:
    key = (metric_name or "").strip().lower()
    return any(sub in key for sub in _BOUNDED_METRIC_SUBSTRINGS)


def _normalize_model_family(model_name: str | None) -> str:
    raw = (model_name or "").strip().lower()
    if re.match(r"^gcn(?:\s|\(|$)", raw):
        return "gcn"
    if re.match(r"^gin(?:\s|\(|$)", raw):
        return "gin"
    if re.match(r"^(?:graphsage|sage)(?:\s|\(|$)", raw):
        return "sage"
    if re.match(r"^mlp(?:\s|\(|$)", raw):
        return "mlp"
    return ""


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


def _paper_explicit_param_map(arxiv_id: str | None) -> dict[str, float]:
    if not arxiv_id:
        return {}
    if arxiv_id in _PAPER_PARAM_CACHE:
        return _PAPER_PARAM_CACHE[arxiv_id]

    mapping: dict[str, float] = {}
    try:
        storage = PaperStorage(arxiv_id)
        if storage.llm_output_path.exists():
            raw = storage.load_llm_output()
            results = raw.get("results", {})
            candidates: list[dict[str, Any]] = []
            proposed = results.get("proposed_model")
            if isinstance(proposed, dict):
                candidates.append(proposed)
            baselines = results.get("baseline_models") or []
            if isinstance(baselines, list):
                candidates.extend(item for item in baselines if isinstance(item, dict))

            for item in candidates:
                name = str(item.get("name") or "").strip()
                params = item.get("params_millions")
                if not name or params is None:
                    continue
                rendered = _sanitize_model(name, arxiv_id)
                plain = _plain_model(rendered)
                value = float(params)
                mapping[rendered.lower()] = value
                mapping[plain.lower()] = value
    except Exception as exc:
        logger.debug("Could not load paper-local param sizes for %s: %s", arxiv_id, exc)

    _PAPER_PARAM_CACHE[arxiv_id] = mapping
    return mapping


def _paper_explicit_param_millions(arxiv_id: str | None, model_name: str | None) -> float | None:
    if not arxiv_id or not model_name:
        return None
    return _paper_explicit_param_map(arxiv_id).get(str(model_name).strip().lower())


def _result_params_millions(
    result: Result | None,
    arxiv_id: str | None,
    model_name: str | None,
) -> float | None:
    if result is not None and result.params_millions is not None:
        return float(result.params_millions)
    return _paper_explicit_param_millions(arxiv_id, model_name)


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
        return {"exportable": False, "result_count": 0}

    variants = (
        session.query(DatasetVariant)
        .filter_by(dataset_id=dataset_id)
        .order_by(DatasetVariant.is_standard.desc(), DatasetVariant.name)
        .all()
    )
    if not variants:
        return {"exportable": False, "result_count": 0}

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
        variant_counts.append((bool(v.is_standard), len(rows)))

    if not exportable:
        return {"exportable": False, "result_count": 0}

    std_count = next((count for is_std, count in variant_counts if is_std), None)
    result_count = (
        std_count if std_count is not None else (variant_counts[0][1] if variant_counts else 0)
    )
    return {"exportable": True, "result_count": result_count}


def _paper_experiment_scope(task_type: str | None) -> str | None:
    task_key = (task_type or "").strip().lower()
    if task_key.startswith("node_"):
        return "node-level"
    if task_key.startswith("graph_"):
        return "graph-level"
    if task_key.startswith("edge_") or task_key == "link_prediction":
        return "edge-level"
    return None


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


def _write_md(path: Path, front_matter: dict, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_str = yaml.dump(front_matter, allow_unicode=True, default_flow_style=False, sort_keys=False)
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
    if primary_metric and primary_metric in seen_metrics:
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
            "params_millions": _result_params_millions(
                r,
                p.arxiv_id if p else None,
                rendered_name,
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
        .filter_by(paper_id=paper.id, is_baseline=False)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )
    if not results:
        return None, None, 0, []

    proposed_models: list[str] = list(
        dict.fromkeys(r.model.canonical_name for r in results if r.model and r.model.canonical_name)
    )

    # Identify the single primary proposed model from the LLM extraction JSON.
    # This avoids inflating MRR via ablation variants that are also non-baseline.
    primary_proposed: str | None = None
    try:
        from backend.paper_storage import PaperStorage

        storage = PaperStorage(paper.arxiv_id)
        if storage.llm_output_path.exists():
            raw = storage.load_llm_output()
            proposed_info = raw.get("results", {}).get("proposed_model") or {}
            raw_name = (proposed_info.get("name") or "").strip()
            if raw_name:
                # Match to canonical name using fuzzy lookup against known proposed models
                raw_lower = raw_name.lower()
                # Try exact match first
                for cname in proposed_models:
                    if cname.lower() == raw_lower:
                        primary_proposed = cname
                        break
                # Fall back: pick the proposed model whose canonical name most closely
                # matches the raw name (token_sort_ratio ≥ 80)
                if primary_proposed is None:
                    from thefuzz import fuzz as _fuzz

                    best_score, best_cname = 0, None
                    for cname in proposed_models:
                        score = _fuzz.token_sort_ratio(raw_lower, cname.lower())
                        if score > best_score:
                            best_score, best_cname = score, cname
                    if best_score >= 80:
                        primary_proposed = best_cname
    except Exception:
        pass

    if primary_proposed is None and proposed_models:
        primary_proposed = proposed_models[0]

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
            model_to_rank, global_rows, _ = _global_ranks_for_dataset(
                session, ds_name, info["primary_metric"], info["hib"]
            )
        except Exception:
            continue
        if len(global_rows) < 10:
            continue
        # Require at least 3 distinct papers contributing to this dataset
        from sqlalchemy import func as _sqla_func

        paper_count = (
            session.query(_sqla_func.count(Result.paper_id.distinct()))
            .join(Result.dataset_variant)
            .join(DatasetVariant.dataset)
            .filter(Dataset.name == ds_name)
            .filter(Result.metric_name == info["primary_metric"])
            .scalar()
        ) or 0
        if paper_count < 3:
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
            truth_cache[cache_key] = _global_ranks_for_dataset(
                session, ds.name, primary_metric, higher
            )
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
        mismatches.append(
            {
                "arxiv_id": paper.arxiv_id,
                "title": _sanitize_title(paper.title),
                "paper_date_iso": paper_date_iso,
                "dataset": ds.name,
                "metric": primary_metric,
                "model": _sanitize_model(model.canonical_name, paper.arxiv_id),
                "paper_value": paper_value,
                "paper_std": paper_std,
                "true_value": true_value,
                "true_std": truth.get("std"),
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


def export_paper(arxiv_id: str) -> bool:
    """Export a single paper's page to Hugo content."""
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            logger.warning("Paper arXiv:%s not found in DB", arxiv_id)
            return False

        results = (
            session.query(Result)
            .filter_by(paper_id=paper.id)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .all()
        )

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
                    "params_millions": _result_params_millions(
                        r,
                        paper.arxiv_id if paper else None,
                        rendered_model,
                    ),
                    **_result_architecture_fields(r),
                    "uses_external_data": r.uses_external_data,
                    "table_ref": r.table_ref or "",
                    "source_ref": r.source_ref or "",
                    "variant_inference_reason": r.variant_inference_reason or "",
                    "date": _fmt_date(paper.published_date) if paper else "",
                    "date_display": _fmt_month_year(paper.published_date) if paper else "",
                    "date_iso": (
                        paper.published_date[:10] if paper and paper.published_date else ""
                    ),
                    "published_venue": paper.venue if paper else "",
                }
            )

        results_for_fm: list[dict] = []
        for ds, rows in sorted(result_groups.items()):
            meta = result_group_meta[ds]
            primary_metric = meta["metric"]
            higher = meta["higher_is_better"]
            distinct_metrics = list(dict.fromkeys(r["metric"] for r in rows if r.get("metric")))

            # Global ranking for this dataset (best result per model, all papers)
            try:
                model_to_rank, global_top_all, truth_map = _global_ranks_for_dataset(
                    session, ds, primary_metric, higher
                )
            except Exception as _exc:
                logger.debug("Global rank lookup failed for %r: %s", ds, _exc)
                model_to_rank, global_top_all, truth_map = {}, [], {}

            for row in rows:
                truth = truth_map.get(row.get("model_key", ""))
                row["global_rank"] = model_to_rank.get(row.get("model_key", ""))
                if row.get("metric") != primary_metric or not truth:
                    row["sort_value"] = row.get("value")
                    row["sort_std"] = row.get("std")
                    continue
                row["true_value"] = truth.get("value")
                row["true_std"] = truth.get("std")
                row["value_gap_source_arxiv"] = truth.get("arxiv_id", "")
                row["value_gap_source_title"] = truth.get("title", "")
                row["value_gap_source_is_current_paper"] = truth.get("arxiv_id", "") == arxiv_id
                row["has_value_gap"] = _has_paper_value_gap(
                    row.get("paper_value"),
                    row.get("paper_std"),
                    row.get("true_value"),
                    row.get("true_std"),
                )
                row["has_value_note"] = _has_paper_value_difference(
                    row.get("paper_value"), row.get("true_value")
                ) and not row.get("has_value_gap")
                row["value_gap"] = (
                    abs(row["paper_value"] - row["true_value"])
                    if _has_paper_value_difference(row.get("paper_value"), row.get("true_value"))
                    and row.get("paper_value") is not None
                    and row.get("true_value") is not None
                    else None
                )
                row["value_note"] = (
                    f"global {row['true_value']:.4f} within std"
                    if row.get("has_value_note") and row.get("true_value") is not None
                    else ""
                )
                row["paper_rank"] = _rank_for_value(
                    global_top_all,
                    row.get("model_key", ""),
                    row.get("paper_value"),
                    higher,
                )
                row["rank_delta"] = (
                    row["paper_rank"] - row["global_rank"]
                    if row.get("paper_rank") is not None and row.get("global_rank") is not None
                    else None
                )
                row["rank_delta_abs"] = (
                    abs(row["rank_delta"]) if row.get("rank_delta") is not None else None
                )
                if row.get("rank_delta") is not None:
                    if row["rank_delta"] < 0:
                        row["rank_delta_direction"] = "better"
                    elif row["rank_delta"] > 0:
                        row["rank_delta_direction"] = "worse"
                    else:
                        row["rank_delta_direction"] = "same"
                row["sort_value"] = row.get("true_value")
                row["sort_std"] = row.get("true_std")

                # Compute comparison context for the comparison column
                paper_date = row.get("date_iso", "")
                source_date = truth.get("date_iso", "")
                paper_val = row.get("paper_value")
                true_val = truth.get("value")
                paper_std = row.get("paper_std")
                true_std = truth.get("std")

                if row.get("is_baseline") and paper_val is not None and true_val is not None:
                    # Compare this baseline against the global best
                    better_than_global = (higher and paper_val > true_val) or (
                        not higher and paper_val < true_val
                    )
                    # Check if values overlap within std
                    delta = abs(paper_val - true_val)
                    std_overlap = (
                        (delta <= (paper_std or 0) + (true_std or 0))
                        if paper_std is not None or true_std is not None
                        else (delta <= 1e-12)
                    )

                    if better_than_global:
                        # This baseline improved over the previous global best
                        row["comparison_type"] = "improved"
                        row["comparison_source_title"] = truth.get("title", "")
                        row["comparison_source_arxiv"] = truth.get("arxiv_id", "")
                    elif paper_date and source_date and source_date <= paper_date and std_overlap:
                        # Same or overlapping result from an older paper
                        row["comparison_type"] = "matches"
                        row["comparison_source_title"] = truth.get("title", "")
                        row["comparison_source_arxiv"] = truth.get("arxiv_id", "")
                    elif source_date and paper_date and source_date < paper_date:
                        # The global best comes from an older paper — worse result
                        row["comparison_type"] = "behind"
                        row["comparison_source_title"] = truth.get("title", "")
                        row["comparison_source_arxiv"] = truth.get("arxiv_id", "")
                    elif source_date and source_date > paper_date:
                        # Future paper has the best result — this baseline was behind
                        row["comparison_type"] = "behind"
                        row["comparison_source_title"] = truth.get("title", "")
                        row["comparison_source_arxiv"] = truth.get("arxiv_id", "")
                    else:
                        row["comparison_type"] = None
                        row["comparison_source_title"] = ""
                        row["comparison_source_arxiv"] = ""
                elif row.get("is_global_top"):
                    row["comparison_type"] = "global_top"
                    row["comparison_source_title"] = ""
                    row["comparison_source_arxiv"] = ""
                else:
                    row["comparison_type"] = None
                    row["comparison_source_title"] = ""
                    row["comparison_source_arxiv"] = ""

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
                    "rank_delta",
                    "comparison_type",
                    "comparison_source_title",
                    "comparison_source_arxiv",
                ),
            )

            if len(distinct_metrics) > 1:
                pivoted = _pivot_paper_rows(rows, primary_metric)
                pv_rows = pivoted["rows"]
                metrics_list = pivoted["metrics"]

                # Attach global ranks to pivoted rows
                paper_models: set[str] = {pr.get("model_key", "") for pr in pv_rows}
                for pr in pv_rows:
                    pr["global_rank"] = model_to_rank.get(pr.get("model_key", ""))

                # Inject up to 3 global-top models not in this paper
                extra_rows: list[dict] = []
                n_metrics = len(metrics_list)
                for gr in global_top_all:
                    if gr["model_key"] not in paper_models:
                        mv = [gr["value"] if i == 0 else None for i in range(n_metrics)]
                        ms = [gr["std"] if i == 0 else None for i in range(n_metrics)]
                        extra_rows.append(
                            {
                                "model": gr["model"],
                                "model_key": gr["model_key"],
                                "model_plain": gr.get("model_plain") or _plain_model(gr["model"]),
                                "metric_values": mv,
                                "metric_stds": ms,
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
                        )
                        if len(extra_rows) >= 3:
                            break

                if extra_rows:
                    combined = pv_rows + extra_rows

                    def _pv_sort(r: dict, _hib: bool = higher) -> tuple:
                        v = r.get("sort_value")
                        if v is None:
                            v = r["metric_values"][0] if r.get("metric_values") else None
                        if v is None:
                            return (1, 0.0)
                        return (0, -v if _hib else v)

                    combined.sort(key=_pv_sort)
                    _mark_is_best(
                        combined,
                        primary_metric,
                        higher,
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

                results_for_fm.append(
                    {
                        "dataset": ds,
                        "is_multi_metric": True,
                        "rows": pv_rows,
                        "metrics": metrics_list,
                        "primary_metric": pivoted["primary_metric"],
                        "higher_is_better": higher,
                    }
                )
            else:

                def _row_sort_key(r: dict, _hib: bool = higher) -> tuple:
                    v = r.get("sort_value")
                    if v is None:
                        v = r.get("value")
                    if v is None:
                        return (1, 0.0)
                    return (0, -float(v) if _hib else float(v))

                rows.sort(key=_row_sort_key)

                # Attach global ranks to paper rows
                paper_models = {r.get("model_key", "") for r in rows}

                # Inject up to 3 global-top models not in this paper
                extra_rows = []
                for gr in global_top_all:
                    if gr["model_key"] not in paper_models:
                        extra_rows.append(gr)
                        if len(extra_rows) >= 3:
                            break

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
                    primary_metric,
                    higher,
                    lambda r: (
                        r.get("sort_value") if r.get("sort_value") is not None else r.get("value")
                    ),
                    lambda r: r.get("sort_std") if r.get("sort_std") is not None else r.get("std"),
                )
                _mark_std_outliers(
                    rows,
                    lambda r: r.get("sort_std") if r.get("sort_std") is not None else r.get("std"),
                )
                results_for_fm.append(
                    {
                        "dataset": ds,
                        "rows": rows,
                        "metric": primary_metric,
                        "higher_is_better": higher,
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

        # Main figure
        storage = PaperStorage(arxiv_id)
        paper_metadata = storage.read_metadata()
        main_figure_hugo: str | None = None
        if storage.main_figure_path and storage.main_figure_path.exists():
            dest = _STATIC / "figures" / arxiv_id / storage.main_figure_path.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(storage.main_figure_path, dest)
            main_figure_hugo = f"/figures/{arxiv_id}/{storage.main_figure_path.name}"

        mrr, adjusted_mrr, mrr_dataset_count, proposed_models = _compute_paper_mrr(session, paper)
        has_results = bool(results_for_fm)

        # Single proposed model: if all proposed results come from the same canonical name
        single_proposed_model: str | None = None
        if len(proposed_models) == 1:
            single_proposed_model = proposed_models[0]

        benchmark_categories = [group["benchmark"] for group in grouped_results]
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
            "published_conference": _normalize_conference(paper.venue),
            "published_conference_slug": _slug(_normalize_conference(paper.venue)),
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
            "task_categories": task_categories,
            "experiment_scopes": experiment_scopes,
            "results": results_for_fm,
            "results_grouped": grouped_results,
        }
        if single_proposed_model:
            front_matter["single_proposed_model"] = single_proposed_model
        if main_figure_hugo:
            front_matter["main_figure"] = main_figure_hugo

        out_path = _CONTENT / "papers" / arxiv_id / "index.md"
        _write_md(out_path, front_matter)
        logger.info("Exported paper %s → %s", arxiv_id, out_path)
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
            groups[key] = {
                "model": model_name,
                "model_plain": _plain_model(model_name),
                "is_baseline": bool(r.is_baseline),
                "is_overridden": bool(r.is_overridden),
                "override_reason": r.override_reason or "",
                "params_millions": _result_params_millions(r, arxiv_id, model_name),
                **_result_architecture_fields(r),
                "arxiv_id": arxiv_id,
                "title": _sanitize_title(paper.title if paper else ""),
                "date": _fmt_date(paper.published_date) if paper else "",
                "date_iso": (paper.published_date[:10] if paper and paper.published_date else ""),
                "date_display": _fmt_month_year(paper.published_date) if paper else "",
                "codebase_url": paper.codebase_url or "",
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


def export_dataset(dataset_id: int) -> bool:
    """Export a dataset page with all variants and leaderboard data."""
    with session_scope() as session:
        ds = session.get(Dataset, dataset_id)
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

            milestones = get_best_results_over_time(v.id, metric)

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
            return False

        # Compute overview stats from the standard (or first) variant
        std_vd = next((v for v in variant_data if v["is_standard"]), variant_data[0])
        result_count = len(std_vd["rows"])
        best_row = std_vd["rows"][0] if std_vd["rows"] else None
        best_model_info: dict | None = None
        if best_row:
            primary_val = (
                best_row["metric_values"][0]
                if best_row.get("metric_values")
                else best_row.get("value")
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
        logger.info("Exported dataset %s → %s", ds.name, out_path)
        return True


# ── Benchmark data file ───────────────────────────────────────────────────────


def export_benchmarks_data() -> None:
    """Write site/data/benchmarks.json for the homepage."""

    _DATA_DIR.mkdir(parents=True, exist_ok=True)

    with session_scope() as session:
        # Result count per dataset aligned with exported dataset pages.
        dataset_export_metadata: dict[int, dict[str, Any]] = {
            ds.id: _dataset_page_export_metadata(session, ds.id)
            for ds in session.query(Dataset).all()
        }
        ds_result_counts: dict[int, int] = {
            dataset_id: int(meta["result_count"])
            for dataset_id, meta in dataset_export_metadata.items()
            if meta["exportable"]
        }

        benchmarks = session.query(Benchmark).all()

        # Sort benchmark groups by total result count (descending)
        def _bm_total(b: Benchmark) -> int:
            return sum(ds_result_counts.get(ds.id, 0) for ds in b.datasets)

        benchmarks = sorted(benchmarks, key=_bm_total, reverse=True)

        data: list[dict] = []
        for b in benchmarks:
            # Sort datasets within this benchmark by cumulated result count (descending)
            sorted_datasets = sorted(
                [
                    ds
                    for ds in b.datasets
                    if dataset_export_metadata.get(ds.id, {}).get("exportable")
                ],
                key=lambda ds: -ds_result_counts.get(ds.id, 0),
            )
            if not sorted_datasets:
                continue
            datasets_info = []
            for ds in sorted_datasets:
                variants = ds.variants  # all variants (not just standard)
                datasets_info.append(
                    {
                        "name": ds.name,
                        "slug": _slug(ds.name),
                        "task_type": ds.task_type or "",
                        "result_count": ds_result_counts.get(ds.id, 0),
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
                    "datasets": datasets_info,
                }
            )

    (_DATA_DIR / "benchmarks.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info("Wrote %s", _DATA_DIR / "benchmarks.json")


def export_development_data() -> None:
    """Write development data files for debugging/admin purposes."""
    from backend.hugo_dev_exports import export_development_data as _export_development_data

    _export_development_data()


def _create_dev_pages() -> None:
    """Compatibility wrapper for the dedicated dev-export module."""
    from backend.hugo_dev_exports import create_dev_pages

    create_dev_pages()


# ── Full export ───────────────────────────────────────────────────────────────


def export_all(arxiv_ids: list[str] | None = None) -> None:
    """Export all papers and datasets (or just the specified papers)."""
    from tqdm import tqdm

    init_db()

    export_benchmarks_data()
    export_development_data()

    with session_scope() as session:
        if arxiv_ids:
            papers = session.query(Paper).filter(Paper.arxiv_id.in_(arxiv_ids)).all()
        else:
            papers = session.query(Paper).all()
        paper_ids = [p.arxiv_id for p in papers]

        dataset_ids = [ds.id for ds in session.query(Dataset).all()]

    ok = 0
    for arxiv_id in tqdm(paper_ids, desc="Exporting papers", unit="paper", leave=True):
        if export_paper(arxiv_id):
            tqdm.write(f"  ✓  {arxiv_id}")
            ok += 1
        else:
            tqdm.write(f"  ✗  {arxiv_id}  (skipped — no results)")

    logger.info("Exported %d/%d papers", ok, len(paper_ids))

    ds_ok = 0
    for did in tqdm(dataset_ids, desc="Exporting datasets", unit="dataset", leave=True):
        if export_dataset(did):
            ds_ok += 1

    logger.info("Exported %d/%d datasets", ds_ok, len(dataset_ids))


# ── CLI ───────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Export DB to Hugo content files")
    parser.add_argument(
        "--paper", "-p", nargs="+", metavar="ARXIV_ID", help="Export only specific papers"
    )
    args = parser.parse_args(argv)
    export_all(arxiv_ids=args.paper)


if __name__ == "__main__":
    main()
