"""Read-only plans reject stale inputs and cannot sneak in withheld repairs."""

import hashlib
import json
import sqlite3

import pytest

from backend.mapping.plan import (
    _repair_fields_match,
    build_plan,
    digest,
    effective_changes,
    proposed_changes,
    read_json,
    validate_proposal,
)
from backend.mapping.schema import stored_rows
from scripts.apply_mapping_plan import _validate_full_cohort


def prepared(tmp_path):
    from tests.unit.test_assignment_protocol_refresh import reviewed_fixture

    _, verdict, source, _ = reviewed_fixture()
    source = source.replace("10-fold CV for tuning, repeated 10 times", "5 runs")
    verdict.eligibility = "ablation"
    database = tmp_path / "test.db"
    with sqlite3.connect(database) as db:
        db.executescript(
            "CREATE TABLE papers(id INTEGER, arxiv_id TEXT, venue TEXT, published_date TEXT);"
            "CREATE TABLE models(id INTEGER, name TEXT);"
            "CREATE TABLE datasets(id INTEGER, name TEXT);"
            "CREATE TABLE dataset_variants(id INTEGER PRIMARY KEY, name TEXT, dataset_id INTEGER);"
            "CREATE TABLE results(id INTEGER, paper_id INTEGER, model_id INTEGER,"
            "dataset_variant_id INTEGER, model_name_override TEXT, metric_name TEXT,"
            "metric_value REAL, metric_std REAL, table_ref TEXT, source_ref TEXT,"
            "evaluation_task TEXT, protocol_decision TEXT, protocol_note TEXT,"
            "num_runs INTEGER, is_overridden INTEGER);"
            "INSERT INTO papers VALUES(1,'one','ICML','2024-01-01');"
            "INSERT INTO models VALUES(1,'Own');"
            "INSERT INTO datasets VALUES(1,'Cora');"
            "INSERT INTO dataset_variants VALUES(1,'fixed',1);"
            "INSERT INTO results VALUES(1,1,1,1,NULL,'Accuracy',0.8,0.002,"
            "'Table 1','this paper','node classification','standard',NULL,NULL,0);"
        )
        rows = stored_rows(db, "one")
    run = tmp_path / "run"
    folder = run / "papers" / "one"
    folder.mkdir(parents=True)
    local = tmp_path / "papers" / "one" / "latex"
    local.mkdir(parents=True)
    (local / "expanded.tex").write_text(source)
    (folder / "source.tex").write_text(source)
    for path, value in (
        (
            run / "status.json",
            {
                "state": "finished",
                "selected_rows_unchanged": True,
                "scope_unchanged": True,
            },
        ),
        (run / "manifest.json", {"papers": [{"paper_id": "one"}]}),
        (
            run / "scope.json",
            {
                "definition": "test scope",
                "candidate_papers": 1,
                "included_papers": [{"paper_id": "one", "rows": len(rows), "tables": 1}],
                "excluded_papers": [],
                "human_reviews_imported": {"protocols": 0, "datasets": 0},
            },
        ),
        (folder / "assessment.json", {"state": "complete", "errors": []}),
        (folder / "rows.json", rows),
        (
            folder / "proposals.json",
            [
                {
                    **rows[0],
                    "action": "propose_quarantine",
                    "reason": "verifier_excluded",
                    "proposed_num_runs": None,
                    "verdict": verdict.model_dump(),
                    "selected_candidate": verdict.corrected_fact.candidates[0].model_dump(),
                }
            ],
        ),
    ):
        path.write_text(json.dumps(value))
    manifest_path = run / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["papers_dir"] = str((tmp_path / "papers").resolve())
    manifest["papers"][0]["source_sha256"] = hashlib.sha256(source.encode()).hexdigest()
    manifest["papers"][0]["input_sha256"] = {
        name: hashlib.sha256((folder / name).read_bytes()).hexdigest()
        for name in ("source.tex", "rows.json")
    }
    manifest_path.write_text(json.dumps(manifest))
    return database, run, tmp_path / "papers", tmp_path / "output"


