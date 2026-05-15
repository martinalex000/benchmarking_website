---
title: Flow
slug: flow
benchmark: GraphBench
task_type: graph_regression
description: Network flow value prediction (GraphBench / CLRS-style algorithmic reasoning).
primary_metric: MAE
higher_is_better: false
pyg_url: https://graphbench.github.io/website/datasets.html
stats: null
result_count: 5
best_model:
  model: RRWP
  value: 1.45
  metric: MAE
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  rows:
  - model: RRWP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.45
    metric_stds:
    - 0.06
  - model: RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.49
    metric_stds:
    - 0.02
  - model: NoPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.73
    metric_stds:
    - 0.09
  - model: LPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.75
    metric_stds:
    - 0.12
  - model: SPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.98
    metric_stds:
    - 0.14
  milestones:
  - value: 1.45
    std: 0.06
    model: RRWP
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: 2025-11
- slug: easy
  name: Easy
  notes: Small graph instances.
  is_standard: false
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  rows:
  - model: agg + I
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 1.83
    metric_stds:
    - 0.01
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 3.4387
    metric_stds:
    - 0.0631
  - model: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 4.27
    metric_stds:
    - null
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 4.2737
    metric_stds:
    - 0.0646
  milestones:
  - value: 3.4387
    std: 0.0631
    model: GIN
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
  - value: 1.83
    std: 0.01
    model: agg + I
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: 2026-05
- slug: hard
  name: Hard
  notes: Large graph instances.
  is_standard: false
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  - RMSE
  rows:
  - model: RRWP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.45
    - null
    metric_stds:
    - 0.06
    - null
  - model: RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.49
    - null
    metric_stds:
    - 0.02
    - null
  - model: NoPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.73
    - null
    metric_stds:
    - 0.09
    - null
  - model: LPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.75
    - null
    metric_stds:
    - 0.12
    - null
  - model: SPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.98
    - null
    metric_stds:
    - 0.14
    - null
  - model: agg + I
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 5.26
    - null
    metric_stds:
    - 0.03
    - null
  - model: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 6.48
    - null
    metric_stds:
    - null
    - null
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 6.4833
    - null
    metric_stds:
    - 0.0869
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 9.5061
    - null
    metric_stds:
    - 0.1265
    - null
  - model: U-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05964'
    title: Multiscale Neural Operators for Solving Time-Independent PDEs
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0064
    metric_stds:
    - null
    - null
  - model: FNO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05964'
    title: Multiscale Neural Operators for Solving Time-Independent PDEs
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.012
    metric_stds:
    - null
    - null
  - model: MGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05964'
    title: Multiscale Neural Operators for Solving Time-Independent PDEs
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0641
    metric_stds:
    - null
    - 0.000523
  - model: MGN + Tree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05964'
    title: Multiscale Neural Operators for Solving Time-Independent PDEs
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0413
    metric_stds:
    - null
    - 0.0147
  - model: BSMS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05964'
    title: Multiscale Neural Operators for Solving Time-Independent PDEs
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.00983
    metric_stds:
    - null
    - 0.000818
  - model: Perceiver IO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05964'
    title: Multiscale Neural Operators for Solving Time-Independent PDEs
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0141
    metric_stds:
    - null
    - 0.00116
  - model: Perceiver IO + GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05964'
    title: Multiscale Neural Operators for Solving Time-Independent PDEs
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0131
    metric_stds:
    - null
    - 0.000219
  milestones:
  - value: 1.45
    std: 0.06
    model: RRWP
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: 2025-11
- slug: medium
  name: Medium
  notes: Medium-scale graph instances.
  is_standard: false
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  rows:
  - model: agg + I
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 5.3
    metric_stds:
    - 0.12
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 6.3786
    metric_stds:
    - 0.4262
  - model: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 6.38
    metric_stds:
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 9.596
    metric_stds:
    - 0.1707
  milestones:
  - value: 6.3786
    std: 0.4262
    model: GT
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
  - value: 5.3
    std: 0.12
    model: agg + I
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: 2026-05
---

