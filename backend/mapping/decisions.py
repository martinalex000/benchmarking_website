from __future__ import annotations

import re
from typing import Literal

from pydantic import Field, StrictBool, StrictInt

from backend.mapping.schema import (
    Span,
    StrictModel,
    span_text,
)
from backend.mapping.source import (
    earlier_matches,
    evidence_text,
    method_key,
    name_key,
    printed_matches,
)
from backend.repetition_metadata import supports_repeat_count, table_inventory
from backend.result_mapping_checks import equivalent_number, same_dataset, sole_verified_selection


class Protocol(StrictModel):
    design: Literal["repeated_training", "single_cv", "repeated_cv", "split_training", "unknown"]
    training_repetitions: StrictInt | None = Field(ge=1)
    cv_folds: StrictInt | None = Field(ge=2)
    cv_repetitions: StrictInt | None = Field(ge=1)
    dataset_splits: StrictInt | None = Field(ge=1)
    repetitions_per_split: StrictInt | None = Field(ge=1)
    reported_runs: StrictInt | None = Field(ge=1)
    variability_scope: Literal[
        "training_runs", "folds", "cv_runs", "pooled_folds", "splits", "unknown"
    ]
    evidence: list[Span]
    scope_evidence: list[Span]
    explanation: str
    cv_repeat_unit: Literal["full_cv", "within_fold", "unknown"] = "unknown"


def total_models(protocol: Protocol) -> int | None:
    """User convention: CV folds are comparable model-training observations."""
    fixed_split = (
        protocol.design == "repeated_training"
        and protocol.dataset_splits == 1
        and protocol.variability_scope == "training_runs"
        and protocol.repetitions_per_split in (None, protocol.training_repetitions)
    )
    if not fixed_split and (
        protocol.dataset_splits is not None or protocol.repetitions_per_split is not None
    ):
        return None
    if protocol.design in ("single_cv", "repeated_cv") and protocol.training_repetitions:
        return None  # A third repetition axis must not disappear into the CV product.
    if protocol.design == "repeated_training":
        if protocol.cv_folds is not None or protocol.cv_repetitions is not None:
            return None
        value = protocol.training_repetitions
    elif protocol.design == "single_cv":
        if protocol.cv_repetitions not in (None, 1):
            return None
        value = protocol.cv_folds
    elif protocol.design == "repeated_cv":
        if not protocol.cv_folds or not protocol.cv_repetitions:
            return None
        value = protocol.cv_folds * protocol.cv_repetitions
    else:
        return None  # Split hierarchies retain structure, not a simple count.
    return value if value is not None and value > 0 else None


def grounded_protocol(protocol: Protocol, source: str, allow_experiments: bool = False) -> bool:
    from backend.repetition_consistency import protocol_consistency_errors

    if protocol_consistency_errors(protocol.model_dump(), source):
        return False
    text = evidence_text(protocol.evidence, source)
    if not text or not evidence_text(protocol.scope_evidence, source):
        return False
    if protocol.design == "repeated_training":
        return bool(
            protocol.training_repetitions
            and (
                supports_repeat_count(protocol.training_repetitions, text, "repeated_training")
                or (
                    allow_experiments
                    and re.search(
                        rf"\bwe\s+(?:run|ran|repeat(?:ed)?)\s+\$?{protocol.training_repetitions}"
                        rf"\$?\s+(?:independent\s+)?experiments\b",
                        text,
                        re.I,
                    )
                )
                or (
                    allow_experiments
                    and re.search(
                        r"\bwe\b[^.!?]{0,150}\brun\b[^.!?]{0,100}\brandom seeds\b", text, re.I
                    )
                    and re.search(rf"\b{protocol.training_repetitions}\s+trials\b", text, re.I)
                )
            )
        )
    if protocol.design in ("single_cv", "repeated_cv"):
        # A dataset's conventional CV setting alone cannot establish this paper's folds.
        folded = re.sub(r"[${}~]", " ", text)
        for word, number in (("two", 2), ("three", 3), ("five", 5), ("ten", 10), ("twenty", 20)):
            folded = re.sub(rf"\b{word}\b", str(number), folded, flags=re.I)
        if not protocol.cv_folds or not re.search(
            rf"\b{protocol.cv_folds}\s*[- ]?\s*fold", folded, re.I
        ):
            return False
        return protocol.design == "single_cv" or bool(
            protocol.cv_repetitions
            and supports_repeat_count(protocol.cv_repetitions, text, "repeated_cv")
        )
    return False


