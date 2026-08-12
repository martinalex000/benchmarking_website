"""Tests for the read-only OpenReview venue statistics tool."""

from __future__ import annotations

import json
import sqlite3

import requests

from backend.arxiv_metadata_analysis import ScreeningConfig
from backend.openreview_client import OpenReviewClient, OpenReviewError, OpenReviewPaper
from scripts import openreview_stats


def _paper(
    title: str,
    *,
    arxiv_id: str = "",
    pdf_url: str = "",
    note_id: str = "note-1",
    abstract: str = "",
) -> OpenReviewPaper:
    return OpenReviewPaper(
        note_id=note_id,
        forum_id=note_id,
        title=title,
        authors=["Alice Example"],
        arxiv_id=arxiv_id,
        venue="Accepted",
        venueid="NeurIPS.cc/2025/Conference",
        pdf_url=pdf_url,
        invitation="NeurIPS.cc/2025/Conference/-/Submission",
        abstract=abstract,
    )


def _local(
    arxiv_id: str,
    title: str,
    *,
    authors: list[dict[str, str]] | None = None,
    abstract: str = "",
    result_count: int = 0,
) -> openreview_stats.LocalPaperRecord:
    return openreview_stats.LocalPaperRecord(
        arxiv_id=arxiv_id,
        title=title,
        authors=authors or [{"name": "Alice Example"}],
        abstract=abstract,
        result_count=result_count,
    )


def test_summarize_submissions_counts_metadata_and_duplicates():
    stats = openreview_stats.summarize_submissions(
        [
            _paper("First", arxiv_id="2501.00001", pdf_url="https://openreview.net/pdf?id=1"),
            _paper("Second", arxiv_id="2501.00001", pdf_url="https://openreview.net/pdf?id=2"),
            _paper("Third", pdf_url="https://openreview.net/pdf?id=3"),
        ]
    )

    assert stats.total == 3
    assert stats.with_arxiv_id == 2
    assert stats.without_arxiv_id == 1
    assert stats.with_pdf_url == 3
    assert stats.without_pdf_url == 0
    assert stats.unique_arxiv_ids == 1
    assert stats.duplicate_arxiv_ids == 1
    assert stats.duplicate_arxiv_submissions == 1


def test_openreview_client_iterates_all_api_pages(monkeypatch):
    client = OpenReviewClient(token="test-token")
    responses = iter(
        [
            {"notes": [{"id": "note-1"}, {"id": "note-2"}]},
            {"notes": [{"id": "note-3"}]},
        ]
    )
    requests_seen: list[dict[str, object]] = []

    class FakeResponse:
        status_code = 200

        def __init__(self, payload):
            self.payload = payload

        def json(self):
            return self.payload

    def fake_get(url, *, params, timeout):
        requests_seen.append({"url": url, "params": params, "timeout": timeout})
        return FakeResponse(next(responses))

    monkeypatch.setattr(client.session, "get", fake_get)

    notes = client.iter_notes(invitation="NeurIPS.cc/2025/Conference/-/Submission", limit=2)

    assert [note["id"] for note in notes] == ["note-1", "note-2", "note-3"]
    assert [request["params"]["offset"] for request in requests_seen] == [0, 2]


def test_load_local_papers_uses_read_only_database(tmp_path):
    db_path = tmp_path / "papers.db"
    connection = sqlite3.connect(db_path)
    connection.execute(
        "CREATE TABLE papers (id INTEGER PRIMARY KEY, arxiv_id TEXT, "
        "title TEXT, authors TEXT, abstract TEXT)"
    )
    connection.execute("CREATE TABLE results (id INTEGER PRIMARY KEY, paper_id INTEGER)")
    connection.execute(
        "INSERT INTO papers VALUES (?, ?, ?, ?, ?)",
        (1, "2501.00001v2", "Local title", '[{"name": "Alice Example"}]', "An abstract."),
    )
    connection.execute(
        "INSERT INTO papers VALUES (?, ?, ?, ?, ?)",
        (2, "2501.00002", "No results", '[{"name": "Alice Example"}]', ""),
    )
    connection.execute("INSERT INTO results VALUES (?, ?)", (1, 1))
    connection.commit()
    connection.close()

    papers = openreview_stats.load_local_papers(db_path)

    assert papers == [
        _local(
            "2501.00001",
            "Local title",
            abstract="An abstract.",
            result_count=1,
        ),
        _local("2501.00002", "No results"),
    ]


