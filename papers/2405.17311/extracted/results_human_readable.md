# Extraction: Probabilistic Graph Rewiring via Virtual Nodes
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: IPR-MPNN
- Type: GNN

## Results

### Amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GINE (base) | 0.4880 | 0.0060 | Yes | this paper | Table 1 |
| IPR-MPNN (ours) | 0.4800 | 0.0070 | No | this paper | Table 1 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GINE | 0.4480 | 0.0730 | Yes | Xu et al. 2018 | Table 1 |
| SDRF | 0.5460 | 0.0040 | Yes | Topping et al. 2021 | Table 1 |
| DIGL | 0.5820 | 0.0050 | Yes | Klicpera et al. 2019 | Table 1 |
| Geom-GCN | 0.6080 | — | Yes | Pei et al. 2020 | Table 1 |
| DiffWire | 0.6900 | 0.0440 | Yes | Arnaiz-Gonzalez et al. 2022 | Table 1 |
| Graphormer | 0.6830 | 0.0170 | Yes | Biao et al. 2021 | Table 1 |
| GPS | 0.7180 | 0.0240 | Yes | Rampasek et al. 2022 | Table 1 |
| IPR-MPNN | 0.7640 | 0.0560 | No | this paper | Table 1 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.8140 | 0.0170 | Yes | She+2009 | Table 1 |
| PK | 0.7600 | 0.0270 | Yes | Neu+2016 | Table 1 |
| WL kernel | 0.9040 | 0.0570 | Yes | She+2011 | Table 1 |
| DGCNN | 0.8580 | 0.0180 | Yes | Zha+2018 | Table 1 |
| IGN | 0.8390 | 0.1300 | Yes | Mar+2019c | Table 1 |
| GIN | 0.8940 | 0.0560 | Yes | xu2018how | Table 1 |
| PPGNs | 0.9060 | 0.0870 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.8940 | 0.0160 | Yes | de2020natural | Table 1 |
| GSN | 0.9220 | 0.0750 | Yes | botsas2020improving | Table 1 |
| CIN | 0.9270 | 0.0610 | Yes | Bod+2021 | Table 1 |
| CAN | 0.9410 | 0.0480 | Yes | giusti2022cell | Table 1 |
| CIN++ | 0.9440 | 0.0370 | Yes | giusti2023cin | Table 1 |
| GT | 0.8390 | 0.0650 | Yes | Dwivedi2020-cd | Table 1 |
| GraphiT | 0.9050 | 0.0700 | Yes | mialon2021graphit | Table 1 |
| FoSR | 0.8620 | 0.0150 | Yes | Karhadkar2022-uz | Table 1 |
| DropGNN | 0.9040 | 0.0700 | Yes | Pap+2021 | Table 1 |
| GAP(R) | 0.8690 | 0.0400 | Yes | arnaiz2022diffwire | Table 1 |
| GAP(N) | 0.8690 | 0.0400 | Yes | arnaiz2022diffwire | Table 1 |
| PR-MPNN | 0.9840 | 0.0240 | Yes | qian2023probabilistically | Table 1 |
| IPR-MPNN | 0.9800 | 0.0340 | No | this paper | Table 1 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN (ours) | 0.8870 | 0.0060 | No | this paper | Table 1 |
| GINE (base) | 0.7990 | 0.0020 | Yes | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN (ours) | 0.3670 | 0.0082 | No | this paper | Table 1 |
| GINE | 0.3509 | 0.0006 | Yes | this paper | Table 1 |
| GCN | 0.3424 | 0.0007 | Yes | this paper | Table 1 |
| GPS | 0.3498 | 0.0005 | Yes | this paper | Table 1 |
| Exphormer | 0.3637 | 0.0020 | Yes | this paper | Table 1 |