class Candidate(StrictModel):
    table_id: StrictInt
    displayed_mean: float
    displayed_std: float | None
    divisor: Literal[1, 100]
    method: str
    dataset: str
    metric: str
    configuration: str
    eligibility: Literal["benchmark", "ablation", "other", "unclear"]
    main_experiment: StrictBool
    row_evidence: Span
    column_evidence: Span
    cell_evidence: Span
    protocol: Protocol
    cell_column_index: StrictInt | None = None
    configuration_axes: dict[str, str] = Field(default_factory=dict)
    identity_evidence: list[Span] = Field(default_factory=list)


class Repair(StrictModel):
    old_value: float
    old_std: float | None
    old_model: str
    old_variant: str
    corrected_value: float
    corrected_std: float | None
    corrected_model: str
    corrected_variant: str
    evidence: list[Span]
    explanation: str
    old_metric: str | None = None
    corrected_metric: str | None = None


class Fact(StrictModel):
    result_id: StrictInt
    candidates: list[Candidate]
    origin: Literal["self_evaluated", "copied", "mixed", "unclear"]
    origin_evidence: list[Span]
    execution_evidence: list[Span]
    repair: Repair | None
    explanation: str


class Facts(StrictModel):
    facts: list[Fact]


class Verdict(StrictModel):
    result_id: StrictInt
    corrected_fact: Fact
    verified_candidate_indices: list[StrictInt]
    origin_supported: StrictBool
    execution_supported: StrictBool
    protocol_supported: StrictBool
    repair_supported: StrictBool
    setting_status: Literal["supported", "unverified", "contradicted"]
    eligibility: Literal["benchmark", "ablation", "other", "unclear"]
    explanation: str
    selected_candidate_index: StrictInt | None = None


class Verdicts(StrictModel):
    verdicts: list[Verdict]


class CompleteRetryFact(Fact):
    candidates: list[Candidate] = Field(min_length=1)


class CompleteRetryVerdict(Verdict):
    corrected_fact: CompleteRetryFact


class CompleteRetryVerdicts(StrictModel):
    verdicts: list[CompleteRetryVerdict]


def appendix_start(source: str) -> int:
    for i, line in enumerate(source.splitlines(), 1):
        if re.search(r"\\appendix\b|\\(?:sub)?section\*?\{[^}]*Appendix", line, re.I):
            return i
    return len(source.splitlines()) + 1


def rank(candidate: Candidate, source: str, allow_experiments: bool = False) -> tuple:
    """Main text, main experiment, more trained models, then first source occurrence."""
    count = (
        total_models(candidate.protocol)
        if grounded_protocol(candidate.protocol, source, allow_experiments=allow_experiments)
        else None
    )
    return (
        candidate.cell_evidence.start_line >= appendix_start(source),
        not candidate.main_experiment,
        -(count if count is not None else -1),
        candidate.cell_evidence.start_line,
    )


def grounded_candidate(candidate: Candidate, source: str) -> Candidate | None:
    spans = (candidate.row_evidence, candidate.column_evidence, candidate.cell_evidence)
    tables = [t for t in table_inventory(source) if all(span_text(s, t, source) for s in spans)]
    if len(tables) != 1:
        return None
    cell = span_text(candidate.cell_evidence, tables[0], source)
    candidate = candidate.model_copy(update={"table_id": tables[0]["table_id"]})
    values = (candidate.displayed_mean, candidate.displayed_std)
    for multiplier in (1, candidate.divisor):
        if all(
            v is None
            or printed_matches(
                v * multiplier, v * multiplier / candidate.divisor, candidate.divisor, cell
            )
            for v in values
        ):
            return normalized_scale(
                candidate.model_copy(
                    update={
                        "displayed_mean": values[0] * multiplier,
                        "displayed_std": None if values[1] is None else values[1] * multiplier,
                    }
                ),
                source,
            )
    return None


