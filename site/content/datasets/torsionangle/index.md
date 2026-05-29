---
title: TorsionAngle
slug: torsionangle
benchmark: DualEquiNet RNA Benchmarks
task_type: graph_regression
description: RNA backbone torsion angle prediction (circular regression task, Circular
  MAE metric).
primary_metric: Circular MAE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 1018
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 25
best_model:
  model: DualEquiNet
  value: 15.87
  metric: Circular MAE
  arxiv_id: '2506.19862'
  paper_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large
    Biomolecules'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Circular MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Circular MAE
  - Accuracy
  - Fidelity
  rows:
  - model: DualEquiNet
    model_plain: DualEquiNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 15.87
    - null
    - null
    metric_stds:
    - 2.03
    - null
    - null
  - model: GotenNet
    model_plain: GotenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 16.27
    - null
    - null
    metric_stds:
    - 1.19
    - null
    - null
  - model: GVPGNN
    model_plain: GVPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 17.56
    - null
    - null
    metric_stds:
    - 0.21
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 18.41
    - null
    - null
    metric_stds:
    - 0.22
    - null
    - null
  - model: SchNet
    model_plain: SchNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 18.54
    - null
    - null
    metric_stds:
    - 0.86
    - null
    - null
  - model: FastEGNN
    model_plain: FastEGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 18.89
    - null
    - null
    metric_stds:
    - 0.22
    - null
    - null
  - model: TFN
    model_plain: TFN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 21.97
    - null
    - null
    metric_stds:
    - 0.45
    - null
    - null
  - model: GNN
    model_plain: GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.52
    - null
    metric_stds:
    - null
    - 0.15
    - null
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 1.0
    - null
    metric_stds:
    - null
    - 0.02
    - null
  - model: SMP
    model_plain: SMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.97
    - null
    metric_stds:
    - null
    - 0.11
    - null
  - model: DropGNN
    model_plain: DropGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.93
    - null
    metric_stds:
    - null
    - 0.13
    - null
  - model: ESAN*
    model_plain: ESAN*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 1.0
    - null
    metric_stds:
    - null
    - 0.01
    - null
  - model: AMP
    model_plain: AMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 1.0
    - null
    metric_stds:
    - null
    - 0.01
    - null
  - model: No augmentation
    model_plain: No augmentation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.506
    - null
    metric_stds:
    - null
    - 0.006
    - null
  - model: Uniform MaskNF
    model_plain: Uniform MaskNF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.509
    - null
    metric_stds:
    - null
    - 0.02
    - null
  - model: Uniform DropNode
    model_plain: Uniform DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.473
    - null
    metric_stds:
    - null
    - 0.006
    - null
  - model: Uniform PerturbEdge
    model_plain: Uniform PerturbEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.303
    - null
    metric_stds:
    - null
    - 0.01
    - null
  - model: Uniform Mixture
    model_plain: Uniform Mixture
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.467
    - null
    metric_stds:
    - null
    - 0.007
    - null
  - model: GraphAug
    model_plain: GraphAug
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.513
    - null
    metric_stds:
    - null
    - 0.006
    - null
  - model: MSA-Real
    model_plain: MSA-Real
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.347
    metric_stds:
    - null
    - null
    - null
  - model: JbDA
    model_plain: JbDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.559
    metric_stds:
    - null
    - null
    - null
  - model: T-RND
    model_plain: T-RND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.565
    metric_stds:
    - null
    - null
    - null
  - model: MSA-AU
    model_plain: MSA-AU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.632
    metric_stds:
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.475
    metric_stds:
    - null
    - null
    - null
  - model: MSA-AD
    model_plain: MSA-AD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.623
    metric_stds:
    - null
    - null
    - null
  milestones:
  - value: 15.87
    std: 2.03
    model: DualEquiNet
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: 2025-06
---