def test_summarize_pdf_pipeline_need_prioritizes_openreview_local_and_s2():
    submissions = [
        _paper("OpenReview", arxiv_id="2501.00001", note_id="note-1"),
        _paper("Local", note_id="note-2"),
        _paper("Semantic Scholar", note_id="note-3"),
        _paper("Missing", note_id="note-4"),
    ]
    local = openreview_stats.compare_local(submissions[1:2], [_local("2501.00002", "Local")])
    s2 = openreview_stats.compare_s2(
        submissions[2:3], [openreview_stats.S2Candidate("2501.00003", "Semantic Scholar")]
    )

    stats = openreview_stats.summarize_pdf_pipeline_need(
        submissions,
        local_comparison=local,
        s2_comparison=s2,
    )

    assert stats.considered == 4
    assert stats.openreview_arxiv == 1
    assert stats.local_arxiv == 1
    assert stats.semantic_scholar_arxiv == 1
    assert stats.needs_pdf_pipeline == 1


def test_resolve_submission_sources_is_arxiv_first_and_blocks_ambiguity():
    submissions = [
        _paper("Processed", note_id="processed"),
        _paper("OpenReview arXiv", arxiv_id="2501.00002", note_id="openreview"),
        _paper("Local pending", note_id="local"),
        _paper("S2 resolved", note_id="s2"),
        _paper("Ambiguous", pdf_url="https://openreview.net/pdf?id=amb", note_id="ambiguous"),
        _paper("PDF only", pdf_url="https://openreview.net/pdf?id=pdf", note_id="pdf"),
        _paper("Unavailable", note_id="unavailable"),
    ]
    local = openreview_stats.compare_local(
        submissions,
        [
            _local("2501.00001", "Processed", result_count=4),
            _local("2501.00003", "Local pending"),
            _local("2501.00004", "Ambiguous"),
            _local("2501.00005", "Ambiguous"),
        ],
    )
    s2 = openreview_stats.compare_s2(
        submissions,
        [openreview_stats.S2Candidate("2501.00006", "S2 resolved")],
    )

    decisions = openreview_stats.resolve_submission_sources(
        submissions,
        local_comparison=local,
        s2_comparison=s2,
    )

    assert [(decision.note_id, decision.action) for decision in decisions] == [
        ("processed", "skip-processed"),
        ("openreview", "queue-arxiv"),
        ("local", "queue-arxiv"),
        ("s2", "queue-arxiv"),
        ("ambiguous", "review"),
        ("pdf", "queue-pdf"),
        ("unavailable", "unavailable"),
    ]
    assert decisions[1].evidence == "openreview-arxiv-id"
    assert decisions[1].venue_id == "NeurIPS.cc/2025/Conference"
    assert decisions[2].evidence == "local-title-author"
    assert decisions[3].evidence == "semantic-scholar-title"
    assert decisions[4].pdf_url.endswith("id=amb")
    assert openreview_stats.summarize_source_plan(decisions) == openreview_stats.SourcePlanStats(
        considered=7,
        already_processed=1,
        planned_arxiv=3,
        planned_openreview_pdf=1,
        review_required=1,
        unavailable=1,
    )


