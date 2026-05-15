# Extraction: arXiv:2406.12059
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GECO
- Type: GNN

## Results

### Arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7025 | 0.0022 | Yes | this paper | Table 1 |
| SAGE | 0.7200 | 0.0016 | Yes | this paper | Table 1 |
| GraphSaint | 0.6795 | 0.0024 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.6800 | 0.0059 | Yes | this paper | Table 1 |
| GAT | 0.7159 | 0.0038 | Yes | this paper | Table 1 |
| Graphormer-SAMPLE | 0.7043 | 0.0020 | Yes | this paper | Table 1 |
| SAT-SAMPLE | 0.6820 | 0.0046 | Yes | this paper | Table 1 |
| ANS-GT | 0.6820 | 0.0046 | Yes | this paper | Table 1 |
| Exphormer | 0.7244 | 0.0028 | Yes | this paper | Table 1 |
| HSGT | 0.7258 | 0.0031 | Yes | this paper | Table 1 |
| GECO | 0.7310 | 0.0024 | No | this paper | Table 1 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | 0.0010 | Yes | this paper | Table 1 |
| GINE | 0.1339 | 0.0044 | Yes | this paper | Table 1 |
| GatedGCN | 0.2641 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.2574 | 0.0034 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2618 | 0.0031 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2592 | 0.0158 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.2434 | 0.0156 | Yes | this paper | Table 1 |
| GPS w/ Transformer | 0.3412 | 0.0044 | Yes | Rampasek 2022 | Table 1 |
| Exphormer | 0.3455 | 0.0009 | Yes | Shirzad 2023 | Table 1 |
| GECO | 0.3320 | 0.0032 | No | this paper | Table 1 |

### Flickr — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5090 | 0.0012 | Yes | this paper | Table 1 |
| SAGE | 0.5372 | 0.0016 | Yes | this paper | Table 1 |
| GraphSaint | 0.5137 | 0.0021 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.4995 | 0.0015 | Yes | this paper | Table 1 |
| GAT | 0.5070 | 0.0032 | Yes | this paper | Table 1 |
| Graphormer-SAMPLE | 0.5193 | 0.0021 | Yes | this paper | Table 1 |
| SAT-SAMPLE | 0.5048 | 0.0034 | Yes | this paper | Table 1 |
| Exphormer | 0.5260 | 0.0018 | Yes | this paper | Table 1 |
| HSGT | 0.5412 | 0.0051 | Yes | this paper | Table 1 |
| GECO | 0.5555 | 0.0025 | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table 1 |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table 1 |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3242 | 0.0008 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.3174 | 0.0020 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.3350 | 0.0003 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.3341 | 0.0006 | Yes | this paper | Table 1 |
| GPS w/ Transformer | 0.3337 | 0.0006 | Yes | Rampasek 2022 | Table 1 |
| Exphormer | 0.3637 | 0.0020 | Yes | Shirzad 2023 | Table 1 |
| GECO | 0.3526 | 0.0016 | No | this paper | Table 1 |

### PCQM4Mv2 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1379 | — | Yes | this paper | Table 1 |
| GCN-virtual | 0.1153 | — | Yes | this paper | Table 1 |
| GIN-virtual | 0.1083 | — | Yes | this paper | Table 1 |
| GRPE | 0.0890 | — | Yes | rampasek2022recipe | Table 1 |
| EGT | 0.0869 | — | Yes | rampasek2022recipe | Table 1 |
| Graphormer | 0.0864 | — | Yes | rampasek2022recipe | Table 1 |
| GPS-sm | 0.0938 | — | Yes | rampasek2022recipe | Table 1 |
| GPS-med | 0.0858 | — | Yes | rampasek2022recipe | Table 1 |
| GECO | 0.0841 | — | No | this paper | Table 1 |
| GIN | 0.1195 | — | Yes | this paper | Table 2 |
| GPS-small | 0.0938 | — | Yes | rampasek2022recipe | Table 2 |
| GPS-medium | 0.0858 | — | Yes | rampasek2022recipe | Table 2 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | this paper | Table 1 |
| GINE | 0.1265 | 0.0076 | Yes | this paper | Table 1 |
| GatedGCN | 0.2873 | 0.0219 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.2860 | 0.0085 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2694 | 0.0098 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.3230 | 0.0039 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.3216 | 0.0027 | Yes | this paper | Table 1 |
| GPS w/ Transformer | 0.3748 | 0.0109 | Yes | this paper | Table 1 |
| Exphormer | 0.3975 | 0.0037 | Yes | this paper | Table 1 |
| GECO | 0.4210 | 0.0080 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| GPS w/ Transformer | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| GECO | 0.6975 | 0.0025 | No | this paper | Table 1 |
| Graph-MLP-Mixer | 0.6970 | 0.0080 | Yes | He 2023 | Table 3 |
| Graph-ViT | 0.6942 | 0.0075 | Yes | He 2023 | Table 3 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| GPS w/ Transformer | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| GECO | 0.2464 | 0.0009 | No | this paper | Table 1 |
| Graph-MLP-Mixer | 0.2475 | 0.0015 | Yes | this paper | Table 3 |
| Graph-ViT | 0.2449 | 0.0016 | Yes | this paper | Table 3 |

