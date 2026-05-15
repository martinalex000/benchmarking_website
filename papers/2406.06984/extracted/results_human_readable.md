# Extraction: arXiv:2406.06984
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: SortMPNN
- Type: GNN

## Results

### Mutag — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.8940 | 0.0560 | Yes | Xu et al. 2018 | Table 1 |
| GCN | 0.8560 | 0.0580 | Yes | Kipf & Welling 2017 | Table 1 |
| GraphSage | 0.8510 | 0.0760 | Yes | Hamilton et al. 2017 | Table 1 |
| SortMPNN | 0.9099 | 0.0620 | No | this paper | Table 1 |
| AdaptMPNN | 0.9041 | 0.0610 | Yes | this paper | Table 1 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.8270 | 0.0170 | Yes | Xu et al. 2018 | Table 1 |
| GCN | 0.8020 | 0.0200 | Yes | Kipf & Welling 2017 | Table 1 |
| GraphSage | 0.7770 | 0.0150 | Yes | Hamilton et al. 2017 | Table 1 |
| SortMPNN | 0.8355 | 0.0182 | No | this paper | Table 1 |
| AdaptMPNN | 0.8277 | 0.0172 | Yes | this paper | Table 1 |

### NCI109 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.8220 | 0.0160 | Yes | Xu et al. 2018 | Table 1 |
| SortMPNN | 0.8275 | 0.0160 | No | this paper | Table 1 |
| AdaptMPNN | 0.8326 | 0.0086 | Yes | this paper | Table 1 |

### PTC — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.6460 | 0.0700 | Yes | Xu et al. 2018 | Table 1 |
| GCN | 0.6420 | 0.0430 | Yes | Kipf & Welling 2017 | Table 1 |
| GraphSage | 0.6390 | 0.0770 | Yes | Hamilton et al. 2017 | Table 1 |
| SortMPNN | 0.6631 | 0.0673 | No | this paper | Table 1 |
| AdaptMPNN | 0.6687 | 0.0537 | Yes | this paper | Table 1 |

### Proteins — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.7620 | 0.0280 | Yes | Xu et al. 2018 | Table 1 |
| GCN | 0.7600 | 0.0320 | Yes | Kipf & Welling 2017 | Table 1 |
| GraphSage | 0.7590 | 0.0320 | Yes | Hamilton et al. 2017 | Table 1 |
| SortMPNN | 0.7646 | 0.0368 | No | this paper | Table 1 |
| AdaptMPNN | 0.7512 | 0.0364 | Yes | this paper | Table 1 |

### peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SortMPNN | 0.6940 | 0.0049 | No | this paper | Table 1 |
| AdaptMPNN | 0.6934 | 0.0099 | Yes | this paper | Table 1 |
| GINE | 0.6621 | 0.0067 | Yes | Hu* 2020 | Table 1 |
| GCN | 0.6860 | 0.0050 | Yes | kipf 2017 | Table 1 |
| GatedGCN | 0.6765 | 0.0047 | Yes | bresson 2018 | Table 1 |

### peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SortMPNN | 0.2464 | 0.0024 | No | this paper | Table 1 |
| AdaptMPNN | 0.2484 | 0.0034 | Yes | this paper | Table 1 |
| GINE | 0.2473 | 0.0017 | Yes | Hu* 2020 | Table 1 |
| GCN | 0.2460 | 0.0007 | Yes | kipf 2017 | Table 1 |
| GatedGCN | 0.2477 | 0.0009 | Yes | bresson 2018 | Table 1 |

## Baseline Models Identified

- **GIN** (from: Xu et al. 2018)
- **GCN** (from: Kipf & Welling 2017)
- **GraphSage** (from: Hamilton et al. 2017)
- **AdaptMPNN**
- **GINE** (from: Hu* 2020)
- **GatedGCN** (from: bresson 2018)

## Extraction Notes

[TUdatasets] Extracted all rows from Table 1 for TUdatasets. Values were converted from percentages
to [0,1] range. GCN on NCI109 was marked as NA in the table and thus excluded. SortMPNN is
identified as the proposed model based on the caption 'Best in bold' and its superior performance in
most columns, though AdaptMPNN is also a strong competitor. The paper does not explicitly name the
proposed model in the provided text snippet, but SortMPNN is the only one with bolded best results
across multiple datasets, suggesting it is the primary contribution. If AdaptMPNN is also proposed,
the is_proposed flag would need adjustment, but typically the first/best listed is the main one.
Given the ambiguity, I marked SortMPNN as proposed. If both are proposed, the schema allows only one
'proposed_model' entry, so I selected the one with the most bolded bests. [LRGB] Extracted results
for LRGB datasets (peptides-func and peptides-struct) from Table 1. The table caption indicates
'LRGB results'. The primary metric for peptides-struct is MAE and for peptides-func is AP. All
values were normalized to [0,1] where applicable (AP is already in [0,1]). Standard deviations were
parsed from the '±' notation. Bold/underlined indicators were noted but values extracted as is.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*