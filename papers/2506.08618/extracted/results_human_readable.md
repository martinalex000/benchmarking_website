# Extraction: HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy Spectra of Non-Hermitian Crystals
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: GraphSAGE
- Type: GCN_variant

## Results

### HSG-12M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3650 | 0.0210 | Yes | Kipf & Welling 2017 | Table 1 |
| GAT | 0.3650 | 0.0100 | Yes | Velickovic et al. 2018 | Table 1 |
| GATv2 | 0.3510 | 0.0020 | Yes | Brody et al. 2022 | Table 1 |
| GIN | 0.0630 | 0.0310 | Yes | Xu et al. 2019 | Table 1 |
| GINE | 0.4600 | 0.0250 | Yes | Hu et al. 2019 | Table 1 |
| MF | 0.2950 | 0.0100 | Yes | Duvenaud et al. 2015 | Table 1 |
| CGCNN | 0.5310 | 0.0040 | Yes | Xie & Grossman 2018 | Table 1 |
| GraphSAGE | 0.5460 | 0.0040 | No | this paper | Table 1 |

### HSG-one-band — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7110 | 0.0100 | Yes | this paper | Table 1 |
| GAT | 0.6770 | 0.0020 | Yes | this paper | Table 1 |
| GATv2 | 0.6440 | 0.0050 | Yes | this paper | Table 1 |
| GIN | 0.7990 | 0.0050 | Yes | this paper | Table 1 |
| GINE | 0.7640 | 0.0060 | Yes | this paper | Table 1 |
| MF | 0.5890 | 0.0120 | Yes | this paper | Table 1 |
| CGCNN | 0.7960 | 0.0080 | Yes | this paper | Table 1 |
| GraphSAGE | 0.8540 | 0.0030 | No | this paper | Table 1 |

### HSG-three-band — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3370 | 0.0140 | Yes | this paper | Table 1 |
| GAT | 0.3440 | 0.0120 | Yes | this paper | Table 1 |
| GATv2 | 0.2820 | 0.0300 | Yes | this paper | Table 1 |
| GIN | 0.0500 | 0.0210 | Yes | this paper | Table 1 |
| GINE | 0.3790 | 0.0130 | Yes | this paper | Table 1 |
| MF | 0.2710 | 0.0040 | Yes | this paper | Table 1 |
| CGCNN | 0.4780 | 0.0110 | Yes | this paper | Table 1 |
| GraphSAGE | 0.5230 | 0.0200 | No | this paper | Table 1 |

### HSG-topology — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3970 | 0.0090 | Yes | this paper | Table 1 |
| GAT | 0.4340 | 0.0150 | Yes | this paper | Table 1 |
| GATv2 | 0.4010 | 0.0030 | Yes | this paper | Table 1 |
| GIN | 0.0950 | 0.0590 | Yes | this paper | Table 1 |
| GINE | 0.5330 | 0.0170 | Yes | this paper | Table 1 |
| MF | 0.3480 | 0.0120 | Yes | this paper | Table 1 |
| CGCNN | 0.5660 | 0.0160 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6200 | 0.0030 | No | this paper | Table 1 |

### HSG-two-band — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4780 | 0.0120 | Yes | this paper | Table 1 |
| GAT | 0.4620 | 0.0080 | Yes | this paper | Table 1 |
| GATv2 | 0.4440 | 0.0040 | Yes | this paper | Table 1 |
| GIN | 0.3430 | 0.0840 | Yes | this paper | Table 1 |
| GINE | 0.5180 | 0.0490 | Yes | this paper | Table 1 |
| MF | 0.3080 | 0.0140 | Yes | this paper | Table 1 |
| CGCNN | 0.5850 | 0.0290 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6780 | 0.0040 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Velickovic et al. 2018)
- **GATv2** (from: Brody et al. 2022)
- **GIN** (from: Xu et al. 2019)
- **GINE** (from: Hu et al. 2019)
- **MF** (from: Duvenaud et al. 2015)
- **CGCNN** (from: Xie & Grossman 2018)

## Extraction Notes

[HSG-12M] Extracted only the 'Accuracy' metric for the 'HSG-12M' dataset from Table 1 as per the
FOCUS instruction. Other metrics (Macro F1, Top-10 Acc) and other datasets were ignored. The
proposed model is identified as GraphSAGE based on the bold/underline formatting indicating best
results and the context of the paper presenting HSG-12M benchmarks. [HSG-topology] Extracted only
the 'Accuracy' metric for the 'topology' dataset variant from Table 1 as requested. Other metrics
(Macro F1, Top-10 Acc) and other dataset variants were ignored. The proposed model is identified as
GraphSAGE based on the bold/underlined best results in the table. [HSG-one-band] Extracted only the
'Accuracy' metric for the 'one-band' dataset variant from Table 1. Other metrics (Macro F1, Top-10
Acc, Test Loss, Throughput, GPU Memory) and other dataset variants (two-band, three-band, topology,
HSG-12M) were ignored as per instructions. [HSG-two-band] Extracted only the 'Accuracy' metric for
the 'two-band' dataset variant from Table 1. Other tables contained secondary metrics (Test Loss,
Top-5 Accuracy, Throughput, GPU Memory) which were ignored per instructions. The proposed model is
identified as GraphSAGE based on the bold/underline formatting indicating best results and the
context of the paper comparing standard GNNs. [HSG-three-band] Extracted only the 'Accuracy' metric
for the 'three-band' dataset variant from Table 1. Other tables (Test Loss, Top-5 Accuracy,
Throughput, GPU Memory) were ignored as per instructions to focus on the primary metric 'Accuracy'.
The proposed model is identified as GraphSAGE based on the bold/underlined best results and context.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*