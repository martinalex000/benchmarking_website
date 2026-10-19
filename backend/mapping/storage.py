"""Transactional application and guarded undo of validated mapping results."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

from backend.mapping.datasets import load_reviews
from backend.mapping.plan import (
    IGNORED_PAPER_REASONS,
    digest,
    effective_changes,
    read_json,
    suppress_metric_unique_conflicts,
    validate_proposal,
)
from backend.mapping.schema import stored_rows

AUDIT_TABLE = "mapping_change_batches"
DIRECT_FIELDS = {
    "value": "metric_value",
    "std": "metric_std",
    "metric": "metric_name",
    "model": "model_name_override",
    "num_runs": "num_runs",
    "trained_by_paper": "trained_by_paper",
}


def row_snapshot(db: sqlite3.Connection, rid: int) -> dict:
    row = db.execute("SELECT * FROM results WHERE id=?", (rid,)).fetchone()
    if row is None:
        raise ValueError(f"Missing result {rid}")
    return dict(row)


def verify_artifacts(plan: dict) -> dict[int, dict]:
    if plan.get("mode") != "dry_run" or plan.get("version") != 1:
        raise ValueError("Unsupported change plan")
    run = Path(plan["run"])
    manifest = read_json(run / "manifest.json")
    if digest(manifest) != plan["manifest_sha256"]:
        raise ValueError("Manifest changed after planning")
    scope = read_json(run / "scope.json")
    if digest(scope) != plan.get("scope_sha256"):
        raise ValueError("Scope ledger changed after planning")
    if scope["excluded_papers"] != plan.get("scope_exclusions"):
        raise ValueError("Scoped-out papers changed after planning")
    manifest_papers = {paper["paper_id"]: paper for paper in manifest["papers"]}
    proposals_by_id = {}
    for ignored in plan.get("ignored_papers", []):
        if ignored.get("reason") not in IGNORED_PAPER_REASONS or not ignored.get("rows"):
            raise ValueError("Ignored cohort paper lacks an approved reason or row snapshot")
    for skipped in plan.get("skipped_papers", []):
        paper_id = skipped["paper_id"]
        if paper_id not in manifest_papers:
            raise ValueError(f"Skipped paper is absent from the manifest: {paper_id}")
        expected_model = manifest_papers[paper_id].get("model", manifest.get("model"))
        if skipped.get("model") != expected_model:
            raise ValueError(f"Skipped model provenance changed for {paper_id}")
        folder = run / "papers" / paper_id
        frozen_rows = read_json(folder / "rows.json")
        if skipped.get("rows") != frozen_rows:
            raise ValueError(f"Skipped row snapshot changed for {paper_id}")
        source = (folder / "source.tex").read_text()
        import hashlib

        source_hash = hashlib.sha256(source.encode()).hexdigest()
        if source_hash != skipped.get("source_sha256"):
            raise ValueError(f"Skipped source changed for {paper_id}")
        if (
            source
            != Path(manifest.get("papers_dir", ""), paper_id, "latex", "expanded.tex").read_text()
        ):
            raise ValueError(f"Local source changed for skipped paper {paper_id}")
    for paper in plan["papers"]:
        expected_model = manifest_papers[paper["paper_id"]].get("model", manifest.get("model"))
        if paper.get("model") != expected_model:
            raise ValueError(f"Model provenance changed for {paper['paper_id']}")
        source_path = run / "papers" / paper["paper_id"] / "source.tex"
        source = source_path.read_text()
        import hashlib

        if hashlib.sha256(source.encode()).hexdigest() != paper["source_sha256"]:
            raise ValueError("Frozen source changed after planning")
        if Path(paper["local_source_file"]).read_text() != source:
            raise ValueError("Local LaTeX changed after planning")
        folder = source_path.parent
        records_path = folder / "reviewed_protocols.json"
        records = read_json(records_path) if records_path.exists() else []
        manifest_paper = manifest_papers[paper["paper_id"]]
        dataset_records = load_reviews(folder, manifest_paper)
        proposals = {p["result_id"]: p for p in read_json(folder / "proposals.json")}
        before_rows = {row["result_id"]: row for row in read_json(folder / "rows.json")}
        for entry in paper["entries"]:
            rid = entry["result_id"]
            if rid in proposals_by_id or rid not in proposals:
                raise ValueError("Duplicated or missing planned result")
            proposal = proposals[rid]
            if digest(proposal) != entry["evidence_sha256"]:
                raise ValueError("Proposal evidence changed after planning")
            validate_proposal(proposal, source, records, dataset_records)
            expected = effective_changes(
                proposal,
                entry["protected_manual_override"],
                {
                    **before_rows[rid],
                    "trained_by_paper": entry["before"].get("trained_by_paper"),
                    "repetition_status": entry["before"].get("repetition_status"),
                },
            )
            for conflict in paper.get("application_conflicts", []):
                if conflict.get("result_id") != rid:
                    continue
                field = conflict.get("field")
                if (
                    field != "metric"
                    or conflict.get("reason") != "would_violate_results_unique_key"
                    or expected.get(field) != conflict.get("proposed")
                    or entry["before"].get("metric_name") != conflict.get("old")
                ):
                    raise ValueError("Invalid unique-key conflict record in plan")
                expected.pop(field)
            if expected != entry["changes"] or digest(entry["before"]) != entry["before_sha256"]:
                raise ValueError("Plan changes or rollback snapshot were modified")
            proposals_by_id[rid] = proposal
    return proposals_by_id


def database_changes(
    db: sqlite3.Connection, entry: dict, proposal: dict, created_variants: list
) -> dict:
    changes = entry["changes"]
    unexpected = set(changes) - set(DIRECT_FIELDS) - {"disposition", "reason", "variant", "dataset"}
    if unexpected:
        raise ValueError(f"Unsupported change fields: {sorted(unexpected)}")
    result = {DIRECT_FIELDS[k]: v for k, v in changes.items() if k in DIRECT_FIELDS}
    if "variant" in changes or "dataset" in changes:
        existing = db.execute(
            "SELECT d.id,d.name,v.name FROM dataset_variants v "
            "JOIN datasets d ON d.id=v.dataset_id WHERE v.id=?",
            (entry["before"]["dataset_variant_id"],),
        ).fetchone()
        if existing is None:
            raise ValueError("Existing dataset variant is missing")
        target_dataset_id = existing[0]
        if changes.get("dataset", existing[1]) != existing[1]:
            review = proposal.get("dataset_identity_review")
            if (
                not review
                or review.get("old_dataset") != existing[1]
                or review.get("corrected_dataset") != changes["dataset"]
            ):
                raise ValueError("Dataset reassignment requires matching human source review")
            target = db.execute(
                "SELECT name FROM datasets WHERE id=?", (review["corrected_dataset_id"],)
            ).fetchone()
            if target is None or target[0] != review["corrected_dataset"]:
                raise ValueError("Approved target dataset registration changed")
            target_dataset_id = review["corrected_dataset_id"]
        variant = changes.get("variant", existing[2])
        matches = db.execute(
            "SELECT id FROM dataset_variants WHERE dataset_id=? AND name=?",
            (target_dataset_id, variant),
        ).fetchall()
        if not matches:
            supported = proposal.get("verdict", {}).get("setting_status") == "supported"
            cursor = db.execute(
                "INSERT INTO dataset_variants(dataset_id,name,description,is_standard,created_at) "
                "VALUES(?,?,?,?,?)",
                (
                    target_dataset_id,
                    variant,
                    "Source-backed mapping configuration repair",
                    int(supported),
                    datetime.now(UTC).isoformat(),
                ),
            )
            new_id = cursor.lastrowid
            created_variants.append(
                dict(db.execute("SELECT * FROM dataset_variants WHERE id=?", (new_id,)).fetchone())
            )
            matches = [(new_id,)]
        if len(matches) != 1:
            raise ValueError(f"Configuration has no unique registered variant: {variant}")
        result["dataset_variant_id"] = matches[0][0]
    disposition = changes.get("disposition")
    if disposition:
        if disposition not in {"quarantine", "copied_excluded"}:
            raise ValueError("Unsupported exclusion")
        result.update(
            is_problematic=1,
            problematic_reason=f"Mapping: {changes.get('reason', disposition)}",
        )
        # Excluded rows must not retain a count from a formerly accepted protocol.
        result.update(
            num_runs=None,
            repetition_status="copied" if disposition == "copied_excluded" else "excluded",
        )
    elif "num_runs" in changes:
        result["repetition_status"] = "count"
    if changes:
        result["num_runs_evidence"] = json.dumps(
            {
                "count_unit": "models_trained",
                "action": entry["action"],
                "source_cell": proposal.get("selected_candidate"),
                "protocol_review": proposal.get("protocol_review"),
                "dataset_identity_review": proposal.get("dataset_identity_review"),
                "previous_evidence": entry["before"].get("num_runs_evidence"),
                "evidence_file": entry["evidence_file"],
                "evidence_sha256": entry["evidence_sha256"],
            },
            ensure_ascii=False,
        )
    return result


def update_row(db: sqlite3.Connection, rid: int, values: dict) -> None:
    # Column names come only from schema snapshots or the fixed mapping above.
    columns = {r[1] for r in db.execute("PRAGMA table_info(results)")}
    if not set(values) <= columns - {"id"}:
        raise ValueError("Unknown or forbidden result column")
    if values:
        assignments = ",".join(f'"{column}"=?' for column in values)
        db.execute(f"UPDATE results SET {assignments} WHERE id=?", (*values.values(), rid))


def apply_completed_paper(database: Path, run: Path, manifest: dict, paper: dict) -> dict:
    """Validate and atomically apply one completed paper, with a durable receipt."""
    paper_id = paper["paper_id"]
    folder = run / "papers" / paper_id
    assessment = read_json(folder / "assessment.json")
    if assessment.get("state") != "complete" or assessment.get("errors") != []:
        raise ValueError(f"{paper_id}: only a complete, error-free assessment can be applied")

    source = (folder / "source.tex").read_text()
    local_source = Path(manifest["papers_dir"], paper_id, "latex", "expanded.tex").read_text()
    source_sha256 = hashlib.sha256(source.encode()).hexdigest()
    if source != local_source or paper.get("source_sha256") != source_sha256:
        raise ValueError(f"{paper_id}: frozen and local source do not match")

    frozen_rows = read_json(folder / "rows.json")
    proposals = read_json(folder / "proposals.json")
    row_ids = [row["result_id"] for row in frozen_rows]
    proposal_ids = [proposal["result_id"] for proposal in proposals]
    if len(set(row_ids)) != len(row_ids) or set(row_ids) != set(proposal_ids):
        raise ValueError(f"{paper_id}: proposals do not cover the frozen result rows exactly")

    reviews_path = folder / "reviewed_protocols.json"
    reviews = read_json(reviews_path) if reviews_path.exists() else []
    dataset_reviews = load_reviews(folder, paper)
    for proposal in proposals:
        validate_proposal(proposal, source, reviews, dataset_reviews)

    proposal_by_id = {item["result_id"]: item for item in proposals}
    before_by_id = {row["result_id"]: row for row in frozen_rows}
    plan_id = digest(
        {
            "kind": "completed-paper-application",
            "paper_id": paper_id,
            "source_sha256": source_sha256,
            "implementation_sha256": manifest.get("implementation_sha256"),
            "prompt_sha256": manifest.get("prompt_sha256"),
            "rows_sha256": digest(frozen_rows),
            "proposals_sha256": digest(proposals),
        }
    )
    database_uri = f"{database.resolve().as_uri()}?mode=rw"
    db = sqlite3.connect(database_uri, uri=True, timeout=60)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    try:
        db.execute("BEGIN IMMEDIATE")
        db.execute(
            f"CREATE TABLE IF NOT EXISTS {AUDIT_TABLE} "
            "(plan_id TEXT PRIMARY KEY, state TEXT NOT NULL, receipt TEXT NOT NULL)"
        )
        previous = db.execute(
            f"SELECT state,receipt FROM {AUDIT_TABLE} WHERE plan_id=?", (plan_id,)
        ).fetchone()
        if previous:
            if previous["state"] != "applied":
                raise ValueError(f"{paper_id}: this application was rolled back")
            receipt = json.loads(previous["receipt"])
            for row in receipt.get("snapshot_rows", receipt["rows"]):
                if row_snapshot(db, row["result_id"]) != row["after"]:
                    raise ValueError(f"{paper_id}: an applied row changed after mapping")
            db.commit()
            return {**receipt, "already_applied": True}

        if stored_rows(db, paper_id) != frozen_rows:
            raise ValueError(f"{paper_id}: database rows changed since mapping inputs were frozen")

        entries = []
        for result_id in row_ids:
            before = row_snapshot(db, result_id)
            proposal = proposal_by_id[result_id]
            protected = bool(before.get("is_overridden"))
            projected = before_by_id[result_id]
            comparison_before = {
                **projected,
                "trained_by_paper": before.get("trained_by_paper"),
                "repetition_status": before.get("repetition_status"),
            }
            entries.append(
                {
                    "result_id": result_id,
                    "action": proposal["action"],
                    "protected_manual_override": protected,
                    "before": before,
                    "before_sha256": digest(before),
                    "changes": effective_changes(proposal, protected, comparison_before),
                    "evidence_file": str((folder / "proposals.json").resolve()),
                    "evidence_sha256": digest(proposal),
                }
            )
        conflicts = suppress_metric_unique_conflicts(db, entries)
        receipt = {
            "plan_id": plan_id,
            "paper_id": paper_id,
            "applied_at": datetime.now(UTC).isoformat(),
            "rows": [],
            "snapshot_rows": [],
            "created_variants": [],
            "application_conflicts": conflicts,
        }
        for entry in entries:
            if not entry["changes"]:
                continue
            if entry["protected_manual_override"]:
                raise ValueError(f"{paper_id}/{entry['result_id']}: manual override is protected")
            result_id = entry["result_id"]
            update_row(
                db,
                result_id,
                database_changes(db, entry, proposal_by_id[result_id], receipt["created_variants"]),
            )
            receipt["rows"].append(
                {
                    "result_id": result_id,
                    "before": entry["before"],
                    "after": row_snapshot(db, result_id),
                }
            )
        receipt["snapshot_rows"] = [
            {
                "result_id": result_id,
                "after": row_snapshot(db, result_id),
            }
            for result_id in row_ids
        ]
        db.execute(
            f"INSERT INTO {AUDIT_TABLE} VALUES(?,?,?)",
            (plan_id, "applied", json.dumps(receipt, ensure_ascii=False)),
        )
        db.commit()
        return receipt
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()


def apply_plan(db: sqlite3.Connection, plan: dict) -> dict:
    """All rows or none; audit receipt is committed in the same transaction."""
    if db.in_transaction:
        raise ValueError("Application requires a connection without an active transaction")
    proposals = verify_artifacts(plan)
    plan_id = digest(plan)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.execute("BEGIN IMMEDIATE")
    try:
        db.execute(
            f"CREATE TABLE IF NOT EXISTS {AUDIT_TABLE} "
            "(plan_id TEXT PRIMARY KEY, state TEXT NOT NULL, receipt TEXT NOT NULL)"
        )
        previous = db.execute(
            f"SELECT state,receipt FROM {AUDIT_TABLE} WHERE plan_id=?", (plan_id,)
        ).fetchone()
        if previous:
            if previous["state"] != "applied":
                raise ValueError("This plan was rolled back; create a new reviewed plan")
            receipt = json.loads(previous["receipt"])
            for row in receipt["rows"]:
                if row_snapshot(db, row["result_id"]) != row["after"]:
                    raise ValueError(
                        "Applied row has changed; cannot treat reapplication as a no-op"
                    )
            db.commit()
            return {**receipt, "already_applied": True}
        entries = [e for p in plan["papers"] for e in p["entries"]]
        # Validate the whole cohort before making even the first row change.
        for excluded in plan.get("scope_exclusions", []):
            if stored_rows(db, excluded["paper_id"]) != excluded["rows"]:
                raise ValueError(f"Stale scoped-out rows for paper {excluded['paper_id']}")
        for skipped in plan.get("skipped_papers", []):
            if stored_rows(db, skipped["paper_id"]) != skipped["rows"]:
                raise ValueError(f"Stale skipped rows for {skipped['paper_id']}; rebuild the plan")
        for ignored in plan.get("ignored_papers", []):
            if stored_rows(db, ignored["paper_id"]) != ignored["rows"]:
                raise ValueError(f"Stale ignored rows for {ignored['paper_id']}; rebuild the plan")
        for entry in entries:
            if row_snapshot(db, entry["result_id"]) != entry["before"]:
                raise ValueError(f"Stale row {entry['result_id']}; rebuild and review the plan")
        receipt = {
            "plan_id": plan_id,
            "applied_at": datetime.now(UTC).isoformat(),
            "rows": [],
            "created_variants": [],
        }
        for entry in entries:
            if not entry["changes"]:
                continue
            if entry["before"].get("is_overridden") or entry["protected_manual_override"]:
                raise ValueError("Cannot modify a manually overridden row")
            rid = entry["result_id"]
            update_row(
                db, rid, database_changes(db, entry, proposals[rid], receipt["created_variants"])
            )
            receipt["rows"].append(
                {"result_id": rid, "before": entry["before"], "after": row_snapshot(db, rid)}
            )
        db.execute(
            f"INSERT INTO {AUDIT_TABLE} VALUES(?,?,?)", (plan_id, "applied", json.dumps(receipt))
        )
        db.commit()
        return receipt
    except BaseException:
        db.rollback()
        raise


def rollback_plan(db: sqlite3.Connection, plan_id: str) -> dict:
    """Undo only if every affected row still exactly matches our applied version."""
    if db.in_transaction:
        raise ValueError("Rollback requires a connection without an active transaction")
    db.row_factory = sqlite3.Row
    db.execute("BEGIN IMMEDIATE")
    try:
        record = db.execute(
            f"SELECT state,receipt FROM {AUDIT_TABLE} WHERE plan_id=?", (plan_id,)
        ).fetchone()
        if record is None or record["state"] != "applied":
            raise ValueError("No applied batch to roll back")
        receipt = json.loads(record["receipt"])
        for row in receipt["rows"]:
            if row_snapshot(db, row["result_id"]) != row["after"]:
                raise ValueError(
                    f"Row {row['result_id']} changed after application; rollback refused"
                )
        changed_ids = {r["result_id"] for r in receipt["rows"]}
        for variant in receipt.get("created_variants", []):
            current = db.execute(
                "SELECT * FROM dataset_variants WHERE id=?", (variant["id"],)
            ).fetchone()
            if current is None or dict(current) != variant:
                raise ValueError("Created variant changed after application; rollback refused")
            users = {
                r[0]
                for r in db.execute(
                    "SELECT id FROM results WHERE dataset_variant_id=?", (variant["id"],)
                )
            }
            if not users <= changed_ids:
                raise ValueError("Created variant acquired other results; rollback refused")
        for row in receipt["rows"]:
            update_row(db, row["result_id"], {k: v for k, v in row["before"].items() if k != "id"})
        for variant in receipt.get("created_variants", []):
            db.execute("DELETE FROM dataset_variants WHERE id=?", (variant["id"],))
        db.execute(f"UPDATE {AUDIT_TABLE} SET state='rolled_back' WHERE plan_id=?", (plan_id,))
        db.commit()
        return receipt
    except BaseException:
        db.rollback()
        raise
