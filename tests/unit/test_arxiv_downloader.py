import pytest

from backend.arxiv_downloader import MAX_PDF_DOWNLOAD_BYTES, _download_pdf
from backend.paper_storage import PaperStorage


class DummyResponse:
    def __init__(self, chunks, headers=None):
        self._chunks = chunks
        self.headers = headers or {}
        self.url = "https://arxiv.org/pdf/2401.00001"

    def iter_content(self, chunk_size=8192):
        yield from self._chunks


def test_download_pdf_rejects_large_content_length(monkeypatch, tmp_path):
    storage = PaperStorage("2401.00001", papers_root=tmp_path)
    response = DummyResponse([], headers={"Content-Length": str(MAX_PDF_DOWNLOAD_BYTES + 1)})
    monkeypatch.setattr("backend.arxiv_downloader._get", lambda *args, **kwargs: response)

    with pytest.raises(ValueError, match="200 MB"):
        _download_pdf("2401.00001", storage)

    assert not storage.pdf_path.exists()


def test_download_pdf_rejects_stream_over_limit_and_removes_partial(monkeypatch, tmp_path):
    storage = PaperStorage("2401.00001", papers_root=tmp_path)
    response = DummyResponse([b"x" * 6, b"y" * 6])
    monkeypatch.setattr("backend.arxiv_downloader.MAX_PDF_DOWNLOAD_BYTES", 10)
    monkeypatch.setattr("backend.arxiv_downloader._get", lambda *args, **kwargs: response)

    with pytest.raises(ValueError, match="200 MB"):
        _download_pdf("2401.00001", storage)

    assert not storage.pdf_path.exists()
