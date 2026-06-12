"""Parse SOTA claim YAML artifacts into the database."""

from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from backend.db import init_db, session_scope
from backend.models import Paper, PaperSotaClaim
from backend.paper_storage import PaperStorage, load_yaml_dict

logger = logging.getLogger(__name__)


@dataclass
class SotaClaimParseSummary:
    arxiv_id: str
    stored: int = 0
    errors: list[str] = field(default_factory=list)


def _json_list(value: Any) -> str:
    if not isinstance(value, list):
        return json.dumps([], ensure_ascii=False)
    return json.dumps(value, ensure_ascii=False)


def _claims_path(arxiv_id: str) -> Path:
    return PaperStorage(arxiv_id).extracted_dir / "sota_claims.yaml"


def parse_and_store_sota_claims(arxiv_id: str) -> SotaClaimParseSummary:
    summary = SotaClaimParseSummary(arxiv_id=arxiv_id)
    path = _claims_path(arxiv_id)
    if not path.exists():
        return summary

    payload = load_yaml_dict(path)
    if not payload:
        summary.errors.append(f"invalid yaml: {path}")
        return summary

    claims = payload.get("claims")
    if not isinstance(claims, list):
        summary.errors.append("missing claims list")
        return summary

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            summary.errors.append(f"paper not found: {arxiv_id}")
            return summary

        session.query(PaperSotaClaim).filter_by(paper_id=paper.id).delete()
        for item in claims:
            if not isinstance(item, dict):
                continue
            raw_sentence = str(item.get("raw_sentence") or "").strip()
            if not raw_sentence:
                continue
            restrictions = item.get("restrictions")
            if not isinstance(restrictions, list):
                restrictions = []
            session.add(
                PaperSotaClaim(
                    paper_id=paper.id,
                    raw_sentence=raw_sentence,
                    claim_summary=str(item.get("claim_summary") or "").strip() or None,
                    datasets=_json_list(item.get("datasets")),
                    metrics=_json_list(item.get("metrics")),
                    claim_type=str(item.get("claim_type") or "").strip() or None,
                    scope=str(item.get("scope") or "unclear").strip() or "unclear",
                    restrictions=json.dumps(restrictions, ensure_ascii=False),
                    source_ref=str(item.get("source_ref") or "").strip() or None,
                    confidence=str(item.get("confidence") or "").strip() or None,
                )
            )
            summary.stored += 1

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse SOTA claims into the database")
    parser.add_argument("--paper", required=True, help="arXiv ID")
    args = parser.parse_args()

    init_db()
    summary = parse_and_store_sota_claims(args.paper)
    print(f"arxiv={summary.arxiv_id} stored={summary.stored}")
    for err in summary.errors:
        print(f"  error: {err}")


if __name__ == "__main__":
    main()
