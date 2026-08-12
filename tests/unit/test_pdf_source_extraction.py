from pathlib import Path

from experiments.pdf_extraction.run_source_extraction import _load_source


def test_load_source_prefers_explicit_pdf_markdown(tmp_path: Path) -> None:
    markdown = tmp_path / "paper.md"
    markdown.write_text("| Model | Score |", encoding="utf-8")

    text, latex_paper, source = _load_source(
        "2401.00001",
        markdown_path=markdown,
        papers_dir=tmp_path / "papers",
    )

    assert text == "| Model | Score |"
    assert latex_paper is None
    assert source == str(markdown)


def test_load_source_parses_local_expanded_latex(tmp_path: Path) -> None:
    latex_dir = tmp_path / "2401.00001" / "latex"
    latex_dir.mkdir(parents=True)
    expanded = latex_dir / "expanded.tex"
    expanded.write_text(
        r"\begin{table}\begin{tabular}{lc}Model & Score \\ A & 1\end{tabular}\end{table}",
        encoding="utf-8",
    )

    text, latex_paper, source = _load_source(
        "2401.00001",
        markdown_path=None,
        papers_dir=tmp_path,
    )

    assert "Model & Score" in text
    assert latex_paper is not None
    assert len(latex_paper.tables) == 1
    assert source == str(expanded)
