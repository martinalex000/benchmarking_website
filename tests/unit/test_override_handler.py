"""Unit tests for override_handler."""

from pathlib import Path
from types import SimpleNamespace

import yaml

from backend.override_handler import (
    apply_overrides_to_db,
    apply_overrides_to_results,
    clear_overrides_cache,
    get_metadata_overrides,
    get_model_metadata_overrides,
    load_overrides,
)


def test_model_metadata_override_can_be_dataset_specific():
    from backend.override_handler import _model_metadata_matches

    molpcba = SimpleNamespace(
        dataset_variant=SimpleNamespace(dataset=SimpleNamespace(name="ogbg-molpcba"))
    )
    code2 = SimpleNamespace(
        dataset_variant=SimpleNamespace(dataset=SimpleNamespace(name="ogbg-code2"))
    )
    override = {"dataset": "ogbg-molpcba"}

    assert _model_metadata_matches(molpcba, override)
    assert not _model_metadata_matches(code2, override)
    assert _model_metadata_matches(code2, {})


def make_overrides_file(content: dict, tmpdir: Path) -> Path:
    p = tmpdir / "2206.08164" / "overrides.yaml"
    p.parent.mkdir(parents=True)
    p.write_text(yaml.dump(content), encoding="utf-8")
    return p


def test_load_overrides_missing(tmp_path):
    assert load_overrides("nonexistent", papers_root=tmp_path) == {}


def test_load_overrides_present(tmp_path):
    data = {
        "result_overrides": [
            {"model": "GCN", "dataset": "Cora", "metric": "Accuracy", "correct_value": 0.9}
        ]
    }
    make_overrides_file(data, tmp_path)
    result = load_overrides("2206.08164", papers_root=tmp_path)
    assert result == data


def test_apply_overrides_to_results_value():
    results = [{"model": "GCN", "dataset": "Cora", "metric": "Accuracy", "value": 0.85}]
    overrides = {
        "result_overrides": [
            {
                "model": "GCN",
                "dataset": "Cora",
                "metric": "Accuracy",
                "correct_value": 0.9,
                "reason": "Typo",
            }
        ]
    }
    out = apply_overrides_to_results(results, overrides)
    assert out[0]["is_overridden"] is True
    assert out[0]["override_value"] == 0.9
    assert "Typo" in out[0]["override_reason"]


def test_apply_overrides_marks_problematic():
    results = [{"model": "BadModel", "dataset": "Cora", "metric": "Accuracy", "value": 0.1}]
    overrides = {
        "problematic_results": [
            {"model": "BadModel", "dataset": "Cora", "metric": "Accuracy", "reason": "Wrong split"}
        ]
    }
    out = apply_overrides_to_results(results, overrides)
    assert out[0]["is_problematic"] is True


def test_apply_overrides_case_insensitive():
    results = [{"model": "GCN", "dataset": "cora", "metric": "accuracy", "value": 0.85}]
    overrides = {
        "result_overrides": [
            {"model": "gcn", "dataset": "Cora", "metric": "Accuracy", "correct_value": 0.9}
        ]
    }
    out = apply_overrides_to_results(results, overrides)
    assert out[0]["is_overridden"] is True


def test_apply_overrides_no_match():
    results = [{"model": "GAT", "dataset": "Cora", "metric": "Accuracy", "value": 0.87}]
    overrides = {
        "result_overrides": [
            {"model": "GCN", "dataset": "Cora", "metric": "Accuracy", "correct_value": 0.9}
        ]
    }
    out = apply_overrides_to_results(results, overrides)
    assert "is_overridden" not in out[0]


def test_get_metadata_overrides():
    overrides = {"metadata_overrides": {"codebase_url": "https://github.com/example/repo"}}
    meta = get_metadata_overrides(overrides)
    assert meta["codebase_url"] == "https://github.com/example/repo"


def test_get_model_metadata_overrides():
    overrides = {
        "model_metadata_overrides": [
            {"model": "GraphGPS", "params_millions": 6.9, "model_type": "hybrid"}
        ]
    }
    items = get_model_metadata_overrides(overrides)
    assert items[0]["model"] == "GraphGPS"
    assert items[0]["model_type"] == "hybrid"


def test_model_rename_overrides_support_dataset_scope():
    from backend.override_handler import _effective_model_name_for_result

    result = SimpleNamespace(
        model=SimpleNamespace(name="MLP"),
        dataset_variant=SimpleNamespace(dataset=SimpleNamespace(name="ogbn-products")),
    )
    overrides = {
        "model_renames": {"MLP": "MLP+global"},
        "model_rename_overrides": [
            {"model": "MLP", "dataset": "ogbn-products", "renamed_model": "MLP+C&S"}
        ],
    }

    assert _effective_model_name_for_result(result, overrides) == "MLP+C&S"
    result.dataset_variant.dataset.name = "ogbn-arxiv"
    assert _effective_model_name_for_result(result, overrides) == "MLP+global"


def test_apply_overrides_to_db_clears_removed_result_overrides(tmp_path, monkeypatch):
    from backend.config import cfg
    from backend.db import init_db, session_scope
    from backend.models import Benchmark, Dataset, DatasetVariant, Model, Paper, Result

    monkeypatch.setattr(cfg, "db_path", tmp_path / "benchmarks.db")
    monkeypatch.setattr(cfg, "papers_dir", tmp_path / "papers")
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(cfg.db_path))

    with session_scope() as session:
        benchmark = Benchmark(name="Bench", short_name="bench")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(benchmark_id=benchmark.id, name="Cora", primary_metric="Accuracy")
        session.add(dataset)
        session.flush()
        variant = DatasetVariant(dataset_id=dataset.id, name="Standard split")
        model = Model(name="GCN", canonical_name="gcn")
        paper = Paper(arxiv_id="2206.08164", title="Paper", codebase_url="https://bad.example")
        session.add_all((variant, model, paper))
        session.flush()
        session.add(
            Result(
                paper_id=paper.id,
                model_id=model.id,
                dataset_variant_id=variant.id,
                metric_name="Accuracy",
                metric_value=0.8,
                is_problematic=1,
                problematic_reason="old",
                is_overridden=1,
                override_value=0.9,
                override_std=0.1,
                override_reason="old",
                override_source="old",
            )
        )

    make_overrides_file(
        {"metadata_overrides": {"codebase_url": "https://github.com/example/repo"}},
        cfg.papers_dir,
    )
    clear_overrides_cache()

    apply_overrides_to_db("2206.08164")

    with session_scope() as session:
        result = session.query(Result).one()
        paper = session.query(Paper).one()
        assert result.is_problematic == 0
        assert result.problematic_reason is None
        assert result.is_overridden == 0
        assert result.override_value is None
        assert result.override_std is None
        assert paper.codebase_url == "https://github.com/example/repo"
