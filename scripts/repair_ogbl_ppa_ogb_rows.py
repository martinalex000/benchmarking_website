#!/usr/bin/env -S uv run python
"""Restore verified OGB ``ogbl-ppa`` rows suppressed by extraction defects.

The values below are copied from the OGB leaderboard and cross-checked against
the papers' local LaTeX sources. This is deliberately narrow: it does not
change the global extraction-quality policy or admit non-standard evaluations.
"""

from __future__ import annotations

from backend.db import init_db, session_scope
from backend.models import Dataset, DatasetVariant, Model, Paper, Result


ROWS = (
    ("2401.00529", "GraphGPT(SMTP)", 0.7655, 0.0067, 1),
    ("2411.03845", "Refined-GAE (large)", 0.7374, 0.0092, 0),
    ("2411.03845", "Refined-GAE", 0.7334, 0.0092, 0),
    ("2302.00890", "NCNC", 0.6142, 0.0073, 0),
    ("2302.00890", "NCN", 0.6119, 0.0085, 0),
    ("2411.14711", "GCN (node embedding)", 0.6354, 0.0121, 0),
    ("2303.03379", "SUREL+", 0.5432, 0.0044, 0),
)


def _model(session, name: str, paper: Paper) -> Model:
    model = session.query(Model).filter_by(canonical_name=name).one_or_none()
    if model is None:
        model = Model(
            name=name,
            canonical_name=name,
            paper_id=paper.id,
            model_type="hybrid" if name in {"SUREL+", "NCN", "NCNC"} else "gnn",
            is_baseline=0,
        )
        session.add(model)
        session.flush()
    return model


def main() -> None:
    init_db()
    with session_scope() as session:
        dataset = session.query(Dataset).filter_by(name="ogbl-ppa").one()
        variant = (
            session.query(DatasetVariant)
            .filter_by(dataset_id=dataset.id, name="Standard split")
            .one()
        )

        for arxiv_id, model_name, value, std, is_baseline in ROWS:
            paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).one()
            model = _model(session, model_name, paper)
            result = (
                session.query(Result)
                .filter_by(
                    paper_id=paper.id,
                    model_id=model.id,
                    dataset_variant_id=variant.id,
                    metric_name="Hits@100",
                )
                .one_or_none()
            )
            if result is None:
                result = Result(
                    paper_id=paper.id,
                    model_id=model.id,
                    dataset_variant_id=variant.id,
                    metric_name="Hits@100",
                    metric_value=value,
                    metric_std=std,
                    is_baseline=is_baseline,
                    higher_is_better=1,
                    table_ref="OGB leaderboard / local paper table",
                    source_ref="OGB verified submission",
                    extraction_model="manual_ogb_repair",
                )
                session.add(result)
            else:
                result.metric_value = value
                result.metric_std = std
            result.is_baseline = is_baseline
            result.higher_is_better = 1
            result.evaluation_task = "link_prediction"
            result.protocol_decision = "standard"
            result.protocol_note = "OGB official split; verified OGB leaderboard submission."
            result.is_problematic = 0
            paper.extraction_status = "extracted"

    print(f"Repaired {len(ROWS)} verified ogbl-ppa rows.")


if __name__ == "__main__":
    main()
