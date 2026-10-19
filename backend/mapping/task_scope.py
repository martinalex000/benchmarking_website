"""Evaluation-target checks for the next frozen mapping revision.

These checks do not run in the active V3 experiment. Independent verification must
establish metric/task compatibility separately from finding a literal table cell.
"""

from __future__ import annotations

import copy
import hashlib
from typing import Literal

from pydantic import StrictBool, StrictInt

from backend.mapping.binding import candidate_identity
from backend.mapping.decisions import metric_key
from backend.mapping.schema import Span, StrictModel
from backend.mapping.source import evidence_text


class TaskScopeReview(StrictModel):
    result_id: StrictInt
    independently_verified: StrictBool
    source_sha256: str
    candidate_sha256: str
    intended_task: str
    measured_task: str
    measured_metric: str
    decision: Literal["compatible", "incompatible", "unclear"]
    task_evidence: list[Span]
    cell_scope_evidence: list[Span]
    explanation: str
    call_refs: list[str]


def guard_task_scope(row: dict, source: str, review: TaskScopeReview | None) -> dict:
    """Fail closed on missing/stale reviews without inventing metric corrections.

    Semantic compatibility is an independent verifier judgment, not a keyword
    heuristic. Bind that judgment to the intended task and exact selected cell;
    table-level source evidence and a task-defining paragraph are both required.
    """
    result = copy.deepcopy(row)
    candidate = row.get("selected_candidate")
    if candidate is None:
        return result
    valid = (
        review is not None
        and review.independently_verified
        and review.result_id == row["result_id"]
        and review.source_sha256 == hashlib.sha256(source.encode()).hexdigest()
        and review.candidate_sha256 == candidate_identity(candidate)
        and bool(row.get("evaluation_task"))
        and review.intended_task == row["evaluation_task"]
        and bool(review.measured_task.strip())
        and bool(review.measured_metric.strip())
        and bool(review.explanation.strip())
        and bool(review.call_refs)
        and bool(evidence_text(review.task_evidence, source))
        and bool(evidence_text(review.cell_scope_evidence, source))
        and any(
            span.start_line <= candidate["cell_evidence"]["start_line"] <= span.end_line
            for span in review.cell_scope_evidence
        )
    )
    compatible = (
        valid
        and review.decision == "compatible"
        and review.measured_task == review.intended_task
        and metric_key(review.measured_metric) == metric_key(candidate.get("metric", ""))
    )
    if compatible:
        result["task_scope_review"] = review.model_dump()
        return result
    if row.get("correction"):
        result["withheld_task_scope_repair"] = result.pop("correction")
        result["correction"] = None
    result["proposed_num_runs"] = None
    if valid and review.decision == "incompatible":
        result["action"] = "propose_quarantine"
        result["task_scope_review"] = review.model_dump()
        result["reason"] = "incompatible_evaluation_target"
        result["task_scope_explanation"] = (
            "Source evaluation target is incompatible with the intended benchmark task."
        )
    else:
        result["action"] = "task_scope_unresolved"
        result["reason"] = "Missing, unclear, or stale independent evaluation-target review."
    return result
