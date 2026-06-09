"""Verify extracted SOTA claims against at-publication leaderboard data."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy.orm import joinedload

from backend.dataset_variant_resolver import (
    build_dataset_variant_lookup,
    resolve_dataset_variant_quiet,
)
from backend.export_to_hugo import (
    _at_pub_timeline,
    _gap_magnitude,
    _is_value_better_than,
    _is_value_directionally_better,
    _is_value_worse_than,
    _primary_proposed_from_results,
)
from backend.models import Dataset, DatasetVariant, Paper, PaperSotaClaim, Result

VERDICT_ORDER = {
    "wrong": 0,
    "overstated": 1,
    "more_or_less": 2,
    "verified": 3,
    "unverifiable": 4,
}


@dataclass
class SotaClaimVerification:
    claim_id: int
    paper_id: int
    arxiv_id: str
    paper_title: str
    raw_sentence: str
    claim_summary: str
    dataset_name: str
    paper_value: float | None = None
    paper_std: float | None = None
    prior_best_value: float | None = None
    prior_best_std: float | None = None
    prior_best_arxiv: str = ""
    prior_best_title: str = ""
    gap: float | None = None
    verdict: str = "unverifiable"
    details: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


def _load_json_list(raw: str | None) -> list:
    if not raw:
        return []
    try:
        loaded = json.loads(raw)
        if isinstance(loaded, list):
            return loaded
    except (json.JSONDecodeError, TypeError):
        return []
    return []


def is_unrestricted_claim(claim: PaperSotaClaim) -> bool:
    if (claim.scope or "").strip().lower() != "unrestricted":
        return False
    restrictions = _load_json_list(claim.restrictions)
    return len(restrictions) == 0


def _global_best_at_publication(
    session: Any,
    *,
    ds_name: str,
    metric: str,
    higher_is_better: bool,
    cutoff_iso: str,
    exclude_arxiv: str,
) -> dict[str, Any] | None:
    timeline = _at_pub_timeline(session, ds_name, metric, higher_is_better)
    truth_map = timeline.truth_map(cutoff_iso, exclude_arxiv=exclude_arxiv)
    best: dict[str, Any] | None = None
    for entry in truth_map.values():
        value = entry.get("value")
        if value is None:
            continue
        if best is None or _is_value_directionally_better(
            float(value), float(best["value"]), higher_is_better
        ):
            best = entry
    return best


def _paper_proposed_result(
    session: Any,
    *,
    paper: Paper,
    dataset: Dataset,
    primary_metric: str,
) -> Result | None:
    results = (
        session.query(Result)
        .options(
            joinedload(Result.model),
            joinedload(Result.dataset_variant).joinedload(DatasetVariant.dataset),
        )
        .filter_by(paper_id=paper.id, is_baseline=False)
        .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
        .all()
    )
    proposed_models = list(
        dict.fromkeys(r.model.canonical_name for r in results if r.model and r.model.canonical_name)
    )
    primary_proposed = _primary_proposed_from_results(results, proposed_models)

    candidates: list[Result] = []
    for result in results:
        dv = result.dataset_variant
        if not dv or not dv.dataset or dv.dataset.id != dataset.id:
            continue
        metric = dataset.primary_metric or result.metric_name
        if result.metric_name != metric:
            continue
        if primary_proposed and result.model and result.model.canonical_name != primary_proposed:
            continue
        if result.display_value is None:
            continue
        candidates.append(result)

    if not candidates:
        return None

    higher = bool(candidates[0].higher_is_better)
    return max(
        candidates,
        key=lambda row: float(row.display_value) if higher else -float(row.display_value),
    )


def _classify_verdict(
    *,
    paper_value: float,
    paper_std: float | None,
    prior_value: float,
    prior_std: float | None,
    higher_is_better: bool,
) -> str:
    if _is_value_worse_than(paper_value, prior_value, higher_is_better, paper_std, prior_std):
        return "wrong"
    if _is_value_better_than(paper_value, prior_value, higher_is_better, paper_std, prior_std):
        return "verified"
    if _is_value_directionally_better(paper_value, prior_value, higher_is_better):
        return "more_or_less"
    return "overstated"


def verify_unrestricted_claims(session: Any) -> list[SotaClaimVerification]:
    """Evaluate unrestricted SOTA claims against at-publication leaderboard data."""
    lookup = build_dataset_variant_lookup(session)
    claims = (
        session.query(PaperSotaClaim)
        .options(joinedload(PaperSotaClaim.paper))
        .order_by(PaperSotaClaim.paper_id, PaperSotaClaim.id)
        .all()
    )

    verifications: list[SotaClaimVerification] = []
    for claim in claims:
        if not is_unrestricted_claim(claim):
            continue
        paper = claim.paper
        if paper is None:
            continue

        dataset_names = [
            str(name).strip() for name in _load_json_list(claim.datasets) if str(name).strip()
        ]
        if not dataset_names:
            verifications.append(
                SotaClaimVerification(
                    claim_id=claim.id,
                    paper_id=claim.paper_id,
                    arxiv_id=paper.arxiv_id,
                    paper_title=paper.title or "",
                    raw_sentence=claim.raw_sentence,
                    claim_summary=claim.claim_summary or "",
                    dataset_name="—",
                    verdict="unverifiable",
                    details="no datasets named in claim",
                )
            )
            continue

        cutoff_iso = paper.published_date[:10] if paper.published_date else ""
        if not cutoff_iso:
            for dataset_name in dataset_names:
                verifications.append(
                    SotaClaimVerification(
                        claim_id=claim.id,
                        paper_id=claim.paper_id,
                        arxiv_id=paper.arxiv_id,
                        paper_title=paper.title or "",
                        raw_sentence=claim.raw_sentence,
                        claim_summary=claim.claim_summary or "",
                        dataset_name=dataset_name,
                        verdict="unverifiable",
                        details="missing publication date",
                    )
                )
            continue

        for dataset_name in dataset_names:
            variant = resolve_dataset_variant_quiet(dataset_name, lookup)
            if variant is None or variant.dataset is None:
                verifications.append(
                    SotaClaimVerification(
                        claim_id=claim.id,
                        paper_id=claim.paper_id,
                        arxiv_id=paper.arxiv_id,
                        paper_title=paper.title or "",
                        raw_sentence=claim.raw_sentence,
                        claim_summary=claim.claim_summary or "",
                        dataset_name=dataset_name,
                        verdict="unverifiable",
                        details="unknown dataset",
                    )
                )
                continue

            dataset = variant.dataset
            primary_metric = dataset.primary_metric or ""
            if not primary_metric:
                verifications.append(
                    SotaClaimVerification(
                        claim_id=claim.id,
                        paper_id=claim.paper_id,
                        arxiv_id=paper.arxiv_id,
                        paper_title=paper.title or "",
                        raw_sentence=claim.raw_sentence,
                        claim_summary=claim.claim_summary or "",
                        dataset_name=dataset.name,
                        verdict="unverifiable",
                        details="dataset has no primary metric",
                    )
                )
                continue

            paper_result = _paper_proposed_result(
                session,
                paper=paper,
                dataset=dataset,
                primary_metric=primary_metric,
            )
            if paper_result is None or paper_result.display_value is None:
                verifications.append(
                    SotaClaimVerification(
                        claim_id=claim.id,
                        paper_id=claim.paper_id,
                        arxiv_id=paper.arxiv_id,
                        paper_title=paper.title or "",
                        raw_sentence=claim.raw_sentence,
                        claim_summary=claim.claim_summary or "",
                        dataset_name=dataset.name,
                        verdict="unverifiable",
                        details="no extracted proposed-model result",
                    )
                )
                continue

            higher = bool(paper_result.higher_is_better)
            paper_value = float(paper_result.display_value)
            paper_std = (
                float(paper_result.display_std) if paper_result.display_std is not None else None
            )

            prior_best = _global_best_at_publication(
                session,
                ds_name=dataset.name,
                metric=primary_metric,
                higher_is_better=higher,
                cutoff_iso=cutoff_iso,
                exclude_arxiv=paper.arxiv_id,
            )

            if prior_best is None or prior_best.get("value") is None:
                verifications.append(
                    SotaClaimVerification(
                        claim_id=claim.id,
                        paper_id=claim.paper_id,
                        arxiv_id=paper.arxiv_id,
                        paper_title=paper.title or "",
                        raw_sentence=claim.raw_sentence,
                        claim_summary=claim.claim_summary or "",
                        dataset_name=dataset.name,
                        paper_value=paper_value,
                        paper_std=paper_std,
                        verdict="verified",
                        details="no prior results in database at publication",
                    )
                )
                continue

            prior_value = float(prior_best["value"])
            prior_std = float(prior_best["std"]) if prior_best.get("std") is not None else None
            verdict = _classify_verdict(
                paper_value=paper_value,
                paper_std=paper_std,
                prior_value=prior_value,
                prior_std=prior_std,
                higher_is_better=higher,
            )
            verifications.append(
                SotaClaimVerification(
                    claim_id=claim.id,
                    paper_id=claim.paper_id,
                    arxiv_id=paper.arxiv_id,
                    paper_title=paper.title or "",
                    raw_sentence=claim.raw_sentence,
                    claim_summary=claim.claim_summary or "",
                    dataset_name=dataset.name,
                    paper_value=paper_value,
                    paper_std=paper_std,
                    prior_best_value=prior_value,
                    prior_best_std=prior_std,
                    prior_best_arxiv=str(prior_best.get("arxiv_id") or ""),
                    prior_best_title=str(prior_best.get("title") or ""),
                    gap=_gap_magnitude(paper_value, prior_value),
                    verdict=verdict,
                )
            )

    verifications.sort(
        key=lambda row: (
            VERDICT_ORDER.get(row.verdict, 99),
            row.paper_title.lower(),
            row.dataset_name.lower(),
        )
    )
    return verifications