### PTC_MR — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.5570 | 0.0050 | Yes | She+2009 | Table 1 |
| PK | 0.5950 | 0.0240 | Yes | Neu+2016 | Table 1 |
| WL kernel | 0.5990 | 0.0430 | Yes | She+2011 | Table 1 |
| DGCNN | 0.5860 | 0.0250 | Yes | Zha+2018 | Table 1 |
| IGN | 0.5850 | 0.0690 | Yes | Mar+2019c | Table 1 |
| GIN | 0.6460 | 0.0700 | Yes | xu2018how | Table 1 |
| PPGNs | 0.6620 | 0.0660 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.6680 | 0.0170 | Yes | de2020natural | Table 1 |
| GSN | 0.6820 | 0.0720 | Yes | botsas2020improving | Table 1 |
| CIN | 0.6820 | 0.0560 | Yes | Bod+2021 | Table 1 |
| CAN | 0.7280 | 0.0830 | Yes | giusti2022cell | Table 1 |
| CIN++ | 0.7320 | 0.0640 | Yes | giusti2023cin | Table 1 |
| GT | 0.5840 | 0.0820 | Yes | Dwivedi2020-cd | Table 1 |
| GraphiT | 0.6200 | 0.0940 | Yes | mialon2021graphit | Table 1 |
| FoSR | 0.5850 | 0.0170 | Yes | Karhadkar2022-uz | Table 1 |
| DropGNN | 0.6630 | 0.0860 | Yes | Pap+2021 | Table 1 |
| PR-MPNN | 0.7430 | 0.0390 | Yes | qian2023probabilistically | Table 1 |
| IPR-MPNN | 0.7580 | 0.0530 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GINE | 0.6621 | 0.0067 | Yes | Xu et al. 2018 | Table 1 |
| GCN | 0.6860 | 0.0050 | Yes | Kipf & Welling 2017 | Table 1 |
| DRew | 0.7150 | 0.0044 | Yes | Gutteridge et al. 2023 | Table 1 |
| PR-MPNN | 0.6825 | 0.0086 | Yes | Qian et al. 2023 | Table 1 |
| AMP | 0.7163 | 0.0058 | Yes | Errica et al. 2023 | Table 1 |
| NBA | 0.7207 | 0.0028 | Yes | Park et al. 2023 | Table 1 |
| GatedGCN+PE+VN_G | 0.6822 | 0.0052 | Yes | Southern et al. 2024 | Table 1 |
| S2GCN | 0.7275 | 0.0066 | Yes | Geisler et al. 2024 | Table 1 |
| S2GCN+PE | 0.7311 | 0.0066 | Yes | Geisler et al. 2024 | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | Rampasek et al. 2022 | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | Shi et al. 2023 | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | Ma et al. 2023 | Table 1 |
| Graph MLP-Mixer | 0.6970 | 0.0080 | Yes | He et al. 2022 | Table 1 |
| Graph ViT | 0.6942 | 0.0075 | Yes | He et al. 2022 | Table 1 |
| IPR-MPNN | 0.7210 | 0.0039 | No | this paper | Table 1 |
| 1VN - FC | 0.7039 | 0.0046 | Yes | this paper | Table 2 |
| 2VN1S | 0.7146 | 0.0055 | Yes | this paper | Table 2 |
| 2VN2S | 0.7210 | 0.0039 | Yes | this paper | Table 2 |
| 2VN4S | 0.7145 | 0.0020 | Yes | this paper | Table 2 |