def test_plan_preserves_database_and_retains_rollback_snapshot(tmp_path):
    database, run, papers, output = prepared(tmp_path)
    before = database.read_bytes()
    plan = build_plan(run, database, papers, output)
    assert database.read_bytes() == before
    entry = plan["papers"][0]["entries"][0]
    assert entry["changes"] == {"disposition": "quarantine", "reason": "verifier_excluded"}
    assert entry["before"]["metric_value"] == 0.8
    assert plan["database_modified"] is False
    assert (output / "summary.md").exists()
    with pytest.raises(FileExistsError):
        build_plan(run, database, papers, output)


def test_repair_snapshot_may_match_old_or_already_corrected_values():
    snapshot = {"value": 0.7190000000000001, "std": 0.004, "model": "GCN"}
    assert _repair_fields_match(
        snapshot,
        {
            "old": {"value": 0.719, "std": 0.0040000000001, "model": "GAT"},
            "corrected": {"value": 0.72, "std": 0.004, "model": "GCN"},
        },
    )
    assert not _repair_fields_match(
        snapshot,
        {"old": {"value": 0.718}, "corrected": {"value": 0.72}},
    )


def test_plan_omits_repairs_already_present_in_frozen_snapshot():
    proposal = {
        "action": "copied_excluded",
        "proposed_num_runs": None,
        "reason": "copied",
        "correction": {
            "old": {"metric": "F1"},
            "corrected": {"metric": "F1-micro"},
        },
    }
    assert effective_changes(proposal, False, {"metric": "F1-micro"}) == {
        "disposition": "copied_excluded",
        "trained_by_paper": False,
    }


def test_plan_omits_repetition_decisions_already_applied():
    count = {
        "action": "propose_count",
        "proposed_num_runs": 5,
    }
    copied = {
        "action": "copied_excluded",
        "proposed_num_runs": None,
    }
    assert effective_changes(
        count,
        False,
        {"num_runs": 5, "trained_by_paper": 1, "repetition_status": "count"},
    ) == {}
    assert effective_changes(
        copied,
        False,
        {"num_runs": None, "trained_by_paper": 0, "repetition_status": "copied"},
    ) == {}


