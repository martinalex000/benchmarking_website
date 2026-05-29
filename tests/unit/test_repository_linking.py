from __future__ import annotations

from pathlib import Path

from backend.paper_storage import PaperStorage
from backend.repository_linking import (
    extract_github_repo_candidates,
    extract_repository_candidates,
    find_verified_repository_link,
    repository_source_from_storage,
)


class _FakeVerifier:
    model_name = "fake-small"

    @staticmethod
    def _read_prompt(_filename: str) -> str:
        return "prompt"

    def _call_json(self, _prompt: str, user_content: str, **_kwargs):
        if "https://github.com/example/project" in user_content:
            return {
                "belongs_to_paper": True,
                "confidence": 0.93,
                "reason": "README explicitly says this repository is the official implementation of the paper.",
                "evidence": ["README references the exact paper title."],
            }
        return {
            "belongs_to_paper": False,
            "confidence": 0.12,
            "reason": "README does not connect the repository to the paper.",
            "evidence": [],
        }


def test_extract_github_repo_candidates_normalizes_and_scores_context():
    text = r"""
    Our code is available at \href{https://github.com/example/project/tree/main}{GitHub}.
    We also compare against baseline code from https://github.com/other/baseline/blob/main/README.md.
    """

    candidates = extract_github_repo_candidates(text)

    assert [candidate["url"] for candidate in candidates] == [
        "https://github.com/example/project",
        "https://github.com/other/baseline",
    ]
    assert "Our code is available" in candidates[0]["paper_context"]


def test_extract_repository_candidates_keeps_non_github_project_links():
    text = """
    The official code is available at https://gitlab.com/example/project and
    the project page is https://example.org/my-method/code .
    """

    candidates = extract_repository_candidates(text)

    assert candidates[0]["url"] == "https://gitlab.com/example/project"
    assert "https://example.org/my-method/code" in [candidate["url"] for candidate in candidates]


def test_find_verified_repository_link_checks_readme(monkeypatch):
    monkeypatch.setattr(
        "backend.repository_linking.fetch_repository_profile",
        lambda url: {"normalized_url": url, "description": "Official implementation."},
    )
    monkeypatch.setattr(
        "backend.repository_linking.fetch_repository_evidence",
        lambda url: {
            "path": "README.md",
            "text": (
                "Official implementation for Invariant-Based Diagnostics for Graph Benchmarks.\n"
                f"Repo: {url}"
            ),
            "evidence_kind": "readme",
        },
    )

    result = find_verified_repository_link(
        llm_verifier=_FakeVerifier(),
        arxiv_id="2605.06462",
        paper_title="Invariant-Based Diagnostics for Graph Benchmarks",
        paper_abstract="We propose invariant baselines for graph benchmarks.",
        source_text="Code: https://github.com/example/project",
        source_kind="latex",
    )

    assert result["verified_url"] == "https://github.com/example/project"
    assert result["confidence"] == 0.93
    assert result["verification_model"] == "fake-small"


def test_find_verified_repository_link_uses_heuristics_without_llm(monkeypatch):
    monkeypatch.setattr(
        "backend.repository_linking.fetch_repository_profile",
        lambda url: {"normalized_url": url, "description": "Official implementation of FloydNet."},
    )
    monkeypatch.setattr(
        "backend.repository_linking.fetch_repository_evidence",
        lambda url: {
            "path": "page",
            "text": "FloydNet official implementation for the paper FloydNet: A Learning Paradigm for Global Relational Reasoning",
            "evidence_kind": "page",
            "normalized_url": url,
        },
    )

    result = find_verified_repository_link(
        llm_verifier=None,
        arxiv_id="2601.19094",
        paper_title="FloydNet: A Learning Paradigm for Global Relational Reasoning",
        paper_abstract="We propose FloydNet for global relational reasoning.",
        source_text="Our code is available at https://gitlab.com/example/floydnet",
        source_kind="latex",
    )

    assert result["verified_url"] == "https://gitlab.com/example/floydnet"
    assert result["confidence"] >= 0.65


def test_repository_source_from_storage_prefers_latex(tmp_path: Path):
    storage = PaperStorage("2401.17791", papers_root=tmp_path / "papers")
    storage.ensure_dirs()
    (storage.latex_dir / "expanded.tex").write_text(
        "https://github.com/example/project", encoding="utf-8"
    )
    storage.text_path.write_text("https://github.com/example/other", encoding="utf-8")

    source_text, source_kind = repository_source_from_storage(storage)

    assert source_kind == "latex"
    assert "example/project" in source_text
