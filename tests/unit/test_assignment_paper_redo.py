import json

from experiments.table_provenance_experiment import redo_assignment_paper as redo


def test_explicit_redo_archives_old_calls_before_fresh_run(tmp_path, monkeypatch):
    def save(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    save(tmp_path / "manifest.json", {"papers": [{"paper_id": "one"}]})
    save(
        tmp_path / "status.json",
        {
            "pipeline_terminal": True,
            "completed": 1,
            "results": {"one": {}},
        },
    )
    folder = tmp_path / "papers/one"
    save(folder / "assessment.json", {"state": "failed", "errors": [{"error": "bad IDs"}]})
    save(folder / "chunks/001/facts.json", {"old": True})
    save(folder / "protocol_keys.json", {"unchanged": True})
    calls = []

    def run(root):
        assert not (folder / "chunks").exists()
        assert not (folder / "assessment.json").exists()
        assert (folder / "protocol_keys.json").exists()
        calls.append(root)

    monkeypatch.setattr(redo.validation, "run", run)
    monkeypatch.setattr(redo, "progress", lambda *args: None)
    monkeypatch.setattr(redo, "supervise", lambda *args, **kwargs: None)
    redo.redo(tmp_path, "one")
    assert calls == [tmp_path]
    assert len(list((tmp_path / "attempt_history").glob("*/chunks/001/facts.json"))) == 1
