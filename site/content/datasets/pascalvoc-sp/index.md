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
  - model: CRAWL
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
    - 0.4588
    metric_stds:
    - 0.0079
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
    - 0.444
    metric_stds:
    - 0.0065
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
    - 0.396
    metric_stds:
    - 0.0027
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
    - 0.388
    metric_stds:
    - 0.004
  - model: DREW
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
    - 0.3314
    metric_stds:
    - 0.0024
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
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.3216
    metric_stds:
    - 0.0027
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
    - 0.2873
    metric_stds:
    - 0.0219
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
    - 0.286
    metric_stds:
    - 0.0085
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
    - 0.2718
    metric_stds:
    - 0.0054
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
    - 0.2694
    metric_stds:
    - 0.0098
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
    - 0.1698
    metric_stds:
    - 0.008
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
    - 0.1268
    metric_stds:
    - 0.006
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
    - 0.1265
    metric_stds:
    - 0.0076
  milestones:
  - value: 0.323
    std: 0.0039
    model: SAN+LapPE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.4588
    std: 0.0079
    model: CRAWL
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
---

