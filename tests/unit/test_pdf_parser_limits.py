import sys

import pytest

from backend.pdf_parser import MAX_PDF_PARSE_PAGES, parse_pdf_paper


class FakeFitz:
    def __init__(self, doc):
        self.doc = doc

    def open(self, _path):
        return self.doc


class FakeDoc:
    def __init__(self, page_count):
        self.page_count = page_count
        self.closed = False

    def __len__(self):
        return self.page_count

    def close(self):
        self.closed = True


def test_parse_pdf_rejects_large_file_before_opening(monkeypatch, tmp_path):
    pdf_path = tmp_path / "paper.pdf"
    pdf_path.write_bytes(b"x" * 12)
    fake_doc = FakeDoc(page_count=1)
    monkeypatch.setitem(sys.modules, "fitz", FakeFitz(fake_doc))
    monkeypatch.setattr("backend.pdf_parser.MAX_PDF_PARSE_BYTES", 10)

    with pytest.raises(ValueError, match="200 MB"):
        parse_pdf_paper(pdf_path)


def test_parse_pdf_rejects_too_many_pages_and_closes_doc(monkeypatch, tmp_path):
    pdf_path = tmp_path / "paper.pdf"
    pdf_path.write_bytes(b"%PDF")
    fake_doc = FakeDoc(page_count=MAX_PDF_PARSE_PAGES + 1)
    monkeypatch.setitem(sys.modules, "fitz", FakeFitz(fake_doc))

    with pytest.raises(ValueError, match="page parse limit"):
        parse_pdf_paper(pdf_path)

    assert fake_doc.closed is True
