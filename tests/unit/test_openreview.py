"""Tests for OpenReview client helpers and paper matching."""

from __future__ import annotations

from backend.openreview_client import OpenReviewClient, parse_openreview_note
from backend.paper_matching import (
    extract_arxiv_id_from_text,
    match_paper_by_title_authors,
    titles_match,
)
from backend.venue import venue_from_openreview_fields


def test_parse_openreview_note_extracts_arxiv_from_pdf():
    note = {
        "id": "note1",
        "forum": "forum1",
        "invitation": "logconference.io/LOG/2023/Conference/-/Submission",
        "content": {
            "title": {"value": "Rank Collapse Causes Over-Smoothing"},
            "authors": {"value": ["Andreas Roth", "Thomas Liebig"]},
            "pdf": {"value": "https://arxiv.org/pdf/2308.16800.pdf"},
            "venue": {"value": "LoG 2023"},
            "venueid": {"value": "logconference.io/LOG/2023/Conference"},
        },
    }
    parsed = parse_openreview_note(note)
    assert parsed.arxiv_id == "2308.16800"
    assert parsed.title.startswith("Rank Collapse")
    assert parsed.authors == ["Andreas Roth", "Thomas Liebig"]


def test_venue_from_openreview_fields_maps_log_venueid():
    assert (
        venue_from_openreview_fields(
            "Accepted as poster",
            "logconference.io/LOG/2023/Conference",
        )
        == "Learning on Graphs Conference"
    )


def test_titles_match_ignores_case_and_punctuation():
    assert titles_match(
        "Rank Collapse Causes Over-Smoothing",
        "rank collapse causes over smoothing",
    )


def test_match_paper_by_title_authors_finds_db_row():
    class _Paper:
        def __init__(self) -> None:
            self.arxiv_id = "2308.16800"
            self.title = "Rank Collapse Causes Over-Smoothing and Over-Correlation in GNNs"
            self.authors = [{"name": "Andreas Roth"}, {"name": "Thomas Liebig"}]

    match = match_paper_by_title_authors(
        [_Paper()],
        title="Rank Collapse Causes Over-Smoothing and Over-Correlation in GNNs",
        authors=["Andreas Roth", "Thomas Liebig"],
    )
    assert match is not None
    assert match.arxiv_id == "2308.16800"


def test_openreview_client_from_config_prefers_token(monkeypatch):
    monkeypatch.setenv("OPENREVIEW_TOKEN", "test-token")
    monkeypatch.setenv("OPENREVIEW_USERNAME", "user@example.com")
    monkeypatch.setenv("OPENREVIEW_PASSWORD", "secret")
    from backend.config import cfg

    cfg.openreview_token = "test-token"
    cfg.openreview_username = "user@example.com"
    cfg.openreview_password = "secret"
    client = OpenReviewClient.from_config()
    assert client.token == "test-token"


def test_extract_arxiv_id_from_text():
    assert extract_arxiv_id_from_text("https://arxiv.org/abs/2308.16800v2") == "2308.16800"


def test_login_for_token_returns_bearer(monkeypatch):
    class _Response:
        status_code = 200

        @staticmethod
        def json():
            return {"token": "abc123"}

    monkeypatch.setattr(
        "backend.openreview_client.requests.Session.post",
        lambda self, url, json, timeout: _Response(),
    )
    token = OpenReviewClient.login_for_token("user@example.com", "pw", expires_in=3600)
    assert token == "abc123"
