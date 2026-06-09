"""Tests for QM9 target normalization."""

from backend.qm9_targets import (
    QM9_DEFAULT_METRIC,
    normalize_qm9_metric,
    order_qm9_metrics,
)


def test_normalize_canonical_keys():
    assert normalize_qm9_metric("gap") == "gap"
    assert normalize_qm9_metric("U0") == "U0"
    assert normalize_qm9_metric("Cv") == "Cv"


def test_normalize_aliases():
    assert normalize_qm9_metric("HOMO-LUMO gap") == "gap"
    assert normalize_qm9_metric("MAE (mu)") == "mu"
    assert normalize_qm9_metric("dipole moment") == "mu"
    assert normalize_qm9_metric("Internal energy (U0)") == "U0"
    assert normalize_qm9_metric("entropy") == "S"


def test_normalize_unknown_returns_none():
    assert normalize_qm9_metric("MAE") is None
    assert normalize_qm9_metric("") is None


def test_order_qm9_metrics_default_first():
    available = {"mu", "gap", "alpha", "H"}
    ordered = order_qm9_metrics(available, default_metric=QM9_DEFAULT_METRIC)
    assert ordered[0] == "gap"
    assert set(ordered) == available


def test_order_qm9_metrics_respects_display_list():
    available = {"S", "gap", "mu", "omega1"}
    ordered = order_qm9_metrics(
        available,
        default_metric="gap",
        display_metrics=["gap", "mu", "S"],
    )
    assert ordered.index("gap") < ordered.index("mu") < ordered.index("S")
    assert "omega1" in ordered
