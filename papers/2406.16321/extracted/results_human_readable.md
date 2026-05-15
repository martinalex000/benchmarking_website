# Extraction: arXiv:2406.16321
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: MM-KGES
- Type: GNN

## Results

### Amazon-Cloth — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MMGCN + CLIP | 0.2220 | 0.0005 | Yes | this paper | Table 1 |
| MMGCN + ViT/T5 | 0.1945 | 0.0034 | Yes | this paper | Table 1 |
| MMGCN + ImageBind | 0.2472 | 0.0019 | Yes | this paper | Table 1 |
| MMGCN + DINOv2/T5 | 0.2177 | 0.0023 | Yes | this paper | Table 1 |
| MGAT + CLIP | 0.2138 | 0.0023 | Yes | this paper | Table 1 |
| MGAT + ViT/T5 | 0.2059 | 0.0041 | Yes | this paper | Table 1 |
| MGAT + ImageBind | 0.2213 | 0.0027 | Yes | this paper | Table 1 |
| MGAT + DINOv2/T5 | 0.2142 | 0.0013 | Yes | this paper | Table 1 |
| GCN + CLIP | 0.2228 | 0.0005 | Yes | this paper | Table 1 |
| GCN + ViT/T5 | 0.2160 | 0.0005 | Yes | this paper | Table 1 |
| GCN + ImageBind | 0.2281 | 0.0003 | Yes | this paper | Table 1 |
| GCN + DINOv2/T5 | 0.2119 | 0.0008 | Yes | this paper | Table 1 |
| SAGE + CLIP | 0.2458 | 0.0018 | Yes | this paper | Table 1 |
| SAGE + ViT/T5 | 0.2311 | 0.0005 | Yes | this paper | Table 1 |
| SAGE + ImageBind | 0.2520 | 0.0009 | Yes | this paper | Table 1 |
| SAGE + DINOv2/T5 | 0.2298 | 0.0001 | Yes | this paper | Table 1 |
| BUDDY + CLIP | 0.2344 | 0.0026 | Yes | this paper | Table 1 |
| BUDDY + ViT/T5 | 0.2282 | 0.0019 | Yes | this paper | Table 1 |
| BUDDY + ImageBind | 0.2435 | 0.0024 | Yes | this paper | Table 1 |
| BUDDY + DINOv2/T5 | 0.2295 | 0.0006 | Yes | this paper | Table 1 |
| MLP + CLIP | 0.2110 | 0.0004 | Yes | this paper | Table 1 |
| MLP + ViT/T5 | 0.1765 | 0.0006 | Yes | this paper | Table 1 |
| MLP + ImageBind | 0.2218 | 0.0002 | Yes | this paper | Table 1 |
| MLP + DINOv2/T5 | 0.1753 | 0.0011 | Yes | this paper | Table 1 |

### Amazon-Sports — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MMGCN + CLIP | 0.3196 | 0.0010 | Yes | this paper | Table 1 |
| MMGCN + ViT/T5 | 0.3033 | 0.0003 | Yes | this paper | Table 1 |
| MMGCN + ImageBind | 0.3174 | 0.0021 | Yes | this paper | Table 1 |
| MMGCN + DINOv2/T5 | 0.3004 | 0.0027 | Yes | this paper | Table 1 |
| MGAT + CLIP | 0.2756 | 0.0030 | Yes | this paper | Table 1 |
| MGAT + ViT/T5 | 0.3015 | 0.0034 | Yes | this paper | Table 1 |
| MGAT + ImageBind | 0.3015 | 0.0012 | Yes | this paper | Table 1 |
| MGAT + DINOv2/T5 | 0.2891 | 0.0009 | Yes | this paper | Table 1 |
| GCN + CLIP | 0.3138 | 0.0008 | Yes | this paper | Table 1 |
| GCN + ViT/T5 | 0.3083 | 0.0007 | Yes | this paper | Table 1 |
| GCN + ImageBind | 0.3167 | 0.0009 | Yes | this paper | Table 1 |
| GCN + DINOv2/T5 | 0.3042 | 0.0002 | Yes | this paper | Table 1 |
| SAGE + CLIP | 0.3383 | 0.0008 | Yes | this paper | Table 1 |
| SAGE + ViT/T5 | 0.3201 | 0.0010 | Yes | this paper | Table 1 |
| SAGE + ImageBind | 0.3432 | 0.0011 | Yes | this paper | Table 1 |
| SAGE + DINOv2/T5 | 0.3220 | 0.0012 | Yes | this paper | Table 1 |
| BUDDY + CLIP | 0.3155 | 0.0013 | Yes | this paper | Table 1 |
| BUDDY + ViT/T5 | 0.3041 | 0.0040 | Yes | this paper | Table 1 |
| BUDDY + ImageBind | 0.3302 | 0.0044 | Yes | this paper | Table 1 |
| BUDDY + DINOv2/T5 | 0.3002 | 0.0034 | Yes | this paper | Table 1 |
| MLP + CLIP | 0.2822 | 0.0009 | Yes | this paper | Table 1 |
| MLP + ViT/T5 | 0.2481 | 0.0005 | Yes | this paper | Table 1 |
| MLP + ImageBind | 0.3045 | 0.0014 | Yes | this paper | Table 1 |
| MLP + DINOv2/T5 | 0.2481 | 0.0016 | Yes | this paper | Table 1 |

