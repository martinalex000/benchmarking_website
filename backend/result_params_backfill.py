"""Backfill ``Result.params_millions`` from stored LLM extraction artifacts."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from backend.db import init_db, session_scope
from backend.models import Paper, Result
from backend.paper_storage import PaperStorage
from backend.parameter_lookup import build_dataset_param_lookup, build_metadata_lookups

logger = logging.getLogger(__name__)


@dataclass
class ParamsBackfillSummary:
    papers_seen: int = 0
    papers_with_yaml: int = 0
    results_updated: int = 0
    results_still_null: int = 0
    papers_without_yaml: int = 0
    errors: list[str] = field(default_factory=list)


def _params_lookup_for_paper(
    arxiv_id: str,
) -> tuple[dict[str, float], dict[tuple[str, str], float]] | None:
    storage = PaperStorage(arxiv_id)
    if not storage.llm_output_path.exists():
        return None
    try:
        raw = storage.load_llm_output()
    except (OSError, ValueError) as exc:
        logger.debug("Could not read llm_output for %s: %s", arxiv_id, exc)
        return None

    extraction = raw.get("results", {})
    if not isinstance(extraction, dict):
        return None
    model_sizes = extraction.get("model_sizes")
    if model_sizes is None:
        model_sizes = raw.get("model_sizes")

    sizes_lookup, _ = build_metadata_lookups(extraction, model_sizes)
    return (
        {k: float(v) for k, v in sizes_lookup.items() if v is not None},
        build_dataset_param_lookup(model_sizes),
    )


def _lookup_params(
    lookup: dict[str, float],
    canonical_name: str | None,
    rendered_name: str | None = None,
) -> float | None:
    for name in (rendered_name, canonical_name):
        if not name:
            continue
        key = str(name).strip().lower()
        if key in lookup:
            return lookup[key]
    return None


def backfill_paper_params_millions(
    session,
    paper: Paper,
    *,
    lookup: dict[str, float] | None = None,
    dataset_lookup: dict[tuple[str, str], float] | None = None,
    sanitize_model=None,
    dry_run: bool = False,
) -> tuple[int, int]:
    """Fill NULL ``params_millions`` on a paper's results. Returns (updated, still_null)."""
    rows = (
        session.query(Result)
        .filter_by(paper_id=paper.id)
        .filter(Result.params_millions.is_(None))
        .all()
    )
    if not rows:
        return 0, 0

    if lookup is None:
        paper_lookups = _params_lookup_for_paper(paper.arxiv_id)
        if paper_lookups is None:
            return 0, len(rows)
        lookup, dataset_lookup = paper_lookups
    if not lookup and not dataset_lookup:
        return 0, len(rows)

    updated = 0
    for result in rows:
        model = result.model
        canonical = model.canonical_name if model else None
        rendered = None
        if sanitize_model and canonical:
            rendered = sanitize_model(canonical, paper.arxiv_id)
        model_key = str(canonical or rendered or "").strip().casefold()
        variant = getattr(result, "dataset_variant", None)
        dataset = variant.dataset if variant else None
        dataset_key = str(dataset.name if dataset else "").strip().casefold()
        params = (dataset_lookup or {}).get((dataset_key, model_key))
        if params is None:
            params = _lookup_params(lookup or {}, canonical, rendered)
        if params is not None:
            if not dry_run:
                result.params_millions = params
            updated += 1

    still_null = len(rows) - updated
    return updated, still_null


def backfill_all_result_params_millions(
    *,
    arxiv_ids: list[str] | None = None,
    dry_run: bool = False,
    limit: int = 0,
) -> ParamsBackfillSummary:
    """Backfill parameter counts for papers that have extraction YAML on disk."""
    init_db()
    summary = ParamsBackfillSummary()

    # Late import avoids circular dependency with export_to_hugo.
    from backend.export_to_hugo import _sanitize_model

    with session_scope() as session:
        query = session.query(Paper)
        if arxiv_ids:
            query = query.filter(Paper.arxiv_id.in_(arxiv_ids))
        papers = query.order_by(Paper.arxiv_id).all()
        if limit > 0:
            papers = papers[:limit]

        from tqdm import tqdm

        for paper in tqdm(papers, desc="Backfill params_millions", unit="paper"):
            summary.papers_seen += 1
            paper_lookups = _params_lookup_for_paper(paper.arxiv_id)
            if paper_lookups is None:
                summary.papers_without_yaml += 1
                null_count = (
                    session.query(Result)
                    .filter_by(paper_id=paper.id)
                    .filter(Result.params_millions.is_(None))
                    .count()
                )
                summary.results_still_null += null_count
                continue

            summary.papers_with_yaml += 1
            lookup, dataset_lookup = paper_lookups
            updated, still_null = backfill_paper_params_millions(
                session,
                paper,
                lookup=lookup,
                dataset_lookup=dataset_lookup,
                sanitize_model=_sanitize_model,
                dry_run=dry_run,
            )
            summary.results_updated += updated
            summary.results_still_null += still_null

        if dry_run:
            session.rollback()

    return summary
