---
title: PascalVOC-SP
slug: pascalvoc-sp
benchmark: LRGB
task_type: node_classification
description: Node classification on superpixel graphs derived from PascalVOC 2011.
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official split. Metric: macro F1.'
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
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
    - 0.323
    metric_stds:
    - 0.0039
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
    - 0.3216
    metric_stds:
    - 0.0027
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
    - 0.286
    metric_stds:
    - 0.0085
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
    - 0.2694
    metric_stds:
    - 0.0098
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
    - 0.1265
    metric_stds:
    - 0.0076
  milestones_json: '[{"value": 0.286, "std": 0.0085, "model": "GCN", "arxiv_id": "2206.08164",
    "title": "Long Range Graph Benchmark", "date": "2022-06-16"}, {"value": 0.323,
    "std": 0.0039, "model": "SAN+LapPE", "arxiv_id": "2206.08164", "title": "Long
    Range Graph Benchmark", "date": "2022-06-16"}]'
---

