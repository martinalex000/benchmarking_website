"""Helpers for cleaning text extracted from papers."""

from __future__ import annotations

import re

_EMPTY_DELIMITER_RE = re.compile(r"\(\s*\)|\[\s*\]|\{\s*\}")
_LATEX_ARTIFACT_RE = re.compile(
    r"~|\\(?:xspace|cite|citep|citet|ref|eqref|label|url|href|footnote|text[a-zA-Z]+|[A-Za-z]{2,})"
)


def clean_extracted_text(text: str | None) -> str:
    """Normalize common text artifacts left behind by LaTeX extraction."""
    if not text:
        return ""
    cleaned = str(text).replace("\u00a0", " ").replace("~", " ")
    cleaned = re.sub(r"\\xspace\b", " ", cleaned)
    cleaned = _EMPTY_DELIMITER_RE.sub(" ", cleaned)
    cleaned = re.sub(r"\s+([,;:.!?])", r"\1", cleaned)
    cleaned = re.sub(r"([([{])\s+", r"\1", cleaned)
    cleaned = re.sub(r"\s+([)\]}])", r"\1", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def abstract_has_latex_artifacts(text: str | None) -> bool:
    """Return True when an abstract still looks like partially stripped LaTeX."""
    return bool(text and _LATEX_ARTIFACT_RE.search(text))
