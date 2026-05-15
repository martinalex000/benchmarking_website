# Extraction: arXiv:2403.16030
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: VCR-Graphormer
- Type: GraphTransformer

## Results

### Amazon2M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PPRGo | 0.6612 | 0.0059 | Yes | this paper | Table 1 |
| GraphSAINT | 0.7521 | 0.0015 | Yes | this paper | Table 1 |
| GRAND+ | 0.7549 | 0.0011 | Yes | this paper | Table 1 |
| NAGphormer | 0.7743 | 0.0011 | Yes | this paper | Table 1 |
| VCR-Graphormer | 0.7609 | 0.0016 | No | this paper | Table 1 |

### Reddit — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PPRGo | 0.9038 | 0.0011 | Yes | this paper | Table 1 |
| GraphSAINT | 0.9235 | 0.0008 | Yes | this paper | Table 1 |
| GRAND+ | 0.9281 | 0.0003 | Yes | this paper | Table 1 |
| NAGphormer | 0.9358 | 0.0005 | Yes | this paper | Table 1 |
| VCR-Graphormer | 0.9369 | 0.0008 | No | this paper | Table 1 |

## Baseline Models Identified

- **PPRGo** (from: null)
- **GraphSAINT** (from: null)
- **GRAND+** (from: null)
- **NAGphormer** (from: null)
- **Exphormer** (from: null)

## Extraction Notes

[PubMed] failed: 1 validation error for ExtractionOutput results.8.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [CoraFull] failed: 1 validation error for
ExtractionOutput results.8.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Amazon-Computers] The provided table contains results
for 'Reddit', 'Aminer', and 'Amazon2M'. The requested dataset 'Amazon-Computers' is not present in
this table. Therefore, no results were extracted. [Amazon-Photo] The provided table contains results
for 'Reddit', 'Aminer', and 'Amazon2M'. The requested dataset 'Amazon-Photo' is not present in the
table. Therefore, no results were extracted. [Coauthor-CS] The provided table contains results for
datasets 'Reddit', 'Aminer', and 'Amazon2M'. The requested dataset 'Coauthor-CS' is not present in
the table. Therefore, no results were extracted. [Coauthor-Physics] The provided table contains
results for 'Reddit', 'Aminer', and 'Amazon2M' datasets. There are no rows or columns corresponding
to the 'Coauthor-Physics' dataset. Therefore, no results could be extracted for the requested
dataset. [Reddit] The paper text mentions 'F1' in the focus instruction, but the provided table
explicitly reports 'Node Classification Accuracy'. The table caption is 'Node Classification
Accuracy on Large-Scale Datasets'. The values in the table are clearly accuracy scores (e.g., 90.38,
93.69). The text mentions parameter analysis on Reddit with values like 93.36, 93.02, 93.16, which
likely refer to accuracy or F1, but these are not in a structured table with standard deviations.
The table provides the most complete quantitative results. I have extracted the Accuracy metric from
Table 1 as it is the only structured result provided for Reddit. The focus instruction asked for F1,
but since the table only provides Accuracy, I extracted Accuracy. Note: The prompt asks to focus on
F1, but if the table only has Accuracy, Accuracy is the primary metric available. I will output
Accuracy as the metric. [Aminer] failed: 1 validation error for ExtractionOutput results.4.value
Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For
further information visit https://errors.pydantic.dev/2.13/v/float_type [Amazon2M] Extracted results
for Amazon2M from Table 1. Excluded Exphormer as it reported OOM (Out of Memory). The proposed model
VCR-Graphormer is listed in the table with its result. Note that NAGphormer has the highest accuracy
(0.7743) in this specific table, while VCR-Graphormer is the proposed method.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*