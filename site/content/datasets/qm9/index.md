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
  num_graphs: 130831
  avg_nodes: 18.0
  avg_edges: 37.3
  num_classes: null
result_count: 54
best_model:
  model: Mace
  value: 0.02
  metric: MAE
variants:
- slug: standard-split
  name: Standard split
  notes: Usually evaluated per-target; results reported for individual properties.
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  - RMSE
  rows:
  - model: Mace
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.02
    - null
    metric_stds:
    - null
    - null
  - model: DropGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.02578744427174226
    - 0.16229444581483676
    metric_stds:
    - 0.000867405321348238
    - 0.0017203168654583633
  - model: ESA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.02578744427174226
    - 0.15244936051398003
    metric_stds:
    - 0.000867405321348238
    - 0.0029945876029935353
  - model: SchNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.026
    - null
    metric_stds:
    - 0.002
    - null
  - model: DimeNet++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.002
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.027
    - null
    metric_stds:
    - 0.002
    - null
  - model: TokenGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.030389001220464663
    - 0.20003333687782282
    metric_stds:
    - 0.0005953300476479862
    - 0.00828174606274421
  - model: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0317492975167588
    - 0.15115694898675025
    metric_stds:
    - 0.0028074830084290074
    - 0.0012178706316662376
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.03219783138040288
    - 0.15725115601797318
    metric_stds:
    - 0.0008736508385477724
    - 0.0023134325943648688
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.03290000183733416
    - 0.1594100643906536
    metric_stds:
    - 0.0014504048065470119
    - 0.00274523474824748
  - model: M3GNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.033
    - null
    metric_stds:
    - null
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.033075999999999994
    - 0.178406
    metric_stds:
    - 0.005936661014408688
    - 0.0020226477696326695
  - model: CGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.045
    - null
    metric_stds:
    - null
    - null
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.05862095989286895
    - 0.17889551252591157
    metric_stds:
    - 0.03095901400991143
    - 0.008689612096286428
  - model: BS-KAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0618
    - null
    metric_stds:
    - 0.0007
    - null
  - model: cf
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.07
    - null
    metric_stds:
    - 0.01
    - null
  - model: RBF-KAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0778
    - null
    metric_stds:
    - 0.0023
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0969
    - null
    metric_stds:
    - 0.0017
    - null
  - model: PST
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.23
    - null
    metric_stds:
    - 0.01
    - null
  - model: cg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.39
    - null
    metric_stds:
    - 0.05
    - null
  - model: XGBoost (agg_+_i)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5846
    - null
    metric_stds:
    - 0.0012
    - null
  - model: XGBoost (agg_+_subset)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5961
    - null
    metric_stds:
    - 0.0012
    - null
  - model: o
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    - null
    metric_stds:
    - 0.02
    - null
  - model: XGBoost (feature_agg)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6047
    - null
    metric_stds:
    - 0.0009
    - null
  - model: eg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    - null
    metric_stds:
    - 0.03
    - null
  - model: XGBoost (sum_+_i)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6509
    - null
    metric_stds:
    - 0.0002
    - null
  - model: XGBoost (sum_+_subset)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6948
    - null
    metric_stds:
    - 0.0
    - null
  - model: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.703
    - null
    metric_stds:
    - null
    - null
  - model: XGBoost (feature_sum)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7634
    - null
    metric_stds:
    - 0.0006
    - null
  - model: XGBoost (all_invariants)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    metric_stds:
    - 0.0001
    - null
  - model: XGBoost (invariants_subset)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8919
    - null
    metric_stds:
    - 0.0003
    - null
  - model: rg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.93
    - null
    metric_stds:
    - 0.01
    - null
  - model: Mole-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.031
    - null
    metric_stds:
    - null
    - null
  - model: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.035
    - null
    metric_stds:
    - null
    - null
  - model: SimSGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.064
    - null
    metric_stds:
    - null
    - null
  - model: rf
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.44
    - null
    metric_stds:
    - 0.02
    - null
  - model: Drew-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.93
    - null
    metric_stds:
    - 0.06
    - null
  - model: PR-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.99
    - null
    metric_stds:
    - 0.02
    - null
  - model: IPR-MPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.01
    - null
    metric_stds:
    - 0.01
    - null
  - model: PPGNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.31
    - null
    metric_stds:
    - null
    - null
  - model: SPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.32
    - null
    metric_stds:
    - 0.28
    - null
  - model: DTNN*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.44
    - null
    metric_stds:
    - null
    - null
  - model: R-GIN+FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.54
    - null
    metric_stds:
    - 0.09
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.64
    - null
    metric_stds:
    - 0.01
    - null
  - model: DF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 3.46
    - null
    metric_stds:
    - null
    - null
  - model: PSDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 3.53
    - null
    metric_stds:
    - 0.05
    - null
  - model: LRP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 3.64
    - null
    metric_stds:
    - null
    - null
  - model: NGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 4.28
    - null
    metric_stds:
    - null
    - null
  - model: IGNN*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 4.28
    - null
    metric_stds:
    - null
    - null
  - model: 123*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 4.76
    - null
    metric_stds:
    - null
    - null
  - model: 1-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 4.93
    - null
    metric_stds:
    - null
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.161956
    metric_stds:
    - null
    - 0.0015081326201631
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.17144381081131788
    metric_stds:
    - null
    - 0.003676356368918919
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.16187201431047754
    metric_stds:
    - null
    - 0.0016597907171188395
  - model: Grph.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.19038245203081353
    metric_stds:
    - null
    - 0.005813449852960949
  milestones:
  - value: 0.02578744427174226
    std: 0.000867405321348238
    model: DropGIN
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: 2024-02
  - value: 0.02
    std: null
    model: Mace
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: 2025-09
---

