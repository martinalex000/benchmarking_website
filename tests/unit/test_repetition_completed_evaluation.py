from experiments.table_provenance_experiment.evaluate_completed_runs import (
    corrected_cases,
    human_comments,
)


def test_split_policy_correction_preserves_original_gold_and_official_split_case():
    original = {"2012.07437": {"counts": {"1": 5, "2": 10}}}
    revised = corrected_cases(original)
    assert original["2012.07437"]["counts"] == {"1": 5, "2": 10}
    assert revised["2012.07437"]["counts"] == {"1": None, "2": 10}


def test_human_comments_are_read_without_changing_their_text():
    text = (
        "# Review\n\n## 1234.56789 — Test paper\n\n### Findings\n\nCandidate count.\n"
        "\n### Your validation\n\nTen splits, NOT ten seeds.\n\n---\n"
    )
    assert human_comments(text) == {"1234.56789": "Ten splits, NOT ten seeds."}
