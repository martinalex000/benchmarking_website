"""Parse dataset statistics YAML artifacts into the database."""

from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from backend.dataset_stats_matcher import (
    MatchResult,
    apply_canonical_to_orm,
    canonical_from_dataset,
    classify_match,
    merge_stats,
    observation_from_dict,
)
from backend.dataset_stats_storage import DatasetStatsStorage
from backend.dataset_variant_resolver import (
    build_dataset_variant_lookup,
    resolve_dataset_variant_quiet,
)
from backend.db import init_db, session_scope
from backend.models import Dataset, DatasetVariant, Paper, PaperDatasetStatistics

logger = logging.getLogger(__name__)


@dataclass
class DatasetStatsParseSummary:
    arxiv_id: str
    stored: int = 0
    matched: int = 0
    mismatched: int = 0
    unmatched: int = 0
    merged: int = 0
    errors: list[str] = field(default_factory=list)


def _load_yaml(path: Path) -> dict[str, Any] | None:
    try:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        return data if isinstance(data, dict) else None
    except Exception as exc:
        logger.warning("Failed to load %s: %s", path, exc)
        return None


_ZINC_FULL_MIN_GRAPHS = 200_000
_ZINC_SUBSET_MAX_GRAPHS = 20_000


def _zinc_variant_by_name(dataset: Dataset, variant_name: str | None) -> DatasetVariant | None:
    if not variant_name:
        return None
    key = variant_name.strip().lower()
    if "full" in key or "250" in key:
        return next((v for v in dataset.variants if v.name.lower() == "full"), None)
    if "subset" in key or "12k" in key or "12 k" in key:
        return next((v for v in dataset.variants if "subset" in v.name.lower()), None)
    return None


def _zinc_variant_by_graph_count(
    dataset: Dataset, num_graphs: int | float | None
) -> DatasetVariant | None:
    """Pick ZINC Full vs Subset (12k) from reported graph counts."""
    if num_graphs is None:
        return None
    count = int(round(float(num_graphs)))
    if count >= _ZINC_FULL_MIN_GRAPHS:
        return next((v for v in dataset.variants if v.name.lower() == "full"), None)
    if count <= _ZINC_SUBSET_MAX_GRAPHS:
        return next((v for v in dataset.variants if "subset" in v.name.lower()), None)
    return None


def _resolve_variant(
    session: Any,
    dataset: Dataset,
    variant_name: str | None,
    lookup: dict[str, DatasetVariant],
    payload: dict[str, Any] | None = None,
) -> DatasetVariant | None:
    if dataset.name.strip().lower() == "zinc":
        by_name = _zinc_variant_by_name(dataset, variant_name)
        if by_name is not None:
            return by_name
        by_count = _zinc_variant_by_graph_count(dataset, (payload or {}).get("num_graphs"))
        if by_count is not None:
            return by_count
        if (payload or {}).get("num_graphs") is not None:
            # e.g. 120k generative-modeling ZINC — not Full (250k) or Subset (12k).
            return None

    if variant_name:
        resolved = resolve_dataset_variant_quiet(variant_name, lookup)
        if resolved and resolved.dataset_id == dataset.id:
            return resolved
    for variant in dataset.variants:
        if variant.is_standard:
            return variant
    return dataset.variants[0] if dataset.variants else None


