---
title: SAT Solving
slug: sat-solving
benchmark: GraphBench
task_type: node_classification
description: 'SAT problem instances represented as graphs. Multi-level node/edge/graph-level
  tasks across 11 solvers and 3 instance-size scales.

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 208788
  avg_nodes: 10400.5
  avg_edges: 2054969.0
  num_classes: null
result_count: 5
best_model:
  model: Pairwise Regression
  value: 0.54
  metric: Gap Closed
  arxiv_id: '2512.04475'
  paper_title: GraphBench
variants:
- slug: standard-split
  name: Standard split
  notes: 208,788 graphs, 3 scales. Node/edge/graph-level tasks.
  is_standard: true
  primary_metric: Gap Closed
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Gap Closed
  - RMSE
  rows:
  - model: Pairwise Regression
    model_plain: Pairwise Regression
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.54
    - null
    metric_stds:
    - 0.02
    - null
  - model: Pairwise Classification
    model_plain: Pairwise Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.33
    - null
    metric_stds:
    - 0.01
    - null
  - model: Multi-class Classification
    model_plain: Multi-class Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.23
    - null
    metric_stds:
    - 0.02
    - null
  - model: Random Forest
    model_plain: Random Forest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.58
    metric_stds:
    - null
    - 0.0
  - model: XGBoost
    model_plain: XGBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.63
    metric_stds:
    - null
    - 0.0
  milestones:
  - value: 0.54
    std: 0.02
    model: Pairwise Regression
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
- slug: large
  name: Large
  notes: SAT solving performance prediction on large-scale instances.
  is_standard: false
  primary_metric: RMSE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - RMSE
  - Gap Closed
  rows:
  - model: Random Forest
    model_plain: Random Forest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.58
    - null
    metric_stds:
    - 0.0
    - null
  - model: XGBoost
    model_plain: XGBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.63
    - null
    metric_stds:
    - 0.0
    - null
  - model: UniMol
    model_plain: UniMol
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    metric_stds:
    - null
    - null
  - model: FPGNN
    model_plain: FPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.747
    - null
    metric_stds:
    - null
    - null
  - model: MPG
    model_plain: MPG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    metric_stds:
    - null
    - null
  - model: KANO
    model_plain: KANO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.772
    - null
    metric_stds:
    - null
    - null
  - model: DTNN*
    model_plain: DTNN*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    metric_stds:
    - null
    - null
  - model: XGBoost
    model_plain: XGBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.832
    - null
    metric_stds:
    - null
    - null
  - model: Trans-M
    model_plain: Trans-M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    metric_stds:
    - null
    - null
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    metric_stds:
    - null
    - null
  - model: FragFormer
    model_plain: FragFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.895
    - null
    metric_stds:
    - null
    - null
  - model: rf
    model_plain: rf
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.918
    - null
    metric_stds:
    - null
    - null
  - model: PharmHGT
    model_plain: PharmHGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.954
    - null
    metric_stds:
    - null
    - null
  - model: BiScale-GTR (Molecule)
    model_plain: BiScale-GTR (Molecule)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.977
    - null
    metric_stds:
    - null
    - null
  - model: KP-GPT
    model_plain: KP-GPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.221
    - null
    metric_stds:
    - null
    - null
  - model: FraGAT
    model_plain: FraGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.352
    - null
    metric_stds:
    - null
    - null
  - model: GraphFP
    model_plain: GraphFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.935
    - null
    metric_stds:
    - null
    - null
  - model: Pairwise Regression
    model_plain: Pairwise Regression
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.54
    metric_stds:
    - null
    - 0.02
  - model: Pairwise Classification
    model_plain: Pairwise Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.33
    metric_stds:
    - null
    - 0.01
  - model: Multi-class Classification
    model_plain: Multi-class Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.23
    metric_stds:
    - null
    - 0.02
  milestones:
  - value: 0.58
    std: null
    model: Random Forest
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
- slug: medium
  name: Medium
  notes: SAT solving performance prediction on medium-scale instances.
  is_standard: false
  primary_metric: Gap Closed
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Gap Closed
  - RMSE
  rows:
  - model: Pairwise Regression
    model_plain: Pairwise Regression
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.44
    - null
    metric_stds:
    - 0.02
    - null
  - model: Pairwise Classification
    model_plain: Pairwise Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.13
    - null
    metric_stds:
    - 0.02
    - null
  - model: Multi-class Classification
    model_plain: Multi-class Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - -0.13
    - null
    metric_stds:
    - 0.02
    - null
  - model: Random Forest
    model_plain: Random Forest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.59
    metric_stds:
    - null
    - 0.0
  - model: XGBoost
    model_plain: XGBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.62
    metric_stds:
    - null
    - 0.0
  milestones:
  - value: 0.44
    std: 0.02
    model: Pairwise Regression
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
- slug: small
  name: Small
  notes: SAT solving performance prediction on small instances.
  is_standard: false
  primary_metric: MRR
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MRR
  - Gap Closed
  - RMSE
  rows:
  - model: CEN
    model_plain: CEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.612
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: RecB_train
    model_plain: RecB_train
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.605
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TLogic
    model_plain: TLogic
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.595
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: RE-GCN
    model_plain: RE-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.594
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: RecB_default
    model_plain: RecB_default
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.486
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: EdgeBank_tw
    model_plain: EdgeBank_tw
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.353
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: EdgeBank_inf
    model_plain: EdgeBank_inf
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.333
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Random Forest
    model_plain: Random Forest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.61
    metric_stds:
    - null
    - null
    - 0.0
  - model: XGBoost
    model_plain: XGBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.63
    metric_stds:
    - null
    - null
    - 0.0
  - model: Pairwise Regression
    model_plain: Pairwise Regression
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.48
    - null
    metric_stds:
    - null
    - 0.03
    - null
  - model: Pairwise Classification
    model_plain: Pairwise Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.03
    - null
    metric_stds:
    - null
    - 0.02
    - null
  - model: Multi-class Classification
    model_plain: Multi-class Classification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - -0.32
    - null
    metric_stds:
    - null
    - 0.02
    - null
  milestones:
  - value: 0.612
    std: 0.001
    model: CEN
    arxiv_id: '2406.09639'
    title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
      Graphs'
    date: 2024-06
---

