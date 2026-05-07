"""Unit tests for override_handler."""

import pytest
from backend.override_handler import (
    apply_overrides_to_results,
    get_metadata_overrides,
    load_overrides,
)
from pathlib import Path
import tempfile, yaml


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
