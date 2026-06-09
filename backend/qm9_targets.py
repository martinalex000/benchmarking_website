"""Canonical QM9 target property names, display labels, and alias normalization."""

from __future__ import annotations

import re

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
        'Do NOT use bare "MAE". Skip generative metrics (COV, FCD, Novelty, etc.).\n'
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
