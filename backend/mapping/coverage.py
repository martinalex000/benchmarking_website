"""Source-grounding and presentation-coverage checks for maintained mapping."""

from __future__ import annotations

import re

from backend.mapping.decisions import Fact, grounded_candidate, grounded_column
from backend.mapping.outputs import MappingVerdict as BatchVerdict
from backend.mapping.outputs import MappingVerdicts as BatchVerdicts
from backend.mapping.source import active_source_lines, evidence_text, name_key
from backend.repetition_metadata import table_inventory


def grounding_errors(
    verdicts: BatchVerdicts, source: str, *, require_identity: bool = False
) -> list[str]:
    errors = []
    active_source = "\n".join(active_source_lines(source))
    for verdict in verdicts.verdicts:
        for index in verdict.verified_candidate_indices:
            candidate = verdict.corrected_fact.candidates[index]
            if grounded_candidate(candidate, active_source) is None:
                errors.append(
                    f"Row {verdict.result_id}, candidate {index}: invalid table/cell anchors or "
                    "ungrounded literal mean/std. Put cell_evidence on the numeric table row, "
                    "row_evidence on the method row and column_evidence on the dataset header; "
                    "all three must lie inside the same table. Protocol prose belongs only "
                    "in protocol.evidence. If no cell can be established, clear verified indices."
                )
            elif require_identity and not grounded_column(candidate, active_source):
                errors.append(
                    f"Row {verdict.result_id}, candidate {index}: mean/std not both in the claimed physical cell_column_index={candidate.cell_column_index}, or missing configuration/identity evidence. Count unescaped & separators on the ACTUAL cell row, including leading empty cells; different tables have different column layouts."
                )
    return errors


def method_keys(row: dict, fact: Fact | None = None) -> set[str]:
    names = [row["model"]]
    if fact:
        names.extend(c.method for c in fact.candidates)
    return {name_key(re.split(r"\s*\(", name)[0]) for name in names if name_key(name)}


def competing_tables(
    row: dict, source: str, fact: Fact | None = None, *, ignore_comments: bool = False
) -> list[int]:
    """Coverage screen only: other named rows may be different experiments or ablations."""
    methods = method_keys(row, fact)
    dataset = name_key(row["dataset"])
    found = {c.table_id for c in fact.candidates} if fact else set()
    active = active_source_lines(source) if ignore_comments else None
    for table in table_inventory(source):
        body = table["body"]
        if active is not None:
            body = "\n".join(active[table["start_line"] - 1 : table["end_line"]])
            if not re.search(r"\\begin\{(?:table\*?|wraptable|longtable|sidewaystable\*?)\}", body):
                continue
        if dataset not in name_key(body):
            continue
        for segment in re.split(r"\\\\|\\cr\b", body):
            cells = segment.split("&")
            if len(cells) < 2:
                continue
            label = name_key(
                re.sub(r"\\(?:textbf|textit|mathrm|mathbf|bf|emph)\b", "", " ".join(cells[:2]))
            )
            if any(key and key in label for key in methods) and re.search(
                r"\d", " & ".join(cells[1:])
            ):
                found.add(table["table_id"])
                break
    return sorted(found)


def coverage_flags(verdict: BatchVerdict, tables: list[int], source: str) -> list[str]:
    flags = []
    reviewed = {}
    for review in verdict.presentations:
        if review.table_id in reviewed:
            flags.append("duplicate_presentation_review")
        reviewed[review.table_id] = review
        if not evidence_text(review.evidence, source):
            flags.append("presentation_evidence_missing")
        if review.decision == "unclear":
            flags.append("presentation_scope_unclear")
        if review.decision == "same_experiment" and not any(
            0 <= index < len(verdict.corrected_fact.candidates)
            and verdict.corrected_fact.candidates[index].table_id == review.table_id
            for index in verdict.verified_candidate_indices
        ):
            flags.append("same_experiment_candidate_omitted")
    if set(tables) - reviewed.keys():
        flags.append("competing_presentations_unreviewed")
    return sorted(set(flags))


def cell_layouts(source: str, fact, previous) -> list[dict]:
    """Only expose literal source structure; make no duplicate/eligibility decisions."""
    spans = [candidate.cell_evidence for candidate in fact.candidates]
    spans += [span for review in previous.presentations for span in review.evidence]
    numbers = {number for span in spans for number in range(span.start_line, span.end_line + 1)}
    lines = source.splitlines()
    return [
        {
            "source_line": number,
            "physical_cells": dict(enumerate(re.split(r"(?<!\\)&", lines[number - 1]))),
        }
        for number in sorted(numbers)
        if 1 <= number <= len(lines) and "&" in lines[number - 1]
    ]
