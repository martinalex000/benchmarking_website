"""Tests for backend.llm_backends."""

from __future__ import annotations

from unittest.mock import patch

from backend.llm_backends import (
    LEGACY_COMPARE_BASELINE,
    LlmBackend,
    ModelRoute,
    client_params_for_model,
    fetch_model_routes,
    probe_backends,
    resolve_baseline_model_id,
    sort_models_local_first,
)


def test_sort_models_local_first() -> None:
    local = LlmBackend(label="local", endpoint="http://127.0.0.1:8000/v1", api_key="local")
    external = LlmBackend(
        label="external",
        endpoint="https://example.com/v1",
        api_key="external",
    )
    routes = {
        "z-local": ModelRoute("z-local", local),
        "a-local": ModelRoute("a-local", local),
        "b-external": ModelRoute("b-external", external),
    }
    ordered = sort_models_local_first(["b-external", "z-local", "a-local"], routes)
    assert ordered == ["a-local", "z-local", "b-external"]


def test_resolve_baseline_model_id_prefers_fallback_over_legacy(monkeypatch) -> None:
    from backend.config import cfg

    monkeypatch.setattr(cfg, "model_fallback", "moonshotai/Kimi-K2.6")
    external = LlmBackend(
        label="external",
        endpoint="https://example.com/v1",
        api_key="external",
    )
    routes = {
        "moonshotai/Kimi-K2.6": ModelRoute("moonshotai/Kimi-K2.6", external),
        LEGACY_COMPARE_BASELINE: ModelRoute(LEGACY_COMPARE_BASELINE, external),
    }
    assert resolve_baseline_model_id(routes) == "moonshotai/Kimi-K2.6"


def test_fetch_model_routes_prefers_local_on_duplicate_names() -> None:
    local = LlmBackend(label="local", endpoint="http://127.0.0.1:8000/v1", api_key="local")
    external = LlmBackend(
        label="external",
        endpoint="https://example.com/v1",
        api_key="external",
    )

    def fake_fetch(endpoint: str, api_key: str, *, timeout: int = 30) -> list[str]:
        if endpoint == local.endpoint:
            return ["shared-model", "local-only"]
        return ["shared-model", "external-only"]

    with patch("backend.llm_backends.fetch_model_ids", side_effect=fake_fetch):
        routes = fetch_model_routes([local, external])

    assert set(routes) == {"shared-model", "local-only", "external-only"}
    assert routes["shared-model"].backend.label == "local"
    assert routes["local-only"].backend.label == "local"
    assert routes["external-only"].backend.label == "external"


def test_probe_backends_reports_unreachable_errors() -> None:
    local = LlmBackend(label="local", endpoint="http://127.0.0.1:8000/v1", api_key="local")
    external = LlmBackend(
        label="external",
        endpoint="https://example.com/v1",
        api_key="external",
    )

    def fake_fetch(endpoint: str, api_key: str, *, timeout: int = 30) -> list[str]:
        if endpoint == local.endpoint:
            raise ConnectionError("connection refused")
        return ["external-model"]

    with patch("backend.llm_backends.fetch_model_ids", side_effect=fake_fetch):
        probes = probe_backends([local, external])

    assert len(probes) == 2
    local_probe = next(p for p in probes if p.backend.label == "local")
    external_probe = next(p for p in probes if p.backend.label == "external")
    assert local_probe.reachable is False
    assert "connection refused" in (local_probe.error or "")
    assert external_probe.reachable is True
    assert external_probe.model_ids == ("external-model",)


def test_client_params_for_model_prefers_local_route() -> None:
    local = LlmBackend(label="local", endpoint="http://127.0.0.1:8000/v1", api_key="local-key")
    routes = {
        "shared-model": ModelRoute("shared-model", local),
    }
    endpoint, api_key, route = client_params_for_model("shared-model", routes)
    assert endpoint == "http://127.0.0.1:8000/v1"
    assert api_key == "local-key"
    assert route is not None
    assert route.backend.label == "local"
