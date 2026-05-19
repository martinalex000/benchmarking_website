---
title: ShapeNet-Part
slug: shapenet-part
benchmark: Other Graph Benchmarks
task_type: node_classification
description: '3D point cloud part segmentation on ShapeNet objects. Graph-based part
  label prediction on point cloud graphs (16 object categories, 50 part classes).

  '
primary_metric: F1
higher_is_better: true
pyg_url: ''
stats: null
result_count: 8
best_model:
  model: GPS + k-MIP
  value: 0.8268000000000001
  metric: F1
variants:
- slug: standard-split
  name: Standard split
  notes: 'Metric: mean IoU / F1 across parts.'
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
  - model: GPS + k-MIP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8268000000000001
    metric_stds:
    - 0.0064
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8262
    metric_stds:
    - 0.0031
  - model: GPS + BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7965000000000001
    metric_stds:
    - 0.0098
  - model: GPS + Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7736
    metric_stds:
    - 0.0123
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    metric_stds:
    - 0.0032
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6456999999999999
    metric_stds:
    - 0.0034999999999999996
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6301
    metric_stds:
    - 0.0017000000000000001
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6018
    metric_stds:
    - 0.0004
  milestones:
  - value: 0.8268000000000001
    std: 0.0064
    model: GPS + k-MIP
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: 2026-04
---