def test_compare_local_prefers_arxiv_then_title_author_and_reports_ambiguity():
    submissions = [
        _paper("Direct", arxiv_id="2501.00001"),
        _paper("Changed Title", note_id="note-2"),
        _paper("Missing", note_id="note-3"),
        _paper("Ambiguous", note_id="note-4"),
    ]
    papers = [
        _local("2501.00001", "Direct"),
        _local("2501.00002", "Changed Title"),
        _local("2501.00003", "Ambiguous"),
        _local("2501.00004", "Ambiguous"),
    ]

    comparison = openreview_stats.compare_local(submissions, papers)

    assert comparison.direct_matches == 1
    assert comparison.title_author_matches == 1
    assert comparison.ambiguous == 1
    assert comparison.unmatched == 1
    assert comparison.matches["note-2"].status == "title-author"
    assert comparison.matches["note-4"].status == "ambiguous"


def test_compare_s2_matches_arxiv_and_unresolved_titles():
    submissions = [
        _paper("Known", arxiv_id="2501.00001"),
        _paper("Changed title", note_id="note-2"),
        _paper("Absent", note_id="note-3"),
    ]
    candidates = [
        openreview_stats.S2Candidate("2501.00001", "Different S2 title"),
        openreview_stats.S2Candidate("2501.00002", "Changed title"),
    ]

    comparison = openreview_stats.compare_s2(submissions, candidates)

    assert comparison.available is True
    assert comparison.candidate_count == 2
    assert comparison.candidates_with_arxiv == 2
    assert comparison.direct_matches == 1
    assert comparison.title_matches == 1
    assert comparison.unmatched == 1


def test_compare_s2_reports_unavailable_without_failing():
    comparison = openreview_stats.compare_s2([], [], "Semantic Scholar unavailable")

    assert comparison.available is False
    assert comparison.error == "Semantic Scholar unavailable"


def test_fetch_s2_candidates_deduplicates_pages(monkeypatch):
    class Page:
        papers = (
            {
                "paperId": "one",
                "title": "First",
                "abstract": "An abstract.",
                "externalIds": {"ArXiv": "2501.00001"},
            },
            {"paperId": "two", "title": "Second", "externalIds": {}},
        )

    monkeypatch.setattr(openreview_stats, "iter_papers_bulk", lambda *_args: iter([Page(), Page()]))

    candidates, error = openreview_stats.fetch_s2_candidates("NeurIPS", 2025)

    assert error == ""
    assert candidates == [
        openreview_stats.S2Candidate("2501.00001", "First", "An abstract."),
        openreview_stats.S2Candidate("", "Second"),
    ]


def test_fetch_s2_candidates_reports_api_failure(monkeypatch):
    def fail(*_args, **_kwargs):
        raise openreview_stats.SemanticScholarAPIError("S2 unavailable")

    monkeypatch.setattr(openreview_stats, "iter_papers_bulk", fail)

    candidates, error = openreview_stats.fetch_s2_candidates("NeurIPS", 2025)

    assert candidates == []
    assert error == "S2 unavailable"


def test_openreview_cache_reuses_successful_response(monkeypatch, tmp_path):
    submissions = [_paper("Cached paper", arxiv_id="2501.00001")]
    calls = 0

    class FakeClient:
        def fetch_venue_submissions(self, _venue_id):
            nonlocal calls
            calls += 1
            return submissions

    monkeypatch.setattr(openreview_stats.OpenReviewClient, "from_config", lambda: FakeClient())

    first = openreview_stats.load_or_fetch_openreview(
        "NeurIPS.cc/2024/Conference",
        cache_dir=tmp_path,
        use_cache=True,
        refresh_cache=False,
    )
    second = openreview_stats.load_or_fetch_openreview(
        "NeurIPS.cc/2024/Conference",
        cache_dir=tmp_path,
        use_cache=True,
        refresh_cache=False,
    )

    assert first == submissions
    assert second == submissions
    assert calls == 1
    assert list(tmp_path.glob("openreview-*.json"))


