"""At-publication leaderboard timelines for export and SOTA verification."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sqlalchemy.orm import joinedload

from backend.export_helpers import plain_model, sanitize_model, sanitize_title
from backend.leaderboard_compare import is_value_directionally_better
from backend.models import Dataset, DatasetVariant, Result

_AT_PUB_ROWS_CACHE: dict[tuple[str, str], list[Any]] = {}
_AT_PUB_TIMELINE_CACHE: dict[tuple[str, str, bool], Any] = {}
_AT_PUB_MODEL_CACHE: dict[tuple[str, str, bool, str], dict[str, dict[str, Any]]] = {}
_AT_PUB_EXCLUDING_CACHE: dict[tuple[str, str, bool, str, str], dict[str, dict[str, Any]]] = {}


def clear_at_pub_caches() -> None:
    _AT_PUB_ROWS_CACHE.clear()
    _AT_PUB_TIMELINE_CACHE.clear()
    _AT_PUB_MODEL_CACHE.clear()
    _AT_PUB_EXCLUDING_CACHE.clear()


def model_key(model_name: str | None) -> str:
    from backend.model_name_resolution import strip_implementation_marker

    return strip_implementation_marker(plain_model(model_name)).lower()


@dataclass(frozen=True, slots=True)
class AtPubEvent:
    pub_iso: str
    value: float
    std: float | None
    arxiv_id: str
    title: str
    venue: str
    model_name: str


class AtPubTimeline:
    """Per-model publication-ordered events for fast at-date best lookups."""

    __slots__ = ("_by_model", "_hib", "_model_truth_cache", "_truth_cache")

    def __init__(self, all_res: list[Any], higher_is_better: bool) -> None:
        self._hib = higher_is_better
        by_model: dict[str, list[AtPubEvent]] = {}
        for result in all_res:
            paper = result.paper
            if not paper:
                continue
            key = model_key(result.model.canonical_name if result.model else "")
            if not key or result.display_value is None:
                continue
            by_model.setdefault(key, []).append(
                AtPubEvent(
                    pub_iso=(paper.published_date[:10] if paper.published_date else ""),
                    value=float(result.display_value),
                    std=float(result.display_std) if result.display_std is not None else None,
                    arxiv_id=paper.arxiv_id or "",
                    title=paper.title or "",
                    venue=paper.venue or "",
                    model_name=(result.model.canonical_name if result.model else ""),
                )
            )
        for events in by_model.values():
            events.sort(key=lambda event: event.pub_iso)
        self._by_model = by_model
        self._truth_cache: dict[tuple[str, str], dict[str, dict[str, Any]]] = {}
        self._model_truth_cache: dict[tuple[str, str, str], dict[str, Any] | None] = {}

    def _best_event(
        self,
        model_key_name: str,
        cutoff_iso: str = "",
        *,
        exclude_arxiv: str = "",
    ) -> AtPubEvent | None:
        best: AtPubEvent | None = None
        for event in self._by_model.get(model_key_name, ()):
            if cutoff_iso and (not event.pub_iso or event.pub_iso > cutoff_iso):
                break
            if exclude_arxiv and event.arxiv_id == exclude_arxiv:
                continue
            if best is None or is_value_directionally_better(event.value, best.value, self._hib):
                best = event
        return best

    def best_for_model(
        self,
        model_key_name: str,
        cutoff_iso: str = "",
        *,
        exclude_arxiv: str = "",
    ) -> dict[str, Any] | None:
        """Best prior result for a single model (avoids building a full truth map)."""
        cache_key = (cutoff_iso or "", (exclude_arxiv or "").strip(), model_key_name)
        if cache_key in self._model_truth_cache:
            return self._model_truth_cache[cache_key]

        event = self._best_event(model_key_name, cutoff_iso, exclude_arxiv=exclude_arxiv)
        if event is None:
            self._model_truth_cache[cache_key] = None
            return None

        entry = {
            "model": sanitize_model(event.model_name),
            "model_key": model_key_name,
            "value": event.value,
            "std": event.std,
            "arxiv_id": event.arxiv_id,
            "title": sanitize_title(event.title),
            "date_iso": event.pub_iso,
            "venue": event.venue,
        }
        self._model_truth_cache[cache_key] = entry
        return entry

    def truth_map(
        self,
        cutoff_iso: str = "",
        *,
        exclude_arxiv: str = "",
    ) -> dict[str, dict[str, Any]]:
        cache_key = (cutoff_iso or "", (exclude_arxiv or "").strip())
        cached = self._truth_cache.get(cache_key)
        if cached is not None:
            return cached

        cutoff = cache_key[0]
        exclude = cache_key[1]
        truth_map: dict[str, dict[str, Any]] = {}
        for key in self._by_model:
            entry = self.best_for_model(key, cutoff, exclude_arxiv=exclude)
            if entry is not None:
                truth_map[key] = entry
        self._truth_cache[cache_key] = truth_map
        return truth_map


def _at_pub_results_for_dataset_metric(session: Any, ds_name: str, metric: str) -> list[Any]:
    """All non-problematic results for a dataset/metric (one query per export run)."""
    rows_key = (ds_name, metric)
    cached = _AT_PUB_ROWS_CACHE.get(rows_key)
    if cached is not None:
        return cached

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
    _AT_PUB_ROWS_CACHE[rows_key] = all_res
    return all_res


def at_pub_timeline(
    session: Any, ds_name: str, metric: str, higher_is_better: bool
) -> AtPubTimeline:
    timeline_key = (ds_name, metric, higher_is_better)
    cached = _AT_PUB_TIMELINE_CACHE.get(timeline_key)
    if cached is not None:
        return cached
    rows = _at_pub_results_for_dataset_metric(session, ds_name, metric)
    timeline = AtPubTimeline(rows, higher_is_better)
    _AT_PUB_TIMELINE_CACHE[timeline_key] = timeline
    return timeline


def at_pub_truth_map_from_results(
    all_res: list[Any],
    higher_is_better: bool,
    cutoff_iso: str,
) -> dict[str, dict[str, Any]]:
    """Best result per model on or before *cutoff_iso* from preloaded rows."""
    timeline = AtPubTimeline(all_res, higher_is_better)
    return timeline.truth_map(cutoff_iso)


def global_best_per_model_as_of_date(
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

    truth_map = at_pub_timeline(session, ds_name, metric, higher_is_better).truth_map(cutoff_iso)
    _AT_PUB_MODEL_CACHE[cache_key] = truth_map
    return truth_map


def global_best_per_model_as_of_date_excluding_paper(
    session: Any,
    ds_name: str,
    metric: str,
    higher_is_better: bool,
    cutoff_iso: str,
    exclude_arxiv: str,
) -> dict[str, dict[str, Any]]:
    """Best per model on/before *cutoff_iso*, excluding *exclude_arxiv*."""
    exclude_norm = (exclude_arxiv or "").strip()
    cache_key = (ds_name, metric, higher_is_better, cutoff_iso or "", exclude_norm)
    if cache_key in _AT_PUB_EXCLUDING_CACHE:
        return _AT_PUB_EXCLUDING_CACHE[cache_key]

    truth_map = at_pub_timeline(session, ds_name, metric, higher_is_better).truth_map(
        cutoff_iso,
        exclude_arxiv=exclude_norm,
    )
    _AT_PUB_EXCLUDING_CACHE[cache_key] = truth_map
    return truth_map
