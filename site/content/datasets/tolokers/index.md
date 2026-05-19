---
title: Tolokers
slug: tolokers
benchmark: Heterophilic Graphs
task_type: node_classification
description: Yandex Toloka worker network binary node classification from the heterophilic
  benchmark.
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.HeterophilousGraphDataset.html
stats:
  num_graphs: null
  avg_nodes: 11758.0
  avg_edges: 519000.0
  num_classes: 2
result_count: 84
best_model:
  model: GRAMA$_{GCN}$
  value: 0.8623
  metric: ROC-AUC
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  metrics:
  - ROC-AUC
  - Accuracy
  rows:
  - model: GRAMA$_{GCN}$
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8623
    - null
    metric_stds:
    - 0.011
    - null
  - model: GRAMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8623
    - null
    metric_stds:
    - 0.011
    - null
  - model: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8591
    - null
    metric_stds:
    - 0.0074
    - null
  - model: IM-CO-GNN(μ,μ)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8577
    - null
    metric_stds:
    - 0.0105
    - null
  - model: Tango\textsubscript{GPS}
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
    - 0.8565999999999999
    - null
    metric_stds:
    - 0.0101
    - null
  - model: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8557
    - null
    metric_stds:
    - 0.0061
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
    is_best: true
    metric_values:
    - 0.8556
    - null
    metric_stds:
    - 0.0074
    - null
  - model: Stable-ChebNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8555
    - null
    metric_stds:
    - 0.0335
    - null
  - model: Tango\textsubscript{GatedGCN}
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
    - 0.8551000000000001
    - null
    metric_stds:
    - 0.0098
    - null
  - model: CSNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8545
    - null
    metric_stds:
    - 0.0053
    - null
  - model: IM-GAT-sep
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8544
    - null
    metric_stds:
    - 0.004
    - null
  - model: MP-SSM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8526
    - null
    metric_stds:
    - 0.0093
    - null
  - model: IM-CO-GNN(Σ,Σ)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8525
    - null
    metric_stds:
    - 0.0103
    - null
  - model: IM-GAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8521
    - null
    metric_stds:
    - 0.0043
    - null
  - model: Lie Unitary GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: '2024-10-07'
    date_iso: '2024-10-07'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8518
    - null
    metric_stds:
    - 0.0043
    - null
  - model: GIN + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8511
    - null
    metric_stds:
    - 0.0077
    - null
  - model: R-GCN (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8511
    - null
    metric_stds:
    - 0.0077
    - null
  - model: IM-GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.851
    - null
    metric_stds:
    - 0.0084
    - null
  - model: GDT (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8502
    - null
    metric_stds:
    - 0.0067
    - null
  - model: Gated + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8502
    - null
    metric_stds:
    - 0.0067
    - null
  - model: GAT (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8499
    - null
    metric_stds:
    - 0.0054
    - null
  - model: GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8495
    - null
    metric_stds:
    - 0.0078
    - null
  - model: CO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8484
    - null
    metric_stds:
    - 0.0096
    - null
  - model: Unitary GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: '2024-10-07'
    date_iso: '2024-10-07'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8483
    - null
    metric_stds:
    - 0.0068
    - null
  - model: GPS₃₂GCN+Performer (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8481
    - null
    metric_stds:
    - 0.0086
    - null
  - model: GPS+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8481
    - null
    metric_stds:
    - 0.0086
    - null
  - model: BuNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8478
    - null
    metric_stds:
    - 0.008
    - null
  - model: GPS₃₀GCN+Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8472
    - null
    metric_stds:
    - 0.0077
    - null
  - model: GPSGCN+Performer (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8472
    - null
    metric_stds:
    - 0.0077
    - null
  - model: GPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8472
    - null
    metric_stds:
    - 0.0077
    - null
  - model: GPS₃₂GAT+Performer (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8462
    - null
    metric_stds:
    - 0.0054
    - null
  - model: GMN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8452
    - null
    metric_stds:
    - 0.0021
    - null
  - model: COMBA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    - null
    metric_stds:
    - 0.0009
    - null
  - model: IM-FAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8449
    - null
    metric_stds:
    - 0.0097
    - null
  - model: CO-GNN(μ, μ)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8445
    - null
    metric_stds:
    - 0.0117
    - null
  - model: CO-GNN($\mu$, $\mu$)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8445
    - null
    metric_stds:
    - 0.0117
    - null
  - model: GPS\textsubscript{GAT+Performer} (RWSE)
    is_baseline: true
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
    - 0.8438
    - null
    metric_stds:
    - 0.0091
    - null
  - model: GPS₃₀GAT+Performer (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8438
    - null
    metric_stds:
    - 0.0091
    - null
  - model: GAT (DEG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8422
    - null
    metric_stds:
    - 0.0081
    - null
  - model: IM-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8417
    - null
    metric_stds:
    - 0.0071
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8377
    - null
    metric_stds:
    - 0.0078
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8371
    - null
    metric_stds:
    - 0.0048
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    - null
    metric_stds:
    - 0.0047
    - null
  - model: GPS + Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    - null
    metric_stds:
    - 0.0105
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8364
    - null
    metric_stds:
    - 0.0067
    - null
  - model: GPSGCN+Transformer (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8353
    - null
    metric_stds:
    - 0.0106
    - null
  - model: GPSGCN+Transformer (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8351
    - null
    metric_stds:
    - 0.0093
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    metric_stds:
    - 0.0045
    - null
  - model: CO-GNN(Σ, Σ)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8336
    - null
    metric_stds:
    - 0.0089
    - null
  - model: CO-GNN($\Sigma$, $\Sigma$)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8336
    - null
    metric_stds:
    - 0.0089
    - null
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8323
    - null
    metric_stds:
    - 0.0064
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.832
    - null
    metric_stds:
    - 0.009
    - null
  - model: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8311
    - null
    metric_stds:
    - 0.0104
    - null
  - model: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8276
    - null
    metric_stds:
    - 0.0061
    - null
  - model: GAT-sep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8252
    - null
    metric_stds:
    - 0.0092
    - null
  - model: GCN (DEG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8251
    - null
    metric_stds:
    - 0.0083
    - null
  - model: GPS₃₂GAT+Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8245
    - null
    metric_stds:
    - 0.0089
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8243
    - null
    metric_stds:
    - 0.0044
    - null
  - model: IPR-MPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    metric_stds:
    - 0.008
    - null
  - model: GBK-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8101
    - null
    metric_stds:
    - 0.0067
    - null
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.807
    - null
    metric_stds:
    - 0.006
    - null
  - model: GPS₃₂GCN+Performer (DEG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8049
    - null
    metric_stds:
    - 0.0097
    - null
  - model: Graph Mamba-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    metric_stds:
    - 0.0199
    - null
  - model: O(d)-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7883
    - null
    metric_stds:
    - 0.0076
    - null
  - model: NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7883
    - null
    metric_stds:
    - 0.0076
    - null
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7832
    - null
    metric_stds:
    - 0.0095
    - null
  - model: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7775
    - null
    metric_stds:
    - 0.0105
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7731
    - null
    metric_stds:
    - 0.0114
    - null
  - model: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    metric_stds:
    - 0.0056
    - null
  - model: MLP-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7458
    - null
    metric_stds:
    - 0.0075
    - null
  - model: SGC-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    metric_stds:
    - 0.0135
    - null
  - model: GLoGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7339
    - null
    metric_stds:
    - 0.0117
    - null
  - model: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7336
    - null
    metric_stds:
    - 0.0101
    - null
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7335
    - null
    metric_stds:
    - 0.0101
    - null
  - model: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7294
    - null
    metric_stds:
    - 0.0097
    - null
  - model: MLP-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7189
    - null
    metric_stds:
    - 0.0082
    - null
  - model: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6866
    - null
    metric_stds:
    - 0.0065
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8364
    metric_stds:
    - null
    - 0.0067
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8243
    metric_stds:
    - null
    - 0.0044
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.837
    metric_stds:
    - null
    - 0.0047
  - model: GAT-sep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8252
    metric_stds:
    - null
    - 0.0092
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8323
    metric_stds:
    - null
    - 0.0064
  - model: CO-GNN($\Sigma$, $\Sigma$)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8336
    metric_stds:
    - null
    - 0.0089
  - model: CO-GNN($\mu$, $\mu$)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8445
    metric_stds:
    - null
    - 0.0117
  milestones:
  - value: 0.8452
    std: 0.0021
    model: GMN
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
  - value: 0.8478
    std: 0.008
    model: BuNN
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: 2024-05
  - value: 0.8591
    std: 0.0074
    model: Polynormer
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: 2024-06
  - value: 0.8623
    std: 0.011
    model: GRAMA
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: 2025-06
---

