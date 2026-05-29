---
title: HSG-12M
slug: hsg-12m
benchmark: HSG-12M
task_type: graph_classification
description: Node classification on the HSG-12M large-scale heterogeneous spatial
  graph (~12M edges).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 11601681
  avg_nodes: null
  avg_edges: null
  num_classes: 1401
result_count: 8
best_model:
  model: GraphSAGE
  value: 0.546
  metric: Accuracy
  arxiv_id: '2506.08618'
  paper_title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
    Spectra of Non-Hermitian Crystals'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.546
    metric_stds:
    - 0.004
  - model: CGCNN
    model_plain: CGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.531
    metric_stds:
    - 0.004
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46
    metric_stds:
    - 0.025
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.365
    metric_stds:
    - 0.021
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.365
    metric_stds:
    - 0.01
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.351
    metric_stds:
    - 0.002
  - model: MF
    model_plain: MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.295
    metric_stds:
    - 0.01
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/sarinstein-yan/Poly2Graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.063
    metric_stds:
    - 0.031
  milestones:
  - value: 0.546
    std: 0.004
    model: GraphSAGE
    arxiv_id: '2506.08618'
    title: 'HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy
      Spectra of Non-Hermitian Crystals'
    date: 2025-06
---

