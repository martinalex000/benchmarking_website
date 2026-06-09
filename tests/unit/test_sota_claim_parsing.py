"""Tests for SOTA claim prose scoping and precheck."""

from __future__ import annotations

from backend.latex_source import LatexPaper, LatexSection
from backend.sota_claim_parsing import (
    main_body_prose_text,
    merge_claim_dicts,
    text_has_sota_markers,
)


def test_main_body_prose_text_truncates_before_appendix_for_latex():
    latex_paper = LatexPaper(
        arxiv_id="1234.5678",
        main_tex=(
            "\\section{Intro}\nWe achieve state-of-the-art results.\n"
            "\\appendix\n\\section{Extra}\nAppendix SOTA claim."
        ),
        sections=[
            LatexSection(level="section", title="Intro", content="We achieve state-of-the-art."),
            LatexSection(
                level="section",
                title="Extra",
                content="Appendix SOTA claim.",
                in_appendix=True,
            ),
        ],
    )
    prose = main_body_prose_text(paper_text="", latex_paper=latex_paper)
    assert "state-of-the-art" in prose.lower()
    assert "appendix sota" not in prose.lower()


def test_main_body_prose_text_strips_table_environments():
    latex_paper = LatexPaper(
        arxiv_id="1234.5678",
        main_tex=(
            "\\section{Results}\n"
            "Our method sets a new record.\n"
            "\\begin{table}\n\\caption{Results}\n1 & 2\n\\end{table}\n"
        ),
        sections=[
            LatexSection(
                level="section",
                title="Results",
                content=(
                    "Our method sets a new record.\n"
                    "\\begin{table}\n\\caption{Results}\n1 & 2\n\\end{table}\n"
                ),
            )
        ],
    )
    prose = main_body_prose_text(paper_text="", latex_paper=latex_paper)
    assert "new record" in prose.lower()
    assert "begin{table}" not in prose


def test_main_body_prose_text_plain_text_appendix_heading():
    paper_text = (
        "Abstract\nWe report state-of-the-art performance on Cora.\n\n"
        "Appendix A\nAdditional ablation SOTA claims."
    )
    prose = main_body_prose_text(paper_text=paper_text, latex_paper=None)
    assert "state-of-the-art" in prose.lower()
    assert "ablation sota" not in prose.lower()


def test_text_has_sota_markers():
    assert text_has_sota_markers("This method achieves state-of-the-art results.")
    assert not text_has_sota_markers("We evaluate on several benchmark datasets.")


def test_merge_claim_dicts_deduplicates_verbatim_sentences():
    merged = merge_claim_dicts(
        [
            {"raw_sentence": "We achieve SOTA on Cora."},
            {"raw_sentence": "We achieve SOTA on Cora."},
            {"raw_sentence": "We also set a new best on Citeseer."},
        ]
    )
    assert len(merged) == 2
