---
title: Walmart
slug: walmart
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: Walmart co-purchase trip hypergraph node classification (product category,
  11 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats: null
result_count: 11
best_model:
  model: HealHGNN
  value: 0.6822
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  rows:
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
    is_best: true
    metric_values:
    - 0.6822
    metric_stds:
    - 0.005600000000000001
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
    - 0.6679
    metric_stds:
    - 0.0040999999999999995
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
    - 0.6546
    metric_stds:
    - 0.0025
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
    - 0.6517000000000001
    metric_stds:
    - 0.0079
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
    - 0.6455
    metric_stds:
    - 0.0033
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
    - 0.6343
    metric_stds:
    - 0.0043
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
    - 0.6235
    metric_stds:
    - 0.0026
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
    - 0.5864
    metric_stds:
    - 0.0074
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
    - 0.5445
    metric_stds:
    - 0.0037
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
    - 0.5118
    metric_stds:
    - 0.0034999999999999996
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
    - 0.4874
    metric_stds:
    - 0.0281
  milestones:
  - value: 0.6822
    std: 0.005600000000000001
    model: HealHGNN
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: 2026-03
---

