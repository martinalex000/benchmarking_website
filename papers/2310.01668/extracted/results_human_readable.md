# Extraction: arXiv:2310.01668
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: LASER
- Type: GNN

## Results

### ENZYMES — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| None | 0.2873 | 0.0530 | Yes | this paper | Table 1 |
| DiffWire | 0.2853 | 0.0447 | Yes | this paper | Table 1 |
| GTR | 0.2633 | 0.0582 | Yes | this paper | Table 1 |
| SDRF | 0.3057 | 0.0619 | Yes | this paper | Table 1 |
| FOSR | 0.2860 | 0.0525 | Yes | this paper | Table 1 |
| BORF | 0.3050 | 0.0659 | Yes | this paper | Table 1 |
| LASER | 0.3433 | 0.0694 | No | this paper | Table 1 |

### IMDB-BINARY — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| None | 0.6428 | 0.0199 | Yes | this paper | Table 1 |
| DiffWire | 0.5900 | 0.0385 | Yes | this paper | Table 1 |
| GTR | 0.5256 | 0.0410 | Yes | this paper | Table 1 |
| SDRF | 0.5829 | 0.0320 | Yes | this paper | Table 1 |
| FOSR | 0.6040 | 0.0585 | Yes | this paper | Table 1 |
| BORF | 0.6082 | 0.0388 | Yes | this paper | Table 1 |
| LASER | 0.6433 | 0.0330 | No | this paper | Table 1 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| None | 0.7474 | 0.0595 | Yes | this paper | Table 1 |
| DiffWire | 0.8042 | 0.0971 | Yes | this paper | Table 1 |
| GTR | 0.7863 | 0.0620 | Yes | this paper | Table 1 |
| SDRF | 0.7453 | 0.0536 | Yes | this paper | Table 1 |
| FOSR | 0.7590 | 0.0721 | Yes | this paper | Table 1 |
| BORF | 0.8168 | 0.0796 | Yes | this paper | Table 1 |
| LASER | 0.8220 | 0.0673 | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| None | 0.3234 | 0.0006 | Yes | this paper | Table 1 |
| SDRF | 0.3249 | 0.0006 | Yes | this paper | Table 1 |
| GTR | 0.3007 | 0.0022 | Yes | this paper | Table 1 |
| FOSR | 0.2783 | 0.0008 | Yes | this paper | Table 1 |
| LASER | 0.3275 | 0.0011 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| None | 0.6429 | 0.0200 | Yes | this paper | Table 1 |
| DiffWire | 0.7271 | 0.0295 | Yes | this paper | Table 1 |
| GTR | 0.7230 | 0.0466 | Yes | this paper | Table 1 |
| SDRF | 0.6871 | 0.0423 | Yes | this paper | Table 1 |
| FOSR | 0.7164 | 0.0343 | Yes | this paper | Table 1 |
| BORF | 0.6841 | 0.0412 | Yes | this paper | Table 1 |
| LASER | 0.7438 | 0.0344 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| SDRF | 0.5947 | 0.0035 | Yes | this paper | Table 1 |
| GTR | 0.5075 | 0.0029 | Yes | this paper | Table 1 |
| FOSR | 0.5947 | 0.0027 | Yes | this paper | Table 1 |
| BORF | 0.6012 | 0.0031 | Yes | this paper | Table 1 |
| LASER | 0.6440 | 0.0010 | No | this paper | Table 1 |
| Random | 0.4796 | 0.0067 | Yes | this paper | Table 2 |
| LASER - Not Equivariant | 0.6385 | 0.0048 | Yes | this paper | Table 3 |
| GCN-FOSR-R | 0.4629 | 0.0071 | Yes | this paper | Table 4 |
| GCN-SDRF-R | 0.5851 | 0.0033 | Yes | this paper | Table 4 |
| GCN-LASER | 0.6440 | 0.0010 | No | this paper | Table 4 |
| GIN | 0.5799 | 0.0006 | Yes | this paper | Table 4 |
| GIN-FOSR-R | 0.4864 | 0.0054 | Yes | this paper | Table 4 |
| GIN-SDRF-R | 0.6131 | 0.0084 | Yes | this paper | Table 4 |
| GIN-LASER | 0.6489 | 0.0074 | No | this paper | Table 4 |
| GAT | 0.5800 | 0.0061 | Yes | this paper | Table 4 |
| GAT-FOSR-R | 0.4515 | 0.0044 | Yes | this paper | Table 4 |
| GAT-SDRF-R | 0.5756 | 0.0037 | Yes | this paper | Table 4 |
| GAT-LASER | 0.6271 | 0.0052 | No | this paper | Table 4 |
| SAGE | 0.5971 | 0.0041 | Yes | this paper | Table 4 |
| SAGE-FOSR-R | 0.4678 | 0.0068 | Yes | this paper | Table 4 |
| SAGE-SDRF-R | 0.5892 | 0.0040 | Yes | this paper | Table 4 |
| SAGE-LASER | 0.6464 | 0.0032 | No | this paper | Table 4 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| None | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| SDRF | 0.3404 | 0.0015 | Yes | this paper | Table 1 |
| GTR | 0.3618 | 0.0010 | Yes | this paper | Table 1 |
| FOSR | 0.3078 | 0.0026 | Yes | this paper | Table 1 |
| BORF | 0.3374 | 0.0011 | Yes | this paper | Table 1 |
| LASER | 0.3043 | 0.0019 | No | this paper | Table 1 |
| Random | 0.3382 | 0.0019 | Yes | this paper | Table 2 |
| LASER - Not Equivariant | 0.3162 | 0.0032 | Yes | this paper | Table 3 |
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 4 |
| GCN-FOSR-R | 0.3078 | 0.0026 | Yes | this paper | Table 4 |
| GCN-SDRF-R | 0.3404 | 0.0015 | Yes | this paper | Table 4 |
| GCN-LASER | 0.3043 | 0.0019 | No | this paper | Table 4 |
| GIN | 0.3493 | 0.0007 | Yes | this paper | Table 4 |
| GIN-FOSR-R | 0.2966 | 0.0024 | Yes | this paper | Table 4 |
| GIN-SDRF-R | 0.3394 | 0.0012 | Yes | this paper | Table 4 |
| GIN-LASER | 0.3078 | 0.0026 | No | this paper | Table 4 |
| GAT | 0.3506 | 0.0011 | Yes | this paper | Table 4 |
| GAT-FOSR-R | 0.3074 | 0.0029 | Yes | this paper | Table 4 |
| GAT-SDRF-R | 0.3422 | 0.0008 | Yes | this paper | Table 4 |
| GAT-LASER | 0.2971 | 0.0037 | No | this paper | Table 4 |
| SAGE | 0.3480 | 0.0007 | Yes | this paper | Table 4 |
| SAGE-FOSR-R | 0.2986 | 0.0013 | Yes | this paper | Table 4 |
| SAGE-SDRF-R | 0.3408 | 0.0011 | Yes | this paper | Table 4 |
| SAGE-LASER | 0.3004 | 0.0032 | No | this paper | Table 4 |

