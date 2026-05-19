---
title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
arxiv_id: '2410.20516'
authors: []
published_date: Oct 2024
abstract: Efficiently processing structured point cloud data while preserving multiscale
  information is a key challenge across domains, from graphics to atomistic modeling.
  Using a curated dataset of simulated galaxy positions and properties, represented
  as point clouds, we benchmark the ability of graph neural networks to simultaneously
  capture local clustering environments and long-range correlations. Given the homogeneous
  and isotropic nature of the Universe, the data exhibits a high degree of symmetry.
  We therefore focus on evaluating the performance of Euclidean symmetry-preserving
  ($E(3)$-equivariant) graph neural networks, showing that they can outperform non-equivariant
  counterparts and domain-specific information extraction techniques in downstream
  performance as well as simulation-efficiency. However, we find that current architectures
  fail to capture information from long-range correlations as effectively as domain-specific
  baselines, motivating future work on architectures better suited for extracting
  long-range information.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- SEGNN (l_max = 1)
mrr: 0.0
results:
- &id001
  dataset: CLUSTER
  rows:
  - model: GCN (+PE)
    value: 0.2684
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.27
    std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: RingGNN
    value: 0.42418
    std: 0.20063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: 2PCF
    value: 2.03
    std: 0.02
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SEGNN (l_max = 1)
    value: 2.37
    std: 0.06
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GNN (global attn. agg.)
    value: 2.6
    std: 0.06
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GNN
    value: 2.77
    std: 0.41
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GNN (mean agg.)
    value: 2.77
    std: 0.41
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: PointNet++
    value: 2.87
    std: 0.07
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GNN (local + global attn. agg.)
    value: 3.0
    std: 0.14
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: NequIP (l_max = 1)
    value: 3.07
    std: 0.18
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GNN (invariant attn.)
    value: 3.62
    std: 0.01
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: EGNN
    value: 13.33
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
results_grouped:
- benchmark: GNNBenchmark
  datasets:
  - *id001
single_proposed_model: SEGNN (l_max = 1)
main_figure: /figures/2410.20516/main_figure.png
---

