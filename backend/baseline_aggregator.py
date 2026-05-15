"""Baseline aggregator — groups result rows by canonical model name and
computes per-baseline summary statistics for a given dataset variant + metric.

Uses thefuzz to merge model names that differ only in whitespace/punctuation.
Called by export_to_hugo.py to populate the leaderboard tables.

Usage::
    python -m backend.baseline_aggregator --dataset-variant 3 --metric AP
"""

from __future__ import annotations

import argparse
import logging
import math
import re
from dataclasses import dataclass, field
from typing import Any

from thefuzz import fuzz as _fuzz

from sqlalchemy import text

from backend.db import init_db, session_scope
from backend.models import DatasetVariant, Model, ModelAlias, Result

logger = logging.getLogger(__name__)

# Title sanitization (matches export_to_hugo.py)
_TITLE_LINEBREAK_RE = re.compile(r"\s*\\{2,}\s*")
_TITLE_LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+\{[^}]*\}")


def _sanitize_title(title: str | None) -> str:
    """Remove LaTeX artifacts and line breaks from paper titles."""
    if not title:
        return ""
    t = _TITLE_LINEBREAK_RE.sub(" - ", str(title))
    t = t.replace("\\", " ")
    t = _TITLE_LATEX_CMD_RE.sub("", t)
    return re.sub(r"\s+", " ", t).strip()


# Similarity threshold for grouping model names (0-100)
FUZZY_THRESHOLD = 85


@dataclass
class BaselineGroup:
    """Aggregate stats for a single canonical model on a dataset/metric."""

    canonical_name: str
    model_id: int
    values: list[float] = field(default_factory=list)
    stds: list[float | None] = field(default_factory=list)
    paper_ids: list[int] = field(default_factory=list)
    arxiv_ids: list[str] = field(default_factory=list)
    higher_is_better: bool = True

    @property
    def count(self) -> int:
        return len(self.values)

    @property
    def mean(self) -> float | None:
        return sum(self.values) / len(self.values) if self.values else None

    @property
    def best(self) -> float | None:
        if not self.values:
            return None
        return max(self.values) if self.higher_is_better else min(self.values)

    @property
    def worst(self) -> float | None:
        if not self.values:
            return None
        return min(self.values) if self.higher_is_better else max(self.values)

    @property
    def std_across_papers(self) -> float | None:
        if len(self.values) < 2:
            return None
        mean = sum(self.values) / len(self.values)
        variance = sum((v - mean) ** 2 for v in self.values) / (len(self.values) - 1)
        return math.sqrt(variance)

    @property
    def representative_std(self) -> float | None:
        """Best available std: use the std from the best result; else mean of reported stds."""
        best_val = self.best
        if best_val is None:
            return None
        idx = self.values.index(best_val)
        if self.stds[idx] is not None:
            return self.stds[idx]
        reported = [s for s in self.stds if s is not None]
        return sum(reported) / len(reported) if reported else None

    def to_dict(self) -> dict[str, Any]:
        return {
            "canonical_name": self.canonical_name,
            "model_id": self.model_id,
            "count": self.count,
            "mean": self.mean,
            "best": self.best,
            "worst": self.worst,
            "std_across_papers": self.std_across_papers,
            "representative_std": self.representative_std,
            "higher_is_better": self.higher_is_better,
            "paper_ids": self.paper_ids,
            "arxiv_ids": self.arxiv_ids,
        }


def get_baseline_summary(
    dataset_variant_id: int,
    metric_name: str,
    fuzzy_threshold: int = FUZZY_THRESHOLD,
    baselines_only: bool = False,
) -> list[dict[str, Any]]:
    """Return grouped baseline statistics for a dataset variant + metric.

    Groups by canonical model name using thefuzz.
    Sorted by best value (descending if higher_is_better, ascending otherwise).
    """
    init_db()

    with session_scope() as session:
        query = (
            session.query(Result)
            .filter_by(dataset_variant_id=dataset_variant_id, metric_name=metric_name)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        )
        if baselines_only:
            query = query.filter_by(is_baseline=1)

        results = query.all()

        if not results:
            return []

        # Load all canonical model names for fuzzy comparison
        models = {m.id: m.canonical_name for m in session.query(Model).all()}

        # Group results
        groups: dict[int, BaselineGroup] = {}
        for r in results:
            model_id = r.model_id
            if model_id not in groups:
                groups[model_id] = BaselineGroup(
                    canonical_name=models.get(model_id, f"Model#{model_id}"),
                    model_id=model_id,
                    higher_is_better=bool(r.higher_is_better),
                )
            g = groups[model_id]
            effective_value = r.display_value
            if effective_value is not None:
                g.values.append(float(effective_value))
                g.stds.append(
                    float(r.override_std)
                    if r.is_overridden and r.override_std is not None
                    else (float(r.metric_std) if r.metric_std is not None else None)
                )
                paper = r.paper
                if paper:
                    g.paper_ids.append(paper.id)
                    g.arxiv_ids.append(paper.arxiv_id)

    # Merge groups with similar names
    merged_groups = _merge_similar_groups(list(groups.values()), fuzzy_threshold)

    # Sort
    higher_is_better = results[0].higher_is_better if results else True
    sorted_groups = sorted(
        merged_groups,
        key=lambda g: (g.best is not None, g.best if g.best is not None else 0),
        reverse=bool(higher_is_better),
    )

    return [g.to_dict() for g in sorted_groups]


