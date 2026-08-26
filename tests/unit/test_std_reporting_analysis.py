"""Tests for quarterly paper-level standard-deviation reporting statistics."""

import sqlite3
from datetime import date

from backend.std_reporting_analysis import (
    PaperObservation,
    PaperResultObservation,
    load_paper_observations,
    quarter_start,
    summarize_quarterly,
    summarize_yearly,
    summarize_yearly_by_std_fraction,
)


def test_quarter_start():
    assert quarter_start(date(2026, 1, 31)) == date(2026, 1, 1)
    assert quarter_start(date(2026, 6, 30)) == date(2026, 4, 1)
    assert quarter_start(date(2026, 12, 1)) == date(2026, 10, 1)


def test_summarize_quarterly_deduplicates_papers_and_fills_gaps():
    summaries = summarize_quarterly(
        [
            PaperObservation(1, date(2020, 1, 5), False),
            PaperObservation(1, date(2020, 1, 5), True),
            PaperObservation(2, date(2020, 7, 5), True),
        ]
    )

    assert [(item.quarter, item.total_papers, item.papers_with_std) for item in summaries] == [
        ("2020-Q1", 1, 1),
        ("2020-Q2", 0, 0),
        ("2020-Q3", 1, 1),
    ]
    assert summaries[0].reporting_rate == 1.0
    assert summaries[1].reporting_rate == 0.0


def test_summarize_yearly_deduplicates_papers_and_fills_gaps():
    summaries = summarize_yearly(
        [
            PaperObservation(1, date(2017, 1, 5), False),
            PaperObservation(1, date(2017, 1, 5), True),
            PaperObservation(2, date(2019, 7, 5), True),
        ]
    )

    assert [(item.year, item.total_papers, item.papers_with_std) for item in summaries] == [
        (2017, 1, 1),
        (2018, 0, 0),
        (2019, 1, 1),
    ]


def test_summarize_yearly_requires_more_than_30_percent_of_results():
    summaries = summarize_yearly_by_std_fraction(
        [
            PaperResultObservation(1, date(2017, 1, 5), 4, 1),
            PaperResultObservation(2, date(2017, 2, 5), 5, 2),
        ]
    )

    assert summaries[0].total_papers == 2
    assert summaries[0].papers_with_std == 1
    assert summaries[0].reporting_rate == 0.5


def test_load_observations_uses_nonzero_raw_std_and_excludes_problematic(tmp_path):
    db_path = tmp_path / "benchmarks.db"
    with sqlite3.connect(db_path) as connection:
        connection.executescript(
            """
            CREATE TABLE papers (id INTEGER PRIMARY KEY, published_date TEXT, venue TEXT);
            CREATE TABLE results (
                paper_id INTEGER,
                metric_std REAL,
                is_problematic INTEGER
            );
            INSERT INTO papers VALUES (1, '2024-01-10', 'NeurIPS 2024');
            INSERT INTO papers VALUES (2, '2024-02', 'arXiv.org');
            INSERT INTO papers VALUES (3, '2024-03-10', 'ICML 2024');
            INSERT INTO results VALUES (1, 0.0, 0);
            INSERT INTO results VALUES (1, 0.02, 0);
            INSERT INTO results VALUES (2, NULL, 0);
            INSERT INTO results VALUES (3, 0.03, 1);
            """
        )

    observations = load_paper_observations(db_path)

    assert [(item.paper_id, item.reports_std) for item in observations] == [
        (1, True),
        (2, False),
    ]

    conference_observations = load_paper_observations(db_path, conference_only=True)
    assert [(item.paper_id, item.reports_std) for item in conference_observations] == [(1, True)]
