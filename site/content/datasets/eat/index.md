---
title: EAT
slug: eat
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: European Airport Transactions hypergraph node classification (4 region
  classes, 399 nodes).
primary_metric: F1
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 1
  avg_nodes: 399.0
  avg_edges: null
  num_classes: 4
result_count: 31
best_model:
  model: CV
  value: 0.5763
  metric: F1
  arxiv_id: '2307.14613'
  paper_title: Self-Contrastive Graph Diffusion Network
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - ARI
  - NMI
  rows:
  - model: CV
    model_plain: CV
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.5763
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: MGAE
    model_plain: MGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4308
    - null
    - null
    metric_stds:
    - 0.0326
    - null
    - null
  - model: DFCN
    model_plain: DFCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4295
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
  - model: ProGCL
    model_plain: ProGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4254
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
  - model: AGC-DRR
    model_plain: AGC-DRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.352
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3472
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3053
    - null
    - null
    metric_stds:
    - 0.0147
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2535
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
  - model: GDCL
    model_plain: GDCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2502
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
  - model: AutoSSL
    model_plain: AutoSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2182
    - null
    - null
    metric_stds:
    - 0.0098
    - null
    - null
  - model: DEC
    model_plain: DEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.036
    - 0.0496
    metric_stds:
    - null
    - 0.0187
    - 0.0174
  - model: DCN
    model_plain: DCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.0511
    - 0.0692
    metric_stds:
    - null
    - 0.0265
    - 0.028
  - model: IDEC
    model_plain: IDEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.0319
    - 0.0463
    metric_stds:
    - null
    - 0.0076
    - 0.0097
  - model: AdaGAE
    model_plain: AdaGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.0247
    - 0.0436
    metric_stds:
    - null
    - 0.0054
    - 0.0187
  - model: MGAE
    model_plain: MGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1833
    - 0.2069
    metric_stds:
    - null
    - 0.0179
    - 0.0098
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.205
    - 0.2133
    metric_stds:
    - null
    - 0.0051
    - 0.0044
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1657
    - 0.2544
    metric_stds:
    - null
    - 0.0031
    - 0.0031
  - model: SDCN
    model_plain: SDCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.2163
    - 0.2161
    metric_stds:
    - null
    - 0.0149
    - 0.0126
  - model: AGE
    model_plain: AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.2039
    - 0.2364
    metric_stds:
    - null
    - 0.007
    - 0.0066
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1712
    - 0.2153
    metric_stds:
    - null
    - 0.0146
    - 0.0094
  - model: DFCN
    model_plain: DFCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1187
    - 0.2649
    metric_stds:
    - null
    - 0.0023
    - 0.0041
  - model: GDCL
    model_plain: GDCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.2176
    - 0.251
    metric_stds:
    - null
    - 0.0001
    - 0.0001
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1437
    - 0.2405
    metric_stds:
    - null
    - 0.0019
    - 0.0025
  - model: MCGC
    model_plain: MCGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1221
    - 0.1664
    metric_stds:
    - null
    - 0.0013
    - 0.0041
  - model: AutoSSL
    model_plain: AutoSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1313
    - 0.1786
    metric_stds:
    - null
    - 0.0071
    - 0.0022
  - model: AGC-DRR
    model_plain: AGC-DRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.095
    - 0.1115
    metric_stds:
    - null
    - 0.0025
    - 0.0024
  - model: DCRNN
    model_plain: DCRNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1717
    - 0.2409
    metric_stds:
    - null
    - 0.0069
    - 0.0053
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1362
    - 0.1733
    metric_stds:
    - null
    - 0.0057
    - 0.0054
  - model: ProGCL
    model_plain: ProGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1474
    - 0.2204
    metric_stds:
    - null
    - 0.0199
    - 0.0223
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.1951
    - 0.2185
    metric_stds:
    - null
    - 0.0045
    - 0.0062
  - model: RGC
    model_plain: RGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.3016
    - 0.3777
    metric_stds:
    - null
    - 0.0015
    - 0.0013
  milestones:
  - value: 0.5763
    std: 0.001
    model: CV
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: 2023-07
---