### Ele-fashion — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MMGCN (CLIP/CLIP) | 0.8610 | 0.0050 | Yes | this paper | Table 1 |
| MMGCN (T5/ViT) | 0.8239 | 0.0030 | Yes | this paper | Table 1 |
| MMGCN (ImageBind/ImageBind) | 0.8621 | 0.0094 | Yes | this paper | Table 1 |
| MMGCN (T5/DINOv2) | 0.8553 | 0.0033 | Yes | this paper | Table 1 |
| MGAT (CLIP/CLIP) | 0.8466 | 0.0029 | Yes | this paper | Table 1 |
| MGAT (T5/ViT) | 0.8401 | 0.0008 | Yes | this paper | Table 1 |
| MGAT (ImageBind/ImageBind) | 0.8612 | 0.0008 | Yes | this paper | Table 1 |
| MGAT (T5/DINOv2) | 0.8454 | 0.0027 | Yes | this paper | Table 1 |
| GCN (CLIP/CLIP) | 0.7983 | 0.0003 | Yes | this paper | Table 1 |
| GCN (T5/ViT) | 0.7963 | 0.0007 | Yes | this paper | Table 1 |
| GCN (ImageBind/ImageBind) | 0.8035 | 0.0002 | Yes | this paper | Table 1 |
| GCN (T5/DINOv2) | 0.7937 | 0.0004 | Yes | this paper | Table 1 |
| SAGE (CLIP/CLIP) | 0.8710 | 0.0002 | Yes | this paper | Table 1 |
| SAGE (T5/ViT) | 0.8441 | 0.0009 | Yes | this paper | Table 1 |
| SAGE (ImageBind/ImageBind) | 0.8771 | 0.0013 | Yes | this paper | Table 1 |
| SAGE (T5/DINOv2) | 0.8531 | 0.0009 | Yes | this paper | Table 1 |
| MLP (CLIP/CLIP) | 0.8516 | 0.0003 | Yes | this paper | Table 1 |
| MLP (T5/ViT) | 0.8498 | 0.0005 | Yes | this paper | Table 1 |
| MLP (ImageBind/ImageBind) | 0.8873 | 0.0001 | Yes | this paper | Table 1 |
| MLP (T5/DINOv2) | 0.8487 | 0.0001 | Yes | this paper | Table 1 |

