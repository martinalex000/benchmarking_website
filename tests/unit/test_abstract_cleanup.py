"""Regression tests for abstract cleaning and metadata refresh."""

from __future__ import annotations

import json
from pathlib import Path

from backend.config import cfg
from backend.llm_extractor import _extract_metadata_from_latex_cache
from backend.models import Paper
from backend.paper_storage import PaperStorage
from backend.results_parser import _enrich_paper_metadata
from backend.text_cleanup import abstract_has_latex_artifacts, clean_extracted_text


def _configure_temp_workspace(monkeypatch, tmp_path: Path) -> None:
    root = tmp_path / "workspace"
    data_dir = root / "data"
    papers_dir = root / "papers"
    logs_dir = root / "logs"
    site_dir = root / "site"
    config_dir = root / "config"

    for directory in (data_dir, papers_dir, logs_dir, site_dir, config_dir):
        directory.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "data_dir", data_dir)
    monkeypatch.setattr(cfg, "papers_dir", papers_dir)
    monkeypatch.setattr(cfg, "logs_dir", logs_dir)
    monkeypatch.setattr(cfg, "site_dir", site_dir)
    monkeypatch.setattr(cfg, "config_dir", config_dir)
    monkeypatch.setattr(cfg, "db_path", data_dir / "benchmarks.db")


def test_extract_metadata_from_latex_cache_cleans_common_artifacts(tmp_path):
    latex_dir = tmp_path / "latex"
    latex_dir.mkdir()
    (latex_dir / "expanded.tex").write_text(
        r"""
\newcommand{\Method}{\textsc{CoCN}\xspace}
\title{Scalable Graph Compressed Convolutions}
\begin{abstract}
Designing effective graph neural networks~(GNNs) is challenging.
We call our approach \Method~and release code at~https://example.com.
\end{abstract}
""".strip(),
        encoding="utf-8",
    )

    metadata = _extract_metadata_from_latex_cache(latex_dir)

    assert metadata["title"] == "Scalable Graph Compressed Convolutions"
    assert metadata["abstract"] == (
        "Designing effective graph neural networks (GNNs) is challenging. "
        "We call our approach CoCN and release code at https://example.com."
    )


def test_enrich_paper_metadata_reextracts_when_abstract_has_tilde_artifacts(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)

    storage = PaperStorage("2407.18480")
    storage.ensure_dirs()
    storage.metadata_path.write_text(
        json.dumps(
            {
                "title": "Scalable Graph Compressed Convolutions",
                "abstract": "Designing effective graph neural networks~(GNNs) is hard.",
            }
        ),
        encoding="utf-8",
    )
    (storage.latex_dir / "expanded.tex").write_text(
        r"""
\newcommand{\Method}{\textsc{CoCN}\xspace}
\title{Scalable Graph Compressed Convolutions}
\begin{abstract}
Designing effective graph neural networks~(GNNs) is challenging.
\Method~learns Euclidean-style convolutions on graphs.
\end{abstract}
""".strip(),
        encoding="utf-8",
    )

    paper = Paper(
        arxiv_id="2407.18480",
        title="Scalable Graph Compressed Convolutions",
        abstract="Designing effective graph neural networks~(GNNs) is hard.",
    )

    changed = _enrich_paper_metadata("2407.18480", paper, storage)

    assert changed is True
    assert "~" not in paper.abstract
    assert paper.abstract == (
        "Designing effective graph neural networks (GNNs) is challenging. "
        "CoCN learns Euclidean-style convolutions on graphs."
    )


def test_clean_extracted_text_removes_inline_latex_formatting():
    cleaned = clean_extracted_text(
        r"GQT (\textbf{G}raph \textbf{Q}uantized \textbf{T}okenizer) applies \textit{curvature shift} and improves by 82.47\% over a 10\times range."
    )

    assert cleaned == (
        "GQT (Graph Quantized Tokenizer) applies curvature shift and improves by "
        "82.47% over a 10 x range."
    )
    assert abstract_has_latex_artifacts(cleaned) is False
