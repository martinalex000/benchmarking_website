"""Every write here targets a disposable fixture database, never the real one."""

import copy
import json
import sqlite3
from pathlib import Path

import pytest

from backend.mapping.plan import build_plan, digest
from backend.mapping.storage import apply_plan, database_changes, rollback_plan
from tests.unit.test_mapping_plan import prepared


def fixture_plan(tmp_path):
    database, run, papers, output = prepared(tmp_path)
    with sqlite3.connect(database) as db:
        for column, kind in (
            ("is_problematic", "INTEGER DEFAULT 0"),
            ("problematic_reason", "TEXT"),
            ("repetition_status", "TEXT"),
            ("num_runs_evidence", "TEXT"),
            ("trained_by_paper", "INTEGER"),
        ):
            db.execute(f"ALTER TABLE results ADD COLUMN {column} {kind}")
    return database, build_plan(run, database, papers, output)


def snapshot(db):
    return tuple(db.execute("SELECT * FROM results ORDER BY id").fetchone())


def test_quarantine_is_reversible_and_application_is_idempotent(tmp_path):
    database, plan = fixture_plan(tmp_path)
    with sqlite3.connect(database) as db:
        before = snapshot(db)
        receipt = apply_plan(db, plan)
        row = dict(db.execute("SELECT * FROM results").fetchone())
        assert row["is_problematic"] == 1
        assert row["repetition_status"] == "excluded"
        assert row["num_runs"] is None
        assert row["metric_value"] == 0.8
        assert len(receipt["rows"]) == 1
        assert apply_plan(db, plan)["already_applied"]
        rollback_plan(db, receipt["plan_id"])
        assert snapshot(db) == before
        with pytest.raises(ValueError, match="rolled back"):
            apply_plan(db, plan)


