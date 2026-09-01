"""Tests for publication venue helpers."""

from __future__ import annotations

import pytest

from backend.semantic_scholar import _resolve_venue_from_s2, resolve_paper_venue
from backend.venue import (
    conference_export_fields,
    export_published_venue,
    is_arxiv_only_venue,
    is_conference_publication_venue,
    is_peer_reviewed_publication_venue,
    is_untrusted_s2_publication_venue,
    is_untrusted_venue,
    normalize_conference_short,
    resolve_canonical_venue,
    venue_from_arxiv_comment,
    venue_needs_resolution,
)


@pytest.mark.parametrize(
    "venue",
    [
        "arXiv",
        "arxiv",
        "arXiv.org",
        "arXiv preprint",
        "CoRR",
        "corr / arxiv",
    ],
)
def test_is_arxiv_only_venue_detects_arxiv_labels(venue: str):
    assert is_arxiv_only_venue(venue)


@pytest.mark.parametrize(
    "venue",
    [
        "NeurIPS 2024",
        "International Conference on Learning Representations",
        "Nature",
        "ICLR (arXiv version)",
        "Learning on Graphs Conference",
    ],
)
def test_is_arxiv_only_venue_keeps_real_venues(venue: str):
    assert not is_arxiv_only_venue(venue)


@pytest.mark.parametrize(
    ("venue", "expected"),
    [
        ("NeurIPS 2024", True),
        ("arXiv.org", False),
        ("Trans. Mach. Learn. Res.", False),
        ("Accepted at the ICLR 2026 GRaM Workshop", False),
    ],
)
def test_is_conference_publication_venue(venue: str, expected: bool):
    assert is_conference_publication_venue(venue) is expected


@pytest.mark.parametrize(
    ("venue", "expected"),
    [("NeurIPS 2024", True), ("Nature", True), ("arXiv", False), ("LOG IN", False)],
)
def test_is_peer_reviewed_publication_venue_uses_trusted_non_arxiv_venue(
    venue: str, expected: bool
):
    assert is_peer_reviewed_publication_venue(venue) is expected


@pytest.mark.parametrize(
    "venue",
    [
        "LOG IN",
        "Log in",
        "log in",
    ],
)
def test_is_untrusted_venue_detects_log_in_journal(venue: str):
    assert is_untrusted_venue(venue)


def test_is_untrusted_s2_publication_venue_detects_log_in_journal_payload():
    payload = {
        "name": "LOG IN",
        "type": "journal",
        "issn": "0720-8642",
        "url": "https://www.log-in-verlag.de/informatische_bildung/",
    }
    assert is_untrusted_s2_publication_venue(payload)


def test_resolve_venue_from_s2_rejects_log_in_journal_payload():
    data = {
        "venue": "LOG IN",
        "publicationVenue": {
            "name": "LOG IN",
            "type": "journal",
            "issn": "0720-8642",
            "url": "https://www.log-in-verlag.de/informatische_bildung/",
        },
    }
    assert _resolve_venue_from_s2(data) == ""


def test_resolve_venue_from_s2_prefers_publication_venue_over_arxiv_label():
    data = {
        "venue": "arXiv",
        "publicationVenue": {"name": "International Conference on Learning Representations"},
    }
    assert _resolve_venue_from_s2(data) == "International Conference on Learning Representations"


def test_resolve_venue_from_s2_keeps_non_arxiv_top_level_venue():
    data = {"venue": "NeurIPS 2024", "publicationVenue": {"name": "arXiv"}}
    assert _resolve_venue_from_s2(data) == "NeurIPS 2024"


@pytest.mark.parametrize(
    ("venue", "expected"),
    [
        ("Graph Learning Conference", "LoG"),
        ("LoG 2023", "LoG"),
        ("Learning on Graphs Conference", "LoG"),
        ("Proceedings of the Second Learning on Graphs Conference", "LoG"),
        ("LOG IN", ""),
        ("NeurIPS 2024", "NeurIPS"),
    ],
)
def test_normalize_conference_short_maps_common_venues(venue: str, expected: str):
    assert normalize_conference_short(venue) == expected


@pytest.mark.parametrize(
    ("comment", "expected"),
    [
        ("LoG 2023", "Learning on Graphs Conference"),
        ("Accepted at LoG 2024", "Learning on Graphs Conference"),
        ("", ""),
        ("LOG IN", ""),
    ],
)
def test_venue_from_arxiv_comment(comment: str, expected: str):
    assert venue_from_arxiv_comment(comment) == expected


def test_resolve_canonical_venue_maps_log_to_long_name():
    assert resolve_canonical_venue("LoG 2023") == "Learning on Graphs Conference"


def test_export_published_venue_strips_arxiv_only_labels():
    assert export_published_venue("arXiv.org") == ""
    assert export_published_venue("NeurIPS 2024", "2024-12-10") == "NeurIPS 2024"
    assert export_published_venue("LOG IN", "2023-08-31") == ""
    assert export_published_venue("Learning on Graphs Conference", "2023-08-31") == "LoG 2023"


def test_conference_export_fields_include_year_for_log():
    fields = conference_export_fields("Learning on Graphs Conference", "2023-08-31")
    assert fields["published_conference"] == "LoG 2023"
    assert fields["published_conference_short"] == "LoG"
    assert fields["published_conference_slug"] == "log"


def test_venue_needs_resolution_for_untrusted_and_missing():
    assert venue_needs_resolution("")
    assert venue_needs_resolution("arXiv.org")
    assert venue_needs_resolution("LOG IN")
    assert not venue_needs_resolution("Learning on Graphs Conference")


def test_resolve_paper_venue_uses_local_metadata_before_arxiv(monkeypatch):
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_paper_metadata",
        lambda _arxiv_id: {"venue": "LOG IN"},
    )
    monkeypatch.setattr(
        "backend.semantic_scholar._venue_from_local_metadata",
        lambda _arxiv_id: "Learning on Graphs Conference",
    )
    monkeypatch.setattr(
        "backend.semantic_scholar._venue_from_openreview_for_paper",
        lambda _arxiv_id: "",
    )
    monkeypatch.setattr(
        "backend.semantic_scholar._venue_from_arxiv_metadata",
        lambda _arxiv_id: (_ for _ in ()).throw(AssertionError("arxiv api should not run")),
    )
    assert resolve_paper_venue("2308.16800") == "Learning on Graphs Conference"
