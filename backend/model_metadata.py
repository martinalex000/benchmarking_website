"""Shared constants and helpers for model architecture type and parameter metadata."""

from __future__ import annotations

ARCHITECTURE_TYPES: frozenset[str] = frozenset(
    {
        "gnn",
        "graph_transformer",
        "hybrid",
        "llm",
        "svm_kernel",
        "random_forest",
        "decision_tree",
        "boosting",
        "other_traditional",
    }
)

_LEGACY_TYPE_MAP: dict[str, str] = {
    "gcn_variant": "gnn",
    "gat_variant": "gnn",
    "graphtransformer": "graph_transformer",
    "graph_transformer": "graph_transformer",
    "gnn": "gnn",
    "other": "other_traditional",
    "graph_llm": "llm",
    "language_model": "llm",
    "lm": "llm",
    "large_language_model": "llm",
}

ARCHITECTURE_LABELS: dict[str, str] = {
    "gnn": "GNN",
    "graph_transformer": "GT",
    "hybrid": "Hyb",
    "llm": "LLM",
    "svm_kernel": "SVM",
    "random_forest": "RF",
    "decision_tree": "Tree",
    "boosting": "Boost",
    "other_traditional": "Trad",
}

ARCHITECTURE_TITLES: dict[str, str] = {
    "gnn": "Message-passing GNN",
    "graph_transformer": "Graph transformer",
    "hybrid": "Hybrid MPNN + transformer",
    "llm": "LLM applied to graphs",
    "svm_kernel": "SVM / kernel method",
    "random_forest": "Random forest",
    "decision_tree": "Decision tree",
    "boosting": "Boosting ensemble",
    "other_traditional": "Traditional / classical method",
}


def normalize_architecture_type(value: str | None) -> str | None:
    """Return a canonical architecture type or None if invalid/empty."""
    if value is None:
        return None
    key = str(value).strip().lower().replace("-", "_").replace(" ", "_")
    if not key or key == "null":
        return None
    if key in ARCHITECTURE_TYPES:
        return key
    if key in _LEGACY_TYPE_MAP:
        return _LEGACY_TYPE_MAP[key]
    return None


def architecture_label(value: str | None) -> str | None:
    normalized = normalize_architecture_type(value)
    if normalized is None:
        return None
    return ARCHITECTURE_LABELS.get(normalized)


def architecture_title(value: str | None) -> str | None:
    normalized = normalize_architecture_type(value)
    if normalized is None:
        return None
    return ARCHITECTURE_TITLES.get(normalized)


def params_exact_from_millions(params_millions: float | None) -> int | None:
    if params_millions is None:
        return None
    return int(round(float(params_millions) * 1_000_000))
