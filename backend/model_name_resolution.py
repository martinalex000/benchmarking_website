"""Shared helpers for resolving and grouping benchmark model names."""

from __future__ import annotations

import re

# Author-role annotations such as "(ours)" — not part of the model name.
ROLE_SUFFIX_RE = re.compile(
    r"\s*\(\s*(?:ours?|base(?:line)?|our\s+model|our\s+method|proposed)\s*\)\s*$",
    re.IGNORECASE,
)

_VIRT_NODE_RE = re.compile(r"\bvirt\.?\s*node\b", re.IGNORECASE)

_OGB_DATASET_FAMILY_RE = re.compile(r"^ogb([gnl])-", re.IGNORECASE)


def normalize_model_name_for_resolution(name: str) -> str:
    """Normalize a model name for canonical lookup and fuzzy matching."""
    clean = ROLE_SUFFIX_RE.sub("", name).strip()
    if not clean:
        return clean
    clean = _VIRT_NODE_RE.sub("Virtual Node", clean)
    clean = re.sub(r"\s+", " ", clean)
    return clean.strip()


def model_family_token(name: str) -> str:
    """Primary architecture token before the first ``+`` modifier."""
    normalized = normalize_model_name_for_resolution(name)
    head = normalized.split("+", 1)[0].strip()
    return re.sub(r"\s+", "", head.lower())


def model_names_fuzzy_compatible(
    name_a: str,
    name_b: str,
    score: int,
    min_score: int,
) -> bool:
    """True when fuzzy score passes and architecture families match."""
    if score < min_score:
        return False
    return model_family_token(name_a) == model_family_token(name_b)


def ogb_dataset_family(name: str) -> str | None:
    """Return OGB middle letter (g/n/l) or None if not an OGB dataset name."""
    match = _OGB_DATASET_FAMILY_RE.match(name.strip().lower())
    if match is None:
        return None
    return match.group(1).lower()


def ogb_dataset_families_compatible(name_a: str, name_b: str) -> bool:
    """Block fuzzy matches across ogbg / ogbn / ogbl families."""
    fam_a = ogb_dataset_family(name_a)
    fam_b = ogb_dataset_family(name_b)
    if fam_a is None or fam_b is None:
        return True
    return fam_a == fam_b
