# Extraction: arXiv:2406.03671
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: PANDA
- Type: GNN

## Results

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.7230 | 0.0030 | Yes | this paper | Table 2 |
| DIGL | 0.7450 | 0.0030 | Yes | this paper | Table 2 |
| SDRF | 0.7260 | 0.0030 | Yes | this paper | Table 2 |
| FoSR | 0.7230 | 0.0040 | Yes | this paper | Table 2 |
| BORF | 0.7380 | 0.0020 | Yes | this paper | Table 2 |
| PANDA | 0.7530 | 0.0030 | No | this paper | Table 2 |

### Collab — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.3378 | 0.0049 | Yes | this paper | Table 1 |
| Last Layer FA | 0.3332 | 0.0043 | Yes | this paper | Table 1 |
| Every Layer FA | 0.5180 | 0.0042 | Yes | this paper | Table 1 |
| DIGL | 0.1553 | 0.0029 | Yes | this paper | Table 1 |
| SDRF | 0.3345 | 0.0047 | Yes | this paper | Table 1 |
| FoSR | 0.3384 | 0.0058 | Yes | this paper | Table 1 |
| GTR | 0.3305 | 0.0040 | Yes | this paper | Table 1 |
| CT-Layer | 0.5215 | 0.0042 | Yes | this paper | Table 1 |
| PANDA | 0.6840 | 0.0045 | No | this paper | Table 1 |
| GIN (None) | 0.7299 | 0.0038 | Yes | this paper | Table 1 |
| R-GCN | 0.3360 | 0.0105 | Yes | this paper | Table 1 |
| PANDA-GCN | 0.6840 | 0.0045 | No | this paper | Table 1 |
| Degree | 0.6816 | 0.0047 | Yes | this paper | Table 1 |
| Betweenness | 0.6784 | 0.0055 | Yes | this paper | Table 1 |
| Closeness | 0.6840 | 0.0045 | Yes | this paper | Table 1 |
| PageRank | 0.6754 | 0.0050 | Yes | this paper | Table 1 |
| Load | 0.6780 | 0.0051 | Yes | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.8670 | 0.0030 | Yes | this paper | Table 1 |
| DIGL | 0.8320 | 0.0020 | Yes | this paper | Table 1 |
| SDRF | 0.8630 | 0.0030 | Yes | this paper | Table 1 |
| FoSR | 0.8590 | 0.0030 | Yes | this paper | Table 1 |
| BORF | 0.8750 | 0.0020 | Yes | this paper | Table 1 |
| PANDA | 0.8700 | 0.0030 | No | this paper | Table 1 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.4150 | 0.0180 | Yes | this paper | Table 1 |
| DIGL | 0.4450 | 0.0120 | Yes | this paper | Table 1 |
| SDRF | 0.4220 | 0.0150 | Yes | this paper | Table 1 |
| FoSR | 0.4020 | 0.0160 | Yes | this paper | Table 1 |
| BORF | 0.5080 | 0.0110 | Yes | this paper | Table 1 |
| PANDA | 0.4750 | 0.0140 | No | this paper | Table 1 |

