"""Build source-bound change plans without opening a writable database connection.

A plan is a proposal, not an authorization to apply it. Full database-row snapshots
are retained so a later application can reject stale rows and support rollback.
"""

from __future__ import annotations

import hashlib
import json
import math
import sqlite3
from collections import Counter
from pathlib import Path

from backend.mapping.audit import override_counts
from backend.mapping.datasets import load_reviews, validated_projection
from backend.mapping.decisions import (
    Candidate,
    grounded_candidate,
    grounded_column,
    grounded_protocol,
    total_models,
)
from backend.mapping.repair_feedback import configuration_axis_repair_errors
from backend.mapping.schema import stored_rows
from backend.repetition_batch import write_json
from backend.result_mapping_checks import equivalent_number

IGNORED_PAPER_REASONS = {
    "user_confirmed_artifact_ignored",
    "adversarial_examples_not_tracked",
}


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, allow_nan=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def _repair_fields_match(snapshot: dict, correction: dict) -> bool:
    """Accept an unchanged or already-applied repair, with float-noise tolerance."""
    old_fields = correction["old"]
    corrected_fields = correction["corrected"]
    for field, expected in old_fields.items():
        actual = snapshot.get(field)
        if field in {"value", "std"}:
            matches_old = equivalent_number(actual, expected)
            matches_corrected = equivalent_number(actual, corrected_fields[field])
            if not (matches_old or matches_corrected):
                return False
        elif actual not in (expected, corrected_fields[field]):
            return False
    return True


def validate_proposal(
    proposal: dict,
    source: str,
    reviews: list[dict] = (),
    dataset_reviews: list[dict] = (),
) -> None:
    """Reject unsafe actionable outputs; abstentions remain legitimate outcomes."""
    proposal = validated_projection(proposal, source, dataset_reviews)
    action = proposal["action"]
    count = proposal.get("proposed_num_runs")
    if action != "propose_count" and count is not None:
        raise ValueError("Non-count disposition carries a repetition count")
    if action not in {
        "propose_count",
        "copied_excluded",
        "propose_quarantine",
        "numeric_repair_only",
    } and not proposal.get("dataset_identity_review"):
        return
    verdict = proposal.get("verdict", {})
    fact = verdict.get("corrected_fact", {})
    candidate = Candidate.model_validate(proposal.get("selected_candidate"))
    index = verdict.get("selected_candidate_index")
    candidates = fact.get("candidates", [])
    if (
        type(index) is not int
        or index not in verdict.get("verified_candidate_indices", [])
        or not 0 <= index < len(candidates)
    ):
        raise ValueError("Action has no independently selected, verified candidate")
    # Normalization and scoped protocol reviews may update units/axes after the
    # verifier, but cannot substitute a different cell or method identity.
    identity_fields = (
        "table_id",
        "method",
        "dataset",
        "metric",
        "cell_evidence",
        "cell_column_index",
        "row_evidence",
        "column_evidence",
        "configuration_axes",
    )
    if any(candidate.model_dump()[k] != candidates[index].get(k) for k in identity_fields):
        raise ValueError("Action candidate differs from the independently verified cell")
    if grounded_candidate(candidate, source) is None or not grounded_column(candidate, source):
        raise ValueError("Action candidate is not grounded in its physical source cell")
    axis_errors = configuration_axis_repair_errors(
        proposal, candidate.model_dump(), proposal.get("correction")
    )
    if axis_errors:
        raise ValueError(" ".join(axis_errors))
    if action == "copied_excluded" and not (
        verdict.get("origin_supported") is True and fact.get("origin") == "copied"
    ):
        raise ValueError("Copied exclusion lacks independently supported copied origin")
    if action == "propose_quarantine":
        reason = proposal.get("reason")
        excluded = reason == "verifier_excluded" and verdict.get("eligibility") in {
            "ablation",
            "other",
        }
        contradicted = (
            reason == "contradicted_setting"
            and verdict.get("setting_status") == "contradicted"
            and verdict.get("execution_supported") is True
            and fact.get("origin") == "self_evaluated"
        )
        if not (excluded or contradicted):
            raise ValueError("Quarantine lacks a verified eligibility/setting contradiction")
    if action != "propose_count":
        return
    if type(count) is not int or count < 1:
        raise ValueError("Invalid repetition count")
    if not (
        verdict.get("origin_supported") is True
        and verdict.get("execution_supported") is True
        and verdict.get("protocol_supported") is True
        and fact.get("origin") == "self_evaluated"
    ):
        raise ValueError("Count lacks independently verified execution/origin/protocol")
    if candidate.eligibility != "benchmark" or total_models(candidate.protocol) != count:
        raise ValueError("Count conflicts with benchmark eligibility or protocol axes")
    human = [
        record
        for record in reviews
        if record.get("reviewer") == "human_user"
        and record.get("authorization")
        and record.get("source_sha256") == hashlib.sha256(source.encode()).hexdigest()
        and record.get("table_id") == candidate.table_id
        and record.get("method") == candidate.method
        and record.get("count") == count
        and record.get("protocol") == candidate.protocol.model_dump()
    ]
    if (
        not grounded_protocol(candidate.protocol, source, allow_experiments=True)
        and len(human) != 1
    ):
        raise ValueError("Count protocol lacks source-grounded repetition evidence")


