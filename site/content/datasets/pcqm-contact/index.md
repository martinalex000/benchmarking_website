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
    - 0.4703
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
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
    - 0.467
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
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
    - 0.4617
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
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
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
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
    - 0.3242
    - 0.1288
    - 0.8517
    - 0.3808
    metric_stds:
    - 0.0008
    - 0.0013
    - 0.0005
    - 0.0006
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
    - 0.3234
    - 0.1321
    - 0.8256
    - 0.3791
    metric_stds:
    - 0.0006
    - 0.0007
    - 0.0006
    - 0.0004
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
    - 0.3218
    - 0.1279
    - 0.8433
    - 0.3783
    metric_stds:
    - 0.0011
    - 0.0018
    - 0.0011
    - 0.0004
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
    date_iso: '2022-06-16'
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: null
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
    - 0.3161
    - 0.1325
    - 0.8116
    - 0.3607
    metric_stds:
    - 0.0004
    - 0.0009
    - 0.0009
    - 0.0003
  milestones:
  - value: 0.3234
    std: 0.0006
    model: GCN
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.335
    std: 0.0003
    model: SAN+LapPE
    arxiv_id: '2206.08164'
    title: Long Range Graph Benchmark
    date: '2022-06-16'
  - value: 0.467
    std: 0.0004
    model: GCN
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
  - value: 0.4703
    std: 0.0014
    model: GPS
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: '2023-09-01'
---

