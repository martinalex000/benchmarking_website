"""Unit tests for alternative PDF downloader safeguards."""

import pytest

from backend import alternative_downloader


class _FakeResponse:
    is_redirect = False
    headers = {"Content-Type": "application/pdf"}
    status_code = 200

    def __init__(self, *, headers=None, chunks=None):
        if headers is not None:
            self.headers = headers
        self._chunks = chunks or []

    def raise_for_status(self):
        return None

    def iter_content(self, chunk_size=8192):  # noqa: ARG002
        yield from self._chunks


def test_get_pdf_rejects_content_length_over_limit(monkeypatch):
    monkeypatch.setattr(alternative_downloader, "validate_public_http_url", lambda url: url)
    monkeypatch.setattr(
        alternative_downloader.requests,
        "get",
        lambda *args, **kwargs: _FakeResponse(
            headers={
                "Content-Type": "application/pdf",
                "Content-Length": str(alternative_downloader.MAX_PDF_BYTES + 1),
            }
        ),
    )

    with pytest.raises(ValueError, match="exceeds"):
        alternative_downloader._get_pdf.__wrapped__("https://example.com/paper.pdf")


def test_get_pdf_rejects_stream_over_limit(monkeypatch):
    monkeypatch.setattr(alternative_downloader, "validate_public_http_url", lambda url: url)
    monkeypatch.setattr(alternative_downloader, "MAX_PDF_BYTES", 4)
    monkeypatch.setattr(
        alternative_downloader.requests,
        "get",
        lambda *args, **kwargs: _FakeResponse(chunks=[b"%PDF", b"too much"]),
    )

    with pytest.raises(ValueError, match="exceeds"):
        alternative_downloader._get_pdf.__wrapped__("https://example.com/paper.pdf")