def proposed_changes(proposal: dict) -> dict:
    """Use semantic field names; foreign-key resolution belongs to application."""
    action = proposal["action"]
    changes = {}
    if action == "propose_count":
        changes.update(num_runs=proposal["proposed_num_runs"], trained_by_paper=True)
    elif action == "copied_excluded":
        changes.update(num_runs=None, trained_by_paper=False, disposition="copied_excluded")
    elif action == "propose_quarantine":
        changes.update(disposition="quarantine", reason=proposal.get("reason", "unspecified"))
    correction = proposal.get("correction")
    # Withheld/conflicting outcomes must never smuggle repairs into an apply plan.
    if correction and action in {"propose_count", "numeric_repair_only", "copied_excluded"}:
        for field, new in correction["corrected"].items():
            if field not in correction["old"]:
                raise ValueError(f"Repair does not echo old field: {field}")
            if field not in {"value", "std", "model", "metric", "variant"}:
                raise ValueError(f"Unsupported repair field: {field}")
            if field in {"value", "std"} and new is not None and not math.isfinite(new):
                raise ValueError("Non-finite numeric repair")
            if new != correction["old"][field]:
                changes[field] = new
    dataset_review = proposal.get("dataset_identity_review")
    if dataset_review and dataset_review["corrected_dataset"] != dataset_review["old_dataset"]:
        changes["dataset"] = dataset_review["corrected_dataset"]
    return changes


def effective_changes(proposal: dict, protected: bool, before: dict) -> dict:
    """Return only real changes, omitting targets already present in the snapshot."""
    changes = {} if protected else proposed_changes(proposal)

    def current_value(field: str):
        if field == "disposition" and "repetition_status" in before:
            status = before.get("repetition_status")
            if status == "copied":
                return "copied_excluded"
            if status == "excluded":
                return "quarantine"
        return before.get(field)

    return {
        field: value
        for field, value in changes.items()
        if not (
            equivalent_number(before.get(field), value)
            if field in {"value", "std"}
            else current_value(field) == value
        )
    }


def suppress_metric_unique_conflicts(db: sqlite3.Connection, entries: list[dict]) -> list[dict]:
    """Withhold only metric renames that would collide with the results unique key."""
    variants = {
        row[0]: (row[1], row[2])
        for row in db.execute(
            "SELECT v.id,d.name,v.name FROM dataset_variants v "
            "JOIN datasets d ON d.id=v.dataset_id"
        )
    }
    dataset_ids = {row[1]: row[0] for row in db.execute("SELECT id,name FROM datasets")}
    variant_ids = {(row[0], row[1]): row[2] for row in db.execute(
        "SELECT dataset_id,name,id FROM dataset_variants"
    )}

    def target_key(entry: dict):
        before = entry["before"]
        changes = entry["changes"]
        old_dataset, old_variant = variants[before["dataset_variant_id"]]
        dataset_name = changes.get("dataset", old_dataset)
        dataset_id = dataset_ids.get(dataset_name)
        if dataset_id is None:
            raise ValueError(f"Unknown target dataset in result {entry['result_id']}")
        variant_name = changes.get("variant", old_variant)
        variant_id = variant_ids.get((dataset_id, variant_name))
        if variant_id is None:
            variant_id = ("new_variant", dataset_id, variant_name)
        return (
            before["paper_id"],
            before["model_id"],
            variant_id,
            changes.get("metric", before["metric_name"]),
        )

    conflicts = []
    while True:
        entries_by_key = {}
        for entry in entries:
            key = target_key(entry)
            entries_by_key.setdefault(key, []).append(entry)
        duplicate_groups = [items for items in entries_by_key.values() if len(items) > 1]
        if not duplicate_groups:
            return conflicts

        changed = False
        for group in duplicate_groups:
            ids = sorted(entry["result_id"] for entry in group)
            proposed = [entry for entry in group if "metric" in entry["changes"]]
            if not proposed:
                raise ValueError(f"Unique-key collision cannot be resolved by metric guard: {ids}")
            for entry in proposed:
                old = entry["before"]["metric_name"]
                new = entry["changes"].pop("metric")
                conflicts.append(
                    {
                        "result_id": entry["result_id"],
                        "field": "metric",
                        "old": old,
                        "proposed": new,
                        "conflicting_result_ids": ids,
                        "reason": "would_violate_results_unique_key",
                    }
                )
                changed = True
        if not changed:
            raise ValueError("Unique-key collision remains after metric guard")


