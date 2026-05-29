---
title: Roman-empire
slug: roman-empire
benchmark: Heterophilic Graphs
task_type: node_classification
description: Wikipedia Roman Empire article node classification (18 syntactic roles)
  from the heterophilic benchmark.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.HeterophilousGraphDataset.html
stats: null
result_count: 65
best_model:
  model: CSNN
  value: 0.9263
  metric: Accuracy
  arxiv_id: '2507.00647'
  paper_title: Cooperative Sheaf Neural Networks
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
  - model: CSNN
    model_plain: CSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9263
    metric_stds:
    - 0.005
  - model: Polynormer
    model_plain: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9255
    metric_stds:
    - 0.003
  - model: Stable-ChebNet
    model_plain: Stable-ChebNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9203
    metric_stds:
    - 0.0085
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
    is_best: true
    metric_values:
    - 0.9189
    metric_stds:
    - 0.003
  - model: CO-GNN(Σ, Σ)
    model_plain: CO-GNN(Σ, Σ)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9157
    metric_stds:
    - 0.0032
  - model: CO-GNN(μ, μ)
    model_plain: CO-GNN(μ, μ)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9137
    metric_stds:
    - 0.0035
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9123
    metric_stds:
    - 0.0032
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
    - 0.9108
    metric_stds:
    - 0.0057
  - model: MP-SSM
    model_plain: MP-SSM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9091
    metric_stds:
    - 0.0048
  - model: COMBA
    model_plain: COMBA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.895
    metric_stds:
    - 0.0038
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8903
    metric_stds:
    - 0.0037
  - model: GRAMA_GCNI
    model_plain: GRAMA_GCNI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8861
    metric_stds:
    - 0.0043
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8807
    metric_stds:
    - 0.0027
  - model: GMN
    model_plain: GMN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8769
    metric_stds:
    - 0.005
  - model: GT-sep
    model_plain: GT-sep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8732
    metric_stds:
    - 0.0039
  - model: GPS_GCNI+Performer (RWSE)
    model_plain: GPS_GCNI+Performer (RWSE)
    is_baseline: true
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
    - 0.8704
    metric_stds:
    - 0.0058
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.869
    metric_stds:
    - 0.0092
  - model: GDT + RWSE
    model_plain: GDT + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8662
    metric_stds:
    - 0.0053
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8651
    metric_stds:
    - 0.0073
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8574
    metric_stds:
    - 0.0067
  - model: GCN (RWSE)
    model_plain: GCN (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8484
    metric_stds:
    - 0.0055
  - model: GAT (LapPE)
    model_plain: GAT (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.848
    metric_stds:
    - 0.0046
  - model: GPS_GCNI+Performer (RWSE)
    model_plain: GPS_GCNI+Performer (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8472
    metric_stds:
    - 0.0065
  - model: GPS_GCNI+Performer (LapPE)
    model_plain: GPS_GCNI+Performer (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8396
    metric_stds:
    - 0.0053
  - model: GCN (LapPE)
    model_plain: GCN (LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8337
    metric_stds:
    - 0.0055
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    metric_stds:
    - 0.0079
  - model: GPS + Mamba
    model_plain: GPS + Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.831
    metric_stds:
    - 0.0028
  - model: Gradient Gating
    model_plain: Gradient Gating
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8216
    metric_stds:
    - 0.0078
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    metric_stds:
    - 0.0061
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    metric_stds:
    - 0.0042
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8087
    metric_stds:
    - 0.003
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.0043
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7992
    metric_stds:
    - 0.0056
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.17893'
    title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context
      Gating State Space Models'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    metric_stds:
    - 0.0088
  - model: GBK-GNN
    model_plain: GBK-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7457
    metric_stds:
    - 0.0047
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7446
    metric_stds:
    - 0.0054
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7434
    metric_stds:
    - 0.0077
  - model: ResNet+SGC
    model_plain: ResNet+SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    metric_stds:
    - 0.0051
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7369
    metric_stds:
    - 0.0074
  - model: GOAT
    model_plain: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7159
    metric_stds:
    - 0.0125
  - model: JDR
    model_plain: JDR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7123
    metric_stds:
    - 0.0018
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7114
    metric_stds:
    - 0.0042
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6966
    metric_stds:
    - 0.0062
  - model: TRIGON
    model_plain: TRIGON
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6652
    metric_stds:
    - 0.0013
  - model: MLP-2
    model_plain: MLP-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6604
    metric_stds:
    - 0.0071
  - model: ResNet
    model_plain: ResNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6588
    metric_stds:
    - 0.0038
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6522
    metric_stds:
    - 0.0056
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6494
    metric_stds:
    - 0.0062
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6485
    metric_stds:
    - 0.0027
  - model: MLP-1
    model_plain: MLP-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6412
    metric_stds:
    - 0.0061
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6396
    metric_stds:
    - 0.0062
  - model: DR
    model_plain: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6199
    metric_stds:
    - 0.0014
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6011
    metric_stds:
    - 0.0052
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5963
    metric_stds:
    - 0.0069
  - model: BORF
    model_plain: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5858
    metric_stds:
    - 0.0014
  - model: DIGL
    model_plain: DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5393
    metric_stds:
    - 0.0014
  - model: GTR
    model_plain: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5331
    metric_stds:
    - 0.0023
  - model: DiGCN
    model_plain: DiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5271
    metric_stds:
    - 0.0032
  - model: SRDF
    model_plain: SRDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5253
    metric_stds:
    - 0.0013
  - model: FOSR
    model_plain: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5238
    metric_stds:
    - 0.0021
  - model: ResNet+adj
    model_plain: ResNet+adj
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/yandex-research/heterophilous-graphs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5225
    metric_stds:
    - 0.004
  - model: Base (GCN)
    model_plain: Base (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5166
    metric_stds:
    - 0.0017
  - model: Base (GAT)
    model_plain: Base (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4923
    metric_stds:
    - 0.0033
  - model: SGC-1
    model_plain: SGC-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.446
    metric_stds:
    - 0.0052
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3755
    metric_stds:
    - 0.0036
  milestones:
  - value: 0.8732
    std: 0.0039
    model: GT-sep
    arxiv_id: '2302.11640'
    title: 'A critical look at the evaluation of GNNs under heterophily: Are we really
      making progress?'
    date: 2023-02
  - value: 0.9123
    std: 0.0032
    model: Dir-GNN
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: 2023-05
  - value: 0.9255
    std: 0.003
    model: Polynormer
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: 2025-06
  - value: 0.9263
    std: 0.005
    model: CSNN
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: 2025-07
---

