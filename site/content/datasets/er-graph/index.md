---
title: ER graph
slug: er-graph
benchmark: GraphBench
task_type: graph_classification
description: Node classification on Erdős–Rényi random graphs (GraphBench algorithmic
  reasoning).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 35
best_model:
  model: 1-WL_F
  value: 1.0
  metric: Accuracy
  arxiv_id: '2402.07568'
  paper_title: '--Leman at the margin: When more expressivity matters'
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
  - AUROC
  - F1
  - MAE
  - RMSE
  rows:
  - model: 1-WL_F
    model_plain: 1-WL_F
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
  - model: 1-WLOA_F
    model_plain: 1-WLOA_F
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.986
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
  - model: RoGN
    model_plain: RoGN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.935
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.921
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.915
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.91
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.905
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.892
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.891
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
  - model: 1-WL
    model_plain: 1-WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.886
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.885
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
  - model: 1-WLOA
    model_plain: 1-WLOA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.879
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.873
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.869
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.852
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.11533'
    title: Accurate Learning of Graph Representations with Graph Multiset Pooling
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/JinheonBaek/GMT
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0331
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.11533'
    title: Accurate Learning of Graph Representations with Graph Multiset Pooling
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/JinheonBaek/GMT
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0324
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.141
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.003
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.135
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.006
    - null
    - null
  - model: InfWalk
    model_plain: InfWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.141
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.004
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.154
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.002
    - null
    - null
  - model: DGLFRM
    model_plain: DGLFRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.143
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.002
    - null
    - null
  - model: DW+Dine
    model_plain: DW+Dine
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.327
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.008
    - null
    - null
  - model: GAE+Dine
    model_plain: GAE+Dine
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.797
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.009
    - null
    - null
  - model: DiSe-FCAE
    model_plain: DiSe-FCAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.21043'
    title: Disentangled and Self-Explainable Node Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/simonepiaggesi/disene
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.791
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.012
    - null
    - null
  - model: FairGCN
    model_plain: FairGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.13186'
    title: Towards a Unified Framework for Fair and Stable Graph Representation Learning
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7269
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0123
    - null
    - null
    - null
  - model: RobustGCN
    model_plain: RobustGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.13186'
    title: Towards a Unified Framework for Fair and Stable Graph Representation Learning
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7298
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0026
    - null
    - null
    - null
  - model: GRL-GCN
    model_plain: GRL-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.13186'
    title: Towards a Unified Framework for Fair and Stable Graph Representation Learning
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7192
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0019
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.07620'
    title: 'EdgeNets: !Edge Varying Graph Neural Networks'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: http://github.com/alelab-upenn/graph-neural-networks
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.89
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: ArmaNet
    model_plain: ArmaNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.07620'
    title: 'EdgeNets: !Edge Varying Graph Neural Networks'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: http://github.com/alelab-upenn/graph-neural-networks
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.07620'
    title: 'EdgeNets: !Edge Varying Graph Neural Networks'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: http://github.com/alelab-upenn/graph-neural-networks
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 1.03
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  - model: GCat
    model_plain: GCat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.07620'
    title: 'EdgeNets: !Edge Varying Graph Neural Networks'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: http://github.com/alelab-upenn/graph-neural-networks
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.87
    metric_stds:
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.891
    std: 0.009
    model: MGNN
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: 2020-06
  - value: 1.0
    std: null
    model: 1-WL_F
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: 2024-02
---

