from types import SimpleNamespace

import pytest

from backend import pipeline


def test_aggregate_returns_failure_when_parse_fails(monkeypatch):
    monkeypatch.setattr(pipeline, "init_db", lambda: None)
    monkeypatch.setattr(pipeline, "stage_parse", lambda args: False)
    monkeypatch.setattr(
        pipeline,
        "stage_export",
        lambda args: pytest.fail("Export must not run after a parse failure"),
    )

    assert pipeline.main(["aggregate"]) == 1


def test_run_all_skips_export_and_build_after_parse_failure(monkeypatch):
    calls = []
    monkeypatch.setattr(pipeline, "stage_discover", lambda args: calls.append("discover"))
    monkeypatch.setattr(pipeline, "stage_download", lambda args: calls.append("download") or True)
    monkeypatch.setattr(pipeline, "stage_extract", lambda args: calls.append("extract") or True)
    monkeypatch.setattr(pipeline, "stage_parse", lambda args: calls.append("parse") or False)
    monkeypatch.setattr(
        pipeline,
        "stage_export",
        lambda args: pytest.fail("Export must not run after a parse failure"),
    )
    monkeypatch.setattr(
        pipeline,
        "stage_build",
        lambda args: pytest.fail("Build must not run after a parse failure"),
    )

    assert pipeline.stage_run_all(SimpleNamespace(since=None)) is False
    assert calls == ["discover", "download", "extract", "parse"]


def test_run_all_propagates_export_and_build_failures(monkeypatch):
    monkeypatch.setattr(pipeline, "stage_discover", lambda args: True)
    monkeypatch.setattr(pipeline, "stage_download", lambda args: True)
    monkeypatch.setattr(pipeline, "stage_extract", lambda args: True)
    monkeypatch.setattr(pipeline, "stage_parse", lambda args: True)
    monkeypatch.setattr(pipeline, "stage_export", lambda args: False)
    monkeypatch.setattr(
        pipeline,
        "stage_build",
        lambda args: pytest.fail("Build must not run after an export failure"),
    )
    assert pipeline.stage_run_all(SimpleNamespace(since=None)) is False

    monkeypatch.setattr(pipeline, "stage_export", lambda args: True)
    monkeypatch.setattr(pipeline, "stage_build", lambda args: False)
    assert pipeline.stage_run_all(SimpleNamespace(since=None)) is False
