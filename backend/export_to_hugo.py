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
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from backend.baseline_aggregator import get_baseline_summary, get_best_results_over_time
from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Paper, Result, TodoPaper
from backend.override_handler import get_model_renames, load_overrides
from backend.paper_storage import PaperStorage
from backend.models import PaperCandidate, PipelineRun

logger = logging.getLogger(__name__)

_SITE_DIR = cfg.base_dir / "site"
_CONTENT = _SITE_DIR / "content"
_DATA_DIR = _SITE_DIR / "data"
_STATIC = _SITE_DIR / "static"

_MODEL_SUFFIX_RE = re.compile(
    r"\s*\(\s*(?:ours?|base(?:line)?|proposed|retuned|re-?eval|none|l\s*=\s*\d+)\s*\)\s*$",
    re.IGNORECASE,
)
_MODEL_FROM_REF_RE = re.compile(r"\s+from\s+ref\..*$", re.IGNORECASE)
_LATEX_CITE_RE = re.compile(r"~?\\cite\{[^}]*\}")
_TITLE_LINEBREAK_RE = re.compile(r"\\\\+")
_TITLE_LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+\*?(?:\{[^}]*\})?")
_MODEL_RENAME_CACHE: dict[str, dict[str, str]] = {}


# ── Helpers ───────────────────────────────────────────────────────────────────


def _slug(name: str) -> str:
    """Convert a string to a URL-safe slug."""
    return re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")


def _sanitize_title(title: str | None) -> str:
    if not title:
        return ""
    t = _TITLE_LINEBREAK_RE.sub(" - ", str(title))
    t = t.replace("\\", " ")
    t = _TITLE_LATEX_CMD_RE.sub("", t)
    return re.sub(r"\s+", " ", t).strip()


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
    if not model_name:
        return ""
    m = str(model_name)
    m = _LATEX_CITE_RE.sub("", m)
    m = _MODEL_FROM_REF_RE.sub("", m)
    m = _MODEL_SUFFIX_RE.sub("", m)
    m = re.sub(r"\s+", " ", m).strip()
    remap = _paper_model_renames(arxiv_id)
    return remap.get(m.lower(), m)


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


def _fmt_date(date_str: str | None) -> str:
    """Format date strings for display while preserving day precision when available.

    - YYYY-MM-DD -> YYYY-MM-DD
    - YYYY-MM    -> Mon YYYY
    """
    if not date_str:
        return ""
    try:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            return date_str
        if re.match(r"^\d{4}-\d{2}$", date_str):
            return datetime.fromisoformat(date_str + "-01").strftime("%b %Y")
        return datetime.fromisoformat(date_str[:10]).strftime("%Y-%m-%d")
    except ValueError:
        return date_str


