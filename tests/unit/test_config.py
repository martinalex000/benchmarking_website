"""Unit tests for central configuration helpers."""

import pytest

from backend.config import normalize_arxiv_id


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("2206.08164", "2206.08164"),
        ("2206.08164v2", "2206.08164"),
        ("arXiv:2206.08164", "2206.08164"),
        ("arXiv:2206.08164v12", "2206.08164"),
        ("  2401.17791v1  ", "2401.17791"),
    ],
)
def test_normalize_arxiv_id_accepts_modern_ids(raw, expected):
    assert normalize_arxiv_id(raw) == expected


@pytest.mark.parametrize(
    "raw",
    [
        "",
        "../2206.08164",
        "../../tmp/ownedv1",
        "arXiv:../../tmp/ownedv1",
        "/tmp/2206.08164",
        "2206.08164/extra",
        "not-an-arxiv-id",
    ],
)
def test_normalize_arxiv_id_rejects_unsafe_or_invalid_ids(raw):
    with pytest.raises(ValueError):
        normalize_arxiv_id(raw)
