---
title: Cora
slug: cora
benchmark: Classic
task_type: node_classification
description: Citation network node classification (7 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 7
result_count: 159
best_model:
  model: GPM
  value: 0.9285
  metric: Accuracy
  arxiv_id: '2501.18739'
  paper_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
variants:
- slug: random-10-fold
  name: Random 10-fold
  notes: 10-fold cross-validation; results not directly comparable to Planetoid.
  is_standard: false
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - F1
  rows:
  - model: GPM
    model_plain: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.9285
    - null
    metric_stds:
    - 0.0054
    - null
  - model: TRIGON
    model_plain: TRIGON
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9171
    - null
    metric_stds:
    - 0.0029
    - null
  - model: DR
    model_plain: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9139
    - null
    metric_stds:
    - 0.0024
    - null
  - model: Flan-T5-base
    model_plain: Flan-T5-base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9077
    - null
    metric_stds:
    - 0.0052
    - null
  - model: LLP
    model_plain: LLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8995
    - null
    metric_stds:
    - 0.0201
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8975
    - null
    metric_stds:
    - 0.0116
    - null
  - model: Snowball-V3
    model_plain: Snowball-V3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8959
    - null
    metric_stds:
    - 0.0158
    - null
  - model: RvGAT
    model_plain: RvGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8911
    - null
    metric_stds:
    - 0.0
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8893
    - null
    metric_stds:
    - 0.0137
    - null
  - model: Flan-T5-large
    model_plain: Flan-T5-large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8893
    - null
    metric_stds:
    - 0.0106
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8886
    - null
    metric_stds:
    - 0.0142
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8885
    - null
    metric_stds:
    - 0.0136
    - null
  - model: ALT
    model_plain: ALT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8882
    - null
    metric_stds:
    - 0.0202
    - null
  - model: RUM
    model_plain: RUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8874
    - null
    metric_stds:
    - 0.006
    - null
  - model: novel all-pair message passing scheme
    model_plain: novel all-pair message passing scheme
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08385'
    title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for
      Graph Neural Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/NodeFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8869
    - null
    metric_stds:
    - 0.0046
    - null
  - model: CoarFormer
    model_plain: CoarFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8869
    - null
    metric_stds:
    - 0.0082
    - null
  - model: ACM-GNN
    model_plain: ACM-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8858
    - null
    metric_stds:
    - 0.019
    - null
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8852
    - null
    metric_stds:
    - 0.0095
    - null
  - model: TAGCN
    model_plain: TAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8838
    - null
    metric_stds:
    - 0.0195
    - null
  - model: DIGL
    model_plain: DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8831
    - null
    metric_stds:
    - 0.0029
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8831
    - null
    metric_stds:
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8827
    - null
    metric_stds:
    - 0.0153
    - null
  - model: GRAPHITE
    model_plain: GRAPHITE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8823
    - null
    metric_stds:
    - 0.0165
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8805
    - null
    metric_stds:
    - 0.0208
    - null
  - model: FOSR
    model_plain: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8794
    - null
    metric_stds:
    - 0.0026
    - null
  - model: GTR
    model_plain: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8786
    - null
    metric_stds:
    - 0.0028
    - null
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8781
    - null
    metric_stds:
    - 0.0196
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8778
    - null
    metric_stds:
    - 0.0096
    - null
  - model: Base (GCN)
    model_plain: Base (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8773
    - null
    metric_stds:
    - 0.0025
    - null
  - model: SRDF
    model_plain: SRDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8773
    - null
    metric_stds:
    - 0.0031
    - null
  - model: BORF
    model_plain: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8772
    - null
    metric_stds:
    - 0.0027
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8766
    - null
    metric_stds:
    - 0.0152
    - null
  - model: Base (GAT)
    model_plain: Base (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8765
    - null
    metric_stds:
    - 0.0024
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8759
    - null
    metric_stds:
    - 0.0168
    - null
  - model: JDR
    model_plain: JDR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8754
    - null
    metric_stds:
    - 0.0025
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8744
    - null
    metric_stds:
    - 0.0137
    - null
  - model: Virtual Node
    model_plain: Virtual Node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8724
    - null
    metric_stds:
    - 0.02
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8724
    - null
    metric_stds:
    - 0.0071
    - null
  - model: Llama-7b
    model_plain: Llama-7b
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8708
    - null
    metric_stds:
    - 0.0032
    - null
  - model: GCN + FoSR
    model_plain: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8690000000000001
    - null
    metric_stds:
    - 0.02
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8687
    - null
    metric_stds:
    - 0.0158
    - null
  - model: GCN + None
    model_plain: GCN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    metric_stds:
    - 0.008
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8658
    - null
    metric_stds:
    - 0.0026
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8642
    - null
    metric_stds:
    - 0.0082
    - null
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8640000000000001
    - null
    metric_stds:
    - 0.021
    - null
  - model: GGCN
    model_plain: GGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8639
    - null
    metric_stds:
    - 0.0193
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8624
    - null
    metric_stds:
    - 0.0085
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8624
    - null
    metric_stds:
    - 0.0158
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    metric_stds:
    - 0.0051
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8565
    - null
    metric_stds:
    - 0.0226
    - null
  - model: SGC-v2
    model_plain: SGC-v2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8548
    - null
    metric_stds:
    - 0.0148
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8527
    - null
    metric_stds:
    - 0.0148
    - null
  - model: DAG + DIFFORMER-a
    model_plain: DAG + DIFFORMER-a
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    metric_stds:
    - 0.007
    - null
  - model: OrderedGNN
    model_plain: OrderedGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8481
    - null
    metric_stds:
    - 0.0167
    - null
  - model: BLEND
    model_plain: BLEND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.848
    - null
    metric_stds:
    - 0.009
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8453
    - null
    metric_stds:
    - 0.0153
    - null
  - model: g-U-Nets
    model_plain: g-U-Nets
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: May 11, 2019
    date_iso: '2019-05-11'
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.844
    - null
    metric_stds:
    - 0.006
    - null
  - model: Graph-Bert
    model_plain: Graph-Bert
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.05140'
    title: 'Graph-Bert: Only Attention is Needed for Learning Graph Representations'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/jwzhanggy/Graph-Bert
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.843
    - null
    metric_stds:
    - null
    - null
  - model: ILSS
    model_plain: ILSS
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
    - 0.842
    - null
    metric_stds:
    - 0.003
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.841
    - null
    metric_stds:
    - 0.005
    - null
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.841
    - null
    metric_stds:
    - 0.006
    - null
  - model: GCDE-rk2
    model_plain: GCDE-rk2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07532'
    title: Graph Neural Ordinary Differential Equations
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.838
    - null
    metric_stds:
    - 0.005
    - null
  - model: GraphHeat
    model_plain: GraphHeat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    - null
    metric_stds:
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    - null
    metric_stds:
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8364
    - null
    metric_stds:
    - null
    - null
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
    - 0.835
    - null
    metric_stds:
    - 0.004
    - null
  - model: CNNs
    model_plain: CNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    metric_stds:
    - 0.012
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    metric_stds:
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    metric_stds:
    - 0.002
    - null
  - model: LGCN
    model_plain: LGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    - null
    metric_stds:
    - 0.005
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    - null
    metric_stds:
    - 0.013
    - null
  - model: GraphSGAN
    model_plain: GraphSGAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    - null
    metric_stds:
    - 0.013
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8285
    - null
    metric_stds:
    - 0.0244
    - null
  - model: GWNN
    model_plain: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    metric_stds:
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    metric_stds:
    - 0.006
    - null
  - model: LoopyNet
    model_plain: LoopyNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.05140'
    title: 'Graph-Bert: Only Attention is Needed for Learning Graph Representations'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/jwzhanggy/Graph-Bert
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.826
    - null
    metric_stds:
    - null
    - null
  - model: BLEND-kNN
    model_plain: BLEND-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    metric_stds:
    - 0.009
    - null
  - model: MLP for adjacency matrix only
    model_plain: MLP for adjacency matrix only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8249
    - null
    metric_stds:
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    - null
    metric_stds:
    - 0.006
    - null
  - model: StochasticGCN
    model_plain: StochasticGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    metric_stds:
    - 0.008
    - null
  - model: CayleyNets
    model_plain: CayleyNets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    metric_stds:
    - 0.007
    - null
  - model: GCDE-dpr5
    model_plain: GCDE-dpr5
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07532'
    title: Graph Neural Ordinary Differential Equations
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    - null
    metric_stds:
    - 0.012
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8169
    - null
    metric_stds:
    - 0.0048
    - null
  - model: GAT-ppr
    model_plain: GAT-ppr
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    metric_stds:
    - 0.003
    - null
  - model: Renormalization trick
    model_plain: Renormalization trick
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
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
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    metric_stds:
    - 0.015
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    metric_stds:
    - 0.014
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.814
    - null
    metric_stds:
    - 0.016
    - null
  - model: Chebyshev filter (K=3)
    model_plain: Chebyshev filter (K=3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    metric_stds:
    - null
    - null
  - model: Chebyshev
    model_plain: Chebyshev
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: May 11, 2019
    date_iso: '2019-05-11'
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    metric_stds:
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    - null
    metric_stds:
    - 0.016
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    - null
    metric_stds:
    - 0.0
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8078
    - null
    metric_stds:
    - 0.0144
    - null
  - model: 1st-order term only
    model_plain: 1st-order term only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    metric_stds:
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    metric_stds:
    - 0.017
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8041
    - null
    metric_stds:
    - 0.003
    - null
  - model: GCN (rand. splits)
    model_plain: GCN (rand. splits)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    metric_stds:
    - 0.005
    - null
  - model: 1st-order model
    model_plain: 1st-order model
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
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
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    metric_stds:
    - 0.006999999999999999
    - null
  - model: Single parameter
    model_plain: Single parameter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    metric_stds:
    - null
    - null
  - model: GS-mean
    model_plain: GS-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    metric_stds:
    - 0.077
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7913
    - null
    metric_stds:
    - 0.0052
    - null
  - model: GDE
    model_plain: GDE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    metric_stds:
    - 0.022
    - null
  - model: HopFormer
    model_plain: HopFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    metric_stds:
    - 0.0125
    - null
  - model: GCN + BORF
    model_plain: GCN + BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    - null
    metric_stds:
    - 0.004
    - null
  - model: GIN + AFR-3
    model_plain: GIN + AFR-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7829999999999999
    - null
    metric_stds:
    - 0.006
    - null
  - model: GCN + AFR-4
    model_plain: GCN + AFR-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7809999999999999
    - null
    metric_stds:
    - 0.012
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    metric_stds:
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7713
    - null
    metric_stds:
    - 0.0101
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7703
    - null
    metric_stds:
    - 0.0021
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7689
    - null
    metric_stds:
    - 0.0225
    - null
  - model: UnionSNN
    model_plain: UnionSNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7686
    - null
    metric_stds:
    - 0.0158
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    metric_stds:
    - 0.006
    - null
  - model: GS-maxpool
    model_plain: GS-maxpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.766
    - null
    metric_stds:
    - 0.019
    - null
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    metric_stds:
    - 0.0099
    - null
  - model: R-GIN + None
    model_plain: R-GIN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.763
    - null
    metric_stds:
    - 0.006
    - null
  - model: UnionGCN
    model_plain: UnionGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    metric_stds:
    - 0.008
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7586
    - null
    metric_stds:
    - 0.0109
    - null
  - model: R-GIN + FoSR
    model_plain: R-GIN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    metric_stds:
    - 0.009000000000000001
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    metric_stds:
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7565
    - null
    metric_stds:
    - 0.0131
    - null
  - model: UnionGraphSNN
    model_plain: UnionGraphSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7558
    - null
    metric_stds:
    - 0.0049
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7545
    - null
    metric_stds:
    - 0.0188
    - null
  - model: GraphSNN
    model_plain: GraphSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7544
    - null
    metric_stds:
    - 0.0073
    - null
  - model: DeGTA
    model_plain: DeGTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7533
    - null
    metric_stds:
    - 0.0056
    - null
  - model: ICA
    model_plain: ICA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.751
    - null
    metric_stds:
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7482
    - null
    metric_stds:
    - 0.0195
    - null
  - model: R-GIN + SDRF
    model_plain: R-GIN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    metric_stds:
    - 0.003
    - null
  - model: CurvGN
    model_plain: CurvGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7406
    - null
    metric_stds:
    - 0.0154
    - null
  - model: Bruna et al.
    model_plain: Bruna et al.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    - null
    metric_stds:
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7302
    - null
    metric_stds:
    - 0.0298
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7256
    - null
    metric_stds:
    - 0.0441
    - null
  - model: CoBFormer
    model_plain: CoBFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7243
    - null
    metric_stds:
    - 0.0118
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.723
    - null
    metric_stds:
    - null
    - null
  - model: GeniePath
    model_plain: GeniePath
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7216
    - null
    metric_stds:
    - 0.0269
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    metric_stds:
    - 0.0051
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7103
    - null
    metric_stds:
    - 0.0175
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    - null
    metric_stds:
    - 0.0064
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    metric_stds:
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    - null
    metric_stds:
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.672
    - null
    metric_stds:
    - null
    - null
  - model: GraphEmb
    model_plain: GraphEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.672
    - null
    metric_stds:
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    - null
    metric_stds:
    - 0.0213
    - null
  - model: ManiReg
    model_plain: ManiReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.595
    - null
    metric_stds:
    - null
    - null
  - model: SemiEmb
    model_plain: SemiEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.59
    - null
    metric_stds:
    - null
    - null
  - model: TSVM
    model_plain: TSVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.575
    - null
    metric_stds:
    - null
    - null
  - model: Feat
    model_plain: Feat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.574
    - null
    metric_stds:
    - null
    - null
  - model: Multi-layer perceptron
    model_plain: Multi-layer perceptron
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.551
    - null
    metric_stds:
    - null
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5403
    - null
    metric_stds:
    - 0.054
    - null
  - model: SpecFormer
    model_plain: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4883
    - null
    metric_stds:
    - 0.0084
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4323
    - null
    metric_stds:
    - 0.0455
    - null
  - model: FA
    model_plain: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2986
    - null
    metric_stds:
    - 0.0028
    - null
  - model: DyGFormer
    model_plain: DyGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0845
    metric_stds:
    - null
    - 0.0013
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0529
    metric_stds:
    - null
    - 0.0047
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.066
    metric_stds:
    - null
    - 0.0011
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0633
    metric_stds:
    - null
    - 0.0041
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0539
    metric_stds:
    - null
    - 0.0019
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0604
    metric_stds:
    - null
    - 0.0027
  - model: DGNs
    model_plain: DGNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0789
    metric_stds:
    - null
    - 0.0033
  milestones:
  - value: 0.835
    std: 0.012
    model: CNNs
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: '2013-12-21'
  - value: 0.844
    std: 0.006
    model: g-U-Nets
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: '2019-05-11'
  - value: 0.848
    std: 0.009
    model: BLEND
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: 2021-10
  - value: 0.8831
    std: null
    model: GloGNN
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: '2022-05-15'
  - value: 0.8869
    std: 0.0046
    model: novel all-pair message passing scheme
    arxiv_id: '2306.08385'
    title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for
      Graph Neural Networks'
    date: 2023-06
  - value: 0.9077
    std: 0.0052
    model: Flan-T5-base
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: 2023-08
  - value: 0.9285
    std: 0.0054
    model: GPM
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
---

