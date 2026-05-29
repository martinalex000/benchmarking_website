---
title: Flow
slug: flow
benchmark: GraphBench
task_type: graph_regression
description: Network flow value prediction (GraphBench / CLRS-style algorithmic reasoning).
primary_metric: MAE
higher_is_better: false
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 3
best_model:
  model: agg + I
  value: 1.83
  metric: MAE
  arxiv_id: '2605.06462'
  paper_title: Invariant-Based Diagnostics for Graph Benchmarks
variants:
- slug: easy
  name: Easy
  notes: Small graph instances.
  is_standard: false
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
  - model: agg + I
    model_plain: agg + I
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
    is_best: true
    metric_values:
    - 1.83
    metric_stds:
    - 0.01
  - model: GIN
    model_plain: GIN
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
    - 3.44
    metric_stds:
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
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
    - 4.27
    metric_stds:
    - null
  milestones:
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
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  - AUC
  - Accuracy
  rows:
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.062
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: SphereNet
    model_plain: SphereNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.065
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.068
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.071
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.079
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: RRWP
    model_plain: RRWP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.45
    - null
    - null
    metric_stds:
    - 0.06
    - null
    - null
  - model: RWSE
    model_plain: RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.49
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: NoPE
    model_plain: NoPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.73
    - null
    - null
    metric_stds:
    - 0.09
    - null
    - null
  - model: LPE
    model_plain: LPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.75
    - null
    - null
    metric_stds:
    - 0.12
    - null
    - null
  - model: SPE
    model_plain: SPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 1.98
    - null
    - null
    metric_stds:
    - 0.14
    - null
    - null
  - model: agg + I
    model_plain: agg + I
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
    - 5.26
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
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
    - 6.48
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 9.51
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Base
    model_plain: Base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.74
    metric_stds:
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.71
    metric_stds:
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.744
    metric_stds:
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.715
    metric_stds:
    - null
    - null
    - null
  - model: LLaMA2 w/. CoT
    model_plain: LLaMA2 w/. CoT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08785'
    title: 'InstructGraph: Boosting Large Language Models via Graph-centric Instruction
      Tuning and Preference Alignment'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/wjn1996/InstructGraph
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
  - model: Vicuna w/. CoT
    model_plain: Vicuna w/. CoT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08785'
    title: 'InstructGraph: Boosting Large Language Models via Graph-centric Instruction
      Tuning and Preference Alignment'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/wjn1996/InstructGraph
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
  - model: LLMs through graph neural networks-INS w/. CoT
    model_plain: LLMs through graph neural networks-INS w/. CoT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08785'
    title: 'InstructGraph: Boosting Large Language Models via Graph-centric Instruction
      Tuning and Preference Alignment'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/wjn1996/InstructGraph
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.5
    metric_stds:
    - null
    - null
    - null
  - model: LLaMA2 w/. GTM
    model_plain: LLaMA2 w/. GTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08785'
    title: 'InstructGraph: Boosting Large Language Models via Graph-centric Instruction
      Tuning and Preference Alignment'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/wjn1996/InstructGraph
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
  - model: Vicuna w/. GTM
    model_plain: Vicuna w/. GTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08785'
    title: 'InstructGraph: Boosting Large Language Models via Graph-centric Instruction
      Tuning and Preference Alignment'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/wjn1996/InstructGraph
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.625
    - null
    metric_stds:
    - null
    - 0.041
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6879
    - null
    metric_stds:
    - null
    - 0.031
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6935
    - null
    metric_stds:
    - null
    - 0.025
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6696
    - null
    metric_stds:
    - null
    - 0.048
    - null
  - model: Graph Infomax
    model_plain: Graph Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.673
    - null
    metric_stds:
    - null
    - 0.066
    - null
  - model: CTDNE
    model_plain: CTDNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7432
    - null
    metric_stds:
    - null
    - 0.0064
    - null
  - model: HTNE
    model_plain: HTNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7493
    - null
    metric_stds:
    - null
    - 0.0039
    - null
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.891
    - null
    metric_stds:
    - null
    - 0.0098
    - null
  - model: DGNN_npt
    model_plain: DGNN_npt
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.12380'
    title: Pre-Training on Dynamic Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/Mobzhang/PT-DGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9196
    - null
    metric_stds:
    - null
    - 0.0107
    - null
  milestones:
  - value: 0.062
    std: 0.001
    model: Graphormer
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
- slug: medium
  name: Medium
  notes: Medium-scale graph instances.
  is_standard: false
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  - Accuracy
  rows:
  - model: agg + I
    model_plain: agg + I
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
    is_best: true
    metric_values:
    - 5.3
    - null
    metric_stds:
    - 0.12
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
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
    - 6.38
    - null
    metric_stds:
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 9.6
    - null
    metric_stds:
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7063
    metric_stds:
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7035
    metric_stds:
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13522'
    title: 'IGB: Addressing The Gaps In Labeling, Features, Heterogeneity, and Size
      of Public Graph Datasets for Deep Learning Research'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/IllinoisGraphBenchmark/IGB-Datasets
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7006
    metric_stds:
    - null
    - null
  milestones:
  - value: 5.3
    std: 0.12
    model: agg + I
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: 2026-05
---

