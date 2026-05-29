---
title: Film
slug: film
benchmark: Heterophilic Graphs
task_type: node_classification
description: Film (Actor) co-occurrence node classification (5 classes). Same graph
  as Actor; referred to as "Film" in some papers.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Actor.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 5
result_count: 28
best_model:
  model: DoG (ACM-GCN)
  value: 0.432
  metric: Accuracy
  arxiv_id: '2503.12563'
  paper_title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
variants:
- slug: standard-split
  name: Standard split
  notes: Geom-GCN 10 fixed splits.
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
  - model: DoG (ACM-GCN)
    model_plain: DoG (ACM-GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.432
    metric_stds:
    - 0.012
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.416
    metric_stds:
    - 0.011
  - model: CSNN
    model_plain: CSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3803
    metric_stds:
    - 0.011200000000000002
  - model: O(d)-NSD
    model_plain: O(d)-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.37810000000000005
    metric_stds:
    - 0.0115
  - model: Gen-NSD
    model_plain: Gen-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.37799999999999995
    metric_stds:
    - 0.012199999999999999
  - model: Diag-NSD
    model_plain: Diag-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3779
    metric_stds:
    - 0.0101
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3759
    metric_stds:
    - 0.0106
  - model: PDE-Log
    model_plain: PDE-Log
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3755
    metric_stds:
    - 0.008
  - model: GGCN
    model_plain: GGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3754
    metric_stds:
    - 0.015600000000000001
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.37439999999999996
    metric_stds:
    - 0.013000000000000001
  - model: PDE-Expn
    model_plain: PDE-Expn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3737
    metric_stds:
    - 0.0117
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3735
    metric_stds:
    - 0.013000000000000001
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3653
    metric_stds:
    - 0.006999999999999999
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3628
    metric_stds:
    - 0.0109
  - model: CO-GNN
    model_plain: CO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3626
    metric_stds:
    - 0.0374
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3595
    metric_stds:
    - 0.0086
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35700000000000004
    metric_stds:
    - 0.01
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3562
    metric_stds:
    - 0.0101
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35619999999999996
    metric_stds:
    - 0.0087
  - model: GRAFF
    model_plain: GRAFF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3555
    metric_stds:
    - 0.012
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.34869999999999995
    metric_stds:
    - 0.0125
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.34630000000000005
    metric_stds:
    - 0.012199999999999999
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3423
    metric_stds:
    - 0.0099
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3222
    metric_stds:
    - 0.023399999999999997
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3159
    metric_stds:
    - 0.0115
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2744
    metric_stds:
    - 0.0089
  - model: PairNorm
    model_plain: PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.274
    metric_stds:
    - 0.0124
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2732
    metric_stds:
    - 0.011
  milestones:
  - value: 0.3759
    std: 0.0106
    model: GRED
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: 2024-02
  - value: 0.432
    std: 0.012
    model: DoG (ACM-GCN)
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: 2025-03
---

