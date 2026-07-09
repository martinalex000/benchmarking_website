# Major Bug Report

This review found three high-impact bugs in the ingestion/export path. Two can silently corrupt leaderboard data; one currently prevents a focused test module from collecting.

## 1. QM9 `gap` metrics are wrongly divided by 100

- Location: `backend/results_parser.py:90`, `backend/results_parser.py:161`, `backend/results_parser.py:1142`
- Severity: High
- Impact: Silent data corruption for QM9 gap results and any non-percentage metric containing `ap`.

`_is_percentage_metric()` uses substring matching over `_PERCENTAGE_METRIC_SUBSTRINGS`. Because `"ap"` is in that list, the normalized QM9 target metric `"gap"` is treated as average precision and divided by 100 whenever the value is above 1.0.

Observed behavior:

```text
normalize_percentage_metric("gap", 2.5, 0.1) -> (0.025, 0.001)
```

That is incorrect for a metric named `gap`; it should remain `(2.5, 0.1)` unless the pipeline has dataset-specific evidence that the value is percentage-scaled.

Recommended fix:

- Replace broad substring matching with token-aware metric matching.
- Treat `"ap"` as a standalone token or exact metric alias, not as any occurrence inside another word.
- Add regression tests for `gap`, `mAP`, `AP`, `Accuracy`, and `Hits@K`.

## 2. String booleans reverse lower-is-better leaderboards

- Location: `backend/results_parser.py:1074`; downstream examples at `backend/export_to_hugo.py:1531`, `backend/export_to_hugo.py:1773`, `backend/export_to_hugo.py:1895`, `backend/export_to_hugo.py:2048`
- Severity: High
- Impact: Lower-is-better metrics can be ranked and compared as higher-is-better when extraction payloads contain string booleans.

The parser stores `higher_is_better=entry.get("higher_is_better", True)` directly. If an extraction payload contains `"False"` or `"false"` as a string, SQLAlchemy accepts it on the model object and downstream code repeatedly uses `bool(r.higher_is_better)`. Non-empty strings are truthy in Python:

```text
Result(higher_is_better="False")
bool(result.higher_is_better) -> True
```

That flips MAE/RMSE/loss-style metrics from ascending to descending order in export, comparisons, at-publication analysis, and baseline aggregation.

Recommended fix:

- Normalize all extracted booleans at parser boundaries with a strict helper such as `parse_bool(value, default=True)`.
- Accept only real booleans and common string forms (`"true"`, `"false"`, `"yes"`, `"no"`, `"1"`, `"0"`); warn or default for unknown values.
- Add parser/export regression tests with `"higher_is_better": "False"` on an MAE metric.

## 3. Dataset export ignores overridden standard deviations

- Location: `backend/export_to_hugo.py:2810`
- Severity: Medium-high
- Impact: Dataset pages can display/use corrected values with stale uncertainty, making value-gap, duplicate, outlier, and “significant difference” annotations wrong after manual overrides.

The multi-metric dataset export correctly uses `r.display_value`, which respects `override_value`, but reads the uncertainty from `r.metric_std` instead of `r.display_std`:

```python
val = float(r.display_value) if r.display_value is not None else None
std = float(r.metric_std) if r.metric_std is not None else None
```

This is inconsistent with other export paths that use `display_std`. If a manual override corrects both value and std, the dataset leaderboard row gets the corrected value but the old standard deviation.

Recommended fix:

- Change this path to use `r.display_std`.
- Add a regression test where `is_overridden=1`, `override_value`, and `override_std` differ from the original metric fields, then assert `metric_stds` uses the override.

## Additional test-suite issue

- Location: `tests/unit/test_export_to_hugo.py:32`
- Impact: `uv run pytest tests/unit/test_export_to_hugo.py` cannot collect.

The test imports `_normalize_conference` from `backend.export_to_hugo`, but that symbol no longer exists there. The venue normalization code now lives in `backend.venue` as `normalize_conference_short()` / `conference_export_fields()`.

Observed command:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run pytest tests/unit/test_results_parser.py tests/unit/test_export_to_hugo.py -q
```

Observed failure:

```text
ImportError: cannot import name '_normalize_conference' from 'backend.export_to_hugo'
```

