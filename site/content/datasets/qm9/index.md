---
title: QM9
slug: qm9
benchmark: Quantum Chemistry
task_type: graph_regression
description: Multi-target quantum property regression on 130k drug-like organic molecules
  (19 targets).
primary_metric: MAE
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.QM9.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 19
result_count: 38
best_model:
  model: ILLS
  value: 0.025
  metric: MAE
  arxiv_id: '2305.17589'
  paper_title: Graph Inductive Biases in Transformers without Message Passing
variants:
- slug: standard-split
  name: Standard split
  notes: Usually evaluated per-target; results reported for individual properties.
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.025
    metric_stds:
    - 0.001
  - model: SphereNet
    model_plain: SphereNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.026
    metric_stds:
    - 0.001
  - model: PaiNN
    model_plain: PaiNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.028
    metric_stds:
    - 0.001
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.033
    metric_stds:
    - 0.001
  - model: EquiBind
    model_plain: EquiBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.045
    metric_stds:
    - 0.002
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.048
    metric_stds:
    - 0.002
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.051
    metric_stds:
    - 0.002
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0512
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.056
    metric_stds:
    - 0.003
  - model: WL
    model_plain: WL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0567
    metric_stds:
    - null
  - model: Deep LRP-1-3
    model_plain: Deep LRP-1-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0567
    metric_stds:
    - null
  - model: 123-gnn
    model_plain: 123-gnn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0657
    metric_stds:
    - null
  - model: DTNN
    model_plain: DTNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1014
    metric_stds:
    - null
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1108
    metric_stds:
    - null
  - model: Maron et al. (2019)
    model_plain: Maron et al. (2019)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/RPaolino/loopy
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.231
    metric_stds:
    - null
  - model: DTNN
    model_plain: DTNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.244
    metric_stds:
    - null
  - model: Wu et al. (2018)
    model_plain: Wu et al. (2018)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/RPaolino/loopy
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.244
    metric_stds:
    - null
  - model: Zhou et al. (2023)
    model_plain: Zhou et al. (2023)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/RPaolino/loopy
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.346
    metric_stds:
    - null
  - model: 5-ℓGIN
    model_plain: 5-ℓGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/RPaolino/loopy
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    metric_stds:
    - 0.011
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.358
    metric_stds:
    - null
  - model: Deep LRP
    model_plain: Deep LRP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.364
    metric_stds:
    - null
  - model: Chen et al. (2020)
    model_plain: Chen et al. (2020)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/RPaolino/loopy
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.364
    metric_stds:
    - null
  - model: Zhang et al. (2021)
    model_plain: Zhang et al. (2021)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/RPaolino/loopy
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.428
    metric_stds:
    - null
  - model: Ne. 1-2-3-GNN
    model_plain: Ne. 1-2-3-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.433
    metric_stds:
    - null
  - model: Ne. 1-GNN
    model_plain: Ne. 1-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.436
    metric_stds:
    - null
  - model: 1-3-GNN
    model_plain: 1-3-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.473
    metric_stds:
    - null
  - model: 123-gnn
    model_plain: 123-gnn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.476
    metric_stds:
    - null
  - model: Morris et al. (2019)
    model_plain: Morris et al. (2019)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/RPaolino/loopy
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.476
    metric_stds:
    - null
  - model: 1-GNN
    model_plain: 1-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.493
    metric_stds:
    - null
  - model: 1-2-GNN
    model_plain: 1-2-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.13197'
    title: Nested Graph Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/muhanzhang/NestedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.493
    metric_stds:
    - null
  - model: XGBoost (agg_+_i)
    model_plain: XGBoost (agg_+_i)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5846
    metric_stds:
    - 0.0012
  - model: XGBoost (agg_+_subset)
    model_plain: XGBoost (agg_+_subset)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5961
    metric_stds:
    - 0.0012
  - model: XGBoost (feature_agg)
    model_plain: XGBoost (feature_agg)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6047
    metric_stds:
    - 0.0009
  - model: XGBoost (sum_+_i)
    model_plain: XGBoost (sum_+_i)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6509
    metric_stds:
    - 0.0002
  - model: XGBoost (sum_+_subset)
    model_plain: XGBoost (sum_+_subset)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6948
    metric_stds:
    - 0.0
  - model: XGBoost (feature_sum)
    model_plain: XGBoost (feature_sum)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7634
    metric_stds:
    - 0.0006
  - model: XGBoost (all_invariants)
    model_plain: XGBoost (all_invariants)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    metric_stds:
    - 0.0001
  - model: XGBoost (invariants_subset)
    model_plain: XGBoost (invariants_subset)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8919
    metric_stds:
    - 0.0003
  milestones:
  - value: 0.0512
    std: null
    model: PPGN
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: 2020-02
  - value: 0.025
    std: 0.001
    model: ILLS
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: '2023-05-27'
---

