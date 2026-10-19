"""Source-first extraction, independent verification, and per-row safety gates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

from backend.mapping.binding import candidate_identity
from backend.mapping.checks import adapt_outputs, has_reviewed_inner_cv, row_errors
from backend.mapping.client import mapping_client
from backend.mapping.compact_verification import (
    CompactVerification,
    merge_compact_verification,
)
from backend.mapping.coverage import (
    cell_layouts,
    competing_tables,
    coverage_flags,
    grounding_errors,
)
from backend.mapping.datasets import project_row, restore_row
from backend.mapping.decisions import propose
from backend.mapping.outputs import MappingFacts, MappingVerdicts
from backend.mapping.presentations import presentation_safety
from backend.mapping.safety import safe_assignment
from backend.mapping.schema import call, exact_coverage
from backend.mapping.settings import guard_setting_scope
from backend.mapping.source import evidence_text
from backend.repetition_batch import write_json
from backend.repetition_extractor import DEFAULT_MODEL, repetition_input
from backend.result_mapping_checks import same_dataset


def optional_json(folder: Path, name: str, default):
    path = folder / name
    return json.loads(path.read_text()) if path.exists() else default


def extraction_content(paper: Path, source: str, pid: str, rows: list[dict]) -> str:
    identities = [
        {k: r[k] for k in ("result_id", "model", "dataset", "variant", "metric")} for r in rows
    ]
    return (
        repetition_input(source, paper_id=pid)
        + "\nREQUIRED TARGET IDENTITIES (labels are fallible, intended dataset must stay):\n"
        + json.dumps(identities)
        + "\nPRIOR SCOPED PROTOCOL KEYS (fallible inputs, not source):\n"
        + json.dumps(optional_json(paper, "protocol_keys.json", []))
        + "\nHUMAN-APPROVED DATASET IDENTITY CORRECTIONS (row-specific; do not generalize):\n"
        + json.dumps(optional_json(paper, "reviewed_datasets.json", []))
        + "\nHUMAN-REVIEWED SCOPED PROTOCOL INTERPRETATIONS:\n"
        + json.dumps(optional_json(paper, "reviewed_protocols.json", []))
        + "\nNo stored numeric values are supplied. Extract source identities first. repair=null."
    )


def facts_cache_key(prompt: str, content: str) -> str:
    payload = json.dumps([prompt, content], ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def cached_facts(folder: Path, cache_key: str, expected_ids: list[int]):
    metadata_path = folder / "facts_cache.json"
    facts_path = folder / "facts.json"
    if not metadata_path.exists() or not facts_path.exists():
        return None
    metadata = optional_json(folder, "facts_cache.json", {})
    attempt_name = metadata.get("fact_attempt")
    attempt = folder / attempt_name if isinstance(attempt_name, str) else None
    if (
        metadata.get("cache_key") != cache_key
        or attempt is None
        or not (attempt / "output.json").is_file()
    ):
        return None
    try:
        facts = MappingFacts.model_validate(optional_json(folder, "facts.json", {}))
        exact_coverage(facts.facts, [{"result_id": result_id} for result_id in expected_ids])
    except (ValueError, TypeError):
        return None
    return facts, attempt


def new_attempt(folder: Path, stage: str) -> Path:
    previous = list(folder.glob(f"{stage}_attempt_*"))
    attempt = folder / f"{stage}_attempt_{len(previous) + 1:03d}"
    attempt.mkdir()
    return attempt


def complete_call(client, prompt, content, schema, name, folder, rows, validate=None):
    feedback = []
    for _ in range(3):
        target = new_attempt(folder, name)
        try:
            output = call(
                client,
                prompt,
                content + "\nOUTPUT VALIDATION FEEDBACK:\n" + json.dumps(feedback),
                schema,
                name,
                target,
            )
            items = (
                output.facts
                if isinstance(output, MappingFacts)
                else output.decisions
                if isinstance(output, CompactVerification)
                else output.verdicts
            )
            exact_coverage(items, rows)
            if validate:
                validate(output)
            write_json(target / "output.json", output.model_dump())
            return output, target
        except Exception as exc:
            feedback.append(f"{type(exc).__name__}: {exc}")
            write_json(target / "error.json", {"error": feedback[-1]})
    raise ValueError(f"{name} failed three complete-output attempts: {'; '.join(feedback)}")


def semantic_errors(rows, facts, verdicts, hints, source):
    result = {}
    by_id = {f.result_id: f for f in facts.facts}
    rows_by_id = {r["result_id"]: r for r in rows}
    for verdict in verdicts.verdicts:
        row = rows_by_id[verdict.result_id]
        errors = grounding_errors(
            MappingVerdicts(verdicts=[verdict]), source, require_identity=True
        )
        errors += row_errors(row, verdict, by_id[verdict.result_id], source)
        errors += coverage_flags(verdict, hints[verdict.result_id], source)
        index = verdict.selected_candidate_index
        if index is not None and not same_dataset(
            verdict.corrected_fact.candidates[index].dataset, row["dataset"]
        ):
            errors.append(
                "Preserve the intended dataset and select its actual source column; repair wrong old values, not the dataset."
            )
        if errors:
            result[verdict.result_id] = errors
    return result


def protocol_scope_feedback(rows, verdicts, keys, earlier, source, paper):
    """Request a targeted review when verified own-run evidence hits an unknown prior key."""
    rows_by_id = {row["result_id"]: row for row in rows}
    prior_reviews = optional_json(paper, "reviewed_protocols.json", [])
    requests = {}
    for verdict in verdicts.verdicts:
        scope_review = verdict.protocol_scope_review
        review_is_grounded = bool(
            scope_review
            and scope_review.prior_reconciled
            and scope_review.scope_supported
            and scope_review.explanation
            and evidence_text(scope_review.evidence, source)
        )
        if (
            review_is_grounded
            or not verdict.origin_supported
            or not verdict.execution_supported
            or verdict.corrected_fact.origin != "self_evaluated"
        ):
            continue
        rid = verdict.result_id
        row = rows_by_id[rid]
        proposal = propose(
            row,
            verdict,
            source,
            allow_experiments=True,
            allow_identity=True,
            reviewed_inner_cv=has_reviewed_inner_cv(verdict, source, paper),
        )
        if proposal["action"] != "propose_count":
            continue
        checked = safe_assignment(
            proposal,
            keys,
            source,
            [hint for hint in earlier if hint["result_id"] == rid],
            protocol_reviews=prior_reviews,
        )
        if checked["action"] not in {
            "protocol_input_unresolved",
            "protocol_binding_unresolved",
            "protocol_input_conflict",
        }:
            continue
        requests[rid] = (
            f"The row is explicitly self-evaluated and execution-supported, but matching its "
            f"proposed count to the prior table/method protocol keys is blocked: "
            f"{checked['protocol_binding'].get('status')}. Independently review the exact "
            "table/method and applicable source sections (captions, setup, appendix). If the "
            "paper explicitly establishes this count and scope, set protocol_scope_review "
            "with cited evidence and explain how the scope applies to this selected result; "
            "otherwise leave it null. Do not infer from a neighboring method or dataset."
        )
    return requests


def protocol_review(proposal, verdict, source, references):
    review = verdict.protocol_scope_review
    if proposal["action"] != "propose_count" or review is None:
        return None
    if (
        not review.prior_reconciled
        or not review.scope_supported
        or not evidence_text(review.evidence, source)
    ):
        return None
    candidate = proposal["selected_candidate"]
    return {
        "result_id": proposal["result_id"],
        "independently_verified": True,
        "prior_reconciled": True,
        "scope_supported": True,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "candidate_sha256": candidate_identity(candidate),
        "protocol": candidate["protocol"],
        "evidence": [s.model_dump() for s in review.evidence],
        "explanation": review.explanation,
        "call_refs": references,
    }


def analyze_chunk(
    folder: Path,
    pid: str,
    rows: list[dict],
    source: str,
    prompts: Path,
    gate,
    *,
    model: str = DEFAULT_MODEL,
    fact_model: str | None = None,
    compact_verifier: bool = False,
    phase1_finished=None,
    phase2_finished=None,
) -> list[dict]:
    folder.mkdir(parents=True, exist_ok=True)
    paper = folder.parent.parent
    original_rows = {row["result_id"]: row for row in rows}
    dataset_records = optional_json(paper, "reviewed_datasets.json", [])
    rows = [project_row(row, source, dataset_records) for row in rows]
    client = mapping_client(gate, model=model)
    fact_client = (
        mapping_client(gate, model=fact_model) if fact_model and fact_model != model else client
    )
    content = extraction_content(paper, source, pid, rows)
    fact_prompt = (prompts / "result_mapping.txt").read_text()
    cache_key = facts_cache_key(fact_prompt, content)
    cached = cached_facts(folder, cache_key, [row["result_id"] for row in rows])
    if cached:
        facts, fact_attempt = cached
        write_json(folder / "facts_cache_use.json", {"reused": True, "cache_key": cache_key})
    else:
        facts, fact_attempt = complete_call(
            fact_client,
            fact_prompt,
            content,
            MappingFacts,
            "mapping_facts",
            folder,
            rows,
        )
        write_json(folder / "facts.json", facts.model_dump())
        write_json(
            folder / "facts_cache.json",
            {"cache_key": cache_key, "fact_attempt": fact_attempt.name},
        )
        write_json(folder / "facts_cache_use.json", {"reused": False, "cache_key": cache_key})
    if phase1_finished:
        phase1_finished()
    by_id = {f.result_id: f for f in facts.facts}
    hints = {
        r["result_id"]: competing_tables(r, source, by_id[r["result_id"]], ignore_comments=True)
        for r in rows
    }
    layouts = [
        layout
        for fact in facts.facts
        for layout in cell_layouts(source, fact, SimpleNamespace(presentations=[]))
    ]
    ids = {r["result_id"] for r in rows}
    earlier = [h for h in optional_json(paper, "earlier_matches.json", []) if h["result_id"] in ids]
    content += "\nOLD FIELDS FOR EXACT REPAIR ONLY (not identity evidence):\n" + json.dumps(rows)
    content += "\nUNTRUSTED SOURCE-FIRST FACTS:\n" + facts.model_dump_json()
    content += "\nFALLIBLE EARLIER NUMERIC HINTS:\n" + json.dumps(earlier)
    content += "\nCOMPETING TABLE HINTS (coverage is separate):\n" + json.dumps(hints)
    content += "\nLITERAL CELL LAYOUTS (zero-based unescaped & columns):\n" + json.dumps(layouts)
    keys = optional_json(paper, "protocol_keys.json", [])
    feedback = {}
    scope_feedback = {}
    previous_compact = None
    for _ in range(3):
        verification_content = (
            content
            + "\nSEMANTIC VALIDATION FEEDBACK:\n"
            + json.dumps(feedback)
            + "\nTARGETED PROTOCOL-SCOPE REVIEW REQUESTS:\n"
            + json.dumps(scope_feedback)
        )
        if previous_compact is not None:
            verification_content += (
                "\nPREVIOUS COMPACT VERIFIER OUTPUT (preserve valid source-grounded patches and "
                "candidate additions unless the feedback explicitly shows they are wrong):\n"
                + json.dumps(previous_compact)
            )
        if compact_verifier:
            expected_ids = [row["result_id"] for row in rows]

            def validate_compact(output, expected=expected_ids):
                merge_compact_verification(facts.facts, output, expected, source)

            verifier_model = (
                gate.phase2_model(model, fact_model) if hasattr(gate, "phase2_model") else model
            )
            verifier_client = (
                client if verifier_model == model else mapping_client(gate, model=verifier_model)
            )
            compact, verification_attempt = complete_call(
                verifier_client,
                (prompts / "result_mapping_delta_verification.txt").read_text(),
                verification_content,
                CompactVerification,
                "mapping_delta_verifier",
                folder,
                rows,
                validate=validate_compact,
            )
            raw, patch_counts = merge_compact_verification(
                facts.facts, compact, expected_ids, source
            )
            write_json(verification_attempt / "merged_verdicts.json", raw.model_dump())
            write_json(verification_attempt / "patch_counts.json", patch_counts)
            write_json(folder / "delta_verification.json", compact.model_dump())
        else:
            verifier_model = (
                gate.phase2_model(model, fact_model) if hasattr(gate, "phase2_model") else model
            )
            verifier_client = (
                client if verifier_model == model else mapping_client(gate, model=verifier_model)
            )
            raw, verification_attempt = complete_call(
                verifier_client,
                (prompts / "result_mapping_verification.txt").read_text(),
                verification_content,
                MappingVerdicts,
                "mapping_verifier",
                folder,
                rows,
            )
        verdicts = adapt_outputs(raw, rows, source, paper)
        feedback = semantic_errors(rows, facts, verdicts, hints, source)
        scope_feedback = protocol_scope_feedback(rows, verdicts, keys, earlier, source, paper)
        if compact_verifier:
            previous_compact = compact.model_dump(mode="json")
        write_json(verification_attempt / "adapted_verdicts.json", verdicts.model_dump())
        if not feedback and not scope_feedback:
            break
    if phase2_finished:
        phase2_finished()
    write_json(folder / "verification.json", verdicts.model_dump())
    write_json(folder / "semantic_warnings.json", feedback)
    write_json(folder / "protocol_scope_feedback.json", scope_feedback)
    references = [str(fact_attempt.resolve()), str(verification_attempt.resolve())]
    rows_by_id = {r["result_id"]: r for r in rows}
    proposals, reviews = [], []
    for verdict in verdicts.verdicts:
        rid = verdict.result_id
        row = rows_by_id[rid]
        result = propose(
            row,
            verdict,
            source,
            allow_experiments=True,
            allow_identity=True,
            reviewed_inner_cv=has_reviewed_inner_cv(verdict, source, paper),
        )
        review = protocol_review(result, verdict, source, references)
        if review:
            reviews.append(review)
            result["protocol_review"] = review
        protocol_reviews = optional_json(paper, "reviewed_protocols.json", [])
        if review:
            protocol_reviews = [*protocol_reviews, review]
        result = safe_assignment(result, keys, source, earlier, protocol_reviews=protocol_reviews)
        result = guard_setting_scope(presentation_safety(result, source))
        if rid in feedback:
            result.update(
                action="targeted_validation_unresolved",
                proposed_num_runs=None,
                correction=None,
                validation_errors=feedback[rid],
            )
        result = restore_row(result, original_rows[rid], source, dataset_records)
        proposals.append(result)
    write_json(folder / "protocol_reviews.json", reviews)
    write_json(folder / "proposals.json", proposals)
    return proposals
