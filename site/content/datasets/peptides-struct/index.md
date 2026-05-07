---
title: Peptides-struct
slug: peptides-struct
benchmark: LRGB
task_type: graph_regression
description: Multi-task graph regression on peptide structural properties (11 targets).
primary_metric: MAE
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official random split (80/10/10). Metric: MAE (lower is better).'
  is_standard: true
  results:
  - model: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: SAN+RWSE
    value: 0.2545
    std: 0.0012
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: SAN+LapPE
    value: 0.2683
    std: 0.0043
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: GCN
    value: 0.3357
    std: 0.0006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: GINE
    value: 0.3547
    std: 0.0045
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  milestones_json: '[{"value": 0.3357, "std": 0.0006, "model": "GCN", "arxiv_id":
    "2206.08164", "title": "Long Range Graph Benchmark", "date": "2022-06-16"}, {"value":
    0.2529, "std": 0.0016, "model": "Transformer+LapPE", "arxiv_id": "2206.08164",
    "title": "Long Range Graph Benchmark", "date": "2022-06-16"}]'
---

