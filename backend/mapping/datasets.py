"""Explicitly approved, source-bound dataset identity corrections."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from backend.mapping.schema import Span
from backend.mapping.source import evidence_text, name_key
from backend.result_mapping_checks import same_dataset

ROW_FIELDS = (
    "result_id",
    "model",
    "dataset",
    "variant",
    "metric",
    "value",
    "std",
    "table_ref",
    "source_ref",
    "evaluation_task",
    "protocol_decision",
    "protocol_note",
    "num_runs",
)


def row_digest(row: dict) -> str:
    payload = {key: row.get(key) for key in ROW_FIELDS}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, allow_nan=False).encode()).hexdigest()


def reviewed_dataset(row: dict, source: str, records: list[dict]) -> dict | None:
    matches = [record for record in records if record.get("result_id") == row["result_id"]]
    if not matches:
        return None
    if len(matches) != 1:
        raise ValueError("Duplicated dataset identity review")
    review = matches[0]
    spans = [Span.model_validate(span) for span in review.get("evidence", [])]
    text = evidence_text(spans, source)
    if not (
        review.get("reviewer") == "human_user"
        and review.get("authorization")
        and review.get("old_dataset") == row.get("dataset")
        and review.get("old_row_sha256") == row_digest(row)
        and review.get("source_sha256") == hashlib.sha256(source.encode()).hexdigest()
        and review.get("source_dataset")
        and name_key(review["source_dataset"]) in name_key(text)
        and review.get("corrected_dataset")
        and review["corrected_dataset"] != review["old_dataset"]
        and type(review.get("corrected_dataset_id")) is int
        and review["corrected_dataset_id"] > 0
        and spans
    ):
        raise ValueError("Stale, unbound or unauthorized dataset identity review")
    return review


def project_row(row: dict, source: str, records: list[dict]) -> dict:
    review = reviewed_dataset(row, source, records)
    if review is None:
        return row
    return {**row, "dataset": review["source_dataset"]}


def restore_row(proposal: dict, original: dict, source: str, records: list[dict]) -> dict:
    review = reviewed_dataset(original, source, records)
    result = {**proposal, "dataset": original["dataset"]}
    if review is not None:
        candidate = proposal.get("selected_candidate")
        if candidate and not same_dataset(candidate.get("dataset"), review["source_dataset"]):
            result.update(
                action="dataset_identity_unresolved",
                proposed_num_runs=None,
                correction=None,
                validation_errors=[
                    "Selected source column does not match the approved dataset review"
                ],
            )
            return result
        result["dataset_identity_review"] = review
    return result


def validated_projection(proposal: dict, source: str, records: list[dict]) -> dict:
    supplied = proposal.get("dataset_identity_review")
    if supplied is None:
        return proposal
    review = reviewed_dataset(proposal, source, records)
    if review is None or supplied != review:
        raise ValueError("Dataset correction has no matching frozen authorization")
    candidate = proposal.get("selected_candidate")
    if not candidate or not same_dataset(candidate.get("dataset"), review["source_dataset"]):
        raise ValueError("Dataset correction has no matching source-grounded candidate")
    if proposal.get("dataset") != review["old_dataset"]:
        raise ValueError("Dataset correction does not preserve the frozen old label")
    return {**proposal, "dataset": review["source_dataset"]}


def load_reviews(folder: Path, manifest_paper: dict) -> list[dict]:
    path = folder / "reviewed_datasets.json"
    expected = manifest_paper.get("input_sha256", {}).get(path.name)
    if not path.exists():
        if expected is not None:
            raise ValueError("Frozen dataset authorization is missing")
        return []
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError("Dataset authorization changed after run preparation")
    return json.loads(path.read_text())