def test_stale_row_refuses_whole_transaction(tmp_path):
    database, plan = fixture_plan(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("UPDATE results SET metric_value=0.7")
        db.commit()
        before = snapshot(db)
        with pytest.raises(ValueError, match="Stale row"):
            apply_plan(db, plan)
        assert snapshot(db) == before
        assert not db.execute(
            "SELECT name FROM sqlite_master WHERE name='mapping_change_batches'"
        ).fetchall()


def test_rollback_cannot_destroy_later_manual_edits(tmp_path):
    database, plan = fixture_plan(tmp_path)
    with sqlite3.connect(database) as db:
        receipt = apply_plan(db, plan)
        db.execute("UPDATE results SET is_overridden=1,metric_value=0.9")
        db.commit()
        before = snapshot(db)
        with pytest.raises(ValueError, match="changed after application"):
            rollback_plan(db, receipt["plan_id"])
        assert snapshot(db) == before


@pytest.mark.parametrize("tamper", ["changes", "snapshot", "source"])
def test_artifact_or_plan_tampering_is_rejected(tmp_path, tamper):
    database, plan = fixture_plan(tmp_path)
    plan = copy.deepcopy(plan)
    entry = plan["papers"][0]["entries"][0]
    if tamper == "changes":
        entry["changes"]["value"] = 0.95
    elif tamper == "snapshot":
        entry["before"]["metric_value"] = 0.95
    else:
        plan["papers"][0]["source_sha256"] = "wrong"
    with sqlite3.connect(database) as db:
        before = snapshot(db)
        with pytest.raises(ValueError):
            apply_plan(db, plan)
        assert snapshot(db) == before


def test_database_failure_rolls_back_rows_and_audit_receipt(tmp_path):
    database, plan = fixture_plan(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute(
            "CREATE TRIGGER reject_update BEFORE UPDATE ON results BEGIN SELECT RAISE(ABORT,'forced failure'); END"
        )
        db.commit()
        before = snapshot(db)
        with pytest.raises(sqlite3.IntegrityError, match="forced failure"):
            apply_plan(db, plan)
        assert snapshot(db) == before
        assert not db.execute(
            "SELECT name FROM sqlite_master WHERE name='mapping_change_batches'"
        ).fetchall()


def test_protected_manual_override_is_not_written(tmp_path):
    database, plan = fixture_plan(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("UPDATE results SET is_overridden=1")
        db.commit()
        entry = plan["papers"][0]["entries"][0]
        entry["before"]["is_overridden"] = 1
        entry["before_sha256"] = digest(entry["before"])
        entry["protected_manual_override"] = True
        entry["changes"] = {}
        before = snapshot(db)
        assert apply_plan(db, plan)["rows"] == []
        assert snapshot(db) == before


def test_new_variant_is_tracked_and_undo_refuses_unrelated_reuse(tmp_path):
    database, original = fixture_plan(tmp_path)
    with sqlite3.connect(database) as db:
        for column, kind in (
            ("description", "TEXT"),
            ("is_standard", "INTEGER"),
            ("created_at", "TEXT"),
        ):
            db.execute(f"ALTER TABLE dataset_variants ADD COLUMN {column} {kind}")
    paper = original["papers"][0]
    folder = Path(original["run"]) / "papers" / paper["paper_id"]
    proposal = json.loads((folder / "proposals.json").read_text())[0]
    proposal.update(
        action="numeric_repair_only",
        correction={"old": {"variant": "fixed"}, "corrected": {"variant": "source-backed split"}},
    )
    proposal["verdict"]["eligibility"] = "benchmark"
    proposal["verdict"]["setting_status"] = "supported"
    (folder / "proposals.json").write_text(json.dumps([proposal]))
    plan = build_plan(
        Path(original["run"]), database, tmp_path / "papers", tmp_path / "variant_plan"
    )
    with sqlite3.connect(database) as db:
        before = snapshot(db)
        receipt = apply_plan(db, plan)
        assert len(receipt["created_variants"]) == 1
        variant = receipt["created_variants"][0]
        assert variant["name"] == "source-backed split"
        assert variant["is_standard"] == 1
        db.execute("INSERT INTO results(id,dataset_variant_id) VALUES(2,?)", (variant["id"],))
        db.commit()
        with pytest.raises(ValueError, match="acquired other results"):
            rollback_plan(db, receipt["plan_id"])
        db.execute("DELETE FROM results WHERE id=2")
        db.commit()
        rollback_plan(db, receipt["plan_id"])
        assert snapshot(db) == before
        assert not db.execute(
            "SELECT id FROM dataset_variants WHERE id=?", (variant["id"],)
        ).fetchall()


def test_approved_dataset_correction_resolves_registered_variant_without_writing():
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.executescript(
        "CREATE TABLE datasets(id INTEGER PRIMARY KEY,name TEXT);"
        "CREATE TABLE dataset_variants(id INTEGER PRIMARY KEY,name TEXT,dataset_id INTEGER);"
        "INSERT INTO datasets VALUES(1,'Amazon2M'),(2,'Amazon-ratings');"
        "INSERT INTO dataset_variants VALUES(10,'standard',1),(20,'standard',2);"
    )
    entry = {
        "before": {"dataset_variant_id": 10},
        "changes": {"dataset": "Amazon-ratings"},
        "action": "propose_count",
        "evidence_file": "frozen/proposals.json",
        "evidence_sha256": "example-hash",
    }
    review = {
        "old_dataset": "Amazon2M",
        "corrected_dataset": "Amazon-ratings",
        "corrected_dataset_id": 2,
    }

    resolved = database_changes(
        db,
        entry,
        {"dataset_identity_review": review},
        created_variants=[],
    )

    assert resolved["dataset_variant_id"] == 20
    assert db.execute("SELECT COUNT(*) FROM dataset_variants").fetchone()[0] == 2
    with pytest.raises(ValueError, match="human source review"):
        database_changes(db, entry, {}, created_variants=[])


def test_apply_cli_requires_explicit_write_confirmation():
    from scripts import apply_mapping_plan

    with pytest.raises(SystemExit):
        apply_mapping_plan.main(["apply", "--plan", "unused.json"])


@pytest.mark.parametrize("omission", ["paper", "result"])
def test_apply_cli_refuses_incomplete_plan_coverage(tmp_path, omission):
    from scripts import apply_mapping_plan

    _, plan = fixture_plan(tmp_path)
    if omission == "paper":
        plan["papers"] = []
        expected_error = "does not cover every paper"
    else:
        plan["papers"][0]["entries"] = []
        expected_error = "cover every result row exactly once"

    with pytest.raises(ValueError, match=expected_error):
        apply_mapping_plan._validate_plan_coverage(plan)


def test_apply_cli_refuses_manifest_that_omits_database_paper(tmp_path, capsys):
    from scripts import apply_mapping_plan

    database, plan = fixture_plan(tmp_path)
    with sqlite3.connect(database) as db:
        db.execute("INSERT INTO papers VALUES(2,'omitted','ICML','2024-01-01')")
        db.execute(
            "INSERT INTO results(id,paper_id,model_id,dataset_variant_id,model_name_override,"
            "metric_name,metric_value,metric_std,table_ref,source_ref,evaluation_task,"
            "protocol_decision,protocol_note,num_runs,is_overridden) "
            "VALUES(2,2,1,1,NULL,'Accuracy',0.7,0.01,"
            "'Table 2','this paper','node classification','standard',NULL,NULL,0)"
        )
    before = database.read_bytes()
    plan_path = tmp_path / "incomplete_cohort_plan.json"
    plan_path.write_text(json.dumps(plan))

    result = apply_mapping_plan.main(
        [
            "apply",
            "--plan",
            str(plan_path),
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )

    assert result == 1
    assert "missing=['omitted']" in capsys.readouterr().err
    assert database.read_bytes() == before


@pytest.mark.xfail(
    strict=True,
    reason="Full-cohort coverage must be rechecked inside the apply transaction",
)
def test_apply_cli_refuses_result_added_after_cohort_check(tmp_path, monkeypatch):
    from scripts import apply_mapping_plan

    database, plan = fixture_plan(tmp_path)
    plan_path = tmp_path / "concurrent_insert_plan.json"
    plan_path.write_text(json.dumps(plan))
    validate_cohort = apply_mapping_plan._validate_full_cohort

    def insert_after_cohort_check(candidate, database_path):
        validate_cohort(candidate, database_path)
        with sqlite3.connect(database_path) as db:
            db.execute(
                "INSERT INTO results(id,paper_id,model_id,dataset_variant_id,metric_name,"
                "metric_value,metric_std,table_ref,source_ref,evaluation_task,"
                "protocol_decision,protocol_note,num_runs,is_overridden) "
                "VALUES(2,1,1,1,'Accuracy',0.7,0.01,'Table 1','this paper',"
                "'node classification','standard',NULL,NULL,0)"
            )

    monkeypatch.setattr(
        apply_mapping_plan, "_validate_full_cohort", insert_after_cohort_check
    )
    result = apply_mapping_plan.main(
        [
            "apply",
            "--plan",
            str(plan_path),
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )

    assert result == 1
    with sqlite3.connect(database) as db:
        assert db.execute(
            "SELECT id,is_problematic FROM results ORDER BY id"
        ).fetchall() == [(1, 0), (2, 0)]


def test_apply_cli_refuses_to_create_missing_database(tmp_path, monkeypatch):
    from scripts import apply_mapping_plan

    database = tmp_path / "missing.db"
    monkeypatch.setattr(
        apply_mapping_plan,
        "apply_plan",
        lambda *_args: pytest.fail("Must not apply a plan to a missing database"),
    )
    result = apply_mapping_plan.main(
        [
            "apply",
            "--plan",
            "unused.json",
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )
    assert result == 1
    assert not database.exists()


@pytest.mark.parametrize("omission", ["paper", "result"])
def test_apply_cli_refuses_incomplete_plan_before_writing(tmp_path, capsys, omission):
    from scripts import apply_mapping_plan

    database, plan = fixture_plan(tmp_path)
    plan = copy.deepcopy(plan)
    if omission == "paper":
        plan["papers"] = []
    else:
        plan["papers"][0]["entries"] = []
    plan_path = tmp_path / "incomplete_plan.json"
    plan_path.write_text(json.dumps(plan))
    result = apply_mapping_plan.main(
        [
            "apply",
            "--plan",
            str(plan_path),
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )

    assert result == 1
    message = capsys.readouterr().err.lower()
    assert "coverage" in message or "cover" in message
    with sqlite3.connect(database) as db:
        assert db.execute("SELECT is_problematic FROM results").fetchone() == (0,)
        assert not db.execute(
            "SELECT name FROM sqlite_master WHERE name='mapping_change_batches'"
        ).fetchall()


@pytest.mark.parametrize("malformation", ["top_level", "paper_id"])
def test_apply_cli_refuses_malformed_plan_before_writing(tmp_path, capsys, malformation):
    from scripts import apply_mapping_plan

    database, plan = fixture_plan(tmp_path)
    plan = copy.deepcopy(plan)
    if malformation == "top_level":
        plan = []
    else:
        plan["papers"][0]["paper_id"] = []
    plan_path = tmp_path / "malformed_plan.json"
    plan_path.write_text(json.dumps(plan))
    result = apply_mapping_plan.main(
        [
            "apply",
            "--plan",
            str(plan_path),
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )

    assert result == 1
    assert "refused" in capsys.readouterr().err.lower()
    with sqlite3.connect(database) as db:
        assert db.execute("SELECT is_problematic FROM results").fetchone() == (0,)
        assert not db.execute(
            "SELECT name FROM sqlite_master WHERE name='mapping_change_batches'"
        ).fetchall()


def test_apply_cli_rejects_plan_and_row_artifacts_changed_together(tmp_path, capsys):
    from scripts import apply_mapping_plan

    database, plan = fixture_plan(tmp_path)
    plan = copy.deepcopy(plan)
    paper_id = plan["papers"][0]["paper_id"]
    folder = Path(plan["run"]) / "papers" / paper_id
    (folder / "rows.json").write_text("[]")
    (folder / "proposals.json").write_text("[]")
    plan["papers"][0]["entries"] = []
    plan_path = tmp_path / "tampered_inputs_plan.json"
    plan_path.write_text(json.dumps(plan))

    result = apply_mapping_plan.main(
        [
            "apply",
            "--plan",
            str(plan_path),
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )

    assert result == 1
    assert "immutable paper input changed" in capsys.readouterr().err.lower()
    with sqlite3.connect(database) as db:
        assert db.execute("SELECT is_problematic FROM results").fetchone() == (0,)
        assert not db.execute(
            "SELECT name FROM sqlite_master WHERE name='mapping_change_batches'"
        ).fetchall()


def test_apply_cli_uses_explicit_saved_plan_and_rw_database(tmp_path, monkeypatch):
    from scripts import apply_mapping_plan

    database = tmp_path / "target.db"
    with sqlite3.connect(database):
        pass
    plan_path = tmp_path / "change_plan.json"
    plan_path.write_text('{"mode":"dry_run"}')
    seen = {}
    monkeypatch.setattr(apply_mapping_plan, "_validate_plan_coverage", lambda _plan: None)
    monkeypatch.setattr(apply_mapping_plan, "_validate_full_cohort", lambda _plan, _database: None)

    def fake_apply(db, plan):
        seen["plan"] = plan
        seen["query_only"] = db.execute("PRAGMA query_only").fetchone()[0]
        return {"rows": [{"result_id": 12}], "plan_id": "test-plan"}

    monkeypatch.setattr(apply_mapping_plan, "apply_plan", fake_apply)
    result = apply_mapping_plan.main(
        [
            "apply",
            "--plan",
            str(plan_path),
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )
    assert result == 0
    assert seen == {"plan": {"mode": "dry_run"}, "query_only": 0}


def test_rollback_cli_requires_confirmation_and_passes_plan_id(tmp_path, monkeypatch):
    from scripts import apply_mapping_plan

    database = tmp_path / "target.db"
    with sqlite3.connect(database):
        pass
    seen = {}

    def fake_rollback(db, plan_id):
        seen["plan_id"] = plan_id
        seen["query_only"] = db.execute("PRAGMA query_only").fetchone()[0]
        return {"rows": [{"result_id": 12}]}

    monkeypatch.setattr(apply_mapping_plan, "rollback_plan", fake_rollback)
    result = apply_mapping_plan.main(
        [
            "rollback",
            "--plan-id",
            "test-plan",
            "--database",
            str(database),
            "--confirm-database-write",
        ]
    )
    assert result == 0
    assert seen == {"plan_id": "test-plan", "query_only": 0}


def test_apply_and_rollback_cli_on_disposable_database(tmp_path, capsys):
    from scripts import apply_mapping_plan

    database, plan = fixture_plan(tmp_path)
    plan_file = tmp_path / "saved_plan.json"
    plan_file.write_text(json.dumps(plan))
    command = [
        "--database",
        str(database),
        "--confirm-database-write",
    ]

    assert apply_mapping_plan.main(["apply", "--plan", str(plan_file), *command]) == 0
    assert f"plan ID {digest(plan)}." in capsys.readouterr().out
    with sqlite3.connect(database) as db:
        assert db.execute("SELECT is_problematic FROM results").fetchone() == (1,)

    assert apply_mapping_plan.main(["rollback", "--plan-id", digest(plan), *command]) == 0
    assert "rolled back" in capsys.readouterr().out
    with sqlite3.connect(database) as db:
        assert db.execute("SELECT is_problematic FROM results").fetchone() == (0,)
