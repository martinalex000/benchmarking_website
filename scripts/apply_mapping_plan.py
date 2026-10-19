"""Apply or roll back a saved result-mapping plan with explicit write confirmation."""

from __future__ import annotations

import argparse
import sqlite3
import sys
from contextlib import closing
from pathlib import Path

from backend.config import cfg
from backend.mapping.batch import check_inputs
from backend.mapping.plan import IGNORED_PAPER_REASONS, build_plan, digest, read_json
from backend.mapping.schema import stored_rows
from backend.mapping.storage import apply_plan, rollback_plan
from backend.venue import conference_export_fields


def _open_database(database: Path) -> sqlite3.Connection:
    if not database.is_file():
        raise ValueError(f"Database does not exist: {database}")
    return sqlite3.connect(f"{database.resolve().as_uri()}?mode=rw", uri=True)


def _already_applied(database: Path, plan: dict) -> bool:
    if not database.is_file():
        return False
    uri = f"{database.resolve().as_uri()}?mode=ro"
    with sqlite3.connect(uri, uri=True) as db:
        table = db.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='mapping_change_batches'"
        ).fetchone()
        if not table:
            return False
        row = db.execute(
            "SELECT state FROM mapping_change_batches WHERE plan_id=?", (digest(plan),)
        ).fetchone()
        return bool(row and row[0] == "applied")


def _validate_plan_coverage(plan: dict) -> None:
    """Refuse accidental truncation before opening the database for writing."""
    if not isinstance(plan, dict):
        raise ValueError("Change plan must be a JSON object")
    run_path = plan.get("run")
    if not isinstance(run_path, str) or not run_path:
        raise ValueError("Change plan has no valid run directory")
    run = Path(run_path)
    manifest = read_json(run / "manifest.json")
    if not isinstance(manifest, dict) or not isinstance(manifest.get("papers"), list):
        raise ValueError("Manifest has no paper list")
    manifest_papers = manifest["papers"]
    planned_papers = plan.get("papers")
    skipped_papers = plan.get("skipped_papers", [])
    ignored_papers = plan.get("ignored_papers", [])
    if not isinstance(planned_papers, list):
        raise ValueError("Change plan has no paper list")
    if not isinstance(skipped_papers, list):
        raise ValueError("Change plan skipped-paper ledger must be a list")
    if not isinstance(ignored_papers, list):
        raise ValueError("Change plan ignored-paper ledger must be a list")
    if any(
        not isinstance(paper, dict) or not isinstance(paper.get("paper_id"), str)
        for paper in manifest_papers + planned_papers + skipped_papers + ignored_papers
    ):
        raise ValueError("Manifest and plan paper IDs must be strings")
    manifest_ids = [paper["paper_id"] for paper in manifest_papers]
    planned_ids = [paper["paper_id"] for paper in planned_papers]
    skipped_ids = [paper["paper_id"] for paper in skipped_papers]
    ignored_ids = [paper["paper_id"] for paper in ignored_papers]
    if len(set(manifest_ids)) != len(manifest_ids):
        raise ValueError("Manifest contains duplicate papers")
    if (
        len(set(planned_ids + skipped_ids)) != len(planned_ids) + len(skipped_ids)
        or set(planned_ids + skipped_ids) != set(manifest_ids)
        or set(ignored_ids) & (set(manifest_ids) | set(skipped_ids))
        or len(set(ignored_ids)) != len(ignored_ids)
    ):
        raise ValueError(
            "Plan does not cover every paper exactly once: each manifest paper must be applied "
            "or explicitly skipped"
        )
    manifest_by_id = {paper["paper_id"]: paper for paper in manifest_papers}

    seen_result_ids = set()
    for paper in skipped_papers:
        folder = run / "papers" / paper["paper_id"]
        rows = read_json(folder / "rows.json")
        if paper.get("rows") != rows:
            raise ValueError(f"{paper['paper_id']}: skipped row snapshot differs from the run")
        row_ids = [row["result_id"] for row in rows]
        if any(type(result_id) is not int for result_id in row_ids):
            raise ValueError(f"{paper['paper_id']}: result IDs must be integers")
        if len(set(row_ids)) != len(row_ids) or seen_result_ids.intersection(row_ids):
            raise ValueError("Skipped result IDs are duplicated across papers")
        seen_result_ids.update(row_ids)

    for paper in planned_papers:
        paper_id = paper["paper_id"]
        check_inputs(manifest, run, manifest_by_id[paper_id])
        folder = run / "papers" / paper_id
        rows = read_json(folder / "rows.json")
        proposals = read_json(folder / "proposals.json")
        entries = paper.get("entries")
        if not isinstance(rows, list) or not isinstance(proposals, list):
            raise ValueError(f"{paper['paper_id']}: rows and proposals must be lists")
        if not isinstance(entries, list) or any(
            not isinstance(item, dict) for item in rows + proposals + entries
        ):
            raise ValueError(f"{paper['paper_id']}: rows, proposals and entries must be objects")
        row_ids = [row["result_id"] for row in rows]
        proposal_ids = [proposal["result_id"] for proposal in proposals]
        entry_ids = [entry["result_id"] for entry in entries]
        if any(type(result_id) is not int for result_id in row_ids + proposal_ids + entry_ids):
            raise ValueError(f"{paper_id}: result IDs must be integers")
        if (
            len(set(row_ids)) != len(row_ids)
            or len(set(proposal_ids)) != len(proposal_ids)
            or len(set(entry_ids)) != len(entry_ids)
            or set(row_ids) != set(proposal_ids)
            or set(row_ids) != set(entry_ids)
        ):
            raise ValueError(f"{paper_id}: plan must cover every result row exactly once")
        if seen_result_ids.intersection(row_ids):
            raise ValueError("Result IDs appear under more than one paper")
        seen_result_ids.update(row_ids)
    expected_result_ids = {
        row["result_id"]
        for paper_id in manifest_ids
        for row in read_json(run / "papers" / paper_id / "rows.json")
    }
    if seen_result_ids != expected_result_ids:
        raise ValueError("Plan does not cover every result row in the manifest")


