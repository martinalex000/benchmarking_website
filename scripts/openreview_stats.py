#!/usr/bin/env python3
"""List and compare papers from an OpenReview venue.

The command is intentionally read-only with respect to the repository data. It
can inspect the local paper database and query Semantic Scholar, but it does
not update the database, enqueue papers, or download PDFs. API responses are
cached under the untracked ``.cache/openreview_stats/`` directory; use
``--refresh-cache`` to fetch fresh responses.

Usage::

    uv run python scripts/openreview_stats.py --venue-id NeurIPS.cc/2025/Conference
    uv run python scripts/openreview_stats.py --venue-id ICML.cc/2022/Conference \
        --compare-local --filter --summary-only
    uv run python scripts/openreview_stats.py --list
    uv run python scripts/openreview_stats.py --venue-id NeurIPS.cc/2025/Conference \
        --compare-local --compare-s2 --s2-venue NeurIPS --s2-year 2025 \
        --filter --summary-only

OpenReview credentials are read by :class:`backend.openreview_client.OpenReviewClient`.
Obtain a token with ``uv run python scripts/openreview_login.py``.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import os
import sqlite3
import sys
import tempfile
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests
from rich.console import Console
from thefuzz import fuzz
from tqdm import tqdm

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

_DEFAULT_VENUE_ID = "NeurIPS.cc/2024/Conference"
_DEFAULT_S2_VENUE = "NeurIPS"
_DEFAULT_S2_YEAR = 2024
_DEFAULT_CACHE_DIR = _PROJECT_ROOT / ".cache" / "openreview_stats"
_CACHE_VERSION = 1
_S2_CACHE_VERSION = 2
console = Console()

from backend.arxiv_metadata_analysis import ScreeningConfig  # noqa: E402
from backend.config import cfg, normalize_arxiv_id  # noqa: E402
from backend.openreview_client import (  # noqa: E402
    OpenReviewClient,
    OpenReviewError,
    OpenReviewPaper,
)
from backend.paper_matching import (  # noqa: E402
    author_last_names,
    author_overlap_score,
    normalize_paper_title,
    paper_author_last_names,
)
from backend.semantic_scholar import (  # noqa: E402
    SemanticScholarAPIError,
    iter_papers_bulk,
)


@dataclass(frozen=True)
class VenueStats:
    """Counts derived from one OpenReview venue response."""

    total: int
    with_arxiv_id: int
    without_arxiv_id: int
    with_pdf_url: int
    without_pdf_url: int
    unique_arxiv_ids: int
    duplicate_arxiv_ids: int
    duplicate_arxiv_submissions: int


@dataclass(frozen=True)
class LocalPaperRecord:
    """Read-only subset of a local paper row used for comparison."""

    arxiv_id: str
    title: str
    authors: list[object]
    abstract: str
    result_count: int = 0


@dataclass(frozen=True)
class IndexedLocalPaper:
    """Precomputed matching fields for one local paper."""

    paper: LocalPaperRecord
    normalized_title: str
    author_last_names: frozenset[str]


@dataclass(frozen=True)
class LocalPaperIndex:
    """In-memory indexes used during one comparison run."""

    papers: tuple[IndexedLocalPaper, ...]
    by_arxiv_id: dict[str, LocalPaperRecord]
    by_title: dict[str, tuple[IndexedLocalPaper, ...]]
    by_token: dict[str, tuple[IndexedLocalPaper, ...]]


@dataclass(frozen=True)
class LocalMatch:
    status: str
    paper: LocalPaperRecord | None = None


@dataclass(frozen=True)
class LocalComparison:
    local_database_papers: int
    local_database_with_results: int
    local_database_without_results: int
    considered: int
    matches: dict[str, LocalMatch]
    direct_matches: int
    title_author_matches: int
    arxiv_not_local: int
    unmatched: int
    ambiguous: int
    matched_with_results: int
    matched_without_results: int


@dataclass(frozen=True)
class S2Candidate:
    arxiv_id: str
    title: str
    abstract: str = ""


@dataclass(frozen=True)
class IndexedS2Candidate:
    candidate: S2Candidate
    normalized_title: str


@dataclass(frozen=True)
class S2CandidateIndex:
    candidates: tuple[IndexedS2Candidate, ...]
    by_arxiv_id: dict[str, S2Candidate]
    by_title: dict[str, tuple[IndexedS2Candidate, ...]]
    by_token: dict[str, tuple[IndexedS2Candidate, ...]]


@dataclass(frozen=True)
class S2Match:
    status: str
    candidate: S2Candidate | None = None


@dataclass(frozen=True)
class S2Comparison:
    available: bool
    matches: dict[str, S2Match] | None = None
    considered: int = 0
    candidate_count: int = 0
    candidates_with_arxiv: int = 0
    direct_matches: int = 0
    title_matches: int = 0
    unmatched: int = 0
    ambiguous: int = 0
    error: str = ""
    arxiv_matches: int = 0


@dataclass(frozen=True)
class FilterStats:
    specific_matches: int
    graph_matches: int
    filtered_out: int
    unknown_abstract: int
    unknown_category: int
    eligible: int


@dataclass(frozen=True)
class CategoryCounts:
    specific: int
    unspecific: int

    @property
    def total(self) -> int:
        return self.specific + self.unspecific


@dataclass(frozen=True)
class S2FilterResult:
    raw_candidate_count: int
    stats: FilterStats
    matched_candidates: list[S2Candidate]
    applied: bool


@dataclass(frozen=True)
class FilterResult:
    stats: FilterStats
    matched_submissions: list[OpenReviewPaper]
    categories: dict[str, str]


@dataclass(frozen=True)
class PdfPipelineStats:
    considered: int
    openreview_arxiv: int
    local_arxiv: int
    semantic_scholar_arxiv: int
    needs_pdf_pipeline: int

    @property
    def arxiv_covered(self) -> int:
        return self.openreview_arxiv + self.local_arxiv + self.semantic_scholar_arxiv


@dataclass(frozen=True)
class SourceDecision:
    """Read-only decision describing which source a submission would use."""

    note_id: str
    title: str
    action: str
    source_kind: str
    venue_id: str = ""
    arxiv_id: str = ""
    pdf_url: str = ""
    evidence: str = ""


@dataclass(frozen=True)
class SourcePlanStats:
    considered: int
    already_processed: int
    planned_arxiv: int
    planned_openreview_pdf: int
    review_required: int
    unavailable: int


@dataclass(frozen=True)
class ConferenceCategorySummary:
    s2_matched: CategoryCounts
    s2_with_arxiv: CategoryCounts
    processed: CategoryCounts
    needs_pdf_pipeline: CategoryCounts
    arxiv_still_to_process: CategoryCounts


@dataclass(frozen=True)
class PendingArxivPaper:
    arxiv_id: str
    title: str
    categories: str = ""
    filter_match_type: str = "unspecific"


@dataclass(frozen=True)
class KaggleCategorySummary:
    papers: list[PendingArxivPaper]
    category_counts: dict[str, int]
    missing_metadata: int
    category_counts_by_match_type: dict[str, dict[str, int]] = field(default_factory=dict)


class LocalDatabaseError(RuntimeError):
    """Raised when the local database cannot be inspected read-only."""


_TITLE_STOPWORDS = frozenset(
    {"a", "an", "and", "as", "at", "by", "for", "from", "in", "of", "on", "the", "to", "via"}
)


def _cache_path(cache_dir: Path, source: str, query: object) -> Path:
    query_json = json.dumps(query, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(query_json.encode("utf-8")).hexdigest()[:16]
    return cache_dir / f"{source}-{digest}.json"


def _read_cache(
    path: Path, *, source: str, query: object, version: int = _CACHE_VERSION
) -> object | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if (
            not isinstance(payload, dict)
            or payload.get("version") != version
            or payload.get("source") != source
            or payload.get("query") != query
        ):
            raise ValueError("unsupported cache format")
        return payload["data"]
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        _status(f"Cache: ignoring invalid {path.name} ({exc})")
        return None


def _write_cache(
    path: Path,
    *,
    source: str,
    query: object,
    data: object,
    version: int = _CACHE_VERSION,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": version,
        "source": source,
        "query": query,
        "fetched_at": datetime.now(UTC).isoformat(),
        "data": data,
    }
    temporary_path: str | None = None
    try:
        fd, temporary_path = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
        temporary_path = None
    except OSError as exc:
        _status(f"Cache: could not write {path.name} ({exc})")
    finally:
        if temporary_path:
            with contextlib.suppress(FileNotFoundError):
                os.unlink(temporary_path)


def load_or_fetch_openreview(
    venue_id: str,
    *,
    cache_dir: Path,
    use_cache: bool,
    refresh_cache: bool,
) -> list[OpenReviewPaper]:
    """Load OpenReview submissions from cache or fetch and cache them."""
    cache_path = _cache_path(cache_dir, "openreview", venue_id)
    if use_cache and not refresh_cache:
        cached = _read_cache(cache_path, source="openreview", query=venue_id)
        if isinstance(cached, list):
            try:
                submissions = [OpenReviewPaper(**row) for row in cached if isinstance(row, dict)]
            except (TypeError, ValueError):
                submissions = []
            if len(submissions) == len(cached):
                _status("Cache: using cached OpenReview submissions")
                return submissions
            _status(f"Cache: ignoring incomplete {cache_path.name}")

    _status("OpenReview: querying API")
    client = OpenReviewClient.from_config()
    submissions = client.fetch_venue_submissions(venue_id)
    if use_cache:
        _write_cache(
            cache_path,
            source="openreview",
            query=venue_id,
            data=[asdict(submission) for submission in submissions],
        )
        _status("Cache: saved OpenReview submissions")
    return submissions


def load_or_fetch_s2(
    venue: str,
    year: int,
    *,
    cache_dir: Path,
    use_cache: bool,
    refresh_cache: bool,
) -> tuple[list[S2Candidate], str]:
    """Load Semantic Scholar candidates from cache or fetch and cache them."""
    query = {"venue": venue, "year": year}
    cache_path = _cache_path(cache_dir, "semantic-scholar", query)
    if use_cache and not refresh_cache:
        cached = _read_cache(
            cache_path,
            source="semantic-scholar",
            query=query,
            version=_S2_CACHE_VERSION,
        )
        if isinstance(cached, list):
            try:
                candidates = [S2Candidate(**row) for row in cached if isinstance(row, dict)]
            except (TypeError, ValueError):
                candidates = []
            if len(candidates) == len(cached):
                _status("Cache: using cached Semantic Scholar candidates")
                return candidates, ""
            _status(f"Cache: ignoring incomplete {cache_path.name}")

    candidates, error = fetch_s2_candidates(venue, year)
    if use_cache and not error:
        _write_cache(
            cache_path,
            source="semantic-scholar",
            query=query,
            data=[asdict(candidate) for candidate in candidates],
            version=_S2_CACHE_VERSION,
        )
        _status("Cache: saved Semantic Scholar candidates")
    return candidates, error


def _status(message: str) -> None:
    """Write a phase update without disrupting an active progress bar."""
    tqdm.write(message)


def _normalize_optional_arxiv_id(value: object) -> str:
    """Normalize an optional arXiv ID without rejecting missing metadata."""
    if not str(value or "").strip():
        return ""
    try:
        return normalize_arxiv_id(value)
    except ValueError:
        return ""


def summarize_submissions(submissions: list[OpenReviewPaper]) -> VenueStats:
    """Return basic metadata coverage and duplicate statistics."""
    arxiv_ids = [paper.arxiv_id for paper in submissions if paper.arxiv_id]
    id_counts = Counter(arxiv_ids)
    duplicate_ids = {arxiv_id for arxiv_id, count in id_counts.items() if count > 1}

    return VenueStats(
        total=len(submissions),
        with_arxiv_id=len(arxiv_ids),
        without_arxiv_id=len(submissions) - len(arxiv_ids),
        with_pdf_url=sum(bool(paper.pdf_url) for paper in submissions),
        without_pdf_url=sum(not bool(paper.pdf_url) for paper in submissions),
        unique_arxiv_ids=len(id_counts),
        duplicate_arxiv_ids=len(duplicate_ids),
        duplicate_arxiv_submissions=sum(count - 1 for count in id_counts.values() if count > 1),
    )


def load_local_papers(db_path: Path) -> list[LocalPaperRecord]:
    """Load local paper metadata through a SQLite read-only connection."""
    if not db_path.exists():
        raise LocalDatabaseError(f"database does not exist: {db_path}")

    uri = f"file:{db_path.resolve()}?mode=ro"
    try:
        connection = sqlite3.connect(uri, uri=True)
        connection.row_factory = sqlite3.Row
        try:
            rows = connection.execute(
                "SELECT p.arxiv_id, p.title, p.authors, p.abstract, "
                "COUNT(DISTINCT r.id) AS result_count "
                "FROM papers AS p LEFT JOIN results AS r ON r.paper_id = p.id "
                "WHERE p.arxiv_id IS NOT NULL "
                "GROUP BY p.id, p.arxiv_id, p.title, p.authors, p.abstract"
            ).fetchall()
        finally:
            connection.close()
    except sqlite3.Error as exc:
        raise LocalDatabaseError(f"could not read database {db_path}: {exc}") from exc

    papers: list[LocalPaperRecord] = []
    for row in rows:
        authors = _parse_authors(row["authors"])
        papers.append(
            LocalPaperRecord(
                arxiv_id=_normalize_optional_arxiv_id(row["arxiv_id"]),
                title=str(row["title"] or "").strip(),
                authors=authors,
                abstract=str(row["abstract"] or "").strip(),
                result_count=int(row["result_count"] or 0),
            )
        )
    return papers


def _parse_authors(raw: object) -> list[object]:
    if not raw:
        return []
    try:
        parsed = json.loads(str(raw))
    except (TypeError, ValueError):
        return [str(raw)]
    return parsed if isinstance(parsed, list) else []


def build_local_index(papers: list[LocalPaperRecord]) -> LocalPaperIndex:
    """Build all local matching indexes in memory; nothing is persisted."""
    indexed: list[IndexedLocalPaper] = []
    by_arxiv_id: dict[str, LocalPaperRecord] = {}
    titles: dict[str, list[IndexedLocalPaper]] = {}
    tokens: dict[str, list[IndexedLocalPaper]] = {}

    for paper in papers:
        normalized_title = normalize_paper_title(paper.title)
        indexed_paper = IndexedLocalPaper(
            paper=paper,
            normalized_title=normalized_title,
            author_last_names=frozenset(paper_author_last_names(paper)),
        )
        indexed.append(indexed_paper)
        if paper.arxiv_id:
            by_arxiv_id[paper.arxiv_id] = paper
        if normalized_title:
            titles.setdefault(normalized_title, []).append(indexed_paper)
            for token in _title_tokens(normalized_title):
                tokens.setdefault(token, []).append(indexed_paper)

    return LocalPaperIndex(
        papers=tuple(indexed),
        by_arxiv_id=by_arxiv_id,
        by_title={title: tuple(matches) for title, matches in titles.items()},
        by_token={token: tuple(matches) for token, matches in tokens.items()},
    )


def _title_tokens(normalized_title: str) -> frozenset[str]:
    return frozenset(
        token
        for token in normalized_title.split()
        if len(token) >= 3 and token not in _TITLE_STOPWORDS
    )


def build_s2_index(candidates: list[S2Candidate]) -> S2CandidateIndex:
    """Build in-memory S2 title indexes; nothing is persisted."""
    indexed: list[IndexedS2Candidate] = []
    by_arxiv_id: dict[str, S2Candidate] = {}
    titles: dict[str, list[IndexedS2Candidate]] = {}
    tokens: dict[str, list[IndexedS2Candidate]] = {}

    for candidate in candidates:
        normalized_title = normalize_paper_title(candidate.title)
        indexed_candidate = IndexedS2Candidate(candidate, normalized_title)
        indexed.append(indexed_candidate)
        if candidate.arxiv_id:
            by_arxiv_id[candidate.arxiv_id] = candidate
        if normalized_title:
            titles.setdefault(normalized_title, []).append(indexed_candidate)
            for token in _title_tokens(normalized_title):
                tokens.setdefault(token, []).append(indexed_candidate)

    return S2CandidateIndex(
        candidates=tuple(indexed),
        by_arxiv_id=by_arxiv_id,
        by_title={title: tuple(matches) for title, matches in titles.items()},
        by_token={token: tuple(matches) for token, matches in tokens.items()},
    )


def _authors_match(candidate_authors: set[str], paper: IndexedLocalPaper) -> bool:
    if not candidate_authors:
        return True
    return author_overlap_score(candidate_authors, paper.author_last_names) >= 0.34


def _title_author_candidates(
    index: LocalPaperIndex, submission: OpenReviewPaper
) -> list[LocalPaperRecord]:
    normalized_title = normalize_paper_title(submission.title)
    candidate_authors = author_last_names(submission.authors)
    exact_candidates = [
        indexed_paper.paper
        for indexed_paper in index.by_title.get(normalized_title, ())
        if _authors_match(candidate_authors, indexed_paper)
    ]
    if exact_candidates:
        return exact_candidates

    candidates: list[LocalPaperRecord] = []
    title_tokens = _title_tokens(normalized_title)
    token_buckets = [
        index.by_token[token] for token in sorted(title_tokens) if token in index.by_token
    ]
    if not token_buckets:
        return []

    for indexed_paper in min(token_buckets, key=len):
        if fuzz.token_sort_ratio(normalized_title, indexed_paper.normalized_title) < 92:
            continue
        if _authors_match(candidate_authors, indexed_paper):
            candidates.append(indexed_paper.paper)
    return candidates


def compare_local(
    submissions: list[OpenReviewPaper], papers: list[LocalPaperRecord] | LocalPaperIndex
) -> LocalComparison:
    """Match OpenReview submissions against local papers."""
    index = papers if isinstance(papers, LocalPaperIndex) else build_local_index(papers)
    matches: dict[str, LocalMatch] = {}
    direct_matches = title_author_matches = arxiv_not_local = unmatched = ambiguous = 0

    submission_iter = (
        tqdm(submissions, desc="Matching local papers", unit="paper")
        if len(submissions) >= 1_000
        else submissions
    )
    for submission in submission_iter:
        key = submission.note_id
        arxiv_id = _normalize_optional_arxiv_id(submission.arxiv_id)
        if arxiv_id:
            local = index.by_arxiv_id.get(arxiv_id)
            if local is not None:
                matches[key] = LocalMatch("direct", local)
                direct_matches += 1
            else:
                matches[key] = LocalMatch("arxiv-not-local")
                arxiv_not_local += 1
            continue

        candidates = _title_author_candidates(index, submission)
        if len(candidates) > 1:
            matches[key] = LocalMatch("ambiguous")
            ambiguous += 1
            continue
        if candidates:
            matches[key] = LocalMatch("title-author", candidates[0])
            title_author_matches += 1
            continue
        matches[key] = LocalMatch("unmatched")
        unmatched += 1

    return LocalComparison(
        local_database_papers=len(index.papers),
        local_database_with_results=sum(
            1 for indexed_paper in index.papers if indexed_paper.paper.result_count > 0
        ),
        local_database_without_results=sum(
            1 for indexed_paper in index.papers if indexed_paper.paper.result_count == 0
        ),
        considered=len(submissions),
        matches=matches,
        direct_matches=direct_matches,
        title_author_matches=title_author_matches,
        arxiv_not_local=arxiv_not_local,
        unmatched=unmatched,
        ambiguous=ambiguous,
        matched_with_results=sum(
            1
            for match in matches.values()
            if match.paper is not None and match.paper.result_count > 0
        ),
        matched_without_results=sum(
            1
            for match in matches.values()
            if match.paper is not None and match.paper.result_count == 0
        ),
    )


def _s2_arxiv_id(record: dict[str, Any]) -> str:
    external_ids = record.get("externalIds")
    if not isinstance(external_ids, dict):
        return ""
    for key, value in external_ids.items():
        if str(key).casefold() == "arxiv":
            return _normalize_optional_arxiv_id(value)
    return ""


def fetch_s2_candidates(venue: str, year: int) -> tuple[list[S2Candidate], str]:
    """Fetch S2 venue candidates without writing or caching response data."""
    candidates: list[S2Candidate] = []
    seen_ids: set[str] = set()
    try:
        pages = iter_papers_bulk(venue, year)
        progress = tqdm(pages, desc="Fetching Semantic Scholar", unit="page")
        for page in progress:
            for record in page.papers:
                paper_id = str(record.get("paperId") or "")
                if paper_id and paper_id in seen_ids:
                    continue
                if paper_id:
                    seen_ids.add(paper_id)
                candidates.append(
                    S2Candidate(
                        arxiv_id=_s2_arxiv_id(record),
                        title=str(record.get("title") or "").strip(),
                        abstract=str(record.get("abstract") or "").strip(),
                    )
                )
    except (SemanticScholarAPIError, requests.RequestException, ValueError) as exc:
        return candidates, str(exc)
    return candidates, ""


def compare_s2(
    submissions: list[OpenReviewPaper],
    candidates: list[S2Candidate] | S2CandidateIndex,
    error: str = "",
) -> S2Comparison:
    """Compare OpenReview records against an S2 venue candidate set."""
    if error:
        candidate_count = (
            len(candidates) if isinstance(candidates, list) else len(candidates.candidates)
        )
        return S2Comparison(
            available=False,
            matches={},
            considered=len(submissions),
            candidate_count=candidate_count,
            error=error,
        )

    index = candidates if isinstance(candidates, S2CandidateIndex) else build_s2_index(candidates)
    direct_matches = title_matches = unmatched = ambiguous = 0
    arxiv_matches = 0
    matches: dict[str, S2Match] = {}
    for submission in submissions:
        arxiv_id = _normalize_optional_arxiv_id(submission.arxiv_id)
        if arxiv_id and arxiv_id in index.by_arxiv_id:
            direct_matches += 1
            arxiv_matches += 1
            candidate = index.by_arxiv_id[arxiv_id]
            matches[submission.note_id] = S2Match("direct", candidate)
            continue

        title_candidates = _s2_title_candidates(index, submission.title)
        if len(title_candidates) > 1:
            ambiguous += 1
            matches[submission.note_id] = S2Match("ambiguous")
        elif title_candidates:
            title_matches += 1
            candidate = title_candidates[0]
            if candidate.arxiv_id:
                arxiv_matches += 1
            matches[submission.note_id] = S2Match("title", candidate)
        else:
            unmatched += 1
            matches[submission.note_id] = S2Match("unmatched")

    return S2Comparison(
        available=True,
        matches=matches,
        considered=len(submissions),
        candidate_count=len(index.candidates),
        candidates_with_arxiv=len(index.by_arxiv_id),
        direct_matches=direct_matches,
        title_matches=title_matches,
        unmatched=unmatched,
        ambiguous=ambiguous,
        arxiv_matches=arxiv_matches,
    )


def _s2_title_candidates(index: S2CandidateIndex, title: str) -> list[S2Candidate]:
    """Find S2 title candidates using exact and token-blocked fuzzy matching."""
    normalized_title = normalize_paper_title(title)
    exact_candidates = index.by_title.get(normalized_title, ())
    if exact_candidates:
        return [indexed.candidate for indexed in exact_candidates]

    title_tokens = _title_tokens(normalized_title)
    token_buckets = [
        index.by_token[token] for token in sorted(title_tokens) if token in index.by_token
    ]
    if not token_buckets:
        return []

    # Use the rarest shared token as the fuzzy candidate block. This avoids
    # comparing every OpenReview title with every S2 record.
    candidates = min(token_buckets, key=len)
    return [
        indexed.candidate
        for indexed in candidates
        if fuzz.token_sort_ratio(normalized_title, indexed.normalized_title) >= 92
    ]


def run_fast_filter(
    submissions: list[OpenReviewPaper],
    *,
    screening_config: ScreeningConfig,
) -> FilterResult:
    """Apply fast filters and return only submissions that matched a filter."""
    matcher = screening_config.matcher()
    specific_matches = graph_matches = filtered_out = unknown_abstract = 0
    unknown_category = 0
    matched_submissions: list[OpenReviewPaper] = []
    categories: dict[str, str] = {}

    for submission in submissions:
        abstract = submission.abstract
        if not abstract:
            unknown_abstract += 1
            continue

        # OpenReview/S2 records do not carry arXiv category fields. Keep this
        # visible instead of silently treating a venue name as a category match.
        unknown_category += 1
        tier = matcher.match_tier(submission.title, abstract)
        if tier is None:
            filtered_out += 1
        elif tier[0] == "specific":
            specific_matches += 1
            matched_submissions.append(submission)
            categories[submission.note_id] = "specific"
        else:
            graph_matches += 1
            matched_submissions.append(submission)
            categories[submission.note_id] = "unspecific"

    eligible = 0
    return FilterResult(
        stats=FilterStats(
            specific_matches=specific_matches,
            graph_matches=graph_matches,
            filtered_out=filtered_out,
            unknown_abstract=unknown_abstract,
            unknown_category=unknown_category,
            eligible=eligible,
        ),
        matched_submissions=matched_submissions,
        categories=categories,
    )


def apply_fast_filter(
    submissions: list[OpenReviewPaper], *, screening_config: ScreeningConfig
) -> FilterStats:
    """Return fast-filter statistics without performing any matching."""
    return run_fast_filter(submissions, screening_config=screening_config).stats


def filter_s2_candidates(
    candidates: list[S2Candidate], *, screening_config: ScreeningConfig
) -> S2FilterResult:
    """Apply the title/abstract filter to S2 candidates before matching."""
    missing_abstracts = sum(not candidate.abstract for candidate in candidates)
    if missing_abstracts:
        return S2FilterResult(
            raw_candidate_count=len(candidates),
            stats=FilterStats(
                specific_matches=0,
                graph_matches=0,
                filtered_out=0,
                unknown_abstract=missing_abstracts,
                unknown_category=0,
                eligible=0,
            ),
            matched_candidates=list(candidates),
            applied=False,
        )

    matcher = screening_config.matcher()
    specific_matches = graph_matches = filtered_out = 0
    matched_candidates: list[S2Candidate] = []
    for candidate in candidates:
        tier = matcher.match_tier(candidate.title, candidate.abstract)
        if tier is None:
            filtered_out += 1
        elif tier[0] == "specific":
            specific_matches += 1
            matched_candidates.append(candidate)
        else:
            graph_matches += 1
            matched_candidates.append(candidate)

    return S2FilterResult(
        raw_candidate_count=len(candidates),
        stats=FilterStats(
            specific_matches=specific_matches,
            graph_matches=graph_matches,
            filtered_out=filtered_out,
            unknown_abstract=0,
            unknown_category=0,
            eligible=0,
        ),
        matched_candidates=matched_candidates,
        applied=True,
    )


def summarize_pdf_pipeline_need(
    submissions: list[OpenReviewPaper],
    *,
    local_comparison: LocalComparison | None,
    s2_comparison: S2Comparison | None,
) -> PdfPipelineStats:
    """Count filtered papers lacking an arXiv source in every available source."""
    openreview_arxiv = local_arxiv = semantic_scholar_arxiv = needs_pdf_pipeline = 0
    s2_matches = s2_comparison.matches if s2_comparison else {}

    for submission in submissions:
        if _normalize_optional_arxiv_id(submission.arxiv_id):
            openreview_arxiv += 1
            continue
        local_match = local_comparison.matches.get(submission.note_id) if local_comparison else None
        if local_match and local_match.paper and local_match.paper.arxiv_id:
            local_arxiv += 1
            continue
        s2_match = s2_matches.get(submission.note_id) if s2_matches else None
        if s2_match and s2_match.candidate and s2_match.candidate.arxiv_id:
            semantic_scholar_arxiv += 1
            continue
        needs_pdf_pipeline += 1

    return PdfPipelineStats(
        considered=len(submissions),
        openreview_arxiv=openreview_arxiv,
        local_arxiv=local_arxiv,
        semantic_scholar_arxiv=semantic_scholar_arxiv,
        needs_pdf_pipeline=needs_pdf_pipeline,
    )


def resolve_submission_sources(
    submissions: list[OpenReviewPaper],
    *,
    local_comparison: LocalComparison | None,
    s2_comparison: S2Comparison | None,
) -> list[SourceDecision]:
    """Choose an arXiv-first source without downloading or changing local state."""
    local_matches = local_comparison.matches if local_comparison else {}
    s2_matches = s2_comparison.matches if s2_comparison and s2_comparison.available else {}
    decisions: list[SourceDecision] = []

    for submission in submissions:
        local_match = local_matches.get(submission.note_id)
        if local_match and local_match.paper and local_match.paper.result_count > 0:
            decisions.append(
                SourceDecision(
                    note_id=submission.note_id,
                    title=submission.title,
                    action="skip-processed",
                    source_kind="local",
                    venue_id=submission.venueid or submission.venue,
                    arxiv_id=local_match.paper.arxiv_id,
                    evidence=f"local-{local_match.status}-with-results",
                )
            )
            continue

        openreview_arxiv = _normalize_optional_arxiv_id(submission.arxiv_id)
        if openreview_arxiv:
            decisions.append(
                SourceDecision(
                    note_id=submission.note_id,
                    title=submission.title,
                    action="queue-arxiv",
                    source_kind="arxiv",
                    venue_id=submission.venueid or submission.venue,
                    arxiv_id=openreview_arxiv,
                    evidence="openreview-arxiv-id",
                )
            )
            continue

        if local_match and local_match.paper and local_match.paper.arxiv_id:
            decisions.append(
                SourceDecision(
                    note_id=submission.note_id,
                    title=submission.title,
                    action="queue-arxiv",
                    source_kind="arxiv",
                    venue_id=submission.venueid or submission.venue,
                    arxiv_id=local_match.paper.arxiv_id,
                    evidence=f"local-{local_match.status}",
                )
            )
            continue

        s2_match = s2_matches.get(submission.note_id)
        if s2_match and s2_match.candidate and s2_match.candidate.arxiv_id:
            decisions.append(
                SourceDecision(
                    note_id=submission.note_id,
                    title=submission.title,
                    action="queue-arxiv",
                    source_kind="arxiv",
                    venue_id=submission.venueid or submission.venue,
                    arxiv_id=s2_match.candidate.arxiv_id,
                    evidence=f"semantic-scholar-{s2_match.status}",
                )
            )
            continue

        ambiguity_sources: list[str] = []
        if local_match and local_match.status == "ambiguous":
            ambiguity_sources.append("local")
        if s2_match and s2_match.status == "ambiguous":
            ambiguity_sources.append("semantic-scholar")
        if ambiguity_sources:
            decisions.append(
                SourceDecision(
                    note_id=submission.note_id,
                    title=submission.title,
                    action="review",
                    source_kind="none",
                    venue_id=submission.venueid or submission.venue,
                    pdf_url=submission.pdf_url,
                    evidence="ambiguous-" + "-and-".join(ambiguity_sources),
                )
            )
            continue

        if submission.pdf_url:
            decisions.append(
                SourceDecision(
                    note_id=submission.note_id,
                    title=submission.title,
                    action="queue-pdf",
                    source_kind="openreview-pdf",
                    venue_id=submission.venueid or submission.venue,
                    pdf_url=submission.pdf_url,
                    evidence="no-arxiv-source-found",
                )
            )
            continue

        decisions.append(
            SourceDecision(
                note_id=submission.note_id,
                title=submission.title,
                action="unavailable",
                source_kind="none",
                venue_id=submission.venueid or submission.venue,
                evidence="no-arxiv-or-pdf-source",
            )
        )

    return decisions


def summarize_source_plan(decisions: list[SourceDecision]) -> SourcePlanStats:
    """Summarize read-only source decisions as planned actions."""
    actions = Counter(decision.action for decision in decisions)
    return SourcePlanStats(
        considered=len(decisions),
        already_processed=actions["skip-processed"],
        planned_arxiv=actions["queue-arxiv"],
        planned_openreview_pdf=actions["queue-pdf"],
        review_required=actions["review"],
        unavailable=actions["unavailable"],
    )


def summarize_conference_categories(
    submissions: list[OpenReviewPaper],
    *,
    categories: dict[str, str],
    local_comparison: LocalComparison | None,
    s2_comparison: S2Comparison | None,
) -> ConferenceCategorySummary:
    """Summarize every downstream count using the same filter categories."""
    category_map = categories or {submission.note_id: "unspecific" for submission in submissions}

    def counts(note_ids: set[str]) -> CategoryCounts:
        return CategoryCounts(
            specific=sum(category_map.get(note_id) == "specific" for note_id in note_ids),
            unspecific=sum(category_map.get(note_id) == "unspecific" for note_id in note_ids),
        )

    s2_matches = s2_comparison.matches if s2_comparison and s2_comparison.available else {}
    s2_matched_ids = {
        note_id for note_id, match in s2_matches.items() if match.status in {"direct", "title"}
    }
    s2_arxiv_ids = {
        note_id
        for note_id in s2_matched_ids
        if s2_matches[note_id].candidate and s2_matches[note_id].candidate.arxiv_id
    }
    processed_ids = {
        note_id
        for note_id, match in (local_comparison.matches if local_comparison else {}).items()
        if match.paper is not None
    }

    covered_ids: set[str] = set()
    for submission in submissions:
        if _normalize_optional_arxiv_id(submission.arxiv_id):
            covered_ids.add(submission.note_id)
            continue
        local_match = local_comparison.matches.get(submission.note_id) if local_comparison else None
        if local_match and local_match.paper and local_match.paper.arxiv_id:
            covered_ids.add(submission.note_id)
            continue
        s2_match = s2_matches.get(submission.note_id)
        if s2_match and s2_match.candidate and s2_match.candidate.arxiv_id:
            covered_ids.add(submission.note_id)

    all_ids = {submission.note_id for submission in submissions}
    return ConferenceCategorySummary(
        s2_matched=counts(s2_matched_ids),
        s2_with_arxiv=counts(s2_arxiv_ids),
        processed=counts(processed_ids),
        needs_pdf_pipeline=counts(all_ids - covered_ids),
        arxiv_still_to_process=counts(covered_ids - processed_ids),
    )


def collect_unprocessed_arxiv_papers(
    submissions: list[OpenReviewPaper],
    *,
    filter_categories: dict[str, str] | None = None,
    local_comparison: LocalComparison | None,
    s2_comparison: S2Comparison | None,
) -> list[PendingArxivPaper]:
    """Return unique arXiv links known for filtered papers but absent locally."""
    filter_categories = filter_categories or {}
    local_matches = local_comparison.matches if local_comparison else {}
    s2_matches = s2_comparison.matches if s2_comparison and s2_comparison.available else {}
    pending: dict[str, PendingArxivPaper] = {}

    for submission in submissions:
        local_match = local_matches.get(submission.note_id)
        if local_match and local_match.paper is not None:
            continue

        arxiv_id = _normalize_optional_arxiv_id(submission.arxiv_id)
        s2_match = s2_matches.get(submission.note_id)
        if not arxiv_id and s2_match and s2_match.candidate:
            arxiv_id = s2_match.candidate.arxiv_id
        if arxiv_id:
            pending_paper = PendingArxivPaper(
                arxiv_id=arxiv_id,
                title=submission.title,
                filter_match_type=filter_categories.get(submission.note_id, "unspecific"),
            )
            existing = pending.get(arxiv_id)
            if existing is None or pending_paper.filter_match_type == "specific":
                pending[arxiv_id] = pending_paper

    return list(pending.values())


def lookup_kaggle_categories(
    papers: list[PendingArxivPaper], snapshot_path: Path
) -> KaggleCategorySummary:
    """Look up pending arXiv records in the downloaded Kaggle snapshot."""
    if not snapshot_path.is_file():
        raise FileNotFoundError(f"Kaggle arXiv snapshot not found: {snapshot_path}")

    pending_by_id = {paper.arxiv_id: paper for paper in papers}
    found: dict[str, PendingArxivPaper] = {}
    remaining = set(pending_by_id)
    file_size = snapshot_path.stat().st_size
    with (
        snapshot_path.open("rb") as handle,
        tqdm(
            total=file_size,
            desc="Looking up Kaggle categories",
            unit="B",
            unit_scale=True,
        ) as progress,
    ):
        for raw_line in handle:
            progress.update(len(raw_line))
            if not remaining:
                break
            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            arxiv_id = _normalize_optional_arxiv_id(record.get("id"))
            if arxiv_id not in remaining:
                continue
            categories = " ".join(str(record.get("categories") or "").split())
            found[arxiv_id] = PendingArxivPaper(
                arxiv_id=arxiv_id,
                title=str(record.get("title") or pending_by_id[arxiv_id].title).strip(),
                categories=categories,
                filter_match_type=pending_by_id[arxiv_id].filter_match_type,
            )
            remaining.remove(arxiv_id)

    category_counts: Counter[str] = Counter()
    category_counts_by_match_type: dict[str, Counter[str]] = {}
    for paper in found.values():
        categories = set(paper.categories.split())
        if "cs.LG" in categories:
            category = "cs.LG"
        elif "stat.ML" in categories:
            category = "stat.ML"
        elif categories:
            category = "other"
        else:
            category = "uncategorized"
        category_counts[category] += 1
        category_counts_by_match_type.setdefault(paper.filter_match_type, Counter())[category] += 1

    ordered_papers = [found.get(paper.arxiv_id, paper) for paper in papers]
    return KaggleCategorySummary(
        papers=ordered_papers,
        category_counts=dict(category_counts),
        category_counts_by_match_type={
            match_type: dict(counts) for match_type, counts in category_counts_by_match_type.items()
        },
        missing_metadata=len(remaining),
    )


def _display_submissions(submissions: list[OpenReviewPaper]) -> None:
    """Print one compact, human-readable row per submission."""
    for index, paper in enumerate(submissions, start=1):
        arxiv_id = paper.arxiv_id or "no arXiv"
        authors = ", ".join(paper.authors) or "no authors"
        pdf_url = paper.pdf_url or "no PDF URL"
        print(f"{index:>4}. [{arxiv_id}] {paper.title}")
        print(f"       authors: {authors}")
        print(f"       note: {paper.note_id or 'unknown'} | pdf: {pdf_url}")


def _print_summary(
    venue_stats: VenueStats,
    *,
    venue_id: str,
    filter_stats: FilterStats | None,
    local_comparison: LocalComparison | None,
    s2_comparison: S2Comparison | None,
    s2_filter_result: S2FilterResult | None,
    category_summary: ConferenceCategorySummary,
    kaggle_summary: KaggleCategorySummary | None,
    show_unprocessed: int,
    pdf_stats: PdfPipelineStats,
    source_decisions: list[SourceDecision],
    source_plan: SourcePlanStats,
    show_source_decisions: int,
) -> None:
    """Print one globally aligned specific/unspecific/total table."""
    console.print(f"\nSummary: {venue_id}")
    console.print(
        f"  OpenReview (authoritative): {venue_stats.total:,} submissions; "
        f"{venue_stats.with_arxiv_id:,} arXiv links"
    )
    if venue_stats.duplicate_arxiv_ids:
        console.print(
            f"  [yellow]duplicate arXiv IDs: {venue_stats.duplicate_arxiv_ids:,}[/yellow]"
        )
    if venue_stats.duplicate_arxiv_submissions:
        console.print(
            f"  [yellow]duplicate submissions: {venue_stats.duplicate_arxiv_submissions:,}[/yellow]"
        )

    console.print("  Conference-paper counts         specific  unspecific     total")

    def print_counts(label: str, values: CategoryCounts) -> None:
        console.print(
            f"  {label:<30}{values.specific:>8,}  {values.unspecific:>9,}  {values.total:>8,}"
        )

    if filter_stats is None:
        print_counts("OpenReview considered (filter off)", CategoryCounts(0, pdf_stats.considered))
    else:
        print_counts(
            "OpenReview filter hits",
            CategoryCounts(filter_stats.specific_matches, filter_stats.graph_matches),
        )

    if s2_comparison is not None and s2_comparison.available:
        if s2_filter_result is None:
            console.print(f"  S2 candidate pool: {s2_comparison.candidate_count:,} (unfiltered)")
        elif s2_filter_result.applied:
            console.print(
                f"  S2 candidate pool: {s2_comparison.candidate_count:,} "
                f"of {s2_filter_result.raw_candidate_count:,} after abstract filter"
            )
        else:
            console.print(
                f"  S2 candidate pool: {s2_comparison.candidate_count:,} "
                "(abstract filter unavailable)"
            )
        print_counts("Matched in S2", category_summary.s2_matched)
        print_counts("S2 matches with arXiv", category_summary.s2_with_arxiv)
    elif s2_comparison is None:
        console.print("  Matched in S2: unavailable or disabled")
    else:
        console.print(f"  Matched in S2: unavailable ({s2_comparison.error})")

    if local_comparison is None:
        console.print("  Processed in local DB: unavailable or disabled")
    else:
        print_counts("Processed in local DB", category_summary.processed)
        console.print(
            f"           results/no results: {local_comparison.matched_with_results:,}/"
            f"{local_comparison.matched_without_results:,}"
        )

    if pdf_stats.needs_pdf_pipeline:
        print_counts("Need PDF pipeline", category_summary.needs_pdf_pipeline)
    if category_summary.arxiv_still_to_process.total:
        print_counts("arXiv still to process", category_summary.arxiv_still_to_process)
    console.print(
        "  Source plan (dry run): "
        f"processed={source_plan.already_processed:,}; "
        f"arXiv={source_plan.planned_arxiv:,}; "
        f"OpenReview PDF={source_plan.planned_openreview_pdf:,}; "
        f"review={source_plan.review_required:,}; "
        f"unavailable={source_plan.unavailable:,}"
    )
    if show_source_decisions:
        console.print(f"  Source decisions (showing up to {show_source_decisions}; no downloads):")
        for decision in source_decisions[:show_source_decisions]:
            identifier = decision.arxiv_id or decision.pdf_url or "no source"
            console.print(
                f"    {decision.action:<14} {decision.note_id}: {decision.title} "
                f"[{identifier}; {decision.evidence}]",
                markup=False,
            )
    if kaggle_summary is not None:
        category_by_match = kaggle_summary.category_counts_by_match_type
        match_types = ["specific", "unspecific"]
        match_types.extend(sorted(set(category_by_match) - set(match_types)))
        if category_by_match:
            console.print("  Kaggle categories (pending arXiv by filter match type)")
            match_header = "  Category".ljust(26) + "".join(
                f"{match_type:>12}" for match_type in match_types
            )
            console.print(match_header + f"{'total':>10}")
            category_names = sorted(
                {category for counts in category_by_match.values() for category in counts}
            )
            for category in category_names:
                total = kaggle_summary.category_counts.get(category, 0)
                values = "".join(
                    f"{category_by_match[match_type].get(category, 0):>12,}"
                    for match_type in match_types
                )
                console.print(f"  {category:<24}{values}{total:>10,}")
        else:
            console.print("  Kaggle categories: none")
        if kaggle_summary.missing_metadata:
            console.print(f"  Kaggle metadata missing: {kaggle_summary.missing_metadata:,}")
        if show_unprocessed:
            console.print(f"  Unprocessed arXiv papers (showing {show_unprocessed}):")
            for paper in kaggle_summary.papers[:show_unprocessed]:
                categories = paper.categories or "Kaggle metadata unavailable"
                console.print(f"    {paper.arxiv_id}: {paper.title} [{categories}]")


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="List and compare OpenReview submissions without writing local state"
    )
    parser.add_argument(
        "--venue-id",
        default=_DEFAULT_VENUE_ID,
        help=(
            "Exact OpenReview venue group ID, e.g. "
            "NeurIPS.cc/2025/Conference or ICML.cc/2022/Conference "
            f"(default: {_DEFAULT_VENUE_ID})"
        ),
    )
    parser.add_argument(
        "--compare-local",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Compare submissions with local papers through a read-only database connection",
    )
    parser.add_argument(
        "--db-path",
        type=Path,
        default=cfg.db_path,
        help="Local SQLite database path (default: data/benchmarks.db)",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=_DEFAULT_CACHE_DIR,
        help="Untracked API cache directory (default: .cache/openreview_stats)",
    )
    parser.add_argument(
        "--cache",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Reuse and write API response caches (enabled by default)",
    )
    parser.add_argument(
        "--refresh-cache",
        action="store_true",
        help="Ignore existing API caches and fetch fresh responses",
    )
    parser.add_argument(
        "--compare-s2",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Compare with Semantic Scholar's venue/year bulk result (enabled by default)",
    )
    parser.add_argument(
        "--s2-venue",
        default=_DEFAULT_S2_VENUE,
        help=f"Semantic Scholar venue name (default: {_DEFAULT_S2_VENUE})",
    )
    parser.add_argument(
        "--s2-year",
        type=int,
        default=_DEFAULT_S2_YEAR,
        help=f"Semantic Scholar publication year (default: {_DEFAULT_S2_YEAR})",
    )
    parser.add_argument(
        "--filter",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Apply the existing fast title/abstract keyword filter",
    )
    parser.add_argument(
        "--screening-config",
        type=Path,
        default=cfg.config_dir / "arxiv_screening.yaml",
        help="Fast-filter configuration path",
    )
    parser.add_argument(
        "--kaggle-snapshot",
        type=Path,
        default=_PROJECT_ROOT / "papers" / "arxiv-metadata" / "arxiv-metadata-oai-snapshot.json",
        help="Downloaded Kaggle arXiv metadata snapshot used for pending-paper categories",
    )
    parser.add_argument(
        "--show-unprocessed",
        nargs="?",
        type=_positive_int,
        const=10,
        default=0,
        metavar="N",
        help="Show up to N titles among pending arXiv papers (default: 10 when enabled)",
    )
    parser.add_argument(
        "--show-source-decisions",
        nargs="?",
        type=_positive_int,
        const=20,
        default=0,
        metavar="N",
        help="Show up to N read-only source decisions (default: 20 when enabled)",
    )
    parser.add_argument(
        "--summary-only",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Print only statistics (default; use --no-summary-only to list papers)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List every paper before printing statistics",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.list:
        args.summary_only = False

    _status(f"OpenReview: fetching submissions for {args.venue_id}")
    try:
        submissions = load_or_fetch_openreview(
            args.venue_id,
            cache_dir=args.cache_dir,
            use_cache=args.cache,
            refresh_cache=args.refresh_cache,
        )
    except (OpenReviewError, requests.RequestException) as exc:
        print(f"OpenReview request failed: {exc}", file=sys.stderr)
        return 1

    _status("OpenReview: submissions loaded")
    if not args.summary_only:
        print(f"Venue: {args.venue_id}")
        _status("OpenReview: listing submissions")
        _display_submissions(submissions)
    venue_stats = summarize_submissions(submissions)

    matching_submissions = submissions
    filter_stats: FilterStats | None = None
    filter_categories: dict[str, str] = {}
    if args.filter:
        _status(f"Filter: loading configuration from {args.screening_config}")
        try:
            screening_config = ScreeningConfig.load(args.screening_config)
        except (OSError, ValueError) as exc:
            print(f"Filter configuration failed: {exc}", file=sys.stderr)
            return 1
        _status("Filter: applying title/abstract keyword tiers before matching")
        filter_result = run_fast_filter(submissions, screening_config=screening_config)
        matching_submissions = filter_result.matched_submissions
        filter_stats = filter_result.stats
        filter_categories = filter_result.categories
        _status("Filter: complete; matched submissions ready")

    local_comparison: LocalComparison | None = None
    local_index: LocalPaperIndex | None = None
    if args.compare_local:
        _status(f"Local DB: loading papers read-only from {args.db_path}")
        try:
            local_papers = load_local_papers(args.db_path)
        except LocalDatabaseError as exc:
            print(f"\nLocal database unavailable: {exc}", file=sys.stderr)
        else:
            _status("Local DB: loaded papers; building in-memory indexes")
            local_index = build_local_index(local_papers)
            _status("Local DB: indexes ready; matching submissions")
            local_comparison = compare_local(matching_submissions, local_index)
            _status("Local DB: matching complete")

    s2_comparison: S2Comparison | None = None
    s2_filter_result: S2FilterResult | None = None
    if args.compare_s2:
        _status(f"Semantic Scholar: fetching {args.s2_venue} {args.s2_year} bulk candidates")
        candidates, error = load_or_fetch_s2(
            args.s2_venue,
            args.s2_year,
            cache_dir=args.cache_dir,
            use_cache=args.cache,
            refresh_cache=args.refresh_cache,
        )
        _status("Semantic Scholar: candidates loaded")
        if error:
            _status("Semantic Scholar: skipping index build because the fetch failed")
            s2_comparison = compare_s2(matching_submissions, candidates, error)
        else:
            if args.filter:
                _status("Semantic Scholar: filtering candidates by title and abstract")
                s2_filter_result = filter_s2_candidates(
                    candidates,
                    screening_config=screening_config,
                )
                if s2_filter_result.applied:
                    candidates = s2_filter_result.matched_candidates
                    _status("Semantic Scholar: filter complete; candidates ready")
                else:
                    _status(
                        "Semantic Scholar: abstracts unavailable; keeping candidates unfiltered"
                    )
            _status("Semantic Scholar: building in-memory title index")
            s2_index = build_s2_index(candidates)
            _status("Semantic Scholar: title index ready; matching submissions")
            s2_comparison = compare_s2(matching_submissions, s2_index)
        _status("Semantic Scholar: matching complete")

    category_summary = summarize_conference_categories(
        matching_submissions,
        categories=filter_categories,
        local_comparison=local_comparison,
        s2_comparison=s2_comparison,
    )
    source_decisions = resolve_submission_sources(
        matching_submissions,
        local_comparison=local_comparison,
        s2_comparison=s2_comparison,
    )
    source_plan = summarize_source_plan(source_decisions)
    pending_arxiv_papers = collect_unprocessed_arxiv_papers(
        matching_submissions,
        filter_categories=filter_categories,
        local_comparison=local_comparison,
        s2_comparison=s2_comparison,
    )
    kaggle_summary: KaggleCategorySummary | None = None
    if pending_arxiv_papers:
        _status("Kaggle: looking up categories for unprocessed arXiv papers")
        try:
            kaggle_summary = lookup_kaggle_categories(
                pending_arxiv_papers,
                args.kaggle_snapshot,
            )
        except OSError as exc:
            _status(f"Kaggle: category lookup unavailable ({exc})")

    _print_summary(
        venue_stats,
        venue_id=args.venue_id,
        filter_stats=filter_stats,
        local_comparison=local_comparison,
        s2_comparison=s2_comparison,
        s2_filter_result=s2_filter_result,
        category_summary=category_summary,
        kaggle_summary=kaggle_summary,
        show_unprocessed=args.show_unprocessed,
        pdf_stats=summarize_pdf_pipeline_need(
            matching_submissions,
            local_comparison=local_comparison,
            s2_comparison=s2_comparison,
        ),
        source_decisions=source_decisions,
        source_plan=source_plan,
        show_source_decisions=args.show_source_decisions,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
