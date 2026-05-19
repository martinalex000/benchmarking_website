---
title: Coauthor-CS
slug: coauthor-cs
benchmark: Classic
task_type: node_classification
description: Co-authorship graph (CS) node classification from the "Pitfalls of Graph
  Neural Network Evaluation" paper.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Coauthor.html
stats:
  num_graphs: null
  avg_nodes: 18333.0
  avg_edges: 163788.0
  num_classes: 15
result_count: 49
best_model:
  model: GraphSAGE
  value: 0.9638
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  rows:
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9638
    metric_stds:
    - 0.0011
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9621
    metric_stds:
    - 0.0014
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9617
    metric_stds:
    - 0.0006
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9592
    metric_stds:
    - 0.0025
  - model: M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9589
    metric_stds:
    - 0.0034
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9585
    metric_stds:
    - 0.0016
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9571
    metric_stds:
    - 0.0024
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9569
    metric_stds:
    - 0.0027
  - model: UFGConvS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9546
    metric_stds:
    - 0.0033
  - model: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9542
    metric_stds:
    - 0.0019
  - model: Scattering GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9518
    metric_stds:
    - 0.003
  - model: SEA-GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9511
    metric_stds:
    - 0.0037
  - model: DEFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9504
    metric_stds:
    - 0.0032
  - model: WaveNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9491
    metric_stds:
    - 0.0029
  - model: WaveShrink-ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    metric_stds:
    - 0.003
  - model: SGWT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9481
    metric_stds:
    - 0.0023
  - model: Scattering
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9477
    metric_stds:
    - 0.0033
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9449
    metric_stds:
    - 0.0007
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9404
    metric_stds:
    - 0.0021
  - model: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9381
    metric_stds:
    - 0.0019
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9361
    metric_stds:
    - 0.0014
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9292
    metric_stds:
    - 0.0012
  - model: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9075
    metric_stds:
    - 0.0059
  - model: CaCoSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9073
    metric_stds:
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9056000000000001
    metric_stds:
    - null
  - model: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9052
    metric_stds:
    - null
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9044
    metric_stds:
    - null
  - model: GOKU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9004000000000001
    metric_stds:
    - null
  - model: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8887
    metric_stds:
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8886
    metric_stds:
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8842
    metric_stds:
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8713
    metric_stds:
    - null
  - model: LASER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    metric_stds:
    - null
  - model: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    metric_stds:
    - null
  - model: 1-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6627
    metric_stds:
    - 0.0277
  - model: GatedGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6614
    metric_stds:
    - 0.0293
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6317
    metric_stds:
    - 0.0201
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6291
    metric_stds:
    - 0.0275
  - model: Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6088
    metric_stds:
    - 0.0193
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6041
    metric_stds:
    - 0.0212
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5989
    metric_stds:
    - 0.0173
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5982
    metric_stds:
    - 0.0404
  - model: LRGB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.595
    metric_stds:
    - null
  - model: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5943
    metric_stds:
    - 0.015
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5925
    metric_stds:
    - 0.0419
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5828
    metric_stds:
    - 0.0209
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.579
    metric_stds:
    - 0.0335
  - model: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5295
    metric_stds:
    - 0.0379
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.529
    metric_stds:
    - 0.0216
  milestones:
  - value: 0.9589
    std: 0.0034
    model: M
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
  - value: 0.9638
    std: 0.0011
    model: GraphSAGE
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: 2024-06
---

