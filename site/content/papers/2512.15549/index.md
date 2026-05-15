---
title: Photonics-Enhanced Graph Convolutional Networks
arxiv_id: '2512.15549'
authors: []
published_date: Dec 2025
abstract: Photonics can offer a hardware-native route for machine learning (ML). However,
  efficient deployment of photonics-enhanced ML requires hybrid workflows that integrate
  optical processing with conventional CPU/GPU based neural network architectures.
  Here, we propose such a workflow that combines photonic positional embeddings (PEs)
  with advanced graph ML models. We introduce a photonics-based method that augments
  graph convolutional networks (GCNs) with PEs derived from light propagation on synthetic
  frequency lattices whose couplings match the input graph. We simulate propagation
  and readout to obtain internode intensity correlation matrices, which are used as
  PEs in GCNs to provide global structural information. Evaluated on Long Range Graph
  Benchmark molecular datasets, the method outperforms baseline GCNs with Laplacian
  based PEs, achieving $6.3\
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GCN+PhotPE
mrr: 0.0038
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
  - model: GCN+PhotPE
    value: 0.4886
    std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    global_rank: 288
    is_best: false
  - model: GCN+LapPE
    value: 0.4776
    std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    global_rank: 225
    is_best: false
  - model: GCN
    value: 0.4566
    std: 0.0059
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: dwivedi2022long
    global_rank: 9
    is_best: false
  - model: GCN
    value: 0.4396
    std: 0.0048
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: Peptides-struct
  rows:
  - model: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
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
    global_rank: 3
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
    global_rank: 4
    is_best: true
  - model: GCN+PhotPE
    value: 0.2995
    std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    global_rank: 237
    is_best: false
  - model: GCN+LapPE
    value: 0.3195
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    global_rank: 255
    is_best: false
  - model: GCN
    value: 0.395
    std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: Dwivedi et al. 2022
    global_rank: 2
    is_best: false
  - model: GCN
    value: 0.4077
    std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
single_proposed_model: GCN+PhotPE
main_figure: /figures/2512.15549/main_figure.png
---

