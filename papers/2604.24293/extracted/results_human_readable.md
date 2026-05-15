# Extraction: Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution via Continuous Phase Transitions
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: HGODE (1.0M params)
- Type: GNN

## Results

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| HGODE | 0.7256 | 0.0124 | No | this paper | Table 1 |
| GraphGPS | 0.4104 | 0.0387 | Yes | this paper | Table 1 |
| Polynormer | 0.4169 | 0.0322 | Yes | this paper | Table 1 |
| SGFormer | 0.4577 | 0.0348 | Yes | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| HGODE | 0.8626 | 0.0078 | No | this paper | Table 1 |
| GraphGPS | 0.8295 | 0.0123 | Yes | this paper | Table 1 |
| Polynormer | 0.8324 | 0.0072 | Yes | this paper | Table 1 |
| SGFormer | 0.8459 | 0.0043 | Yes | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.6550 | 0.0040 | Yes | this paper | Table 2 |
| Subgraphormer | 0.6610 | 0.0050 | Yes | this paper | Table 2 |
| HGODE | 0.7140 | 0.0220 | No | this paper | Table 2 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| HGODE | 0.0780 | 0.0250 | No | this paper | Table 1 |
| GraphGPS | 0.0690 | 0.0080 | Yes | this paper | Table 1 |
| Subgraphormer | 0.0820 | 0.0400 | Yes | this paper | Table 1 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| HGODE | 0.2780 | 0.0030 | No | this paper | Table 1 |
| GraphGPS | 0.2910 | 0.0010 | Yes | this paper | Table 1 |
| Subgraphormer | 0.2930 | 0.0040 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: kipf2017semisupervised)
- **GCNII** (from: chen2020simple)
- **GCN+** (from: luo2025can)
- **GDE** (from: poli2019graph)
- **CGNN** (from: pmlr-v119-xhonneux20a)
- **GRAND** (from: chamberlain2021grand)
- **Sheaf Diffusion** (from: bodnar2022neural)
- **FLODE** (from: maskey2024fractional)
- **GREAD** (from: choi2023gread)
- **BuNN** (from: bamberger2025bundle)
- **ACMP** (from: wang2022acmp)
- **FROND** (from: kang2024frond)
- **DRAGON** (from: zhao2024dragon)
- **GraphGPS** (from: this paper)
- **Polynormer** (from: this paper)
- **SGFormer** (from: this paper)
- **Subgraphormer** (from: this paper)

## Extraction Notes

[Cora] Extracted results for Cora from Table 1 (labeled tab:transformer_baselines in the text, but
referred to as Table 1 in the prompt's context of 'main table' or potentially Table 2 if the
transformer table is separate. The text says 'Table 1 summarizes the results... The transformer
comparison in Table 2 shows...'. However, the provided table caption says 'Comparison with graph-
transformer baselines' and label is tab:transformer_baselines. The text references 'Table 1' for
main results and 'Table 2' (implied by app reference or context) for transformers. Wait, the text
says 'Table 1 summarizes... The transformer comparison in Table 2...'. The provided table has label
tab:transformer_baselines. I will assume this is the table provided. The prompt asks to extract from
the provided text/tables. The table provided contains Cora results for HGODE and transformer
baselines. The main MP baselines (GCN, GCNII, etc.) are NOT in this specific table. The text
mentions they are in Table 1 (tb:performance). Since only the transformer table was provided in the
'TABLES' section, I can only extract from it. I will note that main MP baselines are missing from
the provided table snippet. [Chameleon] Extracted results for Chameleon from Table 1 (labeled
tab:transformer_baselines in the text, but referred to as Table 1 in the main text context for
transformer baselines). The table explicitly lists Accuracy for Chameleon. Note that the main
performance table (Table tb:performance) is not provided in the text snippet, but the text states
HGODE obtains the best results on Chameleon. The transformer baseline table provides specific
numerical values for HGODE and three transformer baselines (GraphGPS, Polynormer, SGFormer) on
Chameleon. Other baselines (GCN, GCNII, etc.) are mentioned in the text but their specific Chameleon
Accuracy values are not present in the provided table snippet. Therefore, only the models with
explicit values in the provided table are extracted. [ogbn-proteins] failed: 1 validation error for
ExtractionOutput results.4.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ZINC] Extracted ZINC MAE results from Table 1
(labeled tab:transformer_baselines in the text, but referred to as Table 1 in the prompt's context
of main results). Polynormer and SGFormer have '--' for ZINC, so they are excluded. Only GraphGPS,
Subgraphormer, and HGODE have reported ZINC MAE values. The table caption mentions 'Table 1'
convention for best values, and the text refers to 'Table 1' for main results, but the provided
table is explicitly labeled 'tab:transformer_baselines'. I have used 'Table 1' as the ref based on
the text description 'Table 1 summarizes the results... The transformer comparison in Table...
shows...', implying this is a supplementary or specific table, but the prompt asks for table_ref. I
will use 'Table 1' as it is the primary reference in the text for performance, although the specific
table provided is the transformer baseline table. To be precise, I will use 'Table 1' as the text
says 'Table 1 summarizes the results...'. Wait, the text says 'Table 1 summarizes the results... The
transformer comparison in Table... shows...'. The provided table is the transformer comparison. I
will label it 'Table 1' as per the text's reference to the main performance table, or more
accurately 'Table 1 (Transformer Baselines)'. However, standard practice is to use the table number.
The text says 'Table 1 summarizes...'. The provided table is likely Table 1 or a part of it. I will
use 'Table 1'. [Peptides-func] Extracted results for Peptides-func from Table 2 (labeled
tab:transformer_baselines). Polynormer and SGFormer have '--' for Peptides-func, so they are
excluded. Only GraphGPS, Subgraphormer, and HGODE have reported values. Metric is AP (Average
Precision), normalized to [0,1]. Higher is better. [ogbg-molpcba] Extracted results for 'ogbg-
molpcba' from Table 1 (labeled tab:transformer_baselines in the text). Polynormer and SGFormer have
'--' for this dataset, so they are excluded. HGODE is marked as third best (0.278), while
Subgraphormer (0.293) and GraphGPS (0.291) are better. The paper text claims HGODE obtains the best
results among 'message-passing and continuous-depth baselines', implying the transformer baselines
(GraphGPS, Subgraphormer, etc.) are considered separately or HGODE's claim is relative to the non-
transformer group. However, the table includes all these models together. I have extracted all
available rows for the dataset.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*