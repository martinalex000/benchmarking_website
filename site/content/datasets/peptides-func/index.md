---
title: Peptides-func
slug: peptides-func
benchmark: LRGB
task_type: graph_classification
description: Multi-label graph classification on peptide molecules (10 classes).
primary_metric: AP
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official random split (80/10/10). Metric: AP (Average Precision).'
  is_standard: true
  primary_metric: AP
  higher_is_better: true
  metrics:
  - AP
  rows:
  - model: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    metric_values:
    - 0.6439
    metric_stds:
    - 0.0075
  - model: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    metric_values:
    - 0.6384
    metric_stds:
    - 0.0121
  - model: Transformer+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    metric_values:
    - 0.6326
    metric_stds:
    - 0.0126
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    metric_values:
    - 0.6069
    metric_stds:
    - 0.0035
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    metric_values:
    - 0.5498
    metric_stds:
    - 0.0079
  milestones_json: '[{"value": 0.6069, "std": 0.0035, "model": "GCN", "arxiv_id":
    "2206.08164", "title": "Long Range Graph Benchmark", "date": "2022-06-16"}, {"value":
    0.6326, "std": 0.0126, "model": "Transformer+LapPE", "arxiv_id": "2206.08164",
    "title": "Long Range Graph Benchmark", "date": "2022-06-16"}, {"value": 0.6384,
    "std": 0.0121, "model": "SAN+LapPE", "arxiv_id": "2206.08164", "title": "Long
    Range Graph Benchmark", "date": "2022-06-16"}, {"value": 0.6439, "std": 0.0075,
    "model": "SAN+RWSE", "arxiv_id": "2206.08164", "title": "Long Range Graph Benchmark",
    "date": "2022-06-16"}]'
---

