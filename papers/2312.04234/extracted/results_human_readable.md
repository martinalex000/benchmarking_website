# Extraction: arXiv:2312.04234
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GFSA (144.0M params)
- Type: Other

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| GPS + GFSA | 0.7244 | 0.0048 | No | this paper | Table 1 |
| Graph-ViT | 0.6967 | 0.0040 | Yes | this paper | Table 1 |
| Graph-ViT + GFSA | 0.6987 | 0.0028 | No | this paper | Table 1 |

### Code Clone Detection — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CodeT5-small | 0.9436 | — | Yes | Wang et al. 2021 | Table 2 |
| CodeT5-small + GFSA | 0.9494 | — | No | this paper | Table 2 |
| CodeT5-base | 0.9431 | — | Yes | Wang et al. 2021 | Table 2 |
| CodeT5-base + GFSA | 0.9492 | — | No | this paper | Table 2 |

### GLUE — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| BERT_BASE | 0.8251 | — | Yes | Devlin et al. 2019 | Table 1 |
| BERT_BASE + ContraNorm | 0.8348 | — | Yes | Guo et al. 2023 | Table 1 |
| BERT_BASE + GFSA | 0.8358 | — | No | this paper | Table 1 |
| ALBERT_BASE | 0.8401 | — | Yes | Lan et al. 2019 | Table 1 |
| ALBERT_BASE + ContraNorm | 0.8469 | — | Yes | Guo et al. 2023 | Table 1 |
| ALBERT_BASE + GFSA | 0.8505 | — | No | this paper | Table 1 |
| RoBERTa_BASE | 0.8587 | — | Yes | Liu et al. 2019 | Table 1 |
| RoBERTa_BASE + ContraNorm | 0.8661 | — | Yes | Guo et al. 2023 | Table 1 |
| RoBERTa_BASE + GFSA | 0.8679 | — | No | this paper | Table 1 |

### Image (4K) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer | 0.3820 | — | Yes | Vaswani et al. 2017 | Table 1 |
| Transformer+GFSA | 0.4020 | — | Yes | this paper | Table 1 |
| Linformer | 0.3780 | — | Yes | Wang et al. 2020 | Table 1 |
| YOSO-E | 0.3980 | — | Yes | Zeng et al. 2021 | Table 1 |
| Efficient Attention | 0.4020 | — | Yes | Shen et al. 2021 | Table 1 |
| Efficient Attention + GFSA | 0.4040 | — | No | this paper | Table 1 |

### ImageNet-1k — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DeiT-S | 0.7980 | — | Yes | this paper | Table 1 |
| DeiT-S + AttnScale | 0.8070 | — | Yes | this paper | Table 1 |
| DeiT-S + FeatScale | 0.8090 | — | Yes | this paper | Table 1 |
| DeiT-S + ContraNorm | 0.8040 | — | Yes | this paper | Table 1 |
| Swin-S | 0.8290 | — | Yes | this paper | Table 1 |
| CaiT-S | 0.8260 | — | Yes | this paper | Table 1 |
| DeiT-S + GFSA | 0.8110 | — | No | this paper | Table 1 |
| CaiT-S + GFSA | 0.8280 | — | No | this paper | Table 1 |
| Swin-S + GFSA | 0.8300 | — | No | this paper | Table 1 |
| ResNet-152 | 0.7810 | — | Yes | this paper | Table 3 |
| DenseNet-201 | 0.7760 | — | Yes | this paper | Table 3 |
| CVT-21 | 0.8250 | — | Yes | this paper | Table 3 |
| Refiner | 0.8120 | — | Yes | this paper | Table 3 |
| ViT-S/16 | 0.7810 | — | Yes | this paper | Table 3 |
| ViT-B/16 | 0.7980 | — | Yes | this paper | Table 3 |
| DeiT-S + LayerScale | 0.8050 | — | Yes | this paper | Table 3 |
| DeiT-S + LateInsertion | 0.8050 | — | Yes | this paper | Table 3 |
| DeiT-S + ClassAttention | 0.8060 | — | Yes | this paper | Table 3 |
| DeiT-S + HAT | 0.8090 | — | Yes | this paper | Table 3 |
| DeiT-S + Diverse | 0.8060 | — | Yes | this paper | Table 3 |
| T2T-ViT-24 | 0.8230 | — | Yes | this paper | Table 3 |
| DeepViT-24B | 0.8010 | — | Yes | this paper | Table 3 |
| DeiT-S + DiversePatch | 0.8220 | — | Yes | this paper | Table 3 |
| Fnet-XS | 0.7120 | — | Yes | this paper | Table 4 |
| GFNet-XS | 0.7860 | — | Yes | this paper | Table 4 |
| SpectFormer-XS | 0.8020 | — | Yes | this paper | Table 4 |
| SVT-XS | 0.7990 | — | Yes | this paper | Table 4 |
| DeiT-S + NeuTRENO | 0.8070 | — | Yes | this paper | Table 4 |
| DeiT-T | 0.7652 | — | Yes | this paper | Table 5 |
| DeiT-T + ContraNorm | 0.7703 | — | Yes | this paper | Table 5 |
| DeiT-T + GFSA | 0.7768 | — | No | this paper | Table 5 |