def get_best_results_over_time(
    dataset_variant_id: int,
    metric_name: str,
) -> list[dict[str, Any]]:
    """Return the monotonically improving results over time.

    Used for the Chart.js step chart on the leaderboard.
    Returns list sorted by paper date, each item being the new best result.
    """
    init_db()

    with session_scope() as session:
        results = (
            session.query(Result)
            .filter_by(dataset_variant_id=dataset_variant_id, metric_name=metric_name)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .join(Result.paper)
            .order_by(text("papers.published_date"))
            .all()
        )

        if not results:
            return []

        higher = bool(results[0].higher_is_better)

        # Group by month (YYYY-MM): keep only the best result per month
        month_best: dict[str, tuple[float, Any]] = {}
        for r in results:
            val = r.display_value
            if val is None:
                continue
            val = float(val)
            paper = r.paper
            if not paper or not paper.published_date:
                continue
            month = paper.published_date[:7]  # YYYY-MM
            if month not in month_best:
                month_best[month] = (val, r)
            else:
                cur_val, _ = month_best[month]
                if (higher and val > cur_val) or (not higher and val < cur_val):
                    month_best[month] = (val, r)

        # Compute running record across months in chronological order
        best_so_far: float | None = None
        milestones: list[dict[str, Any]] = []

        for month in sorted(month_best.keys()):
            val, r = month_best[month]
            is_new_best = (
                best_so_far is None
                or (higher and val > best_so_far)
                or (not higher and val < best_so_far)
            )
            if is_new_best:
                best_so_far = val
                paper = r.paper
                milestones.append(
                    {
                        "value": val,
                        "std": float(r.metric_std) if r.metric_std else None,
                        "model": r.model.canonical_name if r.model else "",
                        "arxiv_id": paper.arxiv_id if paper else "",
                        "title": _sanitize_title(paper.title if paper else ""),
                        "date": (
                            paper.published_date[:10] if paper and paper.published_date else None
                        ),
                    }
                )

    return milestones


# ── Fuzzy merge ───────────────────────────────────────────────────────────────


def _merge_similar_groups(
    groups: list[BaselineGroup],
    threshold: int,
) -> list[BaselineGroup]:
    """Merge groups whose canonical names are similar above threshold.

    The group with more papers wins the canonical name.
    """
    if not groups:
        return groups

    merged: list[BaselineGroup] = []
    used: set[int] = set()

    for i, g in enumerate(groups):
        if i in used:
            continue
        combined = BaselineGroup(
            canonical_name=g.canonical_name,
            model_id=g.model_id,
            values=list(g.values),
            stds=list(g.stds),
            paper_ids=list(g.paper_ids),
            arxiv_ids=list(g.arxiv_ids),
            higher_is_better=g.higher_is_better,
        )
        for j, other in enumerate(groups):
            if j <= i or j in used:
                continue
            sim = _fuzz.token_sort_ratio(g.canonical_name.lower(), other.canonical_name.lower())
            if sim >= threshold:
                combined.values.extend(other.values)
                combined.stds.extend(other.stds)
                combined.paper_ids.extend(other.paper_ids)
                combined.arxiv_ids.extend(other.arxiv_ids)
                # Keep the name of the group with more papers
                if len(other.paper_ids) > len(g.paper_ids):
                    combined.canonical_name = other.canonical_name
                used.add(j)
        used.add(i)
        merged.append(combined)

    return merged


# ── CLI ───────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Compute baseline aggregation stats")
    parser.add_argument(
        "--dataset-variant", "-d", type=int, required=True, help="DatasetVariant ID"
    )
    parser.add_argument("--metric", "-m", required=True, help="Metric name (e.g. AP, MAE)")
    parser.add_argument("--baselines-only", action="store_true")
    parser.add_argument("--threshold", type=int, default=FUZZY_THRESHOLD)
    args = parser.parse_args(argv)

    import json as _json

    groups = get_baseline_summary(
        args.dataset_variant,
        args.metric,
        fuzzy_threshold=args.threshold,
        baselines_only=args.baselines_only,
    )
    print(_json.dumps(groups, indent=2))


if __name__ == "__main__":
    main()