### Enzymes — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.2767 | 0.0116 | Yes | this paper | Table 1 |
| GCN + Last Layer FA | 0.2647 | 0.0120 | Yes | this paper | Table 1 |
| GCN + Every Layer FA | 0.1833 | 0.0104 | Yes | this paper | Table 1 |
| GCN + DIGL | 0.2752 | 0.0105 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.2837 | 0.0117 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.2507 | 0.0099 | Yes | this paper | Table 1 |
| GCN + BORF | 0.2470 | 0.0100 | Yes | this paper | Table 1 |
| GCN + GTR | 0.2752 | 0.0099 | Yes | this paper | Table 1 |
| GCN + CT-Layer | 0.1738 | 0.0103 | Yes | this paper | Table 1 |
| PANDA (GCN) | 0.3155 | 0.0123 | No | this paper | Table 1 |
| GIN (None) | 0.3380 | 0.0011 | Yes | this paper | Table 1 |
| GIN + Last Layer FA | 0.4740 | 0.0139 | Yes | this paper | Table 1 |
| GIN + Every Layer FA | 0.2838 | 0.0105 | Yes | this paper | Table 1 |
| GIN + DIGL | 0.3572 | 0.0120 | Yes | this paper | Table 1 |
| GIN + SDRF | 0.3582 | 0.0109 | Yes | this paper | Table 1 |
| GIN + FoSR | 0.2920 | 0.0137 | Yes | this paper | Table 1 |
| GIN + BORF | 0.3550 | 0.0120 | Yes | this paper | Table 1 |
| GIN + GTR | 0.3057 | 0.0142 | Yes | this paper | Table 1 |
| GIN + CT-Layer | 0.1658 | 0.0091 | Yes | this paper | Table 1 |
| PANDA (GIN) | 0.4620 | 0.0141 | No | this paper | Table 1 |
| R-GCN | 0.2860 | 0.0119 | Yes | this paper | Table 2 |
| PANDA-GCN | 0.3155 | 0.0123 | No | this paper | Table 2 |
| PANDA-GCN (Degree) | 0.3112 | 0.0126 | No | this paper | Table 3 |
| PANDA-GCN (Betweenness) | 0.2960 | 0.0121 | No | this paper | Table 3 |
| PANDA-GCN (Closeness) | 0.2997 | 0.0123 | No | this paper | Table 3 |
| PANDA-GCN (PageRank) | 0.3155 | 0.0123 | No | this paper | Table 3 |
| PANDA-GCN (Load) | 0.2817 | 0.0109 | No | this paper | Table 3 |
| R-GCN (None) | 0.2860 | 0.0119 | Yes | this paper | Table 4 |
| R-GCN + Last Layer FA | 0.2823 | 0.0114 | Yes | this paper | Table 4 |
| R-GCN + Every Layer FA | 0.3340 | 0.0114 | Yes | this paper | Table 4 |

### IMDB-Binary — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.4977 | 0.0082 | Yes | this paper | Table 1 |
| GCN + Last Layer FA | 0.4898 | 0.0095 | Yes | this paper | Table 1 |
| GCN + Every Layer FA | 0.4817 | 0.0080 | Yes | this paper | Table 1 |
| GCN + DIGL | 0.4991 | 0.0084 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.4940 | 0.0090 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.4966 | 0.0086 | Yes | this paper | Table 1 |
| GCN + BORF | 0.5010 | 0.0090 | Yes | this paper | Table 1 |
| GCN + GTR | 0.4992 | 0.0099 | Yes | this paper | Table 1 |
| GCN + CT-Layer | 0.5032 | 0.0094 | Yes | this paper | Table 1 |
| PANDA | 0.6376 | 0.0101 | No | this paper | Table 1 |
| GIN (None) | 0.7018 | 0.0099 | Yes | this paper | Table 1 |
| GIN + Last Layer FA | 0.7091 | 0.0079 | Yes | this paper | Table 1 |
| GIN + Every Layer FA | 0.4916 | 0.0087 | Yes | this paper | Table 1 |
| GIN + DIGL | 0.6439 | 0.0091 | Yes | this paper | Table 1 |
| GIN + SDRF | 0.6972 | 0.0115 | Yes | this paper | Table 1 |
| GIN + FoSR | 0.7121 | 0.0092 | Yes | this paper | Table 1 |
| GIN + BORF | 0.7130 | 0.0150 | Yes | this paper | Table 1 |
| GIN + GTR | 0.7128 | 0.0086 | Yes | this paper | Table 1 |
| GIN + CT-Layer | 0.5000 | 0.0097 | Yes | this paper | Table 1 |
| R-GCN | 0.5001 | 0.0092 | Yes | this paper | Table 2 |
| PANDA-GCN | 0.6376 | 0.0101 | No | this paper | Table 2 |
| PANDA-GCN (Degree) | 0.6210 | 0.0104 | No | this paper | Table 3 |
| PANDA-GCN (Betweenness) | 0.5963 | 0.0115 | No | this paper | Table 3 |
| PANDA-GCN (Closeness) | 0.6116 | 0.0099 | No | this paper | Table 3 |
| PANDA-GCN (PageRank) | 0.6376 | 0.0101 | No | this paper | Table 3 |
| PANDA-GCN (Load) | 0.5984 | 0.0115 | No | this paper | Table 3 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.4420 | 0.0150 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.4390 | 0.0160 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.4600 | 0.0160 | Yes | this paper | Table 1 |
| GCN + BORF | 0.4560 | 0.0150 | Yes | this paper | Table 1 |
| GCN + PANDA | 0.5540 | 0.0160 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.3478 | 0.0013 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.3473 | 0.0007 | Yes | this paper | Table 1 |
| GCN + BORF | 0.3514 | 0.0009 | Yes | this paper | Table 1 |
| GCN + PANDA | 0.3272 | 0.0001 | No | this paper | Table 1 |

