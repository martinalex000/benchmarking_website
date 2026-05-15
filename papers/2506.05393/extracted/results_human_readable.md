# Extraction: Are Large Language Models Good Temporal Graph Learners?
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: TGTalker
- Type: Other

## Results

### Enron — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| TGTalker (Qwen3-1.7B) | 0.1660 | — | No | this paper | Table 1 |
| TGTalker (Qwen3-8B) | 0.1920 | — | No | this paper | Table 1 |
| TGTalker (Qwen2.5-7B) | 0.2000 | — | No | this paper | Table 1 |
| TGTalker (Mistral-7B-v0.3) | 0.1840 | — | No | this paper | Table 1 |
| TGTalker (Llama3-8B) | 0.1930 | — | No | this paper | Table 1 |
| TGTalker (GPT-4.1-mini) | 0.1690 | — | No | this paper | Table 1 |
| TGN | 0.1300 | 0.0660 | Yes | TGN 2020 | Table 1 |
| TNCN | 0.3790 | 0.0810 | Yes | Zhang 2024 | Table 1 |
| GraphMixer | 0.0140 | 0.0020 | Yes | Cong 2022 | Table 1 |
| EdgeBank | 0.1010 | — | Yes | Poursafaei 2022 | Table 1 |
| HTGN | 0.1070 | 0.0090 | Yes | Huang 2021 | Table 1 |
| GCLSTM | 0.1570 | 0.0190 | Yes | Huang 2022 | Table 1 |
| GCN | 0.2320 | 0.0050 | Yes | Kipf 2016 | Table 1 |

### LastFM — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| TGTalker (Qwen3-1.7B) | 0.0660 | — | No | this paper | Table 1 |
| TGTalker (Qwen3-8B) | 0.0690 | — | No | this paper | Table 1 |
| TGTalker (Qwen2.5-7B) | 0.0790 | — | No | this paper | Table 1 |
| TGTalker (Mistral-7B-v0.3) | 0.0670 | — | No | this paper | Table 1 |
| TGTalker (Llama3-8B) | 0.0690 | — | No | this paper | Table 1 |
| TGTalker (GPT-4.1-mini) | 0.0650 | — | No | this paper | Table 1 |
| TGN | 0.0530 | 0.0150 | Yes | tgn2020 | Table 1 |
| TNCN | 0.1560 | 0.0020 | Yes | zhang2024efficient | Table 1 |
| GraphMixer | 0.0870 | 0.0050 | Yes | cong2022we | Table 1 |
| EdgeBank_inf | 0.0200 | — | Yes | poursafaei2022towards | Table 1 |
| EdgeBank_tw | 0.0260 | — | Yes | poursafaei2022towards | Table 1 |
| HTGN (UTG) | 0.0270 | 0.0070 | Yes | htgn2021,huangutg | Table 1 |
| GCLSTM (UTG) | 0.0190 | 0.0010 | Yes | gclstm2022,huangutg | Table 1 |
| GCN (UTG) | 0.0240 | 0.0010 | Yes | kipf2016semi,huangutg | Table 1 |

### Reddit — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| TGTalker (Qwen3-1.7B) | 0.6060 | — | No | this paper | Table 1 |
| TGTalker (Qwen3-8B) | 0.6260 | — | No | this paper | Table 1 |
| TGTalker (Qwen2.5-7B) | 0.6170 | — | No | this paper | Table 1 |
| TGTalker (Mistral-7B-v0.3) | 0.6120 | — | No | this paper | Table 1 |
| TGTalker (Llama3-8B) | 0.6130 | — | No | this paper | Table 1 |
| TGTalker (GPT-4.1-mini) | 0.2250 | — | No | this paper | Table 1 |
| TGN | 0.4990 | 0.0110 | Yes | TGN 2020 | Table 1 |
| TNCN | 0.6960 | 0.0200 | Yes | Zhang 2024 | Table 1 |
| GraphMixer | 0.1360 | 0.0780 | Yes | Cong 2022 | Table 1 |
| EdgeBank | 0.4850 | — | Yes | Poursafaei 2022 | Table 1 |
| HTGN | 0.5330 | 0.0070 | Yes | HTGN 2021 | Table 1 |
| GCLSTM | 0.4670 | 0.0040 | Yes | GCLSTM 2022 | Table 1 |
| GCN | 0.2420 | 0.0050 | Yes | Kipf 2016 | Table 1 |

### UCI — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Qwen3-1.7B | 0.1660 | — | No | this paper | Table 1 |
| Qwen3-8B | 0.1890 | — | No | this paper | Table 1 |
| Qwen2.5-7B | 0.2200 | — | No | this paper | Table 1 |
| Mistral-7B-v0.3 | 0.2120 | — | No | this paper | Table 1 |
| Llama3-8B | 0.2130 | — | No | this paper | Table 1 |
| GPT-4.1-mini | 0.2020 | — | No | this paper | Table 1 |
| TGN | 0.0510 | 0.0110 | Yes | tgn2020 | Table 1 |
| TNCN | 0.2450 | 0.0400 | Yes | zhang2024efficient | Table 1 |
| GraphMixer | 0.0340 | 0.0620 | Yes | cong2022we | Table 1 |
| EdgeBank_infinity | 0.0790 | — | Yes | poursafaei2022towards | Table 1 |
| EdgeBank_tw | 0.2220 | — | Yes | poursafaei2022towards | Table 1 |
| HTGN (UTG) | 0.0380 | 0.0050 | Yes | htgn2021 | Table 1 |
| GCLSTM (UTG) | 0.0130 | 0.0010 | Yes | gclstm2022 | Table 1 |
| GCN (UTG) | 0.0220 | 0.0010 | Yes | kipf2016semi | Table 1 |

