---
title: Peptides-func
slug: peptides-func
benchmark: LRGB
task_type: graph_classification
description: Multi-label graph classification on peptide molecules (10 classes).
primary_metric: AP
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
stats:
  num_graphs: 15535
  avg_nodes: 150.94
  avg_edges: 307.3
  num_classes: 10
result_count: 24
best_model:
  model: DREW
  value: 0.715
  metric: AP
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
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    is_best: true
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
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    is_best: true
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
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6988
    metric_stds:
    - 0.0082
  - model: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6988
    metric_stds:
    - 0.0082
  - model: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.697
    metric_stds:
    - 0.008
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
    is_best: false
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
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6921
    metric_stds:
    - 0.0054
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
    is_best: false
    metric_values:
    - 0.6765
    metric_stds:
    - 0.0047
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6762
    metric_stds:
    - 0.0053
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
    is_best: false
    metric_values:
    - 0.6621
    metric_stds:
    - 0.0067
  - model: NID_GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6608
    metric_stds:
    - 0.0058
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6535
    metric_stds:
    - 0.0041
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
    is_best: false
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
    date_iso: '2023-09-01'
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6527
    metric_stds:
    - 0.0043
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
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
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    is_best: false
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
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    is_best: false
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
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6326
    metric_stds:
    - 0.0126
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6326
    metric_stds:
    - 0.0126
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
    is_best: false
    metric_values:
    - 0.6069
    metric_stds:
    - 0.0035
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
    is_best: false
    metric_values:
    - 0.593
    metric_stds:
    - 0.0023
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
    is_best: false
    metric_values:
    - 0.5864
    metric_stds:
    - 0.0077
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
    is_best: false
    metric_values:
    - 0.5543
    metric_stds:
    - 0.0078
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
    is_best: false
    metric_values:
    - 0.5498
    metric_stds:
    - 0.0079
  milestones:
  - value: 0.6439
    std: 0.0075
    model: SAN+RWSE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.715
    std: 0.0044
    model: DREW
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
---

