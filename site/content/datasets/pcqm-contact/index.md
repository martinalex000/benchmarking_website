---
title: PCQM-Contact
slug: pcqm-contact
benchmark: LRGB
task_type: link_prediction
description: Link prediction of spatial atom contacts in quantum chemistry molecules.
primary_metric: MRR
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official split. Metric: MRR (Mean Reciprocal Rank). Also reported: Hits@1,
    Hits@3, Hits@10.'
  is_standard: true
  primary_metric: MRR
  higher_is_better: true
  metrics:
  - MRR
  - Hits@1
  - Hits@10
  - Hits@3
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
    - 0.335
    - 0.1355
    - 0.8478
    - 0.4004
    metric_stds:
    - 0.0003
    - 0.0017
    - 0.0044
    - 0.0021
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
    - 0.3341
    - 0.1312
    - 0.855
    - 0.403
    metric_stds:
    - 0.0006
    - 0.0016
    - 0.0024
    - 0.0008
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
    - 0.3242
    - 0.1288
    - 0.8517
    - 0.3808
    metric_stds:
    - 0.0008
    - 0.0013
    - 0.0005
    - 0.0006
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
    - 0.318
    - 0.1337
    - 0.8147
    - 0.3642
    metric_stds:
    - 0.0027
    - 0.0013
    - 0.0062
    - 0.0043
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
    - 0.3174
    - 0.1221
    - 0.8517
    - 0.3679
    metric_stds:
    - 0.002
    - 0.0011
    - 0.0039
    - 0.0033
  milestones_json: '[{"value": 0.3242, "std": 0.0008, "model": "GCN", "arxiv_id":
    "2206.08164", "title": "Long Range Graph Benchmark", "date": "2022-06-16"}, {"value":
    0.335, "std": 0.0003, "model": "SAN+LapPE", "arxiv_id": "2206.08164", "title":
    "Long Range Graph Benchmark", "date": "2022-06-16"}]'
---

