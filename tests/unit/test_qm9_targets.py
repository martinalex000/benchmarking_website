"""Tests for QM9 target normalization."""

import pytest

from backend.llm_types import ExtractionOutput, ResultEntry
from backend.qm9_targets import (
    QM9_DEFAULT_METRIC,
    apply_qm9_extraction_guard,
    normalize_qm9_metric,
    normalize_qm9_result_mapping,
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
    assert normalize_qm9_metric("entropy") is None


def test_normalize_unknown_returns_none():
    assert normalize_qm9_metric("MAE") is None
    assert normalize_qm9_metric("") is None


def test_order_qm9_metrics_default_first():
    available = {"mu", "gap", "alpha", "H"}
    ordered = order_qm9_metrics(available, default_metric=QM9_DEFAULT_METRIC)
    assert ordered[0] == "gap"
    assert set(ordered) == available


def test_order_qm9_metrics_respects_display_list():
    available = {"Cv", "gap", "mu", "omega1"}
    ordered = order_qm9_metrics(
        available,
        default_metric="gap",
        display_metrics=["gap", "mu", "Cv"],
    )
    assert ordered.index("gap") < ordered.index("mu") < ordered.index("Cv")
    assert "omega1" in ordered


def test_normalize_qm9_milli_units_and_mae_direction():
    source = (
        "110,000 training, 10,000 validation, 10,000 test. Energies are reported in meV.\n"
        "mu & mD & alpha & m a_0^3 & Cv & mcal/mol K"
    )
    normalized = normalize_qm9_result_mapping(
        {
            "model": "SchNet",
            "dataset": "QM9",
            "metric": "HOMO",
            "value": 41,
            "std": 2,
            "unit": "meV",
            "protocol_decision": "standard",
        },
        source,
    )

    assert normalized is not None
    assert normalized["value"] == 0.041
    assert normalized["std"] == 0.002
    assert normalized["higher_is_better"] is False
    assert normalized["protocol_decision"] == "standard"

    alpha = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "alpha", "value": 235, "unit": "m a_0^3"},
        source,
    )
    assert alpha is not None
    assert abs(alpha["value"] - 0.235) < 1e-12


def test_qm9_normalization_is_idempotent():
    source = "110,000 train, 10,000 validation, 10,000 test. Gap is reported in meV."
    first = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "gap", "value": 69, "std": 2, "unit": "meV"},
        source,
    )
    assert first is not None
    assert first["value"] == 0.069
    assert first["std"] == 0.002
    assert first["unit"] == "eV"

    second = normalize_qm9_result_mapping(first, source)
    assert second is not None
    assert second["value"] == first["value"]
    assert second["std"] == first["std"]
    assert second["unit"] == "eV"


def test_qm9_converts_kcal_mol_and_hartree_to_ev():
    kcal = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "U0", "value": 0.26, "unit": "kcal mol^-1"},
        "QM9 benchmark table.",
    )
    hartree = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "HOMO", "value": 0.001, "unit": "Hartree"},
        "QM9 benchmark table.",
    )

    assert kcal is not None
    assert kcal["value"] == pytest.approx(0.01127466998)
    assert hartree is not None
    assert hartree["value"] == pytest.approx(0.02721138625)


def test_qm9_ratio_explanation_outside_table_is_rejected():
    source = (
        "In all of our tables we report the ratio of the mean absolute error of our models "
        "with chemical accuracy."
    )
    result = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "gap", "value": 1.23, "unit": None},
        source,
        table_text="Target & model; gap & 1.23",
    )
    assert result is None


def test_qm9_unitless_physical_error_is_rejected_without_source_evidence():
    result = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "gap", "value": 1.23, "unit": None},
        "QM9 test mean absolute errors.",
        table_text="Target & model; gap & 1.23",
    )

    assert result is None


def test_qm9_drops_ratios_and_generation_results():
    ratio = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "zpve", "value": 29.96},
        "The table reports the error ratio of MAE to chemical accuracy.",
    )
    generation = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "gap", "value": 0.4},
        "Conditional generation of molecules from QM9 samples.",
    )

    assert ratio is None
    assert generation is None


def test_qm9_repairs_r2_stored_as_mu():
    normalized = normalize_qm9_result_mapping(
        {"dataset": "QM9", "metric": "mu", "value": 51.1},
        "mu (D) and R2 (Bohr^2) are reported in the QM9 table.",
    )

    assert normalized is not None
    assert normalized["metric"] == "R2"


def test_apply_qm9_guard_filters_and_normalizes_output():
    output = ExtractionOutput(
        results=[
            ResultEntry(model="A", dataset="QM9", metric="HOMO", value=41, unit="meV"),
            ResultEntry(model="B", dataset="QM9", metric="zpve", value=29.96, unit="meV"),
        ]
    )
    apply_qm9_extraction_guard(
        output,
        "110,000 train, 10,000 validation, 10,000 test. Energies are in meV.",
    )

    assert len(output.results) == 2
    assert [result.value for result in output.results] == [0.041, 0.02996]
    assert all(result.higher_is_better is False for result in output.results)
