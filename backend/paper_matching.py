"""Match external paper records to corpus rows by title and authors."""

from __future__ import annotations

import re

from thefuzz import fuzz

from backend.config import normalize_arxiv_id
from backend.models import Paper, author_display_name

_ARXIV_RE = re.compile(r"\b(\d{4}\.\d{4,5})(?:v\d+)?\b")
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def normalize_paper_title(title: str | None) -> str:
    raw = " ".join(str(title or "").split()).strip().lower()
    if not raw:
        return ""
    return _NON_ALNUM_RE.sub(" ", raw).strip()


def author_last_names(authors: list[str] | None) -> set[str]:
    names: set[str] = set()
    for author in authors or []:
        text = " ".join(str(author).split()).strip()
        if not text:
            continue
        parts = text.split()
        last = parts[-1].lower()
        last = re.sub(r"[^a-z'-]", "", last)
        if len(last) >= 2:
            names.add(last)
    return names


def paper_author_last_names(paper: Paper) -> set[str]:
    return author_last_names([author_display_name(author) for author in paper.authors or []])


def author_overlap_score(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    overlap = len(left & right)
    return overlap / min(len(left), len(right))


def titles_match(left: str | None, right: str | None, *, min_score: int = 92) -> bool:
    a = normalize_paper_title(left)
    b = normalize_paper_title(right)
    if not a or not b:
        return False
    if a == b:
        return True
    return fuzz.token_sort_ratio(a, b) >= min_score


def match_paper_by_title_authors(
    papers: list[Paper],
    *,
    title: str,
    authors: list[str] | None,
    min_title_score: int = 92,
    min_author_overlap: float = 0.34,
) -> Paper | None:
    """Return the best matching paper row for an external title/authors pair."""
    candidate_authors = author_last_names(authors)
    best: Paper | None = None
    best_score = 0.0
    for paper in papers:
        if not paper.title:
            continue
        title_score = fuzz.token_sort_ratio(
            normalize_paper_title(title), normalize_paper_title(paper.title)
        )
        if title_score < min_title_score:
            continue
        overlap = author_overlap_score(candidate_authors, paper_author_last_names(paper))
        if candidate_authors and overlap < min_author_overlap:
            continue
        combined = title_score + (30.0 * overlap)
        if combined > best_score:
            best = paper
            best_score = combined
    return best


def extract_arxiv_id_from_text(*values: object) -> str:
    for value in values:
        text = str(value or "")
        match = _ARXIV_RE.search(text)
        if match:
            return normalize_arxiv_id(match.group(1))
    return ""
