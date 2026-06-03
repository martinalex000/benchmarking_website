"""Tests for Result.params_millions backfill."""

from types import SimpleNamespace

from backend.result_params_backfill import _lookup_params, backfill_paper_params_millions


def test_lookup_params_matches_rendered_or_canonical():
    lookup = {"graphgps": 1.5, "gcn": 0.1}
    assert _lookup_params(lookup, "GraphGPS", "GraphGPS") == 1.5
    assert _lookup_params(lookup, "GCN", None) == 0.1
    assert _lookup_params(lookup, "Missing", "Missing") is None


def test_backfill_paper_params_millions_updates_null_rows():
    paper = SimpleNamespace(id=1, arxiv_id="9999.00001")
    model = SimpleNamespace(canonical_name="GraphGPS")
    row = SimpleNamespace(model=model, params_millions=None)
    session = SimpleNamespace(
        query=lambda *_a, **_k: SimpleNamespace(
            filter_by=lambda **_kw: SimpleNamespace(
                filter=lambda *_a2, **_k2: SimpleNamespace(all=lambda: [row])
            )
        )
    )
    lookup = {"graphgps": 2.5}

    updated, still_null = backfill_paper_params_millions(
        session,
        paper,
        lookup=lookup,
        dry_run=False,
    )

    assert updated == 1
    assert still_null == 0
    assert row.params_millions == 2.5