def build_plan(
    run: Path,
    database: Path,
    papers: Path,
    output: Path,
    *,
    allow_partial: bool = False,
    eligible_models: set[str] | None = None,
    ignored_paper_ids: set[str] | None = None,
    ignored_paper_reasons: dict[str, str] | None = None,
) -> dict:
    """Validate saved assessments against live rows and local LaTeX.

    Partial plans explicitly freeze and skip every paper without a complete,
    eligible-model assessment. The full cohort is still snapshot-checked.
    """
    status = read_json(run / "status.json")
    terminal = status.get("state") == "finished" or (
        status.get("pipeline_terminal") is True and status.get("phase") == "complete"
    )
    if not allow_partial and status.get("selected_rows_unchanged") is not True:
        raise ValueError("Run has no verified unchanged-row check")
    if not allow_partial and not terminal:
        raise ValueError("Run is not terminal")
    if not allow_partial and status.get("phase") not in (None, "complete", "saved_output_recheck"):
        raise ValueError("Independent verification phase is not complete")
    if not allow_partial and status.get("scope_unchanged") is not True:
        raise ValueError("Scoped-out result rows have no terminal unchanged-row check")
    manifest = read_json(run / "manifest.json")
    scope = read_json(run / "scope.json")
    plan = {
        "version": 1,
        "mode": "dry_run",
        "coverage_mode": "partial_skips" if allow_partial else "complete",
        "database_modified": False,
        "count_unit": "models_trained",
        "run": str(run.resolve()),
        "manifest_sha256": digest(manifest),
        "scope_sha256": digest(scope),
        "scope_exclusions": scope["excluded_papers"],
        "papers": [],
        "skipped_papers": [],
        "ignored_papers": [],
    }
    # SQLite read-only mode also prevents accidentally creating a missing database.
    with sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True) as db:
        db.execute("PRAGMA query_only=ON")
        db.execute("BEGIN")
        ignored_paper_ids = ignored_paper_ids or set()
        ignored_paper_reasons = ignored_paper_reasons or {}
        if set(ignored_paper_reasons) - ignored_paper_ids:
            raise ValueError("Ignored-paper reasons supplied for IDs not marked ignored")
        included_ids = {paper["paper_id"] for paper in manifest["papers"]}
        excluded_ids = {paper["paper_id"] for paper in scope["excluded_papers"]}
        if ignored_paper_ids & (included_ids | excluded_ids):
            raise ValueError("Ignored paper IDs overlap the frozen run scope")
        for paper_id in sorted(ignored_paper_ids):
            rows = stored_rows(db, paper_id)
            if not rows:
                raise ValueError(f"Ignored paper has no stored results: {paper_id}")
            reason = ignored_paper_reasons.get(paper_id, "user_confirmed_artifact_ignored")
            if reason not in IGNORED_PAPER_REASONS:
                raise ValueError(f"Unsupported ignored-paper reason for {paper_id}: {reason}")
            plan["ignored_papers"].append(
                {
                    "paper_id": paper_id,
                    "reason": reason,
                    "rows": rows,
                }
            )
        for excluded in scope["excluded_papers"]:
            if stored_rows(db, excluded["paper_id"]) != excluded["rows"]:
                raise ValueError(
                    f"{excluded['paper_id']}: scoped-out rows changed since the dry run"
                )
        for paper in manifest["papers"]:
            pid = paper["paper_id"]
            folder = run / "papers" / pid
            frozen = read_json(folder / "rows.json")
            current = stored_rows(db, pid)
            if current != frozen:
                raise ValueError(f"{pid}: stored rows changed since the dry-run")
            source = (folder / "source.tex").read_text()
            local = (papers / pid / "latex" / "expanded.tex").read_text()
            if source != local:
                raise ValueError(f"{pid}: local LaTeX changed since assessment")
            source_hash = hashlib.sha256(source.encode()).hexdigest()
            if paper.get("source_sha256") not in (None, source_hash):
                raise ValueError(f"{pid}: source disagrees with frozen manifest")
            assessment_path = folder / "assessment.json"
            assessment = read_json(assessment_path) if assessment_path.exists() else {}
            model = paper.get("model", manifest.get("model"))
            is_eligible = eligible_models is None or model in eligible_models
            if (
                allow_partial
                and (
                    not is_eligible
                    or assessment.get("state") != "complete"
                    or assessment.get("errors") != []
                )
            ):
                plan["skipped_papers"].append(
                    {
                        "paper_id": pid,
                        "model": model,
                        "assessment_state": assessment.get("state", "missing"),
                        "assessment_errors": assessment.get("errors", []),
                        "reason": (
                            "model_not_eligible"
                            if not is_eligible
                            else "assessment_incomplete_or_failed"
                        ),
                        "source_sha256": source_hash,
                        "rows": frozen,
                    }
                )
                continue
            if assessment.get("state") != "complete" or assessment.get("errors") != []:
                raise ValueError(f"{pid}: assessment failed or incomplete")
            proposals = read_json(folder / "proposals.json")
            reviews_path = folder / "reviewed_protocols.json"
            reviews = read_json(reviews_path) if reviews_path.exists() else []
            dataset_reviews = load_reviews(folder, paper)
            ids = [p["result_id"] for p in proposals]
            if len(ids) != len(set(ids)) or set(ids) != {r["result_id"] for r in frozen}:
                raise ValueError(f"{pid}: missing, duplicated or invented proposal IDs")
            old_by_id = {r["result_id"]: r for r in frozen}
            entries = []
            for proposal in proposals:
                rid = proposal["result_id"]
                validate_proposal(proposal, source, reviews, dataset_reviews)
                correction = proposal.get("correction")
                if correction and not _repair_fields_match(old_by_id[rid], correction):
                    raise ValueError(f"{pid}/{rid}: repair old fields do not match snapshot")
                raw = db.execute("SELECT * FROM results WHERE id=?", (rid,)).fetchone()
                snapshot = dict(raw)
                protected = bool(snapshot.get("is_overridden"))
                before_projection = old_by_id[rid]
                comparison_before = {
                    **before_projection,
                    "trained_by_paper": snapshot.get("trained_by_paper"),
                    "repetition_status": snapshot.get("repetition_status"),
                }
                changes = effective_changes(proposal, protected, comparison_before)
                entries.append(
                    {
                        "result_id": rid,
                        "action": proposal["action"],
                        "protected_manual_override": protected,
                        "before": snapshot,
                        "before_sha256": digest(snapshot),
                        "changes": changes,
                        "evidence_sha256": digest(proposal),
                        "evidence_file": str((folder / "proposals.json").resolve()),
                    }
                )
            application_conflicts = suppress_metric_unique_conflicts(db, entries)
            plan["papers"].append(
                {
                    "paper_id": pid,
                    "model": model,
                    "source_sha256": source_hash,
                    "source_file": str((folder / "source.tex").resolve()),
                    "local_source_file": str((papers / pid / "latex" / "expanded.tex").resolve()),
                    "decisions": dict(Counter(p["action"] for p in proposals)),
                    "override_counts": override_counts(proposals),
                    "application_conflicts": application_conflicts,
                    "entries": entries,
                }
            )
    output.mkdir(parents=True, exist_ok=True)
    destination = output / "change_plan.json"
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing plan: {destination}")
    write_json(destination, plan)
    (output / "override_counts.log").write_text(
        "Dry-run override counts only; no database changes. Types can overlap.\n"
        + "\n".join(
            f"{p['paper_id']} | "
            + ", ".join(f"{k}={v}" for k, v in p["override_counts"]["types"].items())
            + f" | protected={sum(e['protected_manual_override'] for e in p['entries'])}"
            for p in plan["papers"]
        )
        + "\n"
    )
    (output / "application_conflicts.log").write_text(
        "Metric corrections withheld to preserve the results uniqueness constraint.\n"
        + "\n".join(
            f"{paper['paper_id']} | result {item['result_id']} | "
            f"metric {item['old']!r} -> {item['proposed']!r} withheld; "
            f"collides with {item['conflicting_result_ids']}"
            for paper in plan["papers"]
            for item in paper.get("application_conflicts", [])
        )
        + "\n"
    )
    count = sum(bool(e["changes"]) for p in plan["papers"] for e in p["entries"])
    selected_models = Counter(paper["model"] for paper in plan["papers"])
    withheld_metrics = sum(len(paper.get("application_conflicts", [])) for paper in plan["papers"])
    (output / "summary.md").write_text(
        "# Mapping change plan\n\n"
        f"Checked {len(plan['papers'])} papers; {count} rows have proposed changes.\n"
        f"Selected by model: {dict(selected_models)}.\n"
        f"Skipped {len(plan['skipped_papers'])} papers; explicitly ignored "
        f"{len(plan['ignored_papers'])} artifact papers.\n"
        f"Withheld {withheld_metrics} metric corrections to prevent DB key collisions.\n\n"
        "Database unchanged. Manual overrides are protected. Counts use models trained, "
        "retaining the CV axes in the linked evidence. This plan does not authorize applying "
        "changes; copied exclusions and quarantines are proposed, not executed.\n"
    )
    return plan
