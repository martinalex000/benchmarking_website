# Extraction: arXiv:2307.03393
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: TAPE
- Type: GNN

## Results

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Zero-shot | 0.6550 | 0.0353 | No | this paper | Table 1 |
| Few-shot | 0.6600 | 0.0566 | No | this paper | Table 1 |
| Zero-shot with COT | 0.6650 | 0.0282 | No | this paper | Table 1 |
| Few-shot with COT | 0.6050 | 0.0494 | No | this paper | Table 1 |
| GCN/SAGE | 0.7119 | 0.0110 | Yes | this paper | Table 1 |
| Zero-Shot with 2-hop info | 0.6200 | 0.0141 | No | this paper | Table 2 |
| Few-Shot with 2-hop info | 0.6700 | 0.0494 | No | this paper | Table 2 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| TF-IDF | 0.8199 | 0.0063 | Yes | this paper | Table 1 |
| Word2Vec | 0.7401 | 0.0124 | Yes | this paper | Table 1 |
| Deberta-base | 0.4849 | 0.0186 | Yes | this paper | Table 1 |
| LLama 7B | 0.6680 | 0.0220 | Yes | this paper | Table 1 |
| Sentence-BERT(MiniLM) | 0.8220 | 0.0049 | Yes | this paper | Table 1 |
| e5-large | 0.8256 | 0.0073 | Yes | this paper | Table 1 |
| text-ada-embedding-002 | 0.8272 | 0.0069 | Yes | this paper | Table 1 |
| Google Palm Cortex 001 | 0.8115 | 0.0101 | Yes | this paper | Table 1 |
| Fine-tuned Deberta-base | 0.5923 | 0.0116 | Yes | this paper | Table 1 |
| GLEM-GNN | 0.4849 | 0.0186 | Yes | this paper | Table 1 |
| GLEM-LM | 0.5923 | 0.0116 | Yes | this paper | Table 1 |
| TAPE | 0.7456 | 0.0203 | No | this paper | Table 3 |
| TAPE (P) | 0.5279 | 0.0147 | Yes | this paper | Table 3 |
| TAPE (TA + E (e5)) | 0.8338 | 0.0042 | Yes | this paper | Table 3 |
| TAPE (TA + E (PLM)) | 0.7802 | 0.0056 | Yes | this paper | Table 3 |
| TAPE (E (PLM)) | 0.7946 | 0.0110 | Yes | this paper | Table 3 |
| TAPE (E (e5)) | 0.8438 | 0.0036 | Yes | this paper | Table 3 |
| TAPE (TA (PLM)) | 0.5923 | 0.0116 | Yes | this paper | Table 3 |
| TAPE (TA (e5)) | 0.8256 | 0.0073 | Yes | this paper | Table 3 |

### Ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| TF-IDF | 0.7223 | 0.0021 | Yes | this paper | Table 1 |
| MLP | 0.6660 | 0.0025 | Yes | this paper | Table 1 |
| RevGAT | 0.7516 | 0.0014 | Yes | this paper | Table 1 |
| Deberta-base | 0.4570 | 0.0559 | Yes | this paper | Table 1 |
| Sentence-BERT(MiniLM) | 0.7310 | 0.0025 | Yes | this paper | Table 1 |
| e5-large | 0.7374 | 0.0012 | Yes | this paper | Table 1 |
| text-ada-embedding-002 | 0.7276 | 0.0023 | Yes | this paper | Table 1 |
| Fine-tuned Deberta-base | 0.7465 | 0.0012 | Yes | this paper | Table 1 |
| GIANT | 0.7329 | 0.0010 | Yes | this paper | Table 1 |
| GLEM-GNN | 0.7593 | 0.0019 | No | this paper | Table 1 |
| GLEM-LM | 0.7571 | 0.0024 | No | this paper | Table 1 |
| ChatGPT (Zero-shot) | 0.5175 | 0.0389 | Yes | this paper | Table 2 |
| ChatGPT (Few-shot) | 0.5025 | 0.0106 | Yes | this paper | Table 2 |
| ChatGPT (Zero-shot with COT) | 0.5050 | 0.0141 | Yes | this paper | Table 2 |
| ChatGPT (Few-shot with COT) | 0.4725 | 0.0247 | Yes | this paper | Table 2 |
| GCN | 0.7310 | 0.0025 | Yes | this paper | Table 2 |
| ChatGPT (Zero-shot with 2-hop info) | 0.5500 | 0.0283 | Yes | this paper | Table 4 |
| ChatGPT (Few-shot with 2-hop info) | 0.5225 | 0.0318 | Yes | this paper | Table 4 |

