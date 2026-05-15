---
title: DBLP
slug: dblp
benchmark: Heterogeneous Graph Benchmarks
task_type: node_classification
description: Heterogeneous academic graph — classify author nodes (4 research areas).
primary_metric: Micro-F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.DBLP.html
stats: null
result_count: 54
best_model:
  model: HGSL
  value: 0.9249
  metric: Micro-F1
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Micro-F1
  higher_is_better: true
  metrics:
  - Micro-F1
  - ACC
  - Accuracy
  - COS
  - F1
  - Normalized AUAC
  rows:
  - model: HGSL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9249
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
  - model: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9182
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
  - model: GTN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9148
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
  - model: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9147
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9113
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9099
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
  - model: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9065
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
    - null
    - null
    - null
  - model: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9061
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
    - null
    - null
  - model: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8943
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
  - model: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8874
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
    - null
    - null
    - null
  - model: ProGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8483
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0136
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8056
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
    - null
    - null
    - null
  - model: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7769
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
  - model: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7642
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0195
    - null
    - null
    - null
    - null
    - null
  - model: HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9120999999999999
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0037
    - null
    - null
    - null
  - model: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8998
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0043
    - null
    - null
    - null
  - model: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8678
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0029
    - null
    - null
    - null
  - model: HCHA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9092
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0022
    - null
    - null
    - null
  - model: UniGCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9168999999999999
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0019
    - null
    - null
    - null
  - model: AllDeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9127
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0027
    - null
    - null
    - null
  - model: AllSetTransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9153
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0023
    - null
    - null
    - null
  - model: Deep-HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9176000000000001
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0028000000000000004
    - null
    - null
    - null
  - model: ED-HNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.919
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0019
    - null
    - null
    - null
  - model: SheafHyperGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9159
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0024
    - null
    - null
    - null
  - model: PhenomNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9186
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0022
    - null
    - null
    - null
  - model: HealHGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9198000000000001
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0031
    - null
    - null
    - null
  - model: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.72
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.05
    - null
  - model: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.42
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.21
    - null
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.5
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.07
    - null
  - model: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.64
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.07
    - null
  - model: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.55
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.07
    - null
  - model: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.6
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.11
    - null
  - model: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.45
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.06
    - null
  - model: VGAER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.5
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.13
    - null
  - model: uAGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.71
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.14
    - null
  - model: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.495
    - null
    - 0.574
    - null
    - null
    metric_stds:
    - null
    - 0.049
    - null
    - 0.0
    - null
    - null
  - model: MinCut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.692
    - null
    - 0.525
    - null
    - null
    metric_stds:
    - null
    - 0.034
    - null
    - 0.039
    - null
    - null
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.637
    - null
    - 0.454
    - null
    - null
    metric_stds:
    - null
    - 0.032
    - null
    - 0.013
    - null
    - null
  - model: JBGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.686
    - null
    - 0.53
    - null
    - null
    metric_stds:
    - null
    - 0.018
    - null
    - 0.044
    - null
    - null
  - model: BNPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.752
    - null
    - 0.585
    - null
    - null
    metric_stds:
    - null
    - 0.007
    - null
    - 0.007
    - null
    - null
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5169
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.004
  - model: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5276
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.011
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5899
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0295
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5636
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0195
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5841
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0167
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5894
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0092
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5721
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0209
  - model: GatedGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6384
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0256
  - model: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6186
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0136
  - model: Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6114
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0128
  - model: 1-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6416
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0196
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5938
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0192
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5813
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.03
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.07188'
    title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking
      from A Spectral Perspective'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6288
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0133
  milestones:
  - value: 0.9249
    std: 0.0035
    model: HGSL
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: 2023-10
---

