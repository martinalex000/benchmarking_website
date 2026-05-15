# Extraction: arXiv:2411.17296
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: GrokFormer
- Type: GraphTransformer

## Results

### Actor — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3323 | 0.0116 | Yes | this paper | Table 1 |
| GAT | 0.3393 | 0.0247 | Yes | this paper | Table 1 |
| H2GCN | 0.3631 | 0.0258 | Yes | this paper | Table 1 |
| HopGNN | 0.3933 | 0.0279 | Yes | this paper | Table 1 |
| ChebyNet | 0.3761 | 0.0089 | Yes | this paper | Table 1 |
| GPRGNN | 0.3992 | 0.0067 | Yes | this paper | Table 1 |
| BernNet | 0.4179 | 0.0101 | Yes | this paper | Table 1 |
| JacobiConv | 0.4117 | 0.0064 | Yes | this paper | Table 1 |
| HiGCN | 0.4181 | 0.0052 | Yes | this paper | Table 1 |
| Transformer | 0.3995 | 0.0064 | Yes | this paper | Table 1 |
| GraphGPS | 0.3768 | 0.0094 | Yes | this paper | Table 1 |
| NodeFormer | 0.3462 | 0.0182 | Yes | this paper | Table 1 |
| SGFormer | 0.4169 | 0.0063 | Yes | this paper | Table 1 |
| NAGphormer | 0.4008 | 0.0150 | Yes | this paper | Table 1 |
| Specformer | 0.4193 | 0.0104 | Yes | this paper | Table 1 |
| PolyFormer | 0.4151 | 0.0071 | Yes | this paper | Table 1 |
| GrokFormer | 0.4298 | 0.0148 | No | this paper | Table 1 |
| *-w/o-GrokFilter | 0.4095 | 0.0205 | Yes | this paper | Table 2 |
| GrokFilter | 0.4215 | 0.0129 | Yes | this paper | Table 2 |

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5961 | 0.0221 | Yes | this paper | Table 1 |
| GAT | 0.6313 | 0.0193 | Yes | this paper | Table 1 |
| H2GCN | 0.6120 | 0.0428 | Yes | this paper | Table 1 |
| HopGNN | 0.6525 | 0.0349 | Yes | this paper | Table 1 |
| ChebyNet | 0.5928 | 0.0125 | Yes | this paper | Table 1 |
| GPRGNN | 0.6728 | 0.0109 | Yes | this paper | Table 1 |
| BernNet | 0.6829 | 0.0158 | Yes | this paper | Table 1 |
| JacobiConv | 0.7420 | 0.0103 | Yes | this paper | Table 1 |
| HiGCN | 0.6847 | 0.0045 | Yes | this paper | Table 1 |
| Transformer | 0.4521 | 0.0201 | Yes | this paper | Table 1 |
| GraphGPS | 0.4607 | 0.0151 | Yes | this paper | Table 1 |
| NodeFormer | 0.5634 | 0.0111 | Yes | this paper | Table 1 |
| SGFormer | 0.6144 | 0.0137 | Yes | this paper | Table 1 |
| NAGphormer | 0.5492 | 0.0111 | Yes | this paper | Table 1 |
| Specformer | 0.7472 | 0.0129 | Yes | this paper | Table 1 |
| PolyFormer | 0.6017 | 0.0139 | Yes | this paper | Table 1 |
| GrokFormer | 0.7558 | 0.0173 | No | this paper | Table 1 |
| *-w/o-GrokFilter | 0.4503 | 0.0180 | Yes | this paper | Table 2 |
| GrokFilter | 0.7497 | 0.0167 | Yes | this paper | Table 2 |

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7986 | 0.0067 | Yes | this paper | Table 1 |
| GAT | 0.8052 | 0.0071 | Yes | this paper | Table 1 |
| H2GCN | 0.8090 | 0.0121 | Yes | this paper | Table 1 |
| HopGNN | 0.8038 | 0.0068 | Yes | this paper | Table 1 |
| ChebyNet | 0.7911 | 0.0075 | Yes | this paper | Table 1 |
| GPRGNN | 0.8012 | 0.0083 | Yes | this paper | Table 1 |
| BernNet | 0.8009 | 0.0079 | Yes | this paper | Table 1 |
| JacobiConv | 0.8078 | 0.0079 | Yes | this paper | Table 1 |
| HiGCN | 0.8112 | 0.0028 | Yes | this paper | Table 1 |
| Transformer | 0.7055 | 0.0120 | Yes | this paper | Table 1 |
| GraphGPS | 0.7587 | 0.0071 | Yes | this paper | Table 1 |
| NodeFormer | 0.7956 | 0.0110 | Yes | this paper | Table 1 |
| SGFormer | 0.7962 | 0.0163 | Yes | this paper | Table 1 |
| NAGphormer | 0.8012 | 0.0124 | Yes | this paper | Table 1 |
| Specformer | 0.8149 | 0.0094 | Yes | this paper | Table 1 |
| PolyFormer | 0.8180 | 0.0076 | Yes | this paper | Table 1 |
| GrokFormer | 0.8192 | 0.0125 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8714 | 0.0101 | Yes | this paper | Table 1 |
| GAT | 0.8803 | 0.0079 | Yes | this paper | Table 1 |
| H2GCN | 0.8796 | 0.0037 | Yes | this paper | Table 1 |
| HopGNN | 0.8868 | 0.0106 | Yes | this paper | Table 1 |
| ChebyNet | 0.8667 | 0.0082 | Yes | this paper | Table 1 |
| GPRGNN | 0.8857 | 0.0069 | Yes | this paper | Table 1 |
| BernNet | 0.8852 | 0.0095 | Yes | this paper | Table 1 |
| JacobiConv | 0.8898 | 0.0046 | Yes | this paper | Table 1 |
| HiGCN | 0.8923 | 0.0023 | Yes | this paper | Table 1 |
| Transformer | 0.7183 | 0.0168 | Yes | this paper | Table 1 |
| GraphGPS | 0.8342 | 0.0122 | Yes | this paper | Table 1 |
| NodeFormer | 0.8732 | 0.0092 | Yes | this paper | Table 1 |
| SGFormer | 0.8787 | 0.0267 | Yes | this paper | Table 1 |
| NAGphormer | 0.8815 | 0.0135 | Yes | this paper | Table 1 |
| Specformer | 0.8857 | 0.0101 | Yes | this paper | Table 1 |
| PolyFormer | 0.8767 | 0.0128 | Yes | this paper | Table 1 |
| GrokFormer | 0.8957 | 0.0143 | No | this paper | Table 1 |
| *-w/o-GrokFilter | 0.7742 | 0.0177 | Yes | this paper | Table 2 |
| GrokFilter | 0.8898 | 0.0125 | Yes | this paper | Table 2 |

