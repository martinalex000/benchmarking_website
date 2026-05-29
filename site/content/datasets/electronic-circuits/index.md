---
title: Electronic Circuits
slug: electronic-circuits
benchmark: GraphBench
task_type: graph_classification
description: 'Analog circuit topology design. Graph-level task: predict 2 continuous
  performance metrics from graph structure across 3 circuit-size datasets.

  '
primary_metric: MAE
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 93000
  avg_nodes: 18.5
  avg_edges: 43.0
  num_classes: null
result_count: 10
best_model:
  model: LightGCN + SSC
  value: 0.0677
  metric: R@20
  arxiv_id: '2502.08071'
  paper_title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item
    Interaction with Graph-Structured Side Information'
variants:
- slug: standard-split
  name: Standard split
  notes: 93,000 graphs, 13–24 nodes, 30–56 edges. Graph-level regression.
  is_standard: true
  primary_metric: R@20
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - R@20
  rows:
  - model: LightGCN + SSC
    model_plain: LightGCN + SSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.0677
    metric_stds:
    - null
  - model: JGCF + SSC
    model_plain: JGCF + SSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0648
    metric_stds:
    - null
  - model: FREEDOM
    model_plain: FREEDOM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0647
    metric_stds:
    - null
  - model: BM3
    model_plain: BM3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0631
    metric_stds:
    - null
  - model: JGCF
    model_plain: JGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0618
    metric_stds:
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0579
    metric_stds:
    - null
  - model: BPR-MF
    model_plain: BPR-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0557
    metric_stds:
    - null
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0418
    metric_stds:
    - null
  - model: mGCN
    model_plain: mGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0339
    metric_stds:
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/yhhe2004/SSC-KDD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0309
    metric_stds:
    - null
  milestones:
  - value: 0.0677
    std: null
    model: LightGCN + SSC
    arxiv_id: '2502.08071'
    title: 'Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction
      with Graph-Structured Side Information'
    date: 2025-02
---

