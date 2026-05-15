# Extraction: GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency Model
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: GPS-GCCM
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 55.7100 | 0.3810 | Yes | this paper | Table 1 |
| GIN | 55.2550 | 1.5270 | Yes | this paper | Table 1 |
| GAT | 64.2230 | 0.4550 | Yes | this paper | Table 1 |
| GatedGCN | 67.3120 | 0.3110 | Yes | this paper | Table 1 |
| PNA | 70.3500 | 0.6300 | Yes | this paper | Table 1 |
| DGN | 72.8380 | 0.4170 | Yes | this paper | Table 1 |
| GIN-AK+ | 72.1900 | 0.1300 | Yes | this paper | Table 1 |
| EGT | 68.7020 | 0.4090 | Yes | this paper | Table 1 |
| GRIT | 76.4680 | 0.8810 | Yes | this paper | Table 1 |
| GPS | 72.3560 | 0.3230 | Yes | this paper | Table 1 |
| GPS-LGD | 70.1630 | 0.3570 | Yes | this paper | Table 1 |
| GPS-PCL | 71.8300 | 0.2180 | Yes | this paper | Table 1 |
| GPS-GCCM (ours) | 72.5020 | 0.2870 | No | this paper | Table 1 |
| GPS+Diffusion | 71.9310 | 0.3470 | Yes | this paper | Table 2 |
| GPS+Consistency | 71.8300 | 0.2180 | Yes | this paper | Table 2 |
| GPS+Consistency+Contrastive | 71.9760 | 0.3210 | Yes | this paper | Table 2 |
| GPS+GCCM (ours) | 72.5020 | 0.2870 | No | this paper | Table 2 |
| GRIT-LGD | 71.1670 | 1.3110 | Yes | this paper | Table 3 |
| GRIT-PCL | 75.7200 | 0.7340 | Yes | this paper | Table 3 |
| GRIT-GCCM (ours) | 75.9050 | 0.8420 | No | this paper | Table 3 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 68.4980 | 0.9760 | Yes | this paper | Table 1 |
| GIN | 64.7160 | 1.5530 | Yes | this paper | Table 1 |
| GAT | 70.5870 | 0.4470 | Yes | this paper | Table 1 |
| GatedGCN | 73.8400 | 0.3260 | Yes | this paper | Table 1 |
| SAN | 76.6910 | 0.6500 | Yes | this paper | Table 1 |
| EGT | 79.2320 | 0.3480 | Yes | this paper | Table 1 |
| GRIT | 80.0260 | 0.2770 | Yes | this paper | Table 1 |
| GPS | 77.7800 | 0.2360 | Yes | this paper | Table 1 |
| GPS-LGD | 76.7730 | 0.3010 | Yes | this paper | Table 1 |
| GPS-PCL | 78.1710 | 0.2310 | Yes | this paper | Table 1 |
| GPS-GCCM (ours) | 78.8200 | 0.1870 | No | this paper | Table 1 |
| GPS+Diffusion | 78.3120 | 0.2510 | Yes | this paper | Table 2 |
| GPS+Consistency | 78.1710 | 0.2310 | Yes | this paper | Table 2 |
| GPS+Consistency+Contrastive | 78.2320 | 0.1590 | Yes | this paper | Table 2 |
| GPS+GCCM (ours) | 78.8200 | 0.1870 | No | this paper | Table 2 |
| SAN-LGD | 68.7110 | 0.6760 | Yes | this paper | Table 3 |
| SAN-PCL | 77.4610 | 0.4270 | Yes | this paper | Table 3 |
| SAN-GCCM (ours) | 78.4810 | 0.1760 | No | this paper | Table 3 |
| GRIT-LGD | 64.9130 | 1.6390 | Yes | this paper | Table 3 |
| GRIT-PCL | 78.6430 | 0.8360 | Yes | this paper | Table 3 |
| GRIT-GCCM (ours) | 79.8160 | 0.1370 | No | this paper | Table 3 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | 0.0010 | Yes | this paper | Table 1 |
| GatedGCN | 0.2641 | 0.0045 | Yes | this paper | Table 1 |
| SAN | 0.2592 | 0.0158 | Yes | this paper | Table 1 |
| GPS | 0.3453 | 0.0056 | Yes | this paper | Table 1 |
| GPS-PCL | 0.3816 | 0.0058 | Yes | this paper | Table 1 |
| GPS-GCCM | 0.3856 | 0.0021 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 90.7050 | 0.2180 | Yes | this paper | Table 1 |
| GIN | 96.4850 | 0.2520 | Yes | this paper | Table 1 |
| GAT | 95.5350 | 0.2050 | Yes | this paper | Table 1 |
| GatedGCN | 97.3400 | 0.1430 | Yes | this paper | Table 1 |
| PNA | 97.9400 | 0.1200 | Yes | this paper | Table 1 |
| EGT | 98.1730 | 0.0870 | Yes | this paper | Table 1 |
| GRIT | 98.1080 | 0.1110 | Yes | this paper | Table 1 |
| GPS | 98.0820 | 0.1140 | Yes | this paper | Table 1 |
| GPS-LGD | 95.4610 | 0.6130 | Yes | this paper | Table 1 |
| GPS-PCL | 98.1140 | 0.1830 | Yes | this paper | Table 1 |
| GPS-GCCM (ours) | 98.2360 | 0.0600 | No | this paper | Table 1 |
| GPS+Diffusion | 98.0810 | 0.2410 | Yes | this paper | Table 2 |
| GPS+Consistency | 98.1140 | 0.1830 | Yes | this paper | Table 2 |
| GPS+Consistency+Contrastive | 98.1180 | 0.0560 | Yes | this paper | Table 2 |
| GPS+GCCM (ours) | 98.2360 | 0.0600 | No | this paper | Table 2 |
| GRIT-LGD | 96.5440 | 0.6150 | Yes | this paper | Table 3 |
| GRIT-PCL | 97.9970 | 0.1260 | Yes | this paper | Table 3 |
| GRIT-GCCM (ours) | 98.4730 | 0.0950 | No | this paper | Table 3 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 71.8920 | 0.3340 | Yes | this paper | Table 1 |
| GIN | 85.3870 | 0.1360 | Yes | this paper | Table 1 |
| GAT | 78.2710 | 0.1860 | Yes | this paper | Table 1 |
| GatedGCN | 85.5680 | 0.0880 | Yes | this paper | Table 1 |
| DGN | 86.6800 | 0.0340 | Yes | this paper | Table 1 |
| GIN-AK+ | 86.8500 | 0.0570 | Yes | this paper | Table 1 |
| SAN | 86.5810 | 0.0370 | Yes | this paper | Table 1 |
| EGT | 86.8210 | 0.0200 | Yes | this paper | Table 1 |
| GRIT | 87.1960 | 0.0760 | Yes | this paper | Table 1 |
| GPS | 86.6480 | 0.0650 | Yes | this paper | Table 1 |
| GPS-LGD | 85.6620 | 0.1810 | Yes | this paper | Table 1 |
| GPS-PCL | 86.6950 | 0.0730 | Yes | this paper | Table 1 |
| GPS-GCCM (ours) | 86.7720 | 0.0420 | No | this paper | Table 1 |
| GPS+Diffusion | 86.7410 | 0.1580 | Yes | this paper | Table 2 |
| GPS+Consistency | 86.6950 | 0.0730 | Yes | this paper | Table 2 |
| GPS+Consistency+Contrastive | 86.6760 | 0.0710 | Yes | this paper | Table 2 |
| GPS+GCCM (ours) | 86.7720 | 0.0420 | No | this paper | Table 2 |
| SAN-LGD | 80.7420 | 0.3150 | Yes | this paper | Table 3 |
| SAN-PCL | 86.7680 | 0.0640 | Yes | this paper | Table 3 |
| SAN-GCCM (ours) | 86.8110 | 0.0210 | No | this paper | Table 3 |
| GRIT-LGD | 84.6000 | 1.8410 | Yes | this paper | Table 3 |
| GRIT-PCL | 86.8730 | 0.0600 | Yes | this paper | Table 3 |
| GRIT-GCCM (ours) | 87.2560 | 0.0840 | No | this paper | Table 3 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | this paper | Table 1 |
| GatedGCN | 0.2873 | 0.0219 | Yes | this paper | Table 1 |
| SAN | 0.3230 | 0.0039 | Yes | this paper | Table 1 |
| GPS | 0.3793 | 0.0171 | Yes | this paper | Table 1 |
| GPS-LGD | 0.3912 | 0.0207 | Yes | this paper | Table 1 |
| GPS-PCL | 0.4196 | 0.0086 | Yes | this paper | Table 1 |
| GPS-GCCM | 0.4219 | 0.0102 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 1 |
| PNA | 0.1880 | 0.0040 | Yes | this paper | Table 1 |
| DGN | 0.1680 | 0.0030 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | this paper | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| EGT | 0.1080 | 0.0090 | Yes | this paper | Table 1 |
| GRIT | 0.0590 | 0.0020 | Yes | this paper | Table 1 |
| GPS | 0.0720 | 0.0040 | Yes | this paper | Table 1 |
| GPS-LGD | 0.0850 | 0.0010 | Yes | this paper | Table 1 |
| GPS-PCL | 0.0690 | 0.0010 | Yes | this paper | Table 1 |
| GPS-GCCM (ours) | 0.0710 | 0.0010 | No | this paper | Table 1 |
| GPS+Diffusion | 0.0730 | 0.0070 | Yes | this paper | Table 2 |
| GPS+Consistency | 0.0690 | 0.0010 | Yes | this paper | Table 2 |
| GPS+Consistency+Contrastive | 0.0680 | 0.0030 | Yes | this paper | Table 2 |
| GPS+GCCM (ours) | 0.0710 | 0.0010 | No | this paper | Table 2 |
| SAN-LGD | 0.2360 | 0.0120 | Yes | this paper | Table 3 |
| SAN-PCL | 0.1400 | 0.0020 | Yes | this paper | Table 3 |
| SAN-GCCM (ours) | 0.1310 | 0.0030 | No | this paper | Table 3 |
| GRIT-LGD | 0.1180 | 0.0110 | Yes | this paper | Table 3 |
| GRIT-PCL | 0.0630 | 0.0050 | Yes | this paper | Table 3 |
| GRIT-GCCM (ours) | 0.0590 | 0.0040 | No | this paper | Table 3 |