def test_s2_cache_reuses_successful_response(monkeypatch, tmp_path):
    candidates = [openreview_stats.S2Candidate("2501.00001", "Cached paper")]
    calls = 0

    def fake_fetch(_venue, _year):
        nonlocal calls
        calls += 1
        return candidates, ""

    monkeypatch.setattr(openreview_stats, "fetch_s2_candidates", fake_fetch)

    first = openreview_stats.load_or_fetch_s2(
        "NeurIPS",
        2024,
        cache_dir=tmp_path,
        use_cache=True,
        refresh_cache=False,
    )
    second = openreview_stats.load_or_fetch_s2(
        "NeurIPS",
        2024,
        cache_dir=tmp_path,
        use_cache=True,
        refresh_cache=False,
    )

    assert first == (candidates, "")
    assert second == (candidates, "")
    assert calls == 1
    assert list(tmp_path.glob("semantic-scholar-*.json"))


def test_fast_filter_counts_matches_and_unknown_metadata():
    submissions = [
        _paper("Graph neural networks", abstract="We study graph neural networks."),
        _paper("Graph only", note_id="note-2", abstract="We study graph structure."),
        _paper("No abstract", note_id="note-3"),
    ]

    result = openreview_stats.run_fast_filter(
        submissions,
        screening_config=ScreeningConfig.load(
            openreview_stats.cfg.config_dir / "arxiv_screening.yaml"
        ),
    )
    stats = result.stats

    assert stats.specific_matches == 1
    assert stats.graph_matches == 1
    assert stats.unknown_abstract == 1
    assert stats.unknown_category == 2
    assert stats.filtered_out == 0
    assert stats.eligible == 0
    assert [paper.title for paper in result.matched_submissions] == [
        "Graph neural networks",
        "Graph only",
    ]
    assert result.categories == {"note-1": "specific", "note-2": "unspecific"}


def test_filter_s2_candidates_uses_titles_and_abstracts():
    candidates = [
        openreview_stats.S2Candidate(
            "2501.00001", "Specific paper", "We study graph neural networks."
        ),
        openreview_stats.S2Candidate("2501.00002", "Graph paper", "We study graph structure."),
        openreview_stats.S2Candidate("2501.00003", "Other paper", "We study weather."),
    ]
    result = openreview_stats.filter_s2_candidates(
        candidates,
        screening_config=ScreeningConfig.load(
            openreview_stats.cfg.config_dir / "arxiv_screening.yaml"
        ),
    )

    assert result.applied is True
    assert result.raw_candidate_count == 3
    assert [candidate.title for candidate in result.matched_candidates] == [
        "Specific paper",
        "Graph paper",
    ]


def test_filter_s2_candidates_does_not_fallback_to_title_only():
    candidate = openreview_stats.S2Candidate("2501.00001", "Graph paper")

    result = openreview_stats.filter_s2_candidates(
        [candidate],
        screening_config=ScreeningConfig.load(
            openreview_stats.cfg.config_dir / "arxiv_screening.yaml"
        ),
    )

    assert result.applied is False
    assert result.stats.unknown_abstract == 1
    assert result.matched_candidates == [candidate]


def test_lookup_kaggle_categories_reads_pending_arxiv_records(tmp_path):
    snapshot = tmp_path / "snapshot.json"
    snapshot.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "id": "2501.00001",
                        "title": "Kaggle title",
                        "categories": "cs.AI cs.LG",
                    }
                ),
                json.dumps(
                    {
                        "id": "2501.00002",
                        "title": "Statistical title",
                        "categories": "stat.ML",
                    }
                ),
            ]
        ),
        encoding="utf-8",
    )

    result = openreview_stats.lookup_kaggle_categories(
        [
            openreview_stats.PendingArxivPaper(
                "2501.00001", "Old title", filter_match_type="specific"
            ),
            openreview_stats.PendingArxivPaper(
                "2501.00002", "Other title", filter_match_type="unspecific"
            ),
            openreview_stats.PendingArxivPaper("2501.00003", "Missing"),
        ],
        snapshot,
    )

    assert result.category_counts == {"cs.LG": 1, "stat.ML": 1}
    assert result.category_counts_by_match_type == {
        "specific": {"cs.LG": 1},
        "unspecific": {"stat.ML": 1},
    }
    assert result.missing_metadata == 1
    assert result.papers[0].title == "Kaggle title"


