---
title: PATTERN
slug: pattern
benchmark: GNNBenchmark
task_type: node_classification
description: Semi-supervised node classification — detect specific graph patterns
  (2 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 2
result_count: 80
best_model:
  model: DGN
  value: 0.96
  metric: Accuracy
  arxiv_id: '2010.02863'
  paper_title: Directional Graph Networks
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
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.96
    metric_stds:
    - 0.002
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.93
    metric_stds:
    - 0.002
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.92
    metric_stds:
    - 0.003
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.91
    metric_stds:
    - 0.003
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    metric_stds:
    - 0.004
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.89
    metric_stds:
    - 0.004
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    metric_stds:
    - 0.005
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
    - 0.87552
    metric_stds:
    - 0.00123
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
    - 0.8751
    metric_stds:
    - 0.00082
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
    - 0.87235
    metric_stds:
    - 0.0004
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
    - 0.87229
    metric_stds:
    - 0.00056
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.87196
    metric_stds:
    - 0.00076
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
    is_best: false
    metric_values:
    - 0.87182
    metric_stds:
    - 0.00063
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
    - 0.87064
    metric_stds:
    - 0.00052
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
    - 0.87008
    metric_stds:
    - 0.00062
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.87
    metric_stds:
    - 0.006
  - model: GIN-AK+
    model_plain: GIN-AK+
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
    - 0.8685
    metric_stds:
    - 0.00057
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
    - 0.8685
    metric_stds:
    - 0.00037
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.86848
    metric_stds:
    - 0.00037
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
    - 0.86834
    metric_stds:
    - 0.00025
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
    - 0.86816
    metric_stds:
    - 0.00027
  - model: GRED
    model_plain: GRED
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.86759
    metric_stds:
    - 0.0002
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
    - 0.86757
    metric_stds:
    - 0.00031
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
    - 0.8674
    metric_stds:
    - 0.00015
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
    - 0.86738
    metric_stds:
    - null
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
    - 0.8673
    metric_stds:
    - 0.0005
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
    - 0.8671
    metric_stds:
    - 0.0005
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
    - 0.8669
    metric_stds:
    - 0.00059
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.86685
    metric_stds:
    - 0.00059
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
    - 0.8668
    metric_stds:
    - null
  - model: DGN
    model_plain: DGN
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
    - 0.8668
    metric_stds:
    - 0.00034
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
    - 0.86672
    metric_stds:
    - 0.00071
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
    - 0.8665
    metric_stds:
    - 0.00033
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
    - 0.8664
    metric_stds:
    - 0.0011
  - model: SAN+RWSE
    model_plain: SAN+RWSE
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
    - 0.86581
    metric_stds:
    - 0.00037
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
    - 0.8658
    metric_stds:
    - 0.00037
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8657
    metric_stds:
    - 0.0002
  - model: PNA
    model_plain: PNA
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
    - 0.86567
    metric_stds:
    - 0.00075
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
    - 0.86363
    metric_stds:
    - 0.00127
  - model: RingGNN, 2 layers
    model_plain: RingGNN, 2 layers
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.86245
    metric_stds:
    - null
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
    - 0.86
    metric_stds:
    - 0.0014
  - model: ViT-PS (Ours), 10-sample
    model_plain: ViT-PS (Ours), 10-sample
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85989
    metric_stds:
    - 0.00011
  - model: ViT-Canonical
    model_plain: ViT-Canonical
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85825
    metric_stds:
    - null
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
    - 0.85735
    metric_stds:
    - 0.00037
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
    - 0.85711
    metric_stds:
    - 0.00047
  - model: PPGN, 3 layers
    model_plain: PPGN, 3 layers
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85661
    metric_stds:
    - null
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
    - 0.85661
    metric_stds:
    - 0.00353
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85614
    metric_stds:
    - 0.00032
  - model: GCN-4
    model_plain: GCN-4
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
    - 0.856
    metric_stds:
    - 0.0
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
    - 0.8559
    metric_stds:
    - 0.00011
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8559
    metric_stds:
    - 0.0001
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
    - 0.8557
    metric_stds:
    - 0.00088
  - model: GatedGCN, 16 layers
    model_plain: GatedGCN, 16 layers
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85568
    metric_stds:
    - null
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
    - 0.85482
    metric_stds:
    - 0.00037
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8548
    metric_stds:
    - 0.0004
  - model: GIN
    model_plain: GIN
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
    - 0.8539
    metric_stds:
    - 0.00136
  - model: GCN, 16 layers
    model_plain: GCN, 16 layers
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85387
    metric_stds:
    - null
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
    - 0.84808
    metric_stds:
    - 0.00068
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
    - 0.848
    metric_stds:
    - 0.0
  - model: GIN-4
    model_plain: GIN-4
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
    - 0.848
    metric_stds:
    - 0.0
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
    - 0.8448
    metric_stds:
    - 0.00122
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8448
    metric_stds:
    - 0.0012
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
    - 0.8334
    metric_stds:
    - 0.0029
  - model: ViT-GA, 10-sample
    model_plain: ViT-GA, 10-sample
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8322
    metric_stds:
    - 0.00057
  - model: IPDGN
    model_plain: IPDGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    metric_stds:
    - 0.0011
  - model: GAT, 16 layers
    model_plain: GAT, 16 layers
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78271
    metric_stds:
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.7827
    metric_stds:
    - 0.00186
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
    - 0.75824
    metric_stds:
    - 0.01823
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
    - 0.75824
    metric_stds:
    - 0.01823
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7501
    metric_stds:
    - 0.0015
  - model: GCN
    model_plain: GCN
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
    - 0.7189
    metric_stds:
    - 0.00334
  - model: ViT-FA
    model_plain: ViT-FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71377
    metric_stds:
    - null
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
    - 0.70194
    metric_stds:
    - 0.00216
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
    - 0.6388
    metric_stds:
    - 0.00074
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6388
    metric_stds:
    - 0.0007
  - model: GAT-4
    model_plain: GAT-4
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
    - 0.583
    metric_stds:
    - 0.088
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
    - 0.583
    metric_stds:
    - 0.088
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
    - 0.54941
    metric_stds:
    - 0.03739
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
    - 0.50516
    metric_stds:
    - 1.0e-05
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
    - 0.50516
    metric_stds:
    - 1.0e-05
  milestones:
  - value: 0.96
    std: 0.002
    model: DGN
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: 2020-10
---

