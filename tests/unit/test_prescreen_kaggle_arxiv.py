"""Tests for the resumable Kaggle arXiv pre-screening CLI."""

from __future__ import annotations

import json
import os
from pathlib import Path

import yaml

from backend import arxiv_scanner
from backend.llm_extractor import ScreenResult
from scripts import prescreen_kaggle_arxiv as scanner


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def _write_keywords(path: Path) -> None:
    path.write_text("specific_keywords:\n  - graph neural network\n  - gnn\n", encoding="utf-8")


def test_match_tier_prefers_specific_and_uses_whole_word_graph():
    patterns = scanner.compile_keyword_patterns(["graph neural network", "gnn"])

    assert scanner.match_tier("A GNN Method", "", patterns) == ("specific", ["gnn"])
    assert scanner.match_tier("Graphical models", "A paragraph.", patterns) is None
    assert scanner.match_tier("A graph method", "", patterns) == ("graph", ["graph"])
    assert scanner.match_tier("GNN and graph\nneural network", "", patterns) == (
        "specific",
        ["gnn", "graph neural network"],
    )


def test_source_fingerprint_ignores_mtime_when_content_is_unchanged(tmp_path):
    source = tmp_path / "source.json"
    source.write_text('{"id":"2401.00001"}\n', encoding="utf-8")
    keywords = ["gnn"]
    first = scanner._source_fingerprint(source, keywords)

    stat = source.stat()
    os.utime(source, ns=(stat.st_atime_ns, stat.st_mtime_ns + 10_000_000))

    assert scanner._source_fingerprint(source, keywords) == first


def test_processing_bucket_prioritizes_cross_listed_cs_lg():
    assert scanner.processing_bucket("cs.AI cs.LG") == "cs.LG"
    assert scanner.processing_bucket("stat.ML cs.AI") == "stat.ML"
    assert scanner.processing_bucket("") == "uncategorized"


def test_existing_arxiv_scanner_preserves_prompt_notes(monkeypatch):
    result = arxiv_scanner.ScanResult(arxiv_id="2401.00001", title="Paper", abstract="Text")
    monkeypatch.setattr(
        arxiv_scanner,
        "_call_llm",
        lambda *_args: {
            "has_benchmark_results": False,
            "has_new_benchmark": False,
            "confidence": 0.7,
            "notes": "No graph-learning experiments.",
        },
    )

    assert arxiv_scanner.stage2_benchmark_check(result, object(), "model", "prompt") is False
    assert result.stage2_reason == "No graph-learning experiments."


def test_work_queue_orders_tiers_and_categories(tmp_path):
    source = tmp_path / "source.json"
    keywords = ["gnn"]
    _write_jsonl(
        source,
        [
            {"id": "1", "title": "GNN", "abstract": "", "categories": "stat.ML"},
            {"id": "2", "title": "a graph", "abstract": "", "categories": "cs.LG"},
            {"id": "3", "title": "GNN", "abstract": "", "categories": "cs.AI cs.LG"},
            {"id": "4", "title": "a graph", "abstract": "", "categories": "cs.AI"},
        ],
    )
    queue = scanner.WorkQueue(tmp_path / "queue.sqlite3")
    try:
        queue.rebuild(
            source,
            scanner.compile_keyword_patterns(keywords),
            scanner._source_fingerprint(source, keywords),
        )

        assert queue.buckets() == [
            ("specific", "cs.LG"),
            ("specific", "stat.ML"),
            ("graph", "cs.LG"),
            ("graph", "cs.AI"),
        ]
        assert queue.remaining_breakdown() == {
            ("specific", "cs.LG"): 1,
            ("specific", "other"): 1,
            ("graph", "cs.LG"): 1,
            ("graph", "other"): 1,
        }
    finally:
        queue.close()


def test_minimal_yaml_round_trip_and_trailing_document_recovery(tmp_path):
    output = tmp_path / "screening" / "results.yaml"
    item = scanner.WorkItem("2401.00001", "title", "abstract", "specific", ["gnn"])
    result = ScreenResult(
        has_benchmark_results=True,
        datasets_mentioned=["Cora"],
        confidence=0.9,
        notes="Reports graph benchmark results.",
    )

    scanner.append_result(output, item, result, "fast-model")
    with output.open("a", encoding="utf-8") as result_file:
        result_file.write("---\narxiv_id: 2401.00002\ndecision:")

    summary = scanner.load_results(output)
    documents = list(yaml.safe_load_all(output.read_text(encoding="utf-8")))

    assert summary.arxiv_ids == {"2401.00001"}
    assert summary.accepted == 1
    assert documents == [
        {
            "schema_version": 1,
            "arxiv_id": "2401.00001",
            "matched_tier": "specific",
            "matched_keywords": ["gnn"],
            "decision": "accepted",
            "has_benchmark_results": True,
            "has_new_benchmark": False,
            "datasets_mentioned": ["Cora"],
            "confidence": 0.9,
            "reason": "Reports graph benchmark results.",
            "model": "fast-model",
            "screened_at": documents[0]["screened_at"],
        }
    ]
    assert "title" not in documents[0]
    assert "abstract" not in documents[0]


def test_run_screening_resumes_and_keeps_errors_retryable(monkeypatch, tmp_path):
    source = tmp_path / "source.json"
    output = tmp_path / "screening" / "results.yaml"
    queue_path = tmp_path / "screening" / "queue.sqlite3"
    keywords_path = tmp_path / "keywords.yaml"
    _write_keywords(keywords_path)
    _write_jsonl(
        source,
        [
            {
                "id": "2401.00001",
                "title": "A GNN benchmark",
                "abstract": "Results on Cora.",
                "categories": "cs.LG",
            },
            {
                "id": "2401.00002",
                "title": "A graph study",
                "abstract": "No machine learning.",
                "categories": "cs.AI",
            },
            {
                "id": "2401.00003",
                "title": "A broken GNN request",
                "abstract": "",
                "categories": "stat.ML",
            },
        ],
    )

    calls: list[str] = []

    def fake_screen(item):
        calls.append(item.arxiv_id)
        if item.arxiv_id == "2401.00003":
            raise RuntimeError("endpoint unavailable")
        accepted = item.arxiv_id == "2401.00001"
        return (
            ScreenResult(
                has_benchmark_results=accepted,
                confidence=0.8,
                notes="accepted" if accepted else "rejected",
            ),
            "fast-model",
            scanner.RequestUsage(
                worker="test-worker",
                duration_s=1.0,
                prompt_tokens=100,
                completion_tokens=20,
            ),
        )

    monkeypatch.setattr(scanner, "_screen", fake_screen)
    first = scanner.run_screening(
        source=source,
        output=output,
        queue_path=queue_path,
        keywords_path=keywords_path,
        workers=2,
        progress_every=1,
        max_papers=0,
    )

    assert first.accepted == 1
    assert first.rejected == 1
    assert calls[:2] == ["2401.00001", "2401.00003"]
    assert calls[2] == "2401.00002"
    assert scanner.load_results(output).arxiv_ids == {"2401.00001", "2401.00002"}

    calls.clear()
    scanner.run_screening(
        source=source,
        output=output,
        queue_path=queue_path,
        keywords_path=keywords_path,
        workers=1,
        progress_every=1,
        max_papers=1,
    )
    assert calls == ["2401.00003"]
    assert scanner.load_results(output).processed == 2
