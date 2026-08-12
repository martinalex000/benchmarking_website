"""Source-aware guards for benchmarks whose scores carry physical units."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

from backend.physical_units import normalize_unit_mapping, unit_key

_DATASET_NAMES = {
    "pcqm4mv2": "PCQM4Mv2",
    "freesolv": "FreeSolv",
    "md17": "MD17",
    "torsionangle": "TorsionAngle",
    "echocharge": "ECHO-Charge",
    # ECHO-Energy is intentionally guarded but unsupported: its benchmark
    # paper does not state a physical unit for the reported energy MAE.
    "echoenergy": "ECHO-Energy",
}

_MD17_MOLECULES = {
    "aspirin": "Aspirin",
    "benzene": "Benzene",
    "ethanol": "Ethanol",
    "malonaldehyde": "Malonaldehyde",
    "naphthalene": "Naphthalene",
    "salicylic acid": "Salicylic acid",
    "salicylicacid": "Salicylic acid",
    "toluene": "Toluene",
    "uracil": "Uracil",
}

_TORSION_NAMES = {
    "alpha": "alpha",
    "beta": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "epsilon",
    "zeta": "zeta",
    "chi": "chi",
    "α": "alpha",
    "β": "beta",
    "γ": "gamma",
    "δ": "delta",
    "ε": "epsilon",
    "ζ": "zeta",
    "χ": "chi",
}


def _key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").casefold())


def canonical_physical_dataset(dataset: str) -> str | None:
    return _DATASET_NAMES.get(_key(dataset))


def is_physical_unit_dataset(dataset: str) -> bool:
    return canonical_physical_dataset(dataset) is not None


def _md17_metric(metric: str) -> str | None:
    text = str(metric or "").strip()
    key = _key(text)
    quantity = None
    if key in {"e", "energy", "energymae", "maeenergy"} or "energy" in key:
        quantity = "Energy"
    elif key in {"f", "force", "forces", "forcemae", "maeforce"} or "force" in key:
        quantity = "Force"
    if quantity is None:
        return None

    for molecule_key, label in _MD17_MOLECULES.items():
        if _key(molecule_key) in key:
            return f"{label} {quantity}"
    return quantity


def _torsion_metric(metric: str) -> str | None:
    text = str(metric or "").strip()
    if text.casefold() in _TORSION_NAMES:
        return _TORSION_NAMES[text.casefold()]
    key = _key(text)
    for alias, canonical in _TORSION_NAMES.items():
        alias_key = _key(alias)
        if alias_key and (alias_key == key or alias_key in key):
            return canonical
    if key in {"mae", "circularmae", "average", "avg", "mean"}:
        return "Circular MAE"
    return None


def _metric_and_unit(dataset: str, metric: str) -> tuple[str, str] | None:
    key = _key(metric)
    if dataset == "PCQM4Mv2":
        if key in {"mae", "gap", "homolumogap", "homolumogapmae"}:
            return "MAE", "eV"
    elif dataset == "FreeSolv":
        if key in {"mae", "rmse"}:
            return key.upper(), "kcal/mol"
    elif dataset == "MD17":
        canonical = _md17_metric(metric)
        if canonical:
            unit = "kcal/mol/angstrom" if canonical.endswith("Force") else "kcal/mol"
            return canonical, unit
    elif dataset == "TorsionAngle":
        canonical = _torsion_metric(metric)
        if canonical:
            return canonical, "degree"
    elif dataset == "ECHO-Charge" and key in {"mae", "charge", "chargemae"}:
        return "MAE", "e"
    return None


_UNIT_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"(?:x|×)?\s*10\s*(?:\^\s*)?\{?\s*-?3\s*\}?\s*e\b", "x10^-3 e"),
    (r"\bmev\s*/\s*(?:angstrom|\\aa|å|Å)\b", "meV/angstrom"),
    (r"\bev\s*/\s*(?:angstrom|\\aa|å|Å)\b", "eV/angstrom"),
    (r"\bkcal\s*/?\s*mol\s*(?:/|\\?\s*)\s*(?:angstrom|\\aa|å|Å)\b", "kcal/mol/angstrom"),
    (r"\bkj\s*/?\s*mol\s*/\s*nm\b", "kJ/mol/nm"),
    (r"\bkcal\s*/?\s*mol\b", "kcal/mol"),
    (r"\bkj\s*/?\s*mol\b", "kJ/mol"),
    (r"\bhartrees?\b|\bE[_ ]?h\b", "Hartree"),
    (r"\bmev\b", "meV"),
    (r"(?<!m)\bev\b", "eV"),
    (r"(?:angstrom|\\aa|å|Å)\s*(?:\^|\{)?\s*3", "angstrom^3"),
    (r"\b(?:radians?|rad)\b", "radian"),
    (r"\bdegrees?\b|°", "degree"),
)


def _infer_source_unit(dataset: str, canonical_unit: str, source_text: str) -> str | None:
    matches = {
        unit
        for pattern, unit in _UNIT_PATTERNS
        if re.search(pattern, source_text, re.IGNORECASE) and unit_key(unit) != "e"
    }
    if dataset == "ECHO-Charge" and re.search(
        r"(?:echo[- ]?charge|\\echoc(?:\{\})?)[\s\S]{0,200}"
        r"(?:x|×|\\times)?\s*10\s*(?:\^\s*)?\{?\s*-?3",
        source_text,
        re.IGNORECASE,
    ):
        return "x10^-3 e"
    if dataset == "TorsionAngle" and re.search(r"-?180\s*\^?\s*\\?circ|180°", source_text):
        return "degree"

    compatible = [
        unit
        for unit in matches
        if normalize_unit_mapping(
            {"value": 1.0},
            dataset=dataset,
            metric="probe",
            source_unit=unit,
            canonical_unit=canonical_unit,
        )
        is not None
    ]
    return compatible[0] if len(compatible) == 1 else None


def normalize_physical_result_mapping(
    entry: Mapping[str, Any],
    source_text: str,
    *,
    table_text: str = "",
) -> dict[str, Any] | None:
    """Normalize one supported physical-unit result or reject ambiguity."""
    dataset = canonical_physical_dataset(str(entry.get("dataset") or ""))
    if dataset is None:
        return dict(entry)
    if dataset == "ECHO-Energy":
        return None
    metric_unit = _metric_and_unit(dataset, str(entry.get("metric") or ""))
    if metric_unit is None:
        return None
    metric, canonical_unit = metric_unit

    explicit_unit = str(entry.get("unit") or "").strip()
    source_unit = explicit_unit
    if not source_unit and table_text:
        source_unit = _infer_source_unit(dataset, canonical_unit, table_text)
    if not source_unit:
        source_unit = _infer_source_unit(dataset, canonical_unit, source_text)
    if not source_unit:
        return None
    return normalize_unit_mapping(
        entry,
        dataset=dataset,
        metric=metric,
        source_unit=source_unit,
        canonical_unit=canonical_unit,
    )


def apply_physical_unit_guard(
    extraction: Any,
    source_text: str,
    *,
    table_text: str = "",
) -> Any:
    """Apply deterministic physical-unit normalization to an extraction output."""
    kept: list[Any] = []
    dropped = 0
    for result in extraction.results:
        if not is_physical_unit_dataset(getattr(result, "dataset", "")):
            kept.append(result)
            continue
        mapping = normalize_physical_result_mapping(
            result.model_dump(), source_text, table_text=table_text
        )
        if mapping is None:
            dropped += 1
            continue
        kept.append(result.__class__.model_validate(mapping))
    extraction.results = kept
    if dropped:
        note = f"Physical-unit guard dropped {dropped} ambiguous or unsupported result(s)."
        extraction.extraction_notes = f"{extraction.extraction_notes or ''} {note}".strip()
    return extraction


def physical_unit_prompt_constraint(dataset: str) -> str:
    """Return dataset-specific extraction guidance for physical-unit benchmarks."""
    canonical = canonical_physical_dataset(dataset)
    if canonical == "PCQM4Mv2":
        detail = 'Use metric="MAE" for HOMO-LUMO gap prediction.'
    elif canonical == "FreeSolv":
        detail = 'Use metric="RMSE" or metric="MAE" exactly as reported.'
    elif canonical == "MD17":
        detail = (
            'Use metric="<molecule> Energy" or "<molecule> Force" for per-molecule tables; '
            'never collapse energy and force or multiple molecules into bare "MAE". Skip rMD17 tables.'
        )
    elif canonical == "TorsionAngle":
        detail = (
            "Use alpha, beta, gamma, delta, epsilon, zeta, chi, or Circular MAE as metric; "
            "do not replace angular error with MSE."
        )
    elif canonical == "ECHO-Charge":
        detail = 'Use metric="MAE" and preserve the table multiplier, such as x10^-3 e, in unit.'
    elif canonical == "ECHO-Energy":
        detail = "The source does not establish a physical result unit; emit no result rows."
    else:
        return ""
    return (
        f"PHYSICAL-UNIT BENCHMARK ({canonical}): {detail} Copy the raw numeric value without "
        "conversion and set unit to the exact source unit or scaled header. Set unit=null when "
        "the source does not state it; deterministic post-processing owns conversion.\n"
    )