def _validate_full_cohort(plan: dict, database: Path) -> None:
    """Reject a plan that omits eligible papers or stale scoped-out rows."""
    run = Path(plan["run"])
    manifest = read_json(run / "manifest.json")
    scope = read_json(run / "scope.json")
    if digest(manifest) != plan.get("manifest_sha256"):
        raise ValueError("Manifest changed after plan generation")
    if digest(scope) != plan.get("scope_sha256"):
        raise ValueError("Scope ledger changed after plan generation")
    if scope.get("excluded_papers") != plan.get("scope_exclusions"):
        raise ValueError("Scope exclusions changed after plan generation")

    included = {paper["paper_id"] for paper in manifest["papers"]}
    excluded_records = scope["excluded_papers"]
    excluded = {paper["paper_id"] for paper in excluded_records}
    ignored_records = plan.get("ignored_papers", [])
    ignored = {paper["paper_id"] for paper in ignored_records}
    if len(ignored) != len(ignored_records):
        raise ValueError("Plan has duplicate ignored paper IDs")
    if len(included) != len(manifest["papers"]) or len(excluded) != len(excluded_records):
        raise ValueError("Run scope contains duplicate paper IDs")
    if (included & excluded) or (included & ignored) or (excluded & ignored):
        raise ValueError("A paper appears in multiple scope dispositions")

    uri = f"{database.resolve().as_uri()}?mode=ro"
    with sqlite3.connect(uri, uri=True) as db:
        db.execute("PRAGMA query_only=ON")
        columns = {row[1] for row in db.execute("PRAGMA table_info(papers)")}
        required = {"arxiv_id", "venue", "published_date"}
        if not required <= columns:
            raise ValueError("Database lacks fields needed to validate conference coverage")
        cohort = {
            row[0]
            for row in db.execute(
                "SELECT p.arxiv_id,p.venue,p.published_date FROM papers p "
                "WHERE p.arxiv_id IS NOT NULL "
                "AND EXISTS(SELECT 1 FROM results r WHERE r.paper_id=p.id)"
            )
            if conference_export_fields(row[1], row[2])["published_conference"]
        }
        represented = included | excluded | ignored
        if represented != cohort:
            missing = sorted(cohort - represented)
            extra = sorted(represented - cohort)
            raise ValueError(
                f"Plan does not cover the full conference cohort; missing={missing}, extra={extra}"
            )

        excluded_by_id = {paper["paper_id"]: paper for paper in excluded_records}
        ignored_by_id = {paper["paper_id"]: paper for paper in ignored_records}
        for paper_id in cohort:
            if paper_id in included:
                frozen_rows = read_json(run / "papers" / paper_id / "rows.json")
            elif paper_id in ignored_by_id:
                if ignored_by_id[paper_id].get("reason") not in IGNORED_PAPER_REASONS:
                    raise ValueError(f"{paper_id}: ignored cohort paper lacks explicit approval")
                frozen_rows = ignored_by_id[paper_id]["rows"]
            else:
                frozen_rows = excluded_by_id[paper_id]["rows"]
            if stored_rows(db, paper_id) != frozen_rows:
                raise ValueError(f"{paper_id}: result rows changed after the dry-run")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)

    apply = commands.add_parser("apply", help="Apply a saved, validated change plan")
    apply.add_argument("--plan", type=Path, required=True, help="Saved change_plan.json")
    _add_write_confirmation(apply)

    apply_run = commands.add_parser(
        "apply-run", help="Build and apply proposals collected by a map-results run"
    )
    apply_run.add_argument("--run-dir", type=Path, required=True)
    apply_run.add_argument(
        "--include-finished-only",
        action="store_true",
        help="Confirm applying successful papers while explicitly skipping incomplete/failed papers",
    )
    _add_write_confirmation(apply_run)

    rollback = commands.add_parser("rollback", help="Undo a previously applied plan")
    rollback.add_argument("--plan-id", required=True, help="Plan ID printed by the apply command")
    _add_write_confirmation(rollback)

    return parser


