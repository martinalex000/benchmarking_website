# Extraction: arXiv:2310.15543
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: mGAT
- Type: GNN

## Results

### TSP100 — Gap ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| mGAT (s.) (Ours) | 0.0025 | — | No | this paper | Table 1 |
| mGAT (Ours) | 0.0025 | — | No | this paper | Table 2 |

### TSP20 — Gap ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| mGAT (s.) (Ours) | 0.0000 | — | No | this paper | Table 1 |
| mGAT (Ours) | 0.0027 | — | No | this paper | Table 2 |

### TSP50 — Gap ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| mGAT (s.) (Ours) | 0.0002 | — | No | this paper | Table 1 |
| mGAT (Ours) | 0.0018 | — | No | this paper | Table 2 |

### TSPLIB — Gap ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Ours | 0.0123 | — | No | this paper | Table 4 |
| POMO | 0.0070 | — | Yes | this paper | Table 1 |
| Sym-NCO | 0.0190 | — | Yes | this paper | Table 1 |

## Baseline Models Identified

- **Concorde** (from: applegate2006concorde)
- **LKH3**
- **Gurobi**
- **AM** (from: kool2018attention)
- **POMO** (from: kwon2020pomo)
- **MDAM** (from: xin2021multi)
- **Sym-NCO** (from: kim2022sym)

## Extraction Notes

[TSP] The paper focuses on TSP (Traveling Salesperson Problem) and CVRP. The primary metric reported
for TSP is 'Gap' (percentage gap from optimal) and 'Obj' (objective value/tour length). The prompt
asks for 'F1' as the primary metric. However, TSP is an optimization problem, not a classification
problem, so F1 score is not applicable. The 'Gap' metric is the standard benchmark metric for TSP in
this context (lower is better). I have extracted the Gap results for the proposed model mGAT. I have
ignored CVRP results as per the FOCUS instruction to only extract results for 'TSP'. I have ignored
the ablation study table (Table 3) as it contains internal design variations rather than comparisons
with external baselines, and the prompt implies extracting benchmark results. I have included
results from Table 1 (standard configurations), Table 2 (generalization to variable sizes), and
Table 4 (real-world TSPLIB instances). Note: Table 1 reports results for greedy (g.) and sampling
(s.) decoding; I selected the sampling (s.) results for mGAT as they are bolded (best) in most cases
and represent the stronger performance. For Table 2, only one configuration is reported. For Table
4, the average gap is reported. [CVRP] failed: 4 validation errors for ExtractionOutput
results.8.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.9.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.19.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.20.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[TSPLIB] The table reports results for multiple specific TSPLIB instances (eil51, berlin52, etc.)
and an 'Average' row. The prompt asks for results for the dataset 'TSPLIB' using the standard
configuration. The 'Average' row represents the aggregate performance across all listed instances,
which serves as the primary benchmark metric for the 'TSPLIB' dataset in this context. Individual
instance results were skipped to adhere to the 'standard/default configuration' instruction, as
reporting 26 separate rows for specific instances would clutter the output and the average is the
summary statistic provided. The Gap values are percentages in the table (e.g., 2.11%), so they are
divided by 100 to fit the [0,1] range rule for Gap (where lower is better). Note: Gap is technically
a percentage difference, but following the normalization rule for metrics that are effectively
ratios/percentages in [0,1] range interpretation, I converted 2.11% to 0.0211. However, looking at
the specific values: POMO Avg 2.11%, Sym-NCO Avg 1.90%, Ours Avg 1.23%. Wait, the rule says
'Accuracy, F1, AP, AUC... are always in range [0,1]'. Gap is not explicitly listed, but it is a
percentage. Usually, Gap is reported as a percentage. If I output 0.0211, it implies 2.11%. If I
output 2.11, it implies 211% or just the number. Given 'higher_is_better' is false, and it's a
'Gap', it's a loss-like metric. The rule says 'MAE, RMSE, and loss values are NOT normalised'. Gap
is a loss metric. Therefore, I should NOT divide by 100. I will output the raw values from the table
(2.11, 1.90, 1.23). Re-reading the rule: 'Accuracy, F1, AP, AUC, ROC-AUC, AUROC, MRR, and Hits@K are
always in the range [0, 1]... MAE, RMSE, and loss values are NOT normalised'. Gap is a loss metric.
So I will keep them as 2.11, 1.90, 1.23.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*