# Extraction: Toward a Graph Foundation Model: \\ Pre-Training Transformers With Random Walks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: MEDIUM

## Proposed Model: RWPT
- Type: GNN

## Results

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Our loss | 0.7546 | 0.0045 | No | this paper | Table 1 |
| DGI | 0.7437 | 0.0088 | Yes | Velickovic 2019 | Table 1 |
| GraphPrompt | 0.7445 | 0.0060 | Yes | this paper | Table 1 |
| MaskGAE | 0.7487 | 0.0043 | Yes | this paper | Table 1 |
| Context prediction | 0.7546 | 0.0045 | No | this paper | Table 2 |
| + Token reconstruction | 0.7525 | 0.0071 | No | this paper | Table 2 |
| + Position reconstruction | 0.7469 | 0.0043 | No | this paper | Table 2 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5803 | — | Yes | this paper | Table 1 |
| GCN | 0.7565 | — | Yes | this paper | Table 1 |
| GIN | 0.7359 | — | Yes | this paper | Table 1 |
| GAT | 0.7624 | — | Yes | this paper | Table 1 |
| DGI | 0.7210 | — | Yes | this paper | Table 1 |
| BGRL | 0.7120 | — | Yes | this paper | Table 1 |
| GraphMAE | 0.7310 | — | Yes | this paper | Table 1 |
| GIANT | 0.7513 | — | Yes | this paper | Table 1 |
| GFT | 0.7862 | — | Yes | Wang 2024 | Table 1 |
| RWPT | 0.7930 | — | No | this paper | Table 1 |
| RWPT (Pre-Train w/ all) | 0.7930 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ Arxiv + FB15k237 + ChEMBL) | 0.7869 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ Arxiv) | 0.7663 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ FB15k237) | 0.7371 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ ChEMBL) | 0.7034 | — | No | this paper | Table 2 |
| RWPT (Context loss) | 0.7802 | 0.0037 | No | this paper | Table 3 |
| GraphPrompt | 0.7497 | 0.0035 | Yes | this paper | Table 3 |
| MaskGAE | 0.7751 | 0.0028 | Yes | this paper | Table 3 |
| RWPT (Context prediction) | 0.7802 | 0.0037 | No | this paper | Table 4 |
| RWPT (+ Token reconstruction) | 0.7818 | 0.0052 | No | this paper | Table 4 |
| RWPT (+ Position reconstruction) | 0.7661 | 0.0044 | No | this paper | Table 4 |

### FB15k237 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.8739 | — | Yes | this paper | Table 1 |
| GCN | 0.8222 | — | Yes | this paper | Table 1 |
| GIN | 0.8321 | — | Yes | this paper | Table 1 |
| GAT | 0.8893 | — | Yes | this paper | Table 1 |
| DGI | 0.8134 | — | Yes | this paper | Table 1 |
| BGRL | 0.8066 | — | Yes | this paper | Table 1 |
| GraphMAE | 0.8530 | — | Yes | this paper | Table 1 |
| GIANT | 0.8745 | — | Yes | this paper | Table 1 |
| GFT | 0.8972 | — | Yes | this paper | Table 1 |
| RWPT | 0.9523 | — | No | this paper | Table 1 |

### HIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.6637 | — | Yes | this paper | Table 1 |
| GCN | 0.6484 | — | Yes | this paper | Table 1 |
| GIN | 0.6686 | — | Yes | this paper | Table 1 |
| GAT | 0.6554 | — | Yes | this paper | Table 1 |
| DGI | 0.5962 | — | Yes | this paper | Table 1 |
| BGRL | 0.6395 | — | Yes | this paper | Table 1 |
| GraphMAE | 0.6104 | — | Yes | this paper | Table 1 |
| GIANT | 0.6544 | — | Yes | this paper | Table 1 |
| GFT | 0.7267 | — | Yes | Wang 2024 | Table 1 |
| RWPT | 0.7515 | — | No | this paper | Table 1 |
| RWPT (Pre-Train w/ Arxiv) | 0.7346 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ FB15k237) | 0.7357 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ ChEMBL) | 0.7485 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ three) | 0.7403 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ all) | 0.7515 | — | No | this paper | Table 2 |
| RWPT (Walk k=16, l=2) | 0.7524 | — | No | this paper | Table 3 |
| RWPT (Walk k=4, l=4) | 0.7578 | — | No | this paper | Table 3 |
| RWPT (Walk k=8, l=4) | 0.7403 | — | No | this paper | Table 3 |
| RWPT (Walk k=4, l=8) | 0.7070 | — | No | this paper | Table 3 |
| RWPT (Walk k=8, l=8) | 0.7514 | — | No | this paper | Table 3 |
| RWPT (Neighbor [4,4,2]) | 0.7178 | — | No | this paper | Table 3 |
| RWPT (Neighbor [8,4]) | 0.7281 | — | No | this paper | Table 3 |
| RWPT (Our model) | 0.7515 | 0.0239 | No | this paper | Table 4 |
| RWPT (Edge feat. input) | 0.7315 | 0.0295 | No | this paper | Table 4 |
| RWPT (Full attn. mask) | 0.7342 | 0.0343 | No | this paper | Table 4 |

### PCBA — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.7230 | — | Yes | this paper | Table 1 |
| GCN | 0.7132 | — | Yes | this paper | Table 1 |
| GIN | 0.7012 | — | Yes | this paper | Table 1 |
| GAT | 0.7269 | — | Yes | this paper | Table 1 |
| DGI | 0.6331 | — | Yes | this paper | Table 1 |
| BGRL | 0.6709 | — | Yes | this paper | Table 1 |
| GraphMAE | 0.6330 | — | Yes | this paper | Table 1 |
| GIANT | 0.6149 | — | Yes | this paper | Table 1 |
| GFT | 0.7790 | — | Yes | Wang 2024 | Table 1 |
| RWPT | 0.8103 | — | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RWPT (Walk, k=4, l=8) | 0.2561 | — | No | this paper | Table 1 (Sampler Ablation) |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.6866 | — | Yes | this paper | Table 1 |
| GCN | 0.7561 | — | Yes | this paper | Table 1 |
| GIN | 0.6951 | — | Yes | this paper | Table 1 |
| GAT | 0.7486 | — | Yes | this paper | Table 1 |
| DGI | 0.7313 | — | Yes | this paper | Table 1 |
| BGRL | 0.7529 | — | Yes | this paper | Table 1 |
| GraphMAE | 0.7432 | — | Yes | this paper | Table 1 |
| GIANT | 0.7231 | — | Yes | this paper | Table 1 |
| GFT | 0.7719 | — | Yes | Wang 2024 | Table 1 |
| RWPT | 0.7497 | — | No | this paper | Table 1 |

### Tox21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RWPT | 0.7449 | 0.0140 | No | this paper | Table 2 |

