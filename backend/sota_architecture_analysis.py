"""Architecture ownership analysis for benchmark SOTA results.

The analysis deliberately operates on the same canonical result rows used by
the site leaderboard.  Paper-local overrides are overlaid in memory so the
report can show the effect of metadata corrections before the database is
re-exported.
"""

from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from sqlalchemy.orm import joinedload

from backend.config import cfg
from backend.model_metadata import normalize_architecture_type
from backend.model_metadata_defaults import lookup_default_model_type
from backend.models import DatasetVariant, Result
from backend.override_handler import load_overrides
from backend.results_parser import result_is_leaderboard_eligible
from backend.significance import is_significantly_different
from backend.venue import is_conference_publication_venue, is_peer_reviewed_publication_venue

TRANSFORMER_TYPES = frozenset({"graph_transformer", "hybrid"})
DEFAULT_CATEGORY_ORDER = (
    "gnn",
    "transformer_involving",
    "llm",
    "walk",
    "svm_kernel",
    "random_forest",
    "decision_tree",
    "boosting",
    "other_traditional",
    "unknown",
)
NODE_TASK_TYPES = frozenset({"node_classification", "node_regression"})
GRAPH_TASK_TYPES = frozenset({"graph_classification", "graph_regression", "graph_generation"})


@dataclass(frozen=True, slots=True)
class AnalysisRow:
    """One eligible primary-metric result used by the analysis."""

    dataset_id: int
    dataset: str
    metric: str
    higher_is_better: bool
    value: float
    std: float | None
    paper_id: int
    arxiv_id: str
    paper_date: date
    model: str
    model_type: str | None
    model_type_before_override: str | None
    task_level: str | None
    override_type_applied: bool = False
    is_baseline: bool = False
    venue: str = ""
    num_runs: int | None = None

    @property
    def category(self) -> str:
        """Return the reporting category for this row."""
        normalized = normalize_architecture_type(self.model_type)
        if normalized in TRANSFORMER_TYPES:
            return "transformer_involving"
        return normalized or "unknown"

    @property
    def is_conference_paper(self) -> bool:
        """Return whether the paper has evidence of conference publication."""
        return is_conference_publication_venue(self.venue)

    @property
    def is_peer_reviewed_paper(self) -> bool:
        """Return whether the paper has a trusted, non-ArXiv publication venue."""
        return is_peer_reviewed_publication_venue(self.venue)


@dataclass(frozen=True, slots=True)
class DatasetOwnership:
    """SOTA ownership for one dataset at one cutoff."""

    dataset_id: int
    dataset: str
    cutoff: date
    paper_count: int
    weight: float
    winner_models: tuple[str, ...]
    winner_model_types: tuple[tuple[str, str], ...]
    winner_types: tuple[str, ...]
    known_winner_types: tuple[str, ...]
    winner_arxiv_ids: tuple[str, ...]

    @property
    def has_unknown_winner(self) -> bool:
        return "unknown" in self.winner_types


@dataclass(frozen=True, slots=True)
class OwnershipSnapshot:
    """Aggregated architecture shares at one historical cutoff."""

    cutoff: date
    ownership: tuple[DatasetOwnership, ...]
    category_weights: dict[str, float]
    total_weight: float

    @property
    def shares(self) -> dict[str, float]:
        if self.total_weight <= 0:
            return {}
        return {
            category: weight / self.total_weight
            for category, weight in self.category_weights.items()
        }


@dataclass(frozen=True, slots=True)
class OverrideAudit:
    """Before/after counts describing the effect of paper corrections."""

    unknown_winner_states_before: int = 0
    classified_from_unknown_states: int = 0
    changed_current_datasets: int = 0
    changed_cutoff_states: int = 0
    problematic_rows_removed: int = 0
    transformer_share_before: float | None = None
    transformer_share_after: float | None = None


def parse_paper_date(value: str | None) -> date | None:
    """Parse the repository's supported paper date formats."""
    raw = str(value or "").strip()
    if len(raw) == 7:
        raw = f"{raw}-01"
    if len(raw) != 10:
        return None
    try:
        return date.fromisoformat(raw)
    except ValueError:
        return None


def architecture_category(model_type: str | None) -> str:
    """Collapse canonical architecture types into report categories."""
    normalized = normalize_architecture_type(model_type)
    if normalized in TRANSFORMER_TYPES:
        return "transformer_involving"
    return normalized or "unknown"


def square_root_weight(paper_count: int) -> float:
    """Return the default activity weight for a dataset."""
    return math.sqrt(max(0, paper_count))


def task_level(task_type: str | None) -> str | None:
    """Map the database task taxonomy to node- or graph-level analysis groups."""
    normalized = str(task_type or "").strip().casefold()
    if normalized in NODE_TASK_TYPES:
        return "node"
    if normalized in GRAPH_TASK_TYPES:
        return "graph"
    return None