def _upsert_observation(
    session: Any,
    *,
    paper: Paper,
    dataset: Dataset,
    variant: DatasetVariant | None,
    payload: dict[str, Any],
    match_status: str,
    mismatch_fields: list[str],
    match_details: dict[str, str],
) -> PaperDatasetStatistics:
    row = (
        session.query(PaperDatasetStatistics)
        .filter_by(paper_id=paper.id, dataset_id=dataset.id)
        .first()
    )
    if row is None:
        row = PaperDatasetStatistics(paper_id=paper.id, dataset_id=dataset.id)
        session.add(row)

    row.dataset_variant_id = variant.id if variant else None
    row.num_graphs = payload.get("num_graphs")
    row.avg_nodes = payload.get("avg_nodes")
    row.avg_edges = payload.get("avg_edges")
    row.num_classes = payload.get("num_classes")
    row.extra_stats = json.dumps(payload.get("extra_stats") or {}, sort_keys=True)
    row.raw_values = json.dumps(payload.get("raw_values") or {}, sort_keys=True)
    row.precision_hints = json.dumps(payload.get("precision_hints") or {}, sort_keys=True)
    row.source_ref = payload.get("source_ref")
    row.confidence = payload.get("confidence")
    row.match_status = match_status
    row.mismatch_fields = json.dumps(mismatch_fields, ensure_ascii=False)
    row.match_details = json.dumps(match_details, sort_keys=True)
    row.extracted_at = payload.get("extracted_at") or row.extracted_at
    return row


def parse_and_store_dataset_statistics(arxiv_id: str) -> DatasetStatsParseSummary:
    """Ingest dataset stats YAML files for a paper into the database."""
    summary = DatasetStatsParseSummary(arxiv_id=arxiv_id)
    storage = DatasetStatsStorage()
    paths = storage.list_paper_stats_for_arxiv(arxiv_id)
    if not paths:
        return summary

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            summary.errors.append(f"paper not found: {arxiv_id}")
            return summary

        lookup = build_dataset_variant_lookup(session)

        for _slug, path in paths:
            payload = _load_yaml(path)
            if not payload:
                summary.errors.append(f"invalid yaml: {path}")
                continue

            dataset_name = payload.get("name") or ""
            variant = resolve_dataset_variant_quiet(dataset_name, lookup)
            if variant is None:
                summary.unmatched += 1
                summary.errors.append(f"unresolved dataset: {dataset_name}")
                continue

            dataset = session.query(Dataset).filter_by(id=variant.dataset_id).first()
            if dataset is None:
                summary.unmatched += 1
                continue

            target_variant = _resolve_variant(
                session,
                dataset,
                payload.get("variant"),
                lookup,
                payload,
            )

            observation = observation_from_dict(payload)
            if target_variant is not None:
                canonical = canonical_from_dataset(dataset, target_variant)
            else:
                canonical = canonical_from_dataset(dataset, None)
            match = classify_match(observation, canonical)
            if target_variant is None and dataset.name.strip().lower() == "zinc":
                match = MatchResult(
                    status="mismatch",
                    mismatch_fields=["num_graphs"],
                    match_details={
                        "num_graphs": "ambiguous ZINC size — not Full (~250k) or Subset (12k)"
                    },
                )

            if match.status == "matched":
                summary.matched += 1
                merged = merge_stats(canonical, observation)
                apply_canonical_to_orm(dataset, target_variant, merged)
                summary.merged += 1
            elif match.status == "mismatch":
                summary.mismatched += 1
            else:
                summary.matched += 1
                merged = merge_stats(canonical, observation)
                apply_canonical_to_orm(dataset, target_variant, merged)
                summary.merged += 1

            _upsert_observation(
                session,
                paper=paper,
                dataset=dataset,
                variant=target_variant,
                payload=payload,
                match_status=match.status,
                mismatch_fields=match.mismatch_fields,
                match_details=match.match_details,
            )
            summary.stored += 1

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse dataset statistics into the database")
    parser.add_argument("--paper", required=True, help="arXiv ID")
    args = parser.parse_args()

    init_db()
    summary = parse_and_store_dataset_statistics(args.paper)
    print(
        f"arxiv={summary.arxiv_id} stored={summary.stored} matched={summary.matched} "
        f"mismatched={summary.mismatched} unmatched={summary.unmatched} merged={summary.merged}"
    )
    for err in summary.errors:
        print(f"  error: {err}")


if __name__ == "__main__":
    main()
