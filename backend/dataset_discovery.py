"""Deterministic resolution of the dataset discovery manifest."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

import yaml

from backend.config import cfg
from backend.dataset_stats_matcher import (
    StatsObservation,
    canonical_from_dataset,
    classify_match,
)
from backend.llm_types import DatasetInfo
from backend.models import Dataset, DatasetVariant

SUPPORTED_TASK_TYPES = frozenset(
    {
        "node_classification",
        "graph_classification",
        "node_regression",
        "graph_regression",
        "link_prediction",
    }
)


@dataclass(frozen=True)
class DatasetResolution:
    dataset_info: DatasetInfo
    status: str
    reason: str
    dataset: Dataset | None = None
    variant: DatasetVariant | None = None

    @property
    def tracked(self) -> bool:
        return self.status == "tracked" and self.variant is not None


def _alias_target(name: str, arxiv_id: str | None = None) -> str:
    path = cfg.config_dir / "dataset_aliases.yaml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return name.strip()

    key = name.strip().casefold()
    if arxiv_id:
        paper_aliases = (data.get("paper_aliases") or {}).get(str(arxiv_id), {})
        if isinstance(paper_aliases, dict):
            for raw, target in paper_aliases.items():
                if str(raw).strip().casefold() == key:
                    return str(target).strip()
    aliases = data.get("aliases") or {}
    if isinstance(aliases, dict):
        for raw, target in aliases.items():
            if str(raw).strip().casefold() == key:
                return str(target).strip()
    return name.strip()


def _normalised_variant_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def _dataset_for_name(session: Any, name: str, arxiv_id: str | None) -> Dataset | None:
    target = _alias_target(name, arxiv_id).casefold()
    for dataset in session.query(Dataset).all():
        if (dataset.name or "").strip().casefold() == target:
            return dataset
    return None


def _variant_from_hint(dataset: Dataset, hint: str) -> DatasetVariant | None:
    target = _normalised_variant_key(hint)
    if not target:
        return None
    if target in {"standard", "default", "canonical"}:
        return _standard_variant(dataset)
    for variant in dataset.variants:
        if _normalised_variant_key(variant.name) == target:
            return variant
    partial = [
        variant
        for variant in dataset.variants
        if len(target) >= 4 and target in _normalised_variant_key(variant.name)
    ]
    if len(partial) == 1:
        return partial[0]
    return None


def _has_observed_statistics(info: DatasetInfo) -> bool:
    return any(
        getattr(info, field_name) is not None
        for field_name in ("num_graphs", "avg_nodes", "avg_edges", "num_classes")
    )


def _observation(info: DatasetInfo) -> StatsObservation:
    return StatsObservation(
        num_graphs=info.num_graphs,
        avg_nodes=info.avg_nodes,
        avg_edges=info.avg_edges,
        num_classes=info.num_classes,
    )


def _compatible_variants(dataset: Dataset, info: DatasetInfo) -> tuple[list[DatasetVariant], bool]:
    observation = _observation(info)
    compatible: list[DatasetVariant] = []
    comparable = False
    for variant in dataset.variants:
        match = classify_match(observation, canonical_from_dataset(dataset, variant))
        if match.status == "mismatch":
            continue
        if match.status == "matched":
            comparable = True
        compatible.append(variant)
    return compatible, comparable


def _standard_variant(dataset: Dataset) -> DatasetVariant | None:
    return next((variant for variant in dataset.variants if variant.is_standard), None)


def classify_dataset_info(
    session: Any,
    info: DatasetInfo,
    *,
    arxiv_id: str | None = None,
) -> DatasetResolution:
    """Resolve one discovery observation without creating catalog records."""
    dataset = _dataset_for_name(session, info.name, arxiv_id)
    if dataset is None:
        return DatasetResolution(info, "unknown_dataset", "dataset is not in the catalog")

    canonical_task = (dataset.task_type or "").strip().casefold()
    observed_task = (info.task_type or "").strip().casefold()
    if canonical_task not in SUPPORTED_TASK_TYPES or (
        observed_task and observed_task not in SUPPORTED_TASK_TYPES
    ):
        task = observed_task or canonical_task or "missing"
        return DatasetResolution(info, "unsupported_task", f"unsupported task: {task}", dataset)

    if not dataset.variants:
        return DatasetResolution(
            info, "unknown_variant", "dataset has no tracked variants", dataset
        )

    hinted = _variant_from_hint(dataset, info.variant_hint) if info.variant_hint else None
    if info.variant_hint and hinted is None:
        return DatasetResolution(
            info,
            "unknown_variant",
            f"variant hint is not tracked: {info.variant_hint}",
            dataset,
        )

    if hinted is not None:
        candidates = [hinted]
    elif _has_observed_statistics(info):
        candidates, comparable = _compatible_variants(dataset, info)
        if not candidates:
            return DatasetResolution(
                info,
                "statistics_conflict",
                "reported structural statistics conflict with every tracked variant",
                dataset,
            )
        if not comparable and len(candidates) > 1:
            return DatasetResolution(
                info,
                "unknown_variant",
                "reported statistics do not uniquely identify a tracked variant",
                dataset,
            )
    else:
        candidates = [_standard_variant(dataset)] if _standard_variant(dataset) else []

    if len(candidates) != 1 or candidates[0] is None:
        return DatasetResolution(
            info,
            "unknown_variant",
            "variant could not be uniquely resolved from the catalog",
            dataset,
        )

    variant = candidates[0]
    if _has_observed_statistics(info):
        match = classify_match(_observation(info), canonical_from_dataset(dataset, variant))
        if match.status == "mismatch":
            return DatasetResolution(
                info,
                "statistics_conflict",
                "reported structural statistics conflict with the selected variant",
                dataset,
                variant,
            )
    return DatasetResolution(
        info, "tracked", f"resolved to variant: {variant.name}", dataset, variant
    )


def classify_dataset_infos(
    session: Any,
    infos: list[DatasetInfo],
    *,
    arxiv_id: str | None = None,
) -> list[DatasetResolution]:
    return [classify_dataset_info(session, info, arxiv_id=arxiv_id) for info in infos]


def discovery_payload(info: DatasetInfo) -> str:
    """Serialize the normalized detector observation for pending-dataset audit."""
    return json.dumps(info.model_dump(mode="json"), ensure_ascii=False, sort_keys=True)
