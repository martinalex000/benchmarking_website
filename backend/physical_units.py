"""Deterministic unit handling for physical-property benchmarks.

The extractor must preserve the source number and source unit.  This module is
the only place outside the QM9 target guard that converts physical quantities
to the canonical units displayed by the site.
"""

from __future__ import annotations

import math
import re
from collections.abc import Mapping
from typing import Any

EV_TO_KCAL_MOL = 23.06054783061903
HARTREE_TO_EV = 27.211386245988
KJ_MOL_TO_KCAL_MOL = 0.2390057361376673
BOHR3_TO_ANGSTROM3 = 0.14818471147216278
RADIAN_TO_DEGREE = 180.0 / math.pi


def unit_key(unit: str) -> str:
    """Return a compact comparison key for a source unit expression."""
    text = str(unit or "").casefold()
    text = re.sub(r"\\(?:mathrm|text|operatorname)\{([^{}]*)\}", r"\1", text)
    text = text.replace("Å", "angstrom").replace("å", "angstrom")
    text = text.replace("−", "-").replace("⁻", "-")
    text = text.replace("³", "^3").replace("²", "^2").replace("×", "x")
    text = text.replace("_{", "").replace("^{", "^").replace("}", "")
    return re.sub(r"[\s$\\,_{}()]", "", text)


def _is_any(key: str, candidates: set[str]) -> bool:
    return key in candidates


def unit_scale(source_unit: str, canonical_unit: str) -> float | None:
    """Return the multiplier from *source_unit* to *canonical_unit*."""
    source = unit_key(source_unit)
    target = unit_key(canonical_unit)
    if not source or not target:
        return None
    if source == target:
        return 1.0

    ev = {"ev", "electronvolt", "electronvolts"}
    mev = {"mev", "millielectronvolt", "millielectronvolts"}
    hartree = {"hartree", "hartrees", "eh"}
    kcal = {"kcal/mol", "kcalmol^-1", "kcalmol-1"}
    kj = {"kj/mol", "kjmol^-1", "kjmol-1"}

    if target == "ev":
        if _is_any(source, mev):
            return 0.001
        if _is_any(source, hartree):
            return HARTREE_TO_EV
        if _is_any(source, kcal):
            return 1.0 / EV_TO_KCAL_MOL
        if _is_any(source, kj):
            return KJ_MOL_TO_KCAL_MOL / EV_TO_KCAL_MOL
    if target == "kcal/mol":
        if _is_any(source, ev):
            return EV_TO_KCAL_MOL
        if _is_any(source, mev):
            return EV_TO_KCAL_MOL / 1000.0
        if _is_any(source, hartree):
            return HARTREE_TO_EV * EV_TO_KCAL_MOL
        if _is_any(source, kj):
            return KJ_MOL_TO_KCAL_MOL

    force_units = {
        "kcal/mol/angstrom": 1.0,
        "kcal/molangstrom": 1.0,
        "kcalmol^-1angstrom^-1": 1.0,
        "kcal/mol/a": 1.0,
        "kcal/mola": 1.0,
        "kcalmol^-1a^-1": 1.0,
        "kj/mol/angstrom": KJ_MOL_TO_KCAL_MOL,
        "kj/molangstrom": KJ_MOL_TO_KCAL_MOL,
        "kjmol^-1angstrom^-1": KJ_MOL_TO_KCAL_MOL,
        "kj/mol/nm": KJ_MOL_TO_KCAL_MOL / 10.0,
        "kjmol^-1nm^-1": KJ_MOL_TO_KCAL_MOL / 10.0,
        "ev/angstrom": EV_TO_KCAL_MOL,
        "evangstrom^-1": EV_TO_KCAL_MOL,
        "ev/a": EV_TO_KCAL_MOL,
        "mev/angstrom": EV_TO_KCAL_MOL / 1000.0,
        "mevangstrom^-1": EV_TO_KCAL_MOL / 1000.0,
        "mev/a": EV_TO_KCAL_MOL / 1000.0,
    }
    if target == "kcal/mol/angstrom":
        return force_units.get(source)

    if target == "angstrom^3":
        if source in {"a0^3", "bohr^3"}:
            return BOHR3_TO_ANGSTROM3
        if source in {"mangstrom^3", "mangstrom3"}:
            return 0.001

    if target == "e":
        if source in {"elementarycharge", "electroncharge"}:
            return 1.0
        if source in {
            "me",
            "millie",
            "10^-3",
            "x10^-3",
            "10-3",
            "10^-3e",
            "x10^-3e",
            "10-3e",
        }:
            return 0.001

    if target in {"degree", "degrees", "deg"}:
        if source in {"degree", "degrees", "deg", "°"}:
            return 1.0
        if source in {"radian", "radians", "rad"}:
            return RADIAN_TO_DEGREE

    if target in {"1", "dimensionless"} and source in {"1", "dimensionless", "unitless"}:
        return 1.0
    return None


def normalize_unit_mapping(
    entry: Mapping[str, Any],
    *,
    dataset: str,
    metric: str,
    source_unit: str,
    canonical_unit: str,
) -> dict[str, Any] | None:
    """Convert one result mapping and preserve idempotent unit provenance."""
    scale = unit_scale(source_unit, canonical_unit)
    if scale is None:
        return None
    try:
        value = float(entry.get("value"))
    except (TypeError, ValueError):
        return None
    try:
        std = None if entry.get("std") is None else float(entry.get("std"))
    except (TypeError, ValueError):
        std = None

    normalized = dict(entry)
    normalized.update(
        {
            "dataset": dataset,
            "metric": metric,
            "value": value * scale,
            "std": std * scale if std is not None else None,
            "unit": canonical_unit,
            "higher_is_better": False,
        }
    )

    note = str(entry.get("protocol_note") or "").strip()
    provenance_markers = (f"{dataset} source unit:", f"{dataset} unit normalization:")
    if not any(marker.casefold() in note.casefold() for marker in provenance_markers):
        if unit_key(source_unit) == unit_key(canonical_unit):
            detail = f"{dataset} source unit: {source_unit}."
        else:
            detail = f"{dataset} unit normalization: {source_unit} to {canonical_unit}."
        normalized["protocol_note"] = f"{note} {detail}".strip()
    return normalized
