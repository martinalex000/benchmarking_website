"""Unit tests for figure extraction safeguards."""

from types import SimpleNamespace

from backend.figure_extractor import extract_from_html


def _storage(root):
    return SimpleNamespace(
        arxiv_id="2206.08164",
        html_dir=root / "html",
        figures_dir=root / "figures",
    )


def test_extract_from_html_refuses_local_path_traversal(tmp_path):
    storage = _storage(tmp_path)
    storage.html_dir.mkdir()
    (tmp_path / "secret.png").write_bytes(b"secret")

    assert extract_from_html(storage, "../secret.png") is None
    assert not (storage.figures_dir / "main_figure.png").exists()


def test_extract_from_html_refuses_private_url(tmp_path):
    storage = _storage(tmp_path)
    storage.html_dir.mkdir()

    assert extract_from_html(storage, "http://127.0.0.1/figure.png") is None
