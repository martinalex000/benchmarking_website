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
    "S",
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
    "gap": "HOMO-LUMO gap",
    "mu": "Dipole moment",
    "alpha": "Polarizability",
    "U0": "Internal energy (U₀)",
    "H": "Enthalpy (H)",
    "G": "Free energy (G)",
    "Cv": "Heat capacity (Cv)",
    "S": "Entropy (S)",
    "HOMO": "HOMO",
    "LUMO": "LUMO",
    "zpve": "Zero point vibrational energy",
    "R2": "Electronic spatial extent (R²)",
    "U": "Internal energy (U)",
    "omega1": "Highest vibrational frequency",
    "A": "Rotational constant A",
    "B": "Rotational constant B",
    "C": "Rotational constant C",
    "mu_N": "Nuclear repulsion energy",
    "R2_xyz": "R² (xyz)",
}

QM9_DEFAULT_METRIC = "gap"

# Target groups for chunked LLM extraction (keeps responses under token limits).
QM9_EXTRACT_TARGET_GROUPS: tuple[tuple[str, ...], ...] = (
    ("gap", "mu", "alpha"),
    ("U0", "H", "G", "Cv", "S"),
    ("HOMO", "LUMO", "zpve", "R2", "U", "omega1"),
)

# Normalized alias -> canonical key
_QM9_ALIAS_MAP: dict[str, str] = {}


_BARE_METRIC_REJECT: frozenset[str] = frozenset({"mae", "rmse", "loss", "mse"})

QM9_ENERGY_TARGETS: frozenset[str] = frozenset({"gap", "HOMO", "LUMO", "U0", "U", "H", "G", "zpve"})

_QM9_TARGET_LINE_PATTERNS: dict[str, str] = {
    "gap": r"(?:homo\s*[- ]?\s*lumo|delta[_ ]?\\?epsilon|\\?Delta[_ ]?\\?epsilon|gap)",
    "mu": r"(?:\\?mu\b|dipole)",
    "alpha": r"(?:\\?alpha\b|polarizability)",
    "U0": r"(?:\\?u[_ ]?0\b|u\{?0\}?|internal\s+energy)",
    "U": r"(?:^|[^a-z])u(?:$|[^a-z0-9])",
    "H": r"(?:^|[^a-z])h(?:$|[^a-z0-9])|enthalpy",
    "G": r"(?:^|[^a-z])g(?:$|[^a-z0-9])|free\s+energy|gibbs",
    "Cv": r"(?:c[_ ]?v|heat\s+capacity)",
    "S": r"(?:^|[^a-z])s(?:$|[^a-z0-9])|entropy",
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


def _qm9_metric_scale(metric: str, value: float, source_text: str) -> float:
    """Return the multiplier converting a source value to the site's units."""
    local = _qm9_target_context(metric, source_text)
    context = local or source_text

    if metric in QM9_ENERGY_TARGETS:
        if _has_mev(local) or (not local and _has_mev(source_text) and not _has_ev(source_text)):
            return 0.001
        if _has_ev(local):
            return 1.0
        if re.search(r"energies?[^.\n]{0,80}\bmev\b", source_text, re.IGNORECASE):
            return 0.001
        if re.search(r"energies?[^.\n]{0,80}(?<!m)\bev\b", source_text, re.IGNORECASE):
            return 1.0
        # Most QM9 energy tables omit units in the row labels but use the
        # conventional meV scale. Explicit eV evidence above protects papers
        # such as structural-transformer evaluations that genuinely report eV.
        return 0.001 if abs(value) > 1.0 else 1.0

    if metric == "mu" and re.search(r"\bm\s*D\b", context, re.IGNORECASE):
        return 0.001
    if metric in {"alpha", "R2"} and re.search(
        r"\bm\s*(?:\$)?\s*(?:a|bohr)(?:\s*\^?\s*\d)?"
        r"(?:\s*[_\{]?\s*0)?",
        context,
        re.IGNORECASE,
    ):
        return 0.001
    if metric == "Cv" and re.search(r"\bm\s*cal", context, re.IGNORECASE):
        return 0.001
    return 1.0


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

    scale = _qm9_metric_scale(metric, value, combined_source)
    value *= scale
    if std is not None:
        std *= scale

    updates: dict[str, Any] = {
        "dataset": "QM9",
        "metric": metric,
        "value": value,
        "std": std,
        # Every canonical QM9 target in this path is an error metric.
        "higher_is_better": False,
    }

    # A recurring extraction failure puts the source R² column under `mu`.
    # Raw R² errors are much larger than dipole errors; after unit handling,
    # this repair is conservative and only activates when the source exposes
    # an R² target and the value is clearly outside dipole-error scale.
    if (
        metric == "mu"
        and value > 5.0
        and re.search(_QM9_TARGET_LINE_PATTERNS["R2"], combined_source, re.IGNORECASE)
    ):
        updates["metric"] = "R2"
        updates["protocol_note"] = (
            f"{entry.get('protocol_note') or ''} Source-column repair: value matched R², not mu."
        ).strip()

    note = str(entry.get("protocol_note") or "").strip()
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
        "S": [
            "entropy",
            "mae s",
            "mae (s)",
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
        'Do NOT use bare "MAE". All values must be converted to canonical units before output: '
        "energies/gap/HOMO/LUMO/ZPVE/U0/U/H/G in eV, mu in D, alpha in a0^3, "
        "R2 in a0^2, and Cv in cal/mol K. Divide meV, mD, m*a0^3, m*a0^2, and "
        "mcal/mol K values by 1000. Never copy a raw table number when its header has a "
        "milli-unit.\n"
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
