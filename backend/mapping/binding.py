import hashlib
import json
import re

from backend.mapping.source import active_source_lines, evidence_text, method_key


def input_total(key: dict) -> int | None:
    method = key["method"]
    verified = key.get("previous_verdict") or {}
    if not all(
        verified.get(field) is True
        for field in (
            "benchmark_supported",
            "origin_supported",
            "count_supported",
            "unit_correct",
            "uniform_datasets",
        )
    ):
        return None
    if method.get("origin") != "self_evaluated" or method.get("status") != "simple":
        return None
    repetitions, folds = method.get("repetitions"), method.get("cv_folds")
    if method.get("design") == "repeated_training":
        return repetitions if type(repetitions) is int and repetitions > 0 else None
    if method.get("design") == "single_cv":
        return folds if type(folds) is int and folds > 1 else None
    if (
        method.get("design") == "repeated_cv"
        and type(repetitions) is int
        and repetitions > 0
        and type(folds) is int
        and folds > 1
    ):
        return repetitions * folds  # Agreed total-model convention, not independence.
    return None


def normalized_method_label(label: str) -> str:
    """Read method text without treating table decorations as model identity."""
    label = re.sub(r"\\(?:toprule|midrule|bottomrule|hline)\b(?:\[[^]]*\])?", "", label)
    label = re.sub(r"\\(?:rowcolor|cellcolor|color)(?:\[[^]]*\])?\s*\{[^{}]*\}", "", label)
    label = re.sub(r"\\cite[a-zA-Z*]*\s*\{[^{}]*\}", "", label)
    label = re.sub(
        r"\\(?:multirow|multicolumn)(?:\[[^]]*\])?\s*\{[^{}]*\}\s*\{[^{}]*\}",
        "",
        label,
    )
    label = re.sub(r"\\(?:m|textbf|textit|mathrm|mathbf|emph)\s*\{([^{}]*)\}", r"\1", label)
    return method_key(label)


def source_method_key(candidate: dict, source: str) -> str | None:
    span = candidate.get("row_evidence")
    lines = active_source_lines(source)
    if not span or not 1 <= span["start_line"] <= span["end_line"] <= len(lines):
        return None
    text = " ".join(lines[span["start_line"] - 1 : span["end_line"]])
    cell_span = candidate.get("cell_evidence")
    column = candidate.get("cell_column_index")
    if cell_span and type(column) is int:
        if not 1 <= cell_span["start_line"] <= cell_span["end_line"] <= len(lines):
            return None
        text = " ".join(lines[cell_span["start_line"] - 1 : cell_span["end_line"]])
        boundaries = list(re.finditer(r"(?<!\\)&", text))
        if not 1 <= column <= len(boundaries):
            return None
        text = text[: boundaries[column - 1].start()]
        text = re.split(r"\\\\(?:\s*\[[^]]*\])?|\\cr\b", text)[-1]
    elif len([part for part in re.split(r"\\\\|\\cr\b", text) if "&" in part]) > 1:
        return None
    labels = [normalized_method_label(label) for label in re.split(r"(?<!\\)&", text)[:2]]
    stem = re.sub(r"[+*]", "", method_key(candidate.get("method", "").split("(")[0]))
    matches = {label for label in labels if stem and re.sub(r"[+*]", "", label) == stem}
    if matches:
        return next(iter(matches)) if len(matches) == 1 else None
    return next((label for label in labels if label), None)


def method_identity_conflict(candidate: dict, source: str) -> bool:
    """Reject variant disagreements without rejecting descriptive method aliases."""
    printed = source_method_key(candidate, source)
    selected = method_key(candidate["method"].split("(")[0])
    return bool(
        printed
        and printed != selected
        and re.sub(r"[+*]", "", printed) == re.sub(r"[+*]", "", selected)
    )


def candidate_identity(candidate: dict) -> str:
    """Bind a review to the actual cell/configuration, not just a method label."""
    identity = {k: v for k, v in candidate.items() if k != "protocol"}
    return hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()


