"""Metadata and dataset-name discovery helpers for LLM extraction."""

from __future__ import annotations

import logging
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import defusedxml.ElementTree as ET
import yaml

from backend.text_cleanup import clean_extracted_text

logger = logging.getLogger(__name__)

_ARXIV_API = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
_ARXIV_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}
_TOP_DATASETS_HINT_LIMIT = 50
_DATASET_RG_MATCH_LIMIT = 80
_DATASET_CONTEXT_WINDOW = 80
_DATASET_BENCHMARK_CONTEXT_MARKERS = (
    "dataset",
    "datasets",
    "benchmark",
    "benchmarks",
    "split",
    "splits",
    "accuracy",
    "acc",
    "f1",
    "auc",
    "roc",
    "mae",
    "rmse",
    "mrr",
    "ap",
    "hits@",
    "results",
    "performance",
    "classification",
    "regression",
    "prediction",
    "table",
)


def _title_looks_corrupted(title: str | None) -> bool:
    """Return True when a stored title looks like a degraded metadata fallback.

    The current checks intentionally catch the most common bad states we saw in
    cached metadata: raw `arXiv:` placeholders, stray LaTeX backslashes, broken
    leading punctuation, and duplicated colon fragments from malformed parsing.
    """
    t = (title or "").strip()
    if not t:
        return True
    return (
        t.startswith("arXiv:") or "\\" in t or t.startswith(": ") or " , " in t or t.count(":") > 1
    )


def _get_top_datasets_hint(limit: int = _TOP_DATASETS_HINT_LIMIT) -> str:
    """Return a formatted list of datasets in the DB ordered by result count.

    Includes datasets with zero results (i.e. seeded but not yet extracted) so
    the discovery LLM can match datasets from newly introduced benchmarks.
    Injected into the discovery prompt so the model uses canonical names.
    Returns an empty string when the DB is unavailable.
    """
    try:
        from sqlalchemy import func

        from backend.db import session_scope
        from backend.models import Dataset, DatasetVariant, Result

        with session_scope() as session:
            rows = (
                session.query(Dataset.name, func.count(Result.id).label("cnt"))
                .join(DatasetVariant, DatasetVariant.dataset_id == Dataset.id)
                .outerjoin(Result, Result.dataset_variant_id == DatasetVariant.id)
                .group_by(Dataset.name)
                .order_by(func.count(Result.id).desc())
                .limit(limit)
                .all()
            )
        if not rows:
            return ""
        lines = []
        for r in rows:
            suffix = f" ({r.cnt} results)" if r.cnt else "  [no results yet — new dataset]"
            lines.append(f"  {r.name}{suffix}")
        return "\n".join(lines)
    except Exception as exc:
        logger.debug("Could not query top datasets from DB: %s", exc)
        return ""


_KNOWN_DATASET_NAMES_CACHE: list[str] | None = None


def clear_known_dataset_names_cache() -> None:
    """Clear the cached dataset names. Call after editing config/seed_data.yaml."""
    global _KNOWN_DATASET_NAMES_CACHE
    _KNOWN_DATASET_NAMES_CACHE = None


