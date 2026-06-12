"""Tests for Semantic Scholar todo crawl helpers."""

from __future__ import annotations

from backend.s2_todo_crawl import infer_arxiv_id_from_s2


def test_infer_arxiv_id_from_external_ids():
    paper = {"externalIds": {"ArXiv": "2206.08164v2"}}
    assert infer_arxiv_id_from_s2(paper) == "2206.08164"


def test_infer_arxiv_id_from_url_fallback():
    paper = {"url": "https://arxiv.org/abs/2406.08993"}
    assert infer_arxiv_id_from_s2(paper) == "2406.08993"
