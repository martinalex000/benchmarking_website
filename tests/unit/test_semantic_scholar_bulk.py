"""Tests for Semantic Scholar bulk search and the arXiv-share experiment."""

from __future__ import annotations

import pytest

import backend.semantic_scholar as semantic_scholar
import scripts.measure_ss_arxiv_share as experiment


def test_fetch_papers_bulk_follows_tokens_and_deduplicates(monkeypatch):
    requests: list[tuple[str, dict, dict]] = []
    responses = iter(
        [
            {
                "data": [
                    {"paperId": "one", "externalIds": {"ArXiv": "2501.00001"}},
                    {"paperId": "two", "externalIds": {}},
                ],
                "token": "next-page",
            },
            {
                "data": [
                    {"paperId": "two", "externalIds": {}},
                    {"paperId": "three", "externalIds": {"ARXIV": "2501.00003"}},
                ]
            },
        ]
    )

    def fake_request(url, payload=None, **_kwargs):
        requests.append((url, payload.copy(), _kwargs))
        return next(responses)

    monkeypatch.setattr(semantic_scholar, "_s2_request", fake_request)

    papers = semantic_scholar.fetch_papers_bulk("NeurIPS", 2025)

    assert [paper["paperId"] for paper in papers] == ["one", "two", "three"]
    assert requests[0][0].endswith("/paper/search/bulk")
    assert requests[0][1] == {
        "venue": "NeurIPS",
        "year": "2025",
        "limit": 1000,
        "fields": "title,venue,year,externalIds",
    }
    assert requests[0][2] == {"include_api_key": False}
    assert requests[1][1]["token"] == "next-page"


def test_fetch_papers_bulk_rejects_malformed_response(monkeypatch):
    monkeypatch.setattr(semantic_scholar, "_s2_request", lambda *_args, **_kwargs: {"data": None})

    with pytest.raises(semantic_scholar.SemanticScholarAPIError):
        semantic_scholar.fetch_papers_bulk("NeurIPS", 2025)


@pytest.mark.parametrize(
    ("paper", "expected"),
    [
        ({"externalIds": {"ARXIV": "2501.00001"}}, True),
        ({"externalIds": {"ArXiv": " 2501.00001 "}}, True),
        ({"externalIds": {"ARXIV": ""}}, False),
        ({"externalIds": {"DOI": "10.1234/example"}}, False),
        ({}, False),
    ],
)
def test_has_arxiv_external_id(paper, expected):
    assert experiment.has_arxiv_external_id(paper) is expected


def test_measure_share_counts_records(monkeypatch):
    monkeypatch.setattr(
        experiment,
        "fetch_papers_bulk",
        lambda venue, year: [
            {"paperId": f"{venue}-{year}-1", "externalIds": {"ARXIV": "2501.00001"}},
            {"paperId": f"{venue}-{year}-2", "externalIds": {}},
            {"paperId": f"{venue}-{year}-3"},
        ],
    )

    result = experiment.measure_share("NeurIPS", 2025)

    assert result.paper_count == 3
    assert result.arxiv_count == 1
    assert result.percentage == pytest.approx(100 / 3)


def test_measure_share_resumes_from_page_cache(monkeypatch, tmp_path):
    cache_path = tmp_path / "share-cache.json"
    cache = {"version": 1, "queries": {}}
    calls = []

    def fake_iterator(venue, year, **kwargs):
        calls.append((venue, year, kwargs))
        if kwargs["continuation_token"] is None:
            yield semantic_scholar.SemanticScholarBulkPage(
                papers=(
                    {"paperId": "one", "externalIds": {"ARXIV": "2501.00001"}},
                    {"paperId": "two", "externalIds": {}},
                ),
                next_token="resume-here",
                estimated_total=3,
                page_number=1,
            )
        else:
            yield semantic_scholar.SemanticScholarBulkPage(
                papers=({"paperId": "three", "externalIds": {"ARXIV": "2501.00003"}},),
                next_token="",
                estimated_total=3,
                page_number=2,
            )

    monkeypatch.setattr(experiment, "iter_papers_bulk", fake_iterator)

    partial = experiment.measure_share(
        "NeurIPS", 2025, cache=cache, cache_path=cache_path, show_progress=False
    )
    complete = experiment.measure_share(
        "NeurIPS", 2025, cache=cache, cache_path=cache_path, show_progress=False
    )

    assert partial.paper_count == 2
    assert complete.paper_count == 3
    assert complete.arxiv_count == 2
    assert calls[1][2]["continuation_token"] == "resume-here"
    assert calls[1][2]["seen_paper_ids"] == {"one", "two"}
    assert cache["queries"]['["NeurIPS",2025]']["complete"] is True
    assert cache_path.exists()


def test_cli_supports_year_range_and_prints_summary(monkeypatch, capsys):
    calls = []

    def fake_measure(venue, year, **_kwargs):
        calls.append((venue, year))
        return experiment.ShareResult(venue, year, 10, 4)

    monkeypatch.setattr(experiment, "measure_share", fake_measure)

    assert experiment.main(["--venue", "NeurIPS", "--years", "2023-2025"]) == 0
    output = capsys.readouterr().out

    assert calls == [("NeurIPS", 2023), ("NeurIPS", 2024), ("NeurIPS", 2025)]
    assert "NeurIPS" in output
    assert "40.0%" in output


def test_cli_rejects_conflicting_year_options(capsys):
    assert experiment.main(["--year", "2025", "--years", "2023-2025"]) == 1
    assert "cannot be used together" in capsys.readouterr().err
