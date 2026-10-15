"""Checks against independently computed t-test and confidence-interval thresholds."""

import math
import statistics

import pytest
from scipy.stats import t, ttest_ind

from backend.significance import is_significantly_different


def test_welch_matches_raw_samples_with_unequal_variances_and_counts():
    left = [0.71, 0.75, 0.79]
    for right in ([0.77, 0.78, 0.79, 0.80, 0.81], [0.90, 0.91, 0.92, 0.93, 0.94]):
        args = (
            statistics.mean(left),
            statistics.stdev(left),
            len(left),
            statistics.mean(right),
            statistics.stdev(right),
            len(right),
        )
        expected = bool(ttest_ind(left, right, equal_var=False).pvalue < 0.05)
        assert is_significantly_different(*args) is expected
        assert is_significantly_different(*args[3:], *args[:3]) is expected


def test_four_runs_reject_below_the_old_std_overlap_threshold():
    assert is_significantly_different(0, 1, 4, 1.8, 1, 4)
    assert not is_significantly_different(0, 1, 4, 1.7, 1, 4)
    assert is_significantly_different(0, 1, None, 1.8, 1, None)


def test_actual_counts_are_used_even_when_less_than_four():
    assert not is_significantly_different(0, 1, 3, 1.8, 1, 3)
    assert is_significantly_different(0, 1, 100, 0.3, 1, 100)
    assert not is_significantly_different(0, 1, None, 0.3, 1, None)


@pytest.mark.parametrize("reference_runs", [None, 1, 5, 100])
def test_one_std_uses_mean_ci_and_ignores_reference_count(reference_runs):
    margin = t.ppf(0.975, 3) / math.sqrt(4)
    for delta, expected in ((margin - 1e-8, False), (margin + 1e-8, True)):
        assert is_significantly_different(0, 1, 4, delta, None, reference_runs) is expected
        assert is_significantly_different(delta, None, reference_runs, 0, 1, 4) is expected
    # A two-standard-deviation gap is inside the prediction interval but outside the mean CI.
    assert is_significantly_different(0, 1, None, 2, None, reference_runs)


@pytest.mark.parametrize("runs", [None, 3, 100])
def test_two_bare_values_use_exact_inequality(runs):
    assert is_significantly_different(0.8, None, runs, 0.8 + 1e-13, None, runs)
    assert not is_significantly_different(0.8, None, runs, 0.8, None, runs)


@pytest.mark.parametrize("bad_mean", [None, math.nan, math.inf, -math.inf])
def test_unavailable_means_return_false(bad_mean):
    assert not is_significantly_different(bad_mean, 1, 4, 0, 1, 4)
    assert not is_significantly_different(0, 1, 4, bad_mean, 1, 4)


@pytest.mark.parametrize("bad_std", [-1, math.nan, math.inf])
def test_invalid_stds_are_missing_not_zero(bad_std):
    assert not is_significantly_different(0, 1, 4, 1, bad_std, 100)
    assert is_significantly_different(0, bad_std, 100, 1, None, None)


@pytest.mark.parametrize("std2", [None, 0])
def test_zero_std_is_distinct_from_missing_std(std2):
    assert is_significantly_different(0, 0, 4, 1, std2, 4)
    assert not is_significantly_different(0, 0, 4, 0, std2, 4)
    # With just one zero std, Welch still accounts for the other side's variance.
    assert not is_significantly_different(0, 0, 4, 1, 1, 4)


@pytest.mark.parametrize("bad_count", [0, 1, -4, 2.5, math.nan, math.inf, True])
def test_invalid_std_bearing_counts_raise(bad_count):
    with pytest.raises(ValueError, match="repetition count"):
        is_significantly_different(0, 1, bad_count, 2, None, None)
