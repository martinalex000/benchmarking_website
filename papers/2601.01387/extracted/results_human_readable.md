# Extraction: Scale-Adaptive Power Flow Analysis with Local Topology Slicing and Multi-Task Graph Learning
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: RMGL
- Type: Other

## Results

### Case 1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GLP | 99.5400 | — | Yes | this paper | Table 1 |
| GLR | 99.6300 | — | Yes | this paper | Table 1 |
| MGL | 99.6400 | — | Yes | this paper | Table 1 |
| RMGL | 99.8700 | — | No | this paper | Table 1 |

### Case 2 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GLP | 50.7200 | — | Yes | this paper | Table 2 |
| GLR | 47.0900 | — | Yes | this paper | Table 2 |
| MGL | 96.0700 | — | Yes | this paper | Table 2 |
| RMGL | 99.2800 | — | No | this paper | Table 2 |

## Baseline Models Identified

- **GLP**
- **GLR**
- **MGL**

## Extraction Notes

[Case 1] Extracted only 'Test set' rows from Table 1 (Case 1) as per FOCUS instructions. Ignored
'Gen-D' and 'Gen-U' rows as they are not the standard/default 'Test set' configuration. Ignored
Table 2 (Case 2). Metric normalized to 'Accuracy' from 'Acc (%)'. No standard deviation reported in
the table. [Case 2] Extracted results for 'Case 2' from Table 2. The table lists 'Test set' and 'Gen
set' rows. The 'Test set' row is the standard evaluation split. The 'Gen set' is a specific
generation set (Gen-N & Gen-U) and is treated as a secondary diagnostic or specific subset, but
since the prompt asks for standard/default configuration and 'Test set' is the primary benchmark
split, only 'Test set' results were extracted. If 'Gen set' is considered part of the standard
evaluation, it should be included, but typically 'Test set' is the primary metric source. Given the
ambiguity of 'Gen set' being a separate split, I prioritized the 'Test set' as the standard
benchmark. However, looking at the table structure, 'Test set' is clearly the main evaluation. The
prompt asks for 'Case 2' results. I will include only the 'Test set' rows as they represent the
standard test performance. If the user intended both, the confidence would be lower due to ambiguity
on what 'standard' means in this specific power system context, but 'Test set' is the safest
interpretation of standard benchmark.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*