### LibriSpeech 100h — WER ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer | 11.0200 | — | Yes | this paper | Table 1 |
| Transformer+GFSA | 10.3000 | — | No | this paper | Table 1 |
| Branchformer | 9.6300 | — | Yes | Peng 2022 | Table 1 |
| Branchformer+GFSA | 9.6000 | — | Yes | this paper | Table 1 |

### LibriSpeech 960h — WER ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer | 2.4200 | — | Yes | this paper | Table 1 |
| Transformer+GFSA | 2.3100 | — | No | this paper | Table 1 |
| Branchformer | 2.1300 | — | Yes | Peng 2022 | Table 1 |
| Branchformer+GFSA | 2.1100 | — | Yes | this paper | Table 1 |

### ListOps (2K) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer | 0.3710 | — | Yes | Vaswani et al. 2017 | Table 1 |
| Transformer+GFSA | 0.3760 | — | Yes | this paper | Table 1 |
| Linformer | 0.3730 | — | Yes | Wang et al. 2020 | Table 1 |
| YOSO-E | 0.3730 | — | Yes | Zeng et al. 2021 | Table 1 |
| Efficient Attention | 0.3690 | — | Yes | Shen et al. 2021 | Table 1 |
| Efficient Attention + GFSA | 0.3790 | — | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPS | 0.9805 | 0.0013 | Yes | this paper | Table 1 |
| GPS + GFSA | 0.9814 | 0.0014 | No | this paper | Table 1 |
| Graph-ViT | 0.9820 | 0.0005 | Yes | this paper | Table 1 |
| Graph-ViT + GFSA | 0.9826 | 0.0004 | No | this paper | Table 1 |

### PCQM4M — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Graphormer | 0.1286 | 0.0160 | Yes | Ying et al. 2021 | Table 2 |
| Graphormer + GFSA | 0.1193 | 0.0000 | No | this paper | Table 2 |

### PCQM4Mv2 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Graphormer | 0.0862 | 0.0000 | Yes | this paper | Table 1 |
| Graphormer + GFSA | 0.0860 | 0.0000 | No | this paper | Table 1 |

### PTB — Perplexity ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPT2 | 19.5130 | — | Yes | Radford et al. 2019 | Table 1 |
| GPT2 + GFSA | 19.4500 | — | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| GPS + GFSA | 0.6593 | 0.0094 | No | this paper | Table 1 |
| Graph-ViT | 0.6919 | 0.0085 | Yes | this paper | Table 1 |
| Graph-ViT + GFSA | 0.6964 | 0.0025 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| GPS + GFSA | 0.2496 | 0.0013 | No | this paper | Table 1 |
| Graph-ViT | 0.2474 | 0.0016 | Yes | He et al. 2023 | Table 1 |
| Graph-ViT + GFSA | 0.2461 | 0.0024 | No | this paper | Table 1 |

