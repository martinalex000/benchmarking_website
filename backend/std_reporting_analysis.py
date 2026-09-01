"""Quarterly paper-level statistics for reported standard deviations."""

from __future__ import annotations

import csv
import math
import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from backend.venue import is_conference_publication_venue, is_peer_reviewed_publication_venue

STD_REPORTING_RESULT_THRESHOLD = 0.30


@dataclass(frozen=True, slots=True)
class PaperObservation:
    """One paper with whether any of its stored results has a nonzero std."""

    paper_id: int
    paper_date: date
    reports_std: bool


@dataclass(frozen=True, slots=True)
class PaperResultObservation:
    """One paper with counts of all results and results reporting a std."""

    paper_id: int
    paper_date: date
    result_count: int
    std_result_count: int

    @property
    def std_result_fraction(self) -> float:
        """Return the fraction of results with a finite, nonzero std."""
        if not self.result_count:
            return 0.0
        return self.std_result_count / self.result_count

    @property
    def reports_std(self) -> bool:
        """Return whether more than 30% of results report a std."""
        return self.std_result_fraction > STD_REPORTING_RESULT_THRESHOLD


@dataclass(frozen=True, slots=True)
class QuarterlySummary:
    """Paper counts for one calendar quarter."""

    quarter_start: date
    total_papers: int
    papers_with_std: int

    @property
    def quarter(self) -> str:
        """Return the human-readable quarter label."""
        return f"{self.quarter_start.year}-Q{((self.quarter_start.month - 1) // 3) + 1}"

    @property
    def reporting_rate(self) -> float:
        """Return the share of result-bearing papers reporting a std."""
        if not self.total_papers:
            return 0.0
        return self.papers_with_std / self.total_papers


@dataclass(frozen=True, slots=True)
class YearlySummary:
    """Paper counts for one publication year."""

    year: int
    total_papers: int
    papers_with_std: int

    @property
    def reporting_rate(self) -> float:
        """Return the share of result-bearing papers reporting a std."""
        if not self.total_papers:
            return 0.0
        return self.papers_with_std / self.total_papers


def parse_paper_date(value: str | None) -> date | None:
    """Parse the repository's full- or month-resolution publication dates."""
    raw = str(value or "").strip()
    if len(raw) == 7:
        raw = f"{raw}-01"
    if len(raw) != 10:
        return None
    try:
        return date.fromisoformat(raw)
    except ValueError:
        return None