def _result_override(result: Result, overrides: dict[str, Any]) -> dict[str, Any] | None:
    raw_model = str(result.model.name if result.model else "").strip().casefold()
    dataset = str(result.dataset_variant.dataset.name if result.dataset_variant else "")
    metric = str(result.metric_name or "").strip().casefold()
    for item in overrides.get("result_overrides") or []:
        if not isinstance(item, dict):
            continue
        if (
            str(item.get("model") or "").strip().casefold() == raw_model
            and str(item.get("dataset") or "").strip().casefold() == dataset.casefold()
            and str(item.get("metric") or "").strip().casefold() == metric
        ):
            return item
    return None


def _is_problematic_override(result: Result, overrides: dict[str, Any]) -> bool:
    raw_model = str(result.model.name if result.model else "").strip().casefold()
    dataset = str(result.dataset_variant.dataset.name if result.dataset_variant else "")
    metric = str(result.metric_name or "").strip().casefold()
    for item in overrides.get("problematic_results") or []:
        if not isinstance(item, dict):
            continue
        if (
            str(item.get("model") or "").strip().casefold() == raw_model
            and str(item.get("dataset") or "").strip().casefold() == dataset.casefold()
            and str(item.get("metric") or "").strip().casefold() == metric
        ):
            return True
    return False


def _override_model_type(result: Result, overrides: dict[str, Any]) -> str | None:
    raw_model = str(result.model.name if result.model else "").strip().casefold()
    dataset = str(result.dataset_variant.dataset.name if result.dataset_variant else "")
    matches: list[dict[str, Any]] = []
    for item in overrides.get("model_metadata_overrides") or []:
        if not isinstance(item, dict):
            continue
        if str(item.get("model") or "").strip().casefold() != raw_model:
            continue
        item_dataset = str(item.get("dataset") or "").strip()
        if item_dataset and item_dataset.casefold() != dataset.casefold():
            continue
        matches.append(item)
    if not matches:
        return None
    matches.sort(key=lambda item: bool(str(item.get("dataset") or "").strip()))
    return normalize_architecture_type(matches[-1].get("model_type"))


def _paper_overrides(arxiv_id: str, papers_root: Path) -> dict[str, Any]:
    """Load one paper override file without requiring a DB write."""
    return load_overrides(arxiv_id, papers_root=papers_root)


def load_analysis_rows(
    session: Any,
    *,
    papers_root: Path | None = None,
    apply_overrides: bool = True,
    as_of: date | None = None,
) -> list[AnalysisRow]:
    """Load canonical primary-metric rows, optionally overlaying overrides."""
    papers_root = papers_root or cfg.papers_dir
    as_of = as_of or date.today()
    results = (
        session.query(Result)
        .options(
            joinedload(Result.model),
            joinedload(Result.paper),
            joinedload(Result.dataset_variant).joinedload(DatasetVariant.dataset),
        )
        .join(Result.dataset_variant)
        .join(DatasetVariant.dataset)
        .filter(DatasetVariant.is_standard == 1)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )

    overrides_cache: dict[str, dict[str, Any]] = {}
    rows: list[AnalysisRow] = []
    for result in results:
        dataset = result.dataset_variant.dataset if result.dataset_variant else None
        paper = result.paper
        if not dataset or not paper or not result.model:
            continue
        if not dataset.primary_metric or result.metric_name != dataset.primary_metric:
            continue
        paper_date = parse_paper_date(paper.published_date)
        if paper_date is None or paper_date > as_of:
            continue
        if not result_is_leaderboard_eligible(result):
            continue

        overrides = {}
        if apply_overrides and paper.arxiv_id:
            if paper.arxiv_id not in overrides_cache:
                overrides_cache[paper.arxiv_id] = _paper_overrides(paper.arxiv_id, papers_root)
            overrides = overrides_cache[paper.arxiv_id]
        if _is_problematic_override(result, overrides):
            continue

        value = result.display_value
        std = result.display_std
        value_override = _result_override(result, overrides)
        if value_override is not None:
            if value_override.get("correct_value") is not None:
                value = float(value_override["correct_value"])
            if "correct_std" in value_override:
                std = (
                    float(value_override["correct_std"])
                    if value_override["correct_std"] is not None
                    else None
                )
        if value is None:
            continue

        before_type = normalize_architecture_type(result.model.model_type)
        if before_type is None:
            before_type = lookup_default_model_type(result.effective_model_name)
        override_type = _override_model_type(result, overrides)
        model_type = override_type or before_type
        rows.append(
            AnalysisRow(
                dataset_id=dataset.id,
                dataset=dataset.name,
                metric=result.metric_name,
                higher_is_better=bool(result.higher_is_better),
                value=float(value),
                std=float(std) if std is not None else None,
                num_runs=result.num_runs,
                paper_id=paper.id,
                arxiv_id=paper.arxiv_id or "",
                paper_date=paper_date,
                model=result.effective_model_name or result.model.name,
                model_type=model_type,
                model_type_before_override=before_type,
                task_level=task_level(dataset.task_type),
                override_type_applied=override_type is not None and override_type != before_type,
                is_baseline=bool(result.is_baseline),
                venue=paper.venue or "",
            )
        )
    return rows


