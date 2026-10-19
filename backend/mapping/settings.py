import copy


def guard_setting_scope(row: dict) -> dict:
    result = copy.deepcopy(row)
    verdict = result.get("verdict", {})
    fact = verdict.get("corrected_fact", {})
    executed = (
        verdict.get("origin_supported") is True
        and verdict.get("execution_supported") is True
        and fact.get("origin") == "self_evaluated"
        and bool(fact.get("execution_evidence"))
    )
    if executed or verdict.get("setting_status") != "contradicted":
        return result
    # This is only a scope gate. Real ablation/other-protocol exclusions stay excluded.
    if result.get("reason") == "contradicted_setting":
        result.update(action="setting_scope_unresolved", proposed_num_runs=None)
        result["withheld_setting_exclusion"] = result.pop("reason")
    correction = result.get("correction")
    if correction and correction["old"]["variant"] != correction["corrected"]["variant"]:
        result["withheld_setting_correction"] = {
            "old": correction["old"]["variant"],
            "corrected": correction["corrected"]["variant"],
        }
        correction["corrected"]["variant"] = correction["old"]["variant"]
        if correction["old"] == correction["corrected"]:
            result["correction"] = None
    if "withheld_setting_exclusion" in result or "withheld_setting_correction" in result:
        result.setdefault("safety_notes", []).append(
            "Current-paper split scope is not established for this copied/unknown baseline. "
            "Do not quarantine or rewrite its setting from an author-level protocol statement; "
            "numeric/metric cell repairs are assessed separately."
        )
    return result
