import json
import math
from collections import Counter
from pathlib import Path

FIELDS = {
    "value": "mean",
    "std": "std",
    "metric": "metric",
    "model": "method",
    "variant": "configuration",
    "dataset": "dataset",
}


def changed(old, new) -> bool:
    if isinstance(old, (int, float)) and isinstance(new, (int, float)):
        return not math.isclose(old, new, rel_tol=0, abs_tol=1e-9)
    return old != new


def override_counts(proposals: list[dict]) -> dict:
    """Count changed fields and unique affected rows separately (types can overlap)."""
    counts = Counter(dict.fromkeys(FIELDS.values(), 0))
    counts.update(num_runs=0, copied_exclusion=0, quarantine=0)
    affected, repaired = set(), set()
    reasons, actions = Counter(), Counter()
    for row in proposals:
        rid = row["result_id"]
        action = row["action"]
        actions[action] += 1
        repair = row.get("correction")
        dataset_review = row.get("dataset_identity_review")
        if dataset_review and dataset_review["old_dataset"] != dataset_review["corrected_dataset"]:
            counts["dataset"] += 1
            affected.add(rid)
            repaired.add(rid)
        if repair:
            for field, kind in FIELDS.items():
                old, new = repair["old"], repair["corrected"]
                if field in old and field in new and changed(old[field], new[field]):
                    counts[kind] += 1
                    affected.add(rid)
                    repaired.add(rid)
        if (
            action == "propose_count"
            and row.get("proposed_num_runs") is not None
            and row.get("num_runs") != row["proposed_num_runs"]
        ):
            counts["num_runs"] += 1
            affected.add(rid)
        if action in {"copied_excluded", "propose_quarantine"}:
            counts["copied_exclusion" if action == "copied_excluded" else "quarantine"] += 1
            affected.add(rid)
            if action == "propose_quarantine":
                reasons[row.get("reason", "unspecified")] += 1
    return {
        "rows_checked": len(proposals),
        "rows_with_proposed_changes": len(affected),
        "rows_with_field_repairs": len(repaired),
        "types": dict(counts),
        "quarantine_reasons": dict(sorted(reasons.items())),
        "decisions": dict(sorted(actions.items())),
    }


def write_override_log(root: Path) -> Path:
    manifest = json.loads((root / "manifest.json").read_text())
    lines = [
        "Proposed override counts — dry run only; no changes applied to database.",
        "One count per changed field per row; categories can overlap. Affected rows are unique.",
        "Count assignments equal to stored counts and withheld repairs are not overrides.",
        "Copied exclusions/quarantines are proposed dispositions, not executed removals.",
        "Decision counts include unresolved/failed cases separately; they are not overrides or accuracy.",
        "",
    ]
    for paper in manifest["papers"]:
        folder = root / "papers" / paper["paper_id"]
        proposals_path = folder / "proposals.json"
        proposals = json.loads(proposals_path.read_text()) if proposals_path.exists() else []
        assessment_path = folder / "assessment.json"
        state = (
            json.loads(assessment_path.read_text())["state"]
            if assessment_path.exists()
            else "pending"
        )
        title = " ".join(paper.get("title", "").split())
        counts = override_counts(proposals)
        refresh_path = folder / "protocol_refresh.json"
        if refresh_path.exists():
            refresh = json.loads(refresh_path.read_text())
            for key in (
                "human_reviewed_keys",
                "reverified_single_cv_keys",
                "accepted_single_cv_keys",
            ):
                counts[key] = refresh.get(key, 0)
        summary = "; ".join(
            f"{key}={value}" for key, value in counts.items() if not isinstance(value, dict)
        )
        details = " | ".join(
            f"{key}: " + (", ".join(f"{kind}={count}" for kind, count in value.items()) or "none")
            for key, value in counts.items()
            if isinstance(value, dict)
        )
        lines.append(f"{paper['paper_id']} | {title} | state={state} | {summary} | {details}")
    destination = root / "override_counts.log"
    destination.write_text("\n".join(lines) + "\n")
    return destination
