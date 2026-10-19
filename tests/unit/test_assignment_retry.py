import json
from contextlib import nullcontext

import pytest

from experiments.table_provenance_experiment import retry_assignment_validation as retry


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


def test_retry_preserves_success_and_does_not_reuse_failed_calls(tmp_path, monkeypatch):
    source = tmp_path / "original"
    destination = tmp_path / "retry"
    save(source / "manifest.json", {"papers": [{"paper_id": "good"}, {"paper_id": "bad"}]})
    save(source / "status.json", {"pipeline_terminal": True})
    for name in ("prompts", "implementation"):
        (source / name).mkdir()
    for pid, state in (("good", "complete"), ("bad", "failed")):
        folder = source / "papers" / pid
        save(folder / "assessment.json", {"state": state, "errors": []})
        save(folder / "rows.json", [{"result_id": pid}])
        save(folder / "chunks" / "001" / "facts.json", {"old_call": True})
    monkeypatch.setattr(retry.batch, "readonly", lambda: nullcontext(None))
    monkeypatch.setattr(retry.batch, "stored_rows", lambda db, pid: [{"result_id": pid}])
    monkeypatch.setattr(retry.batch, "analyze", lambda root: None)
    assert retry.prepare_retry(source, destination) == ["bad"]
    assert (destination / "papers/good/chunks/001/facts.json").exists()
    assert not (destination / "papers/bad/chunks").exists()
    assert (source / "papers/bad/chunks/001/facts.json").exists()
    assert json.loads((destination / "status.json").read_text())["completed"] == 1
    with pytest.raises(ValueError, match="already exists"):
        retry.prepare_retry(source, destination)


def test_retry_rejects_nonterminal_parent(tmp_path):
    save(tmp_path / "original/manifest.json", {"papers": []})
    save(tmp_path / "original/status.json", {"pipeline_terminal": False})
    with pytest.raises(ValueError, match="terminal"):
        retry.prepare_retry(tmp_path / "original", tmp_path / "retry")
