from pathlib import Path

import pytest

from backend.latex_source import (
    _find_appendix_start,
    _parse_expanded,
    _strip_comment_environments,
)


def test_strip_comment_environment_removes_only_balanced_standalone_block():
    source = (
        "before\n"
        "\\begin{comment}\n"
        "\\begin{table}\n"
        "\\caption{Dead table}\n"
        "\\end{table}\n"
        "\\end{comment}\n"
        "after\n"
    )

    assert _strip_comment_environments(source) == "before\nafter\n"


def test_strip_comment_environment_preserves_unbalanced_block():
    source = "before\n\\begin{comment}\nkeep this content\n"

    assert _strip_comment_environments(source) == source


def test_strip_comment_environment_does_not_remove_inline_markers():
    source = "before \\begin{comment}\nkeep this content\n\\end{comment}\nafter\n"

    assert _strip_comment_environments(source) == source


def test_strip_comment_environment_preserves_text_after_whitespace_end_marker():
    source = "\\begin{comment}\nremove this content\n\\end{comment} \\section{Kept}\n"

    assert _strip_comment_environments(source) == " \\section{Kept}\n"


@pytest.mark.parametrize(
    "heading",
    [
        "\\appendix\n",
        "\\section{Appendix: Additional Results}\n",
        "\\section*{Supplement}\n",
        "\\section{Supplementary Material}\n",
    ],
)
def test_find_appendix_start_recognizes_directives_and_headings(heading: str):
    source = "\\section{Results}\nmain\n" + heading + "appendix\n"

    boundary = _find_appendix_start(source)

    assert boundary == source.index(heading)


def test_find_appendix_start_ignores_prose_references():
    source = "We refer to Appendix~\\ref{app:results}.\n\\section{Results}\n"

    assert _find_appendix_start(source) == len(source)


def test_parse_expanded_marks_heading_based_appendix_tables():
    source = r"""
\section{Results}
\begin{table}
\caption{Main results}
\begin{tabular}{c}1\\\end{tabular}
\end{table}
\section{Appendix: Detailed Results}
\begin{table}
\caption{Appendix results}
\begin{tabular}{c}2\\\end{tabular}
\end{table}
"""

    paper = _parse_expanded("1234.5678", source)

    assert [table.in_appendix for table in paper.tables] == [False, True]
    assert [section.in_appendix for section in paper.sections] == [False, True]


def test_table_selection_prompts_keep_appendix_benchmark_tables_in_scope():
    prompt_dir = Path(__file__).parents[2] / "config" / "prompts"

    for filename in ("table_selection.txt", "table_selection_multi.txt"):
        prompt = (prompt_dir / filename).read_text(encoding="utf-8").lower()
        assert "appendix benchmark tables are first-class sources" in prompt
        assert "do not exclude or deprioritize" in prompt
