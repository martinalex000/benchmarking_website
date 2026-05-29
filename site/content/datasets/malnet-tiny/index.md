---
title: MalNet-Tiny
slug: malnet-tiny
benchmark: Other Graph Benchmarks
task_type: graph_classification
description: 'Malware detection graph classification on a tiny (balanced 5-class)
  subset of the MalNet-Large dataset. Graphs are function call graphs of Android apps.

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MalNetTiny.html
stats:
  num_graphs: 5000
  avg_nodes: null
  avg_edges: null
  num_classes: 5
result_count: 12
best_model:
  model: Exphormer
  value: 0.9422
  metric: Accuracy
  arxiv_id: '2402.00789'
  paper_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
    State Spaces'
variants:
- slug: standard-split
  name: Standard split
  notes: '5 classes, 5,000 graphs total. Metric: Accuracy.'
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
  - model: Exphormer
    model_plain: Exphormer
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
    is_best: true
    metric_values:
    - 0.9422
    metric_stds:
    - 0.0024
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
    is_best: true
    metric_values:
    - 0.9406
    metric_stds:
    - 0.0064
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
    is_best: true
    metric_values:
    - 0.9372
    metric_stds:
    - 0.0029
  - model: DAG+GraphGPS
    model_plain: DAG+GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9345
    metric_stds:
    - 0.0041
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285125
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
    - 0.934
    metric_stds:
    - 0.0027
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
    - 0.9264
    metric_stds:
    - 0.0078
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9264
    metric_stds:
    - 0.0078
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
    - 0.9234
    metric_stds:
    - 0.0034
  - model: GatedGCN
    model_plain: GatedGCN
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
    - 0.9223
    metric_stds:
    - 0.0065
  - model: GAT
    model_plain: GAT
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
    - 0.921
    metric_stds:
    - 0.0024
  - model: GIN
    model_plain: GIN
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
    - 0.8898
    metric_stds:
    - 0.0055
  - model: GCN
    model_plain: GCN
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
    - 0.81
    metric_stds:
    - null
  milestones:
  - value: 0.9345
    std: 0.0041
    model: DAG+GraphGPS
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: '2022-10-24'
  - value: 0.9422
    std: 0.0024
    model: Exphormer
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
---