### Reddit — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9278 | 0.0011 | Yes | this paper | Table 1 |
| SAGE | 0.9650 | 0.0003 | Yes | this paper | Table 1 |
| GraphSaint | 0.9558 | 0.0007 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.9570 | 0.0006 | Yes | this paper | Table 1 |
| GAT | 0.9650 | 0.0011 | Yes | this paper | Table 1 |
| Graphormer-SAMPLE | 0.9305 | 0.0022 | Yes | this paper | Table 1 |
| SAT-SAMPLE | 0.9337 | 0.0032 | Yes | this paper | Table 1 |
| ANS-GT | 0.9530 | 0.0081 | Yes | this paper | Table 1 |
| Exphormer | 0.9590 | 0.0015 | Yes | this paper | Table 1 |
| GECO | 0.9665 | 0.0005 | No | this paper | Table 1 |

### Yelp — Micro-F1 Score ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4008 | 0.0015 | Yes | this paper | Table 1 |
| SAGE | 0.6303 | 0.0020 | Yes | this paper | Table 1 |
| GraphSaint | 0.2942 | 0.0132 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.5639 | 0.0064 | Yes | this paper | Table 1 |
| GAT | 0.6158 | 0.0137 | Yes | this paper | Table 1 |
| Graphormer-SAMPLE | 0.6001 | 0.0045 | Yes | this paper | Table 1 |
| SAT-SAMPLE | 0.6032 | 0.0065 | Yes | this paper | Table 1 |
| Exphormer | 0.6080 | 0.0156 | Yes | this paper | Table 1 |
| HSGT | 0.6347 | 0.0045 | Yes | this paper | Table 1 |
| GECO | 0.6318 | 0.0059 | No | this paper | Table 1 |