### Proteins — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.7098 | 0.0074 | Yes | this paper | Table 1 |
| GCN + Last Layer FA | 0.7102 | 0.0096 | Yes | this paper | Table 1 |
| GCN + Every Layer FA | 0.6004 | 0.0092 | Yes | this paper | Table 1 |
| GCN + DIGL | 0.7061 | 0.0073 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.7092 | 0.0079 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.7342 | 0.0081 | Yes | this paper | Table 1 |
| GCN + BORF | 0.7100 | 0.0080 | Yes | this paper | Table 1 |
| GCN + GTR | 0.7259 | 0.0248 | Yes | this paper | Table 1 |
| GCN + CT-Layer | 0.6036 | 0.0106 | Yes | this paper | Table 1 |
| PANDA | 0.7600 | 0.0077 | No | this paper | Table 1 |
| GIN (None) | 0.7080 | 0.0083 | Yes | this paper | Table 1 |
| GIN + Last Layer FA | 0.7230 | 0.0067 | Yes | this paper | Table 1 |
| GIN + Every Layer FA | 0.7037 | 0.0091 | Yes | this paper | Table 1 |
| GIN + DIGL | 0.7076 | 0.0077 | Yes | this paper | Table 1 |
| GIN + SDRF | 0.6981 | 0.0079 | Yes | this paper | Table 1 |
| GIN + FoSR | 0.7511 | 0.0082 | Yes | this paper | Table 1 |
| GIN + BORF | 0.7420 | 0.0080 | Yes | this paper | Table 1 |
| GIN + GTR | 0.7313 | 0.0069 | Yes | this paper | Table 1 |
| GIN + CT-Layer | 0.6111 | 0.0118 | Yes | this paper | Table 1 |
| R-GCN | 0.6952 | 0.0073 | Yes | this paper | Table 2 |
| PANDA-GCN | 0.7600 | 0.0077 | No | this paper | Table 2 |
| PANDA-GCN (Degree) | 0.7538 | 0.0080 | No | this paper | Table 3 |
| PANDA-GCN (Betweenness) | 0.7459 | 0.0079 | No | this paper | Table 3 |
| PANDA-GCN (Closeness) | 0.7600 | 0.0077 | No | this paper | Table 3 |
| PANDA-GCN (PageRank) | 0.7410 | 0.0085 | No | this paper | Table 3 |
| PANDA-GCN (Load) | 0.7419 | 0.0081 | No | this paper | Table 3 |

