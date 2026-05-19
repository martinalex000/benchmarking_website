---
title: Stronger Graph Transformer with Regularized Attention Scores
arxiv_id: '2312.11730'
authors: []
published_date: Dec 2023
abstract: 1cmGraph Neural Networks are notorious for its memory consumption. A recent
  Transformer-based GNN called Graph Transformer is shown to obtain superior performances
  when long range dependencies exist. However, combining graph data and Transformer
  architecture led to a combinationally worse memory issue. We propose a novel version
  of "edge regularization technique" that alleviates the need for Positional Encoding
  and ultimately alleviate GT's out of memory issue. We observe that it is not clear
  whether having an edge regularization on top of positional encoding is helpful.
  However, it seems evident that applying our edge regularization technique indeed
  stably improves GT's performance compared to GT without Positional Encoding.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GraphGPS (w/ Positional Encoding, 0.01 CE)
- GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE)
- 0.01 L1
- 0.05 L1
- 0.01 CE
- No-PE 0.1 L1
mrr: 0.0096
results:
- &id001
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: 0.01 L1
    value: 0.6477
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    global_rank: 162
    is_best: false
  - model: 0.05 L1
    value: 0.6468
    std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    global_rank: 164
    is_best: false
  - model: Baseline
    value: 0.6435
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    global_rank: 175
    is_best: false
  - model: 0.01 CE
    value: 0.6423
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    global_rank: 177
    is_best: false
  - model: No-PE 0.1 L1
    value: 0.6096
    std: 0.00185
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    global_rank: 201
    is_best: false
  - model: No-PE Baseline
    value: 0.5866
    std: 0.0184
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    global_rank: 224
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: Peptides-struct
  rows:
  - model: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: IPR-MPNN
    value: 0.2422
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GraphGPS (w/ Positional Encoding, 0.01 CE)
    value: 0.2491
    std: 0.0024
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    global_rank: 104
    is_best: false
  - model: GraphGPS (w/ Positional Encoding, No Reg)
    value: 0.2499
    std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    global_rank: 108
    is_best: false
  - model: GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE)
    value: 0.25
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    global_rank: 116
    is_best: false
  - model: Baseline (w/out Positional Encoding)
    value: 0.257
    std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 2
    source_ref: this paper
    global_rank: 163
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
main_figure: /figures/2312.11730/main_figure.png
---

