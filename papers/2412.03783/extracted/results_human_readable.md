# Extraction: arXiv:2412.03783
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: CTAN
- Type: GNN

## Results

### TGBL-Coin — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| JODIE | 0.7130 | 0.0280 | Yes | this paper | Table 1 |
| DyRep | 0.6880 | 0.0070 | Yes | this paper | Table 1 |
| TGN | 0.7380 | 0.0070 | Yes | this paper | Table 1 |
| TGAT | 0.7480 | 0.0250 | Yes | this paper | Table 1 |
| CTAN | 0.7090 | 0.0030 | No | this paper | Table 1 |

### TGBL-Wiki — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| JODIE | 0.2610 | 0.1230 | Yes | this paper | Table 2 |
| DyRep | 0.2630 | 0.0050 | Yes | this paper | Table 2 |
| TGN | 0.5770 | 0.0150 | Yes | this paper | Table 2 |
| TGAT | 0.2820 | 0.0220 | Yes | this paper | Table 2 |
| CTAN | 0.6110 | 0.0110 | No | this paper | Table 2 |

## Baseline Models Identified

- **JODIE**
- **DyRep**
- **TGN**
- **TGAT**

## Extraction Notes

[TGBL-Wiki] Extracted only Test MRR for TGBL-Wiki as requested. Table 2 (labeled table:tgbl-wiki)
provided clear values for all models. [TGBL-Coin] Extracted only the 'Test' column for MRR on the
TGBL-Coin dataset as requested. The proposed model is identified as CTAN based on the text
describing its specific hyperparameters. [PascalVOC-SP] The paper mentions the use of a temporal
version of the PascalVOC-SP graph (T-PascalVOC) in the text and lists it in the dataset statistics
table (Table 4), but no performance results (F1 or otherwise) for this specific dataset are provided
in any of the provided tables. The tables only contain results for TGBL-Wiki, SBM Community-Based
Graph, and TGBL-Coin.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*