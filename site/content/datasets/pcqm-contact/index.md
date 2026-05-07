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
  results:
  - model: SAN+LapPE
    value: 0.335
    std: 0.0003
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: SAN+RWSE
    value: 0.3341
    std: 0.0006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: GCN
    value: 0.3242
    std: 0.0008
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: GINE
    value: 0.318
    std: 0.0027
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  - model: Transformer+LapPE
    value: 0.3174
    std: 0.002
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
  milestones_json: '[{"value": 0.3242, "std": 0.0008, "model": "GCN", "arxiv_id":
    "2206.08164", "title": "Long Range Graph Benchmark", "date": "2022-06-16"}, {"value":
    0.335, "std": 0.0003, "model": "SAN+LapPE", "arxiv_id": "2206.08164", "title":
    "Long Range Graph Benchmark", "date": "2022-06-16"}]'
---

