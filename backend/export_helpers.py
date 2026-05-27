"""Shared formatting and ranking helpers for Hugo export paths."""

from __future__ import annotations

import re
from typing import Any

_MODEL_SUFFIX_RE = re.compile(
    r"\s*\(\s*(?:ours?|base(?:line)?|proposed|retuned|re-?eval|none|l\s*=\s*\d+)\s*\)\s*$",
    re.IGNORECASE,
)
_MODEL_FROM_REF_RE = re.compile(r"\s+from\s+ref\..*$", re.IGNORECASE)
_LATEX_CITE_RE = re.compile(r"~?\\cite\{[^}]*\}")
_TITLE_LINEBREAK_RE = re.compile(r"\\\\+")
_TITLE_LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+\*?(?:\{[^}]*\})?")
_MODEL_SUBSCRIPT_DOLLAR_RE = re.compile(r"\$_\{([^{}]+)\}\$")
_MODEL_SUPERSCRIPT_DOLLAR_RE = re.compile(r"\$\^\{([^{}]+)\}\$")
_MODEL_TEXTSUBSCRIPT_RE = re.compile(r"\\textsubscript\{([^{}]+)\}")
_MODEL_TEXTSUPERSCRIPT_RE = re.compile(r"\\textsuperscript\{([^{}]+)\}")
_HTML_TAG_RE = re.compile(r"<[^>]+>")


def sanitize_title(title: str | None) -> str:
    if not title:
        return ""
    cleaned = _TITLE_LINEBREAK_RE.sub(" - ", str(title))
    cleaned = _TITLE_LATEX_CMD_RE.sub("", cleaned)
    cleaned = cleaned.replace("\\", " ")
    return re.sub(r"\s+", " ", cleaned).strip()


def truncate_words(text: str | None, max_words: int) -> str:
    cleaned = sanitize_title(text)
    if not cleaned:
        return ""
    words = cleaned.split()
    if len(words) <= max_words:
        return cleaned
    return " ".join(words[:max_words]) + "..."


def sanitize_model(
    model_name: str | None,
    *,
    remap: dict[str, str] | None = None,
) -> str:
    if not model_name:
        return ""
    cleaned = str(model_name)
    cleaned = _LATEX_CITE_RE.sub("", cleaned)
    cleaned = _MODEL_FROM_REF_RE.sub("", cleaned)
    cleaned = _MODEL_SUFFIX_RE.sub("", cleaned)
    cleaned = _MODEL_SUBSCRIPT_DOLLAR_RE.sub(r"<sub>\1</sub>", cleaned)
    cleaned = _MODEL_SUPERSCRIPT_DOLLAR_RE.sub(r"<sup>\1</sup>", cleaned)
    cleaned = _MODEL_TEXTSUBSCRIPT_RE.sub(r"<sub>\1</sub>", cleaned)
    cleaned = _MODEL_TEXTSUPERSCRIPT_RE.sub(r"<sup>\1</sup>", cleaned)
    cleaned = cleaned.replace("$", "")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    replacements = remap or {}
    return replacements.get(cleaned.lower(), cleaned)


def plain_model(model_name: str | None) -> str:
    if not model_name:
        return ""
    return re.sub(r"\s+", " ", _HTML_TAG_RE.sub("", str(model_name))).strip()


def has_paper_value_gap(
    paper_value: float | None,
    paper_std: float | None,
    true_value: float | None,
    true_std: float | None,
) -> bool:
    if paper_value is None or true_value is None:
        return False
    delta = abs(paper_value - true_value)
    if paper_std is None and true_std is None:
        return delta > 1e-12
    if paper_std is not None and delta <= float(paper_std):
        return False
    if true_std is not None and delta <= float(true_std):
        return False
    return delta > 1e-12


def rank_for_value(
    global_rows: list[dict[str, Any]],
    model_key: str,
    candidate_value: float | None,
    higher_is_better: bool,
) -> int | None:
    if not model_key or candidate_value is None:
        return None

    ranked_values: list[tuple[str, float]] = []
    seen = False
    for row in global_rows:
        row_key = row.get("model_key", "")
        row_value = row.get("value")
        if row_value is None:
            continue
        if row_key == model_key:
            ranked_values.append((model_key, float(candidate_value)))
            seen = True
        else:
            ranked_values.append((row_key, float(row_value)))

    if not seen:
        ranked_values.append((model_key, float(candidate_value)))

    ranked_values.sort(key=lambda item: -item[1] if higher_is_better else item[1])
    for rank, (row_key, _) in enumerate(ranked_values, start=1):
        if row_key == model_key:
            return rank
    return None
