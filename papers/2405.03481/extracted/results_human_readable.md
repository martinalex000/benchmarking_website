# Extraction: arXiv:2405.03481
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: LOW

## Proposed Model: Graphormer-AnchorGT-SPD
- Type: GraphTransformer

## Results

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | this paper | Table 2 |
| GAT | 0.7059 | 0.0045 | Yes | this paper | Table 2 |
| GIN (GINE) | 0.6472 | 0.0155 | Yes | this paper | Table 2 |
| GatedGCN | 0.7384 | 0.0033 | Yes | this paper | Table 2 |
| SAT | 0.7786 | 0.0010 | Yes | this paper | Table 2 |
| SAN (LapPE) | 0.7669 | 0.0065 | Yes | this paper | Table 2 |
| Graphormer | 0.7755 | 0.0055 | Yes | this paper | Table 2 |
| GraphGPS | 0.7802 | 0.0018 | Yes | this paper | Table 2 |
| GraphGPS-AnchorGT | 0.7812 | 0.0037 | Yes | this paper | Table 2 |
| GraphGPS-AnchorGT-SPD | 0.7880 | 0.0025 | No | this paper | Table 2 |

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7943 | 0.0026 | Yes | this paper | Table 3 |
| GAT | 0.8013 | 0.0062 | Yes | this paper | Table 3 |
| GraphSAGE | 0.7923 | 0.0053 | Yes | this paper | Table 3 |
| APPNP | 0.7933 | 0.0035 | Yes | this paper | Table 3 |
| SAN | 0.7064 | 0.0097 | Yes | this paper | Table 3 |
| Gophormer | 0.7643 | 0.0078 | Yes | this paper | Table 3 |
| ANS-GT | 0.8025 | 0.0039 | Yes | this paper | Table 3 |
| ANS-GT-AnchorGT | 0.8201 | 0.0021 | No | this paper | Table 3 |

### LRGB-Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 1 |
| GIN (GINE) | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| SAT | 0.2601 | 0.0248 | Yes | this paper | Table 1 |
| SAN (LapPE) | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| Graphormer | 0.6453 | 0.0121 | Yes | this paper | Table 1 |
| Graphormer-AnchorGT-SPD | 0.6520 | 0.0264 | No | this paper | Table 1 |
| GraphGPS | 0.6535 | 0.0041 | Yes | this paper | Table 2 |
| GraphGPS-AnchorGT | 0.6214 | 0.0056 | Yes | this paper | Table 2 |
| GraphGPS-AnchorGT-SPD | 0.6460 | 0.0031 | Yes | this paper | Table 2 |

### LRGB-Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | Kipf & Welling 2016 | Table 1 |
| GCNII | 0.3471 | 0.0010 | Yes | Chen et al. 2020 | Table 1 |
| GIN (GINE) | 0.3547 | 0.0045 | Yes | Xu et al. 2018 | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | Bresson & Laurent 2017 | Table 1 |
| SAT | 0.6473 | 0.0849 | Yes | Chen et al. 2022 | Table 1 |
| SAN (LapPE) | 0.2683 | 0.0043 | Yes | Kreuzer et al. 2021 | Table 1 |
| Graphormer | 0.2705 | 0.0045 | Yes | Ying et al. 2021 | Table 1 |
| Graphormer-AnchorGT-SPD | 0.2519 | 0.0033 | No | this paper | Table 1 |
| GraphGPS | 0.2500 | 0.0005 | Yes | Rampásek et al. 2022 | Table 2 |
| GraphGPS-AnchorGT | 0.2674 | 0.0011 | Yes | this paper | Table 2 |
| GraphGPS-AnchorGT-SPD | 0.2437 | 0.0006 | No | this paper | Table 2 |

### QM8 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0279 | 0.0001 | Yes | this paper | Table 1 |
| GCNII | 0.0256 | 0.0002 | Yes | this paper | Table 1 |
| GAT | 0.0317 | 0.0001 | Yes | this paper | Table 1 |
| GIN (GINE) | 0.0276 | 0.0001 | Yes | this paper | Table 1 |
| SAT | 0.0281 | 0.0025 | Yes | this paper | Table 1 |
| Graphormer | 0.0079 | 0.0001 | Yes | this paper | Table 1 |
| Graphormer-AnchorGT-SPD | 0.0077 | 0.0001 | No | this paper | Table 1 |
| GraphGPS | 0.7050 | 0.0810 | Yes | this paper | Table 2 |
| GraphGPS-AnchorGT | 0.7120 | 0.0740 | Yes | this paper | Table 2 |
| GraphGPS-AnchorGT-SPD | 0.6650 | 0.0860 | No | this paper | Table 2 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1379 | — | Yes | this paper | Table 1 |
| GIN (GINE) | 0.1218 | — | Yes | this paper | Table 1 |
| GT | 0.2260 | 0.0100 | Yes | this paper | Table 1 |
| SAN (LapPE) | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| Graphormer | 0.1200 | 0.0080 | Yes | this paper | Table 1 |
| Graphormer-AnchorGT-SPD | 0.1220 | 0.0060 | No | this paper | Table 1 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7124 | 0.0029 | Yes | this paper | Table 3 |
| GAT | 0.5788 | 0.0018 | Yes | this paper | Table 3 |
| GraphSAGE | 0.7149 | 0.0027 | Yes | this paper | Table 3 |
| ANS-GT | 0.7186 | 0.0020 | Yes | this paper | Table 3 |
| ANS-GT-AnchorGT | 0.7234 | 0.0045 | No | this paper | Table 3 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GIN (GINE)** (from: Xu et al. 2019)
- **GT** (from: Vaswani et al. 2017 (adapted for graphs))
- **SAN (LapPE)** (from: Corso et al. 2020)
- **Graphormer** (from: Ying et al. 2021)
- **GCNII** (from: Chen 2020)
- **GAT** (from: Velickovic 2017)
- **GIN** (from: Xu 2018)
- **GatedGCN** (from: Bresson 2017)
- **APPNP** (from: Klicpera 2018)
- **SAN** (from: Kreuzer 2021)
- **Gophormer** (from: Zhao 2021)
- **SAT** (from: Chen 2022)
- **GraphGPS** (from: Rampavsek 2022)
- **ANS-GT** (from: Zhang 2022)
- **GraphGPS-AnchorGT** (from: this paper)
- **Graphormer-AnchorGT-SPD** (from: this paper)
- **GraphSAGE** (from: Hamilton et al. 2017)