def test_ignored_scope_papers_retain_distinct_approved_reasons(tmp_path):
    database, run, papers, output = prepared(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("INSERT INTO papers VALUES(2,'two','ICLR','2024-01-01')")
        db.execute(
            "INSERT INTO results VALUES(2,2,1,1,NULL,'Accuracy',0.7,0.01,"
            "'Table 1','this paper','node classification','standard',NULL,NULL,0)"
        )
    plan = build_plan(
        run,
        database,
        papers,
        output,
        ignored_paper_ids={"two"},
        ignored_paper_reasons={"two": "adversarial_examples_not_tracked"},
    )
    assert plan["ignored_papers"][0]["reason"] == "adversarial_examples_not_tracked"
    with pytest.raises(ValueError, match="Unsupported ignored-paper reason"):
        build_plan(
            run,
            database,
            papers,
            tmp_path / "invalid-output",
            ignored_paper_ids={"two"},
            ignored_paper_reasons={"two": "not_authorized"},
        )


def test_manual_override_is_protected(tmp_path):
    database, run, papers, output = prepared(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("UPDATE results SET is_overridden=1")
    plan = build_plan(run, database, papers, output)
    entry = plan["papers"][0]["entries"][0]
    assert entry["protected_manual_override"]
    assert entry["changes"] == {}


def test_partial_plan_freezes_failed_papers_as_skipped(tmp_path):
    from backend.mapping.storage import apply_plan
    from scripts.apply_mapping_plan import _validate_plan_coverage

    database, run, papers, output = prepared(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("ALTER TABLE results ADD COLUMN is_problematic INTEGER DEFAULT 0")
        db.execute("ALTER TABLE results ADD COLUMN problematic_reason TEXT")
        db.execute("ALTER TABLE results ADD COLUMN num_runs_evidence TEXT")
        db.execute("ALTER TABLE results ADD COLUMN trained_by_paper INTEGER")
        db.execute("ALTER TABLE results ADD COLUMN repetition_status TEXT")
    source = (run / "papers" / "one" / "source.tex").read_text()
    second_folder = run / "papers" / "two"
    second_folder.mkdir()
    second_local = papers / "two" / "latex"
    second_local.mkdir(parents=True)
    (second_folder / "source.tex").write_text(source)
    (second_local / "expanded.tex").write_text(source)
    with sqlite3.connect(database) as db:
        db.execute("INSERT INTO papers VALUES(2,'two','ICLR','2024-01-01')")
        db.execute(
            "INSERT INTO results(id,paper_id,model_id,dataset_variant_id,model_name_override,"
            "metric_name,metric_value,metric_std,table_ref,source_ref,evaluation_task,"
            "protocol_decision,protocol_note,num_runs,is_overridden) VALUES("
            "2,2,1,1,NULL,'Accuracy',0.7,0.01,'Table 1','this paper',"
            "'node classification','standard',NULL,NULL,0)"
        )
        second_rows = stored_rows(db, "two")
    (second_folder / "rows.json").write_text(json.dumps(second_rows))
    (second_folder / "assessment.json").write_text(
        json.dumps({"state": "failed", "errors": [{"chunk": "001"}]})
    )
    manifest = read_json(run / "manifest.json")
    manifest["papers"][0]["model"] = "glm"
    manifest["papers"].append(
        {
            "paper_id": "two",
            "model": "glm",
            "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "input_sha256": {
                "source.tex": hashlib.sha256(source.encode()).hexdigest(),
                "rows.json": hashlib.sha256((second_folder / "rows.json").read_bytes()).hexdigest(),
            },
        }
    )
    (run / "manifest.json").write_text(json.dumps(manifest))
    scope = read_json(run / "scope.json")
    scope["candidate_papers"] = 2
    scope["included_papers"].append({"paper_id": "two", "rows": 1, "tables": 1})
    (run / "scope.json").write_text(json.dumps(scope))
    (run / "status.json").write_text(json.dumps({"phase": "mapping"}))

    plan = build_plan(
        run,
        database,
        papers,
        output,
        allow_partial=True,
        eligible_models={"glm"},
    )
    assert [paper["paper_id"] for paper in plan["papers"]] == ["one"]
    assert [paper["paper_id"] for paper in plan["skipped_papers"]] == ["two"]
    _validate_plan_coverage(plan)
    _validate_full_cohort(plan, database)
    with sqlite3.connect(database) as db:
        receipt = apply_plan(db, plan)
        assert [row["result_id"] for row in receipt["rows"]] == [1]
        assert db.execute("SELECT is_problematic FROM results WHERE id=1").fetchone()[0] == 1
        assert db.execute("SELECT is_problematic FROM results WHERE id=2").fetchone()[0] == 0


@pytest.mark.parametrize("failure", ["row", "source", "assessment", "coverage"])
def test_plan_refuses_stale_failed_or_incomplete_inputs(tmp_path, failure):
    database, run, papers, output = prepared(tmp_path)
    folder = run / "papers" / "one"
    if failure == "row":
        with sqlite3.connect(database) as db:
            db.execute("UPDATE results SET metric_value=0.9")
    elif failure == "source":
        (papers / "one" / "latex" / "expanded.tex").write_text("Changed")
    elif failure == "assessment":
        (folder / "assessment.json").write_text('{"state":"complete","errors":["timeout"]}')
    else:
        (folder / "proposals.json").write_text("[]")
    with pytest.raises(ValueError):
        build_plan(run, database, papers, output)
    assert not output.exists()


def test_apply_coverage_guard_rejects_paper_missing_from_run_scope(tmp_path):
    database, run, _papers, _output = prepared(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("INSERT INTO papers VALUES(2,'omitted','ICLR','2025-01-01')")
        db.execute(
            "INSERT INTO results VALUES(2,2,1,1,NULL,'Accuracy',0.7,0.01,"
            "'Table 1','this paper','node classification','standard',NULL,NULL,0)"
        )

    manifest = read_json(run / "manifest.json")
    scope = read_json(run / "scope.json")
    plan = {
        "run": str(run.resolve()),
        "manifest_sha256": digest(manifest),
        "scope_sha256": digest(scope),
        "scope_exclusions": scope["excluded_papers"],
        "papers": manifest["papers"],
    }

    with pytest.raises(ValueError, match=r"missing=\['omitted'\]"):
        _validate_full_cohort(plan, database)


def test_apply_coverage_guard_accepts_only_explicitly_ignored_artifact(tmp_path):
    database, run, _papers, _output = prepared(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("INSERT INTO papers VALUES(2,'artifact','ICLR','2025-01-01')")
        db.execute(
            "INSERT INTO results(id,paper_id,model_id,dataset_variant_id,model_name_override,"
            "metric_name,metric_value,metric_std,table_ref,source_ref,evaluation_task,"
            "protocol_decision,protocol_note,num_runs,is_overridden) VALUES("
            "2,2,1,1,NULL,'Accuracy',0.7,0.01,'Table 1','this paper',"
            "'node classification','standard',NULL,NULL,0)"
        )
        ignored_rows = stored_rows(db, "artifact")

    manifest = read_json(run / "manifest.json")
    scope = read_json(run / "scope.json")
    plan = {
        "run": str(run.resolve()),
        "manifest_sha256": digest(manifest),
        "scope_sha256": digest(scope),
        "scope_exclusions": scope["excluded_papers"],
        "papers": manifest["papers"],
        "ignored_papers": [
            {
                "paper_id": "artifact",
                "reason": "user_confirmed_artifact_ignored",
                "rows": ignored_rows,
            }
        ],
    }
    _validate_full_cohort(plan, database)
    plan["ignored_papers"][0]["reason"] = "unspecified"
    with pytest.raises(ValueError, match="lacks explicit approval"):
        _validate_full_cohort(plan, database)


def test_unresolved_repairs_cannot_become_changes():
    proposal = {
        "action": "configuration_scope_unresolved",
        "correction": {"old": {"value": 1}, "corrected": {"value": 2}},
    }
    assert proposed_changes(proposal) == {}
    with pytest.raises(ValueError, match="Non-count"):
        validate_proposal({**proposal, "proposed_num_runs": 10}, "")


def test_mapping_plan_command_does_not_initialize_database(monkeypatch):
    from backend import pipeline

    monkeypatch.setattr(
        pipeline, "init_db", lambda: pytest.fail("Read-only command initialized DB")
    )
    monkeypatch.setattr(pipeline, "stage_mapping_plan", lambda args: True)
    assert pipeline.main(["mapping-plan", "--run-dir", "unused", "--output-dir", "unused"]) == 0


@pytest.mark.parametrize("tamper", [None, "identity", "selection", "origin", "count"])
def test_count_requires_verified_physical_cell_and_execution(tamper):
    from tests.unit.test_assignment_protocol_refresh import reviewed_fixture

    _, verdict, source, _ = reviewed_fixture()
    source = source.replace("10-fold CV for tuning, repeated 10 times", "5 runs")
    proposal = {
        "action": "propose_count",
        "proposed_num_runs": 5,
        "verdict": verdict.model_dump(),
        "selected_candidate": verdict.corrected_fact.candidates[0].model_dump(),
    }
    if tamper == "identity":
        proposal["selected_candidate"]["method"] = "Unverified alternative"
    elif tamper == "selection":
        proposal["verdict"]["selected_candidate_index"] = 8
    elif tamper == "origin":
        proposal["verdict"]["execution_supported"] = False
    elif tamper == "count":
        proposal["proposed_num_runs"] = 50
    if tamper is None:
        validate_proposal(proposal, source)
    else:
        with pytest.raises(ValueError):
            validate_proposal(proposal, source)


def test_plan_rejects_model_repair_that_drops_stored_optimizer_axis():
    from tests.unit.test_assignment_protocol_refresh import reviewed_fixture

    _, verdict, source, _ = reviewed_fixture()
    candidate = verdict.corrected_fact.candidates[0]
    candidate.method = "GotenNet"
    candidate.configuration_axes = {"backbone": "GotenNet", "optimizer": "Muon"}
    proposal = {
        "model": "Muon",
        "variant": "Standard split",
        "action": "propose_count",
        "proposed_num_runs": 5,
        "correction": {
            "old": {"model": "Muon", "variant": "Standard split"},
            "corrected": {"model": "GotenNet", "variant": "Standard split"},
        },
        "verdict": verdict.model_dump(),
        "selected_candidate": candidate.model_dump(),
    }

    with pytest.raises(ValueError, match="optimizer=Muon"):
        validate_proposal(proposal, source)