def test_collect_unprocessed_arxiv_papers_preserves_filter_match_type():
    submissions = [
        _paper("OpenReview paper", arxiv_id="2501.00001", note_id="openreview"),
        _paper("S2 direct paper", note_id="s2-direct"),
        _paper("S2 title paper", note_id="s2-title"),
    ]
    s2 = openreview_stats.compare_s2(
        submissions[1:],
        [
            openreview_stats.S2Candidate("2501.00002", "S2 direct paper"),
            openreview_stats.S2Candidate("2501.00003", "S2 title paper"),
        ],
    )

    pending = openreview_stats.collect_unprocessed_arxiv_papers(
        submissions,
        filter_categories={"openreview": "specific", "s2-direct": "unspecific"},
        local_comparison=None,
        s2_comparison=s2,
    )

    assert [(paper.arxiv_id, paper.filter_match_type) for paper in pending] == [
        ("2501.00001", "specific"),
        ("2501.00002", "unspecific"),
        ("2501.00003", "unspecific"),
    ]


def test_main_fetches_and_lists_submissions_without_database_or_download(monkeypatch, capsys):
    submissions = [_paper("A paper", arxiv_id="2501.00001", note_id="note-42")]
    calls: list[str] = []

    class FakeClient:
        def fetch_venue_submissions(self, venue_id):
            calls.append(venue_id)
            return submissions

    monkeypatch.setattr(openreview_stats.OpenReviewClient, "from_config", lambda: FakeClient())
    monkeypatch.setattr(
        openreview_stats,
        "_display_submissions",
        lambda papers: [print(paper.title) for paper in papers],
    )
    monkeypatch.setattr(
        openreview_stats,
        "lookup_kaggle_categories",
        lambda _papers, _snapshot: openreview_stats.KaggleCategorySummary([], {}, 1),
    )

    assert (
        openreview_stats.main(
            [
                "--venue-id",
                "NeurIPS.cc/2025/Conference",
                "--no-compare-local",
                "--no-compare-s2",
                "--no-filter",
                "--no-cache",
                "--list",
            ]
        )
        == 0
    )

    output = capsys.readouterr().out
    assert calls == ["NeurIPS.cc/2025/Conference"]
    assert "A paper" in output
    assert "OpenReview (authoritative): 1 submissions; 1 arXiv links" in output


def test_main_can_show_read_only_source_decisions(monkeypatch, capsys):
    submissions = [
        _paper("arXiv paper", arxiv_id="2501.00001", note_id="arxiv"),
        _paper("PDF paper", pdf_url="/pdf/paper.pdf", note_id="pdf"),
    ]

    class FakeClient:
        @staticmethod
        def fetch_venue_submissions(_venue_id):
            return submissions

    monkeypatch.setattr(openreview_stats.OpenReviewClient, "from_config", lambda: FakeClient())
    monkeypatch.setattr(
        openreview_stats,
        "lookup_kaggle_categories",
        lambda _papers, _snapshot: openreview_stats.KaggleCategorySummary([], {}, 1),
    )

    assert (
        openreview_stats.main(
            [
                "--no-compare-local",
                "--no-compare-s2",
                "--no-filter",
                "--no-cache",
                "--show-source-decisions",
                "2",
            ]
        )
        == 0
    )

    output = capsys.readouterr().out
    assert "Source plan (dry run): processed=0; arXiv=1; OpenReview PDF=1" in output
    assert "queue-arxiv" in output
    assert "queue-pdf" in output


