"""Source-aware guards for the multi-target QM7b benchmark."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any


def is_qm7b_dataset(dataset: str) -> bool:
    """Return whether *dataset* explicitly names QM7b rather than QM7."""
    key = re.sub(r"[\s-]+", "", str(dataset or "")).casefold()
    return key in {"qm7b", "qm7bdataset"}


def _source_signals(source_text: str, *, table_text: str = "") -> tuple[str | None, bool]:
    """Return ``(reject_reason, has_random_split_evidence)`` for QM7b source."""
    text = source_text.casefold()
    context = (table_text or source_text).casefold()
    if not re.search(r"\bqm\s*7[-\s]*b\b", text):
        return "source names QM7, not the distinct QM7b benchmark", False
    if table_text and re.search(r"\bqm\s*7\b(?![-\s]*b\b)", context) and not re.search(
        r"\bqm\s*7[-\s]*b\b", context
    ):
        return "selected result table is for QM7 rather than QM7b", False
    if re.search(
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

    QM7b contains 14 heterogeneous targets, so this path deliberately does not
    invent unit conversions or accept a generic row from a per-target table.
    Target-specific rows must retain their source metric; an aggregate row is
    accepted only when the selected source explicitly describes a mean/average.
    """
    if not is_qm7b_dataset(str(entry.get("dataset") or "")):
        return dict(entry)

    combined_source = "\n".join(part for part in (source_text, table_text) if part)
    reject_reason, has_random_split = _source_signals(
        combined_source, table_text=table_text
    )
    if reject_reason:
        return None

    metric = str(entry.get("metric") or "").strip()
    metric_key = metric.casefold()
    if not metric:
        return None
    if str(entry.get("protocol_decision") or "").strip().casefold() == "nonstandard":
        return None
    if metric_key in {"mse", "rmse", "root mean squared error"}:
        return None

    context = (table_text or combined_source).casefold()
    if metric_key == "mae" and re.search(
        r"\bqm\s*7\s*b\b.{0,160}\b(?:task|target)s?\b", context, re.DOTALL
    ) and not re.search(r"\b(?:mean|average|overall)\b", context):
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
            "dataset": "QM7b",
            "metric": metric,
            "value": value,
            "std": std,
            "higher_is_better": False,
        }
    )
    decision = str(entry.get("protocol_decision") or "").strip().casefold()
    if decision == "nonstandard":
        normalized["uses_standard_protocol"] = False
    else:
        normalized["protocol_decision"] = "standard"
        normalized["uses_standard_protocol"] = True
        note = str(entry.get("protocol_note") or "").strip()
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
