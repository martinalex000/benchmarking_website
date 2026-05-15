# Extraction: FloydNet: A Learning Paradigm for Global Relational Reasoning
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: FloydNet
- Type: GNN

## Results

### BREC — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| 1-WL Test | 0.0000 | — | Yes | this paper | Table 1 |
| 3-WL Test | 0.6750 | — | Yes | this paper | Table 1 |
| GIN (MPNN) | 0.0000 | — | Yes | this paper | Table 1 |
| Graphormer | 0.1980 | — | Yes | this paper | Table 1 |
| GDT+RWSE | 0.5080 | — | Yes | this paper | Table 1 |
| PPGT | 0.5850 | — | Yes | this paper | Table 1 |
| I^2-GNN | 0.7020 | — | Yes | this paper | Table 1 |
| KP-GNN | 0.6880 | — | Yes | this paper | Table 1 |
| PPGN | 0.5820 | — | Yes | this paper | Table 1 |
| KC-SetGNN | 0.5280 | — | Yes | this paper | Table 1 |
| FloydNet | 0.6750 | — | No | this paper | Table 1 |
| FloydNet-KP | 0.8150 | — | No | this paper | Table 1 |
| k-FWL 3 | 0.9500 | — | No | this paper | Table 1 |
| k-FWL 4 | 0.9980 | — | No | this paper | Table 1 |

### CLRS-30 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Triplet-GMPNN | 0.8004 | — | Yes | Ibarz et al. 2022 | Table 1 |
| RANR | 0.7578 | — | Yes | Xu et al. 2024 | Table 1 |
| G-ForgetNet | 0.8289 | — | Yes | Bohde et al. 2024 | Table 1 |
| RT | 0.6618 | — | Yes | Diao et al. 2022 | Table 1 |
| ET | 0.8013 | — | Yes | Muller et al. 2024 | Table 1 |
| FloydNet | 0.9664 | — | No | this paper | Table 1 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | — | Yes | Brossard et al. 2020 | Table 1 |
| Exphormer | 0.3430 | — | Yes | Shirzad et al. 2023 | Table 1 |
| GPS | 0.3774 | — | Yes | Rampásek et al. 2022 | Table 1 |
| Graph-Mamba | 0.3960 | — | Yes | Wang et al. 2024 | Table 1 |
| FloydNet | 0.4901 | — | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | — | Yes | Brossard et al. 2020 | Table 1 |
| Exphormer | 0.3587 | — | Yes | Shirzad et al. 2023 | Table 1 |
| GPS | 0.3437 | — | Yes | Rampásek et al. 2022 | Table 1 |
| Graph-Mamba | 0.3395 | — | Yes | Wang et al. 2024 | Table 1 |
| FloydNet | 0.6143 | — | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | — | Yes | this paper | Table 1 |
| Exphormer | 0.3446 | — | Yes | this paper | Table 1 |
| GPS | 0.3724 | — | Yes | this paper | Table 1 |
| Graph-Mamba | 0.4191 | — | Yes | this paper | Table 1 |
| FloydNet | 0.4046 | — | No | this paper | Table 1 |

### Peptides-Struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | — | Yes | Brossard et al. 2020 | Table 1 |
| Exphormer | 0.2512 | — | Yes | Shirzad et al. 2023 | Table 1 |
| GPS | 0.2500 | — | Yes | Rampásek et al. 2022 | Table 1 |
| Graph-Mamba | 0.2478 | — | Yes | Wang et al. 2024 | Table 1 |
| FloydNet | 0.2612 | — | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | — | Yes | Brossard et al. 2020 | Table 1 |
| Exphormer | 0.6258 | — | Yes | Shirzad et al. 2023 | Table 1 |
| GPS | 0.6535 | — | Yes | Rampásek et al. 2022 | Table 1 |
| Graph-Mamba | 0.6739 | — | Yes | Wang et al. 2024 | Table 1 |
| FloydNet | 0.6224 | — | No | this paper | Table 1 |

### TSP-100 — Gap ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Linkern | 0.0010 | — | Yes | this paper | Table 1 |
| Proposed Method (Single Solution, Metric) | 0.0010 | — | No | this paper | Table 1 |
| Proposed Method (Single Solution, Non-Metric) | 0.0010 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Metric, k=1) | 0.0250 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Metric, k=5) | 0.0020 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Metric, k=10) | 0.0010 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Non-Metric, k=1) | 0.0620 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Non-Metric, k=5) | 0.0040 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Non-Metric, k=10) | 0.0010 | — | No | this paper | Table 1 |

