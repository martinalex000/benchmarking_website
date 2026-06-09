"""Tests for SOTA claim parser."""

from __future__ import annotations

import yaml

from backend.db import init_db, session_scope
from backend.models import Paper, PaperSotaClaim
from backend.paper_storage import PaperStorage
from backend.sota_claim_parser import parse_and_store_sota_claims


def test_parse_and_store_sota_claims_upserts_rows(tmp_path, monkeypatch):
    db_path = tmp_path / "benchmarks.db"
    monkeypatch.setattr("backend.config.cfg.db_path", db_path)
    monkeypatch.setattr("backend.config.cfg.papers_dir", tmp_path / "papers")
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))

    arxiv_id = "2206.08164"
    storage = PaperStorage(arxiv_id)
    storage.ensure_dirs()
    storage.extracted_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "arxiv_id": arxiv_id,
        "claims": [
            {
                "raw_sentence": "We achieve state-of-the-art on Peptides-func.",
                "claim_summary": "SOTA on Peptides-func",
                "datasets": ["Peptides-func"],
                "metrics": ["AP"],
                "claim_type": "absolute_sota",
                "scope": "unrestricted",
                "restrictions": [],
                "source_ref": "Abstract",
                "confidence": "high",
            },
            {
                "raw_sentence": "Among MPNNs, our model is best on Cora.",
                "claim_summary": "Best MPNN on Cora",
                "datasets": ["Cora"],
                "scope": "restricted",
                "restrictions": [{"type": "model_class", "description": "MPNNs only"}],
            },
        ],
    }
    (storage.extracted_dir / "sota_claims.yaml").write_text(
        yaml.safe_dump(payload, sort_keys=False),
        encoding="utf-8",
    )

    with session_scope() as session:
        session.add(
            Paper(
                arxiv_id=arxiv_id,
                title="Test Paper",
                extraction_status="extracted",
            )
        )

    summary = parse_and_store_sota_claims(arxiv_id)
    assert summary.stored == 2

    with session_scope() as session:
        rows = session.query(PaperSotaClaim).order_by(PaperSotaClaim.id).all()
        assert len(rows) == 2
        assert rows[0].scope == "unrestricted"
        assert rows[1].scope == "restricted"

    summary_again = parse_and_store_sota_claims(arxiv_id)
    assert summary_again.stored == 2
    with session_scope() as session:
        assert session.query(PaperSotaClaim).count() == 2
