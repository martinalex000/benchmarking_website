---
title: CLUSTER
slug: cluster
benchmark: GNNBenchmark
task_type: node_classification
description: Semi-supervised node classification on stochastic block model graphs
  (6 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 6
result_count: 59
best_model:
  model: Tango_GPS
  value: 0.80113
  metric: Accuracy
  arxiv_id: '2508.05070'
  paper_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  rows:
  - model: Tango_GPS
    model_plain: Tango_GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.80113
    metric_stds:
    - 0.00138
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.80026
    metric_stds:
    - 0.00277
  - model: GRIT-RWSE
    model_plain: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7973
    metric_stds:
    - 0.00189
  - model: GRIT-SPSE
    model_plain: GRIT-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79571
    metric_stds:
    - 0.00122
  - model: LRDs
    model_plain: LRDs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79284
    metric_stds:
    - 0.00122
  - model: EGT
    model_plain: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79232
    metric_stds:
    - 0.00348
  - model: GSSC
    model_plain: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79156
    metric_stds:
    - 0.00152
  - model: CSA-RWSE
    model_plain: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79071
    metric_stds:
    - 0.0012
  - model: CSA-SPSE
    model_plain: CSA-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7894
    metric_stds:
    - 0.00132
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78495
    metric_stds:
    - 0.00103
  - model: GPS + GPSE
    model_plain: GPS + GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7844
    metric_stds:
    - 0.00177
  - model: GPS+Performer
    model_plain: GPS+Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7829
    metric_stds:
    - 0.0004
  - model: Tango_GatedGCN
    model_plain: Tango_GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78194
    metric_stds:
    - 0.00307
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7807
    metric_stds:
    - 0.00037
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7802
    metric_stds:
    - 0.0018
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78016
    metric_stds:
    - 0.0018
  - model: GPS+Transformer
    model_plain: GPS+Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.287
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7799
    metric_stds:
    - 0.0017
  - model: K-Subgraph SAT
    model_plain: K-Subgraph SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7786
    metric_stds:
    - 0.00104
  - model: Ours(100K)
    model_plain: Ours(100K)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77575
    metric_stds:
    - 0.00149
  - model: GPS+BigBird
    model_plain: GPS+BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7746
    metric_stds:
    - 0.0002
  - model: Eigenformer (feat.)
    model_plain: Eigenformer (feat.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77456
    metric_stds:
    - null
  - model: Eigenformer
    model_plain: Eigenformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77262
    metric_stds:
    - null
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    metric_stds:
    - 0.0036
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7669
    metric_stds:
    - 0.0065
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76082
    metric_stds:
    - 0.00196
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7466
    metric_stds:
    - 0.00236
  - model: GatedGCN-PE/E(500K)
    model_plain: GatedGCN-PE/E(500K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74088
    metric_stds:
    - 0.00344
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7384
    metric_stds:
    - 0.00326
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73169
    metric_stds:
    - 0.00622
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.70587
    metric_stds:
    - 0.00447
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68498
    metric_stds:
    - 0.00976
  - model: SoGCN
    model_plain: SoGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68167
    metric_stds:
    - 0.01164
  - model: SoGCN-GRU
    model_plain: SoGCN-GRU
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67994
    metric_stds:
    - 0.02619
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64716
    metric_stds:
    - 0.01553
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.63844
    metric_stds:
    - 0.0011
  - model: PNA(100K)
    model_plain: PNA(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6302
    metric_stds:
    - 0.00262
  - model: GatedGCN(100K)
    model_plain: GatedGCN(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.60404
    metric_stds:
    - 0.00419
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.60404
    metric_stds:
    - 0.00419
  - model: GCN-3-TOGL-1
    model_plain: GCN-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.604
    metric_stds:
    - 0.002
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.585
    metric_stds:
    - 0.001
  - model: GAT-3-TOGL-1
    model_plain: GAT-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.584
    metric_stds:
    - 0.037
  - model: GIN(100K)
    model_plain: GIN(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.58384
    metric_stds:
    - 0.00236
  - model: MoNet(100K)
    model_plain: MoNet(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.58064
    metric_stds:
    - 0.00131
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.58064
    metric_stds:
    - 0.00131
  - model: Vanilla GCN + GRU
    model_plain: Vanilla GCN + GRU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.57932
    metric_stds:
    - 0.00168
  - model: GAT(100K)
    model_plain: GAT(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.57732
    metric_stds:
    - 0.00323
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.57732
    metric_stds:
    - 0.00323
  - model: 3WLGNN
    model_plain: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5713
    metric_stds:
    - 0.06539
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.57
    metric_stds:
    - 0.009
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.566
    metric_stds:
    - 0.004
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.53445
    metric_stds:
    - 0.02029
  - model: GraphSage(100K)
    model_plain: GraphSage(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.50454
    metric_stds:
    - 0.00145
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.50454
    metric_stds:
    - 0.00145
  - model: GCoT
    model_plain: GCoT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2754
    metric_stds:
    - null
  - model: GraphTransformer(500K)
    model_plain: GraphTransformer(500K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.27121
    metric_stds:
    - 0.08471
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2427
    metric_stds:
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2382
    metric_stds:
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2218
    metric_stds:
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2127
    metric_stds:
    - null
  milestones:
  - value: 0.604
    std: 0.002
    model: GCN-3-TOGL-1
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: 2021-02
  - value: 0.79232
    std: 0.00348
    model: EGT
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: 2021-08
  - value: 0.80026
    std: 0.00277
    model: GRIT
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: 2024-01
  - value: 0.80113
    std: 0.00138
    model: Tango_GPS
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: 2025-08
---

