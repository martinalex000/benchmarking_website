"""Load canonical architecture defaults for well-known baseline model families."""

from __future__ import annotations

import logging
from functools import lru_cache
from pathlib import Path

import yaml

from backend.model_metadata import normalize_architecture_type
from backend.model_name_resolution import model_family_token_for_metadata

logger = logging.getLogger(__name__)

_DEFAULTS_FILE = Path(__file__).resolve().parent.parent / "config" / "model_metadata_defaults.yaml"


@lru_cache(maxsize=1)
def load_model_metadata_defaults() -> dict[str, str]:
    """Return {family_token: canonical model_type} from config/model_metadata_defaults.yaml."""
    path = _DEFAULTS_FILE
    if not path.exists():
        logger.debug("Model metadata defaults file not found: %s", path)
        return {}

    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        logger.warning("Failed to load model metadata defaults: %s", exc)
        return {}

    models = raw.get("models") if isinstance(raw, dict) else None
    if not isinstance(models, dict):
        return {}

    defaults: dict[str, str] = {}
    for key, value in models.items():
        if not key or value is None:
            continue
        normalized_key = str(key).strip().lower().replace(" ", "")
        normalized_type = normalize_architecture_type(str(value))
        if normalized_key and normalized_type:
            defaults[normalized_key] = normalized_type
    return defaults


def lookup_default_model_type(model_name: str) -> str | None:
    """Return a default architecture type for a model name via its family token."""
    family = model_family_token_for_metadata(model_name)
    if not family:
        return None
    return load_model_metadata_defaults().get(family)


def lookup_model_type(
    model_name: str,
    type_lookup: dict[str, str | None],
    *,
    defaults: dict[str, str] | None = None,
) -> str | None:
    """Resolve model_type from per-paper lookups, then family token, then defaults."""
    key = model_name.strip().lower()
    if key in type_lookup and type_lookup[key]:
        return type_lookup[key]

    family = model_family_token_for_metadata(model_name)
    if family in type_lookup and type_lookup[family]:
        return type_lookup[family]

    active_defaults = defaults if defaults is not None else load_model_metadata_defaults()
    if family in active_defaults:
        return active_defaults[family]
    return None
