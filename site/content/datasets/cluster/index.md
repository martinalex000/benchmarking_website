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
  num_graphs: 12000
  avg_nodes: 117.2
  avg_edges: 4303.9
  num_classes: 6
result_count: 89
best_model:
  model: Tango_GPS
  value: 0.80113
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
  - MAE
  - MSE
  - RMSE
  - RMSE E
  - RMSE F
  rows:
  - model: Tango_GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.80113
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013800000000000002
    - null
    - null
    - null
    - null
    - null
  - model: PPGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.80027
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00114
    - null
    - null
    - null
    - null
    - null
  - model: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.80026
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00277
    - null
    - null
    - null
    - null
    - null
  - model: GT + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.79965
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00203
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79816
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013700000000000001
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7973
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00189
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79571
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00122
    - null
    - null
    - null
    - null
    - null
  - model: GRASS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79541
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00173
    - null
    - null
    - null
    - null
    - null
  - model: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79284
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00122
    - null
    - null
    - null
    - null
    - null
  - model: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79232
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00348
    - null
    - null
    - null
    - null
    - null
  - model: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79156
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00152
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79128
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00235
    - null
    - null
    - null
    - null
    - null
  - model: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79071
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
  - model: CKGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79003
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
  - model: CSA-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7894
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00132
    - null
    - null
    - null
    - null
    - null
  - model: GPS-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7881999999999999
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00187
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS-AnchorGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78802
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00252
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78643
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00836
    - null
    - null
    - null
    - null
    - null
  - model: GPS + RandAlign
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78592
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00052
    - null
    - null
    - null
    - null
    - null
  - model: SAT + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78513
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00097
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78498
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00121
    - null
    - null
    - null
    - null
    - null
  - model: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78495
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00103
    - null
    - null
    - null
    - null
    - null
  - model: SAN-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7848099999999999
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017599999999999998
    - null
    - null
    - null
    - null
    - null
  - model: GPSE + GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7844
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00177
    - null
    - null
    - null
    - null
    - null
  - model: GPS+Diffusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7831199999999999
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00251
    - null
    - null
    - null
    - null
    - null
  - model: GPS + Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7829
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
    - null
  - model: GPS+Consistency+Contrastive
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78232
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00159
    - null
    - null
    - null
    - null
    - null
  - model: Tango_GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7819400000000001
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00307
    - null
    - null
    - null
    - null
    - null
  - model: NeuralWalker
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78189
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00188
    - null
    - null
    - null
    - null
    - null
  - model: GPS-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78171
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00231
    - null
    - null
    - null
    - null
    - null
  - model: GPS+Consistency
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78171
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00231
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7808
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78071
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00037
    - null
    - null
    - null
    - null
    - null
  - model: GPTrans-Nano
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7807
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
  - model: TIGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7803
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78016
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78016
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
  - model: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7799
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
  - model: GPS w/ Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7799
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
  - model: K-Subgraph SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77856
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00104
    - null
    - null
    - null
    - null
    - null
  - model: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77856
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00104
    - null
    - null
    - null
    - null
    - null
  - model: SAN + RandAlign
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77847
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00073
    - null
    - null
    - null
    - null
    - null
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77552
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00546
    - null
    - null
    - null
    - null
    - null
  - model: SAN-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77461
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042699999999999995
    - null
    - null
    - null
    - null
    - null
  - model: GPS + BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7746
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
  - model: Eigenformer (feat.)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77456
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7735
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
  - model: Eigenformer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77262
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77109
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00872
    - null
    - null
    - null
    - null
    - null
  - model: Graph Mamba-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
  - model: Graph-Mamba
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
  - model: GPS-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7677299999999999
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00301
    - null
    - null
    - null
    - null
    - null
  - model: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76691
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
  - model: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76691
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76691
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN + SSFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7596
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74794
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00213
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7384
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00326
    - null
    - null
    - null
    - null
    - null
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73169
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00622
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.70587
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00447
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69972
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00634
    - null
    - null
    - null
    - null
    - null
  - model: SAN-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68711
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00676
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68498
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00976
    - null
    - null
    - null
    - null
    - null
  - model: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.66407
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64913
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016390000000000002
    - null
    - null
    - null
    - null
    - null
  - model: GIN (GINE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64716
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01553
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64716
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01553
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.63844
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
  - model: S² GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4546
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
  - model: S² GCN (+PE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4546
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
  - model: RingGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.42418
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.20063
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.27
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
  - model: GCN (+PE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2684
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
  - model: Lorem
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.020999
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.09
    - null
    - 0.112
    - 0.112
    - 1.155
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cace-Les
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.161
    - null
    - 0.21
    - 0.21
    - 9.784
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Mace
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 1.345
    - null
    - 1.681
    - 1.681
    - 40.219
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 1.249
    - null
    - 1.517
    - 1.517
    - 42.438
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 4G-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.481
    - 0.481
    - 32.78
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SpookyNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.135
    - 0.135
    - 1.052
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 2PCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 2.03
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.02
    - null
    - null
    - null
  - model: GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 2.77
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.41
    - null
    - null
    - null
  - model: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 13.33
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0
    - null
    - null
    - null
  - model: NequIP (l_max = 1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 3.07
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.18
    - null
    - null
    - null
  - model: SEGNN (l_max = 1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 2.37
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.06
    - null
    - null
    - null
  - model: PointNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 2.87
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.07
    - null
    - null
    - null
  - model: GNN (mean agg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 2.77
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.41
    - null
    - null
    - null
  - model: GNN (global attn. agg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 2.6
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.06
    - null
    - null
    - null
  - model: GNN (local + global attn. agg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 3.0
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.14
    - null
    - null
    - null
  - model: GNN (invariant attn.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 3.62
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.01
    - null
    - null
    - null
  milestones:
  - value: 0.80026
    std: 0.00277
    model: GRIT
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.8003
    std: 0.0028
    model: GRIT
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
  - value: 0.80113
    std: 0.0013800000000000002
    model: Tango_GPS
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: 2025-08
---