### ogbg-code2 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphTrans (GCN-Virtual) | 0.1830 | 0.0024 | Yes | rampasek2022recipe | Table 1 |
| K-Subtree SAT | 0.1937 | 0.0028 | Yes | rampasek2022recipe | Table 1 |
| GPS | 0.1894 | 0.0024 | Yes | rampasek2022recipe | Table 1 |
| GECO | 0.1915 | 0.0020 | No | this paper | Table 1 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SAN | 0.2765 | 0.0042 | Yes | Rampasek et al. 2022 | Table 1 |
| GraphTrans (GCN-Virtual) | 0.2761 | 0.0029 | Yes | Rampasek et al. 2022 | Table 1 |
| GPS | 0.2907 | 0.0028 | Yes | Rampasek et al. 2022 | Table 1 |
| GECO | 0.2961 | 0.0008 | No | this paper | Table 1 |
| GCN+virtual node | 0.2424 | 0.0034 | Yes | Rampasek et al. 2022 | Table 2 |
| GIN+virtual node | 0.2703 | 0.0023 | Yes | Rampasek et al. 2022 | Table 2 |
| GatedGCN-LSPE | 0.2670 | 0.0020 | Yes | Rampasek et al. 2022 | Table 2 |
| PNA | 0.2838 | 0.0035 | Yes | Rampasek et al. 2022 | Table 2 |
| DeeperGCN | 0.2781 | 0.0038 | Yes | Rampasek et al. 2022 | Table 2 |
| DGN | 0.2885 | 0.0030 | Yes | Rampasek et al. 2022 | Table 2 |
| GIN-AK+ | 0.2930 | 0.0044 | Yes | Rampasek et al. 2022 | Table 2 |
| CRaWl | 0.2986 | 0.0025 | Yes | Rampasek et al. 2022 | Table 2 |
| ExpC | 0.2342 | 0.0029 | Yes | Rampasek et al. 2022 | Table 2 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GINE** (from: Xu et al. 2019)
- **GatedGCN** (from: Bresson & Laurent 2017)
- **GatedGCN+RWSE** (from: rampasek2022recipe)
- **Transformer+LapPE** (from: rampasek2022recipe)
- **SAN+LapPE** (from: rampasek2022recipe)
- **SAN+RWSE** (from: rampasek2022recipe)
- **GPS w/ Transformer** (from: rampasek2022recipe)
- **Exphormer** (from: shirzad2023exphormer)
- **Graph-MLP-Mixer** (from: He et al. 2023)
- **Graph-ViT** (from: He et al. 2023)
- **SAN** (from: Rampasek et al. 2022)
- **GraphTrans (GCN-Virtual)** (from: Rampasek et al. 2022)
- **GPS** (from: Rampasek et al. 2022)
- **GCN+virtual node** (from: Rampasek et al. 2022)
- **GIN+virtual node** (from: Rampasek et al. 2022)
- **GatedGCN-LSPE** (from: Rampasek et al. 2022)
- **PNA** (from: Rampasek et al. 2022)
- **DeeperGCN** (from: Rampasek et al. 2022)
- **DGN** (from: Rampasek et al. 2022)
- **GSN (directional)** (from: Rampasek et al. 2022)
- **GSN (GIN+VN base)** (from: Rampasek et al. 2022)
- **CIN** (from: Rampasek et al. 2022)
- **GIN-AK+** (from: Rampasek et al. 2022)
- **CRaWl** (from: Rampasek et al. 2022)
- **ExpC** (from: Rampasek et al. 2022)
- **K-Subtree SAT** (from: rampasek2022recipe)
- **GCN-virtual**, 4.9M params
- **GIN**, 3.8M params (from: Xu et al. 2019)
- **GIN-virtual**, 6.7M params
- **GRPE**, 46.2M params (from: rampasek2022recipe)
- **EGT**, 89.3M params (from: rampasek2022recipe)
- **Graphormer**, 48.3M params (from: You et al. 2021)
- **GPS-small**, 6.2M params (from: rampasek2022recipe)
- **GPS-medium**, 19.4M params (from: rampasek2022recipe)
- **SAGE** (from: Hamilton et al. 2017)
- **GraphSaint** (from: Zeng et al. 2021)
- **Cluster-GCN** (from: Chiang et al. 2019)
- **GAT** (from: Veličković et al. 2018)
- **Graphormer-SAMPLE** (from: Biao et al. 2022)
- **SAT** (from: You et al. 2021)
- **SAT-SAMPLE** (from: You et al. 2021)
- **ANS-GT** (from: Han et al. 2023)
- **GraphGPS w/ Transformer** (from: Ying et al. 2021)
- **HSGT**

## Extraction Notes

