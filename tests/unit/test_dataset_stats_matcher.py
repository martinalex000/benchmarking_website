"""Unit tests for dataset statistics matching and merging."""

from backend.dataset_stats_matcher import (
    CanonicalStats,
    StatsObservation,
    classify_match,
    merge_stats,
    observation_from_dict,
)
from backend.dataset_stats_parsing import values_compatible


def test_abbreviated_3k_and_4k_compatible_with_3800():
    ok3, tier3 = values_compatible(
        3000, 3800, raw_value="3k", precision_hint="abbreviated", is_integer_field=True
    )
    ok4, tier4 = values_compatible(
        4000, 3800, raw_value="4k", precision_hint="abbreviated", is_integer_field=True
    )
    assert ok3 is True
    assert ok4 is True
    assert "abbreviated" in tier3
    assert "abbreviated" in tier4


def test_abbreviated_12k_compatible_with_12345():
    ok, tier = values_compatible(
        12000,
        12345,
        raw_value="12k",
        precision_hint="abbreviated",
        is_integer_field=True,
    )
    assert ok is True
    assert "abbreviated" in tier


def test_abbreviated_3k_incompatible_with_1500():
    ok, _tier = values_compatible(
        3000,
        1500,
        raw_value="3k",
        precision_hint="abbreviated",
        is_integer_field=True,
    )
    assert ok is False


def test_precise_counts_within_two_percent_match():
    ok, tier = values_compatible(15535, 15400, is_integer_field=True)
    assert ok is True
    assert tier == "precise_2pct"


def test_classify_match_mismatch_when_precise_values_disagree():
    observation = StatsObservation(num_graphs=1000, avg_nodes=50.0)
    canonical = CanonicalStats(num_graphs=5000, avg_nodes=50.0)
    result = classify_match(observation, canonical)
    assert result.status == "mismatch"
    assert "num_graphs" in result.mismatch_fields


def test_classify_match_accepts_abbreviated_graph_count():
    observation = observation_from_dict(
        {
            "num_graphs": 3000,
            "raw_values": {"num_graphs": "3k"},
            "precision_hints": {"num_graphs": "abbreviated"},
        }
    )
    canonical = CanonicalStats(num_graphs=3800)
    result = classify_match(observation, canonical)
    assert result.status == "matched"


def test_merge_stats_fills_gaps_and_extends_extra_stats():
    canonical = CanonicalStats(num_graphs=3800, extra_stats={"density": 0.1})
    observation = StatsObservation(
        num_graphs=3000,
        avg_nodes=150.0,
        extra_stats={"heterophily": 0.42, "density": 0.2},
    )
    merged = merge_stats(canonical, observation)
    assert merged.num_graphs == 3800
    assert merged.avg_nodes == 150.0
    assert merged.extra_stats == {"density": 0.1, "heterophily": 0.42}
