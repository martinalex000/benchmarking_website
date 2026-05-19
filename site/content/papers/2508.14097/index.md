---
title: Non-Dissipative Graph Propagation for Non-Local Community Detection
arxiv_id: '2508.14097'
authors: []
published_date: Aug 2025
abstract: Community detection in graphs aims to cluster nodes into meaningful groups,
  a task particularly challenging in heterophilic graphs, where nodes sharing similarities
  and membership to the same community are typically distantly connected. This is
  particularly evident when this task is tackled by graph neural networks, since they
  rely on an inherently local message passing scheme to learn the node representations
  that serve to cluster nodes into communities. In this work, we argue that the ability
  to propagate long-range information during message passing is key to effectively
  perform community detection in heterophilic graphs. To this end, we introduce the
  Unsupervised Antisymmetric Graph Neural Network (uAGNN), a novel unsupervised community
  detection approach leveraging non-dissipative dynamical systems to ensure stability
  and to propagate long-range information effectively. By employing antisymmetric
  weight matrices, uAGNN captures both local and global graph structures, overcoming
  the limitations posed by heterophilic scenarios. Extensive experiments across ten
  datasets demonstrate uAGNN's superior performance in high and medium heterophilic
  settings, where traditional methods fail to exploit long-range dependencies. These
  results highlight uAGNN's potential as a powerful tool for unsupervised community
  detection in diverse graph environments.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- uAGNN
mrr: 0.0071
results:
- &id008
  dataset: AMAP
  rows:
  - model: DMON
    value: 0.67
    std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: SUBLIME
    value: 0.65
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: VGAER
    value: 0.61
    std: 0.16
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: GRACE
    value: 0.51
    std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: BGRL
    value: 0.48
    std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: true
  - model: uAGNN
    value: 0.48
    std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: DAEGC
    value: 0.34
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: DGI
    value: 0.34
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: MVGRL
    value: 0.25
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  metric: F1
  higher_is_better: true
- &id006
  dataset: Amazon-Computers
  rows:
  - model: GAT
    value: 0.9409
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.9399
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Polynormer
    value: 0.9378
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DMON
    value: 0.67
    std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SUBLIME
    value: 0.65
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: VGAER
    value: 0.61
    std: 0.16
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GRACE
    value: 0.51
    std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BGRL
    value: 0.48
    std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: uAGNN
    value: 0.48
    std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DAEGC
    value: 0.34
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DGI
    value: 0.34
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MVGRL
    value: 0.25
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: BAT
  rows:
  - model: MVGRL
    value: 0.65
    std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: uAGNN
    value: 0.54
    std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GRACE
    value: 0.53
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: BGRL
    value: 0.52
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: DAEGC
    value: 0.46
    std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: DGI
    value: 0.44
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: DMON
    value: 0.38
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: SUBLIME
    value: 0.36
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: VGAER
    value: 0.36
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 9
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: CiteSeer
  rows:
  - model: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DGI
    value: 0.63
    std: 0.01
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 99
    is_best: false
  - model: GRACE
    value: 0.61
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: VGAER
    value: 0.61
    std: 0.14
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DAEGC
    value: 0.6
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MVGRL
    value: 0.58
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: uAGNN
    value: 0.55
    std: 0.11
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMON
    value: 0.5
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 207
    is_best: false
  - model: BGRL
    value: 0.5
    std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SUBLIME
    value: 0.38
    std: 0.15
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 120
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Cora
  rows:
  - model: GPM
    value: 0.9285
    std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: DGI
    value: 0.61
    std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 226
    is_best: false
  - model: DAEGC
    value: 0.58
    std: 0.08
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GRACE
    value: 0.54
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MVGRL
    value: 0.54
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: VGAER
    value: 0.54
    std: 0.14
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMON
    value: 0.48
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 284
    is_best: false
  - model: uAGNN
    value: 0.48
    std: 0.08
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SUBLIME
    value: 0.39
    std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 124
    is_best: false
  - model: BGRL
    value: 0.38
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 232
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Cornell
  is_multi_metric: true
  rows:
  - model: ACM-Snowball-2
    metric_values:
    - 0.9525
    - null
    metric_stds:
    - 0.0155
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ACMGCN
    metric_values:
    - 0.9393
    - null
    metric_stds:
    - 0.0105
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: ACM-SGC-1
    metric_values:
    - 0.9377
    - null
    metric_stds:
    - 0.0217
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DGI
    metric_values:
    - 0.34
    - 0.06
    metric_stds:
    - 0.06
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: DMON
    metric_values:
    - 0.34
    - 0.22
    metric_stds:
    - 0.05
    - 0.07
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: uAGNN
    metric_values:
    - 0.29
    - 0.27
    metric_stds:
    - 0.04
    - 0.07
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: MVGRL
    metric_values:
    - 0.27
    - 0.06
    metric_stds:
    - 0.05
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: GRACE
    metric_values:
    - 0.25
    - 0.05
    metric_stds:
    - 0.03
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: BGRL
    metric_values:
    - 0.25
    - 0.05
    metric_stds:
    - 0.02
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: DAEGC
    metric_values:
    - 0.24
    - 0.05
    metric_stds:
    - 0.03
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: SUBLIME
    metric_values:
    - 0.23
    - 0.03
    metric_stds:
    - 0.03
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 62
  - model: VGAER
    metric_values:
    - 0.22
    - 0.08
    metric_stds:
    - 0.02
    - 0.03
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  metrics:
  - F1
  - NMI
  primary_metric: Accuracy
  higher_is_better: true
