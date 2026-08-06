"""LLM-guided, deterministic extraction from expanded LaTeX tables.

The LLM supplies the table/dataset/task/method selection and method renames.  This
module is deliberately responsible for reading numeric cells only from LaTeX.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

import pandas as pd
from pydantic import BaseModel, Field

from backend.config import cfg
from backend.llm_types import (
    BaselineModelInfo,
    DatasetInfo,
    ExtractionOutput,
    ProposedModel,
    ResultEntry,
)
from backend.results_parser import (
    normalize_dataset_scaled_metric,
    normalize_percentage_metric,
    parse_value_std,
)

logger = logging.getLogger(__name__)


class GuidedMethod(BaseModel):
    source_names: list[str] = Field(default_factory=list)
    output_name: str
    is_proposed: bool = False


class GuidedTask(BaseModel):
    name: str = ""
    metric: str
    columns: list[str] = Field(default_factory=list)
    higher_is_better: bool = True
    input_feature_source: str | None = None
    feature_source_evidence: str | None = None


class GuidedDataset(BaseModel):
    name: str
    table_refs: list[str] = Field(default_factory=list)
    tasks: list[GuidedTask] = Field(default_factory=list)
    statistics_mentioned: bool = False
    statistics_sources: list[str] = Field(default_factory=list)


class GuidedTableSpec(BaseModel):
    table_ref: str
    include_results: bool = True
    exclusion_reason: str = ""
    datasets: list[GuidedDataset] = Field(default_factory=list)
    methods: list[GuidedMethod] = Field(default_factory=list)


class GuidedDiscovery(BaseModel):
    tables: list[GuidedTableSpec] = Field(default_factory=list)
    notes: str = ""


@dataclass
class ParsedLatexTable:
    frame: pd.DataFrame
    raw_rows: list[list[str]]
    table_ref: str


_TABLE_REF_RE = re.compile(r"table\s*(\d+)", re.IGNORECASE)
_TABULAR_RE = re.compile(
    r"\\begin\{(?:tabular\*?|tabularx|tabulary|tabu|longtable)\}"
    r"(?:\s*\[[^]]*\])?\s*\{(?:[^{}]|\{[^{}]*\})*\}"
    r"(.*?)\\end\{(?:tabular\*?|tabularx|tabulary|tabu|longtable)\}",
    re.DOTALL,
)


def _split_latex(text: str, separator: str) -> list[str]:
    """Split on a LaTeX separator outside nested braces."""
    parts: list[str] = []
    start = 0
    depth = 0
    escaped = False
    for index, char in enumerate(text):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "{":
            depth += 1
        elif char == "}" and depth:
            depth -= 1
        elif text.startswith(separator, index) and depth == 0:
            parts.append(text[start:index])
            start = index + len(separator)
    parts.append(text[start:])
    return parts


def _strip_latex_cell(value: str) -> str:
    value = re.sub(r"%.*", "", value).strip()
    value = value.replace(r"\pm", "±").replace(r"\%", "%").replace(r"\times", "×")
    value = re.sub(
        r"\\(?:textbf|mathbf|mathrm|textit|emph|underline|text|mbox)\s*\{([^{}]*)\}",
        r"\1",
        value,
    )
    value = re.sub(r"\\(?:footnotesize|scriptsize|small|large|centering|arraystretch)\b", "", value)
    value = re.sub(r"\\(?:[a-zA-Z]+|[^a-zA-Z\s])", "", value)
    value = value.replace("~", " ").replace("\\&", "&")
    value = value.replace("$", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" {}")


def _local_latex_macros(body: str) -> dict[str, tuple[int, str]]:
    """Collect simple braced-argument macros that expand table headers."""
    macros: dict[str, tuple[int, str]] = {}
    pattern = re.compile(
        r"\\(?:newcommand|renewcommand)\s*\{\\(?P<name>[A-Za-z]+)\}"
        r"\s*\[(?P<arity>\d+)\]\s*\{(?P<replacement>(?:[^{}]|\{[^{}]*\})*)\}",
        re.DOTALL,
    )
    for match in pattern.finditer(body):
        macros[match.group("name")] = (
            int(match.group("arity")),
            match.group("replacement"),
        )
    return macros


def _braced_arguments(value: str, count: int) -> tuple[list[str], str] | None:
    arguments: list[str] = []
    position = 0
    for _ in range(count):
        while position < len(value) and value[position].isspace():
            position += 1
        if position >= len(value) or value[position] != "{":
            return None
        depth = 1
        end = position + 1
        while end < len(value) and depth:
            if value[end] == "{":
                depth += 1
            elif value[end] == "}":
                depth -= 1
            end += 1
        if depth:
            return None
        arguments.append(value[position + 1 : end - 1])
        position = end
    return arguments, value[position:].strip()


def _expand_cell(cell: str, local_macros: dict[str, tuple[int, str]] | None = None) -> list[str]:
    cell = cell.strip()
    match = re.match(r"\\multicolumn\s*\{(\d+)\}\s*\{[^}]*\}\s*\{(.*)\}\s*$", cell, re.DOTALL)
    if match:
        return [_strip_latex_cell(match.group(2))] + [""] * (int(match.group(1)) - 1)
    if local_macros:
        macro_match = re.match(r"\\(?P<name>[A-Za-z]+)(?P<arguments>.*)$", cell, re.DOTALL)
        if macro_match and macro_match.group("name") in local_macros:
            arity, replacement = local_macros[macro_match.group("name")]
            parsed = _braced_arguments(macro_match.group("arguments"), arity)
            if parsed is not None:
                arguments, remainder = parsed
                if not remainder:
                    expanded = replacement
                    for index, argument in enumerate(arguments, start=1):
                        expanded = expanded.replace(f"#{index}", argument)
                    return _expand_cell(expanded, local_macros)
    return [_strip_latex_cell(cell)]


def _latex_rows(
    body: str, local_macros: dict[str, tuple[int, str]] | None = None
) -> list[list[str]]:
    rows: list[list[str]] = []
    # A row terminator is two literal backslashes.  Splitting with the generic
    # escaped-character scanner would mistake it for an escaped slash.
    row_chunks = re.split(r"\\\\(?:\s*\[[^]]*\])?", body)
    for raw_row in row_chunks:
        row = re.sub(
            r"\\(?:toprule|midrule|bottomrule|hline|cline\{[^}]*\}|cmidrule(?:\([^)]*\))?\{[^}]*\})",
            "",
            raw_row,
        ).strip()
        if not row or re.fullmatch(
            r"(?:\\toprule|\\midrule|\\bottomrule|\\hline|\\cline\{[^}]+\}|\\cmidrule[^\n]*)+", row
        ):
            continue
        cells: list[str] = []
        for cell in _split_latex(row, "&"):
            cells.extend(_expand_cell(cell, local_macros))
        if cells and any(cell for cell in cells):
            rows.append(cells)
    width = max((len(row) for row in rows), default=0)
    return [row + [""] * (width - len(row)) for row in rows]


def parse_latex_table(table: Any) -> ParsedLatexTable:
    """Convert one ``LatexTable`` body into a DataFrame."""
    body = getattr(table, "body", "")
    match = _TABULAR_RE.search(body)
    rows = _latex_rows(match.group(1) if match else body, _local_latex_macros(body))
    if not rows:
        raise ValueError("no tabular rows found")
    header = rows[0]
    columns = [cell or f"column_{index + 1}" for index, cell in enumerate(header)]
    columns = _unique_columns(columns)
    frame = pd.DataFrame(rows[1:], columns=columns)
    return ParsedLatexTable(frame=frame, raw_rows=rows, table_ref=f"Table {table.number}")


def build_table_column_guide(table: Any) -> str:
    """Describe grouped header spans without extracting any numeric cells.

    A flat DataFrame cannot represent a ``dataset × metric`` header.  This small
    deterministic aid gives the extraction model the missing alignment while
    leaving the complete raw table as the source of numeric values.
    """
    body = getattr(table, "body", "")
    match = _TABULAR_RE.search(body)
    rows = _latex_rows(match.group(1) if match else body, _local_latex_macros(body))
    if not rows:
        return ""

    dataset_row = next(
        (row for row in rows if row and row[0].casefold().strip() == "dataset"), None
    )
    metric_row = next((row for row in rows if row and row[0].casefold().strip() == "metric"), None)
    if dataset_row is None or metric_row is None:
        return ""

    groups: list[tuple[str, int, int]] = []
    current_dataset = ""
    start = 0
    width = max(len(dataset_row), len(metric_row))
    for index in range(1, width):
        cell = dataset_row[index] if index < len(dataset_row) else ""
        if cell.strip():
            if current_dataset:
                end = index - 1
                while end >= start and (end >= len(metric_row) or not metric_row[end].strip()):
                    end -= 1
                groups.append((current_dataset, start, end))
            current_dataset = cell.strip()
            start = index
    if current_dataset:
        end = width - 1
        while end >= start and (end >= len(metric_row) or not metric_row[end].strip()):
            end -= 1
        groups.append((current_dataset, start, end))

    # A useful guide requires an actual span and at least one metric label.
    grouped = [group for group in groups if group[2] > group[1]]
    if not grouped:
        return ""

    lines = [
        "=== COLUMN GROUP GUIDE (header-only; read numeric values from the raw table) ===",
        "Use the dataset span first, then the metric label within that span; do not flatten grouped columns.",
    ]
    for dataset, first, last in grouped:
        metrics = [
            metric_row[index].strip()
            for index in range(first, min(last + 1, len(metric_row)))
            if metric_row[index].strip()
        ]
        metric_text = ", ".join(metrics) or "metric labels unavailable"
        lines.append(
            f"- table columns {first + 1}-{last + 1}: dataset {dataset!r}; metrics: {metric_text}"
        )
    return "\n".join(lines)


def _unique_columns(columns: list[str]) -> list[str]:
    counts: dict[str, int] = {}
    result: list[str] = []
    for column in columns:
        count = counts.get(column, 0)
        counts[column] = count + 1
        result.append(column if count == 0 else f"{column}_{count + 1}")
    return result


def _table_number(ref: str) -> int | None:
    match = _TABLE_REF_RE.search(ref)
    return int(match.group(1)) if match else None


def _matches(value: str, selectors: list[str]) -> bool:
    value_key = re.sub(r"\W+", " ", value.casefold()).strip()
    return not selectors or any(
        re.sub(r"\W+", " ", selector.casefold()).strip() in value_key for selector in selectors
    )


def _method_for_row(raw_name: str, methods: list[GuidedMethod]) -> GuidedMethod | None:
    key = raw_name.casefold().strip()
    for method in methods:
        if key == method.output_name.casefold().strip() or any(
            key == alias.casefold().strip() for alias in method.source_names
        ):
            return method
    return None


def _log_guided_error(payload: dict[str, Any]) -> None:
    try:
        cfg.logs_dir.mkdir(parents=True, exist_ok=True)
        with (cfg.logs_dir / "guided_table_errors.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {"timestamp": datetime.now(UTC).isoformat(), **payload}, ensure_ascii=False
                )
                + "\n"
            )
    except OSError as exc:
        logger.warning("Could not write guided-table global diagnostics: %s", exc)


def extract_guided_results(
    latex_tables: list[Any],
    discovery: GuidedDiscovery,
    *,
    arxiv_id: str,
) -> ExtractionOutput:
    """Extract selected result cells and never infer numeric values."""
    by_number = {getattr(table, "number", None): table for table in latex_tables}
    results: list[ResultEntry] = []
    datasets: dict[str, DatasetInfo] = {}
    proposed: dict[str, ProposedModel] = {}
    baselines: dict[str, BaselineModelInfo] = {}
    notes = [discovery.notes] if discovery.notes else []
    from backend.table_caption_interpretation import (
        build_table_caption_policy_map,
        is_ablation_table_ref,
    )

    caption_policies = build_table_caption_policy_map(latex_tables)

    for spec in discovery.tables:
        number = _table_number(spec.table_ref)
        table = by_number.get(number)
        if not spec.include_results or table is None:
            if spec.include_results and table is None:
                _log_guided_error(
                    {
                        "arxiv_id": arxiv_id,
                        "table_ref": spec.table_ref,
                        "kind": "missing_table",
                        "message": "LLM referenced a table not present in LaTeX",
                    }
                )
            continue
        if is_ablation_table_ref(spec.table_ref, caption_policies):
            _log_guided_error(
                {
                    "arxiv_id": arxiv_id,
                    "table_ref": spec.table_ref,
                    "kind": "ablation_rejected",
                    "message": "Deterministic caption policy rejected an ablation or diagnostic table",
                }
            )
            continue
        if not spec.datasets or not spec.methods:
            continue
        try:
            parsed = parse_latex_table(table)
        except Exception as exc:
            _log_guided_error(
                {
                    "arxiv_id": arxiv_id,
                    "table_ref": spec.table_ref,
                    "kind": "table_parse",
                    "message": str(exc),
                    "latex": getattr(table, "body", "")[:4000],
                }
            )
            continue

        method_column = parsed.frame.columns[0]
        for dataset in spec.datasets:
            datasets.setdefault(
                dataset.name.casefold(),
                DatasetInfo(
                    name=dataset.name,
                    table_refs=dataset.table_refs or [spec.table_ref],
                    primary_metric=dataset.tasks[0].metric if dataset.tasks else None,
                    statistics_mentioned=dataset.statistics_mentioned,
                    statistics_sources=list(dataset.statistics_sources),
                ),
            )
            for task in dataset.tasks:
                columns = [
                    column
                    for column in parsed.frame.columns
                    if _matches(str(column), task.columns or [task.metric])
                ]
                if not columns:
                    _log_guided_error(
                        {
                            "arxiv_id": arxiv_id,
                            "table_ref": spec.table_ref,
                            "dataset": dataset.name,
                            "metric": task.metric,
                            "kind": "missing_column",
                            "message": "No selected task column matched the parsed header",
                            "columns": [str(column) for column in parsed.frame.columns],
                        }
                    )
                    continue
                for _, row in parsed.frame.iterrows():
                    raw_method = str(row[method_column]).strip()
                    method = _method_for_row(raw_method, spec.methods)
                    if method is None:
                        continue
                    model_name = method.output_name
                    if method.is_proposed:
                        proposed.setdefault(model_name.casefold(), ProposedModel(name=model_name))
                    else:
                        baselines.setdefault(
                            model_name.casefold(), BaselineModelInfo(name=model_name)
                        )
                    for column in columns:
                        raw_value = row[column]
                        value, std = parse_value_std(raw_value)
                        if value is None:
                            _log_guided_error(
                                {
                                    "arxiv_id": arxiv_id,
                                    "table_ref": spec.table_ref,
                                    "dataset": dataset.name,
                                    "metric": task.metric,
                                    "method": model_name,
                                    "kind": "invalid_value",
                                    "raw_value": str(raw_value),
                                }
                            )
                            continue
                        value, std = normalize_percentage_metric(task.metric, value, std)
                        value, std = normalize_dataset_scaled_metric(
                            dataset.name, task.metric, value, std
                        )
                        results.append(
                            ResultEntry(
                                model=model_name,
                                is_proposed=method.is_proposed,
                                dataset=dataset.name,
                                metric=task.metric,
                                value=value,
                                std=std,
                                higher_is_better=task.higher_is_better,
                                input_feature_source=task.input_feature_source,
                                feature_source_evidence=task.feature_source_evidence,
                                table_ref=spec.table_ref,
                            )
                        )

    confidence = "HIGH" if results else "LOW"
    if not results:
        notes.append("Guided-table parsing produced no numeric result rows.")
    return ExtractionOutput(
        proposed_model=next(iter(proposed.values()), None),
        baseline_models=list(baselines.values()),
        results=results,
        extraction_confidence=confidence,
        extraction_notes="\n".join(notes),
        discovered_datasets=list(datasets.values()),
        paper_has_statistics=any(item.statistics_mentioned for item in datasets.values()),
    )