### WikiCS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.7036 | — | Yes | this paper | Table 1 |
| GCN | 0.7528 | — | Yes | this paper | Table 1 |
| GIN | 0.4977 | — | Yes | this paper | Table 1 |
| GAT | 0.7678 | — | Yes | this paper | Table 1 |
| DGI | 0.7532 | — | Yes | this paper | Table 1 |
| BGRL | 0.7653 | — | Yes | this paper | Table 1 |
| GraphMAE | 0.7761 | — | Yes | this paper | Table 1 |
| GIANT | 0.7656 | — | Yes | this paper | Table 1 |
| GFT | 0.7939 | — | Yes | Wang 2024 | Table 1 |
| RWPT | 0.8027 | — | No | this paper | Table 1 |
| RWPT (Pre-Train w/ Arxiv) | 0.7995 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ FB15k237) | 0.7950 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ ChEMBL) | 0.7927 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ three) | 0.8015 | — | No | this paper | Table 2 |
| RWPT (Pre-Train w/ all) | 0.8027 | — | No | this paper | Table 2 |
| RWPT (Walk, k=16, l=2) | 0.8080 | — | No | this paper | Table 3 |
| RWPT (Walk, k=4, l=4) | 0.7951 | — | No | this paper | Table 3 |
| RWPT (Walk, k=8, l=4) | 0.8045 | — | No | this paper | Table 3 |
| RWPT (Walk, k=4, l=8) | 0.7974 | — | No | this paper | Table 3 |
| RWPT (Walk, k=8, l=8) | 0.8025 | — | No | this paper | Table 3 |
| RWPT (Neighbor, [4,4,2]) | 0.8046 | — | No | this paper | Table 3 |
| RWPT (Neighbor, [8,4]) | 0.8002 | — | No | this paper | Table 3 |
| RWPT (Our loss) | 0.8027 | 0.0019 | No | this paper | Table 4 |
| GraphPrompt | 0.8001 | 0.0029 | Yes | this paper | Table 4 |
| MaskGAE | 0.8048 | 0.0013 | Yes | this paper | Table 4 |
| RWPT (Context prediction) | 0.8027 | 0.0019 | No | this paper | Table 5 |
| RWPT (+ Token reconstruction) | 0.8074 | 0.0034 | No | this paper | Table 5 |
| RWPT (+ Position reconstruction) | 0.8025 | 0.0023 | No | this paper | Table 5 |
| RWPT (Our model) | 0.8027 | 0.0019 | No | this paper | Table 6 |
| RWPT (Edge feat. input) | 0.8093 | 0.0026 | No | this paper | Table 6 |
| RWPT (Full attn. mask) | 0.7955 | 0.0012 | No | this paper | Table 6 |

## Baseline Models Identified

- **MLP**
- **GCN** (from: Kipf 2017)
- **GIN** (from: Xu 2019)
- **GAT** (from: Velickovic 2018)
- **DGI** (from: Velickovic 2019)
- **BGRL** (from: Thakoor 2022)
- **GraphMAE** (from: Hou 2022)
- **GIANT** (from: Chien 2022)
- **GFT** (from: Wang 2024)
- **GraphPrompt**
- **MaskGAE**
- **PRODIGY** (from: Huang 2023)
- **OFA** (from: Liu 2024)

## Extraction Notes