## Baseline Models Identified

- **None**
- **DiffWire**
- **GTR**
- **SDRF**
- **FOSR**
- **BORF**
- **GCN** (from: Kipf & Welling 2016)
- **GIN** (from: Xu et al. 2018)
- **GAT** (from: Veličković et al. 2017)
- **GraphSAGE** (from: Hamilton et al. 2017)
- **Random Rewiring**
- **GCN-FOSR-R**
- **GCN-SDRF-R**
- **GIN-FOSR-R**
- **GIN-SDRF-R**
- **GAT-FOSR-R**
- **GAT-SDRF-R**
- **SAGE**
- **SAGE-FOSR-R**
- **SAGE-SDRF-R**

## Extraction Notes

[REDDIT-BINARY] failed: 1 validation error for ExtractionOutput results.1.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type [IMDB-BINARY] Extracted only IMDB-BINARY results
from Table 1. Values converted from percentages to [0,1] range. Standard deviations parsed
correctly. All rows included as per instructions. [MUTAG] Extracted only MUTAG results as requested.
Values were converted from percentages to [0,1] range. Standard deviations were parsed from the
'mean ± std' format. [ENZYMES] Extracted Accuracy results for ENZYMES dataset from Table 1. Values
were percentages in the table (e.g., 34.333) and were divided by 100 to fit the [0,1] range as per
instructions. Standard deviations were parsed from the 'mean ± std' format. [PROTEINS] Extracted
only the PROTEINS column from Table 1. Values were converted from percentages to [0,1] range.
Standard deviations were parsed from the ± notation. [COLLAB] failed: 1 validation error for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-func] Extracted all Peptides-func AP results
from Table 1, Table 2, Table 3, and Table 4. Table 1 and Table 4 contain overlapping results for the
main LASER vs baselines comparison (Table 1 seems to be the main result table, Table 4 breaks it
down by MPNN backbone). Table 2 shows an ablation against random rewiring. Table 3 shows an ablation
against non-equivariant implementation. All values were normalized to [0,1] range. Standard
deviations were parsed from the ± notation. [Peptides-struct] Extracted all Peptides-struct MAE
results from Table 1, Table 2, Table 3, and Table 4. Table 1 and Table 4 contain overlapping results
for the main LASER model (GCN-LASER) and baselines (None/SDRF/FOSR/BORF vs GCN/SDRF-R/FOSR-R). Table
2 and Table 3 contain ablation results for LASER vs Random and Equivariant vs Non-Equivariant. All
values are normalized to [0, 1] range where applicable (MAE is not normalized but < 1 here).
Standard deviations were parsed from 'value ± std' format. [PCQM-Contact] Extracted only PCQM-
Contact MRR results from Table 1. BORF row contains 'TIMEOUT' for PCQM-Contact, so it was excluded
from quantitative results. Other tables did not contain PCQM-Contact MRR results. [PascalVOC-SP] The
paper contains tables for TUDatasets (Table 1), Peptides (Table 2, 3, 4, 6), and Scalability/Times
(Table 5). Table 5 mentions 'PascalVOC-SP' in its caption and row labels, but it only reports
'Rewiring Time' (e.g., 4m 3s for FOSR, 31m 30s for SDRF, 9m 6s for LASER). It does not report any
performance metrics (such as F1, Accuracy, etc.) for PascalVOC-SP. The primary performance results
table (Table 4) only covers Peptides-func and Peptides-struct. Therefore, no quantitative
performance results for PascalVOC-SP could be extracted.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*