def _add_write_confirmation(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--database", type=Path, default=cfg.db_path)
    parser.add_argument(
        "--confirm-database-write",
        action="store_true",
        required=True,
        help="Confirm that this command may write to the target database",
    )


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.action == "apply-run":
            manifest = read_json(args.run_dir / "manifest.json")
            if manifest.get("database_mode") not in {"collect-only", "read_only"}:
                raise ValueError(
                    "apply-run is only for runs prepared with --database-mode collect-only"
                )
            status = read_json(args.run_dir / "status.json")
            if status.get("state") != "finished":
                raise ValueError(
                    "Run must be stopped and terminal before applying collected papers"
                )
            incomplete = status.get("failed", 0) > 0 or status.get("successful", 0) < status.get(
                "total", 0
            )
            allow_partial = False
            if incomplete:
                message = (
                    f"Run has {status.get('successful', 0)} successful and "
                    f"{status.get('failed', 0)} failed/incomplete paper(s). Apply successful papers only?"
                )
                if args.include_finished_only:
                    print(message + " Confirmed by --include-finished-only.")
                    allow_partial = True
                elif sys.stdin.isatty():
                    answer = input(message + " [y/N] ").strip().casefold()
                    if answer not in {"y", "yes"}:
                        print("Apply cancelled.")
                        return 1
                    allow_partial = True
                else:
                    raise ValueError(
                        message
                        + " Re-run with --include-finished-only to confirm the partial apply."
                    )
            application_dir = args.run_dir / "application"
            plan_path = application_dir / "change_plan.json"
            if plan_path.exists():
                plan = read_json(plan_path)
            else:
                plan = build_plan(
                    args.run_dir,
                    args.database,
                    Path(manifest["papers_dir"]),
                    application_dir,
                    allow_partial=allow_partial,
                )
            _validate_plan_coverage(plan)
            if not _already_applied(args.database, plan):
                _validate_full_cohort(plan, args.database)
        else:
            plan = read_json(args.plan) if args.action == "apply" else None
        if plan is not None and args.action == "apply":
            _validate_plan_coverage(plan)
            if not _already_applied(args.database, plan):
                _validate_full_cohort(plan, args.database)
        with closing(_open_database(args.database)) as db, db:
            if args.action in {"apply", "apply-run"}:
                receipt = apply_plan(db, plan)
                state = "already applied" if receipt.get("already_applied") else "applied"
                print(
                    f"Mapping plan {state}: {len(receipt['rows'])} rows; "
                    f"plan ID {receipt['plan_id']}."
                )
            else:
                receipt = rollback_plan(db, args.plan_id)
                print(
                    f"Mapping plan rolled back: {len(receipt['rows'])} rows; "
                    f"plan ID {args.plan_id}."
                )
    except (OSError, ValueError, TypeError, sqlite3.Error, KeyError) as exc:
        print(f"Mapping plan refused: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
