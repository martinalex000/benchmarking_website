import copy
import re

from backend.mapping.source import active_source_lines, printed_matches
from backend.repetition_metadata import table_inventory
from backend.repetition_storage import name_key


def presentation_safety(row: dict, source: str) -> dict:
    result = copy.deepcopy(row)
    candidate = result.get("selected_candidate")
    if not candidate:
        return result
    tables = [t for t in table_inventory(source) if t["table_id"] == candidate["table_id"]]
    if len(tables) != 1:
        return result
    table = tables[0]
    lines = active_source_lines(source)
    # Only the local experimental introduction and table can establish this table's
    # uncertainty. Do not apply a confidence interval mentioned elsewhere in a paper.
    before = max(0, table["start_line"] - 31)
    context = "\n".join(lines[before : table["end_line"]])
    intervals = re.search(r"\b(?:confidence|credible)\s+intervals?\b", context, re.I)
    if intervals and candidate.get("displayed_std") is not None:
        result.update(action="special_uncertainty", proposed_num_runs=None)
        result["uncertainty_type"] = "interval_not_std"
        result["uncertainty_scope"] = {"start_line": before + 1, "end_line": table["end_line"]}
        if result.get("correction"):
            result["withheld_uncertainty_repair"] = result.pop("correction")
            result["correction"] = None
        return result
    correction = result.get("correction")
    if not correction or row.get("std") is None:
        return result
    if abs(correction["old"]["value"] - correction["corrected"]["value"]) < 1e-9:
        return result
    selected_line = candidate["cell_evidence"]["start_line"]
    selected_column = candidate.get("cell_column_index")
    if selected_column is None:
        return result
    method = name_key(row["model"])
    conflicts = []
    for number in range(table["start_line"], table["end_line"] + 1):
        cells = re.split(r"(?<!\\)&", lines[number - 1])
        # Some tables put datasets in rows and backbone/method combinations in
        # columns. An old mean/std pair in another column is configuration evidence,
        # not permission to replace it by the chosen default backbone's score.
        if number == selected_line and cells and name_key(row["dataset"]) in name_key(cells[0]):
            for column, cell in enumerate(cells[1:], 1):
                if column == selected_column:
                    continue
                if any(
                    all(
                        printed_matches(value * scale, value, scale, cell)
                        for value in (row["value"], row["std"])
                    )
                    for scale in (1, 100)
                ):
                    conflicts.append(number)
            continue
        if len(cells) <= selected_column or method not in name_key(cells[0]):
            continue
        cell = cells[selected_column]
        if any(
            all(
                printed_matches(value * scale, value, scale, cell)
                for value in (row["value"], row["std"])
            )
            for scale in (1, 100)
        ):
            conflicts.append(number)
    if conflicts:
        result.update(action="configuration_scope_unresolved", proposed_num_runs=None)
        result["withheld_cross_configuration_repair"] = result.pop("correction")
        result["correction"] = None
        result["competing_old_value_lines"] = conflicts
    return result
