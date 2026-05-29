---
title: ECHO-Synth
slug: echo-synth
benchmark: ECHO Benchmark
task_type: graph_regression
description: ECHO synthetic propagation task — node-level regression on synthetic
  long-range graphs.
primary_metric: MAE
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 10080
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 5
best_model:
  model: SDNE
  value: 0.987
  metric: MAP
  arxiv_id: '1805.11273'
  paper_title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: MAP
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAP
  rows:
  - model: SDNE
    model_plain: SDNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.987
    metric_stds:
    - null
  - model: DynGEM
    model_plain: DynGEM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.987
    metric_stds:
    - null
  - model: GF_init
    model_plain: GF_init
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.126
    metric_stds:
    - null
  - model: SDNE_align
    model_plain: SDNE_align
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.119
    metric_stds:
    - null
  - model: GF_align
    model_plain: GF_align
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.027
    metric_stds:
    - null
  milestones:
  - value: 0.987
    std: null
    model: SDNE
    arxiv_id: '1805.11273'
    title: 'DynGEM: Deep Embedding Method for Dynamic Graphs'
    date: 2018-05
---