### tgbl-wiki — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Qwen3-1.7B | 0.6070 | — | No | this paper | Table 1 |
| Qwen3-8B | 0.6510 | — | No | this paper | Table 1 |
| Qwen2.5-7B | 0.6480 | — | No | this paper | Table 1 |
| Mistral-7B-v0.3 | 0.6040 | — | No | this paper | Table 1 |
| Llama3-8B | 0.6040 | — | No | this paper | Table 1 |
| GPT-4.1-mini | 0.4250 | — | No | this paper | Table 1 |
| TGN | 0.3960 | 0.0600 | Yes | tgn2020 | Table 1 |
| TNCN | 0.7110 | 0.0070 | Yes | zhang2024efficient | Table 1 |
| GraphMixer | 0.1180 | 0.0020 | Yes | cong2022we | Table 1 |
| EdgeBank_inf | 0.4950 | — | Yes | poursafaei2022towards | Table 1 |
| EdgeBank_tw | 0.6000 | — | Yes | poursafaei2022towards | Table 1 |
| HTGN (UTG) | 0.4640 | 0.0050 | Yes | htgn2021,huangutg | Table 1 |
| GCLSTM (UTG) | 0.3740 | 0.0100 | Yes | gclstm2022,huangutg | Table 1 |
| GCN (UTG) | 0.3360 | 0.0090 | Yes | kipf2016semi,huangutg | Table 1 |
| TGTalker (All components) | 0.6490 | — | No | this paper | Table 2 |
| TGTalker (w/o In Context Learning) | 0.6450 | — | No | this paper | Table 2 |
| TGTalker (w/o Temporal Neighbours) | 0.3220 | — | No | this paper | Table 2 |
| TGTalker (w/o Background Set) | 0.6480 | — | No | this paper | Table 2 |
| TGTalker (with no components) | 0.0080 | — | No | this paper | Table 2 |
| TGTalker (nbr = 2) | 0.6490 | — | No | this paper | Table 3 |
| TGTalker (nbr = 0) | 0.3220 | — | No | this paper | Table 3 |
| TGTalker (nbr = 1) | 0.6460 | — | No | this paper | Table 3 |
| TGTalker (nbr = 5) | 0.6520 | — | No | this paper | Table 3 |
| TGTalker (nbr = 10) | 0.6560 | — | No | this paper | Table 3 |

## Baseline Models Identified

- **TGN** (from: tgn2020)
- **TNCN** (from: zhang2024efficient)
- **GraphMixer** (from: cong2022we)
- **EdgeBank_inf** (from: poursafaei2022towards)
- **EdgeBank_tw** (from: poursafaei2022towards)
- **HTGN (UTG)** (from: htgn2021,huangutg)
- **GCLSTM (UTG)** (from: gclstm2022,huangutg)
- **GCN (UTG)** (from: kipf2016semi,huangutg)
- **EdgeBank** (from: Poursafaei 2022)
- **HTGN** (from: HTGN 2021)
- **GCLSTM** (from: GCLSTM 2022)
- **GCN** (from: Kipf 2016)
- **EdgeBank_infinity** (from: poursafaei2022towards)

## Extraction Notes

[tgbl-wiki] Extracted all rows from Table 1, Table 2, and Table 3 for the 'tgbl-wiki' dataset. Table
1 contains the main comparison with baselines. Tables 2 and 3 contain ablation studies for the
proposed TGTalker model. All values are MRR. Standard deviations are extracted where provided (only
for baselines in Table 1). LLM models use external pre-trained data. [Reddit] The paper focuses on
Temporal Link Prediction using MRR as the primary metric. The user requested F1 for the Reddit
dataset. However, the paper does not report F1 scores for Reddit; it only reports MRR. Per the
instructions to extract quantitative results reported in the paper, I have extracted the MRR
results. The F1 metric is not present in the provided text or tables for the Reddit dataset. I have
included all models from Table 1 for the Reddit column. [LastFM] Extracted all rows for the LastFM
dataset from Table 1. The proposed model TGTalker uses various LLM backbones; all are considered
part of the proposed method family but have different parameter counts. Since the paper does not
specify exact parameter counts for the LLMs used in the prompt context (only model names like
Qwen3-1.7B), params_millions is set to null. The 'uses_external_data' is set to true for TGTalker
because it leverages pre-trained LLMs. Standard deviations are extracted where provided (for TGNN
baselines). Values are already in [0,1] range as MRR. [UCI] Extracted all rows from Table 1
corresponding to the 'UCI' dataset column. The primary metric MRR is used for all entries. Standard
deviations are extracted where provided (for TGNN baselines). LLMs are marked as using external data
due to pre-training. No standard deviations are reported for LLMs in the table. [Enron] Extracted
all models for the Enron dataset from Table 1. The primary metric MRR is used. TGTalker variants are
treated as proposed models. Baselines are extracted with their reported standard deviations where
available. EdgeBank is reported as a single run (no std). All values are normalized to [0,1] range
as they are MRR scores.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*