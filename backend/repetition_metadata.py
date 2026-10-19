"""Source-grounded, table-local repetition metadata with fail-closed acceptance.

Coverage diagnostics are separate from fact acceptance. Source grounding and logical
checks are deterministic; an independent model verdict adds semantic scrutiny, not proof.
This module never writes database rows.
"""

from __future__ import annotations

import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt

from backend.latex_source import _extract_caption_text, _extract_tables_with_spans


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Evidence(StrictModel):
    start_line: StrictInt = Field(ge=1)
    end_line: StrictInt = Field(ge=1)
    quote: str | None = Field(default=None, min_length=8)


class MethodFact(StrictModel):
    name: str = Field(min_length=1)
    role: Literal["proposed", "baseline"]
    origin: Literal["self_evaluated", "copied", "mixed", "unclear"]
    origin_evidence: list[Evidence]
    status: Literal["simple", "complex", "unstated"]
    repetitions: StrictInt | None = Field(default=None, ge=1)
    cv_folds: StrictInt | None = Field(default=None, ge=2)
    design: Literal["repeated_training", "repeated_cv", "single_cv", "nested", "unknown"]
    count_evidence: list[Evidence]
    scope_evidence: list[Evidence]
    explanation: str


class TableFact(StrictModel):
    table_id: StrictInt = Field(ge=1)
    role: Literal["benchmark", "excluded", "unclear"]
    role_evidence: list[Evidence]
    complication: str
    methods: list[MethodFact]
    decision: Literal["count", "excluded", "unknown", "special"] | None = None


class ProposedMethod(StrictModel):
    name: str
    evidence: list[Evidence]


class RepetitionFacts(StrictModel):
    proposed_methods: list[ProposedMethod]
    tables: list[TableFact]


class MethodVerdict(StrictModel):
    table_id: StrictInt
    name: str
    benchmark_supported: StrictBool
    origin_supported: StrictBool
    count_supported: StrictBool
    unit_correct: StrictBool
    uniform_datasets: StrictBool
    explanation: str


class Verification(StrictModel):
    methods: list[MethodVerdict]


def table_inventory(source: str) -> list[dict]:
    """Preserve full raw captions, including escaped percent signs and wraptables.

    IDs are source-environment ordinals, not guaranteed printed PDF table numbers.
    """
    tables, spans = _extract_tables_with_spans(source)
    return [
        {
            "table_id": table.number,
            "environment": span.env_name,
            "label": table.label,
            "caption": _extract_caption_text(table.body),
            "captions": [
                _extract_caption_text(table.body[match.start() :])
                for match in re.finditer(r"\\caption\s*(?:\[[^\]]*\]\s*)?\{", table.body)
            ],
            "start_line": source.count("\n", 0, span.start) + 1,
            "end_line": source.count("\n", 0, span.end) + 1,
            "body": table.body,
        }
        for table, span in zip(tables, spans, strict=True)
    ]


def grounded(evidence: Evidence, source: str) -> bool:
    lines = source.splitlines()
    if not 1 <= evidence.start_line <= evidence.end_line <= len(lines):
        return False
    original = " ".join(lines[evidence.start_line - 1 : evidence.end_line])
    # No citation removal, fuzzy token matching or model paraphrase acceptance.
    return evidence.quote is None or " ".join(evidence.quote.split()) in " ".join(original.split())


def evidence_text(evidence: Evidence, source: str) -> str:
    if not grounded(evidence, source):
        return ""
    return evidence.quote or "\n".join(
        source.splitlines()[evidence.start_line - 1 : evidence.end_line]
    )


_NUMBER_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "twenty": 20,
    "thirty": 30,
    "fifty": 50,
    "hundred": 100,
}