def historical_cutoffs(rows: Iterable[AnalysisRow]) -> list[date]:
    """Return one year-end cutoff for every year represented by *rows*."""
    dates = [row.paper_date for row in rows]
    if not dates:
        return []
    first_year = min(dates).year
    last_date = max(dates)
    cutoffs = [date(year, 12, 31) for year in range(first_year, last_date.year + 1)]
    if cutoffs[-1] > last_date:
        cutoffs[-1] = last_date
    return cutoffs


def monthly_cutoffs(rows: Iterable[AnalysisRow]) -> list[date]:
    """Return month-end cutoffs through the latest observed paper date."""
    dates = [row.paper_date for row in rows]
    if not dates:
        return []
    first_date = min(dates)
    latest_date = max(dates)
    year, month = first_date.year, first_date.month
    cutoffs: list[date] = []
    while (year, month) <= (latest_date.year, latest_date.month):
        next_month = date(year + 1, 1, 1) if month == 12 else date(year, month + 1, 1)
        month_end = next_month.fromordinal(next_month.toordinal() - 1)
        cutoffs.append(
            latest_date if (year, month) == (latest_date.year, latest_date.month) else month_end
        )
        if month == 12:
            year, month = year + 1, 1
        else:
            month += 1
    return cutoffs


def _winner_rows(rows: list[AnalysisRow], winner_policy: str = "ci") -> list[AnalysisRow]:
    if not rows:
        return []
    if winner_policy not in {"ci", "single_mean"}:
        raise ValueError(f"Unsupported winner policy: {winner_policy!r}")
    higher = rows[0].higher_is_better
    best = max(rows, key=lambda row: row.value) if higher else min(rows, key=lambda row: row.value)
    if winner_policy == "single_mean":
        tied = [row for row in rows if row.value == best.value]
        return [max(tied, key=lambda row: (row.paper_date, row.paper_id, row.model))]
    return [
        row
        for row in rows
        if not is_significantly_different(
            row.value, row.std, row.num_runs, best.value, best.std, best.num_runs
        )
    ]


def _ownership_for_dataset(
    dataset_rows: list[AnalysisRow],
    cutoff: date,
    min_papers: int,
    weight_fn: Any,
    winner_policy: str = "ci",
) -> DatasetOwnership | None:
    current = [row for row in dataset_rows if row.paper_date <= cutoff]
    paper_count = len({row.paper_id for row in current})
    if paper_count < min_papers:
        return None
    winners = _winner_rows(current, winner_policy=winner_policy)
    model_types: dict[str, str] = {}
    for winner in winners:
        existing_type = model_types.setdefault(winner.model, winner.category)
        if existing_type != winner.category:
            raise ValueError(
                f"Winning model {winner.model!r} has conflicting architecture categories "
                f"{existing_type!r} and {winner.category!r}"
            )
    winner_model_types = tuple(sorted(model_types.items()))
    winner_types = tuple(sorted(set(model_types.values())))
    known_types = tuple(category for category in winner_types if category != "unknown")
    return DatasetOwnership(
        dataset_id=dataset_rows[0].dataset_id,
        dataset=dataset_rows[0].dataset,
        cutoff=cutoff,
        paper_count=paper_count,
        weight=float(weight_fn(paper_count)),
        winner_models=tuple(model for model, _category in winner_model_types),
        winner_model_types=winner_model_types,
        winner_types=winner_types,
        known_winner_types=known_types,
        winner_arxiv_ids=tuple(sorted({row.arxiv_id for row in winners})),
    )


