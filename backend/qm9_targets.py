"""Canonical QM9 target property names, display labels, and alias normalization."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

# Curated display order: user-priority targets first, then other common PyG targets.
QM9_TARGETS: tuple[str, ...] = (
    "gap",
    "mu",
    "alpha",
    "U0",
    "H",
    "G",
    "Cv",
    "HOMO",
    "LUMO",
    "zpve",
    "R2",
    "U",
    "omega1",
    "A",
    "B",
    "C",
    "mu_N",
    "R2_xyz",
)

QM9_METRIC_LABELS: dict[str, str] = {
    "gap": "HOMO-LUMO gap (eV)",
    "mu": "Dipole moment (D)",
    "alpha": "Polarizability (a₀³)",
    "U0": "Internal energy (U₀, eV)",
    "H": "Enthalpy (H, eV)",
    "G": "Free energy (G, eV)",
    "Cv": "Heat capacity (cal mol⁻¹ K⁻¹)",
    "HOMO": "HOMO (eV)",
    "LUMO": "LUMO (eV)",
    "zpve": "Zero point vibrational energy (eV)",
    "R2": "Electronic spatial extent (a₀²)",
    "U": "Internal energy (U, eV)",
    "omega1": "Highest vibrational frequency (cm⁻¹)",
    "A": "Rotational constant A (GHz)",
    "B": "Rotational constant B (GHz)",
    "C": "Rotational constant C (GHz)",
    "mu_N": "Nuclear repulsion energy (eV)",
    "R2_xyz": "R² (xyz, a₀²)",
}

QM9_DEFAULT_METRIC = "gap"

# Target groups for chunked LLM extraction (keeps responses under token limits).
QM9_EXTRACT_TARGET_GROUPS: tuple[tuple[str, ...], ...] = (
    ("gap", "mu", "alpha"),
    ("U0", "H", "G", "Cv"),
    ("HOMO", "LUMO", "zpve", "R2", "U", "omega1"),
)

# Normalized alias -> canonical key
_QM9_ALIAS_MAP: dict[str, str] = {}


_BARE_METRIC_REJECT: frozenset[str] = frozenset({"mae", "rmse", "loss", "mse"})

QM9_ENERGY_TARGETS: frozenset[str] = frozenset({"gap", "HOMO", "LUMO", "U0", "U", "H", "G", "zpve"})

QM9_CANONICAL_UNITS: dict[str, str] = {
    **dict.fromkeys(QM9_ENERGY_TARGETS, "eV"),
    "mu": "D",
    "alpha": "a0^3",
    "R2": "a0^2",
    "Cv": "cal/mol K",
    "omega1": "cm^-1",
    "A": "GHz",
    "B": "GHz",
    "C": "GHz",
    "mu_N": "eV",
    "R2_xyz": "a0^2",
}

_KCAL_MOL_TO_EV = 0.0433641153087705
_HARTREE_TO_EV = 27.211386245988
_ANGSTROM3_TO_BOHR3 = 6.748334494600374
_ANGSTROM2_TO_BOHR2 = 3.571064826093132
_JOULE_TO_CALORIE = 0.2390057361376673

_QM9_TARGET_LINE_PATTERNS: dict[str, str] = {
    "gap": r"(?:homo\s*[- ]?\s*lumo|delta[_ ]?\\?epsilon|\\?Delta[_ ]?\\?epsilon|gap)",
    "mu": r"(?:\\?mu\b|dipole)",
    "alpha": r"(?:\\?alpha\b|polarizability)",
    "U0": r"(?:\\?u[_ ]?0\b|u\{?0\}?|internal\s+energy)",
    "U": r"(?:^|[^a-z])u(?:$|[^a-z0-9])",
    "H": r"(?:^|[^a-z])h(?:$|[^a-z0-9])|enthalpy",
    "G": r"(?:^|[^a-z])g(?:$|[^a-z0-9])|free\s+energy|gibbs",
    "Cv": r"(?:c[_ ]?v|heat\s+capacity)",
    "HOMO": r"(?:homo|highest\s+occupied)",
    "LUMO": r"(?:lumo|lowest\s+unoccupied)",
    "zpve": r"(?:zpve|zero\s+point)",
    "R2": r"(?:r\\?\s*\^?\s*2|r\s*squared|spatial\s+extent)",
    "omega1": r"(?:omega|vibrational\s+frequency)",
}


@dataclass(frozen=True)
class QM9SourceSignals:
    """Source-level facts used to protect the canonical QM9 result stream."""

    reject_reason: str | None = None
    has_canonical_split: bool = False


def _qm9_source_signals(source_text: str, *, result_table_text: str = "") -> QM9SourceSignals:
    # Reject only when the selected result table itself carries the bad
    # protocol marker. A property-prediction paper may discuss generation in a
    # related-work section without making its QM9 table non-canonical.
    signal_text = (result_table_text or source_text).casefold()
    text = source_text.casefold()
    if re.search(
        r"(?:error\s+ratio|ratio\s+of\s+(?:the\s+)?mae|"
        r"mae\s+(?:to|/)\s+chemical\s+accuracy|chemical\s+accuracy.{0,40}ratio)",
        signal_text,
    ):
        return QM9SourceSignals(
            reject_reason="source reports an error ratio rather than test-set MAE"
        )
    # Some papers explain immediately outside the table that every displayed
    # value is a ratio. Keep this deliberately strong to avoid rejecting a
    # canonical table merely because related work mentions error ratios.
    if re.search(
        r"(?:in\s+all\s+of\s+our\s+tables|tables?\s+(?:show|report|display))"
        r".{0,100}\bratio\s+of\s+(?:the\s+)?(?:mean\s+absolute\s+error|mae)\b",
        text,
        re.DOTALL,
    ):
        return QM9SourceSignals(
            reject_reason="source reports an error ratio rather than test-set MAE"
        )
    if re.search(
        r"(?:conditional\s+generation|molecule(?:\s+|-)generation|"
        r"generated\s+(?:molecules|samples|structures))",
        signal_text,
    ):
        return QM9SourceSignals(
            reject_reason="source reports molecular generation rather than supervised property prediction"
        )

    # QM9's commonly published split is 110k/10k/10k (some papers use 10,831
    # test examples), or the equivalent 80/10/10 statement.
    has_split = bool(
        re.search(r"\b80\s*/\s*10\s*/\s*10\b", text)
        or re.search(
            r"\b110\s*,?\s*000\b.{0,180}\b10\s*,?\s*000\b.{0,180}" r"\b10\s*,?\s*(?:000|831)\b",
            text,
            re.DOTALL,
        )
        or re.search(
            r"\b10\s*,?\s*000\b.{0,120}\b10\s*,?\s*831\b.{0,120}" r"(?:remaining|train|training)",
            text,
            re.DOTALL,
        )
    )
    return QM9SourceSignals(has_canonical_split=has_split)


def _qm9_target_context(metric: str, source_text: str) -> str:
    pattern = _QM9_TARGET_LINE_PATTERNS.get(metric)
    if not pattern:
        return ""
    lines = [line for line in source_text.splitlines() if re.search(pattern, line, re.IGNORECASE)]
    return "\n".join(lines)


def _has_mev(text: str) -> bool:
    return bool(re.search(r"\bmev\b", text, re.IGNORECASE))


def _has_ev(text: str) -> bool:
    return bool(re.search(r"(?<!m)\bev\b", text, re.IGNORECASE))


def _unit_key(unit: str) -> str:
    """Return a compact comparison key for a source unit string."""
    text = unit.casefold()
    text = re.sub(r"\\(?:mathrm|text|operatorname)\{([^{}]*)\}", r"\1", text)
    text = text.replace("Å", "angstrom").replace("å", "angstrom")
    text = text.replace("⁻", "-").replace("³", "^3").replace("²", "^2")
    text = text.replace("_{", "").replace("^{", "^").replace("}", "")
    return re.sub(r"[\s$\\,_{}()]", "", text)


def _explicit_unit_scale(metric: str, unit: str) -> float | None:
    """Return the multiplier from an explicit source unit to the canonical unit."""
    key = _unit_key(unit)
    if metric in QM9_ENERGY_TARGETS or metric == "mu_N":
        if key in {"ev", "electronvolt", "electronvolts"}:
            return 1.0
        if key in {"mev", "millielectronvolt", "millielectronvolts"}:
            return 0.001
        if "kcal/mol" in key or "kcalmol^-1" in key or "kcalmol-1" in key:
            return _KCAL_MOL_TO_EV
        if key in {"hartree", "eh", "e_h"}:
            return _HARTREE_TO_EV
    if metric == "mu":
        if key in {"d", "debye"}:
            return 1.0
        if key in {"md", "millidebye"}:
            return 0.001
    if metric in {"alpha", "R2", "R2_xyz"}:
        power = "3" if metric == "alpha" else "2"
        if key in {f"a0^{power}", f"bohr^{power}"}:
            return 1.0
        # Many QM9 comparison tables repeat a known R² header typo as bohr³.
        # The values are still the conventional spatial-extent MAE in bohr².
        if metric in {"R2", "R2_xyz"} and key in {"a0^3", "bohr^3"}:
            return 1.0
        if key in {f"ma0^{power}", f"mbohr^{power}"}:
            return 0.001
        if key == f"angstrom^{power}":
            return _ANGSTROM3_TO_BOHR3 if power == "3" else _ANGSTROM2_TO_BOHR2
    if metric == "Cv":
        if key in {"cal/molk", "calmol^-1k^-1", "calmol-1k-1"}:
            return 1.0
        if key in {"mcal/molk", "mcalmol^-1k^-1", "mcalmol-1k-1"}:
            return 0.001
        if key in {"j/molk", "jmol^-1k^-1", "jmol-1k-1"}:
            return _JOULE_TO_CALORIE
    if metric == "omega1" and key in {"cm^-1", "cm-1"}:
        return 1.0
    if metric in {"A", "B", "C"} and key == "ghz":
        return 1.0
    return None


def _infer_legacy_unit(metric: str, value: float, source_text: str) -> str | None:
    """Infer units for legacy outputs that predate the explicit ``unit`` field."""
    local = _qm9_target_context(metric, source_text)
    context = local or source_text

    if metric in QM9_ENERGY_TARGETS:
        if re.search(r"\bkcal\s*(?:/|\s)\s*mol", local, re.IGNORECASE):
            return "kcal/mol"
        if re.search(r"\bhartree\b|\bE[_ ]?h\b", local, re.IGNORECASE):
            return "hartree"
        if _has_mev(local) or (not local and _has_mev(source_text) and not _has_ev(source_text)):
            # Old prompts sometimes converted before this guard. Values below
            # one are therefore ambiguous and are left canonical rather than
            # risking a second 1000x conversion. Re-extraction supplies units.
            return "meV" if abs(value) >= 1.0 else "eV"
        if _has_ev(local):
            return "eV"
        if re.search(r"energies?[^.\n]{0,80}\bmev\b", source_text, re.IGNORECASE):
            return "meV" if abs(value) >= 1.0 else "eV"
        if re.search(r"energies?[^.\n]{0,80}(?<!m)\bev\b", source_text, re.IGNORECASE):
            return "eV"
        return None

    if metric == "mu":
        if re.search(r"\bm\s*D\b", context, re.IGNORECASE):
            return "mD"
        if re.search(r"\bdebye\b|(?:^|[&|])\s*D\s*(?:[&|]|$)", context, re.IGNORECASE):
            return "D"
    if metric in {"alpha", "R2"}:
        power = "3" if metric == "alpha" else "2"
        if re.search(
            r"\bm\s*(?:\$)?\s*(?:a|bohr)(?:\s*\^?\s*\d)?"
            r"(?:\s*[_\{]?\s*0)?",
            context,
            re.IGNORECASE,
        ):
            return f"m a0^{power}"
        if re.search(
            rf"\bbohr\b[^\n]{{0,20}}(?:\^|\{{){power}|a[_ ]?0[^\n]{{0,20}}{power}",
            context,
            re.IGNORECASE,
        ):
            return f"a0^{power}"
    if metric == "Cv":
        if re.search(r"\bm\s*cal", context, re.IGNORECASE):
            return "mcal/mol K"
        if re.search(r"\bcal(?:orie)?s?\b[^\n]{0,30}\bmol\b", context, re.IGNORECASE):
            return "cal/mol K"
        if re.search(r"\bjoules?\b|(?:^|[&|])\s*J\s*/?\s*mol", context, re.IGNORECASE):
            return "J/mol K"
    if metric == "omega1" and re.search(
        r"\bcm\s*(?:\^?\s*[-−]?\s*1|\{\s*-1\s*\})", context, re.IGNORECASE
    ):
        return "cm^-1"
    return None


def normalize_qm9_result_mapping(
    entry: Mapping[str, Any],
    source_text: str,
    *,
    table_text: str = "",
) -> dict[str, Any] | None:
    """Normalize or reject one extracted QM9 row before it reaches storage.

    The LLM is still responsible for reading the table, but this deterministic
    layer owns canonical units and the hard exclusions that are easy to miss in
    a long paper. Returning ``None`` means the row is not a canonical result.
    """
    dataset = str(entry.get("dataset") or "").strip()
    if not is_qm9_dataset(dataset):
        return dict(entry)

    combined_source = "\n".join(part for part in (source_text, table_text) if part)
    signals = _qm9_source_signals(combined_source, result_table_text=table_text)
    if signals.reject_reason:
        return None

    metric = normalize_qm9_metric(str(entry.get("metric") or ""))
    if metric is None:
        return None

    try:
        value = float(entry.get("value"))
    except (TypeError, ValueError):
        return None
    try:
        std = None if entry.get("std") is None else float(entry.get("std"))
    except (TypeError, ValueError):
        std = None

    repaired = False
    if (
        metric == "mu"
        and value > 5.0
        and re.search(_QM9_TARGET_LINE_PATTERNS["R2"], combined_source, re.IGNORECASE)
    ):
        metric = "R2"
        repaired = True

    explicit_unit = str(entry.get("unit") or "").strip()
    source_unit = explicit_unit or _infer_legacy_unit(metric, value, combined_source)
    canonical_unit = QM9_CANONICAL_UNITS.get(metric)
    scale = _explicit_unit_scale(metric, source_unit) if source_unit else None
    if canonical_unit is None or scale is None:
        return None
    value *= scale
    if std is not None:
        std *= scale

    updates: dict[str, Any] = {
        "dataset": "QM9",
        "metric": metric,
        "value": value,
        "std": std,
        "unit": canonical_unit,
        # Every canonical QM9 target in this path is an error metric.
        "higher_is_better": False,
    }

    # A recurring extraction failure puts the source R² column under `mu`.
    # Raw R² errors are much larger than dipole errors; after unit handling,
    # this repair is conservative and only activates when the source exposes
    # an R² target and the value is clearly outside dipole-error scale.
    note = str(entry.get("protocol_note") or "").strip()
    if repaired:
        note = f"{note} Source-column repair: value matched R², not mu.".strip()
    if explicit_unit:
        if source_unit != canonical_unit:
            note = f"{note} QM9 unit normalization: {source_unit} to {canonical_unit}.".strip()
        elif "qm9 source unit:" not in note.casefold():
            note = f"{note} QM9 source unit: {source_unit}.".strip()
    decision = str(entry.get("protocol_decision") or "").strip().casefold()
    if decision == "nonstandard":
        updates["protocol_decision"] = "nonstandard"
        updates["uses_standard_protocol"] = False
    elif signals.has_canonical_split:
        updates["protocol_decision"] = "standard"
        updates["uses_standard_protocol"] = True
    else:
        updates["protocol_decision"] = "uncertain"
        updates["uses_standard_protocol"] = False
        if "canonical qm9 split evidence" not in note.casefold():
            note = f"{note} QM9 canonical split evidence was not found in the source.".strip()

    if note:
        updates["protocol_note"] = note

    normalized = dict(entry)
    normalized.update(updates)
    return normalized


def apply_qm9_extraction_guard(
    extraction: Any,
    source_text: str,
    *,
    table_text: str = "",
) -> Any:
    """Apply :func:`normalize_qm9_result_mapping` to an ExtractionOutput."""
    kept: list[Any] = []
    dropped = 0
    repaired = 0
    scaled = 0
    for result in extraction.results:
        if not is_qm9_dataset(getattr(result, "dataset", "")):
            kept.append(result)
            continue
        mapping = normalize_qm9_result_mapping(
            result.model_dump(), source_text, table_text=table_text
        )
        if mapping is None:
            dropped += 1
            continue
        if mapping["metric"] != result.metric:
            repaired += 1
        if mapping["value"] != result.value:
            scaled += 1
        kept.append(result.__class__.model_validate(mapping))

    extraction.results = kept
    if dropped or repaired or scaled:
        notes = []
        if scaled:
            notes.append(f"QM9 guard normalized {scaled} value(s) to canonical units.")
        if repaired:
            notes.append(f"QM9 guard repaired {repaired} target-column assignment(s).")
        if dropped:
            notes.append(f"QM9 guard dropped {dropped} non-canonical or non-MAE row(s).")
        extraction.extraction_notes = "\n".join(
            part for part in (extraction.extraction_notes, *notes) if part
        )
    return extraction


def _norm_alias(text: str) -> str:
    text = text.strip().lower()
    text = text.replace("₀", "0").replace("₁", "1").replace("₂", "2")
    text = re.sub(r"[()]", " ", text)
    text = re.sub(r"[_\-/]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _register_alias(alias: str, canonical: str) -> None:
    key = _norm_alias(alias)
    if key:
        _QM9_ALIAS_MAP[key] = canonical


def _build_alias_map() -> None:
    if _QM9_ALIAS_MAP:
        return

    for canonical in QM9_TARGETS:
        _register_alias(canonical, canonical)

    for canonical, label in QM9_METRIC_LABELS.items():
        _register_alias(label, canonical)

    extra_aliases: dict[str, list[str]] = {
        "gap": [
            "homo lumo gap",
            "homo-lumo gap",
            "homo lumo",
            "epsilon gap",
            "ε gap",
            "e gap",
            "mae gap",
            "gap mae",
            "mae (gap)",
            "gap (mae)",
        ],
        "mu": [
            "dipole",
            "dipole moment",
            "mu",
            "mae mu",
            "mae (mu)",
        ],
        "alpha": [
            "polarizability",
            "isotropic polarizability",
            "mae alpha",
            "mae (alpha)",
        ],
        "U0": [
            "u0",
            "u_0",
            "internal energy u0",
            "internal energy at 0k",
            "mae u0",
            "mae (u0)",
        ],
        "U": [
            "internal energy",
            "internal energy u",
            "internal energy at 298",
            "mae u",
            "mae (u)",
        ],
        "H": [
            "enthalpy",
            "mae h",
            "mae (h)",
        ],
        "G": [
            "free energy",
            "gibbs free energy",
            "mae g",
            "mae (g)",
        ],
        "Cv": [
            "heat capacity",
            "heat capacity cv",
            "mae cv",
            "mae (cv)",
        ],
        "HOMO": [
            "homo",
            "highest occupied molecular orbital",
            "mae homo",
            "mae (homo)",
        ],
        "LUMO": [
            "lumo",
            "lowest unoccupied molecular orbital",
            "mae lumo",
            "mae (lumo)",
        ],
        "zpve": [
            "zero point vibrational energy",
            "zero point energy",
            "zpve",
            "mae zpve",
        ],
        "R2": [
            "r2",
            "r squared",
            "electronic spatial extent",
            "mae r2",
        ],
        "omega1": [
            "omega1",
            "omega 1",
            "highest fundamental vibrational frequency",
        ],
    }
    for canonical, aliases in extra_aliases.items():
        for alias in aliases:
            _register_alias(alias, canonical)


def is_qm9_dataset(dataset_name: str) -> bool:
    return dataset_name.strip().lower() == "qm9"


def qm9_extract_metric_constraint(targets: tuple[str, ...] | list[str]) -> str:
    """Build per-chunk QM9 extraction instruction for the LLM."""
    keys = ", ".join(targets)
    return (
        "QM9 MULTI-TARGET: extract per-target test MAE for these properties ONLY: "
        f'{keys}. Use each property key exactly as metric (e.g. metric="gap" for '
        "HOMO-LUMO gap). Emit one results[] row per (model, property). "
        'Do NOT use bare "MAE". Copy the raw numeric table value without converting it, '
        "and set unit to the exact unit printed for that property (for example meV, eV, "
        "kcal/mol, Hartree, D, bohr^3, or cal/mol K). The deterministic QM9 guard owns "
        "all conversion to canonical units. If the source does not state a unit, set unit=null.\n"
        "Only extract supervised property-prediction test MAE on QM9's canonical split "
        "(normally 110k/10k/10k or 80/10/10). Skip error-ratio tables, chemical-accuracy "
        "ratios, generation/conditional-generation evaluations, transfer or linear-probe "
        "evaluations, OOD/attack settings, custom/size-based splits, and auxiliary metrics. "
        "Require protocol_decision=standard and protocol_note naming the exact canonical "
        "split; if the paper does not provide that evidence, emit no canonical rows.\n"
    )


def normalize_qm9_metric(metric_name: str) -> str | None:
    """Map a paper/extraction metric string to a canonical QM9 target key."""
    _build_alias_map()
    raw = metric_name.strip()
    if not raw:
        return None

    paren_match = re.search(r"\(([^)]+)\)", raw)
    if paren_match:
        inner = normalize_qm9_metric(paren_match.group(1))
        if inner:
            return inner

    # Bare canonical keys (case-sensitive for U0, Cv, etc.)
    if raw in QM9_TARGETS:
        return raw
    if raw.upper() in {t.upper() for t in QM9_TARGETS}:
        for target in QM9_TARGETS:
            if target.upper() == raw.upper():
                return target

    normalized = _norm_alias(raw)
    if normalized in _BARE_METRIC_REJECT:
        return None
    if normalized in _QM9_ALIAS_MAP:
        return _QM9_ALIAS_MAP[normalized]

    # Strip leading "mae" prefix: "mae gap" -> gap
    if normalized.startswith("mae "):
        stripped = normalized[4:].strip()
        if stripped in _QM9_ALIAS_MAP:
            return _QM9_ALIAS_MAP[stripped]

    # Try last token after common separators
    for part in re.split(r"[\s,;:]+", normalized):
        if part in _BARE_METRIC_REJECT:
            continue
        if part in _QM9_ALIAS_MAP:
            return _QM9_ALIAS_MAP[part]

    return None


def order_qm9_metrics(
    available: set[str] | list[str],
    *,
    default_metric: str = QM9_DEFAULT_METRIC,
    display_metrics: list[str] | None = None,
) -> list[str]:
    """Return metrics in curated order: default first, then display list, then rest."""
    avail = set(available)
    ordered: list[str] = []
    seen: set[str] = set()

    def add(metric: str) -> None:
        if metric in avail and metric not in seen:
            ordered.append(metric)
            seen.add(metric)

    if default_metric in avail:
        add(default_metric)
    elif default_metric not in avail and avail:
        # Fall back to first curated target present
        for candidate in QM9_TARGETS:
            if candidate in avail:
                add(candidate)
                break

    display_list = display_metrics or list(QM9_TARGETS)
    for metric in display_list:
        add(metric)

    for metric in sorted(avail - seen):
        add(metric)

    return ordered
