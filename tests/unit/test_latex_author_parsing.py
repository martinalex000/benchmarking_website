"""Tests for LaTeX author parsing and S2 ORCID merge."""

from __future__ import annotations

import json

from backend.llm_metadata import _extract_metadata_from_latex_cache, _parse_author_names_from_latex
from backend.models import Paper, author_display_name, normalize_author_entry
from backend.semantic_scholar import (
    fetch_author_external_ids,
    merge_latex_authors_with_s2,
    resolve_paper_authors,
)
from backend.text_cleanup import author_name_looks_broken, authors_look_broken


def test_parse_author_names_single_author():
    tex = r"\author{Alice Smith}"
    assert _parse_author_names_from_latex(tex) == ["Alice Smith"]


def test_parse_author_names_with_and_separator():
    tex = r"\author{Alice Smith \and Bob Jones}"
    assert _parse_author_names_from_latex(tex) == ["Alice Smith", "Bob Jones"]


def test_parse_author_names_optional_short_argument():
    tex = r"\author[Short]{Alice Smith \and Bob Jones}"
    assert _parse_author_names_from_latex(tex) == ["Alice Smith", "Bob Jones"]


def test_parse_author_names_comma_separated_with_affiliations():
    tex = (
        r"\author{Haiteng Zhao$^1$\thanks{Work done during internship} , "
        r"Shuming Ma$^2$, Dongdong Zhang$^2$, Zhi-Hong Deng$^1$, Furu Wei$^2$\\"
        r"$^1$ Peking University\\"
        r"\texttt{\{zhaohaiteng,zhdeng\}@pku.edu.cn}\\"
        r"\texttt{\{shumma,dozhang,fuwei\}@microsoft.com}\\"
        r"}"
    )
    assert _parse_author_names_from_latex(tex) == [
        "Haiteng Zhao",
        "Shuming Ma",
        "Dongdong Zhang",
        "Zhi-Hong Deng",
        "Furu Wei",
    ]


def test_authors_look_broken_detects_latex_blob():
    blob = normalize_author_entry(
        "Haiteng Zhao$^1$, Shuming Ma$^2$, Dongdong Zhang$^2$, "
        "Zhi-Hong Deng$^1$, Furu Wei$^2$ $^1$ Peking University"
    )
    assert authors_look_broken([blob]) is True
    assert author_name_looks_broken("Chendi Qian$^*$") is True


def test_authors_look_broken_accepts_clean_records():
    authors = [
        normalize_author_entry("Alice Smith"),
        normalize_author_entry(
            {
                "name": "Bob Jones",
                "orcid": "0000-0001-2345-6789",
                "s2_author_id": "1",
                "s2_url": "https://www.semanticscholar.org/author/1",
            }
        ),
    ]
    assert authors_look_broken(authors) is False


def test_extract_metadata_from_latex_cache_includes_authors(tmp_path):
    latex_dir = tmp_path / "latex"
    latex_dir.mkdir()
    (latex_dir / "expanded.tex").write_text(
        r"""
\title{Example Paper}
\author{Alice Smith \and Bob Jones}
\begin{abstract}
We study graphs.
\end{abstract}
""".strip(),
        encoding="utf-8",
    )

    metadata = _extract_metadata_from_latex_cache(latex_dir)

    assert metadata["title"] == "Example Paper"
    assert metadata["authors"] == ["Alice Smith", "Bob Jones"]


def test_normalize_author_entry_from_string():
    assert normalize_author_entry("Alice") == {
        "name": "Alice",
        "orcid": None,
        "s2_author_id": None,
        "s2_url": None,
    }


def test_normalize_author_entry_from_structured_dict():
    entry = normalize_author_entry(
        {
            "name": "Alice",
            "orcid": "0000-0001-2345-6789",
            "s2_author_id": "123",
            "s2_url": "https://www.semanticscholar.org/author/123",
        }
    )
    assert entry["name"] == "Alice"
    assert entry["orcid"] == "0000-0001-2345-6789"
    assert entry["s2_author_id"] == "123"


def test_paper_authors_property_normalizes_legacy_strings():
    paper = Paper(arxiv_id="1234.56789", title="Test")
    paper.authors = ["Alice", "Bob"]

    assert author_display_name(paper.authors[0]) == "Alice"
    assert paper.authors[1]["name"] == "Bob"
    assert paper.authors[1]["orcid"] is None


def test_fetch_author_external_ids_parses_orcid(monkeypatch):
    monkeypatch.setattr(
        "backend.semantic_scholar._s2_request",
        lambda *_args, **_kwargs: [
            {
                "authorId": "1741101",
                "name": "Alice",
                "url": "https://www.semanticscholar.org/author/1741101",
                "externalIds": {"ORCID": "https://orcid.org/0000-0001-2345-6789"},
            }
        ],
    )

    result = fetch_author_external_ids(["1741101"])

    assert result["1741101"]["orcid"] == "0000-0001-2345-6789"
    assert result["1741101"]["url"] == "https://www.semanticscholar.org/author/1741101"


def test_merge_latex_authors_with_s2_prefers_s2_names(monkeypatch):
    latex_names = ["Alice", "Bob"]
    s2_authors = [
        {"author_id": "1", "name": "Alice"},
        {"author_id": "2", "name": "Bob"},
    ]
    s2_external = {
        "1": {"orcid": "0000-0001-2345-6789", "url": "https://www.semanticscholar.org/author/1"},
        "2": {"orcid": None, "url": "https://www.semanticscholar.org/author/2"},
    }
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_author_external_ids",
        lambda _ids: s2_external,
    )

    merged = merge_latex_authors_with_s2(latex_names, s2_authors, s2_external)

    assert merged[0]["name"] == "Alice"
    assert merged[0]["orcid"] == "0000-0001-2345-6789"
    assert merged[0]["s2_author_id"] == "1"
    assert merged[1]["name"] == "Bob"
    assert merged[1]["orcid"] is None
    assert merged[1]["s2_url"] == "https://www.semanticscholar.org/author/2"


