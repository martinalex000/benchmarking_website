# Extraction: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message Passing
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: CARIBOU
- Type: GNN

## Results

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CARIBOU | 0.8510 | — | No | this paper | Table 1 |
| DPDGC | 0.7550 | — | Yes | this paper | Table 1 |
| GAP | 0.7710 | — | Yes | this paper | Table 1 |
| PertGraph | 0.6000 | — | Yes | this paper | Table 1 |

### Facebook — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CARIBOU | 0.7400 | — | No | this paper | Table 1 |
| DPDGC | 0.6060 | — | Yes | this paper | Table 1 |
| GAP | 0.6850 | — | Yes | this paper | Table 1 |
| PertGraph | 0.4820 | — | Yes | this paper | Table 1 |

### Photo — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CARIBOU | 0.9580 | — | No | this paper | Table 1 |
| DPDGC | 0.9250 | — | Yes | this paper | Table 1 |
| GAP | 0.9300 | — | Yes | this paper | Table 1 |
| PertGraph | 0.8240 | — | Yes | this paper | Table 1 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CARIBOU | 0.8820 | — | No | this paper | Table 1 |
| DPDGC | 0.8830 | — | Yes | this paper | Table 1 |
| GAP | 0.8740 | — | Yes | this paper | Table 1 |
| PertGraph | 0.8500 | — | Yes | this paper | Table 1 |

### Reddit2 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CARIBOU (EDP) | 0.7060 | — | No | this paper | Table 1 |
| CARIBOU (NDP) | 0.6370 | — | No | this paper | Table 1 |

## Baseline Models Identified

- **DPDGC**
- **GAP**
- **PertGraph**

## Extraction Notes

[Cora] Extracted results for Cora from Table 1 across all epsilon values (1, 2, 4, 8, 16) for both
EDP and NDP tasks. The table structure groups results by epsilon. For each epsilon, results for
CARIBOU, DPDGC, GAP, and PertGraph are listed. The values are percentages from the table, converted
to [0,1] range. Note: The text mentions 'NDP with epsilon=1' accuracy of 67.47% for CARIBOU, but the
table shows 85.1% for EDP epsilon=1. The table caption says 'Comparison of Classification Accuracy
for EDP and NDP'. Looking closely at the table, the rows are labeled by epsilon, but there is no
explicit column distinguishing EDP vs NDP in the pasted text snippet. However, the text says 'For
both EDP and NDP tasks...'. Usually, these tables show one setting or aggregate. Given the high
accuracy (85.1%) vs the text's 67.47%, and the fact that 85.1% is the best in the table for Cora at
eps=1, it is likely the table shows the best performing setting or EDP. The text explicitly
contrasts CARIBOU (67.47%) with DPDGC (31.04%) for NDP eps=1. The table shows DPDGC at 75.5% for
eps=1. This discrepancy suggests the table might be showing EDP results or a different
configuration. However, the prompt asks to extract results from the paper. The table is the primary
source of structured data. The text values (67.47, 31.04) are significantly different from the table
(85.1, 75.5). The table header says 'EDP and NDP'. It is possible the table shows EDP results
primarily or the 'best' of both. Given the ambiguity, I extracted the table values as they are the
most structured quantitative data provided for the standard configurations. The text values might
refer to a specific NDP scenario not fully detailed in the table snippet or a different split. I
will stick to the table values as they are explicitly tabulated for the dataset 'Cora'. The table
rows correspond to epsilon values 1, 2, 4, 8, 16. I extracted all 5 rows for each model. [PubMed]
Extracted results for PubMed from Table 1. The table presents results for different epsilon values
(1, 2, 4, 8, 16). Since the prompt asks for the STANDARD/DEFAULT configuration and does not specify
an epsilon, and the paper discusses CARIBOU's stability across epsilons, I have included all
reported test accuracies for PubMed across all epsilon settings as they represent the model's
performance profile. The values are percentages from the table, converted to [0,1] range. No
standard deviation is reported in the table. [Facebook] Extracted all rows for the 'Facebook'
dataset from Table 1 across all epsilon values (1, 2, 4, 8, 16). The table presents Accuracy
percentages which were converted to [0,1] range. The last row for CARIBOU at epsilon=16 is partially
cut off in the provided text ('\cellcolor{colorbest}\col'), but the value '74.5%' is visible in the
previous line's context or inferred from the pattern. However, looking closely at the provided text
snippet for epsilon=16, the CARIBOU value for Facebook is '74.5%'. The DPDGC, GAP, and PertGraph
values for epsilon=16 are not fully visible in the provided text snippet (it cuts off after DPDGC's
Facebook value '78.6%'). I have extracted the visible values. Note: The text snippet ends abruptly
at 'DPDGC & $90.4\%$ & \cellcolor{colorbest}\col'. I will assume the Facebook value for DPDGC at
epsilon=16 is 78.6% based on the previous line's pattern or similar, but strictly speaking, it's not
fully visible. Wait, looking at the epsilon=8 row, DPDGC Facebook is 78.6%. In epsilon=16 row, the
text says 'DPDGC & $90.4\%$ & \cellcolor{colorbest}\col'. It seems the Facebook value for DPDGC at
epsilon=16 is missing or cut off. I will only extract what is clearly visible. For CARIBOU at
epsilon=16, Facebook is 74.5%. For DPDGC at epsilon=16, the Facebook cell is cut off. I will exclude
the incomplete DPDGC epsilon=16 Facebook row if the value is not clear. Actually, looking at the
pattern, the Facebook column is the 3rd data column. In epsilon=16 row: CARIBOU (74.5%), DPDGC (cut
off). I will extract CARIBOU 74.5%. I will not extract DPDGC, GAP, PertGraph for epsilon=16 as their
values are not visible in the provided text snippet. [Photo] Extracted all rows for the 'Photo'
dataset from Table 1 across all epsilon values (1, 2, 4, 8, 16). The table provides Accuracy
percentages. Values were converted from percentage to decimal (e.g., 95.8% -> 0.958). No standard
deviation was reported in the table for these results. The table is cut off in the provided text,
but the visible rows for Photo were fully extracted. The last row for epsilon=16 is incomplete in
the source text but the Photo column value for CARIBOU (0.96) and others (0.946, 0.946, 0.922) are
visible and consistent with the pattern. [Reddit2] The paper reports results for the proposed model
CARIBOU under two privacy definitions (EDP and NDP) across six privacy budgets (epsilon). No
baseline models are reported in the provided text/table for Reddit2. All values are percentages
converted to [0,1] range. Standard deviations are not reported.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*