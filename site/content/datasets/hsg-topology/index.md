---
title: HSG-topology
slug: hsg-topology
benchmark: HSG-12M
task_type: graph_classification
description: Topology-based classification sub-task of the HSG-12M spatial graph benchmark.
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 1812325
  avg_nodes: null
  avg_edges: null
  num_classes: 1401
result_count: 8
best_model:
  model: GraphSAGE
  value: 0.62
  metric: Accuracy
  arxiv_id: '2506.08618'
  paper_title: HSG-12M
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
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.62
    metric_stds:
    - 0.003
  - model: CGCNN
    model_plain: CGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.566
    metric_stds:
    - 0.016
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.533
    metric_stds:
    - 0.017
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.434
    metric_stds:
    - 0.015
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.401
    metric_stds:
    - 0.003
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.397
    metric_stds:
    - 0.009
  - model: MF
    model_plain: MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.348
    metric_stds:
    - 0.012
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.095
    metric_stds:
    - 0.059
  milestones:
  - value: 0.62
    std: 0.003
    model: GraphSAGE
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: 2025-06
---