### Ogbn-products — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| TF-IDF | 0.6442 | 0.0018 | Yes | this paper | Table 1 |
| Word2Vec | 0.6927 | 0.0054 | Yes | this paper | Table 1 |
| Deberta-base | 0.0718 | 0.0109 | Yes | this paper | Table 1 |
| Sentence-BERT(MiniLM) | 0.7273 | 0.0034 | Yes | this paper | Table 1 |
| e5-large | 0.7749 | 0.0029 | Yes | this paper | Table 1 |
| text-ada-embedding-002 | 0.7642 | 0.0031 | Yes | this paper | Table 1 |
| Fine-tuned Deberta-base | 0.7908 | 0.0023 | Yes | this paper | Table 1 |
| GIANT | 0.7982 | 0.0007 | Yes | this paper | Table 1 |
| GLEM-GNN | 0.8736 | 0.0007 | No | this paper | Table 1 |
| GLEM-LM | 0.8483 | 0.0004 | No | this paper | Table 1 |
| LLM Zero-shot | 0.7075 | 0.0248 | No | this paper | Table 2 |
| LLM Few-shot | 0.7775 | 0.0106 | No | this paper | Table 2 |
| LLM Zero-shot with COT | 0.7125 | 0.0106 | No | this paper | Table 2 |
| LLM Few-shot with COT | 0.7325 | 0.0177 | No | this paper | Table 2 |
| GCN/SAGE | 0.8251 | 0.0053 | Yes | this paper | Table 2 |
| LLM Zero-Shot with 2-hop info | 0.7525 | 0.0353 | No | this paper | Table 3 |
| LLM Few-Shot with 2-hop info | 0.7600 | 0.0282 | No | this paper | Table 3 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| TF-IDF | 0.7886 | 0.0200 | Yes | this paper | Table 1 |
| Word2Vec | 0.7010 | 0.0180 | Yes | this paper | Table 1 |
| Deberta-base | 0.6208 | 0.0006 | Yes | this paper | Table 1 |
| LLama 7B | 0.7353 | 0.0006 | Yes | this paper | Table 1 |
| Sentence-BERT(MiniLM) | 0.8101 | 0.0132 | Yes | this paper | Table 1 |
| e5-large | 0.8263 | 0.0113 | Yes | this paper | Table 1 |
| text-ada-embedding-002 | 0.7909 | 0.0151 | Yes | this paper | Table 1 |
| Google Palm Cortex 001 | 0.8091 | 0.0019 | Yes | this paper | Table 1 |
| Fine-tuned Deberta-base | 0.6212 | 0.0007 | Yes | this paper | Table 1 |
| GLEM-GNN | 0.6208 | 0.0006 | Yes | this paper | Table 1 |
| GLEM-LM | 0.6212 | 0.0007 | Yes | this paper | Table 1 |
| TAPE | 0.8597 | 0.0031 | No | this paper | Table 3 |
| TAPE (P) | 0.8192 | 0.0189 | Yes | this paper | Table 3 |
| TAPE (TA + E) (e5) | 0.8744 | 0.0049 | Yes | this paper | Table 3 |
| TAPE (TA + E) (PLM) | 0.8070 | 0.0173 | Yes | this paper | Table 3 |
| TAPE (E) (PLM) | 0.8188 | 0.0005 | Yes | this paper | Table 3 |
| TAPE (E) (e5) | 0.8223 | 0.0078 | Yes | this paper | Table 3 |
| TAPE (TA) (PLM) | 0.6212 | 0.0007 | Yes | this paper | Table 3 |
| TAPE (TA) (e5) | 0.8263 | 0.0113 | Yes | this paper | Table 3 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **MLP** (from: this paper)
- **TF-IDF** (from: this paper)
- **Word2Vec** (from: Mikolov et al. 2013)
- **Deberta-base** (from: He et al. 2021)
- **LLama 7B** (from: Touvron et al. 2023)
- **Sentence-BERT(MiniLM)** (from: Reimers & Gurevych 2019)
- **e5-large** (from: Wang et al. 2022)
- **text-ada-embedding-002** (from: OpenAI 2022)
- **Google Palm Cortex 001** (from: Google 2023)
- **Fine-tuned Deberta-base** (from: this paper)
- **GLEM-GNN** (from: this paper)
- **GLEM-LM** (from: this paper)
- **TAPE (P)** (from: this paper)
- **TAPE (TA + E)** (from: this paper)
- **TAPE (E)** (from: this paper)
- **TAPE (TA)** (from: this paper)
- **Original attributes** (from: this paper)
- **RevGAT** (from: Wang et al. 2020)
- **SAGE** (from: Hamilton et al. 2017)
- **SAGN** (from: this paper)
- **GIANT** (from: this paper)
- **ChatGPT (Zero-shot)** (from: OpenAI)
- **ChatGPT (Few-shot)** (from: OpenAI)
- **ChatGPT (Zero-shot with COT)** (from: OpenAI)
- **ChatGPT (Few-shot with COT)** (from: OpenAI)
- **ChatGPT (Zero-shot with 2-hop info)** (from: OpenAI)
- **ChatGPT (Few-shot with 2-hop info)** (from: OpenAI)
- **LLM Zero-shot** (from: this paper)
- **LLM Few-shot** (from: this paper)
- **LLM Zero-shot with COT** (from: this paper)
- **LLM Few-shot with COT** (from: this paper)
- **LLM Zero-Shot with 2-hop info** (from: this paper)
- **LLM Few-Shot with 2-hop info** (from: this paper)