def test_resolve_paper_authors_prefers_s2_over_latex_blob(monkeypatch):
    latex_blob = [
        "Haiteng Zhao$^1$, Shuming Ma$^2$, Dongdong Zhang$^2$, "
        "Zhi-Hong Deng$^1$, Furu Wei$^2$ $^1$ Peking University"
    ]
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_paper_author_ids",
        lambda _arxiv_id: [
            {"author_id": "2146233407", "name": "Haiteng Zhao"},
            {"author_id": "2118866998", "name": "Shuming Ma"},
            {"author_id": "40232931", "name": "Dongdong Zhang"},
            {"author_id": "", "name": "Zhi-Hong Deng"},
            {"author_id": "49807919", "name": "Furu Wei"},
        ],
    )
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_author_external_ids",
        lambda _ids: {
            "2146233407": {
                "orcid": "0000-0001-2345-6789",
                "url": "https://www.semanticscholar.org/author/2146233407",
            }
        },
    )

    authors = resolve_paper_authors("2303.00579", latex_names=latex_blob)

    assert [author["name"] for author in authors] == [
        "Haiteng Zhao",
        "Shuming Ma",
        "Dongdong Zhang",
        "Zhi-Hong Deng",
        "Furu Wei",
    ]
    assert authors[0]["orcid"] == "0000-0001-2345-6789"
    assert authors_look_broken(authors) is False


def test_enrich_paper_metadata_populates_authors_from_latex_and_s2(monkeypatch, tmp_path):
    from backend.config import cfg
    from backend.models import Paper
    from backend.paper_storage import PaperStorage
    from backend.results_parser import _enrich_paper_metadata

    root = tmp_path / "workspace"
    papers_dir = root / "papers"
    papers_dir.mkdir(parents=True)
    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "papers_dir", papers_dir)

    storage = PaperStorage("2407.18480")
    storage.ensure_dirs()
    (storage.latex_dir / "expanded.tex").write_text(
        r"""
\title{Graph Paper}
\author{Alice Smith \and Bob Jones}
\begin{abstract}
We benchmark graph models.
\end{abstract}
""".strip(),
        encoding="utf-8",
    )

    paper = Paper(
        arxiv_id="2407.18480",
        title="Graph Paper",
        abstract="We benchmark graph models.",
    )

    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_paper_author_ids",
        lambda _arxiv_id: [
            {"author_id": "1", "name": "Alice Smith"},
            {"author_id": "2", "name": "Bob Jones"},
        ],
    )
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_author_external_ids",
        lambda _ids: {
            "1": {
                "orcid": "0000-0001-2345-6789",
                "url": "https://www.semanticscholar.org/author/1",
            },
            "2": {"orcid": None, "url": "https://www.semanticscholar.org/author/2"},
        },
    )
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_paper_metadata",
        lambda _arxiv_id: {},
    )

    changed = _enrich_paper_metadata("2407.18480", paper, storage)

    assert changed is True
    assert len(paper.authors) == 2
    assert paper.authors[0]["name"] == "Alice Smith"
    assert paper.authors[0]["orcid"] == "0000-0001-2345-6789"
    assert paper.authors[1]["name"] == "Bob Jones"

    metadata = json.loads(storage.metadata_path.read_text(encoding="utf-8"))
    assert len(metadata["authors"]) == 2


def test_enrich_paper_metadata_repairs_broken_metadata_authors(monkeypatch, tmp_path):
    from backend.config import cfg
    from backend.models import Paper
    from backend.paper_storage import PaperStorage
    from backend.results_parser import _enrich_paper_metadata

    root = tmp_path / "workspace"
    papers_dir = root / "papers"
    papers_dir.mkdir(parents=True)
    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "papers_dir", papers_dir)

    storage = PaperStorage("2303.00579")
    storage.ensure_dirs()
    storage.update_metadata(
        {
            "authors": [
                normalize_author_entry(
                    "Haiteng Zhao$^1$, Shuming Ma$^2$, Dongdong Zhang$^2$, "
                    "Zhi-Hong Deng$^1$, Furu Wei$^2$ $^1$ Peking University"
                )
            ]
        }
    )

    paper = Paper(
        arxiv_id="2303.00579",
        title="Are More Layers Beneficial to Graph Transformers?",
        abstract="Graph transformers.",
    )

    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_paper_author_ids",
        lambda _arxiv_id: [
            {"author_id": "2146233407", "name": "Haiteng Zhao"},
            {"author_id": "2118866998", "name": "Shuming Ma"},
            {"author_id": "40232931", "name": "Dongdong Zhang"},
            {"author_id": "", "name": "Zhi-Hong Deng"},
            {"author_id": "49807919", "name": "Furu Wei"},
        ],
    )
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_author_external_ids",
        lambda _ids: {},
    )
    monkeypatch.setattr(
        "backend.semantic_scholar.fetch_paper_metadata",
        lambda _arxiv_id: {},
    )

    changed = _enrich_paper_metadata("2303.00579", paper, storage)

    assert changed is True
    assert len(paper.authors) == 5
    assert paper.authors[0]["name"] == "Haiteng Zhao"
    assert authors_look_broken(paper.authors) is False
    metadata = json.loads(storage.metadata_path.read_text(encoding="utf-8"))
    assert len(metadata["authors"]) == 5
