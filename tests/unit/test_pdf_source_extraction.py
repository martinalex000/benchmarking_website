from pathlib import Path

from experiments.pdf_extraction.run_source_extraction import _load_source, parse_markdown_tables


def test_load_source_prefers_explicit_pdf_markdown(tmp_path: Path) -> None:
    markdown = tmp_path / "paper.md"
    markdown.write_text("| Model | Score |", encoding="utf-8")

    text, latex_paper, tables, source = _load_source(
        "2401.00001",
        markdown_path=markdown,
        papers_dir=tmp_path / "papers",
    )

    assert text == "| Model | Score |"
    assert latex_paper is None
    assert tables == []
    assert source == str(markdown)


def test_load_source_parses_local_expanded_latex(tmp_path: Path) -> None:
    latex_dir = tmp_path / "2401.00001" / "latex"
    latex_dir.mkdir(parents=True)
    expanded = latex_dir / "expanded.tex"
    expanded.write_text(
        r"\begin{table}\begin{tabular}{lc}Model & Score \\ A & 1\end{tabular}\end{table}",
        encoding="utf-8",
    )

    text, latex_paper, tables, source = _load_source(
        "2401.00001",
        markdown_path=None,
        papers_dir=tmp_path,
    )

    assert "Model & Score" in text
    assert latex_paper is not None
    assert len(latex_paper.tables) == 1
    assert tables == []
    assert source == str(expanded)


def test_parse_markdown_tables_uses_nearby_caption() -> None:
    text = """Some prose.

Table 7. Results on Cora.

| Model | Accuracy |
|:------|---------:|
| Ours  | 91.2     |
"""

    tables = parse_markdown_tables(text)

    assert len(tables) == 1
    assert tables[0].number == 7
    assert tables[0].caption == "Results on Cora."
    assert tables[0].header == "| Model | Accuracy |"
    assert "| Ours  | 91.2" in tables[0].markdown


def test_parse_markdown_tables_numbers_uncaptioned_tables_sequentially() -> None:
    text = """| Model | Score |
|-------|-------|
| GCN   | 0.8   |
"""

    tables = parse_markdown_tables(text)

    assert tables[0].number == 1
    assert tables[0].caption == ""
