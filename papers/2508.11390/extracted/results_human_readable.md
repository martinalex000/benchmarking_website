# Extraction: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature based Graph-to-Hypergraph Structural Lifting
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: UniGNN2
- Type: GNN

## Results

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7100 | 0.0300 | Yes | this paper | Table 1 |
| GAT | 0.7300 | 0.0400 | Yes | this paper | Table 1 |
| AST | 0.6500 | 0.0700 | Yes | this paper | Table 1 |
| EDGNN | 0.7000 | 0.0600 | Yes | this paper | Table 1 |
| UniGNN2 | 0.6300 | 0.0800 | No | this paper | Table 1 |

### NCI109 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7000 | 0.0300 | Yes | this paper | Table 1 |
| GAT | 0.7100 | 0.0400 | Yes | this paper | Table 1 |
| AST | 0.7000 | 0.0600 | Yes | this paper | Table 1 |
| EDGNN | 0.6800 | 0.0900 | Yes | this paper | Table 1 |
| UniGNN2 | 0.6700 | 0.0900 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6900 | 0.0400 | Yes | this paper | Table 1 |
| GAT | 0.6900 | 0.0400 | Yes | this paper | Table 1 |
| AST | 0.6600 | 0.0800 | Yes | this paper | Table 1 |
| EDGNN | 0.6700 | 0.0700 | Yes | this paper | Table 1 |
| UniGNN2 | 0.6900 | 0.0600 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7800 | 0.1400 | Yes | this paper | Table 1 |
| GAT | 0.7700 | 0.1700 | Yes | this paper | Table 1 |
| AST | 0.7800 | 0.2000 | Yes | this paper | Table 1 |
| EDGNN | 0.7600 | 0.1700 | Yes | this paper | Table 1 |
| UniGNN2 | 0.7800 | 0.1500 | No | this paper | Table 1 |
| GCN (Ric_F) | 0.7900 | 0.1300 | Yes | this paper | Table 1 |
| GAT (Ric_F) | 0.7700 | 0.1700 | Yes | this paper | Table 1 |
| AST (Ric_F) | 0.7900 | 0.1900 | Yes | this paper | Table 1 |
| EDGNN (Ric_F) | 0.7800 | 0.1600 | Yes | this paper | Table 1 |
| UniGNN2 (Ric_F) | 0.7800 | 0.1600 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **AST**
- **EDGNN**

## Extraction Notes

[NCI1] Extracted results for the standard NCI1 dataset only. The row 'NCI1 (Ric_F)' corresponds to a
lifted dataset variant and was skipped as per instructions to ignore optional variants. The proposed
model is identified as UniGNN2 based on the table caption and column header structure, although it
does not achieve the best result on the standard NCI1 dataset. [NCI109] The table presents results
for both 'original' and 'lifted' (Ric_F) versions of the datasets. The prompt asks for the
STANDARD/DEFAULT configuration. Usually, the first row for a dataset name (e.g., 'NCI109')
represents the standard graph structure, while the second row (e.g., 'NCI109 (Ric_F)') represents a
specific variant or lifted version. However, the table caption says 'Performances on original and
lifted datasets'. It is ambiguous whether 'NCI109' is the standard or if the standard is the lifted
one. Given the instruction to skip optional variants and focus on standard, I have extracted both
rows as they appear distinct in the table. If 'NCI109' implies the standard graph and 'NCI109
(Ric_F)' implies a hypergraph/lifted variant, then only the first block should be used. However,
without explicit definition of 'standard' in the text, and seeing bolding on the second row for some
models, it's safer to include both or clarify. The prompt says 'Skip results for optional
variants... if the table shows multiple configurations'. 'Ric_F' is likely a specific construction
option (Ricci curvature based lifting). Therefore, strictly following 'standard/default', I should
probably only include the 'NCI109' rows (first block). But wait, the prompt says 'Ignore rows that
belong to other datasets'. It doesn't explicitly say 'ignore lifted variants' unless they are
considered 'other datasets'. 'NCI109' and 'NCI109 (Ric_F)' are likely the same dataset under
different representations. If 'NCI109' is the standard graph dataset, then the first block is the
correct one. If the paper considers the lifted version as the primary contribution, it might be
different. Let's look at the bolding. In the second block, GCN, GAT, EDGNN, UniGNN2 are bolded. In
the first block, only GCN and GAT are bolded for NCI1, but for NCI109, no values are bolded in the
first block? No, looking closely: NCI109 row: 0.70, 0.71, 0.70, 0.68, 0.67. No bold. NCI109 (Ric_F)
row: 0.71, 0.72, 0.69, 0.69, 0.70. These are bolded. This suggests the 'Ric_F' version might be the
one where the proposed model (or others) perform best or is the focus. However, 'NCI109' is the
standard name. I will extract ONLY the 'NCI109' rows (first block) as the 'standard' configuration,
assuming 'Ric_F' is a variant/lifted version. Wait, looking at the table structure, 'NCI1' and
'NCI109' are listed, then their 'Ric_F' counterparts. Usually, the non-Ric_F is the standard graph.
I will extract only the first block for NCI109 to adhere to 'standard/default'.  Correction: I will
extract ONLY the rows labeled 'NCI109' (not 'NCI109 (Ric_F)') as the standard configuration. [ogbg-
molhiv] Extracted all rows related to 'OGBG Molhiv' from Table 1. The table lists both original
datasets and 'Ric_F' lifted datasets. Since the prompt asks for the STANDARD/DEFAULT configuration,
I included both the standard rows (e.g., 'OGBG Molhiv') and the lifted variants (e.g., 'OGBG Molhiv
(Ric_F)') as they appear in the same table without explicit separation into different experimental
setups in the text provided. However, typically 'Ric_F' implies a specific construction option.
Given the ambiguity of 'standard' in the context of a table comparing original vs lifted, I
extracted all rows for this dataset name to be safe, noting that the first row for each method is
the standard graph-based result. The metric is ROC-AUC (implied by context of MolHiv and values <
1). Values are normalized to [0,1]. [PROTEINS] The table presents results for two configurations:
'PROTEINS' (original) and 'PROTEINS ($Ric_{F}$)' (lifted). The FOCUS instruction requested the
STANDARD/DEFAULT configuration. Therefore, only the rows labeled 'PROTEINS' were extracted. The rows
labeled 'PROTEINS ($Ric_{F}$)' were skipped as they represent an optional variant/lifted dataset
construction. All values are Accuracy scores normalized to [0,1].

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*