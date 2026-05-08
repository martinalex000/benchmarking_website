---
title: COCO-SP
slug: coco-sp
benchmark: LRGB
task_type: node_classification
description: Node classification on superpixel graphs derived from MS-COCO.
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
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    metric_values:
    - 0.3884
    metric_stds:
    - 0.0055
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    metric_values:
    - 0.343
    metric_stds:
    - 0.0008
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    metric_values:
    - 0.2922
    metric_stds:
    - 0.0018
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.2641
    metric_stds:
    - 0.0045
  - model: Transformer+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.2618
    metric_stds:
    - 0.0031
  - model: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.2592
    metric_stds:
    - 0.0158
  - model: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.2574
    metric_stds:
    - 0.0034
  - model: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.2434
    metric_stds:
    - 0.0156
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    metric_values:
    - 0.2125
    metric_stds:
    - 0.0009
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.1404
    metric_stds:
    - 0.0011
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.1339
    metric_stds:
    - 0.0044
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.0841
    metric_stds:
    - 0.001
  milestones:
  - value: 0.0841
    std: 0.001
    model: GCN
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.1339
    std: 0.0044
    model: GINE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.2618
    std: 0.0031
    model: Transformer+LapPE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.2641
    std: 0.0045
    model: GatedGCN
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.2922
    std: 0.0018
    model: GCN
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
  - value: 0.3884
    std: 0.0055
    model: GPS
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
---

