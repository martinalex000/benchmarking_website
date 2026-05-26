---
title: TSP
slug: tsp
benchmark: GNNBenchmark
task_type: link_prediction
description: Travelling salesman problem — edge classification (in/not in optimal
  tour).
primary_metric: F1
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats:
  num_graphs: 12000
  avg_nodes: 275.4
  avg_edges: 6885.0
  num_classes: 2
result_count: 8
best_model:
  model: Proposed Method (Single Solution, Metric)
  value: 0.0
  metric: Gap
  arxiv_id: '2601.19094'
  paper_title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Gap
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Gap
  rows:
  - model: Proposed Method (Single Solution, Metric)
    model_plain: Proposed Method (Single Solution, Metric)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.0
    metric_stds:
    - null
  - model: Proposed Method (Multi-Solution, Metric, k=1)
    model_plain: Proposed Method (Multi-Solution, Metric, k=1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.001
    metric_stds:
    - null
  - model: Linkern
    model_plain: Linkern
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.002
    metric_stds:
    - null
  - model: mGAT (s.)
    model_plain: mGAT (s.)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.15543'
    title: Symmetry-preserving graph attention network to solve routing problems at
      multiple resolutions
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0025
    metric_stds:
    - null
  - model: mGAT
    model_plain: mGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.15543'
    title: Symmetry-preserving graph attention network to solve routing problems at
      multiple resolutions
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0025
    metric_stds:
    - null
  - model: POMO
    model_plain: POMO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.15543'
    title: Symmetry-preserving graph attention network to solve routing problems at
      multiple resolutions
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.007
    metric_stds:
    - null
  - model: Ours
    model_plain: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.15543'
    title: Symmetry-preserving graph attention network to solve routing problems at
      multiple resolutions
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0123
    metric_stds:
    - null
  - model: Sym-NCO
    model_plain: Sym-NCO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.15543'
    title: Symmetry-preserving graph attention network to solve routing problems at
      multiple resolutions
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.019
    metric_stds:
    - null
  milestones:
  - value: 0.0025
    std: null
    model: mGAT (s.)
    arxiv_id: '2310.15543'
    title: Symmetry-preserving graph attention network to solve routing problems at
      multiple resolutions
    date: 2023-10
  - value: 0.0
    std: null
    model: Proposed Method (Single Solution, Metric)
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: 2026-01
---

