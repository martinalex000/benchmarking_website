import hashlib
import json

from backend.mapping.decisions import (
    Protocol,
    grounded_column,
)
from backend.mapping.priority import repair_echo_errors
from backend.mapping.priority_grounding import priority_with_grounding
from backend.mapping.repair_feedback import repair_feedback
from backend.mapping.repairs import adapt_verified_repair
from backend.mapping.source import name_key


def reviewed_protocol(verdict, records, source):
    """A reviewed count cannot supply a cell, origin, eligibility or configuration."""
    result = verdict.model_copy(deep=True)
    index = result.selected_candidate_index
    if index is None or index not in result.verified_candidate_indices:
        return result
    candidate = result.corrected_fact.candidates[index]
    if candidate.eligibility != "benchmark" or not grounded_column(candidate, source):
        return result
    matches = [
        r
        for r in records
        if r["table_id"] == candidate.table_id
        and name_key(r["method"]) == name_key(candidate.method)
    ]
    if not matches:
        return result
    if (
        len(matches) != 1
        or matches[0]["source_sha256"] != hashlib.sha256(source.encode()).hexdigest()
    ):
        raise ValueError("Reviewed protocol source/identity mismatch")
    record = matches[0]
    candidate.protocol = (
        Protocol.model_validate(record["protocol"])
        if "protocol" in record
        else Protocol(
            design="repeated_training",
            training_repetitions=record["count"],
            cv_folds=None,
            cv_repetitions=None,
            dataset_splits=None,
            repetitions_per_split=None,
            reported_runs=record["count"],
            variability_scope="unknown",
            evidence=record["evidence"],
            scope_evidence=record["scope_evidence"],
            explanation=record["interpretation"],
        )
    )
    from backend.mapping.decisions import total_models

    if total_models(candidate.protocol) != record["count"]:
        raise ValueError("Human-reviewed protocol count disagrees with its repetition axes")
    result.protocol_supported = True
    return result


def adapt_outputs(verdicts, rows, source, paper_folder):
    path = paper_folder / "reviewed_protocols.json"
    records = json.loads(path.read_text()) if path.exists() else []
    by_id = {row["result_id"]: row for row in rows}
    result = verdicts.model_copy(deep=True)
    result.verdicts = [
        adapt_verified_repair(by_id[v.result_id], reviewed_protocol(v, records, source), source)
        for v in result.verdicts
    ]
    return result


def has_reviewed_inner_cv(verdict, source, paper_folder):
    path = paper_folder / "reviewed_protocols.json"
    if not path.exists() or verdict.selected_candidate_index is None:
        return False
    candidate = verdict.corrected_fact.candidates[verdict.selected_candidate_index]
    records = json.loads(path.read_text())
    return any(
        r["source_sha256"] == hashlib.sha256(source.encode()).hexdigest()
        and r["table_id"] == candidate.table_id
        and name_key(r["method"]) == name_key(candidate.method)
        and candidate.protocol.design == "repeated_training"
        and candidate.protocol.training_repetitions == r["count"]
        for r in records
    )


def row_errors(row, verdict, fact, source):
    errors = repair_echo_errors(row, verdict) + repair_feedback(row, verdict)
    priority = priority_with_grounding(row, verdict, fact, source)
    if priority:
        errors.append(priority)
    return errors
