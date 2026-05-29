---
title: RDT-B
slug: rdt-b
benchmark: TU Dortmund
task_type: graph_classification
description: Alias for REDDIT-BINARY in some papers.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 2000
  avg_nodes: 429.63
  avg_edges: 497.75
  num_classes: 2
result_count: 15
best_model:
  model: PDF
  value: 0.934
  metric: Accuracy
  arxiv_id: '2305.06102'
  paper_title: Towards Better Graph Representation Learning with Parameterized Decomposition
    & Filtering
variants:
- slug: 10-fold-cv
  name: 10-fold CV
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
  - model: PDF
    model_plain: PDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.934
    metric_stds:
    - 0.013
  - model: MOSGSL
    model_plain: MOSGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8745
    metric_stds:
    - 0.0219
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8552
    metric_stds:
    - 0.0079
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.848
    metric_stds:
    - 0.0625
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8415
    metric_stds:
    - 0.024700000000000003
  - model: CL
    model_plain: CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8399
    metric_stds:
    - 0.0034
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8263
    metric_stds:
    - 0.0099
  - model: EdgePool
    model_plain: EdgePool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8115000000000001
    metric_stds:
    - 0.0356
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7879
    metric_stds:
    - 0.0214
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.755
    metric_stds:
    - 0.024
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    metric_stds:
    - 0.0369
  - model: NeuralSparse
    model_plain: NeuralSparse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    metric_stds:
    - 0.0279
  - model: VIBGSL
    model_plain: VIBGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.684
    metric_stds:
    - 0.0381
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6779999999999999
    metric_stds:
    - 0.0424
  - model: RU-GIN
    model_plain: RU-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5897
    metric_stds:
    - 0.0013
  milestones:
  - value: 0.934
    std: 0.013
    model: PDF
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: '2023-05-10'
---