## Baseline Models Identified

- **GCN** (from: Kipf 2017)
- **GIN** (from: Xu 2019)
- **GAT** (from: Veličković 2018)
- **GatedGCN** (from: Bresson 2018)
- **PNA** (from: Corso 2020)
- **DGN** (from: Beaini 2021)
- **GIN-AK+** (from: Zhao 2022)
- **SAN** (from: Kreuzer 2021)
- **EGT** (from: Hussain 2022)
- **GRIT** (from: 2022)
- **GPS** (from: Rampášek 2023)
- **GPS-LGD** (from: Zhou 2024)
- **GPS-PCL** (from: Li 2025)
- **GPS+Diffusion** (from: this paper)
- **GPS+Consistency** (from: this paper)
- **GPS+Consistency+Contrastive** (from: this paper)
- **SAN-GCCM** (from: this paper)
- **GRIT-GCCM** (from: this paper)
- **SAN-LGD** (from: Zhou 2024)
- **SAN-PCL** (from: Li 2025)
- **GRIT-LGD** (from: Zhou 2024)
- **GRIT-PCL** (from: Li 2025)

## Extraction Notes

[MNIST] Extracted all rows from Table 1, Table 2, and Table 3 that correspond to the MNIST dataset
and the Accuracy metric. Note that Table 3 includes additional backbone variants (SAN-GCCM, GRIT-
GCCM) which are also reported for MNIST. The proposed model name varies slightly in the tables (GPS-
GCCM vs GPS+GCCM vs GRIT-GCCM), but all are variants of the proposed GCCM framework. All values are
test-set results. [CIFAR10] Extracted all CIFAR10 Accuracy results from Table 1, Table 2, and Table
3. Note that GRIT and GRIT-GCCM show significantly higher accuracy in Table 3 compared to Table 1,
likely due to different backbone configurations or experimental settings as hinted by the table
captions (Table 3 shows 'different backbone' results). The values are extracted exactly as reported
in the tables. [PATTERN] Extracted all rows for the PATTERN dataset from Table 1, Table 2, and Table
3. The primary metric is Accuracy. Note that PNA has no result for PATTERN (marked as --). Some
model names in Table 3 include suffixes like '(ours)' which were kept as they appear in the table
for exact matching, though they refer to the same proposed method variants. [CLUSTER] Extracted all
rows for the CLUSTER dataset from Table 1, Table 2, and Table 3. The primary metric is Accuracy. All
values are test-set results. Standard deviations are included where available. Duplicate entries
across tables (e.g., GPS, GPS-GCCM) are preserved as they represent different experimental setups
(main benchmark vs ablation vs backbone variants). [ZINC] Extracted all ZINC MAE results from Table
1, Table 2, and Table 3. Note that Table 3 contains duplicate entries for GPS, GPS-LGD, GPS-PCL, and
GPS-GCCM which are also present in Table 1. These are included as they appear in distinct tables in
the source text. The proposed model name varies slightly across tables (e.g., 'GPS-GCCM (ours)',
'GPS+GCCM (ours)'), but refers to the same proposed method. [PascalVOC-SP] Extracted only PascalVOC-
SP F1 results as requested. Excluded models with missing values (GIN, GAT, PNA, DGN, GIN-AK+, EGT,
GRIT) for this specific dataset/metric combination. All values parsed from Table 1. [COCO-SP]
Extracted only COCO-SP results as requested. Note that GIN, PNA, DGN, GIN-AK+, EGT, GRIT, and GPS-
LGD do not have reported results for COCO-SP in the provided table (marked as '—' or missing). The
primary metric F1 was used. All values are test-set results.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*