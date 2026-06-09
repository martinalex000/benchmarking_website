"""Helpers for preparing pre-appendix prose and detecting SOTA claim language."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from backend.latex_source import LatexPaper, _find_appendix_start, _strip_latex

if TYPE_CHECKING:
    pass

_PROSE_ENV_RE = re.compile(
    r"\\begin\{(figure\*?|table\*?|longtable|tabular|wrapfigure|subfigure)\}" r".*?" r"\\end\{\1\}",
    re.DOTALL,
)

_APPENDIX_HEADING_RE = re.compile(
    r"(?im)"
    r"(?:^|\n)\s*(?:#+\s*)?(?:\\)?appendix\b"
    r"|(?:^|\n)\s*#+\s*[A-Z]\.\s+\S"
    r"|(?:^|\n)\s*Appendix\s+[A-Z]\b"
)

_SOTA_MARKERS = (
    "state-of-the-art",
    "state of the art",
    "sota",
    "new best",
    "new state",
    "outperforms all",
    "outperforms existing",
    "sets a new record",
    "achieves the best",
    "achieve the best",
    "best performance",
    "best results",
    "best-known",
    "best known",
    "surpasses all",
    "superior to all",
    "leading performance",
)

_SOTA_CLAIM_CHUNK_SIZE = 30_000
_SOTA_CLAIM_CHUNK_OVERLAP = 2_000


def _strip_prose_environments(text: str) -> str:
    """Remove LaTeX table/figure environments from prose."""
    return _PROSE_ENV_RE.sub(" ", text)


def _find_plain_text_appendix_start(text: str) -> int:
    """Return character index where appendix content begins in plain text."""
    match = _APPENDIX_HEADING_RE.search(text)
    return match.start() if match else len(text)


def _latex_pre_appendix_tex(latex_paper: LatexPaper) -> str:
    appendix_pos = _find_appendix_start(latex_paper.main_tex)
    parts: list[str] = []
    for section in latex_paper.sections:
        if section.in_appendix:
            continue
        parts.append(f"=== {section.title} ===\n{section.content}")
    if parts:
        combined = "\n\n".join(parts)
        return combined[:appendix_pos] if appendix_pos < len(combined) else combined
    return latex_paper.main_tex[:appendix_pos]


def main_body_prose_text(
    *,
    paper_text: str,
    latex_paper: LatexPaper | None = None,
) -> str:
    """Return pre-appendix prose with tables/figures stripped."""
    if latex_paper is not None:
        raw = _latex_pre_appendix_tex(latex_paper)
        cleaned = _strip_prose_environments(raw)
        return _strip_latex(cleaned).strip()

    appendix_pos = _find_plain_text_appendix_start(paper_text)
    scoped = paper_text[:appendix_pos]
    cleaned = _strip_prose_environments(scoped)
    return cleaned.strip()


def text_has_sota_markers(text: str) -> bool:
    lower = text.lower()
    return any(marker in lower for marker in _SOTA_MARKERS)


def chunk_prose_for_extraction(text: str) -> list[str]:
    """Split long scoped prose into overlapping chunks for LLM extraction."""
    if len(text) <= _SOTA_CLAIM_CHUNK_SIZE:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + _SOTA_CLAIM_CHUNK_SIZE)
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = max(0, end - _SOTA_CLAIM_CHUNK_OVERLAP)
    return chunks


def merge_claim_dicts(claims: list[dict]) -> list[dict]:
    """Deduplicate extracted claim dicts by verbatim raw_sentence."""
    seen: set[str] = set()
    merged: list[dict] = []
    for claim in claims:
        if not isinstance(claim, dict):
            continue
        raw = str(claim.get("raw_sentence") or "").strip()
        if not raw or raw in seen:
            continue
        seen.add(raw)
        merged.append(claim)
    return merged