def supports_repeat_count(count: int, text: str, design: str) -> bool:
    normalized = text.casefold().replace("$", "").replace("~", " ")
    normalized = re.sub(
        r"\\(?:num|text|textbf|textit|textrm|emph|mathrm)\{([^{}]*)\}", r"\1", normalized
    )
    for word, value in _NUMBER_WORDS.items():
        normalized = re.sub(rf"\b{word}\b", str(value), normalized)
    number = rf"(?<!\d){count}(?!\d)"
    units = r"(?:independent\s+|random\s+|different\s+|predetermined\s+|executed\s+|seed\s+|weight\s+|model\s+)*"
    unit = (
        r"(?:trials?|runs?|reruns?|times|repeats?|repetitions?)"
        if design == "repeated_cv"
        else r"(?:seeds?|runs?|reruns?|times|repetitions?|initializations?)"
    )
    if re.search(rf"{number}\s+{units}{unit}\b", normalized):
        return True

    # Papers often elide the unit in the final item of a parallel list, e.g.
    # "five random seeds for A and four for the other datasets." Require the
    # earlier explicit unit and the same-sentence "for others" construction.
    return bool(
        design == "repeated_training"
        and re.search(
            rf"\b{unit}\b[^.!?]{{0,160}}\b{number}\s+for\s+(?:the\s+)?others\b",
            normalized,
        )
    )


def _name_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def _family_key(value: str) -> str:
    # Definitions sometimes append an explanation rather than a method alias.
    return _name_key(re.split(r"[;(]", value, maxsplit=1)[0])


def has_execution_evidence(text: str) -> bool:
    """Conservative lexical gate; the verifier must still establish whose values."""
    return bool(
        re.search(
            r"\bwe\b[^.!?]{0,200}\b(?:train(?:ed)?|retrain(?:ed)?|reimplement(?:ed)?|"
            r"implement(?:ed)?|rerun|re-run|evaluat(?:e|ed))\b|"
            r"\bwe\b[^.!?]{0,100}\b(?:use[ds]?|employ(?:ed)?)\b[^.!?]{0,100}"
            r"\b(?:implementation|code|checkpoints?|weights|repository)\b|"
            r"\b(?:experiments?|evaluations?)\s+(?:were\s+)?conducted\b|"
            r"\bresults\b[^.!?]{0,80}\b(?:running|reimplementation)\b",
            text,
            re.IGNORECASE,
        )
    )


def table_outcomes(
    facts: RepetitionFacts | None, source: str, validated: dict, error: str | None = None
) -> list[dict]:
    """One auditable outcome per inventory table; omissions are NOT paper unknowns."""
    declared: dict[int, list[TableFact]] = {}
    for table in facts.tables if facts else []:
        declared.setdefault(table.table_id, []).append(table)
    outcomes = []
    for entry in table_inventory(source):
        table_id = entry["table_id"]
        matches = declared.get(table_id, [])
        accepted = [
            m
            for m in validated.get("accepted", [])
            if m["table_id"] == table_id and m["role"] == "proposed"
        ]
        rejected = [
            m
            for m in validated.get("withheld", [])
            if m["table_id"] == table_id
            and m["role"] == "proposed"
            and "ablation_variant_not_eligible" not in m["flags"]
        ]
        decision, reason, kind = "special", "", ""
        if error:
            reason, kind = error, "call_failure"
        elif not matches:
            reason, kind = (
                "Extractor omitted this table; this does not establish an unknown paper count.",
                "missing_output",
            )
        elif len(matches) != 1:
            reason, kind = "Duplicate table outputs require resolution.", "duplicate_output"
        else:
            table = matches[0]
            if (
                table.role == "excluded"
                and table.role_evidence
                and all(grounded(e, source) for e in table.role_evidence)
                and table.complication
            ):
                decision, reason = "excluded", table.complication
            elif table.role != "benchmark":
                reason, kind = (
                    table.complication or "Benchmark eligibility unresolved.",
                    "eligibility_unresolved",
                )
            elif len(entry["captions"]) > 1:
                reason, kind = (
                    "Several independently captioned tables share this source environment.",
                    "multiple_captions",
                )
            elif (
                accepted
                and not rejected
                and len({(m["repetitions"], m["cv_folds"], m["design"]) for m in accepted}) == 1
            ):
                decision, reason = (
                    "count",
                    "Validated proposed-method repetition count; baseline origins/counts remain method-local.",
                )
            elif (
                rejected
                and all(
                    m["candidate_repetitions"] is None
                    and m["design"] in {"unknown", "single_cv"}
                    and m["verification"]
                    and m["verification"]["benchmark_supported"]
                    and m["verification"]["origin_supported"]
                    and set(m["flags"])
                    <= {
                        "non_simple_repeat_protocol",
                        "repeat_count_missing",
                        "semantic_verification_not_passed",
                    }
                    for m in rejected
                )
                and not accepted
                and all(m.status == "unstated" for m in table.methods if m.role == "proposed")
            ):
                decision, reason = (
                    "unknown",
                    " ".join(dict.fromkeys(m["explanation"] for m in rejected)),
                )
            else:
                reason = (
                    table.complication
                    or "; ".join(dict.fromkeys(m["explanation"] for m in rejected))
                    or "No supported proposed-method protocol; eligibility, identity or verification needs review."
                )
                kind = "protocol_or_verification_unresolved"
        outcomes.append(
            {
                "table_id": table_id,
                "caption": entry["caption"],
                "captions": entry["captions"],
                "outcome": decision,
                "reason": reason,
                "special_kind": kind or None,
                "count": accepted[0]["repetitions"] if decision == "count" else None,
                "cv_folds": accepted[0]["cv_folds"] if decision == "count" else None,
                "proposed_counts": accepted,
                "withheld_proposed": rejected,
                "method_origins": [
                    {
                        "name": m.name,
                        "role": m.role,
                        "origin_candidate": m.origin,
                        "evidence": [
                            {**e.model_dump(), "quote": evidence_text(e, source)}
                            for e in m.origin_evidence
                        ],
                    }
                    for m in matches[0].methods
                ]
                if len(matches) == 1
                else [],
                "raw_model_decision": matches[0].decision if len(matches) == 1 else None,
                "decision_changed_by_validation": bool(
                    len(matches) == 1
                    and matches[0].decision is not None
                    and matches[0].decision != decision
                ),
                "evidence": [
                    {**e.model_dump(), "quote": evidence_text(e, source)}
                    for e in matches[0].role_evidence
                ]
                if len(matches) == 1
                else [],
            }
        )
    return outcomes