def analyze_snapshots(
    rows: Iterable[AnalysisRow],
    *,
    cutoffs: Iterable[date] | None = None,
    min_papers: int = 5,
    weight: str = "uniform",
    task_level: str | None = None,
    winner_policy: str = "ci",
) -> list[OwnershipSnapshot]:
    """Compute weighted architecture ownership snapshots."""
    rows = list(rows)
    if task_level is not None:
        if task_level not in {"node", "graph"}:
            raise ValueError(f"Unsupported task level: {task_level!r}")
        rows = [row for row in rows if row.task_level == task_level]
    if weight == "sqrt":
        weight_fn = square_root_weight
    elif weight == "uniform":

        def weight_fn(_count: int) -> float:
            return 1.0

    else:
        raise ValueError(f"Unsupported weight: {weight!r}")
    if winner_policy not in {"ci", "single_mean"}:
        raise ValueError(f"Unsupported winner policy: {winner_policy!r}")

    by_dataset: dict[int, list[AnalysisRow]] = defaultdict(list)
    for row in rows:
        by_dataset[row.dataset_id].append(row)
    cutoffs = list(cutoffs) if cutoffs is not None else historical_cutoffs(rows)

    snapshots: list[OwnershipSnapshot] = []
    for cutoff in cutoffs:
        ownership: list[DatasetOwnership] = []
        category_weights: dict[str, float] = defaultdict(float)
        for dataset_rows in by_dataset.values():
            item = _ownership_for_dataset(
                dataset_rows, cutoff, min_papers, weight_fn, winner_policy=winner_policy
            )
            if item is None or not item.winner_model_types:
                continue
            ownership.append(item)
            allocation = item.weight / len(item.winner_model_types)
            for _model, category in item.winner_model_types:
                category_weights[category] += allocation
        total_weight = sum(category_weights.values())
        snapshots.append(
            OwnershipSnapshot(
                cutoff=cutoff,
                ownership=tuple(sorted(ownership, key=lambda item: item.dataset.casefold())),
                category_weights=dict(category_weights),
                total_weight=total_weight,
            )
        )
    return snapshots


def compare_override_effects(
    before_rows: Iterable[AnalysisRow],
    after_rows: Iterable[AnalysisRow],
    *,
    min_papers: int = 5,
    weight: str = "uniform",
) -> OverrideAudit:
    """Compare ownership before and after in-memory paper overrides."""
    before_rows = list(before_rows)
    after_rows = list(after_rows)
    cutoffs = historical_cutoffs(before_rows + after_rows)
    before = analyze_snapshots(before_rows, cutoffs=cutoffs, min_papers=min_papers, weight=weight)
    after = analyze_snapshots(after_rows, cutoffs=cutoffs, min_papers=min_papers, weight=weight)

    def signatures(rows: list[AnalysisRow]) -> dict[tuple[int, date], tuple]:
        by_dataset: dict[int, list[AnalysisRow]] = defaultdict(list)
        for row in rows:
            by_dataset[row.dataset_id].append(row)
        weight_fn = square_root_weight if weight == "sqrt" else (lambda _count: 1.0)
        result: dict[tuple[int, date], tuple] = {}
        for cutoff in cutoffs:
            for dataset_rows in by_dataset.values():
                item = _ownership_for_dataset(dataset_rows, cutoff, min_papers, weight_fn)
                if item is not None:
                    result[(item.dataset_id, cutoff)] = (
                        item.winner_models,
                        item.winner_types,
                        item.winner_arxiv_ids,
                    )
        return result

    before_sig = signatures(before_rows)
    after_sig = signatures(after_rows)
    all_keys = set(before_sig) | set(after_sig)
    changed = sum(before_sig.get(key) != after_sig.get(key) for key in all_keys)
    unknown_states = sum("unknown" in signature[1] for signature in before_sig.values())
    classified = sum(
        key in before_sig
        and key in after_sig
        and "unknown" in before_sig[key][1]
        and "unknown" not in after_sig[key][1]
        and bool(set(before_sig[key][2]) & set(after_sig[key][2]))
        for key in all_keys
    )
    current_cutoff = cutoffs[-1] if cutoffs else None
    before_current = {
        dataset_id: signature
        for (dataset_id, cutoff), signature in before_sig.items()
        if cutoff == current_cutoff
    }
    after_current = {
        dataset_id: signature
        for (dataset_id, cutoff), signature in after_sig.items()
        if cutoff == current_cutoff
    }
    current_changed = sum(
        before_current.get(dataset_id) != after_current.get(dataset_id)
        for dataset_id in set(before_current) | set(after_current)
    )
    removed = len({(row.paper_id, row.model, row.dataset) for row in before_rows}) - len(
        {(row.paper_id, row.model, row.dataset) for row in after_rows}
    )
    current_before_snapshot = before[-1] if before else None
    current_after_snapshot = after[-1] if after else None
    current_before_share = (
        current_before_snapshot.shares.get("transformer_involving", 0.0)
        if current_before_snapshot
        else None
    )
    current_after_share = (
        current_after_snapshot.shares.get("transformer_involving", 0.0)
        if current_after_snapshot
        else None
    )
    return OverrideAudit(
        unknown_winner_states_before=unknown_states,
        classified_from_unknown_states=classified,
        changed_current_datasets=current_changed,
        changed_cutoff_states=changed,
        problematic_rows_removed=max(0, removed),
        transformer_share_before=current_before_share,
        transformer_share_after=current_after_share,
    )
