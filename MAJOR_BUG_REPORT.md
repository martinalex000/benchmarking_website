# Fixed Bug Summary

## 1. QM9 `gap` percentage normalization
Bug: substring metric matching treated `gap` as `AP` and divided values by 100.
Fix: percentage detection is now token-aware and keeps non-percentage `gap` values unchanged.
Tests: regression coverage added for `gap`, `AP`, `mAP`, `Accuracy`, `Micro-F1`, and `Hits@K`.

## 2. Extracted boolean parsing
Bug: string values like `"False"` were truthy and reversed lower-is-better rankings.
Fix: extraction booleans are normalized with strict helpers before persistence.
Tests: regression coverage added for string true/false and optional boolean fields.

## 3. Dataset table override standard deviations
Bug: dataset multi-metric rows used `display_value` but stale `metric_std`.
Fix: dataset export now reads `display_std`, preserving manual std overrides.
Tests: regression coverage added for overridden value/std rows.

## 4. Timeline milestone override standard deviations
Bug: milestone chart data used stale `metric_std` for overridden results.
Fix: milestone generation now emits `display_std`.
Tests: regression coverage added for overridden milestone stds.

## 5. Quiet OGB dataset fuzzy matching
Bug: shared quiet resolver could fuzzy-match unrelated OGB datasets.
Fix: quiet resolver now uses token-sort scoring plus OGB family compatibility checks.
Tests: regression coverage added for `ogbg-ppa` and `ogbl-ppa` false positives.

## 6. arXiv ID path traversal
Bug: `normalize_arxiv_id()` allowed malformed IDs like `../../tmp/ownedv1` into storage paths.
Fix: arXiv IDs are now explicitly parsed and validated before use.
Tests: regression coverage added for valid modern IDs and unsafe invalid inputs.

## 7. Hugo paper export path traversal and destructive delete
Bug: paper export used raw `arxiv_id` path components for writes and removals.
Fix: export now validates arXiv IDs and refuses deletion outside generated content roots.
Tests: regression coverage added for refusing out-of-root Hugo content deletion.

## 8. Alternative downloader SSRF
Bug: alternative PDF downloads accepted arbitrary URLs and followed redirects blindly.
Fix: URL fetches now allow only public HTTP(S) targets and validate each redirect target.
Tests: regression coverage added for private IP and private DNS-resolution rejection.

## 9. Alternative downloader unbounded download
Bug: alternative PDF downloads accumulated unlimited response bodies in memory.
Fix: PDF downloads now enforce a 200 MB `Content-Length` and streaming byte limit.
Tests: regression coverage added for header-declared and streamed over-limit PDFs.

## 10. Figure extractor local path traversal
Bug: HTML image sources could escape the downloaded HTML directory via `../` paths.
Fix: local image copies now require resolved paths to stay under the HTML asset root.
Tests: regression coverage added for refusing `../secret.png` style traversal.

## 11. Figure extractor SSRF and unbounded download
Bug: HTML figure downloads accepted arbitrary HTTP URLs and wrote unbounded response bodies.
Fix: figure downloads now use public HTTP(S) URL validation and a 50 MB streaming byte limit.
Tests: regression coverage added for rejecting private figure URLs.

## 12. Scientific-notation result parsing
Bug: result values like `1e-3` were skipped, and `1e-3 ± 2e-4` was corrupted.
Fix: result value parsing now supports signed decimal scientific notation.
Tests: regression coverage added for plain and plus-minus scientific notation.

## 13. Dataset statistics exponent parsing
Bug: dataset stats like `1e6` and `1.2e3` lost their exponents.
Fix: dataset statistic number parsing now recognizes scientific notation.
Tests: regression coverage added for exponent-form dataset statistics.

## 14. Removed overrides remaining in DB
Bug: deleting a result override from `overrides.yaml` did not clear prior DB override flags.
Fix: override application now clears stale result override/problematic fields before applying current overrides.
Tests: regression coverage added for clearing removed DB overrides.

## 15. Metadata override replacing bad codebase URLs
Bug: `metadata_overrides.codebase_url` only applied when the DB field was empty.
Fix: metadata overrides now replace an existing incorrect codebase URL.
Tests: regression coverage added for replacing a bad stored codebase URL.

## 16. Uncertainty comparison overlap
Bug: value comparison checked each std independently rather than combined uncertainty.
Fix: comparison now treats differences inside the summed uncertainty as not significant.
Tests: regression coverage added for overlapping combined-std intervals.