def quarter_start(value: date) -> date:
    """Return the first day of the quarter containing *value*."""
    month = ((value.month - 1) // 3) * 3 + 1
    return date(value.year, month, 1)


def _next_quarter(value: date) -> date:
    if value.month == 10:
        return date(value.year + 1, 1, 1)
    return date(value.year, value.month + 3, 1)


def _deduplicate_observations(
    observations: list[PaperObservation],
) -> dict[int, PaperObservation]:
    """Collapse result-level observations to one std-reporting flag per paper."""
    if not observations:
        return {}

    papers: dict[int, PaperObservation] = {}
    for observation in observations:
        previous = papers.get(observation.paper_id)
        if previous is None:
            papers[observation.paper_id] = observation
            continue
        if previous.paper_date != observation.paper_date:
            raise ValueError(f"Paper {observation.paper_id} has multiple publication dates")
        papers[observation.paper_id] = PaperObservation(
            paper_id=observation.paper_id,
            paper_date=previous.paper_date,
            reports_std=previous.reports_std or observation.reports_std,
        )
    return papers


def summarize_quarterly(observations: list[PaperObservation]) -> list[QuarterlySummary]:
    """Aggregate observations once per paper and return a continuous series.

    A paper may have many result rows.  Its quarter is determined by its paper
    date, and it contributes to ``papers_with_std`` if any row reports a finite,
    nonzero standard deviation.
    """
    papers = _deduplicate_observations(observations)
    if not papers:
        return []

    by_quarter: dict[date, list[PaperObservation]] = {}
    for observation in papers.values():
        by_quarter.setdefault(quarter_start(observation.paper_date), []).append(observation)

    first = min(by_quarter)
    last = max(by_quarter)
    summaries: list[QuarterlySummary] = []
    current = first
    while current <= last:
        quarter_papers = by_quarter.get(current, [])
        summaries.append(
            QuarterlySummary(
                quarter_start=current,
                total_papers=len(quarter_papers),
                papers_with_std=sum(paper.reports_std for paper in quarter_papers),
            )
        )
        current = _next_quarter(current)
    return summaries


def summarize_yearly(observations: list[PaperObservation]) -> list[YearlySummary]:
    """Aggregate observations once per paper and return a continuous yearly series."""
    papers = _deduplicate_observations(observations)
    if not papers:
        return []

    by_year: dict[int, list[PaperObservation]] = {}
    for observation in papers.values():
        by_year.setdefault(observation.paper_date.year, []).append(observation)

    first = min(by_year)
    last = max(by_year)
    return [
        YearlySummary(
            year=year,
            total_papers=len(by_year.get(year, [])),
            papers_with_std=sum(paper.reports_std for paper in by_year.get(year, [])),
        )
        for year in range(first, last + 1)
    ]


def summarize_yearly_by_std_fraction(
    observations: list[PaperResultObservation],
) -> list[YearlySummary]:
    """Summarize papers whose std-bearing result fraction exceeds 30%."""
    papers: dict[int, PaperResultObservation] = {}
    for observation in observations:
        previous = papers.get(observation.paper_id)
        if previous is None:
            papers[observation.paper_id] = observation
            continue
        if previous.paper_date != observation.paper_date:
            raise ValueError(f"Paper {observation.paper_id} has multiple publication dates")
        papers[observation.paper_id] = PaperResultObservation(
            paper_id=observation.paper_id,
            paper_date=previous.paper_date,
            result_count=previous.result_count + observation.result_count,
            std_result_count=previous.std_result_count + observation.std_result_count,
        )
    if not papers:
        return []

    by_year: dict[int, list[PaperResultObservation]] = {}
    for observation in papers.values():
        by_year.setdefault(observation.paper_date.year, []).append(observation)
    return [
        YearlySummary(
            year=year,
            total_papers=len(by_year.get(year, [])),
            papers_with_std=sum(paper.reports_std for paper in by_year.get(year, [])),
        )
        for year in range(min(by_year), max(by_year) + 1)
    ]


def _is_nonzero_finite(value: object) -> bool:
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return False
    return math.isfinite(numeric) and numeric != 0.0


def load_paper_observations(
    db_path: Path, *, conference_only: bool = False, peer_reviewed_only: bool = False
) -> list[PaperObservation]:
    """Load result-bearing papers and their raw nonzero ``metric_std`` status.

    Problematic result rows are omitted because they are known not to represent
    trustworthy benchmark observations.  Manual std overrides are deliberately
    not used: this analysis measures what was present in the extracted paper
    result, not what was later corrected for display.
    """
    resolved_path = db_path.expanduser().resolve()
    if not resolved_path.is_file():
        raise FileNotFoundError(f"Database not found: {db_path}")

    observations: dict[int, PaperObservation] = {}
    with sqlite3.connect(f"file:{resolved_path}?mode=ro", uri=True) as connection:
        rows = connection.execute(
            """
            SELECT p.id, p.published_date, r.metric_std, p.venue
            FROM papers AS p
            JOIN results AS r ON r.paper_id = p.id
            WHERE COALESCE(r.is_problematic, 0) = 0
            """
        )
        for paper_id, raw_date, raw_std, venue in rows:
            if conference_only and not is_conference_publication_venue(venue):
                continue
            if peer_reviewed_only and not is_peer_reviewed_publication_venue(venue):
                continue
            paper_date = parse_paper_date(raw_date)
            if paper_date is None:
                continue
            reports_std = _is_nonzero_finite(raw_std)
            previous = observations.get(paper_id)
            if previous is None:
                observations[paper_id] = PaperObservation(paper_id, paper_date, reports_std)
            else:
                observations[paper_id] = PaperObservation(
                    paper_id=paper_id,
                    paper_date=previous.paper_date,
                    reports_std=previous.reports_std or reports_std,
                )
    return list(observations.values())


def load_paper_result_observations(
    db_path: Path, *, conference_only: bool = False, peer_reviewed_only: bool = False
) -> list[PaperResultObservation]:
    """Load per-paper result counts for the 30% std-reporting analysis."""
    resolved_path = db_path.expanduser().resolve()
    if not resolved_path.is_file():
        raise FileNotFoundError(f"Database not found: {db_path}")

    observations: dict[int, PaperResultObservation] = {}
    with sqlite3.connect(f"file:{resolved_path}?mode=ro", uri=True) as connection:
        rows = connection.execute(
            """
            SELECT p.id, p.published_date, r.metric_std, p.venue
            FROM papers AS p
            JOIN results AS r ON r.paper_id = p.id
            WHERE COALESCE(r.is_problematic, 0) = 0
            """
        )
        for paper_id, raw_date, raw_std, venue in rows:
            if conference_only and not is_conference_publication_venue(venue):
                continue
            if peer_reviewed_only and not is_peer_reviewed_publication_venue(venue):
                continue
            paper_date = parse_paper_date(raw_date)
            if paper_date is None:
                continue
            has_std = int(_is_nonzero_finite(raw_std))
            previous = observations.get(paper_id)
            if previous is None:
                observations[paper_id] = PaperResultObservation(
                    paper_id=paper_id,
                    paper_date=paper_date,
                    result_count=1,
                    std_result_count=has_std,
                )
            else:
                observations[paper_id] = PaperResultObservation(
                    paper_id=paper_id,
                    paper_date=previous.paper_date,
                    result_count=previous.result_count + 1,
                    std_result_count=previous.std_result_count + has_std,
                )
    return list(observations.values())


def write_csv(summaries: list[QuarterlySummary], output_path: Path) -> None:
    """Write the quarterly series as a portable CSV file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["quarter", "quarter_start", "total_papers", "papers_with_std", "reporting_rate"]
        )
        for summary in summaries:
            writer.writerow(
                [
                    summary.quarter,
                    summary.quarter_start.isoformat(),
                    summary.total_papers,
                    summary.papers_with_std,
                    f"{summary.reporting_rate:.6f}",
                ]
            )


def write_report(summaries: list[QuarterlySummary], output_path: Path) -> None:
    """Write a concise markdown report alongside the CSV and figure."""
    total_papers = sum(summary.total_papers for summary in summaries)
    papers_with_std = sum(summary.papers_with_std for summary in summaries)
    lines = [
        "# Quarterly reporting of standard deviations",
        "",
        "Each paper is counted once in its publication quarter. A paper is counted as reporting a "
        "standard deviation when any non-problematic stored result has a finite, nonzero `metric_std`.",
        "The denominator is papers with at least one stored result and a parseable publication date.",
        "Manual std overrides are not included because this measures the extracted paper report.",
        "",
        f"- Papers with stored results: **{total_papers}**",
        f"- Papers reporting a nonzero std: **{papers_with_std}**",
        f"- Overall reporting rate: **{papers_with_std / total_papers:.1%}**"
        if total_papers
        else "- Overall reporting rate: **0.0%**",
        "",
        "| Quarter | Papers with results | Papers with nonzero std | Reporting rate |",
        "|---|---:|---:|---:|",
    ]
    lines.extend(
        f"| {summary.quarter} | {summary.total_papers} | {summary.papers_with_std} | "
        f"{summary.reporting_rate:.1%} |"
        for summary in summaries
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
