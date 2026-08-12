"""Tests for deterministic physical-unit benchmark normalization."""

import pytest

from backend.llm_types import ExtractionOutput, ResultEntry
from backend.physical_unit_targets import (
    apply_physical_unit_guard,
    normalize_physical_result_mapping,
)
from backend.physical_units import unit_scale


def test_energy_and_force_unit_scales():
    assert unit_scale("meV", "eV") == pytest.approx(0.001)
    assert unit_scale("eV", "kcal/mol") == pytest.approx(23.06054783061903)
    assert unit_scale("meV/angstrom", "kcal/mol/angstrom") == pytest.approx(0.02306054783061903)
    assert unit_scale("kJ/mol/nm", "kcal/mol/angstrom") == pytest.approx(0.02390057361376673)


def test_pcqm4mv2_normalization_is_idempotent():
    first = normalize_physical_result_mapping(
        {"dataset": "PCQM4Mv2", "metric": "MAE", "value": 80, "unit": "meV"},
        "HOMO-LUMO gap benchmark.",
    )
    assert first is not None
    assert first["value"] == pytest.approx(0.08)
    assert first["unit"] == "eV"

    second = normalize_physical_result_mapping(first, "HOMO-LUMO gap benchmark.")
    assert second is not None
    assert second["value"] == first["value"]


def test_freesolv_converts_kj_per_mol():
    result = normalize_physical_result_mapping(
        {"dataset": "FreeSolv", "metric": "RMSE", "value": 4.184, "unit": "kJ/mol"},
        "FreeSolv hydration free energy.",
    )

    assert result is not None
    assert result["value"] == pytest.approx(1.0)
    assert result["unit"] == "kcal/mol"


def test_md17_preserves_molecule_and_quantity():
    force = normalize_physical_result_mapping(
        {
            "dataset": "MD17",
            "metric": "Aspirin Force",
            "value": 10,
            "unit": "meV/angstrom",
        },
        "MD17 force benchmark.",
    )
    energy = normalize_physical_result_mapping(
        {"dataset": "MD17", "metric": "Ethanol Energy", "value": 1, "unit": "kcal/mol"},
        "MD17 energy benchmark.",
    )

    assert force is not None
    assert force["metric"] == "Aspirin Force"
    assert force["value"] == pytest.approx(0.2306054783061903)
    assert energy is not None
    assert energy["metric"] == "Ethanol Energy"


def test_torsion_angles_convert_radians_to_degrees():
    result = normalize_physical_result_mapping(
        {"dataset": "TorsionAngle", "metric": "alpha", "value": 0.1, "unit": "radian"},
        "Torsion angles.",
    )

    assert result is not None
    assert result["value"] == pytest.approx(5.729577951308233)
    assert result["unit"] == "degree"


def test_echo_charge_applies_scaled_header():
    result = normalize_physical_result_mapping(
        {"dataset": "ECHO-Charge", "metric": "MAE", "value": 6.109, "unit": "x10^-3 e"},
        "Atomic partial-charge benchmark.",
    )

    assert result is not None
    assert result["value"] == pytest.approx(0.006109)
    assert result["unit"] == "e"

    inferred = normalize_physical_result_mapping(
        {"dataset": "ECHO-Charge", "metric": "MAE", "value": 6.109, "unit": None},
        r"ECHO-Charge results are reported in units of $10^{-3}$.",
    )
    assert inferred is not None
    assert inferred["value"] == pytest.approx(0.006109)


def test_ambiguous_or_unsupported_physical_units_fail_closed():
    assert (
        normalize_physical_result_mapping(
            {"dataset": "FreeSolv", "metric": "RMSE", "value": 1.2, "unit": None},
            "FreeSolv results without a stated unit.",
        )
        is None
    )
    assert (
        normalize_physical_result_mapping(
            {"dataset": "MD17", "metric": "MAE", "value": 1.2, "unit": "meV"},
            "MD17 energy and force results.",
        )
        is None
    )
    assert (
        normalize_physical_result_mapping(
            {"dataset": "ECHO-Energy", "metric": "MAE", "value": 5.257, "unit": None},
            "The paper does not state the energy unit.",
        )
        is None
    )
    assert (
        normalize_physical_result_mapping(
            {"dataset": "TorsionAngle", "metric": "MSE", "value": 1.2, "unit": "degree"},
            "TorsionAngle results.",
        )
        is None
    )


def test_physical_guard_only_changes_supported_datasets():
    output = ExtractionOutput(
        results=[
            ResultEntry(model="A", dataset="PCQM4Mv2", metric="MAE", value=80, unit="meV"),
            ResultEntry(model="B", dataset="Cora", metric="Accuracy", value=0.8),
        ]
    )

    apply_physical_unit_guard(output, "PCQM4Mv2 gap results in meV.")

    assert [result.dataset for result in output.results] == ["PCQM4Mv2", "Cora"]
    assert output.results[0].value == pytest.approx(0.08)