### Goodreads-LP — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MMGCN + CLIP | 0.3184 | 0.0009 | Yes | this paper | Table 1 |
| MMGCN + ViT+T5 | 0.3111 | 0.0025 | Yes | this paper | Table 1 |
| MMGCN + ImageBind | 0.2632 | 0.0023 | Yes | this paper | Table 1 |
| MMGCN + DINOv2+T5 | 0.2764 | 0.0095 | Yes | this paper | Table 1 |
| MGAT + CLIP | 0.7475 | 0.0123 | Yes | this paper | Table 1 |
| MGAT + ViT+T5 | 0.7526 | 0.0121 | Yes | this paper | Table 1 |
| MGAT + ImageBind | 0.7477 | 0.0049 | Yes | this paper | Table 1 |
| MGAT + DINOv2+T5 | 0.7489 | 0.0146 | Yes | this paper | Table 1 |
| GCN + CLIP | 0.2534 | 0.0006 | Yes | this paper | Table 1 |
| GCN + ViT+T5 | 0.2650 | 0.0010 | Yes | this paper | Table 1 |
| GCN + ImageBind | 0.2756 | 0.0126 | Yes | this paper | Table 1 |
| GCN + DINOv2+T5 | 0.2821 | 0.0112 | Yes | this paper | Table 1 |
| SAGE + CLIP | 0.4410 | 0.0137 | Yes | this paper | Table 1 |
| SAGE + ViT+T5 | 0.4479 | 0.0018 | Yes | this paper | Table 1 |
| SAGE + ImageBind | 0.3461 | 0.0043 | Yes | this paper | Table 1 |
| SAGE + DINOv2+T5 | 0.4561 | 0.0022 | Yes | this paper | Table 1 |
| BUDDY + CLIP | 0.4325 | 0.0023 | Yes | this paper | Table 1 |
| BUDDY + ViT+T5 | 0.4318 | 0.0053 | Yes | this paper | Table 1 |
| BUDDY + ImageBind | 0.4156 | 0.0061 | Yes | this paper | Table 1 |
| BUDDY + DINOv2+T5 | 0.4325 | 0.0013 | Yes | this paper | Table 1 |
| MLP + CLIP | 0.1103 | 0.0006 | Yes | this paper | Table 1 |
| MLP + ViT+T5 | 0.1110 | 0.0017 | Yes | this paper | Table 1 |
| MLP + ImageBind | 0.0773 | 0.0006 | Yes | this paper | Table 1 |
| MLP + DINOv2+T5 | 0.1028 | 0.0004 | Yes | this paper | Table 1 |

### Goodreads-NC — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MMGCN (CLIP/CLIP) | 0.8329 | 0.0020 | Yes | this paper | Table 1 |
| MMGCN (T5/ViT) | 0.8185 | 0.0022 | Yes | this paper | Table 1 |
| MMGCN (ImageBind/ImageBind) | 0.8058 | 0.0108 | Yes | this paper | Table 1 |
| MMGCN (T5/DINOv2) | 0.8244 | 0.0011 | Yes | this paper | Table 1 |
| MGAT (CLIP/CLIP) | 0.7648 | 0.0059 | Yes | this paper | Table 1 |
| MGAT (T5/ViT) | 0.7543 | 0.0076 | Yes | this paper | Table 1 |
| MGAT (ImageBind/ImageBind) | 0.6945 | 0.0625 | Yes | this paper | Table 1 |
| MGAT (T5/DINOv2) | 0.7498 | 0.0123 | Yes | this paper | Table 1 |
| GCN (CLIP/CLIP) | 0.8161 | 0.0001 | Yes | this paper | Table 1 |
| GCN (T5/ViT) | 0.8167 | 0.0003 | Yes | this paper | Table 1 |
| GCN (ImageBind/ImageBind) | 0.7891 | 0.0004 | Yes | this paper | Table 1 |
| GCN (T5/DINOv2) | 0.8171 | 0.0003 | Yes | this paper | Table 1 |
| SAGE (CLIP/CLIP) | 0.8330 | 0.0002 | Yes | this paper | Table 1 |
| SAGE (T5/ViT) | 0.8303 | 0.0004 | Yes | this paper | Table 1 |
| SAGE (ImageBind/ImageBind) | 0.8039 | 0.0021 | Yes | this paper | Table 1 |
| SAGE (T5/DINOv2) | 0.8299 | 0.0008 | Yes | this paper | Table 1 |
| MLP (CLIP/CLIP) | 0.7229 | 0.0002 | Yes | this paper | Table 1 |
| MLP (T5/ViT) | 0.6782 | 0.0007 | Yes | this paper | Table 1 |
| MLP (ImageBind/ImageBind) | 0.5875 | 0.0005 | Yes | this paper | Table 1 |
| MLP (T5/DINOv2) | 0.6883 | 0.0003 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **MMGCN** (from: MMGCN)
- **MGAT** (from: MGAT)
- **GCN** (from: GCN)
- **SAGE** (from: SAGE)
- **BUDDY** (from: BUDDY)
- **MLP** (from: MLP)
- **MoSE** (from: Mentioned in text as baseline for KGC)
- **VISTA** (from: Lee et al. 2023)

## Extraction Notes