### Photo — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8826 | 0.0073 | Yes | this paper | Table 1 |
| GAT | 0.9094 | 0.0068 | Yes | this paper | Table 1 |
| H2GCN | 0.9545 | 0.0067 | Yes | this paper | Table 1 |
| HopGNN | 0.9449 | 0.0033 | Yes | this paper | Table 1 |
| ChebyNet | 0.9377 | 0.0032 | Yes | this paper | Table 1 |
| GPRGNN | 0.9385 | 0.0028 | Yes | this paper | Table 1 |
| BernNet | 0.9363 | 0.0035 | Yes | this paper | Table 1 |
| JacobiConv | 0.9543 | 0.0023 | Yes | this paper | Table 1 |
| HiGCN | 0.9533 | 0.0037 | Yes | this paper | Table 1 |
| Transformer | 0.8958 | 0.0105 | Yes | this paper | Table 1 |
| GraphGPS | 0.9435 | 0.0025 | Yes | this paper | Table 1 |
| NodeFormer | 0.9527 | 0.0022 | Yes | this paper | Table 1 |
| SGFormer | 0.9434 | 0.0023 | Yes | this paper | Table 1 |
| NAGphormer | 0.9549 | 0.0011 | Yes | this paper | Table 1 |
| Specformer | 0.9548 | 0.0032 | Yes | this paper | Table 1 |
| PolyFormer | 0.9408 | 0.0137 | Yes | this paper | Table 1 |
| GrokFormer | 0.9552 | 0.0052 | No | this paper | Table 1 |
| *-w/o-GrokFilter | 0.8958 | 0.0105 | Yes | this paper | Table 2 |
| GrokFilter | 0.9510 | 0.0078 | Yes | this paper | Table 2 |

