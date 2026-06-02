"""Unit tests for model architecture and parameter metadata helpers."""

import pytest

from backend.model_metadata import (
    architecture_label,
    normalize_architecture_type,
    params_exact_from_millions,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("gnn", "gnn"),
        ("graph_transformer", "graph_transformer"),
        ("llm", "llm"),
        ("graph_llm", "llm"),
        ("GraphTransformer", "graph_transformer"),
        ("GCN_variant", "gnn"),
        ("random_forest", "random_forest"),
        ("boosting", "boosting"),
        ("invalid", None),
        (None, None),
    ],
)
def test_normalize_architecture_type(raw, expected):
    assert normalize_architecture_type(raw) == expected


def test_architecture_label():
    assert architecture_label("llm") == "LLM"
    assert architecture_label("hybrid") == "Hyb"
    assert architecture_label("random_forest") == "RF"
    assert architecture_label("boosting") == "Boost"


def test_params_exact_from_millions():
    assert params_exact_from_millions(6.9) == 6_900_000
    assert params_exact_from_millions(None) is None
