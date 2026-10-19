"""Results parser — converts LLM extraction output into DB records.

Handles:
  - Fuzzy dataset variant resolution (exact → thefuzz)
  - Model canonical name lookup + alias matching; creates new models if unseen
  - Numeric value normalisation ("mean±std", parenthetical std)
  - Skips rows where is_overridden=1 already exists in DB
  - Calls apply_overrides_to_db after writing new records

Usage::
    python -m backend.results_parser 2206.08164
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import re
from dataclasses import dataclass, field
from typing import Any

import yaml
from thefuzz import fuzz as fuzz_lib
from thefuzz import process as fuzz_process

from backend.config import cfg, normalize_arxiv_id
from backend.dataset_discovery import SUPPORTED_TASK_TYPES
from backend.db import init_db, session_scope
from backend.llm_postprocessing import _normalise_model_name_text
from backend.llm_types import DatasetInfo, normalize_input_feature_source
from backend.method_name_audit import audit_extraction_payload
from backend.model_metadata import normalize_architecture_type
from backend.model_metadata_defaults import load_model_metadata_defaults, lookup_model_type
from backend.model_name_resolution import (
    ROLE_SUFFIX_RE,
    model_names_fuzzy_compatible,
    normalize_model_name_for_resolution,
    ogb_dataset_families_compatible,
)
from backend.models import (
    DatasetVariant,
    Model,
    ModelAlias,
    Paper,
    Result,
)
from backend.override_handler import apply_overrides_to_db, get_result_override
from backend.paper_storage import PaperStorage
from backend.parameter_lookup import build_dataset_param_lookup as _build_dataset_param_lookup
from backend.parameter_lookup import build_metadata_lookups as _build_metadata_lookups
from backend.physical_unit_targets import (
    is_physical_unit_dataset,
    normalize_physical_result_mapping,
)
from backend.qm7b_targets import is_qm7b_dataset, normalize_qm7b_result_mapping
from backend.qm9_targets import (
    is_qm9_dataset,
    normalize_qm9_metric,
    normalize_qm9_result_mapping,
)
from backend.repetition_metadata import supports_repeat_count
from backend.repository_linking import (
    find_verified_repository_link,
    repository_source_from_storage,
    repository_url_exists,
)
from backend.text_cleanup import (
    abstract_has_latex_artifacts,
    authors_look_broken,
    clean_extracted_text,
)
from backend.venue import resolve_canonical_venue, venue_needs_resolution

logger = logging.getLogger(__name__)


def _apply_feature_source_model_name(entry: dict[str, Any]) -> None:
    """Apply the stable MLP display name even when parsing an older artifact."""
    source = normalize_input_feature_source(entry.get("input_feature_source", entry.get("f")))
    entry["input_feature_source"] = source
    if "feature_source_evidence" not in entry and "x" in entry:
        entry["feature_source_evidence"] = entry.get("x")
    if source != "llm_features":
        return
    model = str(entry.get("model") or "").strip()
    base = re.sub(r"\s*\([^)]*\)\s*$", "", model.rstrip("*")).strip().casefold()
    if base == "mlp":
        entry["model"] = "MLP+LLM_features"


def _validated_run_metadata(entry: dict[str, Any]) -> tuple[int | None, int | None, str | None]:
    """Return conservative run metadata for a result row.

    A paper-level count must not leak onto cited rows. Keep it only when the
    extractor explicitly identifies an author-trained row and supplies evidence
    containing the same count attached to a repetition unit, not merely folds or epochs.
    """
    trained = parse_optional_extracted_bool(entry.get("trained_by_paper"))
    trained_db = 1 if trained is True else 0 if trained is False else None
    raw_count = entry.get("num_runs")
    evidence = str(entry.get("num_runs_evidence") or "").strip()
    source_ref = str(entry.get("source_ref") or "").strip().casefold()

    if trained is not True or source_ref != "this paper" or not evidence:
        return None, trained_db, None
    if isinstance(raw_count, bool):
        return None, trained_db, None
    try:
        numeric_count = float(raw_count)
    except (TypeError, ValueError):
        return None, trained_db, None
    if not numeric_count.is_integer() or numeric_count <= 0:
        return None, trained_db, None
    num_runs = int(numeric_count)
    design = (
        "repeated_cv"
        if re.search(r"cross.validation|\bfold", evidence, re.I)
        else "repeated_training"
    )
    if not supports_repeat_count(num_runs, evidence, design):
        return None, trained_db, None
    return num_runs, trained_db, evidence


# ── Dataset alias normalisation (post-extraction) ─────────────────────────────

_DATASET_ALIAS_MAP: dict[str, str] | None = None
_AMBIGUOUS_DATASET_NAMES: set[str] | None = None
_PROTOCOL_EXCLUSIONS: dict[str, Any] | None = None
_PROTOCOL_CONTRACTS: dict[str, Any] | None = None


def _load_dataset_alias_map() -> dict[str, str]:
    """Load the user-facing alias map from ``config/dataset_aliases.yaml``."""
    global _DATASET_ALIAS_MAP
    if _DATASET_ALIAS_MAP is None:
        path = cfg.config_dir / "dataset_aliases.yaml"
        if path.exists():
            with path.open(encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
            raw = data.get("aliases", {})
            _DATASET_ALIAS_MAP = {k.strip().lower(): v.strip() for k, v in raw.items()}
        else:
            _DATASET_ALIAS_MAP = {}
    return _DATASET_ALIAS_MAP


def normalize_dataset_alias(dataset_name: str, arxiv_id: str | None = None) -> str:
    """Return the canonical dataset name, honoring narrow paper-specific aliases."""
    path = cfg.config_dir / "dataset_aliases.yaml"
    if path.exists() and arxiv_id:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        paper_map = (data.get("paper_aliases") or {}).get(str(arxiv_id).strip(), {})
        if isinstance(paper_map, dict):
            target = {
                str(key).strip().casefold(): str(value).strip() for key, value in paper_map.items()
            }.get(dataset_name.strip().casefold())
            if target:
                return target
    key = dataset_name.strip().lower()
    return _load_dataset_alias_map().get(key, dataset_name)


def is_ambiguous_dataset_name(dataset_name: str) -> bool:
    """Return whether a generic name is unsafe to resolve by fuzzy matching."""
    global _AMBIGUOUS_DATASET_NAMES
    if _AMBIGUOUS_DATASET_NAMES is None:
        path = cfg.config_dir / "dataset_aliases.yaml"
        if path.exists():
            with path.open(encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
            _AMBIGUOUS_DATASET_NAMES = {
                str(name).strip().casefold() for name in (data.get("ambiguous_names") or [])
            }
        else:
            _AMBIGUOUS_DATASET_NAMES = set()
    return dataset_name.strip().casefold() in _AMBIGUOUS_DATASET_NAMES


def _load_protocol_exclusions() -> dict[str, Any]:
    global _PROTOCOL_EXCLUSIONS
    if _PROTOCOL_EXCLUSIONS is None:
        path = cfg.config_dir / "protocol_exclusions.yaml"
        if path.exists():
            with path.open(encoding="utf-8") as fh:
                _PROTOCOL_EXCLUSIONS = yaml.safe_load(fh) or {}
        else:
            _PROTOCOL_EXCLUSIONS = {}
    return _PROTOCOL_EXCLUSIONS


def _load_protocol_contracts() -> dict[str, Any]:
    global _PROTOCOL_CONTRACTS
    if _PROTOCOL_CONTRACTS is None:
        path = cfg.config_dir / "protocol_contracts.yaml"
        if path.exists():
            with path.open(encoding="utf-8") as fh:
                _PROTOCOL_CONTRACTS = yaml.safe_load(fh) or {}
        else:
            _PROTOCOL_CONTRACTS = {}
    return _PROTOCOL_CONTRACTS


def _allowed_by_protocol_curation(
    arxiv_id: str,
    variant: DatasetVariant,
    model_name: str | None = None,
    metric_name: str | None = None,
) -> bool:
    exclusions = _load_protocol_exclusions()
    if arxiv_id in (exclusions.get("exclude_all_results") or {}):
        return False
    excluded_datasets = (exclusions.get("exclude_datasets") or {}).get(arxiv_id) or {}
    if isinstance(excluded_datasets, dict):
        excluded_names = {str(name).strip().casefold() for name in excluded_datasets}
    else:
        excluded_names = {str(name).strip().casefold() for name in excluded_datasets}
    if (variant.dataset.name or "").strip().casefold() in excluded_names:
        return False
    row_rules = (exclusions.get("exclude_results") or {}).get(arxiv_id) or {}
    dataset_rules = row_rules.get((variant.dataset.name or "").strip())
    if dataset_rules is None:
        dataset_rules = row_rules.get((variant.dataset.name or "").strip().casefold())
    if isinstance(dataset_rules, dict):
        excluded_models = {
            str(name).strip().casefold() for name in (dataset_rules.get("models") or [])
        }
        excluded_metrics = {
            str(name).strip().casefold() for name in (dataset_rules.get("metrics") or [])
        }
        if model_name and str(model_name).strip().casefold() in excluded_models:
            return False
        if metric_name and str(metric_name).strip().casefold() in excluded_metrics:
            return False
    allowed_tasks = (exclusions.get("allowed_dataset_tasks") or {}).get(arxiv_id)
    return not allowed_tasks or variant.dataset.task_type in allowed_tasks


def _curation_excludes_all_results(arxiv_id: str) -> bool:
    return arxiv_id in (_load_protocol_exclusions().get("exclude_all_results") or {})


# ── Metric normalisation ──────────────────────────────────────────────────────

# Metrics that should be in [0, 1] but are sometimes reported as percentages
# (e.g. 44.2 instead of 0.442).  MAE/RMSE/loss intentionally excluded.
_PERCENTAGE_METRIC_TOKENS: frozenset[str] = frozenset(
    {
        "accuracy",
        "acc",
        "f1",
        "ap",
        "map",
        "auc",  # covers AUC, ROC-AUC, AUC-ROC
        "auroc",  # AUROC
        "mrr",
    }
)
_PERCENTAGE_METRIC_PREFIXES: tuple[str, ...] = ("hits@",)

_TRUE_STRINGS = frozenset({"true", "t", "yes", "y", "1"})
_FALSE_STRINGS = frozenset({"false", "f", "no", "n", "0"})

_ZINC_SUBSET_ALIASES: tuple[str, ...] = (
    "zinc",
    "zinc subset",
    "zinc subset (12k)",
    "zinc 12k",
    "zinc-12k",
    "zinc12k",
)
_ZINC_FULL_ALIASES: tuple[str, ...] = (
    "zinc full",
    "full zinc",
    "zinc-full",
    "zinc 250k",
    "zinc full dataset",
)
_ZINC_SUBSET_CUE_RE = re.compile(
    r"(?:zinc[^\n]{0,120}(?:12k|12,000|12000|subset)|"
    r"(?:12k|12,000|12000)[^\n]{0,120}zinc|"
    r"benchmarking graph neural networks|"
    r"arxiv:?\s*2003\.00982)",
    re.IGNORECASE,
)
_ZINC_FULL_CUE_RE = re.compile(
    r"(?:zinc[^\n]{0,120}(?:249,456|249456|250,000|250000|full)|"
    r"(?:249,456|249456|250,000|250000)[^\n]{0,120}zinc|"
    r"tab[:_ -]*zinc[_ -]*full)",
    re.IGNORECASE,
)
_ZINC_FULL_MAX_MAE = 0.06
_ZINC_SUBSET_MIN_MAE = 0.07

_OGB_DATASET_ALIASES: dict[str, str] = {
    "ogbg-code2": "ogbg-code2",
    "ogbg-moltox21": "tox21",
}
_DATASET_VARIANT_QUALIFIER_RE = re.compile(
    r"\b(?:full|subset|random|temporal|continual|few[- ]shot|test[- ](?:dev|challenge)|"
    r"challenge|competition|large|small|ca)\b",
    re.IGNORECASE,
)

# token_sort_ratio >= 88 matched the current model set well enough to reuse
# obvious variants like punctuation or spacing changes without collapsing short
# families such as GCN into unrelated names like GatedGCN.
_MODEL_FUZZY_MATCH_MIN_SCORE = 88


@dataclass
class ParseStoreSummary:
    arxiv_id: str
    extraction_model: str = "unknown"
    new_results: int = 0
    updated_results: int = 0
    candidate_results: int = 0
    replaced_results: int = 0
    skipped_unknown_datasets: list[str] = field(default_factory=list)
    skipped_invalid_values: list[str] = field(default_factory=list)
    skipped_protocol_mismatches: list[str] = field(default_factory=list)
    uncertain_protocol_results: list[str] = field(default_factory=list)
    created_models: list[str] = field(default_factory=list)
    created_stub_paper: bool = False
    metadata_changed: bool = False
    overrides_applied: int = 0
    quarantined: bool = False
    quarantine_reasons: list[str] = field(default_factory=list)
    quarantine_model_names: list[str] = field(default_factory=list)


def _is_percentage_metric(metric_name: str) -> bool:
    key = metric_name.strip().lower()
    if any(key.startswith(prefix) for prefix in _PERCENTAGE_METRIC_PREFIXES):
        return True
    tokens = [token for token in re.split(r"[^a-z0-9@]+", key) if token]
    return any(token in _PERCENTAGE_METRIC_TOKENS for token in tokens)


def parse_extracted_bool(value: Any, *, default: bool) -> bool:
    """Normalize bool-like extraction values without treating non-empty strings as true."""
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, (int, float)) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        key = value.strip().lower()
        if key in _TRUE_STRINGS:
            return True
        if key in _FALSE_STRINGS:
            return False
    logger.warning("Could not parse boolean value %r; using default=%s", value, default)
    return default


def parse_optional_extracted_bool(value: Any) -> bool | None:
    """Normalize optional bool-like extraction values; return None for unknown/missing."""
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        key = value.strip().lower()
        if key in _TRUE_STRINGS:
            return True
        if key in _FALSE_STRINGS:
            return False
    logger.warning("Could not parse optional boolean value %r; using None", value)
    return None


_TASK_TYPE_ALIASES: dict[str, str] = {
    "node classification": "node_classification",
    "node-classification": "node_classification",
    "graph classification": "graph_classification",
    "graph-classification": "graph_classification",
    "graph regression": "graph_regression",
    "graph-regression": "graph_regression",
    "node regression": "node_regression",
    "node-regression": "node_regression",
    "link prediction": "link_prediction",
    "link-prediction": "link_prediction",
    "edge prediction": "link_prediction",
    "edge-prediction": "link_prediction",
}

_NONSTANDARD_PROTOCOL_CUE_RE = re.compile(
    r"\b(?:"
    r"selected\s+(?:balanced\s+)?tasks?|"
    r"(?:balanced|hand[- ]picked|chosen|selected)\s+(?:task|label)s?|"
    r"most\s+balanced\s+(?:task|label)s?|"
    r"subset(?:\s+of)?\s+(?:the\s+)?(?:\d+\s+)?tasks?|"
    r"(?:only|just)\s+\d+\s+tasks?|"
    r"(?:not|fewer\s+than|less\s+than)\s+(?:all|the\s+full)\s+\d*\s*tasks?|"
    r"(?:custom|non[- ]standard|random|stratified|temporal|time[- ]based|chronological|"
    r"size[- ]based|scaffold[- ]free|ood|out[- ]of[- ]distribution)\s+split|"
    r"different\s+split|"
    r"largest\s+\d+%\s+of\s+(?:graphs|molecules)|"
    r"\b(?:few[- ]shot|linear[- ]probe|linear probing|continual|"
    r"attack|backdoor|poison|asr|attack success|cta|meta[- ]attack|"
    r"attribute injection|robustness|training accuracy|validation accuracy|"
    r"accuracy ratio|correlation coefficient|correlation between|tgb|dynamic destination)\b"
    r")\b",
    re.IGNORECASE,
)


def _protocol_contract_for_variant(variant: DatasetVariant) -> dict[str, Any]:
    contracts = _load_protocol_contracts().get("datasets") or {}
    dataset_name = getattr(variant.dataset, "name", "") or ""
    return contracts.get(str(dataset_name).strip().casefold()) or {}


def _contract_patterns_match(patterns: Any, note: str) -> bool:
    return any(re.search(str(pattern), note, re.IGNORECASE) for pattern in (patterns or []))


def _protocol_contract_disallows(entry: dict[str, Any], variant: DatasetVariant) -> bool:
    contract = _protocol_contract_for_variant(variant)
    note = str(entry.get("protocol_note") or "").strip()
    return bool(note and _contract_patterns_match(contract.get("forbidden_any"), note))


def _protocol_contract_has_evidence(entry: dict[str, Any], variant: DatasetVariant) -> bool:
    contract = _protocol_contract_for_variant(variant)
    required = contract.get("required_any")
    if not required:
        return True
    note = str(entry.get("protocol_note") or "").strip()
    return bool(note and _contract_patterns_match(required, note))


def _requires_explicit_protocol_evidence(variant: DatasetVariant) -> bool:
    """Return whether this canonical variant has a declared split contract."""
    return bool(
        getattr(variant, "is_standard", False)
        and (getattr(variant, "split_type", None) or _protocol_contract_for_variant(variant))
    )


def _protocol_note_indicates_nonstandard(entry: dict[str, Any]) -> bool:
    note = str(entry.get("protocol_note") or "").strip()
    return bool(note and _NONSTANDARD_PROTOCOL_CUE_RE.search(note))


def _protocol_note_indicates_metric_mismatch(
    entry: dict[str, Any], variant: DatasetVariant
) -> bool:
    """Reject rows whose local evidence names a different reported metric."""
    note = str(entry.get("protocol_note") or "").casefold()
    metric = str(entry.get("metric") or "").strip().casefold()
    if not note or not metric:
        return False
    if metric == "mrr" and re.search(r"\bhits?\s*@?\s*\d+\b", note):
        return True
    return metric in {"accuracy", "acc"} and bool(
        re.search(r"\b(?:accuracy\s+ratio|correlation(?:\s+coefficient)?|pearson)\b", note)
    )


def _normalized_evaluation_task(value: Any) -> str:
    task = str(value or "").strip().casefold().replace("_", " ")
    return _TASK_TYPE_ALIASES.get(task, task.replace(" ", "_"))


def _protocol_compatible_with_variant(entry: dict[str, Any], variant: DatasetVariant) -> bool:
    """Whether a versioned extraction explicitly contradicts the canonical task.

    Missing protocol fields are treated as unknown rather than incompatible.
    This is intentionally recall-oriented: older models and partially upgraded
    prompts may omit the declaration even when the extracted result is valid.
    """
    expected_task = _normalized_evaluation_task(variant.dataset.task_type)
    actual_task = _normalized_evaluation_task(entry.get("evaluation_task"))
    return not actual_task or actual_task == expected_task


def _protocol_decision(entry: dict[str, Any], variant: DatasetVariant) -> str:
    """Normalize the LLM protocol decision with a safe legacy fallback."""
    expected_task = _normalized_evaluation_task(variant.dataset.task_type)
    actual_task = _normalized_evaluation_task(entry.get("evaluation_task"))
    if actual_task and actual_task != expected_task:
        return "nonstandard"

    if _protocol_contract_disallows(entry, variant):
        return "nonstandard"

    if _protocol_note_indicates_metric_mismatch(entry, variant):
        return "nonstandard"

    # A row-local note describing a subset or custom split overrides an
    # overconfident LLM decision. Wisconsin is the one deliberate exception:
    # the canonical Geom-GCN masks are sometimes described as random splits,
    # so the cited Pei/Geom-GCN or PyG evidence must be considered first.
    if _protocol_note_indicates_nonstandard(entry):
        contract = _protocol_contract_for_variant(variant)
        note = str(entry.get("protocol_note") or "")
        canonical_random_split = bool(
            contract.get("allow_canonical_random_split")
            and re.search(r"\brandom\b[^.]{0,40}\bsplits?\b", note, re.IGNORECASE)
            and _protocol_contract_has_evidence(entry, variant)
        )
        if not canonical_random_split:
            return "nonstandard"

    decision = str(entry.get("protocol_decision") or "").strip().casefold()
    if decision == "nonstandard":
        return decision
    if _requires_explicit_protocol_evidence(variant) and not _protocol_contract_has_evidence(
        entry, variant
    ):
        contract = _protocol_contract_for_variant(variant)
        if decision == "standard" and contract.get("allow_standard_decision_without_evidence"):
            return "standard"
        return "uncertain"
    if decision in {"standard", "nonstandard", "uncertain"}:
        if (
            decision == "standard"
            and _requires_explicit_protocol_evidence(variant)
            and not str(entry.get("protocol_note") or "").strip()
        ):
            return "uncertain"
        return decision

    standard = parse_optional_extracted_bool(entry.get("uses_standard_protocol"))
    if standard is True and actual_task == expected_task:
        return "standard"
    # A false legacy boolean is not enough to distinguish a clearly
    # non-standard experiment from an uncertain/omitted declaration.
    return "uncertain"


def _protocol_result_is_eligible(decision: str, variant: DatasetVariant) -> bool:
    """Return whether a parsed row may become a canonical benchmark result."""
    if decision == "nonstandard" or not getattr(variant, "is_standard", True):
        return False
    return not (decision == "uncertain" and _requires_explicit_protocol_evidence(variant))


def _manual_protocol_note(arxiv_id: str, dataset_name: str) -> str | None:
    notes = (_load_protocol_exclusions().get("manual_protocol_notes") or {}).get(arxiv_id) or {}
    if not isinstance(notes, dict):
        return None
    dataset_key = str(dataset_name or "").strip().casefold()
    for name, note in notes.items():
        if str(name).strip().casefold() == dataset_key and str(note).strip():
            return str(note).strip()
    return None


def result_is_leaderboard_eligible(result: Result) -> bool:
    """Apply the current protocol contract to a stored result row.

    Parsing enforces this before insertion, but legacy rows predate the
    contracts. Export paths must apply the same rule so unsupported historical
    rows cannot re-enter a final comparison merely because they still exist in
    the database.
    """
    variant = result.dataset_variant
    if variant is None:
        return True
    if not variant.is_standard:
        return False
    paper = result.paper
    arxiv_id = paper.arxiv_id if paper else ""
    if not _allowed_by_protocol_curation(
        arxiv_id,
        variant,
        model_name=result.effective_model_name,
        metric_name=result.metric_name,
    ):
        return False
    contract = _protocol_contract_for_variant(variant)
    if not contract and not getattr(variant, "split_type", None):
        # Preserve legacy datasets that have no declared contract at all, while
        # still honoring explicit task/protocol contradictions and the global
        # curation exclusions above.
        if result.protocol_decision == "nonstandard":
            return False
        return _protocol_compatible_with_variant(
            {"evaluation_task": getattr(result, "evaluation_task", None)}, variant
        )
    note = _manual_protocol_note(arxiv_id, variant.dataset.name) or result.protocol_note
    entry = {
        "evaluation_task": result.evaluation_task,
        "protocol_decision": result.protocol_decision,
        "protocol_note": note,
        "uses_standard_protocol": True,
    }
    return _protocol_decision(entry, variant) == "standard"


def source_indicates_incompatible_protocol(
    entry: dict[str, Any], variant: DatasetVariant, paper_text: str
) -> bool:
    """Reject explicit row-local protocol mismatches.

    Protocol evidence must be attached to the extracted row (normally via the
    table caption/header or ``protocol_note``). Scanning the whole paper is
    unsafe for multi-task benchmarks such as LRGB: a paper can legitimately
    discuss link prediction for PCQM-Contact while reporting graph or node
    classification results for other datasets.

    ``paper_text`` remains in the signature for compatibility, but is
    intentionally not used as row-level evidence.
    """
    del paper_text
    return _protocol_decision(entry, variant) == "nonstandard"


def normalize_percentage_metric(
    metric_name: str,
    value: float,
    std: float | None,
) -> tuple[float, float | None]:
    """Convert percentage-scale metrics from [0, 100] to [0, 1].

    If *value* > 1.0 and the metric is a known percentage-type metric,
    divides both value and std by 100.  Returns unchanged values otherwise.
    """
    if value <= 1.0 or not _is_percentage_metric(metric_name):
        return value, std
    if value > 100.0:
        logger.warning(
            "Metric %r value %.4f is outside [0, 100] — skipping normalisation",
            metric_name,
            value,
        )
        return value, std
    normalized = value / 100.0
    normalized_std = std / 100.0 if std is not None else None
    logger.debug(
        "Normalised %r: %.4f±%s → %.6f±%s",
        metric_name,
        value,
        std,
        normalized,
        normalized_std,
    )
    return normalized, normalized_std


def normalize_dataset_scaled_metric(
    dataset_name: str,
    metric_name: str,
    value: float,
    std: float | None,
) -> tuple[float, float | None]:
    """Correct known dataset-specific scale conventions omitted by extraction.

    Some papers report Peptides-struct MAE on a x100 scale while the benchmark
    leaderboard and the rest of the repo store the native decimal value.
    """
    dataset_key = dataset_name.strip().lower()
    metric_key = metric_name.strip().lower()
    if dataset_key == "peptides-struct" and metric_key == "mae" and value > 2.0:
        return value / 100.0, std / 100.0 if std is not None else None
    return value, std


def _dataset_metric_value_is_valid(dataset_name: str, metric_name: str, value: float) -> bool:
    """Reject values that violate an unambiguous dataset/metric invariant."""
    if not math.isfinite(value):
        return False
    dataset_key = dataset_name.strip().casefold()
    metric_key = metric_name.strip().casefold()
    if _is_percentage_metric(metric_name) and not 0.0 <= value <= 1.0:
        # Accuracy-like metrics are normalised to [0, 1]. This also blocks
        # negative sentinels such as -1.0 from becoming artificial SOTA rows.
        return False
    # log10-transformed error metrics legitimately take negative values.  The
    # SSSP catalog metric is still named MSE although this benchmark reports
    # log10(MSE), so retain its negative values as well.
    if (
        any(token in metric_key for token in ("mae", "rmse", "mse", "error", "loss"))
        and "log10" not in metric_key
        and not (dataset_key == "sssp" and metric_key == "mse")
        and value < 0
    ):
        # Error metrics are non-negative; negative values are almost always a
        # missing-value sentinel or a column/metric mismatch.
        return False
    # The QM9 HOMO-LUMO gap is strictly positive. Zero values in the audit were
    # produced by a failed meV-to-eV conversion and are never valid results.
    return not (is_qm9_dataset(dataset_name) and metric_name.casefold() == "gap" and value <= 0)


# ── Value parsing ─────────────────────────────────────────────────────────────

_NUMBER_RE = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
_PAREN_STD_RE = re.compile(rf"({_NUMBER_RE})\s*\(\s*({_NUMBER_RE})\s*\)")
_PM_AFTER_RE = re.compile(rf"({_NUMBER_RE})\s*±\s*({_NUMBER_RE})")
_PLAIN_NUMBER_RE = re.compile(rf"^\s*({_NUMBER_RE})\s*$")


def parse_value_std(raw: Any) -> tuple[float | None, float | None]:
    """Parse a raw value into (value, std). Returns (None, None) on failure."""
    if raw is None:
        return None, None
    if isinstance(raw, (int, float)):
        return float(raw), None
    s = str(raw).strip()

    # "0.653 ± 0.004" or "0.653±0.004"
    m = _PM_AFTER_RE.search(s)
    if m:
        return float(m.group(1)), float(m.group(2))

    # "0.653 (0.004)"
    m = _PAREN_STD_RE.match(s)
    if m:
        return float(m.group(1)), float(m.group(2))

    # plain number
    clean = s.replace(",", "")
    if clean.endswith("%"):
        clean = clean[:-1].strip()
    m = _PLAIN_NUMBER_RE.match(clean)
    if m:
        return float(m.group(1)), None
    return None, None


# ── Dataset variant resolution ────────────────────────────────────────────────


def _load_variant_map(session) -> dict[str, int]:
    """Build {name.lower() → variant_id} for all variants + their dataset names."""
    mapping: dict[str, int] = {}
    zinc_variants: dict[str, int] = {}
    for v in session.query(DatasetVariant).all():
        mapping[v.name.lower()] = v.id
        dataset_key = v.dataset.name.lower()
        # A bare dataset name means the canonical/default benchmark.  Do not
        # let a later non-standard variant (e.g. Cora's random 10-fold split)
        # silently replace the standard variant in this lookup.
        if dataset_key not in mapping or v.is_standard:
            mapping[dataset_key] = v.id
        if dataset_key == "zinc":
            variant_key = v.name.lower()
            zinc_variants[variant_key] = v.id
            mapping[f"zinc {variant_key}"] = v.id

    zinc_subset_id = zinc_variants.get("subset (12k)")
    zinc_full_id = zinc_variants.get("full")
    if zinc_subset_id is not None:
        for alias in _ZINC_SUBSET_ALIASES:
            mapping[alias] = zinc_subset_id
    if zinc_full_id is not None:
        for alias in _ZINC_FULL_ALIASES:
            mapping[alias] = zinc_full_id
    if zinc_subset_id is not None:
        mapping["zinc"] = zinc_subset_id
    elif zinc_full_id is not None:
        mapping["zinc"] = zinc_full_id
    for alias, canonical in _OGB_DATASET_ALIASES.items():
        target = mapping.get(canonical)
        if target is not None:
            mapping[alias] = target
    return mapping


def _zinc_variant_id(kind: str, variant_map: dict[str, int]) -> int | None:
    if kind == "subset":
        return variant_map.get("zinc subset") or variant_map.get("subset (12k)")
    if kind == "full":
        return variant_map.get("zinc full") or variant_map.get("full")
    return None


def _collect_zinc_context(entry: dict[str, Any]) -> str:
    parts = [
        str(entry.get("dataset") or ""),
        str(entry.get("table_ref") or ""),
        str(entry.get("source_ref") or ""),
        str(entry.get("notes") or ""),
    ]
    return " ".join(part for part in parts if part).strip().lower()


def _extract_numeric_value(raw: Any) -> float | None:
    value, _std = parse_value_std(raw)
    return value


def _infer_zinc_variant(
    entry: dict[str, Any],
    variant_map: dict[str, int],
    paper_text: str | None = None,
) -> tuple[int | None, str]:
    context = _collect_zinc_context(entry)

    if _ZINC_FULL_CUE_RE.search(context):
        return _zinc_variant_id("full", variant_map), "zinc: entry cue matched full"
    if _ZINC_SUBSET_CUE_RE.search(context):
        return _zinc_variant_id("subset", variant_map), "zinc: entry cue matched subset"

    paper_text_lower = (paper_text or "").lower()
    if paper_text_lower:
        has_subset_cue = _ZINC_SUBSET_CUE_RE.search(paper_text_lower) is not None
        has_full_cue = _ZINC_FULL_CUE_RE.search(paper_text_lower) is not None
        if has_subset_cue and not has_full_cue:
            return _zinc_variant_id("subset", variant_map), "zinc: paper text matched subset"
        if has_full_cue and not has_subset_cue:
            return _zinc_variant_id("full", variant_map), "zinc: paper text matched full"

    metric_key = str(entry.get("metric") or "").strip().lower()
    if metric_key == "mae":
        value = _extract_numeric_value(entry.get("value"))
        if value is not None:
            if value <= _ZINC_FULL_MAX_MAE:
                return (
                    _zinc_variant_id("full", variant_map),
                    f"zinc: mae fallback <= {_ZINC_FULL_MAX_MAE:.2f}",
                )
            if value >= _ZINC_SUBSET_MIN_MAE:
                return (
                    _zinc_variant_id("subset", variant_map),
                    f"zinc: mae fallback >= {_ZINC_SUBSET_MIN_MAE:.2f}",
                )

    return _zinc_variant_id("subset", variant_map), "zinc: default subset fallback"


def resolve_dataset_variant_with_reason(
    dataset_name: str,
    session,
    variant_map: dict[str, int] | None = None,
    entry: dict[str, Any] | None = None,
    paper_text: str | None = None,
    arxiv_id: str | None = None,
) -> tuple[int | None, str]:
    if variant_map is None:
        variant_map = _load_variant_map(session)

    raw_key = str(dataset_name or "").strip().casefold()
    if raw_key in {"arxiv", "arxiv dataset"}:
        logger.warning("Ambiguous dataset label '%s' is not treated as ogbn-arxiv", dataset_name)
        return None, "dataset: ambiguous arXiv label"

    dataset_name = normalize_dataset_alias(dataset_name, arxiv_id=arxiv_id)
    key = dataset_name.strip().lower()

    if key == "zinc":
        return _infer_zinc_variant(entry or {"dataset": dataset_name}, variant_map, paper_text)

    if key == "pcqm4mv2":
        context = " ".join(
            str((entry or {}).get(field) or "")
            for field in ("table_ref", "source_ref", "protocol_note", "notes")
        ).casefold()
        if re.search(r"test[- ]challenge|challenge\s+(?:split|set)|competition", context):
            challenge_id = variant_map.get("test challenge")
            if challenge_id is not None:
                return challenge_id, "PCQM4Mv2: test-challenge cue"

    if key in variant_map:
        return variant_map[key], "dataset: exact match"

    if is_ambiguous_dataset_name(dataset_name):
        logger.warning("Ambiguous dataset label '%s' is not fuzzy-matched", dataset_name)
        return None, "dataset: ambiguous generic name"

    alias_target = _OGB_DATASET_ALIASES.get(key)
    if alias_target is not None and alias_target in variant_map:
        return variant_map[alias_target], f"dataset: alias to {alias_target}"

    if variant_map:
        min_score = 85 if len(key) <= 6 else 75
        best_match, score = fuzz_process.extractOne(
            key,
            list(variant_map.keys()),
            scorer=fuzz_lib.token_sort_ratio,
        )
        raw_qualifiers = set(_DATASET_VARIANT_QUALIFIER_RE.findall(key.casefold()))
        match_qualifiers = set(_DATASET_VARIANT_QUALIFIER_RE.findall(best_match.casefold()))
        conflicting_qualifier = raw_qualifiers - match_qualifiers
        if (
            score >= min_score
            and not conflicting_qualifier
            and ogb_dataset_families_compatible(key, best_match)
        ):
            logger.debug(
                "Fuzzy-matched dataset '%s' → '%s' (score=%d)", dataset_name, best_match, score
            )
            return variant_map[best_match], f"dataset: fuzzy match to {best_match} (score={score})"

    logger.warning("Could not resolve dataset variant '%s'", dataset_name)
    return None, "dataset: unresolved"


def resolve_dataset_variant(
    dataset_name: str,
    session,
    variant_map: dict[str, int] | None = None,
    entry: dict[str, Any] | None = None,
    paper_text: str | None = None,
    arxiv_id: str | None = None,
) -> int | None:
    """Return the DatasetVariant.id best matching dataset_name.

    Falls back to thefuzz similarity (threshold 75%) if exact match fails.
    Returns None if no match found.
    """
    variant_id, _reason = resolve_dataset_variant_with_reason(
        dataset_name,
        session,
        variant_map,
        entry=entry,
        paper_text=paper_text,
        arxiv_id=arxiv_id,
    )
    return variant_id


# ── Model resolution ──────────────────────────────────────────────────────────


def _load_model_map(session) -> tuple[dict[str, int], dict[str, int]]:
    """Returns (canonical_map, alias_map) both keyed on lowercased name → model_id."""
    canonical: dict[str, int] = {}
    aliases: dict[str, int] = {}
    for m in session.query(Model).all():
        canonical[m.canonical_name.lower()] = m.id
    for a in session.query(ModelAlias).all():
        aliases[a.alias.lower()] = a.model_id
    return canonical, aliases


def _update_model_metadata(model: Model, model_type: str | None) -> None:
    normalized_type = normalize_architecture_type(model_type)
    if normalized_type and not model.model_type:
        model.model_type = normalized_type


def _register_model_alias(
    session,
    alias_map: dict[str, int],
    model_id: int,
    alias: str,
) -> None:
    alias_clean = re.sub(r"\s+", " ", alias).strip()
    alias_key = alias_clean.lower()
    if not alias_key or alias_key in alias_map:
        return
    existing = session.query(ModelAlias).filter_by(alias=alias_clean).first()
    if existing is not None:
        alias_map[alias_key] = existing.model_id
        return
    session.add(ModelAlias(model_id=model_id, alias=alias_clean))
    session.flush()
    alias_map[alias_key] = model_id


def resolve_or_create_model(
    model_name: str,
    is_proposed: bool,
    model_type: str | None,
    session,
    canonical_map: dict[str, int],
    alias_map: dict[str, int],
) -> tuple[int, bool]:
    """Find or create a Model record. Returns ``(model_id, created_new)``."""
    raw_name = ROLE_SUFFIX_RE.sub("", model_name).strip()
    normalized = normalize_model_name_for_resolution(raw_name)
    key = normalized.lower()

    if key in canonical_map:
        model = session.query(Model).filter_by(id=canonical_map[key]).first()
        if model is not None:
            _update_model_metadata(model, model_type)
        if raw_name.lower() != key:
            _register_model_alias(session, alias_map, canonical_map[key], raw_name)
        return canonical_map[key], False
    if key in alias_map:
        model = session.query(Model).filter_by(id=alias_map[key]).first()
        if model is not None:
            _update_model_metadata(model, model_type)
        return alias_map[key], False

    # thefuzz against canonical names — use token_sort_ratio to avoid
    # partial-substring false positives (e.g. "GCN" ⊂ "GatedGCN" scores 90
    # with the default WRatio scorer because partial_ratio=100).
    all_names = list(canonical_map.keys()) + list(alias_map.keys())
    if all_names:
        best_match, score = fuzz_process.extractOne(
            key, all_names, scorer=fuzz_lib.token_sort_ratio
        )
        if model_names_fuzzy_compatible(
            normalized, best_match, score, _MODEL_FUZZY_MATCH_MIN_SCORE
        ):
            logger.debug(
                "Fuzzy-matched model '%s' → '%s' (score=%d)", normalized, best_match, score
            )
            match_id = canonical_map.get(best_match) or alias_map.get(best_match)
            if match_id:
                model = session.query(Model).filter_by(id=match_id).first()
                if model is not None:
                    _update_model_metadata(model, model_type)
                if raw_name.lower() != best_match:
                    _register_model_alias(session, alias_map, match_id, raw_name)
                return match_id, False

    # Create new model
    new_model = Model(
        name=normalized,
        canonical_name=normalized,
    )
    _update_model_metadata(new_model, model_type)
    session.add(new_model)
    session.flush()  # get the new id
    canonical_map[key] = new_model.id
    if raw_name.lower() != key:
        _register_model_alias(session, alias_map, new_model.id, raw_name)
    logger.info("Created new model: '%s' (id=%d)", normalized, new_model.id)
    return new_model.id, True


# ── Metadata enrichment ───────────────────────────────────────────────────────

# GitHub URLs to skip — known ML/graph libraries, not project repos
_GH_SKIP = re.compile(
    r"github\.com/(pytorch|pyg-team|dmlc|rusty1s|facebookresearch|google|"
    r"microsoft|openai|shelhamer|snap-stanford|benedekrozemberczki|"
    r"diningphil|asappresearch)/"
)


def _extract_github_url(text: str) -> str | None:
    """Return the first project-specific GitHub URL found in text, or None."""
    urls = re.findall(r"https?://github\.com/([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)", text)
    for path in urls:
        if not _GH_SKIP.search("github.com/" + path):
            return "https://github.com/" + path.rstrip("/.")
    return None


def _apply_remote_metadata(paper: Paper, meta: dict[str, str]) -> bool:
    """Apply title/abstract/date/venue from a metadata dict. Returns True if abstract changed."""
    abstract_changed = False
    if meta.get("title"):
        paper.title = meta["title"]
    if meta.get("abstract"):
        paper.abstract = meta["abstract"]
        abstract_changed = True
    if meta.get("published_date") and not paper.published_date:
        paper.published_date = meta["published_date"]
    if meta.get("venue") and venue_needs_resolution(paper.venue):
        paper.venue = resolve_canonical_venue(meta["venue"]) or meta["venue"]
    return abstract_changed


def _enrich_paper_metadata(arxiv_id: str, paper: Paper, storage: PaperStorage) -> bool:
    """Update Paper record from local caches, Semantic Scholar, then arXiv API if needed."""
    abstract_has_artifacts = abstract_has_latex_artifacts(paper.abstract)
    paper.abstract = clean_extracted_text(paper.abstract)
    before = (
        paper.title,
        paper.abstract,
        paper.published_date,
        json.dumps(paper.authors, ensure_ascii=False),
        paper.venue,
        paper.codebase_url,
    )
    metadata = storage.read_metadata()
    if paper.codebase_url and repository_url_exists(paper.codebase_url) is False:
        stale_url = paper.codebase_url
        paper.codebase_url = None
        storage.update_metadata({"codebase_url": ""})
        logger.warning("Discarded unavailable codebase_url=%s for arXiv:%s", stale_url, arxiv_id)

    def _usable_repository_url(value: Any) -> str:
        url = str(value or "").strip()
        return url if url and repository_url_exists(url) is not False else ""

    if metadata:
        if metadata.get("title"):
            paper.title = metadata["title"]
        if metadata.get("abstract"):
            raw_abstract = metadata["abstract"]
            abstract_has_artifacts = abstract_has_artifacts or abstract_has_latex_artifacts(
                raw_abstract
            )
            paper.abstract = clean_extracted_text(raw_abstract)
        if metadata.get("published_date") and not paper.published_date:
            paper.published_date = metadata["published_date"]
        if metadata.get("authors") and not paper.authors:
            from backend.models import author_display_name, normalize_author_entry

            normalized_authors = [
                normalize_author_entry(entry)
                for entry in metadata["authors"]
                if author_display_name(entry)
            ]
            if normalized_authors and not authors_look_broken(normalized_authors):
                paper.authors = normalized_authors
        if metadata.get("venue") and venue_needs_resolution(paper.venue):
            paper.venue = resolve_canonical_venue(metadata["venue"]) or metadata["venue"]
        if metadata.get("codebase_url") and not paper.codebase_url:
            paper.codebase_url = _usable_repository_url(metadata["codebase_url"])
        repo_meta = metadata.get("repository")
        if isinstance(repo_meta, dict) and repo_meta.get("verified_url") and not paper.codebase_url:
            paper.codebase_url = _usable_repository_url(repo_meta["verified_url"])

    if not paper.codebase_url and storage.llm_output_path.exists():
        try:
            raw_output = storage.load_llm_output()
            repository = raw_output.get("repository")
            if isinstance(repository, dict) and repository.get("verified_url"):
                paper.codebase_url = _usable_repository_url(repository["verified_url"])
        except (ValueError, OSError):
            pass

    from backend.llm_metadata import _title_looks_corrupted

    need_meta = not paper.abstract or abstract_has_artifacts or _title_looks_corrupted(paper.title)

    if need_meta:
        # 1. Try local HTML — free, no rate limit
        if storage.html_index_path.exists():
            try:
                from backend.html_parser import parse_html_paper

                parsed = parse_html_paper(storage.html_index_path)
                if parsed.title and not _title_looks_corrupted(parsed.title):
                    paper.title = parsed.title
                if parsed.abstract:
                    paper.abstract = parsed.abstract
                    abstract_has_artifacts = abstract_has_latex_artifacts(parsed.abstract)
                need_meta = (
                    not paper.abstract
                    or abstract_has_artifacts
                    or _title_looks_corrupted(paper.title)
                )
            except Exception:
                pass

        # 2. Try cached LaTeX (expanded.tex)
        if need_meta and storage.latex_dir.exists():
            try:
                from backend.llm_metadata import _extract_metadata_from_latex_cache

                latex_meta = _extract_metadata_from_latex_cache(storage.latex_dir)
                if latex_meta.get("title"):
                    paper.title = latex_meta["title"]
                if latex_meta.get("abstract"):
                    paper.abstract = latex_meta["abstract"]
                    abstract_has_artifacts = abstract_has_latex_artifacts(latex_meta["abstract"])
                need_meta = (
                    not paper.abstract
                    or abstract_has_artifacts
                    or _title_looks_corrupted(paper.title)
                )
            except Exception:
                pass

    need_daily_date = not paper.published_date or len(paper.published_date) < 10
    need_venue = venue_needs_resolution(paper.venue)
    if need_meta or need_daily_date or need_venue:
        from backend.semantic_scholar import fetch_paper_metadata, resolve_paper_venue

        ss_meta = fetch_paper_metadata(arxiv_id) or {}
        if ss_meta:
            selective_meta = {
                key: value
                for key, value in ss_meta.items()
                if (
                    (key in {"title", "abstract"} and need_meta)
                    or (key == "published_date" and need_daily_date)
                )
            }
            if selective_meta and _apply_remote_metadata(paper, selective_meta):
                abstract_has_artifacts = abstract_has_latex_artifacts(paper.abstract)
            need_meta = (
                not paper.abstract or abstract_has_artifacts or _title_looks_corrupted(paper.title)
            )
            need_daily_date = not paper.published_date or len(paper.published_date) < 10
        if need_venue:
            resolved_venue = resolve_paper_venue(arxiv_id, ss_meta)
            if resolved_venue:
                paper.venue = resolved_venue
            storage.update_metadata(
                {
                    **({"published_date": paper.published_date} if paper.published_date else {}),
                    **({"venue": paper.venue} if paper.venue else {}),
                }
            )

        # arXiv Atom API when date/abstract still missing after Semantic Scholar.
        if (need_meta or need_daily_date) and (not cfg.semantic_scholar_api_key or need_daily_date):
            from backend.llm_metadata import fetch_arxiv_metadata

            meta = fetch_arxiv_metadata(arxiv_id)
            if meta:
                selective_meta = {
                    key: value
                    for key, value in meta.items()
                    if (
                        (key in {"title", "abstract"} and need_meta)
                        or (key == "published_date" and need_daily_date)
                    )
                }
                if selective_meta and _apply_remote_metadata(paper, selective_meta):
                    abstract_has_artifacts = abstract_has_latex_artifacts(paper.abstract)
                need_meta = (
                    not paper.abstract
                    or abstract_has_artifacts
                    or _title_looks_corrupted(paper.title)
                )
                need_daily_date = not paper.published_date or len(paper.published_date) < 10
                storage.update_metadata(
                    {
                        **(
                            {"published_date": paper.published_date} if paper.published_date else {}
                        ),
                    }
                )

    # Fallback: derive date from arXiv ID (e.g. 2206.08164 → 2022-06)
    if not paper.published_date:
        m = re.match(r"^(\d{2})(\d{2})\.\d+", arxiv_id)
        if m:
            year, month = int(m.group(1)) + 2000, int(m.group(2))
            if 1 <= month <= 12:
                paper.published_date = f"{year}-{month:02d}"

    # Extract GitHub codebase URL from paper text if not already set
    if not paper.codebase_url:
        repo_source_text, repo_source_kind = repository_source_from_storage(storage)
        if repo_source_text:
            try:
                from backend.llm_tasks import LLMExtractor

                verifier = (
                    LLMExtractor(model_tier="small")
                    if cfg.llm_endpoint and cfg.llm_api_key
                    else None
                )
                repository = find_verified_repository_link(
                    llm_verifier=verifier,
                    arxiv_id=arxiv_id,
                    paper_title=paper.title or "",
                    paper_abstract=paper.abstract or "",
                    source_text=repo_source_text,
                    source_kind=repo_source_kind,
                )
                if repository.get("verified_url"):
                    paper.codebase_url = str(repository["verified_url"]).strip()
                    storage.update_metadata(
                        {
                            "codebase_url": paper.codebase_url,
                            "repository": repository,
                        }
                    )
                    logger.info(
                        "Set verified codebase_url=%s for arXiv:%s", paper.codebase_url, arxiv_id
                    )
            except Exception as exc:
                logger.warning("Verified repo extraction failed for arXiv:%s: %s", arxiv_id, exc)

    if not paper.codebase_url and storage.text_path.exists():
        text = storage.text_path.read_text(encoding="utf-8", errors="ignore")
        url = _extract_github_url(text)
        if url:
            paper.codebase_url = url
            logger.info("Set heuristic codebase_url=%s for arXiv:%s", url, arxiv_id)

    if not paper.authors or authors_look_broken(paper.authors):
        try:
            from backend.semantic_scholar import resolve_paper_authors

            latex_names: list[str] | None = None
            if storage.latex_dir.exists():
                from backend.llm_metadata import _extract_metadata_from_latex_cache

                latex_meta = _extract_metadata_from_latex_cache(storage.latex_dir)
                raw_names = latex_meta.get("authors")
                if isinstance(raw_names, list) and raw_names:
                    latex_names = [str(name) for name in raw_names if str(name).strip()]

            resolved_authors = resolve_paper_authors(arxiv_id, latex_names=latex_names)
            if resolved_authors and not authors_look_broken(resolved_authors):
                paper.authors = resolved_authors
                storage.update_metadata({"authors": paper.authors})
        except Exception as exc:
            logger.debug("Author extraction failed for arXiv:%s: %s", arxiv_id, exc)

    after = (
        paper.title,
        paper.abstract,
        paper.published_date,
        json.dumps(paper.authors, ensure_ascii=False),
        paper.venue,
        paper.codebase_url,
    )
    return before != after


# Extraction call types whose parse failures should not block DB ingest.
_NON_FATAL_EXTRACT_CALL_PREFIXES: tuple[str, ...] = ("extract_dataset_statistics",)

_SUSPICIOUS_EXTRACTION_NOTE_RE = re.compile(
    r"\b(?:truncated|synthesi[sz]ed|fabricated|representative\s+values?|"
    r"partial\s+(?:table|results?)|incomplete\s+(?:table|results?)(?!\s+row))\b",
    re.IGNORECASE,
)


def _is_fatal_extraction_parse_failure(entry: str) -> bool:
    call_type = entry.split(":", 1)[0].strip()
    if not call_type.startswith("extract_"):
        return False
    return not any(
        call_type == prefix or call_type.startswith(f"{prefix}:")
        for prefix in _NON_FATAL_EXTRACT_CALL_PREFIXES
    )


def _extraction_quality_issues(
    extraction: dict[str, Any], fatal_parse_failures: list[str]
) -> list[str]:
    """Return reasons why an extraction is unsafe to merge into the database."""
    issues = list(fatal_parse_failures)
    coverage = str(extraction.get("coverage_assessment") or "").casefold()
    if coverage in {"partial", "incomplete"}:
        issues.append(f"coverage_assessment={coverage}")
    notes = str(extraction.get("extraction_notes") or "").strip()
    if _SUSPICIOUS_EXTRACTION_NOTE_RE.search(notes):
        issues.append(f"extraction_notes contain incomplete/synthetic wording: {notes}")
    return issues


def parse_and_store_with_summary(
    arxiv_id: str, *, replace_existing: bool = False, allow_quality_issues: bool = False
) -> ParseStoreSummary:
    """Parse LLM output for a paper and report the side effects explicitly."""
    init_db()
    storage = PaperStorage(arxiv_id)
    summary = ParseStoreSummary(arxiv_id=arxiv_id)

    # Curation exclusions are authoritative. Clear any legacy rows before
    # checking the extraction artifact so a normal reparse cannot leave a
    # previously exported paper result set behind.
    if _curation_excludes_all_results(arxiv_id):
        with session_scope() as session:
            paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
            if paper is not None:
                deleted = (
                    session.query(Result)
                    .filter_by(paper_id=paper.id)
                    .delete(synchronize_session=False)
                )
                summary.replaced_results = deleted
                if deleted:
                    logger.info(
                        "Deleted %d curated-exclusion result row(s) for arXiv:%s",
                        deleted,
                        arxiv_id,
                    )
        summary.skipped_protocol_mismatches.append(
            f"all results excluded by protocol curation: {arxiv_id}"
        )
        return summary

    if not storage.llm_output_path.exists():
        logger.error("No LLM output found for arXiv:%s — run extractor first", arxiv_id)
        return summary

    raw = storage.load_llm_output()
    extraction = raw.get("results", {})
    model_name_used = raw.get("model_used", "unknown")
    summary.extraction_model = model_name_used

    # Discovery is an independent audit artifact. Persist unresolved dataset
    # observations even when the result payload is empty or later quarantined.
    from backend.pending_datasets import collect_pending_datasets

    collect_pending_datasets(arxiv_id, raw)

    call_log = storage.load_llm_calls()
    parse_failures: list[str] = []
    for call in call_log:
        if not isinstance(call, dict):
            continue
        call_type = str(call.get("call_type") or "")
        parse_error = str(call.get("parse_error") or "").strip()
        if parse_error and (
            call_type.startswith("extract_") or call_type.startswith("extract_dataset")
        ):
            parse_failures.append(f"{call_type}: {parse_error}")

    paper_text = ""
    if storage.text_path.exists():
        paper_text = storage.text_path.read_text(encoding="utf-8", errors="ignore")
    elif (storage.latex_dir / "expanded.tex").exists():
        paper_text = (storage.latex_dir / "expanded.tex").read_text(
            encoding="utf-8", errors="ignore"
        )

    result_entries: list[dict] = (
        extraction.get("results", []) if isinstance(extraction, dict) else []
    )
    qm9_source_text = paper_text
    expanded_source_path = storage.latex_dir / "expanded.tex"
    if expanded_source_path.exists():
        qm9_source_text += "\n" + expanded_source_path.read_text(encoding="utf-8", errors="ignore")

    guarded_entries: list[dict] = []
    molecular_guard_dropped = False
    for entry in result_entries:
        if isinstance(entry, dict):
            _apply_feature_source_model_name(entry)
            if is_qm9_dataset(str(entry.get("dataset") or "")):
                entry = normalize_qm9_result_mapping(entry, qm9_source_text)
                if entry is None:
                    molecular_guard_dropped = True
                    continue
            elif is_qm7b_dataset(str(entry.get("dataset") or "")):
                entry = normalize_qm7b_result_mapping(entry, qm9_source_text)
                if entry is None:
                    molecular_guard_dropped = True
                    continue
            elif is_physical_unit_dataset(str(entry.get("dataset") or "")):
                entry = normalize_physical_result_mapping(entry, qm9_source_text)
                if entry is None:
                    molecular_guard_dropped = True
                    continue
        guarded_entries.append(entry)
    result_entries = guarded_entries
    # Apply the same light LaTeX cleanup used during extraction.  This also
    # handles responses that omit the backslash in ``extsubscript{...}``.
    for entry in result_entries:
        if isinstance(entry, dict) and entry.get("model") is not None:
            entry["model"] = _normalise_model_name_text(str(entry["model"]))
    fatal_parse_failures = [f for f in parse_failures if _is_fatal_extraction_parse_failure(f)]
    quality_issues = _extraction_quality_issues(extraction, fatal_parse_failures)

    if quality_issues and not allow_quality_issues:
        with session_scope() as session:
            paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
            if paper is None:
                paper = Paper(
                    arxiv_id=arxiv_id,
                    title=f"arXiv:{arxiv_id}",
                    extraction_status="downloaded",
                    discovery_source="manual",
                )
                session.add(paper)
                session.flush()
                summary.created_stub_paper = True

            paper.extraction_model = model_name_used
            paper.extraction_status = "quarantined_extraction_quality"

        summary.quarantined = True
        summary.quarantine_reasons = quality_issues[:5]
        logger.warning(
            "Quarantining arXiv:%s due to extraction-quality issue(s): %s",
            arxiv_id,
            "; ".join(quality_issues[:2]),
        )
        return summary
    if quality_issues:
        logger.warning(
            "Accepting arXiv:%s despite extraction-quality issue(s) by explicit override: %s",
            arxiv_id,
            "; ".join(quality_issues[:2]),
        )

    if not result_entries:
        if replace_existing and molecular_guard_dropped:
            with session_scope() as session:
                paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
                if paper is not None:
                    deleted = (
                        session.query(Result)
                        .filter_by(paper_id=paper.id, is_overridden=0)
                        .delete(synchronize_session=False)
                    )
                    summary.replaced_results = deleted
                    paper.extraction_model = model_name_used
                    paper.extraction_status = "extracted"
                    if deleted:
                        logger.info(
                            "Deleted %d rejected QM9 result row(s) for arXiv:%s",
                            deleted,
                            arxiv_id,
                        )
            return summary
        logger.warning(
            "No result entries in LLM output for arXiv:%s; existing rows were retained",
            arxiv_id,
        )
        return summary

    # Build a sizes lookup from baseline info
    sizes_lookup, type_lookup = _build_metadata_lookups(
        extraction,
        model_sizes=raw.get("model_sizes"),
    )
    dataset_param_lookup = _build_dataset_param_lookup(raw.get("model_sizes"))
    metadata_defaults = load_model_metadata_defaults()

    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            logger.warning("Paper arXiv:%s not in DB — creating stub", arxiv_id)
            paper = Paper(
                arxiv_id=arxiv_id,
                title=f"arXiv:{arxiv_id}",
                extraction_status="downloaded",
                discovery_source="manual",
            )
            session.add(paper)
            session.flush()
            summary.created_stub_paper = True

        paper.extraction_model = model_name_used

        summary.metadata_changed = _enrich_paper_metadata(arxiv_id, paper, storage)

        overrides: dict[str, Any] = {}
        if storage.overrides_path.exists():
            try:
                import yaml

                overrides = yaml.safe_load(storage.overrides_path.read_text(encoding="utf-8")) or {}
            except (yaml.YAMLError, OSError) as exc:
                logger.error("Failed to load overrides for %s: %s", arxiv_id, exc)
                overrides = {}

        finding = audit_extraction_payload(
            arxiv_id=arxiv_id,
            title=paper.title or f"arXiv:{arxiv_id}",
            results_payload=extraction,
            overrides=overrides,
        )
        if finding is not None:
            paper.extraction_status = "quarantined_method_name"
            summary.quarantined = True
            summary.quarantine_reasons = list(finding.reasons)
            summary.quarantine_model_names = [
                name for name in [finding.proposed_name, *finding.suspicious_result_names] if name
            ]
            logger.warning(
                "Quarantining arXiv:%s due to suspicious method names: %s",
                arxiv_id,
                "; ".join(finding.reasons),
            )
            return summary

        previous_results = (
            session.query(Result).filter_by(paper_id=paper.id).all() if replace_existing else []
        )
        previous_result_ids = {result.id for result in previous_results}
        retained_existing_ids: set[int] = {
            result.id for result in previous_results if result.is_overridden
        }
        pending_updates: list[tuple[Result, dict[str, Any], float | None, bool, str, str]] = []
        pending_new_by_key: dict[tuple[int, int, str], Result] = {}

        paper.extraction_status = "extracted"

        variant_map = _load_variant_map(session)
        canonical_map, alias_map = _load_model_map(session)

        discovered_infos: list[DatasetInfo] = []
        for value in extraction.get("discovered_datasets") or []:
            try:
                discovered_infos.append(DatasetInfo.model_validate(value))
            except (TypeError, ValueError):
                continue
        allowed_discovered_variant_ids: set[int] | None = None
        if discovered_infos:
            from backend.dataset_discovery import classify_dataset_infos

            resolutions = classify_dataset_infos(session, discovered_infos, arxiv_id=arxiv_id)
            allowed_discovered_variant_ids = {
                resolution.variant.id for resolution in resolutions if resolution.tracked
            }

        for entry in result_entries:
            dataset_name = normalize_dataset_alias(entry.get("dataset", ""), arxiv_id=arxiv_id)
            # Code2 predicts method-name sub-tokens on whole AST graphs. Some
            # older extraction outputs called this node classification, which
            # incorrectly caused otherwise valid F1 rows to be rejected.
            if (
                dataset_name.strip().casefold() == "ogbg-code2"
                and _normalized_evaluation_task(entry.get("evaluation_task"))
                == "node_classification"
            ):
                entry = dict(entry)
                entry["evaluation_task"] = "graph_classification"
            model_name = entry.get("model", "")
            metric_name = entry.get("metric", "")
            result_override = get_result_override(overrides, model_name, dataset_name, metric_name)
            corrected_metric = str((result_override or {}).get("correct_metric") or "").strip()
            if corrected_metric:
                metric_name = corrected_metric
            if is_qm9_dataset(dataset_name):
                normalized_target = normalize_qm9_metric(metric_name)
                if normalized_target is None:
                    logger.warning(
                        "Skipping QM9 result with unknown target metric %r for arXiv:%s model=%s",
                        metric_name,
                        arxiv_id,
                        model_name,
                    )
                    summary.skipped_invalid_values.append(
                        f"{model_name} / {dataset_name} / {metric_name} (unknown QM9 target)"
                    )
                    continue
                metric_name = normalized_target

            variant_id, variant_reason = resolve_dataset_variant_with_reason(
                dataset_name,
                session,
                variant_map,
                entry=entry,
                paper_text=paper_text,
                arxiv_id=arxiv_id,
            )
            if (
                allowed_discovered_variant_ids is not None
                and variant_id not in allowed_discovered_variant_ids
            ):
                logger.warning(
                    "Skipping result for dataset outside the tracked discovery manifest: %s",
                    dataset_name,
                )
                if dataset_name and dataset_name not in summary.skipped_unknown_datasets:
                    summary.skipped_unknown_datasets.append(dataset_name)
                continue
            if variant_id is None:
                logger.warning(
                    "Skipping result (unknown dataset '%s') for arXiv:%s",
                    dataset_name,
                    arxiv_id,
                )
                if dataset_name and dataset_name not in summary.skipped_unknown_datasets:
                    summary.skipped_unknown_datasets.append(dataset_name)
                continue
            variant = session.get(DatasetVariant, variant_id)
            canonical_task = (
                _normalized_evaluation_task(variant.dataset.task_type) if variant else ""
            )
            observed_task = _normalized_evaluation_task(entry.get("evaluation_task"))
            if canonical_task not in SUPPORTED_TASK_TYPES or (
                observed_task and observed_task not in SUPPORTED_TASK_TYPES
            ):
                detail = (
                    f"{model_name} / {dataset_name} / {metric_name} "
                    f"(unsupported task: {observed_task or canonical_task or 'missing'})"
                )
                logger.warning(
                    "Skipping unsupported-task result for arXiv:%s: %s", arxiv_id, detail
                )
                summary.skipped_protocol_mismatches.append(detail)
                continue
            if variant is None or not _allowed_by_protocol_curation(
                arxiv_id, variant, model_name=model_name, metric_name=metric_name
            ):
                detail = f"{model_name} / {dataset_name} / {metric_name} (curation exclusion)"
                logger.warning(
                    "Skipping protocol-excluded result for arXiv:%s: %s", arxiv_id, detail
                )
                summary.skipped_protocol_mismatches.append(detail)
                continue
            manual_note = _manual_protocol_note(arxiv_id, variant.dataset.name)
            if manual_note:
                entry = dict(entry)
                entry["protocol_note"] = manual_note
            decision = _protocol_decision(entry, variant)
            if not _protocol_result_is_eligible(decision, variant):
                expected_task = _normalized_evaluation_task(variant.dataset.task_type)
                actual_task = _normalized_evaluation_task(entry.get("evaluation_task"))
                detail = (
                    f"{model_name} / {dataset_name} / {metric_name} "
                    f"(decision={decision}; expected {expected_task}; "
                    f"got {actual_task or 'unknown'}; "
                    f"note={entry.get('protocol_note') or 'none'})"
                )
                logger.warning(
                    "Skipping protocol-ineligible result for arXiv:%s: %s",
                    arxiv_id,
                    detail,
                )
                summary.skipped_protocol_mismatches.append(detail)
                continue
            if decision == "uncertain":
                summary.uncertain_protocol_results.append(
                    f"{model_name} / {dataset_name} / {metric_name}"
                )
            value, std = _parse_entry_value(entry)
            if value is None or not _dataset_metric_value_is_valid(
                dataset_name, metric_name, value
            ):
                logger.warning(
                    "Could not parse valid value for %s / %s / %s — skipping",
                    model_name,
                    dataset_name,
                    metric_name,
                )
                summary.skipped_invalid_values.append(
                    f"{model_name} / {dataset_name} / {metric_name}"
                )
                continue
            num_runs, trained_by_paper, num_runs_evidence = _validated_run_metadata(entry)
            if dataset_name.strip().lower() == "zinc":
                logger.info(
                    "Resolved ZINC variant for arXiv:%s model=%s metric=%s via %s",
                    arxiv_id,
                    model_name,
                    metric_name,
                    variant_reason,
                )

            model_key = model_name.strip().lower()
            params = dataset_param_lookup.get((dataset_name.strip().casefold(), model_key))
            params_present = params is not None
            if not params_present:
                params = sizes_lookup.get(model_key)
                params_present = model_key in sizes_lookup
            model_type = lookup_model_type(
                model_name,
                type_lookup,
                defaults=metadata_defaults,
            )
            is_proposed = parse_extracted_bool(entry.get("is_proposed"), default=False)
            uses_external_data = parse_optional_extracted_bool(entry.get("uses_external_data"))
            input_feature_source = normalize_input_feature_source(entry.get("input_feature_source"))
            higher_is_better = parse_extracted_bool(
                entry.get("higher_is_better"),
                default=True,
            )

            model_id, created_model = resolve_or_create_model(
                model_name,
                is_proposed=is_proposed,
                model_type=model_type,
                session=session,
                canonical_map=canonical_map,
                alias_map=alias_map,
            )
            if created_model and model_name not in summary.created_models:
                summary.created_models.append(model_name)

            # Check for duplicate (same paper + variant + model + metric)
            existing = (
                session.query(Result)
                .filter_by(
                    paper_id=paper.id,
                    dataset_variant_id=variant_id,
                    model_id=model_id,
                    metric_name=metric_name,
                )
                .first()
            )
            if existing and existing.is_overridden:
                logger.debug(
                    "Skipping overridden result: %s / %s / %s",
                    model_name,
                    dataset_name,
                    metric_name,
                )
                retained_existing_ids.add(existing.id)
                continue
            if existing:
                # Do not mutate an existing row until every candidate entry has
                # passed validation. This keeps a failed/partial replacement
                # from leaving a paper half-updated inside a long parse.
                pending_updates.append(
                    (existing, entry, params, params_present, variant_reason, decision)
                )
                retained_existing_ids.add(existing.id)
                continue

            key = (variant_id, model_id, metric_name)
            result = pending_new_by_key.get(key)
            if result is None:
                result = Result(
                    paper_id=paper.id,
                    dataset_variant_id=variant_id,
                    model_id=model_id,
                    metric_name=metric_name,
                    metric_value=value,
                    metric_std=std,
                    num_runs=num_runs,
                    trained_by_paper=trained_by_paper,
                    num_runs_evidence=num_runs_evidence,
                    higher_is_better=higher_is_better,
                    is_baseline=not is_proposed,
                    uses_external_data=(
                        1
                        if uses_external_data is True
                        else 0
                        if uses_external_data is False
                        else None
                    ),
                    input_feature_source=input_feature_source,
                    feature_source_evidence=entry.get("feature_source_evidence"),
                    params_millions=params,
                    table_ref=entry.get("table_ref"),
                    source_ref=entry.get("source_ref", "this paper"),
                    extraction_model=model_name_used,
                    variant_inference_reason=variant_reason,
                    evaluation_task=entry.get("evaluation_task") or variant.dataset.task_type,
                    protocol_decision=decision,
                    protocol_note=entry.get("protocol_note"),
                )
                pending_new_by_key[key] = result

        # Candidate construction and validation are complete. Only now mutate
        # existing rows. The surrounding session_scope transaction rolls back
        # all changes if replacement or insertion fails below.
        pending_new_results = list(pending_new_by_key.values())

        if previous_results:
            candidate_count = len(retained_existing_ids) + len(pending_new_results)
            summary.candidate_results = candidate_count
            stale_ids = previous_result_ids - retained_existing_ids
            summary.replaced_results = (
                session.query(Result)
                .filter(Result.id.in_(stale_ids), Result.is_overridden == 0)
                .delete(synchronize_session=False)
                if stale_ids
                else 0
            )

        for existing, entry, params, params_present, variant_reason, decision in pending_updates:
            changed = _update_result(
                existing,
                entry,
                model_name_used,
                params_millions=params,
                params_present=params_present,
            )
            existing.variant_inference_reason = variant_reason
            existing.evaluation_task = entry.get("evaluation_task") or variant.dataset.task_type
            existing.protocol_decision = decision
            existing.protocol_note = entry.get("protocol_note")
            if changed:
                summary.updated_results += 1

        for result in pending_new_results:
            session.add(result)
        summary.new_results = len(pending_new_results)
        if not previous_results:
            summary.candidate_results = summary.new_results

        param_lookup = {k: float(v) for k, v in sizes_lookup.items() if v is not None}
        if param_lookup:
            from backend.export_to_hugo import _sanitize_model
            from backend.result_params_backfill import backfill_paper_params_millions

            backfill_paper_params_millions(
                session,
                paper,
                lookup=param_lookup,
                sanitize_model=_sanitize_model,
            )

    logger.info("Stored %d new Result rows for arXiv:%s", summary.new_results, arxiv_id)
    if summary.updated_results:
        logger.info(
            "Updated %d existing Result row(s) for arXiv:%s — usually duplicate model/dataset/metric keys in the extraction output",
            summary.updated_results,
            arxiv_id,
        )

    # Always re-apply overrides after inserting fresh results
    overridden = apply_overrides_to_db(arxiv_id)
    summary.overrides_applied = overridden
    if overridden:
        logger.info("Applied %d overrides for arXiv:%s", overridden, arxiv_id)

    return summary


def parse_and_store(arxiv_id: str) -> int:
    """Parse LLM output for a paper and write Result rows to DB.

    Returns number of new Result rows created.
    """
    return parse_and_store_with_summary(arxiv_id).new_results


def _collect_unknown_datasets(arxiv_id: str) -> int:
    """Compatibility wrapper for the discovery-only pending-dataset collector."""
    storage = PaperStorage(arxiv_id)
    if not storage.llm_output_path.exists():
        return 0
    from backend.pending_datasets import collect_pending_datasets

    return collect_pending_datasets(arxiv_id, storage.load_llm_output())


def _parse_entry_value(entry: dict) -> tuple[float | None, float | None]:
    value = entry.get("value")
    std = entry.get("std")
    if isinstance(value, str):
        value, parsed_std = parse_value_std(value)
        if std is None:
            std = parsed_std
    if std is not None:
        try:
            std = float(std)
        except (TypeError, ValueError):
            std = None
    if value is not None:
        dataset_name = entry.get("dataset", "")
        metric_name = entry.get("metric", "")
        value, std = normalize_percentage_metric(metric_name, float(value), std)
        value, std = normalize_dataset_scaled_metric(dataset_name, metric_name, value, std)
    return value, std


def _update_result(
    result: Result,
    entry: dict,
    model_name_used: str,
    params_millions: float | None = None,
    params_present: bool = False,
) -> bool:
    changed = False
    value, std = _parse_entry_value(entry)
    if value is not None and result.metric_value != value:
        result.metric_value = value
        changed = True
    if value is not None and result.metric_std != std:
        result.metric_std = std
        changed = True
    num_runs, trained_by_paper, num_runs_evidence = _validated_run_metadata(entry)
    for field_name, new_value in (
        ("num_runs", num_runs),
        ("trained_by_paper", trained_by_paper),
        ("num_runs_evidence", num_runs_evidence),
    ):
        if getattr(result, field_name) != new_value:
            setattr(result, field_name, new_value)
            changed = True
    if "uses_external_data" in entry:
        ued = parse_optional_extracted_bool(entry.get("uses_external_data"))
        new_uses_external_data = 1 if ued is True else 0 if ued is False else None
        if result.uses_external_data != new_uses_external_data:
            result.uses_external_data = new_uses_external_data
            changed = True
    if "input_feature_source" in entry:
        new_source = normalize_input_feature_source(entry.get("input_feature_source"))
        if result.input_feature_source != new_source:
            result.input_feature_source = new_source
            changed = True
    if "feature_source_evidence" in entry:
        evidence = entry.get("feature_source_evidence")
        if result.feature_source_evidence != evidence:
            result.feature_source_evidence = evidence
            changed = True
    if params_present and result.params_millions != params_millions:
        changed = True
        result.params_millions = params_millions
    if result.extraction_model != model_name_used:
        result.extraction_model = model_name_used
        changed = True
    return changed


# ── CLI ───────────────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Parse LLM output and store results in the DB")
    p.add_argument("arxiv_ids", nargs="+", metavar="ARXIV_ID")
    return p


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args(argv)

    total_new = 0
    for arxiv_id in args.arxiv_ids:
        arxiv_id = normalize_arxiv_id(arxiv_id)
        total_new += parse_and_store(arxiv_id)

    print(f"Total new Result rows created: {total_new}")


if __name__ == "__main__":
    main()
