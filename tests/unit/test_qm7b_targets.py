"""Tests for QM7b target and protocol normalization."""

import pytest

from backend.llm_types import ExtractionOutput, ResultEntry
from backend.qm7b_targets import (
    apply_qm7b_extraction_guard,
    is_qm7b_dataset,
    normalize_qm7b_metric,
    normalize_qm7b_result_mapping,
)

_CANONICAL_SOURCE = "QM7b is randomly split into train, validation, and test sets."


def test_qm7b_identity_does_not_include_qm7():
    assert is_qm7b_dataset("QM7b")
    assert is_qm7b_dataset("QM7b dataset")
    assert not is_qm7b_dataset("QM7")


def test_qm7b_normalizes_target_units():
    normalized = normalize_qm7b_result_mapping(
        {"dataset": "QM7b", "metric": "HOMO - ZINDO", "value": 200, "unit": "meV"},
        _CANONICAL_SOURCE,
    )

    assert normalized is not None
    assert normalized["dataset"] == "QM7b"
    assert normalized["metric"] == "HOMO_ZINDO"
    assert normalized["value"] == pytest.approx(0.2)
    assert normalized["unit"] == "eV"
    assert normalized["higher_is_better"] is False
    assert normalized["protocol_decision"] == "standard"


def test_qm7b_normalizes_polarizability_and_dimensionless_targets():
    alpha = normalize_qm7b_result_mapping(
        {"dataset": "QM7b", "metric": "alpha_PBE0", "value": 1, "unit": "bohr^3"},
        _CANONICAL_SOURCE,
    )
    intensity = normalize_qm7b_result_mapping(
        {"dataset": "QM7b", "metric": "Imax_ZINDO", "value": 0.08},
        _CANONICAL_SOURCE,
    )

    assert alpha is not None
    assert alpha["value"] == pytest.approx(0.14818471147216278)
    assert alpha["unit"] == "angstrom^3"
    assert intensity is not None
    assert intensity["unit"] == "dimensionless"


def test_qm7b_metric_aliases_and_aggregate_rejection():
    assert normalize_qm7b_metric("Atomization energy - PBE0") == "E_PBE0"
    assert normalize_qm7b_metric("Polarizability - SCS") == "alpha_SCS"
    assert normalize_qm7b_metric("MAE") is None


def test_qm7b_rejects_qm7_and_noncanonical_metrics_or_settings():
    assert (
        normalize_qm7b_result_mapping(
            {"dataset": "QM7b", "metric": "MAE", "value": 2.0},
            "QM7 is evaluated with a stratified split.",
        )
        is None
    )
    assert (
        normalize_qm7b_result_mapping(
            {"dataset": "QM7b", "metric": "RMSE", "value": 2.0},
            _CANONICAL_SOURCE,
        )
        is None
    )
    assert (
        normalize_qm7b_result_mapping(
            {"dataset": "QM7b", "metric": "MAE", "value": 2.0},
            "QM7b is randomly split. Transfer learning is used for the evaluation.",
        )
        is None
    )


def test_qm7b_rejects_generic_mae_from_per_target_table():
    assert (
        normalize_qm7b_result_mapping(
            {"dataset": "QM7b", "metric": "MAE", "value": 1.05},
            _CANONICAL_SOURCE,
            table_text="QM7b test set performances of all tasks. Task & MAE",
        )
        is None
    )


def test_apply_qm7b_guard_filters_output():
    output = ExtractionOutput(
        results=[
            ResultEntry(model="A", dataset="QM7b", metric="E1_ZINDO", value=1.05, unit="eV"),
            ResultEntry(model="B", dataset="QM7b", metric="RMSE", value=2.0),
        ]
    )
    apply_qm7b_extraction_guard(output, _CANONICAL_SOURCE)

    assert len(output.results) == 1
    assert output.results[0].model == "A"