### WikiText-103 — Perplexity ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPT2 | 15.9390 | — | Yes | Radford et al. 2019 | Table 1 |
| GPT2 + GFSA | 15.9190 | — | No | this paper | Table 1 |

### WikiText-2 — Perplexity ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPT2 | 20.9660 | — | Yes | Radford et al. 2019 | Table 1 |
| GPT2 + GFSA | 20.9230 | — | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Graphormer | 0.1240 | 0.0060 | Yes | this paper | Table 1 (tab:gnn_zinc_std) |
| Graphormer + GFSA | 0.1189 | 0.0020 | No | this paper | Table 1 (tab:gnn_zinc_std) |
| GPS | 0.0700 | 0.0040 | Yes | this paper | Table 2 (tab:gps_vit) |
| GPS + GFSA | 0.0690 | 0.0020 | No | this paper | Table 2 (tab:gps_vit) |
| Graph-ViT | 0.0849 | 0.0047 | Yes | this paper | Table 2 (tab:gps_vit) |
| Graph-ViT + GFSA | 0.0845 | 0.0032 | No | this paper | Table 2 (tab:gps_vit) |

## Baseline Models Identified

- **ContraNorm** (from: Guo et al. 2023)
- **BERT_BASE**, 110.0M params (from: Devlin et al. 2019)
- **ALBERT_BASE**, 11.0M params (from: Lan et al. 2019)
- **RoBERTa_BASE**, 125.0M params (from: Liu et al. 2019)
- **DeiT-S**, 22.0M params (from: Touvron et al. 2021)
- **DeiT-S + AttnScale**, 22.0M params (from: Wang et al. 2022)
- **DeiT-S + FeatScale**, 22.0M params (from: Wang et al. 2022)
- **DeiT-S + ContraNorm**, 22.0M params (from: Guo et al. 2023)
- **Swin-S**, 50.0M params (from: Liu et al. 2021)
- **CaiT-S**, 47.0M params (from: Touvron et al. 2021)
- **ResNet-152**, 230.0M params (from: He et al. 2016)
- **DenseNet-201**, 77.0M params (from: Huang et al. 2017)
- **CVT-21**, 32.0M params (from: Wu et al. 2021)
- **Refiner**, 86.0M params (from: Zhou et al. 2021)
- **ViT-S/16**, 49.0M params (from: Dosovitskiy et al. 2020)
- **ViT-B/16**, 86.0M params (from: Dosovitskiy et al. 2020)
- **DeiT-S + LayerScale**, 22.0M params (from: Touvron et al. 2021)
- **DeiT-S + LateInsertion**, 22.0M params (from: Touvron et al. 2021)
- **DeiT-S + ClassAttention**, 22.0M params (from: Touvron et al. 2021)
- **DeiT-S + HAT**, 22.0M params (from: Bai et al. 2022)
- **DeiT-S + Diverse**, 22.0M params (from: Chen et al. 2022)
- **T2T-ViT-24**, 64.0M params (from: Yuan et al. 2021)
- **DeepViT-24B**, 36.0M params (from: Zhou et al. 2021)
- **DeiT-S + DiversePatch**, 44.0M params (from: Gong et al. 2021)
- **Fnet-XS**, 20.0M params (from: Lee et al. 2021)
- **GFNet-XS**, 16.0M params (from: Rao et al. 2021)
- **SpectFormer-XS**, 20.0M params (from: Patro et al. 2023)
- **SVT-XS**, 20.0M params (from: Patro et al. 2023)
- **DeiT-S + NeuTRENO**, 20.0M params (from: Nguyen et al. 2023)
- **DeiT-T** (from: Touvron et al. 2021)
- **DeiT-T + ContraNorm** (from: Guo et al. 2023)
- **Graphormer**, 0.5M params (from: Ying et al. 2021)
- **GPS** (from: Rampásek et al. 2022)
- **Graph-ViT** (from: He et al. 2023)
- **Transformer**, 71.5M params
- **Branchformer**, 109.8M params (from: Peng 2022)
- **Branchformer+GFSA**, 109.8M params (from: Peng 2022)
- **GPT2**, 117.0M params (from: Radford et al. 2019)
- **CodeT5-small**, 60.0M params (from: Wang et al. 2021)
- **CodeT5-base** (from: Wang et al. 2021)
- **Transformer+GFSA**
- **Linformer** (from: Wang et al. 2020)
- **YOSO-E** (from: Zeng et al. 2021)
- **Efficient Attention** (from: Shen et al. 2021)

