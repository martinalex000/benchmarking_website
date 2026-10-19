"""Experiment eligibility is based on result rows, not the old paper list."""

import sqlite3

from experiments.table_provenance_experiment.run_proposed_metadata import eligible_papers


def test_only_result_tracked_non_attack_papers_with_source_are_eligible(tmp_path):
    database = tmp_path / "cohort.db"
    with sqlite3.connect(database) as connection:
        connection.executescript(
            "CREATE TABLE papers(id INTEGER, arxiv_id TEXT, title TEXT, abstract TEXT);"
            "CREATE TABLE results(id INTEGER, paper_id INTEGER);"
            "INSERT INTO papers VALUES(1,'2301.00001','Graph learning','');"
            "INSERT INTO papers VALUES(2,'2301.00002','Adversarial examples on graphs','');"
            "INSERT INTO papers VALUES(3,'2301.00003','Untracked model','');"
            "INSERT INTO results VALUES(1,1); INSERT INTO results VALUES(2,2);"
        )
    for paper_id in ("2301.00001", "2301.00002", "2301.00003"):
        folder = tmp_path / "papers" / paper_id / "latex"
        folder.mkdir(parents=True)
        (folder / "expanded.tex").write_text(r"\begin{table}\caption{Benchmark}\end{table}")
    before = database.read_bytes()
    eligible = eligible_papers(database, tmp_path / "papers")
    assert [p["paper_id"] for p in eligible] == ["2301.00001"]
    assert database.read_bytes() == before
