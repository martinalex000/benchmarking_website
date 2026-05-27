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
result_count: 92
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
  - MAE
  - MSE
  - RMSE
  - RMSE E
  - RMSE F
  - W. Accuracy
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
    - null
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
    - null
  - model: PPGT
    model_plain: PPGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
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
    - 0.80027
    metric_stds:
    - 0.00114
    - null
    - null
    - null
    - null
    - null
    - 0.00114
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00277
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GT + HDSE
    model_plain: GT + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00203
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT (our run)
    model_plain: GRIT (our run)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.79856
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00156
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-GCCM
    model_plain: GRIT-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.0013700000000000001
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT 2-QiQRW
    model_plain: GRIT 2-QiQRW
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79777
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00171
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-RWSE
    model_plain: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00189
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-SPSE
    model_plain: GRIT-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00122
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRASS
    model_plain: GRASS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
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
    - null
    metric_stds:
    - 0.00173
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Ours
    model_plain: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00122
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EGT
    model_plain: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00348
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSSC
    model_plain: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00152
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00235
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CSA-RWSE
    model_plain: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CKGCN
    model_plain: CKGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
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
    - 0.79003
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - 0.0014
  - model: CSA-SPSE
    model_plain: CSA-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00132
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT 1-CQRW
    model_plain: GRIT 1-CQRW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78895
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001145
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS-GCCM
    model_plain: GPS-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7882
    - null
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
    - null
  - model: GraphGPS-AnchorGT
    model_plain: GraphGPS-AnchorGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.00252
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-PCL
    model_plain: GRIT-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.00836
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS + RandAlign
    model_plain: GPS + RandAlign
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
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
    - null
    metric_stds:
    - 0.00052
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAT + HDSE
    model_plain: SAT + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00097
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS + HDSE
    model_plain: GraphGPS + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00121
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRED
    model_plain: GRED
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
    date_iso: '2023-12-03'
    date_display: Dec 2023
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
    - null
    metric_stds:
    - 0.00103
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAN-GCCM
    model_plain: SAN-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.0017599999999999998
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPSE + GPS
    model_plain: GPSE + GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00177
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS+Diffusion
    model_plain: GPS+Diffusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.00251
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS + Performer
    model_plain: GPS + Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
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
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS+Consistency+Contrastive
    model_plain: GPS+Consistency+Contrastive
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.00159
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7819400000000001
    - null
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
    - null
  - model: NeuralWalker
    model_plain: NeuralWalker
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
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
    - null
    metric_stds:
    - 0.00188
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS-PCL
    model_plain: GPS-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.00231
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS+Consistency
    model_plain: GPS+Consistency
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.00231
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00037
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPTrans-Nano
    model_plain: GPTrans-Nano
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TIGT
    model_plain: TIGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
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
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph transformer
    model_plain: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
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
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS w/ Transformer
    model_plain: GPS w/ Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
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
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00104
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-Subgraph SAT
    model_plain: K-Subgraph SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
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
    - null
    metric_stds:
    - 0.00104
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAN + RandAlign
    model_plain: SAN + RandAlign
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
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
    - null
    metric_stds:
    - 0.00073
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.00546
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAN-PCL
    model_plain: SAN-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.0042699999999999995
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS + BigBird
    model_plain: GPS + BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
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
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Eigenformer (feat.)
    model_plain: Eigenformer (feat.)
    is_baseline: false
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
    - null
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
    - null
  - model: ARGNP
    model_plain: ARGNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Eigenformer
    model_plain: Eigenformer
    is_baseline: false
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
    - null
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
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00872
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph Mamba-1
    model_plain: Graph Mamba-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
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
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
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
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
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
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS-LGD
    model_plain: GPS-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76773
    - null
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
    - null
  - model: SAN+RWSE
    model_plain: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAN+LapPE
    model_plain: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN + SSFG
    model_plain: GatedGCN + SSFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
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
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
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
    - null
    metric_stds:
    - 0.00213
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00326
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00622
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
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
    - null
    metric_stds:
    - 0.00447
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00634
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAN-LGD
    model_plain: SAN-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.00676
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.00976
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
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
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRIT-LGD
    model_plain: GRIT-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
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
    - null
    metric_stds:
    - 0.016390000000000002
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN (GINE)
    model_plain: GIN (GINE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.01553
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
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
    - null
    metric_stds:
    - 0.01553
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
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
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S² GCN
    model_plain: S² GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S² GCN (+PE)
    model_plain: S² GCN (+PE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RingGNN
    model_plain: RingGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
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
    - null
    metric_stds:
    - 0.20063
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN (+PE)
    model_plain: GCN (+PE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    date_display: May 2024
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
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Lorem
    model_plain: Lorem
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.021
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
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
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cace-Les
    model_plain: Cace-Les
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
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
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Mace
    model_plain: Mace
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
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
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pet
    model_plain: Pet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
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
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 4G-NN
    model_plain: 4G-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
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
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SpookyNet
    model_plain: SpookyNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
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
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 2PCF
    model_plain: 2PCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.02
    - null
    - null
    - null
    - null
  - model: GNN
    model_plain: GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.41
    - null
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.0
    - null
    - null
    - null
    - null
  - model: NequIP (l_max = 1)
    model_plain: NequIP (l_max = 1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.18
    - null
    - null
    - null
    - null
  - model: SEGNN (l_max = 1)
    model_plain: SEGNN (l_max = 1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.06
    - null
    - null
    - null
    - null
  - model: PointNet++
    model_plain: PointNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.07
    - null
    - null
    - null
    - null
  - model: GNN (mean agg.)
    model_plain: GNN (mean agg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.41
    - null
    - null
    - null
    - null
  - model: GNN (global attn. agg.)
    model_plain: GNN (global attn. agg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.06
    - null
    - null
    - null
    - null
  - model: GNN (local + global attn. agg.)
    model_plain: GNN (local + global attn. agg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.14
    - null
    - null
    - null
    - null
  - model: GNN (invariant attn.)
    model_plain: GNN (invariant attn.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.20516'
    title: A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
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
    - null
    metric_stds:
    - null
    - null
    - 0.01
    - null
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

