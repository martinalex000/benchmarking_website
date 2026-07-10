"""Helpers for auditing suspicious extracted method names."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from backend.config import cfg
from backend.llm_postprocessing import (
    _canonical_model_name_key,
    _is_generic_proposed_name,
    _matches_proposed_model_name,
    _normalise_model_name_text,
    _title_looks_like_benchmarking_study,
)
from backend.paper_storage import PaperStorage

_GENERIC_RESULT_NAMES = {
    "baseline",
    "graph neural network",
    "method",
    "model",
    "our method",
    "our model",
    "ours",
    "proposed method",
    "proposed model",
    "this work",
}
_LATEX_OR_REFERENCE_PATTERN = re.compile(
    r"\\[A-Za-z]+|\{[^}]*\}|~\\cite|ref\.?|table\s+\d|figure\s+\d",
    re.IGNORECASE,
)


@dataclass(slots=True)
class MethodNameAuditFinding:
    arxiv_id: str
    title: str
    proposed_name: str | None
    suggested_name: str | None
    candidate_names: list[str]
    suspicious_result_names: list[str]
    reasons: list[str]
    benchmark_title: bool
    has_model_renames: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def audit_method_names(
    paper_ids: list[str] | None = None,
    papers_root: Path | None = None,
) -> list[MethodNameAuditFinding]:
    """Return suspicious papers whose extracted method names deserve manual review."""
    root = papers_root or cfg.papers_dir
    ids = paper_ids or _discover_paper_ids(root)
    findings: list[MethodNameAuditFinding] = []

    for arxiv_id in ids:
        finding = audit_single_paper(arxiv_id, papers_root=root)
        if finding is not None:
            findings.append(finding)

    findings.sort(key=lambda item: (len(item.reasons), item.arxiv_id), reverse=True)
    return findings


def audit_extraction_payload(
    arxiv_id: str,
    title: str,
    results_payload: dict[str, Any],
    overrides: dict[str, Any] | None = None,
) -> MethodNameAuditFinding | None:
    """Audit an in-memory extraction payload without reading from disk."""
    proposed_info = results_payload.get("proposed_model") or {}
    proposed_name = _clean_name(proposed_info.get("name"))
    overrides = overrides or {}

    proposed_rows = [
        _clean_name(entry.get("model"))
        for entry in results_payload.get("results") or []
        if entry.get("is_proposed") and _clean_name(entry.get("model"))
    ]
    candidate_names = _unique_names(proposed_rows)
    suspicious_result_names = _unique_names(
        _clean_name(entry.get("model"))
        for entry in results_payload.get("results") or []
        if _looks_like_suspicious_result_name(entry.get("model"))
    )

    reasons: list[str] = []
    benchmark_title = _title_looks_like_benchmarking_study(title.lower())
    suggested_name = _choose_suggested_name(title, candidate_names)
    proposed_key = _canonical_model_name_key(proposed_name) if proposed_name else ""
    candidate_keys = {_canonical_model_name_key(name): name for name in candidate_names if name}

    if benchmark_title and proposed_name and _is_generic_or_placeholder(proposed_name):
        reasons.append("benchmark paper has a proposed model name")

    if not proposed_name and candidate_names:
        reasons.append("proposed rows exist but proposed_model is missing")

    if proposed_name and _is_generic_or_placeholder(proposed_name):
        reasons.append("proposed model name is generic or placeholder text")

    if proposed_name and _looks_like_rendering_artifact(proposed_name):
        reasons.append("proposed model name still contains LaTeX or citation text")

    family_matches = [
        name for name in candidate_names if _matches_proposed_model_name(name, proposed_name)
    ]

    if (
        proposed_name
        and candidate_names
        and proposed_key
        and proposed_key not in candidate_keys
        and not family_matches
    ):
        reasons.append("proposed model does not match any proposed result row")

    if len(candidate_keys) > 1 and len(family_matches) != len(candidate_names):
        reasons.append("multiple distinct proposed result names")

    if suspicious_result_names:
        reasons.append("result rows contain suspicious method labels")

    if not reasons:
        return None

    return MethodNameAuditFinding(
        arxiv_id=arxiv_id,
        title=title,
        proposed_name=proposed_name,
        suggested_name=suggested_name,
        candidate_names=candidate_names,
        suspicious_result_names=suspicious_result_names,
        reasons=reasons,
        benchmark_title=benchmark_title,
        has_model_renames=bool(overrides.get("model_renames") or {}),
    )


def audit_single_paper(
    arxiv_id: str,
    papers_root: Path | None = None,
) -> MethodNameAuditFinding | None:
    """Audit the stored extraction for one paper."""
    storage = PaperStorage(arxiv_id, papers_root=papers_root)
    if not storage.llm_output_path.exists():
        return None

    raw = storage.load_llm_output()
    results_payload = raw.get("results") or {}
    title = _load_title(storage, raw)
    overrides = _load_overrides(storage.overrides_path)
    return audit_extraction_payload(
        arxiv_id=arxiv_id,
        title=title,
        results_payload=results_payload,
        overrides=overrides,
    )


def _discover_paper_ids(root: Path) -> list[str]:
    return sorted(path.name for path in root.iterdir() if path.is_dir()) if root.exists() else []


def _load_title(storage: PaperStorage, raw: dict[str, Any]) -> str:
    if storage.metadata_path.exists():
        metadata = json.loads(storage.metadata_path.read_text(encoding="utf-8"))
        title = str(metadata.get("title") or "").strip()
        if title:
            return title
    return str(raw.get("title") or storage.arxiv_id).strip()


def _load_overrides(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    import yaml

    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _clean_name(value: Any) -> str:
    if value is None:
        return ""
    return _normalise_model_name_text(str(value))


def _unique_names(names: Any) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for raw_name in names:
        name = _clean_name(raw_name)
        if not name:
            continue
        key = _canonical_model_name_key(name) or name.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(name)
    return ordered


def _choose_suggested_name(title: str, candidate_names: list[str]) -> str | None:
    if not candidate_names:
        return None
    title_lower = title.lower()
    title_matches = [name for name in candidate_names if _clean_name(name).lower() in title_lower]
    if len(title_matches) == 1:
        return title_matches[0]
    if len(candidate_names) == 1:
        return candidate_names[0]
    return None


def _is_generic_or_placeholder(name: str) -> bool:
    lowered = _clean_name(name).lower()
    if not lowered:
        return True
    if lowered in _GENERIC_RESULT_NAMES or _is_generic_proposed_name(name):
        return True
    return "benchmark" in lowered or "dataset" in lowered or "datasets" in lowered


def _looks_like_rendering_artifact(name: str) -> bool:
    return bool(_LATEX_OR_REFERENCE_PATTERN.search(str(name)))


def _looks_like_suspicious_result_name(name: Any) -> bool:
    clean = _clean_name(name)
    if not clean:
        return False
    lowered = clean.lower()
    return lowered in _GENERIC_RESULT_NAMES or _looks_like_rendering_artifact(clean)