- &id012
  dataset: DBLP
  rows:
  - model: HGSL
    value: 0.9249
    std: 0.0035
    metric: Micro-F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GTN
    value: 0.9148
    std: 0.0039
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: HAN
    value: 0.9147
    std: 0.0022
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: DAEGC
    value: 0.72
    std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: uAGNN
    value: 0.71
    std: 0.14
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GRACE
    value: 0.64
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SUBLIME
    value: 0.6
    std: 0.11
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: MVGRL
    value: 0.55
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMON
    value: 0.5
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: VGAER
    value: 0.5
    std: 0.13
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BGRL
    value: 0.45
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DGI
    value: 0.42
    std: 0.21
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id011
  dataset: EAT
  rows:
  - model: GRACE
    value: 0.48
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: MVGRL
    value: 0.47
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: uAGNN
    value: 0.47
    std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: DGI
    value: 0.46
    std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: SUBLIME
    value: 0.42
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 5
    is_best: true
  - model: DAEGC
    value: 0.41
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: DMON
    value: 0.35
    std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: VGAER
    value: 0.34
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: BGRL
    value: 0.19
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 9
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: Texas
  is_multi_metric: true
  rows:
  - model: ACMGCN
    metric_values:
    - 0.9656
    - null
    metric_stds:
    - 0.02
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ACM-Snowball-2
    metric_values:
    - 0.9574
    - null
    metric_stds:
    - 0.0222
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: ACMII-Snowball-3
    metric_values:
    - 0.9475
    - null
    metric_stds:
    - 0.0309
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DAEGC
    metric_values:
    - 0.35
    - 0.14
    metric_stds:
    - 0.05
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: DMON
    metric_values:
    - 0.33
    - 0.21
    metric_stds:
    - 0.02
    - 0.04
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: uAGNN
    metric_values:
    - 0.33
    - 0.22
    metric_stds:
    - 0.09
    - 0.07
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: DGI
    metric_values:
    - 0.31
    - 0.12
    metric_stds:
    - 0.03
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: GRACE
    metric_values:
    - 0.29
    - 0.15
    metric_stds:
    - 0.08
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: MVGRL
    metric_values:
    - 0.29
    - 0.1
    metric_stds:
    - 0.02
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: BGRL
    metric_values:
    - 0.24
    - 0.06
    metric_stds:
    - 0.03
    - 0.03
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: VGAER
    metric_values:
    - 0.24
    - 0.08
    metric_stds:
    - 0.03
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: SUBLIME
    metric_values:
    - 0.21
    - 0.03
    metric_stds:
    - 0.03
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 78
  metrics:
  - F1
  - NMI
  primary_metric: Accuracy
  higher_is_better: true
- &id010
  dataset: UAT
  rows:
  - model: DAEGC
    value: 0.54
    std: 0.01
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2019
    global_rank: 1
    is_best: true
  - model: uAGNN
    value: 0.53
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: DGI
    value: 0.52
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2019
    global_rank: 3
    is_best: true
  - model: GRACE
    value: 0.52
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    global_rank: 4
    is_best: true
  - model: DMON
    value: 0.49
    std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tsitsulin et al. 2023
    global_rank: 5
    is_best: true
  - model: MVGRL
    value: 0.49
    std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hassani et al. 2020
    global_rank: 6
    is_best: true
  - model: BGRL
    value: 0.48
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor et al. 2021
    global_rank: 7
    is_best: false
  - model: VGAER
    value: 0.44
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qiu et al. 2022
    global_rank: 8
    is_best: false
  - model: SUBLIME
    value: 0.17
    std: 0.13
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    global_rank: 9
    is_best: false
  metric: F1
  higher_is_better: true
- &id007
  dataset: Weather Forecasting
  rows:
  - model: GRACE
    value: 0.48
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: MVGRL
    value: 0.47
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: uAGNN
    value: 0.47
    std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: DGI
    value: 0.46
    std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: SUBLIME
    value: 0.42
    std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: DAEGC
    value: 0.41
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMON
    value: 0.35
    std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: VGAER
    value: 0.34
    std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BGRL
    value: 0.19
    std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: MAE
  higher_is_better: true
- &id003
  dataset: Wisconsin
  rows:
  - model: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: uAGNN
    value: 0.43
    std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 140
    is_best: false
  - model: DMON
    value: 0.39
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 141
    is_best: false
  - model: GRACE
    value: 0.29
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 142
    is_best: false
  - model: DAEGC
    value: 0.28
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 143
    is_best: false
  - model: VGAER
    value: 0.27
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 144
    is_best: false
  - model: MVGRL
    value: 0.25
    std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 145
    is_best: false
  - model: DGI
    value: 0.24
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 146
    is_best: false
  - model: SUBLIME
    value: 0.23
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 51
    is_best: false
  - model: BGRL
    value: 0.19
    std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 147
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Classic
  datasets:
  - *id004
  - *id005
  - *id006
- benchmark: GraphBench
  datasets:
  - *id007
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id008
  - *id009
  - *id010
  - *id011
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id012
single_proposed_model: uAGNN
main_figure: /figures/2508.14097/main_figure.png
---

