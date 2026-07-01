"""Tests for LaTeX table extraction and diagnostics."""

from __future__ import annotations

from pathlib import Path

from backend.latex_source import (
    TABLE_ENV_NAMES,
    _extract_tables,
    _extract_tables_with_spans,
    diagnose_latex_table_coverage,
)


def test_table_env_names_include_wrap_and_sideways():
    assert "wraptable" in TABLE_ENV_NAMES
    assert "sidewaystable" in TABLE_ENV_NAMES
    assert "sidewaystable*" in TABLE_ENV_NAMES


def test_extract_wraptable_environment():
    tex = r"""
\section{Results}
\begin{wraptable}{r}{5cm}
\caption{LRGB benchmark results.}
\label{tab:lrgb_res}
\begin{tabular}{lcc}
\toprule
Method & Peptides-func & Peptides-struct \\
\midrule
D-GRAND-l & 0.7571 & 0.2461 \\
\bottomrule
\end{tabular}
\end{wraptable}
Body text continues here.
"""
    tables, spans = _extract_tables_with_spans(tex)
    assert len(tables) == 1
    assert spans[0].env_name == "wraptable"
    assert tables[0].label == "tab:lrgb_res"
    assert "Peptides-func" in tables[0].body
    assert "0.7571" in tables[0].body


def test_extract_sidewaystable_environment():
    tex = r"""
\begin{sidewaystable}
\caption{Rotated results}
\label{tab:rot}
\begin{tabular}{lc}
A & B \\
1 & 2 \\
\end{tabular}
\end{sidewaystable}
"""
    tables = _extract_tables(tex)
    assert len(tables) == 1
    assert tables[0].label == "tab:rot"


def test_diagnose_flags_wraptable_for_reextract():
    tex = r"\begin{wraptable}{r}{5cm}\caption{x}\begin{tabular}{cc}a&b\\c&d\end{tabular}\end{wraptable}"
    issues = diagnose_latex_table_coverage(tex)
    kinds = {item.kind for item in issues}
    assert "wraptable" in kinds


def test_diagnose_unparsed_tabular_lines_outside_table_env():
    tex = r"""
\begin{table}
\caption{Node classification}
\begin{tabular}{lcc}
Method & Cora & Citeseer \\
\midrule
GCN & 0.81 & 0.71 \\
\end{tabular}
\end{table}

Standalone layout not wrapped in a table environment:
\begin{tabular}{lcc}
Model & Peptides-func & Peptides-struct \\
D-GRAND-l & 0.7571 & 0.2461 \\
\end{tabular}
"""
    issues = diagnose_latex_table_coverage(tex)
    kinds = {item.kind for item in issues}
    assert "unparsed_tabular_lines" in kinds
    unparsed = next(item for item in issues if item.kind == "unparsed_tabular_lines")
    assert unparsed.sample_lines
    assert "Peptides-func" in unparsed.sample_lines[0]


def test_dragon_paper_parses_lrgb_wraptable():
    tex_path = Path("papers/2411.05274/latex/expanded.tex")
    if not tex_path.is_file():
        return
    tex = tex_path.read_text(encoding="utf-8", errors="replace")
    tables, spans = _extract_tables_with_spans(tex)
    labels = {table.label for table in tables}
    assert "tab:lrgb_res" in labels
    assert any(span.env_name == "wraptable" for span in spans)