def apply_human_protocol_review(
    row: dict, source: str, reviews: list[dict]
) -> tuple[dict, dict | None]:
    """Apply an explicit table/method-scoped user decision to verified own runs."""
    from backend.mapping.decisions import (
        Candidate,
        Protocol,
        grounded_candidate,
        grounded_column,
        grounded_protocol,
        total_models,
    )

    selected = row.get("selected_candidate")
    verdict = row.get("verdict", {})
    fact = verdict.get("corrected_fact", {})
    index = verdict.get("selected_candidate_index")
    if (
        not selected
        or row.get("action")
        not in {
            "propose_count",
            "self_evaluated_protocol_unresolved",
            "protocol_input_unresolved",
            "protocol_input_conflict",
            "protocol_binding_unresolved",
        }
        or not isinstance(fact, dict)
        or type(index) is not int
        or index not in verdict.get("verified_candidate_indices", [])
        or not 0 <= index < len(fact.get("candidates", []))
        or not all(verdict.get(key) is True for key in ("origin_supported", "execution_supported"))
        or fact.get("origin") != "self_evaluated"
        or selected.get("eligibility") != "benchmark"
    ):
        return row, None

    from_candidate = fact["candidates"][index]
    bound_fields = (
        "table_id",
        "method",
        "dataset",
        "metric",
        "cell_evidence",
        "cell_column_index",
        "row_evidence",
        "column_evidence",
        "configuration_axes",
    )
    if any(selected.get(field) != from_candidate.get(field) for field in bound_fields):
        return row, None
    try:
        candidate = Candidate.model_validate(selected)
    except (TypeError, ValueError):
        return row, None
    if grounded_candidate(candidate, source) is None or not grounded_column(candidate, source):
        return row, None

    matches = [
        review
        for review in reviews
        if review.get("reviewer") == "human_user"
        and review.get("authorization")
        and review.get("table_id") == selected.get("table_id")
        and method_key(review.get("method", "")) == method_key(selected.get("method", ""))
    ]
    if len(matches) != 1:
        return row, None
    review = matches[0]
    if review.get("source_sha256") != hashlib.sha256(source.encode()).hexdigest():
        return row, None
    try:
        from backend.mapping.schema import Span

        evidence = [Span.model_validate(span) for span in review.get("evidence", [])]
        scope_evidence = [Span.model_validate(span) for span in review.get("scope_evidence", [])]
        protocol = Protocol.model_validate(review.get("protocol"))
    except (TypeError, ValueError):
        return row, None
    if (
        not evidence
        or not scope_evidence
        or not evidence_text(evidence, source)
        or not evidence_text(scope_evidence, source)
        or total_models(protocol) != review.get("count")
        or not grounded_protocol(protocol, source, allow_experiments=True)
    ):
        return row, None

    result = dict(row)
    result["selected_candidate"] = {**selected, "protocol": protocol.model_dump()}
    result["protocol"] = protocol.model_dump()
    result["proposed_num_runs"] = review["count"]
    result["action"] = "propose_count"
    accepted = {
        **review,
        "result_id": row["result_id"],
        "candidate_sha256": candidate_identity(selected),
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "protocol": protocol.model_dump(),
        "explanation": review.get("interpretation", "User-reviewed protocol scope."),
        "human_authorized": True,
    }
    result["protocol_review"] = accepted
    return result, accepted


def verified_override(row: dict, source: str, reviews: list[dict]) -> dict | None:
    """Only accept an independently reviewed, source-bound protocol revision."""
    from backend.mapping.decisions import (
        Protocol,
        grounded_protocol,
        total_models,
    )

    matches = [r for r in reviews if r.get("result_id") == row["result_id"]]
    if len(matches) != 1 or not source:
        return None
    review = matches[0]
    model_authorized = all(
        review.get(flag) is True
        for flag in ("independently_verified", "prior_reconciled", "scope_supported")
    ) and bool(review.get("call_refs"))
    human_authorized = review.get("human_authorized") is True and bool(review.get("authorization"))
    if not (model_authorized or human_authorized):
        return None
    if (
        review.get("source_sha256") != hashlib.sha256(source.encode()).hexdigest()
        or review.get("candidate_sha256") != candidate_identity(row["selected_candidate"])
        or not review.get("explanation")
    ):
        return None
    try:
        protocol = Protocol.model_validate(review.get("protocol"))
    except ValueError:
        return None
    total = total_models(protocol)
    if (
        type(row.get("proposed_num_runs")) is not int
        or total != row["proposed_num_runs"]
        or row["selected_candidate"].get("protocol") != protocol.model_dump()
        or not grounded_protocol(protocol, source, allow_experiments=True)
    ):
        return None
    return review