[Amazon-Sports] Extracted all MRR results for Amazon-Sports from Table 1. The table uses a custom
macro \numstd{value}{std} which was parsed correctly. All values are percentages in the table (e.g.,
31.96), so they were divided by 100 to fit the [0,1] range for MRR. The proposed model is referred
to as MM-KGES in the text, but the table lists specific backbone/encoder combinations for various
GNN architectures (MMGCN, MGAT, GCN, SAGE, BUDDY, MLP). The best performing model is SAGE +
ImageBind with MRR 0.3432. External data usage is marked true for all rows because the encoders
(CLIP, ViT, ImageBind, DINOv2, T5) are pre-trained on external datasets (ImageNet, LAION, etc.).
[Amazon-Cloth] Extracted all MRR results for Amazon-Cloth from Table 1. The table uses a custom
LaTeX command \numstd{value}{std} which was parsed correctly. All values are percentages in the
table (e.g., 22.20) but the schema requires normalization to [0,1] for MRR, so they were divided by
100. The 'proposed model' is inferred as MM-KGES based on the text claiming MM-KGES outperforms
others, but the table lists specific encoder/model combinations. Since the table does not explicitly
label a single 'MM-KGES' row but rather compares baselines (MMGCN, MGAT, GCN, SAGE, BUDDY, MLP) with
different encoders, and the text suggests the proposed method is a specific configuration or
architecture not explicitly named in the table rows (or potentially the best performing one among
them, likely SAGE+ImageBind or similar), I have marked all rows as baselines relative to the
specific table entries. However, the prompt asks for the proposed model name. The text says 'MM-KGES
often outperforms'. It is likely MM-KGES is the framework containing these variants. Without a
specific row labeled 'MM-KGES', I cannot extract a specific result for it. I will leave
proposed_model params as null and is_proposed as false for all rows as they are standard baselines
with different encoders. The best result is SAGE + ImageBind with MRR 0.252. [Goodreads-LP]
Extracted all MRR results for Goodreads-LP from Table 1. The table uses a custom macro
\numstd{value}{std} which was parsed correctly. Note that MGAT models show significantly higher MRR
(~0.75) compared to other baselines (~0.25-0.45) and the proposed MMGCN (~0.32). This is likely due
to the specific architecture of MGAT handling the link prediction task better on this dataset, or
potentially different evaluation protocols not fully detailed in the snippet, but the values are
extracted exactly as reported. The 'proposed model' is identified as MMGCN based on the caption
'best performing combination' highlighting MMGCN results in orange for Goodreads-LP, although MGAT
actually achieves higher scores. The prompt asks to extract ALL rows, so all baselines are included.
[Ele-fashion] Extracted all rows for Ele-fashion from Table 1. The table uses a custom macro
\numstd{value}{std} which was parsed correctly. All models use external pre-trained encoders (CLIP,
T5, ImageBind, DINOv2), so uses_external_data is set to true. No proposed model is explicitly
identified in the table caption or structure; all are treated as baselines/comparisons. [Goodreads-
NC] Extracted all rows for Goodreads-NC from Table 1. The table presents results for multiple model
architectures (MMGCN, MGAT, GCN, SAGE, MLP) combined with different external image/text encoders
(CLIP, T5, ImageBind, DINOv2). Since the paper does not propose a single new architecture but rather
evaluates these combinations, no single 'proposed_model' is identified; all are treated as
baselines/comparisons. The 'uses_external_data' field is set to true for all rows because all models
rely on pre-trained encoders (CLIP, T5, ImageBind, DINOv2) which constitute external data/pre-
training. Values were normalized from percentages to [0,1] range. [MM-CoDEx-s] The paper text
mentions MM-CoDEx-s and MoSE in the context of Knowledge Graph Completion (KGC), stating 'ImageBind
consistently demonstrates superior performance across datasets and various KGEs, except for MM-
CoDEx-s on MoSE.' However, the provided text and tables do not contain the actual numerical results
table for KGC tasks or MM-CoDEx-s. The provided tables only cover dataset statistics and Link
Prediction results (Amazon-Sports, Amazon-Cloth, Goodreads-LP). Therefore, no quantitative results
for MM-CoDEx-s could be extracted. [MM-CoDEx-m] The provided text and tables do not contain any
quantitative results for the dataset 'MM-CoDEx-m'. Table 1 is a qualitative comparison. Table 2
provides dataset statistics. Table 3 provides graph statistics (excluding MM-CoDEx-m). Table 4
provides KG statistics (including MM-CoDEx-m counts but no performance metrics). Table 5 provides
Link Prediction results for Amazon-Sports, Amazon-Cloth, and Goodreads-LP only. The text mentions
that MoSE and VISTA perform well on MM-CoDEx-m with the exception of MoSE, but no numerical values
(MRR, Hits@K, etc.) are provided in the excerpt. Therefore, no results could be extracted for MM-
CoDEx-m.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*