"""Tests for SOTA claim verification."""

from __future__ import annotations

import json

from backend.db import init_db, session_scope
from backend.export_to_hugo import clear_export_caches
from backend.models import (
    Benchmark,
    Dataset,
    DatasetVariant,
    Model,
    Paper,
    PaperSotaClaim,
    Result,
)
from backend.sota_claim_verifier import is_unrestricted_claim, verify_unrestricted_claims


def _seed_benchmark_graph(session, *, dataset_name: str = "Cora") -> tuple[Dataset, DatasetVariant]:
    benchmark = Benchmark(name="TestBench", short_name="testbench")
    session.add(benchmark)
    session.flush()
    dataset = Dataset(
        benchmark_id=benchmark.id,
        name=dataset_name,
        task_type="node_classification",
        primary_metric="Accuracy",
        higher_is_better=1,
    )
    session.add(dataset)
    session.flush()
    variant = DatasetVariant(dataset_id=dataset.id, name="Standard split", is_standard=1)
    session.add(variant)
    session.flush()
    return dataset, variant


def _add_result(
    session,
    *,
    paper: Paper,
    model: Model,
    variant: DatasetVariant,
    value: float,
    is_baseline: bool = False,
) -> None:
    session.add(
        Result(
            paper_id=paper.id,
            model_id=model.id,
            dataset_variant_id=variant.id,
            metric_name="Accuracy",
            metric_value=value,
            is_baseline=1 if is_baseline else 0,
            higher_is_better=1,
        )
    )


def test_is_unrestricted_claim():
    unrestricted = PaperSotaClaim(
        paper_id=1,
        raw_sentence="SOTA",
        scope="unrestricted",
        restrictions=json.dumps([]),
    )
    restricted = PaperSotaClaim(
        paper_id=1,
        raw_sentence="SOTA among MPNNs",
        scope="restricted",
        restrictions=json.dumps([{"type": "model_class", "description": "MPNNs"}]),
    )
    assert is_unrestricted_claim(unrestricted) is True
    assert is_unrestricted_claim(restricted) is False


def test_verify_unrestricted_claims_marks_overstated_claim(tmp_path, monkeypatch):
    db_path = tmp_path / "benchmarks.db"
    monkeypatch.setattr("backend.config.cfg.db_path", db_path)
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))
    clear_export_caches()

    with session_scope() as session:
        dataset, variant = _seed_benchmark_graph(session)
        prior_paper = Paper(
            arxiv_id="2001.00001",
            title="Prior Best",
            published_date="2020-06-01",
            extraction_status="extracted",
        )
        claim_paper = Paper(
            arxiv_id="2101.00001",
            title="Overstated Claim",
            published_date="2021-06-01",
            extraction_status="extracted",
        )
        session.add_all((prior_paper, claim_paper))
        session.flush()

        prior_model = Model(
            name="PriorGNN",
            canonical_name="priorgnn",
            paper_id=prior_paper.id,
            is_baseline=0,
        )
        claim_model = Model(
            name="NewGNN",
            canonical_name="newgnn",
            paper_id=claim_paper.id,
            is_baseline=0,
        )
        session.add_all((prior_model, claim_model))
        session.flush()

        _add_result(
            session,
            paper=prior_paper,
            model=prior_model,
            variant=variant,
            value=0.90,
        )
        _add_result(
            session,
            paper=claim_paper,
            model=claim_model,
            variant=variant,
            value=0.70,
        )
        session.add(
            PaperSotaClaim(
                paper_id=claim_paper.id,
                raw_sentence="We achieve state-of-the-art on Cora.",
                claim_summary="SOTA on Cora",
                datasets=json.dumps(["Cora"]),
                scope="unrestricted",
                restrictions=json.dumps([]),
            )
        )

    clear_export_caches()
    with session_scope() as session:
        rows = verify_unrestricted_claims(session)
    assert len(rows) == 1
    assert rows[0].verdict == "wrong"
    assert rows[0].prior_best_value == 0.90
    assert rows[0].paper_value == 0.70


def test_verify_unrestricted_claims_verified_when_no_prior_results(tmp_path, monkeypatch):
    db_path = tmp_path / "benchmarks.db"
    monkeypatch.setattr("backend.config.cfg.db_path", db_path)
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))
    clear_export_caches()

    with session_scope() as session:
        _dataset, variant = _seed_benchmark_graph(session)
        claim_paper = Paper(
            arxiv_id="2201.00001",
            title="First Claim",
            published_date="2022-06-01",
            extraction_status="extracted",
        )
        session.add(claim_paper)
        session.flush()
        claim_model = Model(
            name="FirstGNN",
            canonical_name="firstgnn",
            paper_id=claim_paper.id,
            is_baseline=0,
        )
        session.add(claim_model)
        session.flush()
        _add_result(
            session,
            paper=claim_paper,
            model=claim_model,
            variant=variant,
            value=0.82,
        )
        session.add(
            PaperSotaClaim(
                paper_id=claim_paper.id,
                raw_sentence="We set a new best on Cora.",
                datasets=json.dumps(["Cora"]),
                scope="unrestricted",
                restrictions=json.dumps([]),
            )
        )

    clear_export_caches()
    with session_scope() as session:
        rows = verify_unrestricted_claims(session)
    assert len(rows) == 1
    assert rows[0].verdict == "verified"
    assert rows[0].prior_best_value is None
