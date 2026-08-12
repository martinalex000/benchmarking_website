"""Source-aware guards for the multi-target QM7b benchmark."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

from backend.physical_units import normalize_unit_mapping

QM7B_TARGET_UNITS: dict[str, str] = {
    "E_PBE0": "eV",
    "Emax_ZINDO": "eV",
    "Imax_ZINDO": "dimensionless",
    "HOMO_ZINDO": "eV",
    "LUMO_ZINDO": "eV",
    "E1_ZINDO": "eV",
    "IP_ZINDO": "eV",
    "EA_ZINDO": "eV",
    "HOMO_PBE0": "eV",
    "LUMO_PBE0": "eV",
    "HOMO_GW": "eV",
    "LUMO_GW": "eV",
    "alpha_PBE0": "angstrom^3",
    "alpha_SCS": "angstrom^3",
}

QM7B_METRIC_LABELS: dict[str, str] = {
    "E_PBE0": "Atomization energy, PBE0 (eV)",
    "Emax_ZINDO": "Max absorption energy, ZINDO (eV)",
    "Imax_ZINDO": "Max absorption intensity, ZINDO",
    "HOMO_ZINDO": "HOMO, ZINDO (eV)",
    "LUMO_ZINDO": "LUMO, ZINDO (eV)",
    "E1_ZINDO": "First excitation energy, ZINDO (eV)",
    "IP_ZINDO": "Ionization potential, ZINDO (eV)",
    "EA_ZINDO": "Electron affinity, ZINDO (eV)",
    "HOMO_PBE0": "HOMO, PBE0 (eV)",
    "LUMO_PBE0": "LUMO, PBE0 (eV)",
    "HOMO_GW": "HOMO, GW (eV)",
    "LUMO_GW": "LUMO, GW (eV)",
    "alpha_PBE0": "Polarizability, PBE0 (Å³)",
    "alpha_SCS": "Polarizability, SCS (Å³)",
}

QM7B_EXTRACT_TARGET_GROUPS: tuple[tuple[str, ...], ...] = (
    ("E_PBE0", "Emax_ZINDO", "Imax_ZINDO", "HOMO_ZINDO", "LUMO_ZINDO"),
    ("E1_ZINDO", "IP_ZINDO", "EA_ZINDO", "HOMO_PBE0", "LUMO_PBE0"),
    ("HOMO_GW", "LUMO_GW", "alpha_PBE0", "alpha_SCS"),
)

_TARGET_ALIASES: dict[str, tuple[str, ...]] = {
    "E_PBE0": ("e_pbe0", "atomization energy pbe0", "atomization energy - pbe0"),
    "Emax_ZINDO": (
        "emax_zindo",
        "excitation energy of maximal optimal absorption zindo",
        "max absorption energy zindo",
    ),
    "Imax_ZINDO": ("imax_zindo", "highest absorption zindo", "max absorption intensity zindo"),
    "HOMO_ZINDO": ("homo_zindo", "homo zindo"),
    "LUMO_ZINDO": ("lumo_zindo", "lumo zindo"),
    "E1_ZINDO": ("e1_zindo", "1st excitation energy zindo", "first excitation energy zindo"),
    "IP_ZINDO": ("ip_zindo", "ionization potential zindo"),
    "EA_ZINDO": ("ea_zindo", "electron affinity zindo"),
    "HOMO_PBE0": ("homo_pbe0", "homo ks", "homo pbe0"),
    "LUMO_PBE0": ("lumo_pbe0", "lumo ks", "lumo pbe0"),
    "HOMO_GW": ("homo_gw", "homo gw"),
    "LUMO_GW": ("lumo_gw", "lumo gw"),
    "alpha_PBE0": ("alpha_pbe0", "polarizability pbe0"),
    "alpha_SCS": ("alpha_scs", "polarizability scs"),
}


def _metric_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").casefold())


_ALIAS_LOOKUP = {
    _metric_key(alias): target
    for target, aliases in _TARGET_ALIASES.items()
    for alias in (target, *aliases)
}


def normalize_qm7b_metric(metric: str) -> str | None:
    """Return a canonical QM7b target key; aggregate MAE is not unit-safe."""
    return _ALIAS_LOOKUP.get(_metric_key(metric))


def qm7b_extract_metric_constraint(targets: tuple[str, ...] | list[str]) -> str:
    keys = ", ".join(targets)
    return (
        "QM7b MULTI-TARGET: extract per-target test MAE for these properties ONLY: "
        f"{keys}. Use each key exactly as metric and emit one row per (model, target). "
        "Never emit aggregate or bare MAE because QM7b mixes incompatible physical units. "
        "Copy the raw number without conversion and set unit to the exact table/source unit. "
        "Canonical target definitions are energy=eV, polarizability=angstrom^3, and "
        "Imax_ZINDO=dimensionless.\n"
    )


def is_qm7b_dataset(dataset: str) -> bool:
    """Return whether *dataset* explicitly names QM7b rather than QM7."""
    key = re.sub(r"[\s-]+", "", str(dataset or "")).casefold()
    return key in {"qm7b", "qm7bdataset"}


def _source_signals(source_text: str, *, table_text: str = "") -> tuple[str | None, bool]:
    """Return ``(reject_reason, has_random_split_evidence)`` for QM7b source."""
    text = source_text.casefold()
    context = table_text.casefold()
    if not re.search(r"\bqm\s*7[-\s]*b\b", text):
        return "source names QM7, not the distinct QM7b benchmark", False
    if (
        table_text
        and re.search(r"\bqm\s*7\b(?![-\s]*b\b)", context)
        and not re.search(r"\bqm\s*7[-\s]*b\b", context)
    ):
        return "selected result table is for QM7 rather than QM7b", False
    if context and re.search(
        r"\b(?:mse|rmse|root\s+mean\s+squared\s+error)\b|"
        r"\b(?:scaffold|stratified|chronological|time[- ]based|size[- ]based|custom)\s+split\b|"
        r"\b(?:transfer\s+learning|linear[- ]probe|linear\s+probing|pre[- ]training|"
        r"ood|out[- ]of[- ]distribution|attack|backdoor|poison)\b",
        context,
    ):
        return "source reports a noncanonical QM7b metric or evaluation setting", False

    has_random_split = bool(
        re.search(r"\brandom(?:ly)?\s+(?:split|splitting|partition|sample)", text)
        or re.search(r"\brandom\s+train(?:ing)?[\s/,-]+(?:validation|val)[\s/,-]+test", text)
        or re.search(r"\bqm\s*7[-\s]*b\b[^.]{0,100}\brandom\b", text)
    )
    if not has_random_split:
        return "canonical QM7b random-split evidence was not found", False
    return None, True


def normalize_qm7b_result_mapping(
    entry: Mapping[str, Any],
    source_text: str,
    *,
    table_text: str = "",
) -> dict[str, Any] | None:
    """Normalize or reject one extracted QM7b row before database storage.

    QM7b contains 14 heterogeneous targets, so aggregate MAE is never a valid
    leaderboard quantity. Each target is converted independently.
    """
    if not is_qm7b_dataset(str(entry.get("dataset") or "")):
        return dict(entry)

    combined_source = "\n".join(part for part in (source_text, table_text) if part)
    reject_reason, has_random_split = _source_signals(combined_source, table_text=table_text)
    if reject_reason:
        return None

    metric = normalize_qm7b_metric(str(entry.get("metric") or ""))
    if metric is None:
        return None
    if str(entry.get("protocol_decision") or "").strip().casefold() == "nonstandard":
        return None
    canonical_unit = QM7B_TARGET_UNITS[metric]
    source_unit = str(entry.get("unit") or "").strip() or canonical_unit
    normalized = normalize_unit_mapping(
        entry,
        dataset="QM7b",
        metric=metric,
        source_unit=source_unit,
        canonical_unit=canonical_unit,
    )
    if normalized is None:
        return None
    decision = str(entry.get("protocol_decision") or "").strip().casefold()
    if decision == "nonstandard":
        normalized["uses_standard_protocol"] = False
    else:
        normalized["protocol_decision"] = "standard"
        normalized["uses_standard_protocol"] = True
        note = str(normalized.get("protocol_note") or "").strip()
        if "random split" not in note.casefold():
            normalized["protocol_note"] = f"{note} QM7b random split evidence.".strip()
    return normalized


def apply_qm7b_extraction_guard(extraction: Any, source_text: str, *, table_text: str = "") -> Any:
    """Apply :func:`normalize_qm7b_result_mapping` to an ExtractionOutput."""
    kept: list[Any] = []
    dropped = 0
    for result in extraction.results:
        if not is_qm7b_dataset(getattr(result, "dataset", "")):
            kept.append(result)
            continue
        mapping = normalize_qm7b_result_mapping(
            result.model_dump(), source_text, table_text=table_text
        )
        if mapping is None:
            dropped += 1
            continue
        result = result.__class__.model_validate(mapping)
        kept.append(result)
    extraction.results = kept
    if dropped:
        extraction.extraction_notes = (
            f"{extraction.extraction_notes} QM7b guard dropped {dropped} noncanonical row(s)."
        ).strip()
    return extraction