def test_main_defaults_to_neurips_2024(monkeypatch, capsys):
    calls: list[str] = []

    class FakeClient:
        def fetch_venue_submissions(self, venue_id):
            calls.append(venue_id)
            return []

    monkeypatch.setattr(openreview_stats.OpenReviewClient, "from_config", lambda: FakeClient())
    monkeypatch.setattr(openreview_stats, "load_local_papers", lambda _path: [])
    monkeypatch.setattr(openreview_stats, "fetch_s2_candidates", lambda _venue, _year: ([], ""))

    assert openreview_stats.main(["--no-cache"]) == 0
    assert calls == ["NeurIPS.cc/2024/Conference"]
    output = capsys.readouterr().out
    assert "Summary: NeurIPS.cc/2024/Conference" in output
    assert "Summary" in output
    assert "OpenReview filter hits" in output
    assert "Processed in local DB" in output
    assert "Matched in S2" in output
    assert "PDF pipeline:" not in output


def test_main_matches_only_filter_hits(monkeypatch):
    submissions = [
        _paper("Graph paper", note_id="hit", abstract="We study graph neural networks."),
        _paper("Other paper", note_id="miss", abstract="We study weather forecasting."),
    ]
    local_seen: list[list[str]] = []
    s2_seen: list[list[str]] = []
    real_compare_local = openreview_stats.compare_local
    real_compare_s2 = openreview_stats.compare_s2

    class FakeClient:
        def fetch_venue_submissions(self, _venue_id):
            return submissions

    def compare_local(submissions, papers):
        local_seen.append([paper.note_id for paper in submissions])
        return real_compare_local(submissions, papers)

    def compare_s2(submissions, candidates, error=""):
        s2_seen.append([paper.note_id for paper in submissions])
        return real_compare_s2(submissions, candidates, error)

    monkeypatch.setattr(openreview_stats.OpenReviewClient, "from_config", lambda: FakeClient())
    monkeypatch.setattr(openreview_stats, "load_local_papers", lambda _path: [])
    monkeypatch.setattr(openreview_stats, "fetch_s2_candidates", lambda _venue, _year: ([], ""))
    monkeypatch.setattr(openreview_stats, "compare_local", compare_local)
    monkeypatch.setattr(openreview_stats, "compare_s2", compare_s2)

    assert openreview_stats.main(["--no-cache"]) == 0
    assert local_seen == [["hit"]]
    assert s2_seen == [["hit"]]


def test_main_reports_openreview_failure(monkeypatch, capsys):
    monkeypatch.setattr(
        openreview_stats.OpenReviewClient,
        "from_config",
        lambda: (_ for _ in ()).throw(OpenReviewError("venue not found")),
    )

    assert openreview_stats.main(["--venue-id", "ICML.cc/2022/Conference", "--no-cache"]) == 1
    assert "OpenReview request failed: venue not found" in capsys.readouterr().err


def test_main_reports_network_failure(monkeypatch, capsys):
    monkeypatch.setattr(
        openreview_stats.OpenReviewClient,
        "from_config",
        lambda: (_ for _ in ()).throw(requests.ConnectionError("network unavailable")),
    )

    assert openreview_stats.main(["--venue-id", "ICML.cc/2022/Conference", "--no-cache"]) == 1
    assert "OpenReview request failed: network unavailable" in capsys.readouterr().err


def test_main_does_not_use_local_state(monkeypatch):
    class FakeClient:
        @staticmethod
        def fetch_venue_submissions(_venue):
            return []

    monkeypatch.setattr(openreview_stats.OpenReviewClient, "from_config", lambda: FakeClient())

    assert (
        openreview_stats.main(
            [
                "--venue-id",
                "NeurIPS.cc/2025/Conference",
                "--no-compare-local",
                "--no-compare-s2",
                "--no-filter",
                "--no-cache",
            ]
        )
        == 0
    )
    assert not hasattr(openreview_stats, "init_db")
    assert not hasattr(openreview_stats, "PaperStorage")
    assert not hasattr(openreview_stats, "download_alternative")
