---
title: Case 2
slug: case-2
benchmark: Power Flow Benchmarks
task_type: graph_regression
description: Power flow analysis on IEEE test case 2 (medium power grid, node-level
  regression).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 750000
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 12
best_model:
  model: MGMT
  value: 0.699
  metric: Accuracy
  arxiv_id: '2601.22593'
  paper_title: arXiv:2601.22593
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
  - model: MGMT
    model_plain: MGMT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.699
    metric_stds:
    - 0.0119
  - model: FlexCare
    model_plain: FlexCare
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6982
    metric_stds:
    - 0.0091
  - model: MT
    model_plain: MT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.663
    metric_stds:
    - 0.0112
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    metric_stds:
    - 0.0089
  - model: AMIGO
    model_plain: AMIGO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6573
    metric_stds:
    - 0.0089
  - model: MedFuse
    model_plain: MedFuse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6435
    metric_stds:
    - 0.0096
  - model: GNN
    model_plain: GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.642
    metric_stds:
    - 0.012
  - model: MaxCorrMGNN
    model_plain: MaxCorrMGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6372
    metric_stds:
    - 0.0164
  - model: MMGL
    model_plain: MMGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.628
    metric_stds:
    - 0.0084
  - model: MGLAM
    model_plain: MGLAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6229
    metric_stds:
    - 0.0129
  - model: MultiMoDN
    model_plain: MultiMoDN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.615
    metric_stds:
    - 0.0101
  - model: DNN
    model_plain: DNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.561
    metric_stds:
    - 0.0113
  milestones:
  - value: 0.699
    std: 0.0119
    model: MGMT
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: 2026-01
---