def normalized_scale(candidate: Candidate, source: str) -> Candidate:
    """Derive bounded-score units from the literal cell and explicit table units."""
    if metric_key(candidate.metric) not in {"accuracy", "f1", "f1macro", "f1micro", "auc", "ap"}:
        return candidate
    tables = [
        t for t in table_inventory(source) if t["table_id"] == getattr(candidate, "table_id", None)
    ]
    if len(tables) != 1:
        return candidate
    table = tables[0]
    # Fractional scores with no percentage declaration must not be divided again.
    # Explicit percentage captions still permit a genuine sub-one-percent result.
    explicit_percent = bool(re.search(r"\\%|\(%\)|percent(?:age)?", table["caption"], re.I))
    divisor = 100 if candidate.displayed_mean > 1 or explicit_percent else 1
    return candidate.model_copy(update={"divisor": divisor})


def metric_key(value: str) -> str:
    # Split qualifiers identify the column, not a different metric definition.
    value = re.sub(r"^(?:test|train|validation|valid|val)\s+", "", value.strip(), flags=re.I)
    key = name_key(value)
    return {
        "acc": "accuracy",
        "rocauc": "auc",
        "averageprecision": "ap",
        "meanabsoluteerror": "mae",
        "meanreciprocalrank": "mrr",
        "macrof1": "f1macro",
        "macroaveragedf1": "f1macro",
    }.get(key, key)


def grounded_column(candidate: Candidate, source: str) -> bool:
    """Check the claimed cell, not any equal number elsewhere on its row."""
    index = candidate.cell_column_index
    if index is None or index < 0:
        return False
    lines = source.splitlines()
    span = candidate.cell_evidence
    if span.start_line != span.end_line or not 1 <= span.start_line <= len(lines):
        return False  # Complex multiline cells need an explicit abstention for now.
    line = re.split(r"(?<!\\)%", lines[span.start_line - 1])[0]
    cells = re.split(r"(?<!\\)&", line)
    if index >= len(cells):
        return False
    cell = cells[index]
    if not printed_matches(candidate.displayed_mean, candidate.displayed_mean, 1, cell):
        return False
    if candidate.displayed_std is not None and not printed_matches(
        candidate.displayed_std, candidate.displayed_std, 1, cell
    ):
        return False
    return bool(candidate.configuration_axes and evidence_text(candidate.identity_evidence, source))


def experiment_identity(candidate: Candidate) -> tuple:
    """Priority may compare presentations only inside one verified identity group."""
    return (
        method_key(candidate.method),
        name_key(candidate.dataset),
        metric_key(candidate.metric),
        tuple(sorted((name_key(k), name_key(v)) for k, v in candidate.configuration_axes.items())),
    )


def verified_repair(
    row: dict,
    candidate: Candidate,
    fact: Fact,
    verdict: Verdict,
    source: str,
    *,
    allow_metric: bool = False,
) -> dict | None:
    repair = fact.repair
    if not repair or not verdict.repair_supported or not evidence_text(repair.evidence, source):
        return None
    old = (row["value"], row["std"], row["model"], row["variant"])
    if old != (repair.old_value, repair.old_std, repair.old_model, repair.old_variant):
        return None
    new = (repair.corrected_value, repair.corrected_std)
    # Absence of setting evidence must not become a spurious setting-label repair.
    setting_refinement = name_key(old[3]) in {"standardsplit", "standard", "defaultsplit"}
    ambiguous_transductive = bool(
        re.search(r"training\s+on\s+all\s+nodes", repair.corrected_variant, re.I)
    )
    cv_absence_as_contradiction = bool(
        re.search(r"\bcv\b|cross[- ]validation|\bfold", old[3], re.I)
        and re.search(r"no\s+cv|\bruns\s+averaged", repair.corrected_variant, re.I)
    )
    hold_setting = (
        verdict.setting_status == "unverified"
        or setting_refinement
        or ambiguous_transductive
        or cv_absence_as_contradiction
    )
    variant = old[3] if hold_setting else repair.corrected_variant
    corrected_key = re.sub(r"extractor$", "", method_key(repair.corrected_model))
    model = old[2] if method_key(old[2]) == corrected_key else repair.corrected_model
    metric_repair = bool(
        allow_metric
        and repair.old_metric == row.get("metric")
        and repair.corrected_metric is not None
        and metric_key(repair.corrected_metric) == metric_key(candidate.metric)
        and metric_key(repair.old_metric) != metric_key(repair.corrected_metric)
    )
    if (
        equivalent_number(old[0], new[0])
        and equivalent_number(old[1], new[1])
        and old[2:] == (model, variant)
        and not metric_repair
    ):
        return None  # Origin-only reclassification is not a numeric/identity repair.
    actual = (
        candidate.displayed_mean / candidate.divisor,
        None if candidate.displayed_std is None else candidate.displayed_std / candidate.divisor,
    )
    if any(
        a != b and (a is None or b is None or abs(a - b) > 1e-9)
        for a, b in zip(new, actual, strict=True)
    ):
        return None
    result = {
        "old": {"value": old[0], "std": old[1], "model": old[2], "variant": old[3]},
        "corrected": {
            "value": new[0],
            "std": new[1],
            "model": model,
            "variant": variant,
        },
        "evidence": [s.model_dump() for s in repair.evidence],
        "explanation": repair.explanation
        + (
            " Unverified/refinement-only setting-label change withheld."
            if variant != repair.corrected_variant
            else ""
        ),
    }
    if metric_repair:
        result["old"]["metric"] = repair.old_metric
        result["corrected"]["metric"] = repair.corrected_metric
    return result


