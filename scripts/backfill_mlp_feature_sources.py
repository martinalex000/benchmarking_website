"""Backfill confirmed MLP rows that consume language-model features.

New extractions derive this from per-result provenance.  This small, explicit
registry repairs historical rows whose extraction artifacts predate that field.
It is intentionally conservative: papers with mixed or ambiguous MLP inputs are
not included.
"""

from __future__ import annotations

import argparse

from sqlalchemy import select

from backend.db import init_db, session_scope
from backend.llm_types import normalize_input_feature_source
from backend.models import Model, Paper, Result

BACKFILL: dict[str, str] = {
    "2111.00064": "GIANT-XRT node embeddings are fed into the downstream MLP.",
    "2408.14512": "The paper uses pretrained BERT node features for the MLP baseline.",
    "2501.15755": "The paper states that MLP baselines uniformly use BERT embeddings.",
    "2503.03313": "The paper states that BERT is used for node initialization across applicable baselines.",
    "2505.19762": "The MLP baseline consumes node embeddings encoded by the DeBERTa SLM.",
}


def backfill(*, apply: bool) -> int:
    init_db()
    changed = 0
    with session_scope() as session:
        target = session.scalar(select(Model).where(Model.canonical_name == "MLP+LLM_features"))
        if target is None:
            target = Model(
                name="MLP+LLM_features",
                canonical_name="MLP+LLM_features",
                model_type="other_traditional",
            )
            if apply:
                session.add(target)
                session.flush()

        for arxiv_id, evidence in BACKFILL.items():
            paper = session.scalar(select(Paper).where(Paper.arxiv_id == arxiv_id))
            if paper is None:
                continue
            rows = list(
                session.scalars(
                    select(Result)
                    .join(Model, Result.model_id == Model.id)
                    .where(Result.paper_id == paper.id, Model.canonical_name == "MLP")
                )
            )
            for result in rows:
                changed += 1
                if not apply:
                    continue
                result.model_id = target.id
                result.input_feature_source = normalize_input_feature_source("llm_features")
                result.feature_source_evidence = evidence

    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the confirmed historical corrections; otherwise only report the count",
    )
    args = parser.parse_args()
    count = backfill(apply=args.apply)
    action = "Updated" if args.apply else "Would update"
    print(f"{action} {count} historical MLP result row(s).")


if __name__ == "__main__":
    main()
