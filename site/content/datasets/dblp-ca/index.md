---
title: DBLP-CA
slug: dblp-ca
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: DBLP co-authorship hypergraph node classification (research area).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 1
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 12
best_model:
  model: HealHGNN
  value: 0.9198000000000001
  metric: Accuracy
  arxiv_id: '2603.00599'
  paper_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local
    Exchanger
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  rows:
  - model: HealHGNN
    model_plain: HealHGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9198000000000001
    metric_stds:
    - 0.0031
  - model: ED-HNN
    model_plain: ED-HNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.919
    metric_stds:
    - 0.0019
  - model: PhenomNN
    model_plain: PhenomNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9186
    metric_stds:
    - 0.0022
  - model: Deep-HGNN
    model_plain: Deep-HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9176000000000001
    metric_stds:
    - 0.0028000000000000004
  - model: UniGCNII
    model_plain: UniGCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9168999999999999
    metric_stds:
    - 0.0019
  - model: SheafHyperGNN
    model_plain: SheafHyperGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9159
    metric_stds:
    - 0.0024
  - model: AllSetTransformer
    model_plain: AllSetTransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9153
    metric_stds:
    - 0.0023
  - model: AllDeepSets
    model_plain: AllDeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9127
    metric_stds:
    - 0.0027
  - model: HGNN
    model_plain: HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9120999999999999
    metric_stds:
    - 0.0037
  - model: HCHA
    model_plain: HCHA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9092
    metric_stds:
    - 0.0022
  - model: HyperGCN
    model_plain: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8998
    metric_stds:
    - 0.0043
  - model: HNHN
    model_plain: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8678
    metric_stds:
    - 0.0029
  milestones:
  - value: 0.9198000000000001
    std: 0.0031
    model: HealHGNN
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: 2026-03
---

