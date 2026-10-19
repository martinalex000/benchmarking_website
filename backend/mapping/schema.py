from __future__ import annotations

import sqlite3
from dataclasses import asdict
from datetime import UTC, datetime, timedelta
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from backend.llm_tasks import LLMExtractor
from backend.repetition_batch import write_json


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Span(StrictModel):
    start_line: int
    end_line: int


def stored_rows(db: sqlite3.Connection, pid: str) -> list[dict]:
    db.row_factory = sqlite3.Row
    return [
        dict(row)
        for row in db.execute(
            "SELECT r.id AS result_id,coalesce(r.model_name_override,m.name) AS model,"
            "d.name AS dataset,v.name AS variant,r.metric_name AS metric,"
            "r.metric_value AS value,r.metric_std AS std,r.table_ref,r.source_ref,"
            "r.evaluation_task,r.protocol_decision,r.protocol_note,r.num_runs "
            "FROM results r JOIN papers p ON p.id=r.paper_id "
            "JOIN models m ON m.id=r.model_id "
            "JOIN dataset_variants v ON v.id=r.dataset_variant_id "
            "JOIN datasets d ON d.id=v.dataset_id WHERE p.arxiv_id=? ORDER BY r.id",
            (pid,),
        )
    ]


def exact_coverage(items: list, rows: list[dict]) -> None:
    ids = [item.result_id for item in items]
    if len(set(ids)) != len(ids) or set(ids) != {row["result_id"] for row in rows}:
        raise ValueError("Missing, duplicate or invented result IDs")


def span_text(span: Span | None, table: dict, source: str) -> str:
    if span is None:
        return ""
    if not table["start_line"] <= span.start_line <= span.end_line <= table["end_line"]:
        return ""
    return "\n".join(source.splitlines()[span.start_line - 1 : span.end_line])


def call(client: LLMExtractor, prompt: str, content: str, schema: type, name: str, folder: Path):
    start = len(client._call_log)
    chunk_folder = folder.parent
    run_root = chunk_folder.parents[3]
    request_gate = getattr(client, "request_gate", None)
    if hasattr(request_gate, "set_context"):
        request_gate.set_context(
            model=client.model_name,
            endpoint=client._model_route.backend.label,
            stage=name,
            chunk=chunk_folder.relative_to(run_root).as_posix(),
        )
    try:
        raw = client._call_structured(
            prompt,
            content,
            max_tokens=64_000,
            call_type=name,
            output_format="json",
            response_format={
                "type": "json_schema",
                "json_schema": {"name": name, "strict": True, "schema": schema.model_json_schema()},
            },
        )
    finally:
        # Failed transports/structured parsing must retain their own new records,
        # rather than accidentally saving a preceding successful call.
        for index, record in enumerate(client._call_log[start:]):
            suffix = "" if index == 0 else f"_retry_{index}"
            payload = asdict(record)
            finished_at = datetime.now(UTC)
            payload.update(
                model=client.model_name,
                endpoint=client._model_route.backend.label,
                stage=name,
                started_at_utc=(finished_at - timedelta(seconds=record.duration_s)).isoformat(),
                finished_at_utc=finished_at.isoformat(),
            )
            write_json(folder / f"{name}{suffix}_call.json", payload)
    record = client._call_log[-1]
    if not record.success or record.parse_error:
        raise ValueError(f"{name} returned a failed call record: {record.parse_error}")
    if record.finish_reason == "length":
        raise ValueError(f"{name} truncated")
    return schema.model_validate(raw)
