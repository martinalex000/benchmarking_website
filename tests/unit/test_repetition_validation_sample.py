from experiments.table_provenance_experiment.compile_manual_validation import coverage_markdown
from experiments.table_provenance_experiment.prepare_manual_validation import select_holdout


def test_holdout_is_seeded_order_independent_and_excludes_previous_or_missing_pdf(tmp_path):
    papers = []
    for index in range(15):
        folder = tmp_path / str(index) / "latex"
        folder.mkdir(parents=True)
        if index != 14:
            (folder.parent / "paper.pdf").touch()
        papers.append({"paper_id": str(index), "path": folder / "expanded.tex"})
    pool, sample = select_holdout(papers, {"0", "1"}, 20261006)
    reversed_pool, reversed_sample = select_holdout(list(reversed(papers)), {"0", "1"}, 20261006)
    assert pool == reversed_pool
    assert sample == reversed_sample
    assert len(pool) == 12
    assert len({p["paper_id"] for p in sample}) == 10
    assert not {"0", "1", "14"} & {p["paper_id"] for p in sample}


def test_coverage_diagnostic_is_readable_markdown_not_json():
    lines = coverage_markdown(
        {
            "missing_table_ids": [2, 4],
            "unexpected_table_ids": [],
            "benchmark_tables_without_proposed_entry": [3],
        }
    )
    assert lines == [
        "- Tables missing from the model output: 2, 4",
        "- Model table IDs absent from the source inventory: none",
        "- Benchmark tables missing the proposed method: 3",
    ]
