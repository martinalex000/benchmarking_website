"""Regression tests for scripts/repopulate_db.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Model, Paper, Result, TodoPaper, TodoPaperStatus


def _load_repopulate_db_module():
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "repopulate_db.py"
    spec = importlib.util.spec_from_file_location("test_repopulate_db_script", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _configure_temp_db(monkeypatch, tmp_path):
    db_path = tmp_path / "benchmarks.db"
    monkeypatch.setattr(cfg, "db_path", db_path)
    monkeypatch.setattr(cfg, "data_dir", tmp_path)
    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db(str(db_path))
    return db_path


def _insert_paper_with_results(arxiv_id: str, *, title: str = "Test Paper") -> None:
    with session_scope() as session:
        benchmark = Benchmark(name="Test Benchmark", short_name=f"bench-{arxiv_id}")
        session.add(benchmark)
        session.flush()
        dataset = Dataset(
            benchmark_id=benchmark.id,
            name="Test Dataset",
            task_type="node_classification",
            primary_metric="accuracy",
            higher_is_better=1,
        )
        session.add(dataset)
        session.flush()
        variant = DatasetVariant(dataset_id=dataset.id, name="Standard", is_standard=1)
        session.add(variant)
        session.flush()

        paper = Paper(
            arxiv_id=arxiv_id,
            title=title,
            extraction_status="done",
            discovery_source="manual",
        )
        session.add(paper)
        session.flush()

        model = Model(paper_id=paper.id, name="Test Model", canonical_name=f"test-model-{arxiv_id}")
        session.add(model)
        session.flush()

        session.add(
            Result(
                paper_id=paper.id,
                model_id=model.id,
                dataset_variant_id=variant.id,
                metric_name="accuracy",
                metric_value=0.9,
                extraction_model="test-model",
            )
        )


def test_papers_with_results_only_returns_papers_that_have_results(monkeypatch, tmp_path):
    module = _load_repopulate_db_module()
    _configure_temp_db(monkeypatch, tmp_path)

    with session_scope() as session:
        touched = Paper(
            arxiv_id="1111.1111",
            title="Touched only",
            extraction_status="downloaded",
            discovery_source="manual",
        )
        session.add(touched)

    _insert_paper_with_results("2222.2222", title="Has results")

    assert module._papers_with_results() == [("2222.2222", "Has results")]
    assert module._papers_with_results(only=["1111.1111"]) == []


def test_repopulate_db_primes_important_queue_for_papers_with_results(monkeypatch, tmp_path):
    module = _load_repopulate_db_module()
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_paper_with_results("2401.17791", title="Queued paper")

    papers_dir = tmp_path / "papers" / "2401.17791" / "extracted"
    papers_dir.mkdir(parents=True)
    (papers_dir / "llm_output.yaml").write_text("results: {}\n", encoding="utf-8")
    (tmp_path / "papers" / "2401.17791" / "paper.pdf").write_bytes(b"%PDF-1.4")

    monkeypatch.setattr(cfg, "papers_dir", tmp_path / "papers")
    monkeypatch.setattr(cfg, "project_root", tmp_path)

    queue_calls: list[dict] = []

    def fake_add_todo_paper(arxiv_id, **kwargs):
        queue_calls.append({"arxiv_id": arxiv_id, **kwargs})
        return True, f"Added {arxiv_id}"

    monkeypatch.setattr(module, "add_todo_paper", fake_add_todo_paper)
    monkeypatch.setattr(
        module,
        "_delete_llm_outputs",
        lambda arxiv_ids: (
            module.LlmOutputDeletionSummary(file_count=1, paper_count=1),
            ["papers/2401.17791/extracted/llm_output.yaml"],
        ),
    )
    monkeypatch.setattr(module.console, "print", lambda *args, **kwargs: None)
    monkeypatch.setattr(module.console, "rule", lambda *args, **kwargs: None)

    original_argv = sys.argv[:]
    try:
        sys.argv = ["repopulate_db.py"]
        module.main()
    finally:
        sys.argv = original_argv

    assert queue_calls == [
        {
            "arxiv_id": "2401.17791",
            "title": "Queued paper",
            "reason": "repopulate_db.py",
            "added_by": "repopulate_db.py",
            "is_manually_important": True,
            "requeue": True,
        }
    ]


def test_repopulate_db_delete_all_llm_outputs_purges_every_paper_dir(monkeypatch, tmp_path):
    module = _load_repopulate_db_module()
    _configure_temp_db(monkeypatch, tmp_path)
    _insert_paper_with_results("2401.17791", title="Queued paper")

    papers_root = tmp_path / "papers"
    for arxiv_id in ("2401.17791", "9999.9999"):
        extracted = papers_root / arxiv_id / "extracted"
        extracted.mkdir(parents=True)
        (extracted / "llm_output.yaml").write_text("results: {}\n", encoding="utf-8")
        (papers_root / arxiv_id / "paper.pdf").write_bytes(b"%PDF-1.4")

    monkeypatch.setattr(cfg, "papers_dir", papers_root)
    monkeypatch.setattr(cfg, "project_root", tmp_path)

    deleted_for: list[list[str]] = []

    def fake_delete_llm_outputs(arxiv_ids):
        deleted_for.append(list(arxiv_ids))
        return (
            module.LlmOutputDeletionSummary(file_count=len(arxiv_ids), paper_count=len(arxiv_ids)),
            [f"papers/{arxiv_id}/extracted/llm_output.yaml" for arxiv_id in arxiv_ids[:3]],
        )

    monkeypatch.setattr(module, "_delete_llm_outputs", fake_delete_llm_outputs)
    monkeypatch.setattr(
        module,
        "_prime_repopulation_queue",
        lambda papers: module._empty_queue_prime_summary(queued=1),
    )
    monkeypatch.setattr(module.console, "print", lambda *args, **kwargs: None)
    monkeypatch.setattr(module.console, "rule", lambda *args, **kwargs: None)

    original_argv = sys.argv[:]
    try:
        sys.argv = ["repopulate_db.py", "--delete-all-llm-outputs"]
        module.main()
    finally:
        sys.argv = original_argv

    assert deleted_for == [["2401.17791", "9999.9999"]]


def test_print_llm_output_deletion_summary_shows_three_examples(monkeypatch, tmp_path):
    module = _load_repopulate_db_module()
    papers_root = tmp_path / "papers"
    for arxiv_id in ("1111.1111", "2222.2222", "3333.3333", "4444.4444"):
        extracted = papers_root / arxiv_id / "extracted"
        extracted.mkdir(parents=True)
        (extracted / "llm_output.yaml").write_text("results: {}\n", encoding="utf-8")

    monkeypatch.setattr(cfg, "papers_dir", papers_root)
    monkeypatch.setattr(cfg, "project_root", tmp_path)

    from rich.console import Console

    console = Console(record=True)
    monkeypatch.setattr(module, "console", console)

    summary, examples = module._summarize_llm_output_deletions(
        ["1111.1111", "2222.2222", "3333.3333", "4444.4444"]
    )
    module._print_llm_output_deletion_summary(
        summary,
        prefix="Delete",
        scope="all papers/",
        examples=examples,
    )
    output = console.export_text()

    assert summary.file_count == 4
    assert len(examples) == 3
    assert "papers/1111.1111/extracted/llm_output.yaml" in output
    assert "papers/2222.2222/extracted/llm_output.yaml" in output
    assert "papers/3333.3333/extracted/llm_output.yaml" in output
    assert "papers/4444.4444/extracted/llm_output.yaml" not in output
    assert "… and 1 more file(s)" in output


def test_render_queue_plan_table_summarizes_large_sets(monkeypatch, tmp_path):
    module = _load_repopulate_db_module()
    papers = [(f"2401.{i:05d}", f"Paper {i}") for i in range(25)]
    monkeypatch.setattr(module, "_has_download", lambda arxiv_id: True)

    from rich.console import Console

    console = Console(record=True)
    monkeypatch.setattr(module, "console", console)

    module._render_queue_plan_table(papers, skip_extract=False)
    output = console.export_text()

    assert "25 total with stored results" in output
    assert "… and 5 more papers" in output
    assert output.count("2401.") <= module._MAX_SAMPLE_ROWS + 2


def test_repopulate_db_clean_reseeds_and_queues_results_papers(monkeypatch, tmp_path):
    module = _load_repopulate_db_module()
    db_path = _configure_temp_db(monkeypatch, tmp_path)
    _insert_paper_with_results("2401.17791", title="Queued paper")

    papers_dir = tmp_path / "papers" / "2401.17791"
    (papers_dir / "extracted").mkdir(parents=True)
    (papers_dir / "extracted" / "llm_output.yaml").write_text("results: {}\n", encoding="utf-8")
    (papers_dir / "paper.pdf").write_bytes(b"%PDF-1.4")
    monkeypatch.setattr(cfg, "papers_dir", tmp_path / "papers")
    monkeypatch.setattr(cfg, "project_root", tmp_path)

    seed_calls: list[str] = []

    def fake_seed():
        seed_calls.append("seeded")

    monkeypatch.setattr("backend.seed_db.seed", fake_seed)
    monkeypatch.setattr(module.console, "print", lambda *args, **kwargs: None)
    monkeypatch.setattr(module.console, "rule", lambda *args, **kwargs: None)

    original_argv = sys.argv[:]
    try:
        sys.argv = ["repopulate_db.py", "--clean"]
        module.main()
    finally:
        sys.argv = original_argv

    assert seed_calls == ["seeded"]

    init_db(str(db_path))
    with session_scope() as session:
        row = session.query(TodoPaper).filter_by(arxiv_id="2401.17791").one()
        assert row.is_manually_important == 1
        assert row.status == TodoPaperStatus.PENDING.value
        assert row.reason == "repopulate_db.py"
