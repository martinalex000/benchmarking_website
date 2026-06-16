"""Interpret table captions/headings to guide result normalization.

Papers often explain row suffixes and value encoding in the table caption (e.g.
``* indicates our implementation, while other results are taken from [12]``).
This module detects those conventions and resolves duplicate model variants to a
single canonical name before deduplication.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

# Caption: "* indicates our implementation" / "∗ denotes our re-implementation"
_IMPLEMENTATION_MARKER_CAPTION_RE = re.compile(
    r"(?:^|[^\w])([*†‡§∗])\s*(?:indicates?|denotes?|marks?|means?|represents?|is|are)\s+"
    r"(?:our\s+)?(?:own\s+)?(?:re-?)?implementation",
    re.IGNORECASE,
)
# Caption: "other results are taken from [12]" alongside an implementation marker
_CITED_BASELINE_CAPTION_RE = re.compile(
    r"(?:other\s+)?results?\s+(?:are\s+)?(?:taken|reported|from)\s+from",
    re.IGNORECASE,
)
# Caption: "without * are from prior work"
_UNMARKED_FROM_LITERATURE_RE = re.compile(
    r"(?:without|w/o)\s+([*†‡§∗])\s+(?:are|is)\s+from",
    re.IGNORECASE,
)
# Caption mentions asterisk as a footnote symbol
_ASTERISK_WORD_RE = re.compile(r"\basterisk\b", re.IGNORECASE)
# Values reported as percentages in caption/header
_PERCENT_VALUES_RE = re.compile(
    r"(?:\(\s*%\s*\)|(?:^|[\s,.])in\s+%|(?:^|[\s,.])percent(?:age)?(?:\s+points?)?)",
    re.IGNORECASE,
)

_TABLE_REF_NUMBER_RE = re.compile(r"table\s*(\d+)", re.IGNORECASE)


@dataclass(frozen=True)
class TableCaptionPolicy:
    """How a table encodes model variants and value units."""

    merge_equivalent_model_variants: bool = False
    equivalent_markers: frozenset[str] = frozenset()
    values_are_percent: bool = False
    is_ablation_or_diagnostic: bool = False
    caption_snippet: str = ""
    notes: str = ""


# Caption describes an ablation / component-removal / sensitivity table (not main benchmark)
_ABLATION_OR_DIAGNOSTIC_CAPTION_RE = re.compile(
    r"\bablation(?:s| study| studies| experiment)?\b"
    r"|component\s+remov"
    r"|sensitivity\s+analysis"
    r"|hyper-?parameter\s+(?:sweep|study|search|analysis)"
    r"|(?:^|[\s,.])w/o\s+\w"
    r"|without\s+(?:the\s+)?(?:\w+\s+){0,3}(?:layer|block|module|component|head|encoder|decoder)",
    re.IGNORECASE,
)
def normalize_caption_text(caption: str) -> str:
    """Unify unicode footnote symbols for pattern matching."""
    return (
        caption.replace("∗", "*")
        .replace("＊", "*")
        .replace("†", "†")
        .replace("‡", "‡")
    )


def interpret_table_caption(caption: str) -> TableCaptionPolicy:
    """Derive normalization rules from a table caption or heading."""
    raw = (caption or "").strip()
    if not raw:
        return TableCaptionPolicy()

    text = normalize_caption_text(raw)
    lower = text.lower()
    markers: set[str] = set()
    merge = False
    notes: list[str] = []

    for match in _IMPLEMENTATION_MARKER_CAPTION_RE.finditer(text):
        markers.add(match.group(1).replace("∗", "*"))
        merge = True
        notes.append("footnote marks authors' implementation")

    if _CITED_BASELINE_CAPTION_RE.search(text) and ("*" in text or _ASTERISK_WORD_RE.search(text)):
        merge = True
        markers.add("*")
        notes.append("unmarked rows cite prior work")

    unmarked = _UNMARKED_FROM_LITERATURE_RE.search(text)
    if unmarked:
        merge = True
        markers.add(unmarked.group(1).replace("∗", "*"))
        notes.append("unmarked rows cite prior work")

    if _ASTERISK_WORD_RE.search(text) and _IMPLEMENTATION_MARKER_CAPTION_RE.search(text):
        markers.add("*")

    percent = bool(_PERCENT_VALUES_RE.search(lower))
    ablation = bool(_ABLATION_OR_DIAGNOSTIC_CAPTION_RE.search(lower))
    if ablation:
        notes.append("ablation or diagnostic table")

    snippet = raw[:160] + ("…" if len(raw) > 160 else "")

    return TableCaptionPolicy(
        merge_equivalent_model_variants=merge and bool(markers),
        equivalent_markers=frozenset(markers),
        values_are_percent=percent,
        is_ablation_or_diagnostic=ablation,
        caption_snippet=snippet,
        notes="; ".join(dict.fromkeys(notes)),
    )


def parse_table_ref_number(table_ref: str | None) -> int | None:
    """Return table number from refs like ``Table 2`` or ``tab:results``."""
    if not table_ref:
        return None
    match = _TABLE_REF_NUMBER_RE.search(table_ref)
    if match is None:
        return None
    return int(match.group(1))


def build_table_caption_policy_map(tables: list[Any]) -> dict[int, TableCaptionPolicy]:
    """Map table numbers to caption policies for structured/LaTeX table objects."""
    policies: dict[int, TableCaptionPolicy] = {}
    for table in tables:
        number = getattr(table, "number", None)
        if number is None:
            continue
        caption = getattr(table, "caption", "") or ""
        policies[int(number)] = interpret_table_caption(caption)
    return policies


def combined_merge_policy(policies: dict[int, TableCaptionPolicy]) -> TableCaptionPolicy | None:
    """Merge policies from all tables that request variant collapsing."""
    merging = [p for p in policies.values() if p.merge_equivalent_model_variants]
    if not merging:
        return None
    all_markers: set[str] = set()
    notes: list[str] = []
    percent = False
    for policy in merging:
        all_markers.update(policy.equivalent_markers)
        if policy.notes:
            notes.append(policy.notes)
        percent = percent or policy.values_are_percent
    return TableCaptionPolicy(
        merge_equivalent_model_variants=True,
        equivalent_markers=frozenset(all_markers),
        values_are_percent=percent,
        notes="; ".join(dict.fromkeys(notes)),
    )


def policy_for_table_ref(
    table_ref: str | None,
    policies: dict[int, TableCaptionPolicy],
    default: TableCaptionPolicy | None,
) -> TableCaptionPolicy | None:
    """Pick the caption policy for a result row."""
    number = parse_table_ref_number(table_ref)
    if number is not None and number in policies:
        policy = policies[number]
        if policy.merge_equivalent_model_variants:
            return policy
    return default


def strip_footnote_markers(name: str, markers: frozenset[str]) -> str:
    """Remove trailing footnote marker symbols from a model row label."""
    clean = name.strip()
    if not clean or not markers:
        return clean
    for marker in sorted(markers, key=len, reverse=True):
        if not marker:
            continue
        pattern = re.compile(rf"\s*{re.escape(marker)}+$")
        clean = pattern.sub("", clean).strip()
    return clean


def is_ablation_table_ref(
    table_ref: str | None,
    policies: dict[int, TableCaptionPolicy],
) -> bool:
    """True when the caption for this table marks it as ablation/diagnostic."""
    number = parse_table_ref_number(table_ref)
    if number is None or number not in policies:
        return False
    return policies[number].is_ablation_or_diagnostic


def resolve_model_name_for_policy(name: str, policy: TableCaptionPolicy | None) -> str:
    """Canonical model name when caption says marked/unmarked rows are the same method."""
    if policy is None or not policy.merge_equivalent_model_variants:
        return name.strip()
    return strip_footnote_markers(name, policy.equivalent_markers) or name.strip()
