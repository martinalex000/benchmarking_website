import pytest

from backend.latex_source import _read_limited_response


class DummySourceResponse:
    def __init__(self, chunks, headers=None):
        self._chunks = list(chunks)
        self.headers = headers or {}

    def read(self, _size=-1):
        if not self._chunks:
            return b""
        return self._chunks.pop(0)


def test_read_limited_response_rejects_large_content_length():
    response = DummySourceResponse([], headers={"Content-Length": str(201 * 1024 * 1024)})

    with pytest.raises(ValueError, match="200 MB"):
        _read_limited_response(response, "2401.00001")


def test_read_limited_response_rejects_stream_over_limit(monkeypatch):
    monkeypatch.setattr("backend.latex_source.MAX_SOURCE_DOWNLOAD_BYTES", 10)
    response = DummySourceResponse([b"x" * 6, b"y" * 6])

    with pytest.raises(ValueError, match="200 MB"):
        _read_limited_response(response, "2401.00001")