def propose(
    row: dict,
    verdict: Verdict,
    source: str,
    prior_eligibility: str | None = None,
    *,
    allow_experiments: bool = False,
    allow_identity: bool = False,
    reviewed_inner_cv: bool = False,
) -> dict:
    result = {
        **row,
        "action": "unresolved",
        "proposed_num_runs": None,
        "verdict": verdict.model_dump(),
        "correction": None,
    }
    verdict = sole_verified_selection(verdict)
    result["verdict"] = verdict.model_dump()
    fact = verdict.corrected_fact
    if fact.result_id != row["result_id"] or verdict.result_id != row["result_id"]:
        return {**result, "action": "invalid_result_id"}
    candidates = []
    indexed_candidates = {}
    for i in verdict.verified_candidate_indices:
        if not 0 <= i < len(fact.candidates):
            return {**result, "action": "invalid_candidate_index"}
        candidate = grounded_candidate(fact.candidates[i], source)
        if candidate is None:
            return {**result, "action": "ungrounded_candidate"}
        if allow_identity and not grounded_column(candidate, source):
            return {**result, "action": "column_identity_unresolved"}
        candidates.append(candidate)
        indexed_candidates[i] = candidate
    if not candidates:
        return result
    benchmarks = [c for c in candidates if c.eligibility == "benchmark"]
    if allow_identity:
        anchor = indexed_candidates.get(verdict.selected_candidate_index)
        if anchor is None:
            return {**result, "action": "experiment_identity_unresolved"}
        if not same_dataset(row["dataset"], anchor.dataset):
            return {**result, "action": "dataset_identity_unresolved"}
        group = experiment_identity(anchor)
        candidates = [c for c in candidates if experiment_identity(c) == group]
        # A duplicate presentation cannot upgrade a verifier-selected ablation
        # into an eligible benchmark result. The selected cell establishes the
        # eligibility boundary; priority only chooses among candidates within it.
        if anchor.eligibility != "benchmark":
            candidates = [c for c in candidates if c.eligibility == anchor.eligibility]
        benchmarks = [c for c in candidates if c.eligibility == "benchmark"]
    selected = min(
        benchmarks or candidates,
        key=lambda c: rank(c, source, allow_experiments=allow_experiments),
    )
    if allow_experiments and selected.protocol.design == "repeated_cv":
        protocol_text = evidence_text(selected.protocol.evidence, source)
        if re.search(r"in each (?:partition|fold)[^.!?]{0,120}repeat", protocol_text, re.I):
            # Same model-fit product, but not evidence of repeated full CV cycles.
            selected = selected.model_copy(
                update={
                    "protocol": selected.protocol.model_copy(
                        update={
                            "cv_repeat_unit": "within_fold",
                            "variability_scope": "unknown",
                        }
                    )
                }
            )
    result["selected_candidate"] = selected.model_dump()
    result["protocol"] = selected.protocol.model_dump()
    repair = verified_repair(row, selected, fact, verdict, source, allow_metric=allow_experiments)
    result["correction"] = repair
    if (
        repair is None
        and fact.repair is not None
        and (
            fact.repair.corrected_value != row["value"]
            or fact.repair.corrected_std != row["std"]
            or name_key(fact.repair.corrected_model) != name_key(row["model"])
            or fact.repair.corrected_variant != row["variant"]
        )
    ):
        result["withheld_repair"] = fact.repair.model_dump()
    if prior_eligibility == "ablation":
        return {
            **result,
            "action": "propose_quarantine",
            "reason": "prior_verifier_excluded",
            "prior_eligibility": prior_eligibility,
        }
    if verdict.eligibility in ("ablation", "other") or selected.eligibility in (
        "ablation",
        "other",
    ):
        return {**result, "action": "propose_quarantine", "reason": "verifier_excluded"}
    expected = repair["corrected"] if repair else row
    if allow_experiments and metric_key(selected.metric) != metric_key(
        expected.get("metric", row.get("metric", selected.metric))
    ):
        return {**result, "action": "metric_unresolved", "proposed_num_runs": None}
    cell = evidence_text([selected.cell_evidence], source)
    if not printed_matches(
        selected.displayed_mean, expected["value"], selected.divisor, cell
    ) or not printed_matches(selected.displayed_std, expected["std"], selected.divisor, cell):
        return {**result, "action": "repair_unverified"}
    if verdict.setting_status == "contradicted" and not repair:
        return {**result, "action": "propose_quarantine", "reason": "contradicted_setting"}
    if verdict.eligibility != "benchmark":
        return result
    if not verdict.origin_supported or not evidence_text(fact.origin_evidence, source):
        return {**result, "action": "origin_unresolved"}
    if fact.origin == "copied":
        return {**result, "action": "copied_excluded"}
    if (
        fact.origin != "self_evaluated"
        or not verdict.execution_supported
        or not evidence_text(fact.execution_evidence, source)
    ):
        return {**result, "action": "execution_unresolved"}
    count = total_models(selected.protocol)
    possible_cv = not reviewed_inner_cv and re.search(
        r"\bcv\b|cross[- ]validation|\bfold", expected["variant"], re.I
    )
    if (
        count is None
        or not verdict.protocol_supported
        or not grounded_protocol(selected.protocol, source, allow_experiments=allow_experiments)
        or (possible_cv and selected.protocol.design == "repeated_training")
    ):
        if possible_cv and selected.protocol.design == "repeated_training":
            result["protocol"] = selected.protocol.model_copy(
                update={
                    "design": "unknown",
                    "training_repetitions": None,
                    "variability_scope": "unknown",
                    "explanation": selected.protocol.explanation
                    + " Local guard: reported runs do not resolve the possible CV unit; "
                    "absence of a fold statement does not disprove CV.",
                }
            ).model_dump()
        return {**result, "action": "self_evaluated_protocol_unresolved"}
    return {
        **result,
        "action": "propose_count",
        "proposed_num_runs": count,
        "count_unit": "models_trained",
    }


def hints_with_aliases(db, pid: str, rows: list[dict]) -> list[dict]:
    hints = earlier_matches(db, pid, rows)
    aliases = {"mlp": ["Multi-layer perceptron", "Raw features"]}
    for row in rows:
        for alias in aliases.get(name_key(row["model"]), []):
            alternative = {**row, "model": alias}
            for hint in earlier_matches(db, pid, [alternative]):
                hint["method_relation"] = "alias candidate; verify identity, not just equal number"
                hints.append(hint)
    return hints


def protocol_description(protocol: dict) -> str:
    labels = {
        "training_repetitions": "training repeats",
        "cv_folds": "CV folds",
        "cv_repetitions": "CV repeats",
        "dataset_splits": "dataset splits",
        "repetitions_per_split": "repeats per split",
        "reported_runs": "reported runs",
    }
    fields = [
        f"{label} {protocol[key]}" for key, label in labels.items() if protocol[key] is not None
    ]
    return "; ".join(
        [
            protocol["design"],
            *fields,
            "variability over " + protocol["variability_scope"],
            protocol["explanation"],
        ]
    )
