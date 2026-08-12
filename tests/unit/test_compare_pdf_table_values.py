from pathlib import Path

from experiments.pdf_extraction.compare_table_values import (
    _numbers,
    compare,
    markdown_tables,
)


def test_markdown_tables_requires_separator_row() -> None:
    markdown = """
| Model | Score |
|---|---:|
| GNN | 91.00 |

Prose | with a pipe
"""

    assert markdown_tables(markdown) == [
        ["| Model | Score |", "|---|---:|", "| GNN | 91.00 |"]
    ]


def test_numbers_normalizes_decimal_spelling_but_preserves_percent_scale() -> None:
    assert _numbers("91.00, 0.9100, +1,000 and 91%") == {
        "91": 1,
        "0.91": 1,
        "1000": 1,
        "91%": 1,
    }


def test_compare_counts_duplicate_numeric_values(tmp_path: Path) -> None:
    expanded = tmp_path / "expanded.tex"
    expanded.write_text(
        r"""
\begin{table}
\begin{tabular}{lc}
Model & Score \\
A & 91.0 \\
B & 91.0 \\
\end{tabular}
\caption{Results}
\end{table}
""",
        encoding="utf-8",
    )
    markdown = tmp_path / "paper.md"
    markdown.write_text(
        "| Model | Score |\n|---|---:|\n| A | 91 |\n",
        encoding="utf-8",
    )

    stats = compare("test", expanded, markdown)

    assert stats.reference_tables == 1
    assert stats.candidate_tables == 1
    assert stats.reference_values == 2
    assert stats.candidate_values == 1
    assert stats.matched_values == 1
    assert stats.recall == 0.5
    assert stats.precision == 1.0