## Extraction Notes

[ZINC] Extracted only ZINC results from Table 1 as requested. Note that Table 1 lists 'Graphormer'
with value 0.120 (bolded as best) and 'Graphormer-AnchorGT-SPD' with 0.122. The paper title/caption
suggests Graphormer-AnchorGT-SPD is the proposed variant, but on ZINC specifically, the vanilla
Graphormer has a slightly lower MAE. I have extracted all rows for ZINC. The 'Graphormer-AnchorGT'
(without SPD) row is not present in Table 1 for ZINC, only in Table 2 for other datasets or implied.
Wait, looking closely at Table 1, the row is 'Graphormer-AnchorGT-SPD'. There is no 'Graphormer-
AnchorGT' row in Table 1. I extracted exactly what is in Table 1 for ZINC. [QM9] The provided text
contains dataset statistics (Table 4) and experimental setup descriptions, but it does not contain
the main results table(s) reporting MAE values for QM9. The text mentions that results for QM9 are
cited from original papers or appendix, but the actual numerical results are not present in the
provided snippet. Therefore, no quantitative results could be extracted. [QM8] Extracted QM8 MAE
results from Table 1 and Table 2. Note that Table 2 contains two different sets of results for
Graphormer and its variants compared to Table 1 (likely due to different experimental settings
mentioned in the text, e.g., 'best setting on ZINC' vs default). Both sets are included as they
represent standard configurations reported for the dataset. The proposed model 'Graphormer-AnchorGT-
SPD' appears in Table 1, while 'GraphGPS-AnchorGT-SPD' appears in Table 2. Both are variants of the
proposed AnchorGT method. The values for GraphGPS variants in Table 2 are significantly higher
(worse) than Graphormer variants, suggesting a different configuration or initialization, but they
are extracted as reported. [LRGB-Peptides-struct] Extracted results for LRGB-Peptides-struct from
Table 1 and Table 2. Table 1 focuses on Graphormer variants, while Table 2 focuses on GraphGPS
variants. Both tables report MAE on the test set (implied by standard benchmark reporting and
context of 'results'). The proposed model is identified as Graphormer-AnchorGT-SPD in Table 1 and
GraphGPS-AnchorGT-SPD in Table 2. Since the paper title/caption suggests 'AnchorGT' is the core
contribution applied to both backbones, both variants are treated as proposed models in their
respective comparison contexts. All other models are baselines. Values are normalized to [0,1] where
applicable (MAE is not normalized). Std deviations are parsed from '±' notation. [LRGB-Peptides-
func] Extracted results for LRGB-Peptides-func from Table 1 and Table 2. Note that Table 1 and Table
2 contain overlapping baseline results (GCN, GCNII, GIN, GatedGCN, SAT, SAN, Graphormer). The
proposed model in the paper is Graphormer-AnchorGT-SPD (Table 1) and GraphGPS-AnchorGT-SPD (Table
2). Since the prompt asks for 'the' proposed model and the paper title/context suggests Graphormer-
AnchorGT is the primary contribution being compared against GraphGPS variants, I included both sets
of results as they appear in the text. The values are identical for shared baselines. I included all
rows from both tables for the specified dataset to ensure completeness as per instructions to
include ALL rows from ALL result tables. [ogb-PCQM4Mv2] failed: 5 validation errors for
ExtractionOutput results.1.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.2.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [CLUSTER] Extracted only the CLUSTER dataset results
from Table 2. The metric is Accuracy. All values were divided by 100 to normalize from percentage to
[0,1] range. GCNII has no result for CLUSTER in Table 2, so it is excluded from the results list.
[Citeseer] Extracted only the Citeseer column from Table 3 as requested. The table reports Accuracy
for node representation learning benchmarks. All values were divided by 100 to normalize percentages
to [0,1] range. Standard deviations were parsed from the '±' notation. [ogbn-arxiv] Extracted only
the 'ogbn-arxiv' column from Table 3. The table header indicates 'Accuracy' is the metric. Values
are percentages (e.g., 71.24) so they were divided by 100 to fit the [0,1] range rule for Accuracy.
Standard deviations were parsed from the '±' notation. APPNP, SAN, and Gophormer had no results for
ogbn-arxiv (marked as '-'), so they were excluded from the results list. [ogbn-products] The
provided text contains dataset statistics (Table 4) for ogbn-products but does not contain any
performance results (Accuracy, etc.) for ogbn-products or any other dataset. The text mentions
comparing against baselines like GCN, GAT, etc., but the actual result tables with numerical
performance metrics are missing from the input. Therefore, no quantitative results could be
extracted.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*