### Reddit-Binary — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.6825 | 0.0110 | Yes | this paper | Table 1 |
| Last Layer FA | 0.6848 | 0.0095 | Yes | this paper | Table 1 |
| Every Layer FA | 0.4849 | 0.0104 | Yes | this paper | Table 1 |
| DIGL | 0.4998 | 0.0068 | Yes | this paper | Table 1 |
| SDRF | 0.6862 | 0.0085 | Yes | this paper | Table 1 |
| FoSR | 0.7033 | 0.0073 | Yes | this paper | Table 1 |
| GTR | 0.6899 | 0.0061 | Yes | this paper | Table 1 |
| CT-Layer | 0.5158 | 0.0102 | Yes | this paper | Table 1 |
| PANDA | 0.8069 | 0.0072 | No | this paper | Table 1 |
| GIN (None) | 0.8679 | 0.0106 | Yes | this paper | Table 1 |
| R-GCN | 0.4985 | 0.0065 | Yes | this paper | Table 1 |
| PANDA-GCN | 0.8069 | 0.0072 | No | this paper | Table 1 |
| PANDA-GCN (Degree) | 0.8069 | 0.0072 | No | this paper | Table 1 |
| PANDA-GCN (Betweenness) | 0.8000 | 0.0066 | No | this paper | Table 1 |
| PANDA-GCN (Closeness) | 0.7970 | 0.0066 | No | this paper | Table 1 |
| PANDA-GCN (PageRank) | 0.8034 | 0.0083 | No | this paper | Table 1 |
| PANDA-GCN (Load) | 0.7950 | 0.0073 | No | this paper | Table 1 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.4250 | 0.0270 | Yes | this paper | Table 1 |
| DIGL | 0.3520 | 0.0300 | Yes | this paper | Table 1 |
| SDRF | 0.4240 | 0.0250 | Yes | this paper | Table 1 |
| FoSR | 0.4250 | 0.0190 | Yes | this paper | Table 1 |
| BORF | 0.4260 | 0.0280 | Yes | this paper | Table 1 |
| PANDA | 0.4310 | 0.0090 | No | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.4420 | 0.0150 | Yes | this paper | Table 1 |
| DIGL | 0.5360 | 0.0150 | Yes | this paper | Table 1 |
| SDRF | 0.4390 | 0.0160 | Yes | this paper | Table 1 |
| FoSR | 0.4600 | 0.0160 | Yes | this paper | Table 1 |
| BORF | 0.4940 | 0.0120 | Yes | this paper | Table 1 |
| PANDA | 0.5540 | 0.0160 | No | this paper | Table 1 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.4460 | 0.0140 | Yes | this paper | Table 1 |
| DIGL | 0.5170 | 0.0130 | Yes | this paper | Table 1 |
| SDRF | 0.4620 | 0.0120 | Yes | this paper | Table 1 |
| FoSR | 0.4830 | 0.0130 | Yes | this paper | Table 1 |
| BORF | 0.5030 | 0.0090 | Yes | this paper | Table 1 |
| PANDA | 0.5820 | 0.0140 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN (None)**
- **Last Layer FA**
- **Every Layer FA**
- **DIGL**
- **SDRF**
- **FoSR**
- **BORF**
- **GTR**
- **CT-Layer**
- **GIN (None)**
- **R-GCN**
- **GCN** (from: Kipf & Welling 2017)
- **GIN** (from: Xu et al. 2019)
- **Degree** (from: this paper)
- **Betweenness** (from: this paper)
- **Closeness** (from: this paper)
- **PageRank** (from: this paper)
- **Load** (from: this paper)

## Extraction Notes

