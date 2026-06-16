"""Resolve local and external OpenAI-compatible LLM backends for model routing."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass

from openai import OpenAI

from backend.config import cfg

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class LlmBackend:
    """One OpenAI-compatible LLM server."""

    label: str  # "local" or "external"
    endpoint: str
    api_key: str


@dataclass(frozen=True)
class ModelRoute:
    """Which backend serves a given model ID."""

    model_id: str
    backend: LlmBackend


@dataclass(frozen=True)
class BackendProbe:
    """Reachability and model inventory for one configured backend."""

    backend: LlmBackend
    reachable: bool
    model_ids: tuple[str, ...] = ()
    error: str | None = None


def fetch_model_ids(endpoint: str, api_key: str, *, timeout: int = 30) -> list[str]:
    client = OpenAI(base_url=endpoint, api_key=api_key or "none", timeout=timeout)
    return sorted(m.id for m in client.models.list())


def configured_backends() -> list[LlmBackend]:
    """Return configured LLM backends (local first, then external when distinct)."""
    backends: list[LlmBackend] = []

    local_endpoint = (cfg.llm_local_endpoint or "").strip()
    if local_endpoint:
        backends.append(
            LlmBackend(
                label="local",
                endpoint=local_endpoint,
                api_key=cfg.llm_local_api_key or cfg.llm_api_key or "none",
            )
        )

    external_endpoint = (cfg.llm_endpoint or "").strip()
    if external_endpoint and external_endpoint not in {b.endpoint for b in backends}:
        backends.append(
            LlmBackend(
                label="external",
                endpoint=external_endpoint,
                api_key=cfg.llm_api_key or "none",
            )
        )

    return backends


def probe_backends(
    backends: list[LlmBackend] | None = None,
    *,
    timeout: int = 30,
) -> list[BackendProbe]:
    """Probe each configured backend and report reachability plus available model IDs."""
    if backends is None:
        backends = configured_backends()

    probes: list[BackendProbe] = []
    for backend in backends:
        try:
            model_ids = fetch_model_ids(backend.endpoint, backend.api_key, timeout=timeout)
            probes.append(BackendProbe(backend, True, tuple(model_ids)))
        except Exception as exc:
            probes.append(BackendProbe(backend, False, error=str(exc)))
    return probes


def fetch_model_routes(
    backends: list[LlmBackend] | None = None,
    *,
    timeout: int = 30,
) -> dict[str, ModelRoute]:
    """Merge model lists from all backends; local wins when a name appears twice."""
    if backends is None:
        backends = configured_backends()

    routes: dict[str, ModelRoute] = {}
    for backend in reversed(backends):
        try:
            model_ids = fetch_model_ids(backend.endpoint, backend.api_key, timeout=timeout)
        except Exception as exc:
            logger.warning("Could not list models from %s (%s): %s", backend.label, backend.endpoint, exc)
            continue
        for model_id in model_ids:
            routes[model_id] = ModelRoute(model_id=model_id, backend=backend)
    return routes


LEGACY_COMPARE_BASELINE = "glm-4.7"


def resolve_baseline_model_id(routes: dict[str, ModelRoute]) -> str:
    """Return the model ID used as the ground-truth comparison baseline."""
    explicit = (os.environ.get("LLM_COMPARE_BASELINE") or "").strip()
    for candidate in (
        explicit,
        cfg.model_fallback,
        LEGACY_COMPARE_BASELINE,
        cfg.model_primary,
    ):
        if candidate and candidate in routes:
            return candidate
    return explicit or cfg.model_fallback or LEGACY_COMPARE_BASELINE


def baseline_model_route(routes: dict[str, ModelRoute]) -> ModelRoute | None:
    model_id = resolve_baseline_model_id(routes)
    return routes.get(model_id)


def resolve_model_route(
    model_name: str,
    routes: dict[str, ModelRoute],
    *,
    allow_fallback: bool = True,
) -> ModelRoute | None:
    """Return routing for *model_name*, optionally substituting the configured fallback."""
    if model_name in routes:
        return routes[model_name]
    if not allow_fallback:
        return None
    fallback = cfg.model_fallback
    if fallback and fallback != model_name and fallback in routes:
        return routes[fallback]
    return None


def sort_models_local_first(
    model_ids: list[str],
    routes: dict[str, ModelRoute],
) -> list[str]:
    """Return *model_ids* with local-backend models first, then alphabetical within each group."""
    local = sorted(m for m in model_ids if m in routes and routes[m].backend.label == "local")
    external = sorted(
        m for m in model_ids if m in routes and routes[m].backend.label != "local"
    )
    unknown = sorted(m for m in model_ids if m not in routes)
    return local + external + unknown


def is_local_model(model_id: str, routes: dict[str, ModelRoute]) -> bool:
    route = routes.get(model_id)
    return route is not None and route.backend.label == "local"


def client_params_for_model(
    model_name: str,
    routes: dict[str, ModelRoute] | None = None,
) -> tuple[str, str, ModelRoute | None]:
    """Return ``(endpoint, api_key, route)`` for constructing an OpenAI client."""
    if routes is None:
        routes = fetch_model_routes()
    route = resolve_model_route(model_name, routes)
    if route is not None:
        return route.backend.endpoint, route.backend.api_key, route
    return (cfg.llm_endpoint or "").strip(), cfg.llm_api_key or "none", None