def _write_md(path: Path, front_matter: dict, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_str = yaml.dump(front_matter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    path.write_text(f"---\n{fm_str}---\n\n{body}", encoding="utf-8")


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
        pval = model_vals[model].get(primary_metric or "", (None, None))[0]
        if pval is None:
            return (1, 0.0)
        return (0, -pval if higher else pval)

    seen_models.sort(key=_sort_key)

    pivoted: list[dict] = []
    for model in seen_models:
        first = model_first[model]
        metric_values = [model_vals[model].get(m, (None, None))[0] for m in seen_metrics]
        metric_stds = [model_vals[model].get(m, (None, None))[1] for m in seen_metrics]
        pivoted.append(
            {
                "model": model,
                "metric_values": metric_values,
                "metric_stds": metric_stds,
                "is_baseline": first.get("is_baseline", False),
                "is_overridden": first.get("is_overridden", False),
                "override_reason": first.get("override_reason", ""),
                "params_millions": first.get("params_millions"),
            }
        )

    _mark_is_best(
        pivoted,
        primary_metric or "",
        higher,
        lambda r: (r["metric_values"][0] if r["metric_values"] else None),
        lambda r: (r["metric_stds"][0] if r["metric_stds"] else None),
    )

    return {"rows": pivoted, "metrics": seen_metrics, "primary_metric": primary_metric}


def _global_ranks_for_dataset(
    session: Any,
    ds_name: str,
    primary_metric: str,
    higher_is_better: bool,
) -> tuple[dict[str, int], list[dict]]:
    """Return (model_to_rank, sorted_rows) for *ds_name* on *primary_metric*.

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
        m_name = (r.model.canonical_name if r.model else "") or ""
        if not m_name:
            continue
        v = float(r.display_value) if r.display_value is not None else None
        if v is None:
            continue
        prev = model_best.get(m_name)
        if (
            prev is None
            or (higher_is_better and v > prev[0])
            or (not higher_is_better and v < prev[0])
        ):
            model_best[m_name] = (v, r)

    sorted_items = sorted(
        model_best.items(),
        key=lambda kv: -kv[1][0] if higher_is_better else kv[1][0],
    )
    model_to_rank: dict[str, int] = {m: i + 1 for i, (m, _) in enumerate(sorted_items)}

    rows: list[dict] = []
    for m_name, (val, r) in sorted_items:
        p = r.paper
        ued = r.uses_external_data
        rows.append(
            {
                "model": m_name,
                "value": val,
                "std": float(r.metric_std) if r.metric_std is not None else None,
                "metric": primary_metric,
                "higher_is_better": bool(r.higher_is_better),
                "is_baseline": bool(r.is_baseline),
                "is_overridden": bool(r.is_overridden),
                "override_reason": r.override_reason or "",
                "params_millions": (
                    r.model.size_params / 1_000_000 if r.model and r.model.size_params else None
                ),
                "arxiv_id": p.arxiv_id if p else "",
                "title": _sanitize_title(p.title if p else ""),
                "date": _fmt_date(p.published_date) if p else "",
                "codebase_url": p.codebase_url or "" if p else "",
                "uses_external_data": (True if ued == 1 else (False if ued == 0 else None)),
                "is_global_top": True,
                "global_rank": model_to_rank.get(m_name),
            }
        )

    return model_to_rank, rows


def _compute_paper_mrr(
    session: Any,
    paper: "Paper",
) -> tuple[float | None, list[str]]:
    """Return (MRR, proposed_model_names) for *paper*.

    MRR is the mean reciprocal rank of the paper's *primary* proposed model on
    each dataset's primary metric, ranked against ALL models globally (baselines
    included).  Only datasets that have ≥10 global entries count toward MRR.

    "Primary proposed model" = the model named in the LLM extraction's
    ``proposed_model.name`` field (read from llm_output.json).  Falls back to
    the first non-baseline model found if the JSON is unavailable.

    Returns ``(None, [])`` for pure benchmarking papers (no non-baseline results).
    Returns ``(0.0, names)`` when the paper has proposed models but none qualify.
    """
    results = (
        session.query(Result)
        .filter_by(paper_id=paper.id, is_baseline=False)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )
    if not results:
        return None, []

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
            import json as _json

            raw = _json.loads(storage.llm_output_path.read_text(encoding="utf-8"))
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
        return 0.0, proposed_models

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
            model_to_rank, global_rows = _global_ranks_for_dataset(
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
        rank = model_to_rank.get(primary_proposed)
        if rank is not None:
            reciprocal_ranks.append(1.0 / rank)

    mrr = round(sum(reciprocal_ranks) / len(reciprocal_ranks), 4) if reciprocal_ranks else 0.0
    return mrr, proposed_models


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
            result_groups.setdefault(ds_name, []).append(
                {
                    "model": _sanitize_model(
                        r.model.canonical_name if r.model else "",
                        paper.arxiv_id,
                    ),
                    "value": float(r.display_value) if r.display_value is not None else None,
                    "std": float(r.metric_std) if r.metric_std else None,
                    "metric": r.metric_name,
                    "higher_is_better": bool(r.higher_is_better),
                    "is_baseline": bool(r.is_baseline),
                    "is_overridden": bool(r.is_overridden),
                    "override_reason": r.override_reason or "",
                    "params_millions": (
                        r.model.size_params / 1_000_000 if r.model and r.model.size_params else None
                    ),
                    "table_ref": r.table_ref or "",
                    "source_ref": r.source_ref or "",
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
                model_to_rank, global_top_all = _global_ranks_for_dataset(
                    session, ds, primary_metric, higher
                )
            except Exception as _exc:
                logger.debug("Global rank lookup failed for %r: %s", ds, _exc)
                model_to_rank, global_top_all = {}, []

            if len(distinct_metrics) > 1:
                pivoted = _pivot_paper_rows(rows, primary_metric)
                pv_rows = pivoted["rows"]
                metrics_list = pivoted["metrics"]

                # Attach global ranks to pivoted rows
                paper_models: set[str] = {pr["model"] for pr in pv_rows}
                for pr in pv_rows:
                    pr["global_rank"] = model_to_rank.get(pr["model"])

                # Inject up to 3 global-top models not in this paper
                extra_rows: list[dict] = []
                n_metrics = len(metrics_list)
                for gr in global_top_all:
                    if gr["model"] not in paper_models:
                        mv = [gr["value"] if i == 0 else None for i in range(n_metrics)]
                        ms = [gr["std"] if i == 0 else None for i in range(n_metrics)]
                        extra_rows.append(
                            {
                                "model": gr["model"],
                                "metric_values": mv,
                                "metric_stds": ms,
                                "is_baseline": gr["is_baseline"],
                                "is_overridden": False,
                                "override_reason": "",
                                "params_millions": gr["params_millions"],
                                "arxiv_id": gr["arxiv_id"],
                                "title": gr["title"],
                                "date": gr["date"],
                                "date_iso": "",
                                "codebase_url": gr["codebase_url"],
                                "uses_external_data": gr.get("uses_external_data"),
                                "is_global_top": True,
                                "global_rank": gr["global_rank"],
                                "is_best": False,
                            }
                        )
                        if len(extra_rows) >= 3:
                            break

                if extra_rows:
                    combined = pv_rows + extra_rows

                    def _pv_sort(r: dict, _hib: bool = higher) -> tuple:
                        v = r["metric_values"][0] if r.get("metric_values") else None
                        if v is None:
                            return (1, 0.0)
                        return (0, -v if _hib else v)

                    combined.sort(key=_pv_sort)
                    _mark_is_best(
                        combined,
                        primary_metric,
                        higher,
                        lambda r: r["metric_values"][0] if r.get("metric_values") else None,
                        lambda r: r["metric_stds"][0] if r.get("metric_stds") else None,
                    )
                    pv_rows = combined

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
                    v = r.get("value")
                    if v is None:
                        return (1, 0.0)
                    return (0, -float(v) if _hib else float(v))

                rows.sort(key=_row_sort_key)

                # Attach global ranks to paper rows
                paper_models = {r.get("model", "") for r in rows}
                for row in rows:
                    row["global_rank"] = model_to_rank.get(row.get("model", ""))

                # Inject up to 3 global-top models not in this paper
                extra_rows = []
                for gr in global_top_all:
                    if gr["model"] not in paper_models:
                        extra_rows.append(gr)
                        if len(extra_rows) >= 3:
                            break

                if extra_rows:
                    rows = rows + extra_rows
                    rows.sort(key=_row_sort_key)

                _mark_is_best(
                    rows,
                    primary_metric,
                    higher,
                    lambda r: r.get("value"),
                    lambda r: r.get("std"),
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
        main_figure_hugo: str | None = None
        if storage.main_figure_path and storage.main_figure_path.exists():
            dest = _STATIC / "figures" / arxiv_id / storage.main_figure_path.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(storage.main_figure_path, dest)
            main_figure_hugo = f"/figures/{arxiv_id}/{storage.main_figure_path.name}"

        mrr, proposed_models = _compute_paper_mrr(session, paper)
        has_results = bool(results_for_fm)

        # Single proposed model: if all proposed results come from the same canonical name
        single_proposed_model: str | None = None
        if len(proposed_models) == 1:
            single_proposed_model = proposed_models[0]

        front_matter: dict[str, Any] = {
            "title": _sanitize_title(paper.title) or arxiv_id,
            "arxiv_id": arxiv_id,
            "authors": paper.authors or [],
            "published_date": _fmt_date(paper.published_date),
            "abstract": paper.abstract or "",
            "codebase_url": paper.codebase_url or "",
            "extraction_model": paper.extraction_model or "",
            "has_results": has_results,
            "proposed_models": proposed_models,
            "mrr": mrr,
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
                "is_baseline": bool(r.is_baseline),
                "is_overridden": bool(r.is_overridden),
                "override_reason": r.override_reason or "",
                "params_millions": (
                    r.model.size_params / 1_000_000 if r.model and r.model.size_params else None
                ),
                "arxiv_id": arxiv_id,
                "title": _sanitize_title(paper.title if paper else ""),
                "date": _fmt_date(paper.published_date) if paper else "",
                "date_iso": (paper.published_date[:10] if paper and paper.published_date else ""),
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


def export_dataset(dataset_id: int) -> bool:
    """Export a dataset page with all variants and leaderboard data."""
    with session_scope() as session:
        ds = session.get(Dataset, dataset_id)
        if ds is None:
            return False

        variants = (
            session.query(DatasetVariant)
            .filter_by(dataset_id=dataset_id)
            .order_by(DatasetVariant.is_standard.desc(), DatasetVariant.name)
            .all()
        )

        if not variants:
            logger.debug("Dataset %s has no variants — skipping export", ds.name)
            return False

        # Determine primary metric from the first variant that has results
        primary_metric = ds.primary_metric or ""
        higher_is_better = True

        variant_data: list[dict] = []
        for v in variants:
            all_results = (
                session.query(Result)
                .filter_by(dataset_variant_id=v.id)
                .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
                .all()
            )

            if not all_results:
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

            milestones = get_best_results_over_time(v.id, metric)

            variant_data.append(
                {
                    "slug": _slug(v.name),
                    "name": v.name,
                    "notes": v.notes or "",
                    "is_standard": bool(v.is_standard),
                    "primary_metric": metric,
                    "higher_is_better": higher_is_better,
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
            }

        # Dataset-level stats are often missing; fall back to the standard variant stats.
        std_variant = next((v for v in variants if v.is_standard), variants[0])
        stats_num_graphs = ds.num_graphs if ds.num_graphs is not None else std_variant.num_graphs
        stats_avg_nodes = ds.avg_nodes if ds.avg_nodes is not None else std_variant.avg_nodes
        stats_avg_edges = ds.avg_edges if ds.avg_edges is not None else std_variant.avg_edges
        stats_num_classes = ds.num_classes

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
    from sqlalchemy import func

    _DATA_DIR.mkdir(parents=True, exist_ok=True)

    with session_scope() as session:
        # Result count per dataset (for ordering datasets by activity)
        ds_result_counts: dict[int, int] = dict(
            session.query(Dataset.id, func.count(Result.id))
            .join(Dataset.variants)
            .join(DatasetVariant.results)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .group_by(Dataset.id)
            .all()
        )

        benchmarks = session.query(Benchmark).all()

        # Sort benchmark groups by total result count (descending)
        def _bm_total(b: Benchmark) -> int:
            return sum(ds_result_counts.get(ds.id, 0) for ds in b.datasets)

        benchmarks = sorted(benchmarks, key=_bm_total, reverse=True)

        data: list[dict] = []
        for b in benchmarks:
            # Sort datasets within this benchmark by cumulated result count (descending)
            sorted_datasets = sorted(
                b.datasets,
                key=lambda ds: -ds_result_counts.get(ds.id, 0),
            )
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
    _DATA_DIR.mkdir(parents=True, exist_ok=True)

    with session_scope() as session:
        # Extraction status summary
        status_counts = {}
        papers = session.query(Paper).all()
        for p in papers:
            status_counts[p.extraction_status] = status_counts.get(p.extraction_status, 0) + 1

        # Skipped papers with reasons
        skipped_papers = (
            session.query(PaperCandidate).filter(PaperCandidate.stage1_passed == 0).all()
        )

        # Papers with both stages failed
        stage2_skipped = (
            session.query(PaperCandidate).filter(PaperCandidate.stage2_passed == 0).all()
        )

        # Papers "to be processed" - papers cited by existing ones
        # This would require querying cited_by relationships (if stored)
        # For now, create a placeholder

        dev_data = {
            "paper_status": {
                "total": len(papers),
                "by_status": status_counts,
            },
            "skipped": {
                "stage1_count": len(skipped_papers),
                "stage2_count": len(stage2_skipped),
            },
        }

        (_DATA_DIR / "development.json").write_text(
            json.dumps(dev_data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        logger.info("Wrote %s", _DATA_DIR / "development.json")

        # Export todo_papers table for admin view
        try:
            todo_rows = session.query(TodoPaper).order_by(TodoPaper.seen_count.desc()).all()
            todo_list = []
            for t in todo_rows:
                todo_list.append(
                    {
                        "arxiv_id": t.arxiv_id,
                        "title": _sanitize_title(t.title),
                        "status": t.status,
                        "seen_count": int(t.seen_count or 0),
                        "seen_from": json.loads(t.seen_from) if t.seen_from else [],
                        "first_seen_at": t.first_seen_at,
                    }
                )
            (_DATA_DIR / "todo_papers.json").write_text(
                json.dumps(todo_list, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            logger.info("Wrote %s", _DATA_DIR / "todo_papers.json")
        except Exception:
            logger.exception("Failed to export todo_papers.json")

    # Create development pages
    _create_dev_pages()


def _create_dev_pages() -> None:
    """Generate development/admin pages."""
    _CONTENT_DEV = _CONTENT / "dev"
    _CONTENT_DEV.mkdir(parents=True, exist_ok=True)

    with session_scope() as session:
        # Index page
        _write_md(_CONTENT_DEV / "_index.md", {"title": "Development", "type": "dev"}, "")

        # Paper status page
        papers = session.query(Paper).all()
        by_status = {}
        for p in papers:
            if p.extraction_status not in by_status:
                by_status[p.extraction_status] = []
            by_status[p.extraction_status].append(p)

        lines = [
            "## Paper Extraction Status",
            "",
            f"**Total:** {len(papers)} papers",
            "",
            "This page tracks the extraction pipeline status for all papers in the benchmarking dataset. "
            "Each paper goes through several stages: first it must be downloaded from arXiv, then the full text "
            "is extracted and parsed (either from HTML, LaTeX source, or PDF), and finally results are extracted "
            "using an LLM. The extraction model shown indicates which LLM (if any) was used to extract results.",
            "",
        ]
        for status in sorted(by_status.keys()):
            count = len(by_status[status])
            lines.append(f"### {status.capitalize()} ({count})")
            lines.append("")

            # Add status-specific descriptions
            if status == "pending":
                lines.append("Papers that have been identified but not yet downloaded from arXiv.")
                lines.append("")
            elif status == "downloaded":
                lines.append(
                    "Papers that have been downloaded but not yet processed for extraction."
                )
                lines.append("")
            elif status == "extracted":
                lines.append(
                    "Papers with successfully extracted results. These papers contribute to the leaderboards."
                )
                lines.append("")
            elif status == "failed":
                lines.append(
                    "Papers where extraction failed. These may have parsing errors, missing datasets, or LLM errors."
                )
                lines.append("")

            if by_status[status]:
                lines.append("| ArXiv | Title | Model |")
                lines.append("|-------|-------|-------|")
                for p in sorted(by_status[status], key=lambda x: x.arxiv_id):
                    title = (p.title[:40] + "...") if len(p.title or "") > 40 else (p.title or "")
                    model = p.extraction_model or "—"
                    lines.append(f"| {p.arxiv_id} | {title} | {model} |")
                lines.append("")

        _write_md(
            _CONTENT_DEV / "paper-status.md",
            {
                "title": "Paper Extraction Status",
                "type": "dev",
                "description": "Overview of extraction status",
            },
            "\n".join(lines),
        )

        # Skipped papers page
        skipped_s1 = session.query(PaperCandidate).filter(PaperCandidate.stage1_passed == 0).all()
        skipped_s2 = session.query(PaperCandidate).filter(PaperCandidate.stage2_passed == 0).all()

        zero_dataset_candidates = []
        for c in skipped_s2:
            raw = c.stage2_datasets or ""
            ds_list: list[str] = []
            if raw:
                try:
                    parsed = json.loads(raw)
                    if isinstance(parsed, list):
                        ds_list = [str(x).strip() for x in parsed if str(x).strip()]
                except Exception:
                    ds_list = []
            if not ds_list:
                zero_dataset_candidates.append(c)

        lines = [
            "## Skipped Papers",
            "",
            "This page shows papers that were identified but rejected by the LLM screening pipeline. "
            "The screening happens in two stages: Stage 1 filters for general relevance to graph neural network "
            "research, and Stage 2 checks whether the paper evaluates results on known benchmarks. Papers that pass "
            "both stages proceed to full result extraction.",
            "",
            f"### Stage 1 Rejections: {len(skipped_s1)}",
            "",
            "Stage 1 rejects papers that are deemed not relevant to graph neural networks. These are typically papers "
            "in unrelated fields that happened to mention GNNs or graph concepts, but don't focus on benchmarking graph neural network models.",
            "",
        ]
        if skipped_s1:
            lines.append("| ArXiv | Title | Reason |")
            lines.append("|-------|-------|--------|")
            for c in skipped_s1:
                reason = (c.stage1_reason or "—")[:80]
                title = (c.title or "")[:40]
                lines.append(f"| {c.arxiv_id or '—'} | {title} | {reason} |")
        lines.append("")
        lines.append(f"### Stage 2 Rejections: {len(skipped_s2)}")
        lines.append("")
        lines.append(
            "Stage 2 rejects papers that are relevant to GNNs but don't evaluate models on any known benchmarks. "
            "This includes position papers, theoretical papers, survey papers, or papers that only propose new "
            "datasets without evaluating existing models. The 'Datasets Found' column shows how many benchmark datasets "
            "the LLM detected in the paper (if any)."
        )
        lines.append("")
        if skipped_s2:
            lines.append("| ArXiv | Title | Datasets Found | Reason |")
            lines.append("|-------|-------|----------------|--------|")
            for c in skipped_s2:
                reason = (c.stage2_reason or "—")[:80]
                ds_count = 0
                raw = c.stage2_datasets or ""
                if raw:
                    try:
                        parsed = json.loads(raw)
                        if isinstance(parsed, list):
                            ds_count = len([x for x in parsed if str(x).strip()])
                    except Exception:
                        ds_count = 0
                title = (c.title or "")[:40]
                lines.append(f"| {c.arxiv_id or '—'} | {title} | {ds_count} | {reason} |")

        lines.append("")
        lines.append(f"### No Datasets/Results Discovered: {len(zero_dataset_candidates)}")
        lines.append("")
        lines.append(
            "These papers passed Stage 2 screening (were deemed relevant and benchmarking-focused) but the extraction "
            "pipeline was unable to discover any benchmark datasets or results. This could mean: the paper's results are "
            "too noisy for extraction, the datasets used have non-standard names, or the extraction model failed to parse "
            "the paper format. These papers may still be worth investigating manually."
        )
        lines.append("")
        if zero_dataset_candidates:
            lines.append("| ArXiv | Title | Stage 2 Reason |")
            lines.append("|-------|-------|----------------|")
            for c in zero_dataset_candidates:
                title = (c.title or "")[:48]
                reason = (c.stage2_reason or "—")[:96]
                lines.append(f"| {c.arxiv_id or '—'} | {title} | {reason} |")

        _write_md(
            _CONTENT_DEV / "skipped-papers.md",
            {
                "title": "Skipped Papers",
                "type": "dev",
                "description": "Papers rejected by LLM screening",
            },
            "\n".join(lines),
        )

        # Missing datasets page from data/pending_datasets.yaml
        pending_path = cfg.data_dir / "pending_datasets.yaml"
        pending_entries: list[dict] = []
        if pending_path.exists():
            try:
                loaded = yaml.safe_load(pending_path.read_text(encoding="utf-8"))
                if isinstance(loaded, list):
                    pending_entries = loaded
            except Exception:
                pending_entries = []

        lines = [
            "## Datasets Detected But Not In DB",
            "",
            "During result extraction, the LLM sometimes detects dataset names that are not yet in our benchmarking database. "
            "This page lists those datasets. Each entry includes the datasets that were detected in the papers, along with suggested "
            "benchmark categories and whether a PyG (PyTorch Geometric) dataset definition is available. These pending datasets should be "
            "reviewed for integration into the main benchmark suite.",
            "",
            f"Source file: `{pending_path}`",
            "",
            f"**Total pending entries:** {len(pending_entries)}",
            "",
        ]
        if pending_entries:
            lines.append("| Status | Dataset | Paper | Metrics Seen | Suggested Benchmark | PyG |")
            lines.append("|--------|---------|-------|--------------|---------------------|-----|")
            for e in pending_entries:
                status = str(e.get("status") or "pending")
                dataset = str(e.get("dataset") or "")
                paper = str(e.get("arxiv_id") or "")
                metrics = ", ".join(e.get("metrics_seen") or [])
                suggestion = e.get("suggestion") or {}
                benchmark_name = str(suggestion.get("benchmark_name") or "")
                pyg_url = str(suggestion.get("pyg_url") or "")
                pyg_marker = "yes" if pyg_url else ""
                lines.append(
                    f"| {status} | {dataset} | {paper} | {metrics} | {benchmark_name} | {pyg_marker} |"
                )

        _write_md(
            _CONTENT_DEV / "missing-datasets.md",
            {
                "title": "Missing Datasets",
                "type": "dev",
                "description": "Datasets detected in extraction but not yet mapped into DB",
            },
            "\n".join(lines),
        )

        logger.info("Created development pages in %s", _CONTENT_DEV)


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