def validate_repetitions(facts: RepetitionFacts, verification: Verification, source: str) -> dict:
    """Return accepted counts, withheld claims and separately scored coverage."""
    inventory = {entry["table_id"]: entry for entry in table_inventory(source)}
    verdicts: dict[tuple[int, str], list[MethodVerdict]] = {}
    for verdict in verification.methods:
        verdicts.setdefault((verdict.table_id, _name_key(verdict.name)), []).append(verdict)
    seen: set[int] = set()
    claimed_ids = [table.table_id for table in facts.tables]
    duplicate_ids = {table_id for table_id in claimed_ids if claimed_ids.count(table_id) > 1}
    proposed_keys = {_family_key(method.name) for method in facts.proposed_methods}
    definitions_grounded = bool(facts.proposed_methods) and all(
        method.evidence and all(grounded(e, source) for e in method.evidence)
        for method in facts.proposed_methods
    )
    accepted, withheld, proposed_missing = [], [], []
    for table in facts.tables:
        seen.add(table.table_id)
        if table.role == "benchmark" and not any(m.role == "proposed" for m in table.methods):
            proposed_missing.append(table.table_id)
        name_keys = [_name_key(m.name) for m in table.methods]
        for method in table.methods:
            flags = []
            key = (table.table_id, _name_key(method.name))
            proof = method.origin_evidence + method.count_evidence + method.scope_evidence
            if table.table_id not in inventory or table.table_id in duplicate_ids:
                flags.append("invalid_or_duplicate_table")
            elif len(inventory[table.table_id]["captions"]) > 1:
                # One environment can contain independently numbered result/ablation tables.
                flags.append("multiple_caption_environment_requires_resolution")
            if (
                table.table_id in inventory
                and method.design == "repeated_training"
                and re.search(r"\d+\s*[-~ ]?\s*fold\b", inventory[table.table_id]["caption"], re.I)
            ):
                flags.append("cv_caption_repetition_design_conflict")
            if name_keys.count(key[1]) > 1:
                flags.append("duplicate_method_claim")
            if table.role != "benchmark":
                flags.append("not_a_benchmark")
            if not table.role_evidence or not all(grounded(e, source) for e in table.role_evidence):
                flags.append("benchmark_evidence_not_grounded")
            if not all(grounded(e, source) for e in proof):
                flags.append("evidence_not_grounded")
            if method.origin != "self_evaluated" or not method.origin_evidence:
                flags.append("not_explicit_current_evaluation")
            if method.role == "baseline" and not has_execution_evidence(
                " ".join(evidence_text(e, source) for e in method.origin_evidence)
            ):
                flags.append("baseline_execution_evidence_missing")
            # A mention of an excluded OTHER variant must not reject the main method.
            ablation_identity = (
                rf"^(?:an?\s+)?ablation (?:version|variant)\b|"
                rf"^{re.escape(method.name)}\s+(?:is\s+)?(?:an?\s+)?ablation (?:version|variant)\b"
            )
            if re.search(ablation_identity, method.explanation, re.I):
                flags.append("ablation_variant_not_eligible")
            if method.role == "proposed" and (
                not any(key[1].startswith(proposed) for proposed in proposed_keys)
                or not definitions_grounded
            ):
                flags.append("proposed_method_definition_not_grounded")
            if method.status != "simple" or method.design not in {
                "repeated_training",
                "repeated_cv",
            }:
                flags.append("non_simple_repeat_protocol")
            if method.repetitions is None or not method.count_evidence:
                flags.append("repeat_count_missing")
            elif not supports_repeat_count(
                method.repetitions,
                " ".join(evidence_text(e, source) for e in method.count_evidence),
                method.design,
            ):
                flags.append("count_or_unit_not_supported")
            count_text = " ".join(evidence_text(e, source) for e in method.count_evidence)
            ambiguous_splits = re.finditer(
                r"\d+\s+(?:dataset\s+)?splits?\s+over\s+\d+\s+"
                r"(?:random\s+)?(?:weight\s+)?initializations?[^.!?]*",
                count_text,
                re.I,
            )
            # PER in a different experiment's sentence cannot resolve this one.
            if any(
                not re.search(r"\b(?:per|each)\s+split\b", clause.group(), re.I)
                for clause in ambiguous_splits
            ):
                flags.append("split_initialization_relationship_unresolved")
            if (
                method.design == "repeated_training"
                and re.search(r"weight\s+initializations?", count_text, re.I)
                and re.search(
                    r"k[- ]means\s+\d+\s+times\s+on\s+each\s+trained\s+encoder", count_text, re.I
                )
            ):
                flags.append("nested_training_clustering_protocol")
            if (
                method.role == "baseline"
                and re.search(r"\bour (?:model|method)\b", count_text, re.I)
                and not re.search(
                    r"\b(?:all|each)\s+(?:baselines?|methods?|models?)\b", count_text, re.I
                )
            ):
                flags.append("baseline_count_scope_is_proposed_only")
            if method.design == "repeated_cv" and method.cv_folds is None:
                flags.append("cv_folds_missing")
            if not method.scope_evidence:
                flags.append("dataset_scope_missing")
            matching = verdicts.get(key, [])
            if len(matching) != 1 or not all(
                [
                    matching[0].benchmark_supported,
                    matching[0].origin_supported,
                    matching[0].count_supported,
                    matching[0].unit_correct,
                    matching[0].uniform_datasets,
                ]
            ):
                flags.append("semantic_verification_not_passed")
            item = {
                "table_id": table.table_id,
                "name": method.name,
                "role": method.role,
                "origin": method.origin,
                "repetitions": method.repetitions,
                "cv_folds": method.cv_folds,
                "design": method.design,
                "explanation": method.explanation,
                "verification": matching[0].model_dump() if len(matching) == 1 else None,
                "flags": flags,
                "evidence_by_purpose": {
                    purpose: [
                        {**e.model_dump(), "quote": evidence_text(e, source)} for e in evidence
                    ]
                    for purpose, evidence in {
                        "benchmark": table.role_evidence,
                        "origin": method.origin_evidence,
                        "count": method.count_evidence,
                        "scope": method.scope_evidence,
                    }.items()
                },
                "evidence": [{**e.model_dump(), "quote": evidence_text(e, source)} for e in proof],
            }
            if flags:
                item["candidate_repetitions"] = method.repetitions
                item["repetitions"] = None
                withheld.append(item)
            else:
                accepted.append(item)
    result = {
        "accepted": accepted,
        "withheld": withheld,
        "coverage": {
            "missing_table_ids": sorted(set(inventory) - seen),
            "unexpected_table_ids": sorted(seen - set(inventory)),
            "benchmark_tables_without_proposed_entry": proposed_missing,
        },
        "semantic_checks_are_model_assisted": True,
    }
    result["table_outcomes"] = table_outcomes(facts, source, result)
    return result