## Extraction Notes

[GLUE] Extracted only the 'Avg' column from Table 1 as the primary benchmark metric for the GLUE
dataset. The paper reports various metrics for individual tasks (Matthews corr, F1, Spearman,
Accuracy), but the 'Avg' column represents the standard GLUE score (average of all task scores, with
appropriate metric normalization). Values are presented as percentages in the table (e.g., 82.51)
and were divided by 100 to fit the [0,1] range for Accuracy. Standard deviations are not reported in
the table. Uses external data is set to true as all models are pre-trained language models (BERT,
ALBERT, RoBERTa) fine-tuned on GLUE. [ImageNet-1k] Extracted results from Table 1, Table 3, Table 4,
and Table 5. Table 1 and Table 3 contain overlapping data; Table 3 is more comprehensive. Table 5
contains results for DeiT-T and DeiT-S with different layer counts (12, 16, 24). The primary metric
'Accuracy' (Top-1 Acc) was used. Values are normalized to [0, 1]. Standard deviations were not
reported in the tables. Table 6 (varying K) and Table 7/8 (runtime) were excluded as they are
ablation/runtime metrics, not standard benchmark accuracy results. Table 2 is a subset of Table 1/3
and was skipped to avoid duplication. [ZINC] Extracted all ZINC results from Table 1 (Graphormer
variants) and Table 2 (GPS/Graph-ViT variants). The primary metric MAE was used. Standard deviations
were extracted from the appendix table (tab:gnn_zinc_std) for Graphormer variants and from Table 2
for GPS/Graph-ViT variants. Note that GPS and Graph-ViT results in Table 2 are significantly better
than Graphormer results in Table 1, likely due to different experimental setups or hyperparameters
as mentioned in the text ('We fix all hyperparameters... as recommended in their paper'). Both sets
of results are included as they are reported for the ZINC dataset. [Peptides-func] Extracted only
Peptides-func AP results as requested. The table lists 'Peptide-func' which corresponds to the
standard 'Peptides-func' dataset in LRGB. All values are normalized to [0,1]. GFSA is the proposed
module, applied on top of GPS and Graph-ViT baselines. [Peptides-struct] Extracted only Peptides-
struct MAE results as requested. Note that 'GPS + GFSA' and 'Graph-ViT + GFSA' are variants using
the proposed GFSA module, so they are marked as is_proposed=true. The baseline models are GPS and
Graph-ViT. Values were normalized from the table (e.g., 0.2500 -> 0.25). Standard deviations were
parsed from the \std{} format. [MNIST] Extracted only MNIST Accuracy results as requested. The table
reports results for GPS and Graph-ViT baselines with and without the proposed GFSA module. All
values are normalized to [0,1] range for Accuracy. [CIFAR10] Extracted only CIFAR10 Accuracy results
as requested. The table reports results for GPS and Graph-ViT baselines and their variants with
GFSA. All values are normalized to [0,1] range. Standard deviations are parsed from the '±'
notation. [Molhiv] failed: 2 validation errors for ExtractionOutput results.0.value   Input should
be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type results.1.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type [MolTOX21] failed: 2 validation errors for
ExtractionOutput results.0.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.1.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [LibriSpeech] Extracted all WER results for
LibriSpeech 100h and 960h from Table 1. Note: The text mentions 'Branchformer+GFSA achieves
2.31/5.49 with an LM', but the table shows 2.11/4.94 for Branchformer+GFSA and 2.31/5.49 for
Transformer+GFSA. The table values are prioritized as they are explicit. The text likely contains a
typo attributing Transformer+GFSA's 960h results to Branchformer+GFSA or implying LM usage not
reflected in the table's 'no LM' baseline context for Transformer. However, since the table is the
primary source of structured data, table values are used. The 'uses_external_data' is set to false
as no external pre-training data is explicitly mentioned for the ASR task in the provided text,
assuming standard LibriSpeech training. [PTB] Extracted results for the PTB dataset from Table 1
(tab:gpt2_sens) and Table 4 (tab:gpt2-even). The values are identical in both tables. The proposed
model is 'GPT2 + GFSA' (specifically the configuration with K=7,8,9 which achieves the best PTB
perplexity of 19.450, rounded to 19.45). The baseline is 'GPT2'. Perplexity is a loss-like metric
where lower is better. No standard deviation is reported in the tables. [WikiText-2] Extracted
Perplexity results for WikiText-2 from Table 1 (results comparison on gpt-2 finetuned with gfsa).
The table lists multiple GFSA variants (K=2 to K=9). The best performing variant is GPT2 + GFSA(K=9)
with 20.923. Table 4 also reports GPT2 + GFSA (implied best/default configuration based on Table 1
best) with 20.923. GPT2 baseline is 20.966. Other tables (2, 3, 5, 6) report runtime metrics which
are ignored per instructions. [WikiText-103] Extracted results for WikiText-103 from Table 1
(tab:gpt2_sens) and Table 4 (tab:gpt2-even). The values are identical across tables for the standard
configurations. GFSA variants with specific K values (K=2..9) and GFSA_even were excluded as they
represent optional variants/sensitivity analysis rather than the standard proposed model
configuration. Perplexity is a loss-like metric where lower is better. [PCQM4M] Extracted validation
MAE results for PCQM4M from Table 2 (labeled tab:gnn_ogb_std in the text). The paper explicitly
states 'Graph-ViT + GFSA shows improvements... in PCQM4M, incorporating GFSA improves the validation
MAE'. Although the table caption mentions PCQM4M and PCQM4Mv2, and the text mentions PCQM4M-LSC, the
table columns are labeled 'Validate' under 'PCQM4M'. The values correspond to the validation set
performance as indicated by the text focusing on validation improvements and the table structure.
Test set results are not explicitly provided in this specific table for PCQM4M (only Train and
Validate columns are present for PCQM4M in Table 2). The prompt asks for standard benchmark results;
typically OGB PCQM4M uses validation MAE for leaderboard submission during training, but test MAE is
the final metric. However, since only validation data is present in the provided table for PCQM4M, I
extracted the validation MAE. Note: The table also lists PCQM4Mv2, but the FOCUS instruction
restricts to 'PCQM4M'. The 'Validate' column for PCQM4M is used. [PCQM4Mv2] Extracted Validate MAE
for PCQM4Mv2 as the primary benchmark metric. The table provides Train and Validate columns; for
graph-level prediction benchmarks like PCQM4Mv2, the Validate (or Test if available) score is the
standard reported metric. The paper does not explicitly list a 'Test' column in this specific table,
but 'Validate' is the standard proxy for final performance in this context (often corresponding to
the leaderboard test set in OGB competitions). Values are normalized to [0,1]. Std is 0.000 for
both. [Code Clone Detection] Extracted results from Table 2 (labeled tab:clone in the text) which
reports 'Clone F1' for the Code Clone Detection task. Values were converted from percentages (e.g.,
94.36) to decimals (0.9436) as per standard F1 metric normalization rules. No standard deviations
were reported in the table. [ListOps] Extracted only ListOps (2K) results as requested. Values were
percentages in the table (e.g., 37.1) and were divided by 100 to fit the [0,1] range for Accuracy.
No standard deviations were reported in the table. [Image (4K)] Extracted only the 'Image (4K)'
dataset results as requested. The table reports Accuracy in percentage, so values were divided by
100. No standard deviation was reported in the table. The proposed model is identified as 'Efficient
Attention + GFSA' based on the bolded best results and context of the paper (GFSA is the proposed
method).

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*