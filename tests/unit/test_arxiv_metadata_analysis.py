import json
import sqlite3
from pathlib import Path

from backend.arxiv_metadata_analysis import (
    ScreeningConfig,
    analyze_snapshot,
    classify_record,
    write_reports,
)


def _config() -> ScreeningConfig:
    return ScreeningConfig.load(Path("config/arxiv_screening.yaml"))


def test_classify_record_matches_title_and_hyphenated_abstract_terms():
    result = classify_record(
        {
            "id": "arXiv:2401.00001v2",
            "title": "A Graph Transformer",
            "abstract": "We use message-passing neural networks for node-classification.",
            "categories": "cs.LG cs.AI",
            "versions": [{"created": "Thu, 04 Jan 2024 12:00:00 GMT"}],
        },
        _config(),
    )

    assert result.arxiv_id == "2401.00001"
    assert result.categories == ("cs.LG", "cs.AI")
    assert result.date == "2024-01-04"
    assert result.keyword_union
    assert result.family_matches["graph_transformer"] == (True, False)
    assert result.family_matches["message_passing"] == (False, True)
    assert result.family_matches["node_tasks"] == (False, True)


def test_analyze_snapshot_audits_known_result_papers(tmp_path):
    snapshot = tmp_path / "snapshot.json"
    records = [
        {
            "id": "2401.00001",
            "title": "Graph learning",
            "abstract": "A benchmark with GNNs.",
            "categories": "cs.LG cs.AI",
            "versions": [{"created": "Thu, 04 Jan 2024 12:00:00 GMT"}],
        },
        {
            "id": "2401.00002",
            "title": "A statistics paper",
            "abstract": "No relevant terms here.",
            "categories": "stat.ML",
            "versions": [{"created": "Fri, 05 Jan 2024 12:00:00 GMT"}],
        },
    ]
    snapshot.write_text("\n".join(json.dumps(record) for record in records) + "\n")

    database = tmp_path / "benchmarks.db"
    with sqlite3.connect(database) as connection:
        connection.executescript("""
            CREATE TABLE papers (id INTEGER PRIMARY KEY, arxiv_id TEXT, title TEXT, abstract TEXT);
            CREATE TABLE results (id INTEGER PRIMARY KEY, paper_id INTEGER);
            INSERT INTO papers VALUES (1, '2401.00001', 'Graph learning', 'A benchmark with GNNs.');
            INSERT INTO papers VALUES (2, '2401.00002', 'A statistics paper', 'No relevant terms here.');
            INSERT INTO papers VALUES (3, '2401.00003', 'Missing paper', 'Graph learning.');
            INSERT INTO results VALUES (1, 1);
            INSERT INTO results VALUES (2, 2);
            INSERT INTO results VALUES (3, 3);
            """)

    report = analyze_snapshot(snapshot, database, _config())
    recall = report["known_results_recall"]
    assert report["corpus"]["records"] == 2
    assert recall["database_papers"] == 3
    assert recall["snapshot_present"] == 2
    assert recall["snapshot_missing"] == 1
    assert recall["combined_prefilter"] == 1
    assert report["snapshot_missing_known_ids"] == ["2401.00003"]

    output = tmp_path / "reports"
    write_reports(report, output, _config())
    assert (output / "summary.md").exists()
    assert (output / "category_keyword_counts.csv").exists()
    assert (output / "known_results_audit.csv").exists()
    assert (output / "known_results_misses.csv").read_text().count("missing_from_snapshot") == 1
