from pathlib import Path

import pytest

from backend import openreview_pdf


class DummyResponse:
    def __init__(self, chunks, *, url="https://openreview.net/pdf?id=test", headers=None):
        self._chunks = chunks
        self.url = url
        self.headers = headers or {}

    def raise_for_status(self):
        return None

    def iter_content(self, chunk_size):
        yield from self._chunks


def test_normalize_openreview_pdf_url_accepts_relative_and_rejects_other_hosts():
    assert (
        openreview_pdf.normalize_openreview_pdf_url("/pdf/paper.pdf")
        == "https://openreview.net/pdf/paper.pdf"
    )
    with pytest.raises(ValueError, match="unsupported"):
        openreview_pdf.normalize_openreview_pdf_url("https://example.com/paper.pdf")


def test_stage_openreview_pdf_writes_pdf_and_metadata_atomically(monkeypatch, tmp_path):
    response = DummyResponse([b"%PDF-1.7\n", b"body"])
    requests_seen = []

    def fake_get(*_args, **kwargs):
        requests_seen.append(kwargs)
        return response

    monkeypatch.setattr(openreview_pdf.requests, "get", fake_get)

    staged = openreview_pdf.stage_openreview_pdf(
        note_id="note-1",
        venue_id="Venue/2024/Conference",
        pdf_url="/pdf/paper.pdf",
        output_dir=tmp_path,
        token="secret-token",
    )

    pdf_path = Path(staged.pdf_path)
    assert pdf_path.read_bytes() == b"%PDF-1.7\nbody"
    assert pdf_path.with_suffix(".json").is_file()
    assert not list(tmp_path.rglob("*.part"))
    assert requests_seen[0]["headers"]["Authorization"] == "Bearer secret-token"


def test_stage_openreview_pdf_reuses_valid_existing_file(monkeypatch, tmp_path):
    venue_dir = tmp_path / "Venue_2024_Conference"
    venue_dir.mkdir()
    (venue_dir / "note.pdf").write_bytes(b"%PDF-existing")
    monkeypatch.setattr(
        openreview_pdf.requests,
        "get",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("downloaded")),
    )

    staged = openreview_pdf.stage_openreview_pdf(
        note_id="note",
        venue_id="Venue/2024/Conference",
        pdf_url="/pdf/paper.pdf",
        output_dir=tmp_path,
    )

    assert staged.reused is True


def test_stage_openreview_pdf_rejects_non_pdf_and_removes_partial(monkeypatch, tmp_path):
    response = DummyResponse([b"<html>not a pdf</html>"])
    monkeypatch.setattr(openreview_pdf.requests, "get", lambda *_args, **_kwargs: response)

    with pytest.raises(ValueError, match="not a valid PDF"):
        openreview_pdf.stage_openreview_pdf(
            note_id="note",
            venue_id="Venue/2024/Conference",
            pdf_url="/pdf/paper.pdf",
            output_dir=tmp_path,
        )

    assert not list(tmp_path.rglob("*.pdf"))
    assert not list(tmp_path.rglob("*.part"))


def test_stage_openreview_pdf_rejects_stream_over_limit(monkeypatch, tmp_path):
    response = DummyResponse([b"%PDF-", b"too-large"])
    monkeypatch.setattr(openreview_pdf.requests, "get", lambda *_args, **_kwargs: response)
    monkeypatch.setattr(openreview_pdf, "MAX_PDF_DOWNLOAD_BYTES", 8)

    with pytest.raises(ValueError, match="200 MB"):
        openreview_pdf.stage_openreview_pdf(
            note_id="note",
            venue_id="Venue/2024/Conference",
            pdf_url="/pdf/paper.pdf",
            output_dir=tmp_path,
        )

    assert not list(tmp_path.rglob("*.part"))