### Physics — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9774 | 0.0035 | Yes | this paper | Table 1 |
| GAT | 0.9782 | 0.0028 | Yes | this paper | Table 1 |
| H2GCN | 0.9719 | 0.0013 | Yes | this paper | Table 1 |
| HopGNN | 0.9786 | 0.0016 | Yes | this paper | Table 1 |
| ChebyNet | 0.9725 | 0.0078 | Yes | this paper | Table 1 |
| GPRGNN | 0.9725 | 0.0013 | Yes | this paper | Table 1 |
| BernNet | 0.9736 | 0.0030 | Yes | this paper | Table 1 |
| JacobiConv | 0.9756 | 0.0028 | Yes | this paper | Table 1 |
| HiGCN | 0.9765 | 0.0035 | Yes | this paper | Table 1 |
| GraphGPS | 0.9760 | 0.0005 | Yes | this paper | Table 1 |
| NodeFormer | 0.9645 | 0.0028 | Yes | this paper | Table 1 |
| SGFormer | 0.9796 | 0.0081 | Yes | this paper | Table 1 |
| NAGphormer | 0.9785 | 0.0026 | Yes | this paper | Table 1 |
| Specformer | 0.9775 | 0.0053 | Yes | this paper | Table 1 |
| PolyFormer | 0.9808 | 0.0027 | Yes | this paper | Table 1 |
| GrokFormer | 0.9831 | 0.0018 | No | this paper | Table 1 |

### Pubmed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8674 | 0.0027 | Yes | this paper | Table 1 |
| GAT | 0.8704 | 0.0024 | Yes | this paper | Table 1 |
| H2GCN | 0.8918 | 0.0028 | Yes | this paper | Table 1 |
| HopGNN | 0.8915 | 0.0035 | Yes | this paper | Table 1 |
| ChebyNet | 0.8795 | 0.0028 | Yes | this paper | Table 1 |
| GPRGNN | 0.8846 | 0.0033 | Yes | this paper | Table 1 |
| BernNet | 0.8848 | 0.0041 | Yes | this paper | Table 1 |
| JacobiConv | 0.8962 | 0.0041 | Yes | this paper | Table 1 |
| HiGCN | 0.8995 | 0.0013 | Yes | this paper | Table 1 |
| Transformer | 0.8666 | 0.0050 | Yes | this paper | Table 1 |
| GraphGPS | 0.8662 | 0.0053 | Yes | this paper | Table 1 |
| NodeFormer | 0.8924 | 0.0023 | Yes | this paper | Table 1 |
| SGFormer | 0.8907 | 0.0014 | Yes | this paper | Table 1 |
| NAGphormer | 0.8970 | 0.0019 | Yes | this paper | Table 1 |
| Specformer | 0.9061 | 0.0023 | Yes | this paper | Table 1 |
| PolyFormer | 0.9068 | 0.0031 | Yes | this paper | Table 1 |
| GrokFormer | 0.9139 | 0.0051 | No | this paper | Table 1 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4678 | 0.0087 | Yes | this paper | Table 1 |
| GAT | 0.4449 | 0.0088 | Yes | this paper | Table 1 |
| H2GCN | 0.3953 | 0.0088 | Yes | this paper | Table 1 |
| HopGNN | 0.5783 | 0.0211 | Yes | this paper | Table 1 |
| ChebyNet | 0.4055 | 0.0042 | Yes | this paper | Table 1 |
| GPRGNN | 0.5015 | 0.0192 | Yes | this paper | Table 1 |
| BernNet | 0.5135 | 0.0073 | Yes | this paper | Table 1 |
| JacobiConv | 0.5738 | 0.0125 | Yes | this paper | Table 1 |
| HiGCN | 0.5186 | 0.0042 | Yes | this paper | Table 1 |
| Transformer | 0.3317 | 0.0132 | Yes | this paper | Table 1 |
| GraphGPS | 0.3414 | 0.0073 | Yes | this paper | Table 1 |
| NodeFormer | 0.4342 | 0.0162 | Yes | this paper | Table 1 |
| SGFormer | 0.4582 | 0.0217 | Yes | this paper | Table 1 |
| NAGphormer | 0.4855 | 0.0256 | Yes | this paper | Table 1 |
| Specformer | 0.6464 | 0.0081 | Yes | this paper | Table 1 |
| PolyFormer | 0.4498 | 0.0303 | Yes | this paper | Table 1 |
| GrokFormer | 0.6512 | 0.0159 | No | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7738 | 0.0328 | Yes | this paper | Table 1 |
| GAT | 0.8082 | 0.0213 | Yes | this paper | Table 1 |
| H2GCN | 0.9189 | 0.0393 | Yes | this paper | Table 1 |
| HopGNN | 0.8915 | 0.0404 | Yes | this paper | Table 1 |
| ChebyNet | 0.8622 | 0.0245 | Yes | this paper | Table 1 |
| GPRGNN | 0.9295 | 0.0131 | Yes | this paper | Table 1 |
| BernNet | 0.9312 | 0.0065 | Yes | this paper | Table 1 |
| JacobiConv | 0.9344 | 0.0213 | Yes | this paper | Table 1 |
| HiGCN | 0.9215 | 0.0073 | Yes | this paper | Table 1 |
| Transformer | 0.8875 | 0.0630 | Yes | this paper | Table 1 |
| GraphGPS | 0.8371 | 0.0585 | Yes | this paper | Table 1 |
| NodeFormer | 0.8463 | 0.0347 | Yes | this paper | Table 1 |
| SGFormer | 0.9246 | 0.0148 | Yes | this paper | Table 1 |
| NAGphormer | 0.9180 | 0.0185 | Yes | this paper | Table 1 |
| Specformer | 0.8823 | 0.0038 | Yes | this paper | Table 1 |
| PolyFormer | 0.8902 | 0.0544 | Yes | this paper | Table 1 |
| GrokFormer | 0.9459 | 0.0208 | No | this paper | Table 1 |
| *-w/o-GrokFilter | 0.9033 | 0.0236 | Yes | this paper | Table 2 |
| GrokFilter | 0.9362 | 0.0304 | Yes | this paper | Table 2 |

