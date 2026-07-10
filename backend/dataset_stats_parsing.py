"""Shared helpers for parsing and comparing dataset statistics."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Any

_STAT_MARKERS = (
    "#graphs",
    "num graphs",
    "number of graphs",
    "avg. #nodes",
    "avg #nodes",
    "avg nodes",
    "number of nodes",
    "num nodes",
    "avg. #edges",
    "avg #edges",
    "avg edges",
    "number of edges",
    "num edges",
    "heterophily",
    "homophily",
    "density",
    "diameter",
    "output dim",
    "#classes",
    "num classes",
    "number of classes",
    "label fraction",
    "train/val/test",
    "train val test",
)
_NUMBER_RE = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?")

STAT_TABLE_MARKERS = (
    "statistic",
    "dataset",
    "#graphs",
    "num graphs",
    "avg nodes",
    "avg edges",
    "properties",
    "summary",
    "total graphs",
    "total nodes",
)


def is_statistics_table(table: Any, *, header: str | None = None) -> bool:
    caption = (getattr(table, "caption", "") or "").strip().lower()
    header_text = header if header is not None else str(getattr(table, "header", "") or "")
    header_lower = header_text.lower()
    return any(marker in caption or marker in header_lower for marker in STAT_TABLE_MARKERS)


def format_stats_summary(
    entry: dict[str, Any] | None = None,
    *,
    num_graphs: int | float | None = None,
    avg_nodes: float | None = None,
    avg_edges: float | None = None,
    num_classes: int | float | None = None,
    extra_stats: dict | None = None,
    raw_values: dict | None = None,
    separator: str = ", ",
) -> str:
    """Format core dataset statistics for logs and dev export tables."""
    if entry is not None:
        num_graphs = entry.get("num_graphs")
        avg_nodes = entry.get("avg_nodes")
        avg_edges = entry.get("avg_edges")
        num_classes = entry.get("num_classes")
        extra_stats = entry.get("extra_stats") or {}
        raw_values = entry.get("raw_values") or {}

    parts: list[str] = []
    raw_values = raw_values or {}
    for key, label in (
        ("num_graphs", "graphs"),
        ("avg_nodes", "nodes"),
        ("avg_edges", "edges"),
        ("num_classes", "classes"),
    ):
        values = {
            "num_graphs": num_graphs,
            "avg_nodes": avg_nodes,
            "avg_edges": avg_edges,
            "num_classes": num_classes,
        }
        value = values[key]
        if value is not None:
            display = raw_values.get(key, value)
            parts.append(f"{label}={display}")

    if extra_stats:
        for key, value in sorted(extra_stats.items()):
            parts.append(f"{key}={value}")
    return separator.join(parts) if parts else "—"


def parse_number(raw: str | int | float | None) -> float | int | None:
    if raw is None:
        return None
    if isinstance(raw, bool):
        return None
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float):
        return int(raw) if raw.is_integer() else raw
    text = str(raw).strip()
    if not text or text.lower() in {"-", "—", "na", "n/a", "none"}:
        return None
    text = text.replace(",", "")
    m = _NUMBER_RE.search(text)
    if not m:
        return None
    val = float(m.group(0))
    if val.is_integer():
        return int(val)
    return val


@dataclass(frozen=True)
class AbbreviatedNumber:
    nominal: float
    scale: float
    raw: str
    is_approximate: bool = False


def parse_abbreviated_number(raw: str | int | float | None) -> AbbreviatedNumber | None:
    if raw is None:
        return None
    if isinstance(raw, (int, float)) and not isinstance(raw, bool):
        val = float(raw)
        return AbbreviatedNumber(nominal=val, scale=1.0, raw=str(raw))

    text = str(raw).strip()
    if not text:
        return None
    is_approximate = text[0] in {"~", "≈", "∼"} or "approx" in text.lower()
    clean = re.sub(r"^[~≈∼]+\s*", "", text, flags=re.IGNORECASE)
    clean = clean.replace(",", "").strip()

    scale_patterns = [
        (r"^([-+]?\d*\.?\d+)\s*(?:million|millions|m)\b", 1_000_000.0),
        (r"^([-+]?\d*\.?\d+)\s*(?:thousand|thousands|k)\b", 1_000.0),
        (r"^([-+]?\d*\.?\d+)\s*k\b", 1_000.0),
        (r"^([-+]?\d*\.?\d+)\s*m\b", 1_000_000.0),
    ]
    for pattern, scale in scale_patterns:
        m = re.match(pattern, clean, flags=re.IGNORECASE)
        if m:
            coeff = float(m.group(1))
            return AbbreviatedNumber(
                nominal=coeff * scale,
                scale=scale,
                raw=text,
                is_approximate=is_approximate,
            )

    parsed = parse_number(clean)
    if parsed is None:
        return None
    return AbbreviatedNumber(
        nominal=float(parsed), scale=1.0, raw=text, is_approximate=is_approximate
    )


def header_role(header: str) -> str | None:
    h = header.strip().lower()
    if any(x in h for x in ["#graphs", "num graphs", "graphs", "items", "molecules"]):
        return "num_graphs"
    if any(x in h for x in ["avg. #nodes", "avg #nodes", "avg nodes", "nodes"]):
        return "avg_nodes"
    if any(x in h for x in ["avg. #edges", "avg #edges", "avg edges", "edges"]):
        return "avg_edges"
    if any(x in h for x in ["output dim", "#classes", "classes", "targets", "labels"]):
        return "num_classes"
    if any(x in h for x in ["dataset", "name"]):
        return "dataset"
    return None


def detect_precision_hint(
    raw: str | None,
    parsed: float | int | None,
    explicit_hint: str | None = None,
) -> str:
    if explicit_hint in {"abbreviated", "rounded", "exact"}:
        return explicit_hint
    if raw is None:
        return "exact"
    text = str(raw).strip().lower()
    if re.search(r"\b(k|m|thousand|million)\b", text) or re.search(r"\d\s*[km]\b", text):
        return "abbreviated"
    if text.startswith(("~", "≈", "∼")) or "approx" in text:
        return "rounded"
    if parsed is not None and isinstance(parsed, (int, float)):
        val = float(parsed)
        if val >= 1000 and val % 1000 == 0:
            return "rounded"
        if val >= 100 and val % 100 == 0:
            return "rounded"
    return "exact"


def _rounding_granularity(value: float) -> float:
    if value >= 1_000_000:
        return 1_000_000.0
    if value >= 1000:
        return 1000.0
    if value >= 100:
        return 100.0
    if value >= 10:
        return 10.0
    return 1.0


def _rounded_bucket_bounds(nominal: float, *, widen: bool = False) -> tuple[float, float]:
    gran = _rounding_granularity(nominal)
    low = nominal - gran
    high = nominal + gran
    if widen:
        low -= gran
        high += gran
    return low, high


def _abbreviated_bounds(abbrev: AbbreviatedNumber, *, widen: bool = False) -> tuple[float, float]:
    if abbrev.scale > 1.0:
        coeff = abbrev.nominal / abbrev.scale
        if coeff == int(coeff):
            n = int(coeff)
            low = (n - 1) * abbrev.scale
            high = (n + 1) * abbrev.scale
            if widen:
                low -= abbrev.scale
                high += abbrev.scale
            return low, high
        low = abbrev.nominal - abbrev.scale
        high = abbrev.nominal + abbrev.scale
        if widen:
            low -= abbrev.scale
            high += abbrev.scale
        return low, high
    return _rounded_bucket_bounds(abbrev.nominal, widen=widen)


def values_compatible(
    paper_value: float | int | None,
    canonical_value: float | int | None,
    *,
    raw_value: str | None = None,
    precision_hint: str | None = None,
    is_integer_field: bool = False,
) -> tuple[bool, str]:
    """Return (compatible, match_tier_description)."""
    if paper_value is None or canonical_value is None:
        return True, "skipped"

    paper_f = float(paper_value)
    canon_f = float(canonical_value)
    hint = detect_precision_hint(raw_value, paper_value, precision_hint)

    if hint == "exact":
        if is_integer_field:
            if paper_f == canon_f:
                return True, "exact"
            rel = abs(paper_f - canon_f) / max(abs(canon_f), 1.0)
            if rel <= 0.02:
                return True, "precise_2pct"
            return False, "mismatch_precise"
        rel = abs(paper_f - canon_f) / max(abs(canon_f), 1.0)
        if rel <= 0.05:
            return True, "precise_5pct"
        return False, "mismatch_precise"

    abbrev = parse_abbreviated_number(raw_value if raw_value is not None else paper_value)
    if abbrev is None:
        return False, "mismatch_unparsed"

    widen = abbrev.is_approximate or hint == "rounded"
    low, high = _abbreviated_bounds(abbrev, widen=widen)
    if low < canon_f <= high:
        tier = "abbreviated" if abbrev.scale > 1.0 else "rounded_bucket"
        if widen:
            tier += "_wide"
        return True, tier

    if hint == "rounded" and abbrev.scale == 1.0:
        gran = _rounding_granularity(abbrev.nominal)
        candidates = {
            math.floor(canon_f / gran) * gran,
            round(canon_f / gran) * gran,
            math.ceil(canon_f / gran) * gran,
        }
        if any(abs(c - abbrev.nominal) < 1e-9 for c in candidates):
            return True, "rounded_union"

    return False, "mismatch_imprecise"


def text_has_stat_markers(text: str) -> bool:
    lower = text.lower()
    return any(marker in lower for marker in _STAT_MARKERS)


def ripgrep_stat_markers_near_datasets(text: str, dataset_names: list[str]) -> dict[str, bool]:
    """Return {dataset_name: statistics_mentioned} based on local context."""
    lower = text.lower()
    hits: dict[str, bool] = {}
    for name in dataset_names:
        pattern = rf"(?<![A-Za-z0-9-]){re.escape(name)}(?![A-Za-z0-9-])"
        mentioned = False
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            start = max(0, match.start() - 400)
            end = min(len(lower), match.end() + 400)
            window = lower[start:end]
            if text_has_stat_markers(window):
                mentioned = True
                break
        hits[name] = mentioned
    return hits


def parse_extra_stats(raw: Any) -> dict[str, float | int]:
    if not isinstance(raw, dict):
        return {}
    out: dict[str, float | int] = {}
    for key, value in raw.items():
        parsed = parse_number(value) if not isinstance(value, (int, float)) else value
        if parsed is not None:
            out[str(key)] = parsed
    return out
