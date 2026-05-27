"""Focused regression tests for export helper behavior."""

import pytest

from backend.export_to_hugo import (
    _description_class_target_count,
    _has_paper_value_difference,
    _has_paper_value_gap,
    _plain_model,
    _rank_for_value,
    _sanitize_model,
    _sanitize_title,
    _truncate_words,
)


def test_sanitize_title_replaces_linebreaks_and_strips_commands():
    title = "Graph\\\\Learning \\emph{for} Molecules"

    assert _sanitize_title(title) == "Graph - Learning Molecules"


def test_truncate_words_uses_sanitized_title():
    title = "Graph\\\\Learning for Molecules and Materials"

    assert _truncate_words(title, 3) == "Graph - Learning..."


def test_sanitize_model_formats_subscripts_and_superscripts():
    model = "GNN$_{L}$ / Net\\textsubscript{small} / Model$^{2}$ / Deep\\textsuperscript{xl} ~\\cite{foo} (ours)"

    assert _sanitize_model(model) == (
        "GNN<sub>L</sub> / Net<sub>small</sub> / Model<sup>2</sup> / Deep<sup>xl</sup>"
    )
    assert _plain_model(_sanitize_model(model)) == "GNNL / Netsmall / Model2 / Deepxl"


def test_value_gap_respects_reported_uncertainty():
    assert _has_paper_value_gap(0.81, None, 0.8, None)
    assert not _has_paper_value_gap(0.81, 0.02, 0.8, None)
    assert not _has_paper_value_gap(0.81, None, 0.8, 0.02)
    assert not _has_paper_value_gap(None, None, 0.8, None)
    assert _has_paper_value_difference(0.81, 0.8)
    assert not _has_paper_value_difference(0.8, 0.8 + 1e-13)


def test_rank_for_value_replaces_existing_model_and_inserts_new_one():
    rows = [
        {"model_key": "gcn", "value": 0.8},
        {"model_key": "gin", "value": 0.75},
    ]

    assert _rank_for_value(rows, "gcn", 0.7, higher_is_better=True) == 2
    assert _rank_for_value(rows, "sage", 0.77, higher_is_better=True) == 2
    assert _rank_for_value(rows, "gin", 0.85, higher_is_better=True) == 1
    assert _rank_for_value(rows, "mae-model", 0.09, higher_is_better=False) == 1
    assert _rank_for_value(rows, "", 0.7, higher_is_better=True) is None


@pytest.mark.parametrize(
    ("description", "expected"),
    [
        ("Node classification on arXiv citation network (40 subject areas).", 40),
        ("Node classification on Amazon product co-purchase graph (47 categories).", 47),
        ("Protein-protein interaction node classification (121 GO labels, multi-label).", 121),
        ("Multi-task graph regression on peptide structural properties (11 targets).", 11),
        ("Analog circuit topology design across 3 circuit-size datasets.", None),
    ],
)
def test_description_class_target_count_extracts_only_relevant_summary_counts(
    description, expected
):
    assert _description_class_target_count(description) == expected