def _get_known_dataset_names() -> list[str]:
    """Return canonical dataset names from config/seed_data.yaml."""
    global _KNOWN_DATASET_NAMES_CACHE
    if _KNOWN_DATASET_NAMES_CACHE is not None:
        return _KNOWN_DATASET_NAMES_CACHE

    seed_path = Path(__file__).resolve().parents[1] / "config" / "seed_data.yaml"
    try:
        raw = yaml.safe_load(seed_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        logger.debug("Could not load canonical dataset names from %s: %s", seed_path, exc)
        _KNOWN_DATASET_NAMES_CACHE = []
        return _KNOWN_DATASET_NAMES_CACHE

    names: list[str] = []
    seen: set[str] = set()
    for benchmark in raw.get("benchmarks", []) or []:
        for dataset in benchmark.get("datasets", []) or []:
            name = str(dataset.get("name", "")).strip()
            if not name:
                continue
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            names.append(name)

    _KNOWN_DATASET_NAMES_CACHE = names
    return names


def _get_known_dataset_names_hint(limit: int | None = None) -> str:
    """Return canonical dataset names from seed_data.yaml as a newline list."""
    names = _get_known_dataset_names()
    if limit is not None:
        names = names[:limit]
    if not names:
        return ""
    return "\n".join(f"- {name}" for name in names)


def _ripgrep_dataset_name_hits(
    text: str, source_path: Path | None = None, limit: int = _DATASET_RG_MATCH_LIMIT
) -> list[str]:
    """Return canonical dataset names whose literal strings appear in the text."""
    dataset_names = _get_known_dataset_names()
    if not dataset_names:
        return []

    canonical_by_lower = {name.lower(): name for name in dataset_names}
    target_path = source_path if source_path and source_path.exists() else None

    try:
        with tempfile.TemporaryDirectory(prefix="dataset-rg-") as tmpdir:
            tmp_path = Path(tmpdir)
            patterns_path = tmp_path / "datasets.regex"
            pattern_lines = [
                rf"(?<![A-Za-z0-9-]){re.escape(name)}(?![A-Za-z0-9-])" for name in dataset_names
            ]
            patterns_path.write_text("\n".join(pattern_lines), encoding="utf-8")

            if target_path is None:
                target_path = tmp_path / "input.txt"
                target_path.write_text(text, encoding="utf-8", errors="replace")

            proc = subprocess.run(
                [
                    "rg",
                    "--pcre2",
                    "--no-filename",
                    "--only-matching",
                    "--ignore-case",
                    "--file",
                    str(patterns_path),
                    str(target_path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
    except FileNotFoundError:
        logger.debug("ripgrep not available; skipping dataset-name precheck")
        return []
    except Exception as exc:
        logger.debug("ripgrep dataset precheck failed: %s", exc)
        return []

    if proc.returncode not in (0, 1):
        logger.debug("ripgrep dataset precheck returned %d: %s", proc.returncode, proc.stderr)
        return []

    text_lower = text.lower()

    def _has_benchmark_context(name: str) -> bool:
        pattern = rf"(?<![A-Za-z0-9-]){re.escape(name)}(?![A-Za-z0-9-])"
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            start = max(0, match.start() - _DATASET_CONTEXT_WINDOW)
            end = min(len(text_lower), match.end() + _DATASET_CONTEXT_WINDOW)
            window = text_lower[start:end]
            if any(marker in window for marker in _DATASET_BENCHMARK_CONTEXT_MARKERS):
                return True
        return False

    hits: list[str] = []
    seen_hits: set[str] = set()
    for line in proc.stdout.splitlines():
        canonical = canonical_by_lower.get(line.strip().lower())
        if not canonical or canonical in seen_hits or not _has_benchmark_context(canonical):
            continue
        seen_hits.add(canonical)
        hits.append(canonical)
        if len(hits) >= limit:
            break
    return hits


def _discovery_text_excerpts(text: str, chunk_size: int = 6_000) -> list[str]:
    """Return head/tail excerpts for discovery prompts without dropping appendices."""
    clean = text.strip()
    if not clean:
        return []
    if len(clean) <= chunk_size * 2:
        return [clean]
    return [clean[:chunk_size], clean[-chunk_size:]]


def _noncanonical_dataset_hints(text: str) -> list[str]:
    """Return common non-canonical dataset/task names seen in appendix tables."""
    hints: list[str] = []
    if re.search(r"\bsubgraph counting\b", text, flags=re.IGNORECASE):
        hints.append("subgraph counting")
    if re.search(r"\breddit-bin(?:ary)?\b", text, flags=re.IGNORECASE):
        hints.append("REDDIT-BINARY")
    return hints


def _extract_latex_braced_group(tex: str, open_brace_pos: int) -> str:
    """Return the inner text of a {...} group starting at *open_brace_pos* (the '{')."""
    if open_brace_pos >= len(tex) or tex[open_brace_pos] != "{":
        return ""
    depth = 1
    pos = open_brace_pos + 1
    while pos < len(tex) and depth > 0:
        if tex[pos] == "{":
            depth += 1
        elif tex[pos] == "}":
            depth -= 1
        pos += 1
    return tex[open_brace_pos + 1 : pos - 1]


def _prepare_author_body(body: str) -> str:
    """Drop affiliation/email tails and inline footnotes from an \\author{...} body."""
    body = re.split(r"\\\\", body, maxsplit=1)[0]
    for _ in range(3):
        body = re.sub(r"\\thanks\s*\{[^{}]*\}", "", body)
        body = re.sub(r"\\texttt\s*\{[^{}]*\}", "", body)
        body = re.sub(r"\$[^$]*\$", "", body)
    return body


def _split_author_parts(body: str) -> list[str]:
    """Split an author block into individual name fragments."""
    parts = re.split(r"\\(?:and|And|AND)\b", body)
    if len(parts) == 1:
        parts = re.split(r",\s*(?=[A-Z\\])", body)
    return [part.strip() for part in parts if part.strip()]


def _looks_like_affiliation(text: str) -> bool:
    if "@" in text:
        return True
    return bool(
        re.search(
            r"\b(?:University|Universit[aà]|Research|Institute|Laboratory|Department|College|School)\b",
            text,
            flags=re.IGNORECASE,
        )
    )


def _parse_author_names_from_latex(tex: str) -> list[str]:
    """Extract ordered author names from \\author{...} blocks in LaTeX source."""
    from backend.latex_source import _strip_latex

    authors: list[str] = []
    for match in re.finditer(r"\\author\s*(?:\[[^\]]*\])?\s*\{", tex):
        body = _extract_latex_braced_group(tex, match.end() - 1)
        if not body:
            continue
        for part in _split_author_parts(_prepare_author_body(body)):
            clean = clean_extracted_text(_strip_latex(part).strip())
            if clean and not _looks_like_affiliation(clean):
                authors.append(clean)
    return authors


def _extract_metadata_from_latex_cache(latex_dir: Path) -> dict[str, str | list[str]]:
    """Read title, abstract, and authors from a cached expanded.tex without a full parse.

    Used as a free, offline fallback during abstract screening when the DB has
    only a stub entry and no HTML is available or HTML lacks an abstract.
    Returns a dict with 'title', 'abstract', and/or 'authors' keys (may be partial).
    """
    expanded = latex_dir / "expanded.tex"
    if not expanded.exists() or expanded.stat().st_size < 100:
        return {}
    try:
        from backend.latex_source import _expand_user_macros, _strip_latex

        tex = expanded.read_text(encoding="utf-8", errors="replace")[:40_000]
        tex, _ = _expand_user_macros(tex)

        result: dict[str, str | list[str]] = {}

        # Extract \title{...} — handles optional [short] argument
        m = re.search(r"\\title\s*(?:\[[^\]]*\])?\s*\{", tex)
        if m:
            raw_title = _extract_latex_braced_group(tex, m.end() - 1)
            clean = _strip_latex(raw_title)
            if clean:
                result["title"] = clean

        # Extract \begin{abstract}...\end{abstract}
        m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.DOTALL)
        if m:
            raw_abstract = m.group(1)
            clean = _strip_latex(raw_abstract)
            if clean:
                result["abstract"] = clean

        author_names = _parse_author_names_from_latex(tex)
        if author_names:
            result["authors"] = author_names

        return result
    except Exception as exc:
        logger.debug("LaTeX metadata cache read failed: %s", exc)
        return {}


def fetch_arxiv_metadata(arxiv_id: str) -> dict[str, str]:
    """Fetch title, abstract, and published date from the arXiv Atom API.

    Retries up to 10 times with 10-second intervals on any transient failure
    (network error, rate limit 429, server error).  Returns {} after all
    attempts are exhausted.
    """
    _MAX_ATTEMPTS = 10
    _RETRY_INTERVAL = 10  # seconds between attempts

    url = _ARXIV_API.format(arxiv_id=arxiv_id)
    for attempt in range(_MAX_ATTEMPTS):
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:  # nosec B310
                xml_bytes = resp.read()
            root = ET.fromstring(xml_bytes)
            entry = root.find("atom:entry", _ARXIV_NS)
            if entry is None:
                return {}
            title = (entry.find("atom:title", _ARXIV_NS).text or "").replace("\n", " ").strip()
            abstract = clean_extracted_text(
                (entry.find("atom:summary", _ARXIV_NS).text or "").replace("\n", " ").strip()
            )
            published_elem = entry.find("atom:published", _ARXIV_NS)
            published_date = ""
            if published_elem is not None and published_elem.text:
                published_date = published_elem.text[:10]  # "YYYY-MM-DD"
            authors = [
                (author_elem.find("atom:name", _ARXIV_NS).text or "").strip()
                for author_elem in entry.findall("atom:author", _ARXIV_NS)
            ]
            authors = [name for name in authors if name]
            result = {"title": title, "abstract": abstract, "published_date": published_date}
            comment_elem = entry.find("arxiv:comment", _ARXIV_NS)
            if comment_elem is not None and comment_elem.text:
                result["arxiv_comment"] = comment_elem.text.replace("\n", " ").strip()
            journal_ref_elem = entry.find("arxiv:journal_ref", _ARXIV_NS)
            if journal_ref_elem is not None and journal_ref_elem.text:
                result["journal_ref"] = journal_ref_elem.text.replace("\n", " ").strip()
            if authors:
                result["authors"] = authors
            return result
        except urllib.error.HTTPError as exc:
            if exc.code == 429:
                logger.warning(
                    "arXiv API rate-limited (429) for %s — waiting %ds (attempt %d/%d)",
                    arxiv_id,
                    _RETRY_INTERVAL,
                    attempt + 1,
                    _MAX_ATTEMPTS,
                )
            else:
                logger.warning(
                    "arXiv API HTTP error for %s: %s (attempt %d/%d)",
                    arxiv_id,
                    exc,
                    attempt + 1,
                    _MAX_ATTEMPTS,
                )
        except Exception as exc:
            logger.warning(
                "arXiv API request failed for %s: %s (attempt %d/%d)",
                arxiv_id,
                exc,
                attempt + 1,
                _MAX_ATTEMPTS,
            )
        if attempt < _MAX_ATTEMPTS - 1:
            time.sleep(_RETRY_INTERVAL)
    logger.warning("arXiv API gave up after %d attempts for %s", _MAX_ATTEMPTS, arxiv_id)
    return {}


def fetch_arxiv_authors(arxiv_id: str) -> list[str]:
    """Fetch author names from the arXiv Atom API."""
    metadata = fetch_arxiv_metadata(arxiv_id)
    authors = metadata.get("authors")
    if isinstance(authors, list):
        return [str(name).strip() for name in authors if str(name).strip()]
    return []


_S2_API_URL = (
    "https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}?fields=publicationDate"
)


def fetch_semantic_scholar_published_date(arxiv_id: str) -> str | None:
    """Fetch exact publication date from Semantic Scholar."""
    from backend.semantic_scholar import fetch_paper_metadata

    metadata = fetch_paper_metadata(arxiv_id)
    published_date = metadata.get("published_date")
    if published_date and re.match(r"^\d{4}-\d{2}-\d{2}$", published_date):
        return published_date
    return None


def _headers_to_dict(headers_obj: Any) -> dict[str, str]:
    """Convert a response header container to a lowercase dict."""
    if headers_obj is None:
        return {}

    try:
        items = headers_obj.items()
    except Exception:
        try:
            return {str(k).lower(): str(v) for k, v in dict(headers_obj).items()}
        except Exception:
            return {}

    return {str(k).lower(): str(v) for k, v in items}