## Extraction Notes

[Cora] Extracted results for Cora from Tables 1, 2, 3, and 4. Table 1 and 2 report results for
'LLMs-as-Enhancer' with low and high labeling ratios respectively. Table 3 and 4 report ablation
studies for TAPE with low and high labeling ratios. The proposed model is TAPE. Baselines include
various embedding methods (TF-IDF, Word2Vec, Deberta, etc.) and GNN architectures (GCN, GAT, MLP)
used as classifiers on top of these embeddings. All values are percentages converted to [0,1].
Standard deviations are extracted from the '±' notation. Note that Table 4 is cut off in the
provided text, so only the rows visible in the snippet were extracted. [PubMed] Extracted results
for PubMed from Tables 1, 2, 3, and 4. Table 1 and 2 show results for low and high labeling ratios
respectively. Table 3 and 4 show ablation studies for TAPE. The proposed model is TAPE. Baselines
include various embedding methods and GNNs. All values are normalized to [0,1] as they are Accuracy
metrics. Standard deviations are extracted from the '±' notation. Note: Table 4 is cut off in the
provided text, so only the first 6 rows of the ablation study for high labeling ratio are included.
[Ogbn-arxiv] Extracted results for Ogbn-arxiv from Table 1, Table 2, and Table 4. Table 3 contains
results for different label designs which are considered variants/non-standard configurations and
were skipped per instructions. Table 1 contains the main benchmark results for GNNs and LLM-as-
Enhancers. Table 2 and 4 contain LLM zero/few-shot results. Note: Table 1 lists 'GCN' and 'SAGE'
baselines with Sentence-BERT features, while Table 2/4 list 'GCN/SAGE' with Sentence-BERT features.
The values are identical (0.7310 for GCN), so they are treated as the same baseline result. The
proposed model is GLEM-GNN (and GLEM-LM). All values are normalized to [0,1] range. [Ogbn-products]
Extracted all rows related to 'Ogbn-products' from Table 1, Table 2, and Table 3. Note that Table 2
and Table 3 contain identical baseline results for 'GCN/SAGE', 'Zero-shot', 'Few-shot', etc., but
Table 3 adds '2-hop info' variants. The metric is Accuracy. Values are normalized to [0,1]. Standard
deviations are parsed from the ± notation. 'GCN/SAGE' refers to SAGE for Ogbn-products as per table
caption. [CiteSeer] Extracted all rows for CiteSeer from Table 1 and Table 2. Note that Table 1 and
Table 2 report identical values for 'Zero-shot', 'Few-shot', and 'GCN/SAGE'. Table 2 includes
additional rows for 'Zero-Shot with 2-hop info' and 'Few-Shot with 2-hop info'. The paper uses
'CiteSeer' and 'Citeseer' interchangeably; normalized to 'CiteSeer' as per FOCUS instruction. Values
are percentages, divided by 100. The baseline 'GCN/SAGE' refers to GCN for CiteSeer (SAGE is used
for Ogbn-products). The LLM model uses external pre-training (ChatGPT), so uses_external_data is
true.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*