### TSP-200 — Gap ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Linkern | 0.0020 | — | Yes | this paper | Table 1 |
| Proposed Method (Single Solution, Metric) | 0.0020 | — | No | this paper | Table 1 |
| Proposed Method (Single Solution, Non-Metric) | 0.0000 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Metric, k=1) | 0.0750 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Metric, k=5) | 0.0110 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Metric, k=10) | 0.0040 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Non-Metric, k=1) | 0.0600 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Non-Metric, k=5) | 0.0030 | — | No | this paper | Table 1 |
| Proposed Method (Multi-Solution, Non-Metric, k=10) | 0.0010 | — | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MPNN | 0.1380 | — | Yes | this paper | Table 1 |
| Subgraph GNN | 0.1100 | — | Yes | this paper | Table 1 |
| Local 2-GNN | 0.0690 | — | Yes | this paper | Table 1 |
| Graphormer | 0.0810 | — | Yes | this paper | Table 1 |
| ET+RRWP | 0.0590 | — | Yes | this paper | Table 1 |
| FloydNet | 0.0580 | — | No | this paper | Table 1 |

## Baseline Models Identified

- **Triplet-GMPNN** (from: Ibarz et al. 2022)
- **RANR** (from: Xu et al. 2024)
- **G-ForgetNet** (from: Bohde et al. 2024)
- **RT** (from: Diao et al. 2022)
- **ET** (from: Muller et al. 2024)
- **Linkern** (from: Linkern solver)
- **GCN** (from: Brossard et al. 2020)
- **Exphormer** (from: Shirzad et al. 2023)
- **GPS** (from: Rampásek et al. 2022)
- **Graph-Mamba** (from: Wang et al. 2024)
- **MPNN**
- **Subgraph GNN**
- **Local 2-GNN**
- **Graphormer** (from: Zhang et al. 2023)
- **ET+RRWP** (from: Muller et al. 2024)
- **1-WL Test**
- **3-WL Test**
- **GIN (MPNN)**
- **GDT+RWSE**
- **PPGT**
- **I^2-GNN**
- **KP-GNN**
- **PPGN**
- **KC-SetGNN**

## Extraction Notes