[Reddit-Binary] Extracted all rows from Table 1 (tab:main) and Table 1 (tab:centrality-gcn) for the
Reddit-Binary dataset. Note that Table 1 (tab:relational) and Table 1 (tab:main-rgnn) contain
redundant or partial data already covered in Table 1 (tab:main). The 'PANDA' model appears twice in
Table 1 (tab:main) corresponding to GCN and GIN backbones. The centrality table (tab:centrality-gcn)
lists specific variants of PANDA-GCN based on centrality measure; these are included as separate
rows. BORF results are 'Time-out' and thus excluded. All values were divided by 100 to normalize
percentages to [0,1]. [IMDB-Binary] Extracted all results for IMDB-Binary from Table 1, Table 2, and
Table 3. Table 1 contains results for GCN and GIN baselines with various rewiring/attention methods.
Table 2 compares R-GCN and PANDA-GCN. Table 3 compares PANDA-GCN with different centrality metrics.
Note that 'PANDA' in Table 1 appears twice: once for GCN backbone and once for GIN backbone. These
are treated as separate entries in the results list but refer to the same proposed method name. The
values are percentages from the table, converted to [0,1] range as per instructions. Standard
deviations are parsed from the '±' or 'std' notation. [Mutag] failed: JSON parse error from
'qwen3.6-35b-a3b': could not extract valid JSON [Enzymes] Extracted all rows from Table 1, Table 2,
Table 3, and the visible portion of Table 4 that contain results for the 'Enzymes' dataset. Table 4
is cut off in the provided text, so only the first three rows for R-GCN variants are included.
Values are normalized from percentages to [0,1] range. Standard deviations are parsed from the '±'
or 'std' notation. [Proteins] Extracted all results for the 'Proteins' dataset from Tables 1, 2, and
3. Table 1 contains results for GCN and GIN baselines with various rewiring/attention methods, plus
the proposed PANDA method. Table 2 compares PANDA-GCN with R-GCN. Table 3 compares PANDA-GCN with
different centrality measures. All values were converted from percentages to [0,1] range. Standard
deviations were parsed from the '±' or 'std' notation. The 'PANDA' row in Table 1 appears twice
(once for GCN backbone, once for GIN backbone); both are extracted as they represent different
configurations of the proposed method. Table 3 results are specific variants of PANDA-GCN based on
centrality metric, so they are marked as proposed model variants. [Collab] Extracted all rows from
Table 1 (tab:main) and Table 2 (tab:relational) and Table 3 (tab:centrality-gcn) corresponding to
the 'Collab' dataset. Note that 'PANDA' appears twice in Table 1 (once for GCN backbone, once for
GIN backbone). 'PANDA-GCN' in Table 2 is identical to the GCN-based PANDA in Table 1. 'Degree',
'Betweenness', etc. in Table 3 are ablation studies of the centrality measure used by PANDA-GCN, so
they are included as baselines/variants. BORF results for Collab are 'Time-out' and were skipped as
per instructions to skip non-numeric/impracticable results. All accuracy values were divided by 100.
[Texas] Extracted only the 'Texas' column from Table 1 as requested. All values were percentages in
the table (e.g., 44.2) and were divided by 100 to fit the [0,1] range for Accuracy. Standard
deviations were parsed from the '±' or 'std' notation. [Cornell] Extracted only the 'Cornell' column
from Table 1. All values are percentages converted to [0,1] range. Standard deviations are parsed
from the '±' notation. The proposed model is PANDA. [Wisconsin] Extracted only the Wisconsin column
from Table 1 as requested. All values were percentages in the table (e.g., 58.2) and were divided by
100 to fit the [0,1] range for Accuracy. Standard deviations were parsed from the format
'value\std{std}'. The proposed model is PANDA. [Squirrel] Extracted only the 'Squirrel' column from
Table 1. All values are percentages converted to [0,1] range. Standard deviations are parsed from
the '±' notation. The proposed model is PANDA. [Cora] Extracted only Cora results from Table 1.
Values were converted from percentages to [0,1] range. Standard deviations were parsed from the '±'
notation. [Citeseer] Extracted only the 'Citeseer' column from Table 2. All values were percentages
in the table (e.g., 75.3) and were divided by 100 to fit the [0,1] range for Accuracy. Standard
deviations were parsed from the '±' notation. All models are variants of GCN with different rewiring
methods or none. [Peptides-func] Extracted results for Peptides-func under two different settings:
'nguyen2023borf's setting' and 'dwivedi2022LRGB's setting'. Both are considered standard
configurations for this dataset in the context of the paper's comparison. Values were converted from
percentages to [0,1] range. Standard deviations were parsed from the '±' notation. [Peptides-struct]
Extracted only Peptides-struct MAE results as requested. The table provides results under
'dwivedi2022LRGB's setting' for Peptides-struct. All values are Test MAE. Standard deviations are
parsed from the '±' notation.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*