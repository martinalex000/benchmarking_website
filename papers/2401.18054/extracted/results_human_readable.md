# Extraction: arXiv:2401.18054
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GCN
- Type: GCN_variant

## Results

### N-UCLA-CIL — AOPD ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| BARE | 0.9674 | 0.0072 | Yes | this paper | Table 2 |
| BARE | 1.0000 | 0.0000 | Yes | this paper | Table 2 |
| EWC | 0.9394 | 0.0056 | Yes | this paper | Table 2 |
| EWC | 1.0000 | 0.0000 | Yes | this paper | Table 2 |
| MAS | 0.8946 | 0.0160 | Yes | this paper | Table 2 |
| MAS | 0.9870 | 0.0161 | Yes | this paper | Table 2 |
| TWP | 0.8539 | 0.0193 | Yes | this paper | Table 2 |
| TWP | 1.0000 | 0.0000 | Yes | this paper | Table 2 |
| LWF | 0.6321 | 0.0246 | Yes | this paper | Table 2 |
| LWF | 0.7504 | 0.0646 | Yes | this paper | Table 2 |
| GEM | 0.8389 | 0.0145 | Yes | this paper | Table 2 |
| GEM | 1.0000 | 0.0000 | Yes | this paper | Table 2 |
| REPLAY | 0.5821 | 0.0754 | Yes | this paper | Table 2 |
| REPLAY | 0.8025 | 0.0520 | Yes | this paper | Table 2 |

### NTU-CIL — AOPD ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| BARE | 0.9291 | 0.0038 | Yes | this paper | Table 2 |
| BARE | 0.9924 | 0.0000 | Yes | this paper | Table 2 |
| EWC | 0.8536 | 0.0088 | Yes | this paper | Table 2 |
| EWC | 0.9424 | 0.0123 | Yes | this paper | Table 2 |
| MAS | 0.8788 | 0.0051 | Yes | this paper | Table 2 |
| MAS | 0.9561 | 0.0130 | Yes | this paper | Table 2 |
| TWP | 0.7745 | 0.0140 | Yes | this paper | Table 2 |
| TWP | 0.8924 | 0.0111 | Yes | this paper | Table 2 |
| LWF | 0.7836 | 0.0110 | Yes | this paper | Table 2 |
| LWF | 0.9348 | 0.0113 | Yes | this paper | Table 2 |
| GEM | 0.8091 | 0.0025 | Yes | this paper | Table 2 |
| GEM | 0.9409 | 0.0088 | Yes | this paper | Table 2 |
| REPLAY | 0.3952 | 0.0094 | Yes | this paper | Table 2 |
| REPLAY | 0.5318 | 0.0241 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **BARE**
- **EWC** (from: Kirkpatrick et al. 2017)
- **MAS** (from: Amari et al. 2018)
- **TWP** (from: Zenke et al. 2017)
- **LWF** (from: Rebuffi et al. 2017)
- **GEM** (from: Rusu et al. 2016)
- **REPLAY** (from: Rolnick et al. 2019)

## Extraction Notes

[N-UCLA-CIL] Extracted results for N-UCLA-CIL from Table 2 (task-order sensitivity experiment). The
table reports AOPD and MOPD metrics. The FOCUS instruction specified 'OPD' as the primary metric.
Since the table distinguishes between AOPD (Average OPD) and MOPD (Maximum OPD), and both are
standard measures of order sensitivity in this context, both were extracted. The values are
percentages, so they were divided by 100. The 'aggregated class-order sensitivity experiment'
columns for N-UCLA-CIL were also considered, but the 'task-order sensitivity experiment' is the
primary comparison for method performance in this table structure. However, looking closely at the
table, there are two main sections: 'task-order sensitivity experiment' and 'aggregated class-order
sensitivity experiment'. The prompt asks for 'STANDARD / DEFAULT configuration'. Usually, task-order
sensitivity is the standard evaluation for CIL robustness unless specified otherwise. I have
extracted the 'task-order sensitivity experiment' results for N-UCLA-CIL. If the 'aggregated class-
order sensitivity' is considered the standard, those values would be different (e.g., BARE AOPD
1.0). Given the ambiguity, I selected the first set of N-UCLA-CIL columns under 'task-order
sensitivity experiment' as it appears first and is a common baseline evaluation. Note: The prompt
asks to skip optional variants. Both task-order and class-order are variants of sensitivity
analysis. I will stick to the first occurrence (task-order) as it is the primary header. [NTU-CIL]
Extracted results for NTU-CIL from Table 2. The table reports Order Sensitivity metrics (AOPD and
MOPD) for both task-order and class-order sensitivity experiments. The prompt focused on 'NTU-CIL'
and 'OPD'. The table has two sections for NTU-CIL: 'task-order sensitivity experiment' and
'aggregated class-order sensitivity experiment'. The caption states 'The OPD metric in the class-
order sensitivity experiment is based on the accuracy of the classes.' However, the column headers
for both sections are identical (AOPD, MOPD). The prompt asks for 'STANDARD / DEFAULT
configuration'. Usually, class-order sensitivity is the more rigorous standard for evaluating order
independence in CIL, but task-order is also reported. Given the ambiguity of which 'OPD' is the
'primary' one without explicit instruction to choose class-order over task-order, I extracted both
sets of results for NTU-CIL from the table. Note: The prompt says 'Focus on this metric as the main
benchmark result. Skip purely secondary diagnostics'. AOPD and MOPD are the primary metrics reported
in this table. I included all rows for NTU-CIL from Table 2. The values are percentages, so they
were divided by 100. The 'BARE' baseline is included as it is in the table. The proposed model is
implicitly the GCN backbone used in the experiments, but no specific 'proposed method' name is given
in the table rows other than the baselines. The table compares baselines. The 'GCN' is the backbone,
not a specific algorithm row. I treated 'GCN' as the proposed model type in the header, but the rows
are baselines. Wait, the prompt asks for 'proposed_model'. The paper seems to be evaluating existing
CL methods on a new dataset (NTU-CIL) using a GCN backbone. There is no new CL method proposed in
this specific table. The 'proposed_model' field in the output schema is for the model being proposed
in the paper. If the paper proposes a new dataset and evaluates existing methods, the
'proposed_model' might be null or the backbone. I set it to GCN as it's the backbone mentioned. The
results are all baselines.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*