[CLRS-30] Extracted only the 'Total (N=30)' column from Table 1 as it represents the aggregated
benchmark result for CLRS-30. Values are percentages from the table, converted to [0,1] range. Table
2 contains per-algorithm breakdowns and hint/no-hint comparisons; per instructions to focus on the
standard/default configuration and primary metric, only the aggregated 'Total' scores from Table 1
are included as they represent the standard evaluation protocol described in the text. Table 2's 'No
Hint' column for FloydNet is a variant analysis, not the primary reported benchmark score in Table
1. [TSP-100] Extracted Gap (%) values for TSP-100. The table reports 'Gap (%)' which is a
percentage. Per instructions, for metrics like Gap (optimality gap), if it represents a percentage
(e.g. 0.001%), it should be treated as a value in [0,1] if it's a standard benchmark score like
Accuracy. However, Gap is typically a small number. The table header says 'Gap (%)'. The values are
0.001, 0.025, etc. If these are percentages, 0.001% = 0.00001. But usually in these tables, the
value *is* the percentage number. Let's look at the instruction: 'Accuracy... are always in the
range [0, 1]. If a paper reports such a value as a percentage... divide by 100'. Gap is not
Accuracy/F1/AP/AUC. It is an error metric. The instruction says 'MAE, RMSE, and loss values are NOT
normalised'. Gap is similar to MAE/RMSE in that it's an error/difference. However, the column header
explicitly says 'Gap (%)'. This implies the value 0.001 means 0.001%. To be consistent with
'percentage' handling for benchmark scores, I will treat the reported number as the percentage value
and divide by 100 to get the fraction. Wait, the instruction says 'Accuracy... are always in the
range [0, 1]'. It does not explicitly say Gap must be normalized. But it says 'If a paper reports
such a value as a percentage... divide by 100'. Is Gap 'such a value'? It's a benchmark score. I
will normalize by dividing by 100 to be safe, as 0.001% is a very small gap. Actually, looking at
the values: Linkern Gap is 0.001%. Proposed is 0.001%. This makes sense. If I don't divide, 0.001 is
0.1%. If I divide, 0.00001 is 0.001%. Let's look at the 'Valid (%)' column. 98.11%. If I normalize
Valid, it becomes 0.9811. The instruction focuses on Accuracy/F1/AP/AUC/Hits@K/MRR. Gap is not in
that list. It says 'MAE, RMSE, and loss values are NOT normalised'. Gap is an error metric. I will
NOT normalize Gap, treating it like MAE/RMSE, but keeping the unit as reported (percentage points).
Wait, the instruction says 'value normalisation: Accuracy... are always in the range [0, 1]... NEVER
output values > 1 for these metrics.' It does not mandate normalization for Gap. However, standard
practice for 'Gap' in TSP papers is often reported as a percentage. I will output the raw value from
the table as it is a 'Gap' metric, not a 'Score' metric like Accuracy. But wait, if the header is
'Gap (%)', the value 0.001 is 0.001%. If I output 0.001, it implies 0.1% if the unit is fraction, or
0.001% if the unit is percent. To avoid ambiguity, I will output the number as it appears in the
table, assuming the user understands the unit is %. However, the prompt asks for 'value' as a float.
I will output the float as it appears in the table. Re-reading: 'MAE, RMSE, and loss values are NOT
normalised'. Gap is an error/difference. I will follow the MAE rule and NOT divide by 100. I will
output 0.001.   Correction: The prompt says 'Focus on this metric as the main benchmark result.' and
'value normalisation...'. It lists specific metrics for normalization. Gap is not listed. Therefore,
I do not normalize. I output the value as is.   One more check: 'Linkern Gap (%)' is 0.001. 'Gap
(%)' for proposed is 0.001. These are the values.   I will extract all rows for TSP-100 Gap.
[TSP-200] Extracted Gap (%) values for TSP-200. The table reports Gap as a percentage (e.g., 0.002
means 0.002%). Since the metric is 'Gap' and typically lower is better for optimization gaps, and
the values are small percentages, I have kept them as floats representing the percentage value (e.g.
0.002). However, standard benchmark metrics like Accuracy are normalized to [0,1]. Gap is a loss-
like metric (lower is better). The prompt says 'MAE, RMSE, and loss values are NOT normalised'. Gap
is effectively a loss/error metric. I will output the raw percentage value as a float (e.g. 0.002)
because it is already a small number. If it were 44.2%, I would output 0.442. Here 0.002% is
0.00002. Wait, the table says 'Gap (%)'. The value is 0.002. This likely means 0.002%. So the actual
gap is 0.00002. However, usually in these tables, if the header is 'Gap (%)', the value 0.002 means
0.002 percent. Let's look at Linkern: 0.017% gap. Proposed: 0.002% gap. I will output the value as
the number in the table, assuming the user wants the number as presented or normalized to [0,1] if
it's a score. Gap is not a score in [0,1] usually, it's a percentage error. I will output the value
as the float in the table (0.002) but note that it represents a percentage. Actually, to be safe and
consistent with 'value normalisation' rules for scores, I should check if Gap is considered a score.
It is not. It is an error metric. I will output the value as the number in the table. 0.002. If the
table said 44.2, I would output 0.442. Here 0.002 is already < 1. I will leave it as 0.002.
[Peptides-func] Extracted only the 'Peptides-func' column results as requested. The table reports
mean performance over five runs but does not provide standard deviations, so std is null. All values
are normalized to [0,1] range for AP metric. [Peptides-struct] Extracted only the Peptides-Struct
column as requested. The table reports mean performance over five runs but does not provide standard
deviations, so std is null for all entries. FloydNet is the proposed model. All other models are
baselines with citations provided in the table. [PascalVOC-SP] Extracted only PascalVOC-SP F1
results from Table 1. No standard deviations were reported in the table. All values are normalized
to [0,1] as they are F1 scores. [COCO-SP] Extracted only the COCO-SP column from Table 1 as
requested. The table reports mean performance over five runs but does not provide standard
deviations, so std is null for all entries. All values are normalized to [0,1] as they are F1
scores. [PCQM-Contact] Extracted MRR results for PCQM-Contact from Table 1. All values are
normalized to [0,1]. No standard deviations were reported in the table. The proposed model is
FloydNet. [ZINC] The table provides results for both 'Subset' and 'Full' configurations of ZINC. Per
instructions to use the STANDARD/DEFAULT configuration, the 'Full' dataset results were extracted as
they represent the complete benchmark. The 'Subset' results were ignored. No standard deviations
were reported in the table. [BREC] Extracted all models from Table 1 for the BREC benchmark. The
table reports 'Total (acc. on 400)' which represents the overall accuracy. Values were converted
from percentages to [0,1] range. Note: 'FloydNet-KP' is a hybrid variant of the proposed model,
included as it is part of the 'Ours' section. 'k-FWL 3' and 'k-FWL 4' correspond to the proposed
framework variants mentioned in the text and table as \kfnet{3} and \kfnet{4}.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*