import copy
import re

from backend.mapping.binding import apply_human_protocol_review, check_binding
from backend.mapping.decisions import (
    Candidate,
    grounded_candidate,
)
from backend.mapping.repair_feedback import configuration_axis_repair_errors
from backend.mapping.schema import Span
from backend.mapping.source import (
    active_source_lines,
    evidence_text,
    name_key,
    printed_matches,
)
from backend.repetition_metadata import table_inventory


def partial_std_repair(row: dict, source: str) -> dict | None:
    """Repair the narrow case of normalized mean with an unnormalized std."""
    raw = row.get("selected_candidate")
    if not raw or raw.get("divisor") != 100 or row.get("correction") or row.get("std") is None:
        return None
    candidate = Candidate.model_validate(raw)
    if (
        candidate.divisor != 100
        or candidate.displayed_std is None
        or name_key(candidate.method) != name_key(row["model"])
        or name_key(candidate.dataset) != name_key(row["dataset"])
        or abs(candidate.displayed_mean / 100 - row["value"]) > 1e-9
        or abs(candidate.displayed_std - row["std"]) > 1e-9
        or candidate.displayed_std == 0
        or grounded_candidate(candidate, source) is None
    ):
        return None
    old = {k: row[k] for k in ("value", "std", "model", "variant", "metric")}
    return {
        "old": old,
        "corrected": {**old, "std": candidate.displayed_std / 100},
        "evidence": [candidate.cell_evidence.model_dump(), candidate.column_evidence.model_dump()],
        "explanation": "Grounded percentage cell: mean was normalized but std was left in percentage units. Normalize std by the same divisor; do not infer origin or repetitions.",
    }


def earlier_exact(row: dict, hints: list[dict]) -> bool:
    actual = (row.get("correction") or {}).get("corrected", row)
    for hint in hints:
        if hint["result_id"] != row["result_id"]:
            continue
        for match in hint.get("matches", []):
            if name_key(match["model"]) != name_key(actual["model"]):
                continue
            if abs(match["value"] - actual["value"]) > 1e-9:
                continue
            a, b = match["std"], actual["std"]
            if a == b or a is not None and b is not None and abs(a - b) < 1e-9:
                return True
    return False


def copied_evidence(row: dict, source: str, hints: list[dict]) -> bool:
    if earlier_exact(row, hints):
        return True  # Strong indication under the user's policy, not chronological proof.
    fact = row.get("verdict", {}).get("corrected_fact", {})
    text = evidence_text([Span.model_validate(s) for s in fact.get("origin_evidence", [])], source)
    if re.search(r"\botherwise\b.*\brun\b", text, re.I):
        return False  # Conditional copying does not identify this row's branch.
    if re.search(
        r"\b(?:copied|taken|adopted|reported results|best reported results)\b|"
        r"\bresults\b[^.!?]{0,100}\b(?:come|obtained|taken) from\b",
        text,
        re.I,
    ):
        return True
    candidate = row.get("selected_candidate", {})
    for table in table_inventory(source):
        if table["table_id"] == candidate.get("table_id") and re.search(
            r"\breference\b", table["body"], re.I
        ):
            return bool(re.search(r"\\cite", text))
    return False


def explicit_execution_rebuttal(row: dict, source: str) -> bool:
    """Earlier coincidences must not defeat explicit, scoped current-paper execution."""
    verdict = row.get("verdict", {})
    if not verdict.get("origin_supported") or not verdict.get("execution_supported"):
        return False
    fact = verdict.get("corrected_fact", {})
    text = evidence_text(
        [Span.model_validate(s) for s in fact.get("execution_evidence", [])], source
    )
    if re.search(r"\botherwise\b|\bif\b[^.!?]{0,120}\breported results\b", text, re.I):
        return False
    method = (row.get("correction") or {}).get("corrected", row)["model"]
    stem = re.split(r"[+(]", method)[0].strip()
    scoped = re.search(rf"\b{re.escape(stem)}\b", text, re.I) or re.search(
        r"\ball baselines\b", text, re.I
    )
    executed = re.search(
        r"\bwe\b[^.!?]{0,600}\btrain(?:ed|ing)?\b(?!/)|\bwe\s+(?:run|ran|evaluate(?:d)?)\b",
        text,
        re.I,
    )
    return bool(scoped and executed)


