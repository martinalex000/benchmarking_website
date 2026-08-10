import json
import sqlite3
from pathlib import Path

from backend.arxiv_metadata_analysis import (
    ScreeningConfig,
    analyze_snapshot,
    classify_record,
    merge_reports,
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


def test_equivariance_is_not_a_keyword_family_and_ml_categories_are_equivalent():
    config = _config()
    matcher = config.matcher()
    assert (
        matcher.match_tier(
            "Equivariance in geometric models",
            "",
        )
        is None
    )
    assert "equivariance" not in {family.name for family in config.keyword_families}

    records = [
        {"id": "2401.00001", "title": "A GCN benchmark", "categories": "cs.LG"},
        {"id": "2401.00002", "title": "A GCN benchmark", "categories": "stat.ML"},
    ]
    assert all(classify_record(record, config).keyword_union for record in records)


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


def test_reports_omit_categories_and_keyword_families_without_matches(tmp_path):
    snapshot = tmp_path / "snapshot.json"
    snapshot.write_text(
        json.dumps({"id": "2401.00001", "title": "A GCN benchmark", "categories": "cs.LG"})
        + "\n"
        + json.dumps({"id": "2401.00002", "title": "Unrelated paper", "categories": "stat.ML"})
        + "\n"
    )
    database = tmp_path / "benchmarks.db"
    with sqlite3.connect(database) as connection:
        connection.executescript(
            """
            CREATE TABLE papers (id INTEGER PRIMARY KEY, arxiv_id TEXT, title TEXT, abstract TEXT);
            CREATE TABLE results (id INTEGER PRIMARY KEY, paper_id INTEGER);
            """
        )

    report = analyze_snapshot(snapshot, database, _config())
    assert set(report["category_counts"]) == {"cs.LG"}
    assert set(report["category_keyword_counts"]["cs.LG"]["primary"]["keywords"]) == {"gcn"}
    assert "stat.ML" not in report["category_keyword_counts"]


def test_merge_reports_combines_chunk_statistics(tmp_path):
    config = _config()
    database = tmp_path / "benchmarks.db"
    with sqlite3.connect(database) as connection:
        connection.executescript(
            """
            CREATE TABLE papers (id INTEGER PRIMARY KEY, arxiv_id TEXT, title TEXT, abstract TEXT);
            CREATE TABLE results (id INTEGER PRIMARY KEY, paper_id INTEGER);
            INSERT INTO papers VALUES (1, '2401.00001', 'GCN', '');
            INSERT INTO papers VALUES (2, '2401.00002', 'GIN', '');
            INSERT INTO results VALUES (1, 1);
            INSERT INTO results VALUES (2, 2);
            """
        )

    reports_dir = tmp_path / "chunks"
    chunk_paths = []
    for index, arxiv_id in enumerate(("2401.00001", "2401.00002"), 1):
        snapshot = tmp_path / f"chunk-{index}.json"
        snapshot.write_text(
            json.dumps(
                {"id": arxiv_id, "title": "GCN" if index == 1 else "GIN", "categories": "cs.LG"}
            )
            + "\n"
        )
        chunk_dir = reports_dir / f"part-{index:03d}"
        report = analyze_snapshot(snapshot, database, config)
        chunk_dir.mkdir(parents=True)
        path = chunk_dir / "report.json"
        path.write_text(json.dumps(report))
        chunk_paths.append(path)

    merged = merge_reports(chunk_paths, tmp_path / "merged", config)
    assert merged["corpus"]["records"] == 2
    assert merged["known_results_recall"]["snapshot_present"] == 2
    assert merged["category_counts"]["cs.LG"]["primary"] == 2
