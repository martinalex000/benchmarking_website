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
  - model: DREW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.715
    metric_stds:
    - 0.0044
  - model: CRAWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.7074
    metric_stds:
    - 0.0032
  - model: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.6988
    metric_stds:
    - 0.0082
  - model: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.6942
    metric_stds:
    - 0.0075
  - model: G-MLPMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.6921
    metric_stds:
    - 0.0054
  - model: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.6765
    metric_stds:
    - 0.0047
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.6621
    metric_stds:
    - 0.0067
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.6534
    metric_stds:
    - 0.0091
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    metric_values:
    - 0.6527
    metric_stds:
    - 0.0043
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
  milestones:
  - value: 0.6069
    std: 0.0035
    model: GCN
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.6326
    std: 0.0126
    model: Transformer+LapPE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.6384
    std: 0.0121
    model: SAN+LapPE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.6439
    std: 0.0075
    model: SAN+RWSE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.6765
    std: 0.0047
    model: GCN
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
  - value: 0.7074
    std: 0.0032
    model: CRAWL
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
  - value: 0.715
    std: 0.0044
    model: DREW
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
---