def conflicting_prose_value(row: dict, source: str) -> list[int]:
    correction = row.get("correction")
    candidate = row.get("selected_candidate")
    if (
        not correction
        or not candidate
        or correction["old"]["value"] == correction["corrected"]["value"]
    ):
        return []
    old = correction["old"]
    if (
        candidate["divisor"] == 100
        and abs(old["value"] / 100 - correction["corrected"]["value"]) < 1e-9
    ):
        return []  # An actual percent-to-fraction conversion is not a new experiment.
    tables = table_inventory(source)
    found = []
    for number, line in enumerate(active_source_lines(source), 1):
        if any(t["start_line"] <= number <= t["end_line"] for t in tables):
            continue
        if name_key(old["model"]) not in name_key(line):
            continue
        if old["std"] is None:
            continue  # A bare repeated scalar is too weak for this guard.
        if all(printed_matches(value, value, 1, line) for value in (old["value"], old["std"])):
            found.append(number)
    return found


def safe_assignment(
    row: dict,
    keys: list[dict],
    source: str,
    hints: list[dict],
    scope_links: list[dict] = (),
    protocol_reviews: list[dict] = (),
) -> dict:
    result = copy.deepcopy(row)
    notes = []
    normalization = partial_std_repair(result, source)
    if normalization:
        result["correction"] = normalization
        if result["action"] == "repair_unverified":
            result.update(action="numeric_repair_only", proposed_num_runs=None)
        notes.append("Partial percent normalization repaired from the grounded table cell.")
    conflicting = conflicting_prose_value(result, source)
    if conflicting:
        result.update(
            action="configuration_scope_unresolved", proposed_num_runs=None, correction=None
        )
        result["withheld_cross_experiment_repair"] = copy.deepcopy(row["correction"])
        result["prose_occurrence_lines"] = conflicting
        notes.append(
            "Old mean/std occurs in method-specific prose outside tables. Do not replace it with a different table experiment merely by main-paper priority."
        )
    if result["action"] == "copied_excluded" and not copied_evidence(result, source, hints):
        result.update(action="origin_unresolved", proposed_num_runs=None)
        notes.append(
            "Copied classification lacks explicit copying/attribution or an earlier exact same-method mean/std indication; no author count is assigned."
        )
    if (
        result["action"] == "propose_count"
        and earlier_exact(result, hints)
        and not explicit_execution_rebuttal(result, source)
    ):
        result.update(action="origin_conflict_unresolved", proposed_num_runs=None)
        notes.append(
            "Earlier exact same-method mean/std conflicts with the self-evaluated assignment. "
            "Require explicit row-scoped execution review; this indication is not an automatic copied rule."
        )
    correction = result.get("correction")
    if (
        correction
        and correction["old"]["variant"] != correction["corrected"]["variant"]
        and (
            result.get("verdict", {}).get("setting_status") != "contradicted"
            or re.search(
                r"copied|as reported|reported result", correction["corrected"]["variant"], re.I
            )
        )
    ):
        correction["corrected"]["variant"] = correction["old"]["variant"]
        correction["explanation"] += (
            " Compatible or unverified existing setting label retained by the safety pass."
        )
        notes.append(
            "Setting-label refinement or origin-only replacement withheld; origin is not a split/configuration label."
        )
        if correction["old"] == correction["corrected"]:
            result["correction"] = None
    protocol = result.get("protocol")
    if protocol and protocol.get("cv_repeat_unit") == "within_fold":
        protocol["variability_scope"] = "unknown"
        protocol["explanation"] = (
            f"{protocol['cv_folds']} folds with {protocol['cv_repetitions']} repetitions within each fold; "
            "total models follow the agreed product convention. Std aggregation is not established by this statement."
        )
        if result.get("selected_candidate"):
            result["selected_candidate"]["protocol"] = copy.deepcopy(protocol)
    result, human_review = apply_human_protocol_review(result, source, protocol_reviews)
    if human_review:
        protocol_reviews = [
            review for review in protocol_reviews if review.get("result_id") != result["result_id"]
        ]
        protocol_reviews.append(human_review)
    axis_errors = configuration_axis_repair_errors(
        result,
        result.get("selected_candidate") or {},
        result.get("correction"),
    )
    if axis_errors and result["action"] in {
        "propose_count",
        "copied_excluded",
        "numeric_repair_only",
    }:
        correction = result.pop("correction", None)
        if correction:
            result["withheld_configuration_axis_repair"] = correction
        result.update(action="configuration_scope_unresolved", proposed_num_runs=None)
        notes.extend(axis_errors)
    original_action = result["action"]
    result = check_binding(result, keys, source, protocol_reviews)
    if original_action == "propose_count" and result["action"] == "protocol_binding_unresolved":
        matches = [
            link
            for link in scope_links
            if link["result_id"] == row["result_id"] and link["supported"]
        ]
        if len(matches) == 1 and matches[0]["inherited_num_runs"] == row["proposed_num_runs"]:
            result.update(
                action="propose_count", proposed_num_runs=matches[0]["inherited_num_runs"]
            )
            result["protocol_binding"] = {
                "status": "verified_scope_extension",
                "link": matches[0]["link"],
            }
    result["safety_notes"] = notes
    return result