[Cora] Extracted all Cora results from Tables 1, 2, 3, and 4. Table 1 contains standard baselines
and the main RWPT result. Table 2 contains transfer learning variants of RWPT. Tables 3 and 4
contain ablation studies and loss comparisons for RWPT and other baselines (DGI, GraphPrompt,
MaskGAE). All values are normalized to [0,1]. Standard deviations are extracted where available.
[CiteSeer] Extracted results for CiteSeer from Table 1 and Table 2. Table 1 compares contextual
losses (Our loss, DGI, GraphPrompt, MaskGAE). Table 2 compares training losses (Context prediction,
+ Token reconstruction, + Position reconstruction). The 'Our loss' and 'Context prediction' rows
appear to represent the same baseline configuration for the proposed method (RWPT) before ablation,
hence identical values. All values are normalized to [0,1]. Standard deviations are parsed from the
± notation. [PubMed] Extracted results for PubMed from Table 1. The table reports node
classification accuracy. RWPT is the proposed model. GFT is a baseline from Wang 2024. Other
baselines are standard GNNs/SSL methods. Values are percentages converted to [0,1]. No standard
deviations reported in Table 1 for these models. Table 4 and 5 report ablation studies with std
devs, but Table 1 contains the main comparison results requested. [Arxiv] failed: 1 validation error
for ExtractionOutput   Input should be a valid dictionary or instance of ExtractionOutput
[type=model_type, input_value=[{'name': 'MLP', 'params_...inal_paper_hint': None}], input_type=list]
For further information visit https://errors.pydantic.dev/2.13/v/model_type [WikiCS] Extracted all
WikiCS results from Tables 1-6. Table 1 provides the main comparison with baselines. Table 2 shows
transfer learning variants. Table 3 shows sampler ablations. Table 4 shows loss ablations. Table 5
shows training loss ablations. Table 6 shows architecture ablations. All values are normalized to
[0,1] as they are Accuracy scores. Standard deviations were extracted where available. [WN18RR]
failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary or instance of
ExtractionOutput [type=model_type, input_value=[{'name': 'MLP', 'params_...paper_hint': 'Liu2024'}],
input_type=list]     For further information visit https://errors.pydantic.dev/2.13/v/model_type
[FB15k237] The paper reports Accuracy for FB15k237 in multiple tables (Table 1, 2, 3, 4, 5). The
FOCUS instruction requested Hits@50, but the paper does not report Hits@50 for FB15k237; it reports
Accuracy. Therefore, Accuracy is extracted as the primary metric. Table 1 contains the main
comparison. Table 2 contains transfer learning results. Table 3 contains few-shot results. Table 4
contains ablation on samplers. Table 5 contains ablation on model design. All results are test-set
results. No standard deviations are reported in Table 1, 2, 3, 4. Table 5 reports std for RWPT.
[HIV] Extracted all HIV results from Tables 1, 2, 3, and 4. Table 1 contains the main comparison.
Table 2 contains transfer learning variants. Table 3 contains ablation on samplers. Table 4 contains
ablation on model architecture. All values are normalized to [0,1]. Standard deviations are
extracted where explicitly provided in Table 4. [PCBA] Extracted only PCBA results from Table 1.
Values are percentages from the table divided by 100 to fit [0,1] range. Table 1 reports test
results (implied by context of performance comparison). Table 2 contains transfer learning results
which are variants/ablations, so excluded per instructions to use standard/default configuration.
The primary metric for PCBA in this paper is ROC-AUC (graph classification task). [Tox21] Extracted
the primary ROC-AUC result for Tox21 from Table 2 (Performance comparison on different model
architectures). The table lists 'Our model' which corresponds to the proposed RWPT method. The value
is 74.49 ± 1.40, normalized to 0.7449 ± 0.014. Other tables (Table 1) contain ablation studies for
samplers on Tox21 but Table 2 presents the main architectural comparison including the final
proposed model configuration. Baselines listed in the text (PRODIGY, OFA, etc.) are not present in
the provided table snippets, so only the proposed model's result could be extracted from the
provided text. [Peptides-func] The provided text contains Table 1 (tab:sampler) which reports
results for 'Pep-F' (Peptides-func) and 'Pep-S' (Peptides-struct). However, this table specifically
compares different sampling strategies (Walk vs Neighbor) and hyperparameters (k, l) for the
proposed method (RWPT). It does NOT contain the results for the baseline models (PRODIGY, OFA, GFT,
GCN, GIN, GAT, DGI, BGRL, GraphMAE, GIANT) on the Peptides-func dataset. The main performance
comparison table containing the baselines is not included in the provided text. Therefore, no
results for the baselines can be extracted for Peptides-func. Only the proposed model's ablation
results are present, but since the focus is on the standard benchmark comparison against baselines,
and the primary metric AP is not explicitly labeled as 'AP' in this specific table (it just says
'higher is better' and lists values like 88.31, which likely corresponds to AP given the context of
Peptides-func, but without explicit metric label and baseline context, it's safer to report empty
for the main benchmark request). Note: The values in 'Pep-F' column (e.g., 90.48) are likely AP
scores (0-100 scale or 0-1 scale? 90.48 suggests percentage). However, without the baseline rows, I
cannot fulfill the request to extract ALL quantitative results including baselines. I will output an
empty results list because the specific table provided is an ablation study on sampling, not the
main benchmark table comparing against the listed baselines. [Peptides-struct] The provided text
only contains an ablation table (Table 1 in the appendix/supplementary section referenced as
tab:sampler) comparing sampling strategies for the proposed model RWPT. It does not contain the main
results table comparing RWPT against the listed baselines (PRODIGY, OFA, GFT, GCN, etc.) on
Peptides-struct. Therefore, only the best-performing configuration of the proposed model (RWPT with
Walk sampler, k=4, l=8, which has the lowest MAE of 0.2561) could be extracted. Baseline results are
missing from the provided text.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*