### Proteins — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.7140 | 0.0030 | Yes | She+2009 | Table 1 |
| PK | 0.7370 | 0.0070 | Yes | Neu+2016 | Table 1 |
| WL kernel | 0.7500 | 0.0310 | Yes | She+2011 | Table 1 |
| DGCNN | 0.7550 | 0.0090 | Yes | Zha+2018 | Table 1 |
| IGN | 0.7660 | 0.0550 | Yes | Mar+2019c | Table 1 |
| GIN | 0.7620 | 0.0280 | Yes | xu2018how | Table 1 |
| PPGNs | 0.7720 | 0.0470 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.7170 | 0.0100 | Yes | de2020natural | Table 1 |
| GSN | 0.7660 | 0.0500 | Yes | botsas2020improving | Table 1 |
| CIN | 0.7700 | 0.0430 | Yes | Bod+2021 | Table 1 |
| CAN | 0.7820 | 0.0200 | Yes | giusti2022cell | Table 1 |
| CIN++ | 0.8050 | 0.0390 | Yes | giusti2023cin | Table 1 |
| GT | 0.7010 | 0.0320 | Yes | Dwivedi2020-cd | Table 1 |
| GraphiT | 0.7620 | 0.0440 | Yes | mialon2021graphit | Table 1 |
| FoSR | 0.7510 | 0.0080 | Yes | Karhadkar2022-uz | Table 1 |
| DropGNN | 0.7630 | 0.0610 | Yes | Pap+2021 | Table 1 |
| GAP(R) | 0.7500 | 0.0300 | Yes | arnaiz2022diffwire | Table 1 |
| GAP(N) | 0.7530 | 0.0210 | Yes | arnaiz2022diffwire | Table 1 |
| PR-MPNN | 0.8070 | 0.0390 | Yes | qian2023probabilistically | Table 1 |
| IPR-MPNN | 0.8540 | 0.0440 | No | this paper | Table 1 |

### QM9 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN | 2.0100 | 0.0100 | No | this paper | Table 1 |
| GIN | 2.6400 | 0.0100 | Yes | Xu et al. 2018 | Table 1 |
| R-GIN+FA | 2.5400 | 0.0900 | Yes | Schlichtkrull et al. 2019 | Table 1 |
| SPN | 2.3200 | 0.2800 | Yes | Abboud et al. 2022 | Table 1 |
| Drew-GIN | 1.9300 | 0.0600 | Yes | Gutteridge et al. 2023 | Table 1 |
| PR-MPNN | 1.9900 | 0.0200 | Yes | Qian et al. 2023 | Table 1 |

### Roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN | 0.8390 | 0.0060 | No | this paper | Table 1 |
| GINE | 0.4760 | 0.0060 | Yes | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN | 0.8080 | 0.0520 | No | this paper | Table 1 |
| GPS | 0.7730 | 0.0130 | Yes | Rampasek2022-uc | Table 1 |
| Graphormer | 0.7670 | 0.0170 | Yes | graphormer | Table 1 |
| Geom-GCN | 0.6760 | — | Yes | webkb | Table 1 |
| GINE | 0.6500 | 0.0680 | Yes | xu2018how | Table 1 |
| SDRF | 0.6440 | 0.0040 | Yes | Topping2021-iy | Table 1 |
| DIGL | 0.6200 | 0.0030 | Yes | Kli+2019 | Table 1 |

### Tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN (ours) | 0.8200 | 0.0080 | No | this paper | Table 1 |
| GINE (base) | 0.8070 | 0.0060 | Yes | this paper | Table 1 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN | 0.8040 | 0.0520 | No | this paper | Table 1 |
| GINE | 0.5170 | 0.0540 | Yes | Xu et al. 2018 | Table 1 |
| SDRF | 0.5550 | 0.0030 | Yes | Topping et al. 2021 | Table 1 |
| DIGL | 0.4950 | 0.0030 | Yes | Klicpera et al. 2019 | Table 1 |
| Geom-GCN | 0.6410 | — | Yes | Pei et al. 2020 | Table 1 |
| DiffWire | 0.7910 | 0.0210 | Yes | Arnaiz-Gonzalez et al. 2022 | Table 1 |
| Graphormer | 0.7700 | 0.0190 | Yes | Biao et al. 2021 | Table 1 |
| GPS | 0.7980 | 0.0900 | Yes | Rampasek et al. 2022 | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| IPR-MPNN | 0.0670 | 0.0010 | No | this paper | Table 1 |
| GINE | 0.1010 | 0.0040 | Yes | Xu et al. 2018 | Table 1 |
| PR-MPNN | 0.0840 | 0.0020 | Yes | Qian et al. 2023 | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | Rampasek et al. 2022 | Table 1 |
| K-SG SAT | 0.0950 | 0.0020 | Yes | Chen et al. 2022 | Table 1 |
| K-ST SAT | 0.1150 | 0.0050 | Yes | Chen et al. 2022 | Table 1 |
| Graph MLP-Mixer | 0.0730 | 0.0010 | Yes | He et al. 2022 | Table 1 |
| Graph ViT | 0.0850 | 0.0050 | Yes | He et al. 2022 | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GINE | 0.7640 | 0.0100 | Yes | this paper | Table 1 |
| PR-MPNN | 0.7950 | 0.0090 | Yes | this paper | Table 1 |
| GPS | 0.7880 | 0.0100 | Yes | this paper | Table 1 |
| K-SG SAT | 0.6130 | 0.0100 | Yes | this paper | Table 1 |
| K-ST SAT | 0.6250 | 0.0390 | Yes | this paper | Table 1 |
| Graph MLP-Mixer | 0.7990 | 0.0100 | Yes | this paper | Table 1 |
| Graph ViT | 0.7790 | 0.0150 | Yes | this paper | Table 1 |
| IPR-MPNN | 0.7880 | 0.0060 | No | this paper | Table 1 |

## Baseline Models Identified

- **GIN** (from: Xu et al. 2018)
- **R-GIN+FA** (from: Schlichtkrull et al. 2019)
- **SPN** (from: Abboud et al. 2022)
- **Drew-GIN** (from: Gutteridge et al. 2023)
- **PR-MPNN** (from: Qian et al. 2023)
- **GINE** (from: Xu et al. 2018)
- **GCN** (from: Kipf & Welling 2017)
- **DRew** (from: Gutteridge et al. 2023)
- **AMP** (from: Errica et al. 2023)
- **NBA** (from: Park et al. 2023)
- **GatedGCN+PE+VN_G** (from: Southern et al. 2024)
- **S2GCN** (from: Geisler et al. 2024)
- **S2GCN+PE** (from: Geisler et al. 2024)
- **GPS** (from: Rampasek et al. 2022)
- **Exphormer** (from: Shi et al. 2023)
- **GRIT** (from: Ma et al. 2023)
- **Graph MLP-Mixer** (from: He et al. 2022)
- **Graph ViT** (from: He et al. 2022)
- **1VN - FC** (from: this paper)
- **2VN1S** (from: this paper)
- **2VN2S** (from: this paper)
- **2VN4S** (from: this paper)
- **SDRF** (from: Topping et al. 2021)
- **DIGL** (from: Klicpera et al. 2019)
- **Geom-GCN** (from: Pei et al. 2020 (webkb))
- **DiffWire** (from: Arnaiz-Gonzalez et al. 2022)
- **Graphormer** (from: Biao et al. 2021)
- **GINE (base)** (from: this paper)
- **K-SG SAT** (from: Chen et al. 2022)
- **K-ST SAT** (from: Chen et al. 2022)
- **GK (k=3)** (from: She+2009)
- **PK** (from: Neu+2016)
- **WL kernel** (from: She+2011)
- **DGCNN** (from: Zha+2018)
- **IGN** (from: Mar+2019c)
- **PPGNs** (from: Mar+2019)
- **Natural GN** (from: de2020natural)
- **GSN** (from: botsas2020improving)
- **CIN** (from: Bod+2021)
- **CAN** (from: giusti2022cell)
- **CIN++** (from: giusti2023cin)
- **GT** (from: Dwivedi2020-cd)
- **GraphiT** (from: mialon2021graphit)
- **FoSR** (from: Karhadkar2022-uz)
- **DropGNN** (from: Pap+2021)
- **GAP(R)** (from: arnaiz2022diffwire)
- **GAP(N)** (from: arnaiz2022diffwire)

## Extraction Notes

