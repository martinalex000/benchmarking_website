---
title: Dirac--Bianconi Graph Neural Networks -- Enabling Non-Diffusive Long-Range
  Graph Predictions
arxiv_id: '2407.12419'
authors: []
published_date: '2024-07-17'
abstract: The geometry of a graph is encoded in dynamical processes on the graph.
  Many graph neural network (GNN) architectures are inspired by such dynamical systems,
  typically based on the graph Laplacian. Here, we introduce Dirac--Bianconi GNNs
  (DBGNNs), which are based on the topological Dirac equation recently proposed by
  Bianconi. Based on the graph Laplacian, we demonstrate that DBGNNs explore the geometry
  of the graph in a fundamentally different way than conventional message passing
  neural networks (MPNNs). While regular MPNNs propagate features diffusively, analogous
  to the heat equation, DBGNNs allow for coherent long-range propagation. Experimental
  results showcase the superior performance of DBGNNs over existing conventional MPNNs
  for long-range predictions of power grid stability and peptide properties. This
  study highlights the effectiveness of DBGNNs in capturing intricate graph dynamics,
  providing notable advancements in GNN architectures.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- DBGNN
mrr: 0.0043
results:
- &id001
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
  - model: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 147
    is_best: false
  - model: SAN+RWSE
    value: 0.2545
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 164
    is_best: false
  - model: SAN+LapPE
    value: 0.2683
    std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 213
    is_best: false
  - model: DBGNN
    value: 0.2864
    std: 0.0046
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.127
    table_ref: Table 1
    source_ref: this paper
    global_rank: 230
    is_best: false
  - model: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 146
    is_best: false
  - model: GatedGCN
    value: 0.342
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 10
    is_best: false
  - model: GCNII
    value: 0.3471
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 267
    is_best: false
  - model: GCN
    value: 0.3496
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 2
    is_best: false
  - model: GINE
    value: 0.3547
    std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    global_rank: 71
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
single_proposed_model: DBGNN
main_figure: /figures/2407.12419/main_figure.png
---

