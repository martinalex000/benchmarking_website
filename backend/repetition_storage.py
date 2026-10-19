"""Apply uniform protocols conservatively; table-dependent rows require review."""

from __future__ import annotations

import hashlib
import json
import re
from contextlib import nullcontext
from pathlib import Path

from backend.db import session_scope
from backend.models import ModelAlias, Paper, RepetitionAssessment, Result
from backend.repetition_extractor import DEFAULT_MODEL
from backend.repetition_metadata import RepetitionFacts, Verification, validate_repetitions

PRODUCTION_MODELS = {DEFAULT_MODEL, "glm-5.3-flash"}


def name_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.casefold())


def total_models_trained(repetitions: int | None, cv_folds: int | None, design: str) -> int | None:
    """Convert the reported repetition protocol into the agreed model-fit count."""
    if design == "repeated_cv":
        if repetitions is None or cv_folds is None:
            return None
        return repetitions * cv_folds
    if design == "single_cv":
        return cv_folds
    if design == "repeated_training":
        return repetitions
    # Nested/unknown protocols need an explicit row-level resolution.
    return None


def paper_protocol(analysis: dict) -> tuple[str, int | None]:
    if analysis.get("error"):
        return "failed", None
    validated = analysis["validated"]
    coverage = validated.get("coverage", {})
    if any(coverage.get(key) for key in coverage):
        return "table_dependent", None
    tables = validated["table_outcomes"]
    benchmarks = [t for t in tables if t["outcome"] != "excluded"]
    if not benchmarks:
        return "unknown", None
    if all(t["outcome"] == "unknown" for t in benchmarks):
        return "unknown", None
    if any(t["outcome"] != "count" for t in benchmarks):
        return "table_dependent", None
    protocols = {(m["repetitions"], m["cv_folds"], m["design"]) for m in validated["accepted"]}
    # Baselines with explicit different repeats also make the paper non-uniform.
    if len(protocols) != 1:
        return "table_dependent", None
    if any(
        m.get("candidate_repetitions") is not None
        and m.get("candidate_repetitions") != next(iter(protocols))[0]
        for m in validated.get("withheld", [])
        if m["origin"] == "self_evaluated" and "ablation_variant_not_eligible" not in m["flags"]
    ):
        return "table_dependent", None
    repetitions, cv_folds, design = next(iter(protocols))
    return "uniform", total_models_trained(repetitions, cv_folds, design)


def apply_assessment(
    arxiv_id: str,
    analysis: dict,
    source: str,
    artifact: Path,
    *,
    session=None,
) -> dict:
    """Revalidate original source before linking rows; never delete or change scores."""
    provenance = analysis["provenance"]
    if provenance["model"] not in PRODUCTION_MODELS:
        raise ValueError("Production repetition metadata must use a configured GLM-5.3-Flash route")
    if hashlib.sha256(source.encode()).hexdigest() != provenance["source_sha256"]:
        raise ValueError("Assessment source hash mismatch")
    if not analysis.get("error"):
        analysis = {
            **analysis,
            "validated": validate_repetitions(
                RepetitionFacts.model_validate(analysis["facts"]),
                Verification.model_validate(analysis["verification"]),
                source,
            ),
        }
    status, count = paper_protocol(analysis)
    prompts = json.dumps(provenance["prompt_sha256"], sort_keys=True)
    counts = {"linked": 0, "assigned": 0, "copied": 0, "conflicts": 0}
    scope = session_scope() if session is None else nullcontext(session)
    with scope as active_session:
        paper = active_session.query(Paper).filter_by(arxiv_id=arxiv_id).one()
        assessment = (
            active_session.query(RepetitionAssessment)
            .filter_by(
                paper_id=paper.id, source_sha256=provenance["source_sha256"], prompt_sha256=prompts
            )
            .one_or_none()
        )
        if assessment is None:
            assessment = RepetitionAssessment(
                paper_id=paper.id,
                source_sha256=provenance["source_sha256"],
                prompt_sha256=prompts,
                model=provenance["model"],
            )
            active_session.add(assessment)
        prior_audit = (
            json.loads(assessment.payload).get("row_update_audit", []) if assessment.payload else []
        )
        assessment.status = status
        assessment.uniform_num_runs = count
        assessment.payload = json.dumps(analysis, ensure_ascii=False)
        assessment.artifact_path = str(artifact.resolve())
        active_session.flush()
        rows = active_session.query(Result).filter_by(paper_id=paper.id).all()
        accepted = analysis["validated"].get("accepted", []) if status == "uniform" else []
        audit = []
        for row in rows:
            audit.append(
                {
                    "result_id": row.id,
                    "previous_num_runs": row.num_runs,
                    "previous_trained_by_paper": row.trained_by_paper,
                    "previous_evidence": row.num_runs_evidence,
                    "previous_assessment_id": row.repetition_assessment_id,
                    "previous_status": row.repetition_status,
                }
            )
            row.repetition_assessment_id = assessment.id
            counts["linked"] += 1
            # Human overrides remain authoritative, including run metadata.
            if row.is_overridden:
                continue
            if status != "uniform":
                row.repetition_status = "table_pending" if status == "table_dependent" else status
                if status in {"table_dependent", "unknown"}:
                    row.num_runs = None
                    row.num_runs_evidence = None
                continue
            if row.source_paper_id not in {None, paper.id} or (
                row.source_ref and row.source_ref.strip().casefold() != "this paper"
            ):
                row.num_runs = None
                row.trained_by_paper = 0
                row.num_runs_evidence = None
                row.repetition_status = "copied"
                counts["copied"] += 1
                continue
            names = {name_key(row.model.name), name_key(row.model.canonical_name)}
            if row.model_name_override:
                names.add(name_key(row.model_name_override))
            names.update(
                name_key(a.alias)
                for a in active_session.query(ModelAlias).filter_by(model_id=row.model_id)
            )
            matched = [m for m in accepted if name_key(m["name"]) in names]
            benchmark_ids = {
                t["table_id"]
                for t in analysis["validated"]["table_outcomes"]
                if t["outcome"] == "count"
            }
            # A method rerun in one table can still be copied in another. Without
            # row-to-table attribution, require proof in every benchmark table.
            if {m["table_id"] for m in matched} != benchmark_ids:
                matched = []
            if not matched:
                row.num_runs = None
                row.num_runs_evidence = None
                row.repetition_status = "unknown"
                continue
            if row.num_runs is not None and row.num_runs != count:
                row.num_runs = None
                row.num_runs_evidence = None
                row.repetition_status = "conflict"
                counts["conflicts"] += 1
                continue
            row.num_runs = count
            row.trained_by_paper = 1
            row.num_runs_evidence = json.dumps(
                [m["evidence_by_purpose"] for m in matched], ensure_ascii=False
            )
            row.repetition_status = "count"
            counts["assigned"] += 1
        # Keep the pre-update metadata for inspection/recovery, without touching scores.
        previous_ids = {r["result_id"] for r in prior_audit}
        analysis["row_update_audit"] = prior_audit + [
            r for r in audit if r["result_id"] not in previous_ids
        ]
        assessment.payload = json.dumps(analysis, ensure_ascii=False)
    return {"paper_id": arxiv_id, "status": status, "uniform_num_runs": count, **counts}