def source_verified_unknown_prior(row: dict, source: str, keys: list[dict]) -> bool:
    """Let exact source-verified row evidence stand when no prior count key applies."""
    from backend.mapping.decisions import (
        Candidate,
        Protocol,
        grounded_candidate,
        grounded_column,
        grounded_protocol,
        total_models,
    )

    selected = row.get("selected_candidate") or {}
    verdict = row.get("verdict") or {}
    fact = verdict.get("corrected_fact") or {}
    if (
        row.get("action") != "propose_count"
        or selected.get("eligibility") != "benchmark"
        or fact.get("origin") != "self_evaluated"
        or not all(
            verdict.get(field) is True
            for field in ("origin_supported", "execution_supported", "protocol_supported")
        )
    ):
        return False
    for key in keys:
        prior = key.get("previous_verdict") or {}
        method = key.get("method") or {}
        if (
            key.get("table_role") == "excluded"
            or prior.get("benchmark_supported") is False
            or prior.get("origin_supported") is False
            or method.get("origin") == "copied"
        ):
            return False
    if any(input_total(key) is not None for key in keys):
        return False
    try:
        candidate = Candidate.model_validate(selected)
        protocol = Protocol.model_validate(selected.get("protocol"))
    except (TypeError, ValueError):
        return False
    return bool(
        total_models(protocol) == row.get("proposed_num_runs")
        and grounded_candidate(candidate, source) is not None
        and grounded_column(candidate, source)
        and grounded_protocol(protocol, source, allow_experiments=True)
    )


def check_binding(
    row: dict, keys: list[dict], source: str = "", protocol_reviews: list[dict] = ()
) -> dict:
    result = {**row, "protocol_binding": {"status": "not_applicable"}}
    selected = row.get("selected_candidate")
    if not selected:
        return result
    if method_identity_conflict(selected, source):
        result["protocol_binding"] = {
            "status": "source_method_identity_conflict",
            "method": selected["method"],
            "explanation": "Selected method and source row disagree on a +/* variant marker; correct the identity before attaching a count.",
        }
        if row["action"] == "propose_count":
            result.update(action="protocol_binding_unresolved", proposed_num_runs=None)
        return result
    identities = {method_key(selected["method"]), method_key(selected["method"].split("(")[0])}
    label_key = source_method_key(selected, source)
    if label_key:
        identities.add(label_key)
    matches = [
        key
        for key in keys
        if key["table_id"] == selected["table_id"]
        and method_key(key["method"]["name"]) in identities
    ]
    if not matches:
        review = verified_override(row, source, protocol_reviews)
        if row["action"] == "propose_count" and review:
            result["protocol_binding"] = {
                "status": "independently_verified_new_method_scope",
                "review": review,
            }
            return result
        if row["action"] == "propose_count" and source_verified_unknown_prior(row, source, []):
            result["protocol_binding"] = {
                "status": "source_verified_new_method_scope",
                "explanation": (
                    "No prior key matches this exact table/method. The selected result cell, "
                    "self-evaluated origin, execution, and protocol are independently "
                    "supported and source-grounded, so its row-scoped count stands on its "
                    "own evidence."
                ),
            }
            return result
        result["protocol_binding"] = {
            "status": "method_scope_extension_unverified",
            "table_id": selected["table_id"],
            "method": selected["method"],
            "explanation": "No exact upstream table/method key. Alias or shared-baseline scope needs explicit verification; do not silently copy another method's count.",
        }
        if row["action"] == "propose_count":
            result.update(action="protocol_binding_unresolved", proposed_num_runs=None)
        return result
    totals = {input_total(key) for key in matches}
    evidence = [span for key in matches for span in key["method"].get("count_evidence", [])]
    result["protocol_binding"] = {
        "status": "matched",
        "table_id": selected["table_id"],
        "method": selected["method"],
        "input_totals": sorted(t for t in totals if t is not None),
        "contains_unknown": None in totals,
        "evidence": evidence,
    }
    if row["action"] != "propose_count":
        return result
    review = verified_override(row, source, protocol_reviews)
    if review and (len(totals) != 1 or None in totals or row["proposed_num_runs"] not in totals):
        result["protocol_binding"].update(
            status="independently_verified_protocol_override",
            previous_status="matched",
            review=review,
        )
        return result
    if totals == {None} and source_verified_unknown_prior(row, source, matches):
        result["protocol_binding"].update(
            status="source_verified_unknown_prior",
            previous_status="upstream_unknown_or_conflict",
            explanation=(
                "The prior table/method key supplies no verified count. The current exact "
                "result cell, self-evaluated origin, execution and protocol are independently "
                "supported and source-grounded, so its row-scoped count is used."
            ),
        )
        return result
    if len(totals) != 1 or None in totals:
        result["protocol_binding"]["status"] = "upstream_unknown_or_conflict"
        result.update(action="protocol_input_unresolved", proposed_num_runs=None)
    elif row["proposed_num_runs"] not in totals:
        result["protocol_binding"]["status"] = "count_mismatch"
        result.update(action="protocol_input_conflict", proposed_num_runs=None)
    return result