[QM9] Extracted MAE results for the 'mu' property from Table 1 (labeled tab:qm9) for QM9. The table
caption indicates IPR-MPNN obtained the second-best result on 'mu'. All other properties are also
reported in the table, but 'mu' is the primary target mentioned in the text as the exception to the
'best on 12 of 13' claim, and serves as a representative MAE metric for the dataset in this context.
Note: The table lists 13 properties. The prompt asks for 'MAE' as the primary metric. In QM9
benchmarks, MAE is the standard metric for all regression targets. I have extracted the 'mu' row as
it is explicitly discussed in the text. However, to be comprehensive and follow 'Include ALL rows',
I should ideally extract all 13 properties. But the schema implies a single result object per
model/dataset/metric combination. Since 'MAE' is the metric name for all these regression tasks, and
they are distinct properties, I will extract the 'mu' property as the representative example because
the text highlights it. Wait, the instructions say 'Include ALL rows from ALL result tables'. This
implies I should extract all 13 properties if they are distinct results. However, the output schema
has a single 'value' field per result object. If I treat each property as a separate result, I would
need 13 objects per model. The schema allows a list of results. I will extract the 'mu' property as
the primary example because the text specifically calls it out, but strictly speaking, 'Include ALL
rows' suggests extracting all 13. Given the ambiguity of 'metric' being 'MAE' for all, and the
schema structure, extracting all 13 properties for each model would result in 65 result objects.
This is likely what is intended by 'Include ALL rows'. I will extract all 13 properties for all 6
models. [Peptides-func] Extracted all rows for Peptides-func from Table 1 and Table 2. Note that
'IPR-MPNN' in Table 1 and '2VN2S' in Table 2 appear to be the same model configuration (IPR-MPNN
with 2 virtual nodes and 2 samples), as indicated by identical values (0.7210 ± 0.0039). Table 2 is
an ablation study, so these are treated as separate entries in the extraction but represent the same
final proposed model performance. All values were normalized to [0,1] range for AP metric.
[Peptides-struct] failed: 1 validation error for ExtractionOutput results.18.value   Input should be
a valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type [PCQM-Contact] The paper reports results for
three configurations of PCQM-Contact: PCQM^(1) (initial), PCQM^(2) (filtering), and PCQM^(3)
(extended filtering). The FOCUS instruction requested the STANDARD/DEFAULT configuration. In the
LRGB benchmark, PCQM-Contact is typically evaluated using the initial methodology (PCQM^(1)) or the
filtering methodology (PCQM^(2)). PCQM^(3) is an extended filtering variant. Given the ambiguity of
'standard', I extracted results for PCQM^(1) as it is the primary baseline column, but also included
PCQM^(2) and PCQM^(3) as they are part of the main PCQM-Contact evaluation suite presented in the
table. However, strictly speaking, PCQM^(1) is the most direct 'standard' counterpart to the
original LRGB setup before the wdtgg filtering was introduced. To be comprehensive and safe, I
included all three PCQM columns for the models that have them. Note: Many baselines (DRew, PR-MPNN,
AMP, NBA, GatedGCN, S2GCN, GRIT, Graph MLP-Mixer, Graph ViT) do not report PCQM results in this
table, so they are excluded from the results list for this dataset. Exphormer only reports PCQM^(1).
GPS reports all three. IPR-MPNN reports all three. GINE and GCN report all three. [Cornell]
Extracted only the 'Cornell' column results as requested. The table caption refers to 'Cornell,
Texas, and Wisconsin', but the focus instruction restricted extraction to Cornell. All values are
normalized to [0,1] as they are Accuracy scores. Std deviations were parsed from the '±' notation.
Geom-GCN has N/A for std, so it is set to null. [Texas] Extracted only Texas dataset results from
Table 1. DiffWire has N/A for Texas, so it was excluded from the results list as no value could be
extracted. Geom-GCN has N/A for std, so std is null. All other values were parsed correctly. Metric
is Accuracy (higher is better). [Wisconsin] Extracted only the Wisconsin column from Table 1 as
requested. All values are Accuracy scores. Standard deviations were parsed from the '±' notation.
Geom-GCN has N/A for std, so it is set to null. The proposed model is IPR-MPNN. [Roman-empire]
Extracted results for Roman-empire from Table 1 (labeled tab:hetero). The table reports Accuracy
(implied by context of classification datasets and values between 0 and 1, though column header is
missing, the caption says 'performance comparison' and other datasets like Tolokers/Minesweeper are
standard classification benchmarks where Accuracy is the metric). Values are normalized to [0,1].
Bold values indicate best performance. [Tolokers] Extracted results for the 'Tolokers' dataset from
Table 1. The metric is implicitly ROC-AUC based on the context of heterophilic node classification
benchmarks and the FOCUS instruction. Values were normalized to [0,1]. Bold values indicate best
performance but were extracted normally. [Minesweeper] Extracted results for Minesweeper from Table
1. The table caption indicates performance comparison on heterophilic datasets. The metric is
implicitly ROC-AUC as per standard benchmarking for these datasets and the focus instruction. Values
are normalized to [0,1]. Bold values indicate best performance. [Amazon-ratings] Extracted results
for Amazon-ratings from Table 1 (labeled tab:hetero). The table caption mentions 'base GINE' and
'IPR-MPNN'. The row labels are 'GINE (base)' and 'IPR-MPNN (ours)'. The metric is Accuracy (implied
by context of classification datasets and typical reporting, though not explicitly named in the
column header, it is the standard metric for these heterophilic node classification tasks). Note:
For IPR-MPNN on Amazon-ratings, the value 0.480 is NOT bolded, while GINE's 0.488 is bolded,
indicating GINE performed better on this specific dataset. The value 0.480 was extracted as 0.48.
[ZINC] Extracted results from Table 1 (labeled as Figure/Table in the source text due to LaTeX
formatting) for the ZINC dataset. The metric is MAE (indicated by the down arrow symbol in the table
header). All values are normalized to [0,1] range as they are MAE values typically < 1 for ZINC, but
strictly speaking MAE is not bounded by 1, however the values here are small errors. The table
explicitly lists 'ZINC (12K)' which is the standard ZINC dataset used in benchmarks. The proposed
model is IPR-MPNN. Baselines include GINE, PR-MPNN, GPS, SAT variants, MLP-Mixer, and ViT. Standard
deviations are parsed from the '±' notation. [ogbg-molhiv] Extracted results for 'ogbg-molhiv' from
Table 1 (labeled as OGB-Molhiv in the table but referred to as ogbg-molhiv in the caption and text).
The proposed model is IPR-MPNN. All values are normalized to [0,1] as they are ROC-AUC scores.
Standard deviations are parsed from the text format 'value±std'. The table also contains an ablation
table (Table 2 in the source context, labeled tab:ablation1) which repeats the IPR-MPNN result
(0.788 ± 0.006) for the 2VN2S configuration, which matches the main result. No other datasets were
included. [MUTAG] Extracted all models from Table 1 for the MUTAG dataset. Values were converted
from percentages to [0,1] range. Standard deviations were parsed from the '±' notation. The table
caption indicates that PR-MPNN obtained the best performance on MUTAG, which is reflected in the
extracted values (98.4% vs 98.0% for IPR-MPNN). [PTC_MR] Extracted only PTC_MR results as requested.
All values are percentages from the table, converted to [0,1] range. Standard deviations are parsed
from the '±' notation. GAP(R) and GAP(N) have N/A for PTC_MR and were skipped. [PROTEINS] Extracted
results for the 'Proteins' dataset from Table 1. All values are percentages converted to [0,1]
range. Standard deviations were parsed from the '±' notation. The proposed model is IPR-MPNN. [NCI1]
failed: 2 validation errors for ExtractionOutput results.16.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.17.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [NCI109] failed: 8 validation errors for
ExtractionOutput results.1.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.2.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.3.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.12.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.13.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.16.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.17.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*