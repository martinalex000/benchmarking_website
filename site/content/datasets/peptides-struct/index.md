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
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  rows:
  - model: Graph ViT
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
    - 0.2449
    metric_stds:
    - 0.0016
  - model: GRIT
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
    - 0.246
    metric_stds:
    - 0.0012
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
    - 0.2473
    metric_stds:
    - 0.0017
  - model: G-MLPMixer
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
    - 0.2475
    metric_stds:
    - 0.0015
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
    - 0.2477
    metric_stds:
    - 0.0009
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
    - 0.2481
    metric_stds:
    - 0.0007
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
    - 0.2506
    metric_stds:
    - 0.0022
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
    - 0.2509
    metric_stds:
    - 0.0014
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
    - 0.2529
    metric_stds:
    - 0.0016
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
    - 0.2536
    metric_stds:
    - 0.0015
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
    - 0.2545
    metric_stds:
    - 0.0012
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
    - 0.2683
    metric_stds:
    - 0.0043
  - model: GatedGCN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: Jun 2022
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    metric_values:
    - 0.3357
    metric_stds:
    - 0.0006
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
    - 0.342
    metric_stds:
    - 0.0013
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
    - 0.3471
    metric_stds:
    - 0.001
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
    - 0.3496
    metric_stds:
    - 0.0013
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
    - 0.3547
    metric_stds:
    - 0.0045
  milestones:
  - value: 0.3496
    std: 0.0013
    model: GCN
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.2529
    std: 0.0016
    model: Transformer+LapPE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.2477
    std: 0.0009
    model: GCN
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
  - value: 0.2473
    std: 0.0017
    model: GINE
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
  - value: 0.246
    std: 0.0012
    model: GRIT
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
  - value: 0.2449
    std: 0.0016
    model: Graph ViT
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
---