### WikiCS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8232 | 0.0069 | Yes | this paper | Table 1 |
| GAT | 0.8322 | 0.0078 | Yes | this paper | Table 1 |
| H2GCN | 0.8345 | 0.0026 | Yes | this paper | Table 1 |
| HopGNN | 0.8473 | 0.0059 | Yes | this paper | Table 1 |
| ChebyNet | 0.8295 | 0.0045 | Yes | this paper | Table 1 |
| GPRGNN | 0.8258 | 0.0089 | Yes | this paper | Table 1 |
| BernNet | 0.8356 | 0.0061 | Yes | this paper | Table 1 |
| JacobiConv | 0.8413 | 0.0049 | Yes | this paper | Table 1 |
| HiGCN | 0.8314 | 0.0078 | Yes | this paper | Table 1 |
| Transformer | 0.7736 | 0.0125 | Yes | this paper | Table 1 |
| GraphGPS | 0.7926 | 0.0057 | Yes | this paper | Table 1 |
| NodeFormer | 0.8103 | 0.0094 | Yes | this paper | Table 1 |
| SGFormer | 0.8271 | 0.0056 | Yes | this paper | Table 1 |
| NAGphormer | 0.8341 | 0.0034 | Yes | this paper | Table 1 |
| Specformer | 0.8515 | 0.0063 | Yes | this paper | Table 1 |
| PolyFormer | 0.8362 | 0.0017 | Yes | this paper | Table 1 |
| GrokFormer | 0.8557 | 0.0065 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN**
- **GAT**
- **H2GCN**
- **HopGNN**
- **ChebyNet**
- **GPRGNN**
- **BernNet**
- **JacobiConv**
- **HiGCN**
- **Transformer**
- **GraphGPS**
- **NodeFormer**
- **SGFormer**
- **NAGphormer**
- **Specformer**
- **PolyFormer**
- ***-w/o-GrokFilter**
- **GrokFilter**

## Extraction Notes

[Cora] Extracted all models for Cora from the main results table and the ablation study table.
Normalised percentages to decimals. [Citeseer] Extracted results for Citeseer from the main results
table. Ablation table results for Citeseer were not included as they represent model variants rather
than the standard proposed model or established baselines. [Pubmed] Extracted all models for the
Pubmed dataset from Table 1. Ablation results for Pubmed were present in Table 2 but were not
included as they represent model variants rather than the primary benchmark comparison. [Photo]
Extracted all models for the 'Photo' dataset from the main results table and the ablation study
table. Normalised percentages to decimals. [WikiCS] Extracted only WikiCS results from Table 1 as
requested. All values were percentages and normalized by dividing by 100. [Physics] Extracted
results for 'Physics' dataset from Table 1. Ablation results for Physics from Table 2 were skipped
as they represent model variants (w/o-GrokFilter, GrokFilter) rather than the standard benchmark
comparison of the proposed model vs baselines. [Penn94] failed: 4 validation errors for
ExtractionOutput results.3.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.9.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Chameleon] Extracted all models for the Chameleon
dataset from the main results table and the ablation study table. Normalised percentages to
decimals. [Squirrel] Extracted all models for the Squirrel dataset from Table 1. Ablation results
for Squirrel from Table 2 were excluded as they represent model variants rather than the standard
proposed model or established baselines. [Actor] Extracted all models for the Actor dataset from the
main results table and the ablation study table. Normalised percentages to decimals. [Texas]
Extracted results for Texas from both the main results table (Table 1) and the ablation study table
(Table 2). All values were normalized from percentages to decimals.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*