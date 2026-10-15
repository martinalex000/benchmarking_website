"""Pairwise 95% significance decisions from reported summary statistics."""

from __future__ import annotations

import math
from functools import lru_cache

from scipy.stats import t, ttest_ind_from_stats

SIGNIFICANCE_METHOD = (
    "Two-sided pairwise tests at alpha=0.05, without multiple-comparison correction. "
    "Two reported stds: Welch's t-test. One reported std: compare the other value "
    "with the 95% Student-t confidence interval for the mean, treating that value "
    "as a fixed reference even when it has a repetition count. Missing repetition "
    "counts on std-bearing results default to 4; explicit counts are preserved. "
    "Without either std, unequal values are considered significantly different. "
    "Negative or non-finite stds are treated as unavailable."
)


def _sample_size(count: int | None) -> int:
    if count is None:
        return 4
    if isinstance(count, bool) or not math.isfinite(count) or count != int(count) or count < 2:
        raise ValueError("A reported std requires an integer repetition count of at least 2")
    return int(count)


# Historical plots compare the same pairs at many successive cutoffs.
@lru_cache(maxsize=65536)
def is_significantly_different(
    mean1: float | None,
    std1: float | None,
    num_runs1: int | None,
    mean2: float | None,
    std2: float | None,
    num_runs2: int | None,
) -> bool:
    """Return whether two values differ under the uncorrected 95% comparison rule.

    Missing/non-finite means return False. Invalid stds are unavailable, not zero.
    Counts are used only for sides with a valid std, defaulting to four if missing.
    Explicit counts below two cannot support a t-test and raise ValueError.
    A zero std is valid; two zero stds imply a difference exactly when means differ.
    """
    if mean1 is None or mean2 is None or not all(map(math.isfinite, (mean1, mean2))):
        return False
    if mean1 == mean2:
        return False
    std1 = std1 if std1 is not None and math.isfinite(std1) and std1 >= 0 else None
    std2 = std2 if std2 is not None and math.isfinite(std2) and std2 >= 0 else None
    if std1 is None and std2 is None:
        return True

    n1 = _sample_size(num_runs1) if std1 is not None else None
    n2 = _sample_size(num_runs2) if std2 is not None else None
    if std1 is not None and std2 is not None:
        if std1 == std2 == 0:
            return True
        result = ttest_ind_from_stats(mean1, std1, n1, mean2, std2, n2, equal_var=False)
        return bool(result.pvalue < 0.05)

    std, count = (std1, n1) if std1 is not None else (std2, n2)
    if std == 0:
        return True
    statistic = abs(mean1 - mean2) / (std / math.sqrt(count))
    return bool(t.sf(statistic, df=count - 1) < 0.025)