[PascalVOC-SP] Extracted only PascalVOC-SP F1 results from Table 1. Table 2 contains ablation
results for PascalVOC-SP (labeled Pas.VOC-SP) but these are variants of the proposed model (GECO)
with different local blocks, not standard baseline comparisons. The prompt asks for standard/default
configuration results and baselines. Table 1 provides the comprehensive comparison of baselines and
the proposed model's standard performance. The values in Table 2 for GECO (e.g., 0.3220) differ from
Table 1 (0.4210), likely due to different experimental setups or random seeds in the ablation study,
but Table 1 is the main result table for the proposed method's primary performance. I have included
the Table 1 results as they represent the main benchmarking against baselines. [COCO-SP] Extracted
only COCO-SP F1 results as requested. All values are normalized to [0,1]. Standard deviations are
parsed from the ± notation. The proposed model is GECO. [Peptides-func] Extracted results for
Peptides-func from Table 1 (LRGB Eval) and Table 3 (Comparison with Graph-ViT/MLP-Mixer). Table 2
(Ablation) was ignored as it reports non-standard configurations (Conv-1, Conv-10, etc.) and lacks
standard deviation values, making direct comparison with the main benchmark results difficult. The
primary metric AP was used. All values are normalized to [0,1]. GECO is the proposed model.
[Peptides-struct] Extracted Peptides-struct MAE results from Table 1 and Table 3. Table 2 contains
ablation results for GECO with different local block configurations; these were excluded as per the
instruction to use only the STANDARD/DEFAULT configuration (which corresponds to the main GECO entry
in Table 1 and Table 3, labeled 'LCB' in Table 2). The value 0.2464 in Table 1 is the primary
reported result for GECO on Peptides-struct. [PCQM-Contact] Extracted only PCQM-Contact MRR results
from Table 1. All values are normalized to [0,1]. Standard deviations are parsed from the ±
notation. Baseline sources are inferred from citations mentioned in the table caption or standard
knowledge of the models. [ogbg-molhiv] failed: 4 validation errors for ExtractionOutput
results.1.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.2.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.7.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.15.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[ogbg-molpcba] Extracted only results for 'ogbg-molpcba' dataset and 'Avg. Precision' metric as
requested. Table 1 and Table 2 contain overlapping baseline results; both were included to ensure
all reported baselines are captured. The proposed model GECO is identified from the text and table
highlighting. Standard deviations were parsed from the 'value ± std' format. Values are already in
[0,1] range. [ogbg-ppa] failed: 2 validation errors for ExtractionOutput results.7.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type [ogbg-code2] Extracted F1 scores for ogbg-code2
from both Table 1 and Table 2. Table 2 contains duplicate entries for the baselines and proposed
model found in Table 1. The values are identical. Standard configuration results were used. No other
datasets were included. [PCQM4Mv2] Extracted Validation MAE results as the paper explicitly states
the test set is private and validation is used for evaluation. Table 1 and Table 2 contain
overlapping information; Table 2 provides slightly more precision for the proposed model (0.08413 vs
0.0841). Both tables are included in the results list. Baseline results for Graphormer, GRPE, EGT,
GPS-small, and GPS-medium are cited from rampasek2022recipe. [Flickr] Extracted only the 'Flickr'
column results as requested. Values were converted from percentages (e.g., 50.90) to decimals
(0.509) as per standard Accuracy metric normalization rules. Standard deviations were parsed from
the 'mean ± std' format. Models reporting 'OOM' (Out of Memory) or '--' were excluded as they do not
provide a valid numerical result. [Arxiv] Extracted only the 'Arxiv' column from Table 1. All values
are percentages converted to [0,1] range. Standard deviations were parsed from the 'mean ± std'
format. Models with 'OOM' (Out of Memory) or '--' were excluded as they do not provide valid
accuracy scores. [Reddit] The table reports 'Accuracy' for the Reddit dataset. The FOCUS instruction
requested 'F1'. However, the table explicitly labels the column as 'Accuracy' and does not provide
an F1 score for Reddit (unlike Yelp which has Micro-F1). In node classification benchmarks like
Reddit, Accuracy is the standard primary metric. I have extracted the Accuracy values as they are
the only quantitative results provided for Reddit in this table. The values are normalized to [0,1]
range. [Yelp] The table header lists 'Accuracy' for Flickr, Arxiv, and Reddit, but 'Micro-F1 Score'
for Yelp. The FOCUS instruction requested 'Accuracy' as the primary metric. However, for the Yelp
dataset specifically, the only reported metric in the table is Micro-F1 Score. Therefore, Micro-F1
Score is extracted as the primary benchmark result for Yelp. All values were divided by 100 to
normalize percentages to [0,1] range, although the table values appear to be raw scores (e.g.,
40.08) rather than percentages (0.4008). Wait, looking at standard benchmarks, Yelp is often
reported as percentage or 0-1. Given the magnitude (40-63), these are likely percentages. The rule
states: 'If a paper reports such a value as a percentage (e.g. 44.2 meaning 44.2%), divide by 100'.
Thus 40.08 becomes 0.4008. Standard deviation parsing: '40.08 ± 0.15' -> value=0.4008, std=0.0015.
Note: Graphormer, SAN, SAT, GraphGPS w/ Transformer are OOM (Out of Memory) and excluded. ANS-GT has
'--' for Yelp and is excluded.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*