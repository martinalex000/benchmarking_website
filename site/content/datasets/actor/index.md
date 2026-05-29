---
title: Actor
slug: actor
benchmark: Heterophilic Graphs
task_type: node_classification
description: Actor co-occurrence node classification (5 classes) from the Geom-GCN
  paper.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Actor.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 5
result_count: 301
best_model:
  model: Vicuna-7B
  value: 0.7682
  metric: Accuracy
  arxiv_id: '2408.14134'
  paper_title: Exploring the Potential of Large Language Models for Heterophilic Graphs
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
  - model: Vicuna-7B
    model_plain: Vicuna-7B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.7682
    metric_stds:
    - 0.005
  - model: Bloom 560M
    model_plain: Bloom 560M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.7616
    metric_stds:
    - 0.006
  - model: 7B-to-560M
    model_plain: 7B-to-560M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7578
    metric_stds:
    - 0.002
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7558
    metric_stds:
    - 0.005
  - model: 7B-to-1B
    model_plain: 7B-to-1B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7537
    metric_stds:
    - 0.009
  - model: Bloom 1B
    model_plain: Bloom 1B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7499
    metric_stds:
    - 0.005
  - model: Sage + DisamGCL
    model_plain: Sage + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    metric_stds:
    - 0.013
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7381
    metric_stds:
    - 0.003
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
    - 0.012
  - model: SEGSL
    model_plain: SEGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7273
    metric_stds:
    - 0.008
  - model: GBK-GNN
    model_plain: GBK-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7249
    metric_stds:
    - 0.01
  - model: OGNN
    model_plain: OGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7208
    metric_stds:
    - 0.024
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    metric_stds:
    - 0.016
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7073
    metric_stds:
    - 0.009
  - model: GCN + DisamGCL
    model_plain: GCN + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    metric_stds:
    - 0.015
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7037
    metric_stds:
    - 0.001
  - model: DisamGCL
    model_plain: DisamGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6778
    metric_stds:
    - 0.003
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.667
    metric_stds:
    - 0.019
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.667
    metric_stds:
    - 0.013
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6374
    metric_stds:
    - 0.067
  - model: DGI + DisamGCL
    model_plain: DGI + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.534
    metric_stds:
    - 0.016
  - model: SupCon + DisamGCL
    model_plain: SupCon + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.532
    metric_stds:
    - 0.016
  - model: CE + DisamGCL
    model_plain: CE + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.519
    metric_stds:
    - 0.011
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.519
    metric_stds:
    - 0.017
  - model: ReNode
    model_plain: ReNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.514
    metric_stds:
    - 0.018
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.513
    metric_stds:
    - 0.011
  - model: TopoImb
    model_plain: TopoImb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.513
    metric_stds:
    - 0.015
  - model: SupCon
    model_plain: SupCon
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.512
    metric_stds:
    - 0.025
  - model: Focal
    model_plain: Focal
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.509
    metric_stds:
    - 0.012
  - model: CE
    model_plain: CE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.508
    metric_stds:
    - 0.014
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.508
    metric_stds:
    - 0.014
  - model: SRGNN
    model_plain: SRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.505
    metric_stds:
    - 0.018
  - model: AdaptKry
    model_plain: AdaptKry
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.427
    metric_stds:
    - 0.0114
  - model: SpatUFG
    model_plain: SpatUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.425
    metric_stds:
    - 0.0019
  - model: FMLP-O
    model_plain: FMLP-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.425
    metric_stds:
    - 0.0011
  - model: GNN-HF
    model_plain: GNN-HF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4247
    metric_stds:
    - 0.0007
  - model: OptBasisGNN
    model_plain: OptBasisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4239
    metric_stds:
    - 0.0052
  - model: GNN-LF
    model_plain: GNN-LF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4197
    metric_stds:
    - 0.0006
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4175
    metric_stds:
    - 0.0107
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4171
    metric_stds:
    - 0.0112
  - model: Ada-Ugnn
    model_plain: Ada-Ugnn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4138
    metric_stds:
    - 0.0012
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4122
    metric_stds:
    - 0.0096
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4117
    metric_stds:
    - 0.0064
  - model: FE-GNN (M)
    model_plain: FE-GNN (M)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4091
    metric_stds:
    - 0.0022
  - model: FE-GNN (C)
    model_plain: FE-GNN (C)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4054
    metric_stds:
    - 0.0015
  - model: EvenNet
    model_plain: EvenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4036
    metric_stds:
    - 0.0065
  - model: SUFG
    model_plain: SUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.401
    metric_stds:
    - 0.002
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3991
    metric_stds:
    - 0.0062
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.399
    metric_stds:
    - 0.0025
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.393
    metric_stds:
    - 0.0027
  - model: CGP (GCN)
    model_plain: CGP (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3921
    metric_stds:
    - null
  - model: ESC-GNN
    model_plain: ESC-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.389
    metric_stds:
    - 0.008
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3886
    metric_stds:
    - 0.0024
  - model: CGP (APPNP)
    model_plain: CGP (APPNP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3882
    metric_stds:
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3861
    metric_stds:
    - 0.0026
  - model: WRGAT
    model_plain: WRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.386
    metric_stds:
    - 0.011
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3858
    metric_stds:
    - 0.0025
  - model: MUSE
    model_plain: MUSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3855
    metric_stds:
    - 0.0134
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.384
    metric_stds:
    - 0.01
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.382
    metric_stds:
    - 0.012
  - model: GCN-Cheby
    model_plain: GCN-Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3802
    metric_stds:
    - 0.0023
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.38
    metric_stds:
    - 0.011
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.379
    metric_stds:
    - 0.011
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.379
    metric_stds:
    - 0.01
  - model: GCN-LPA
    model_plain: GCN-LPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.378
    metric_stds:
    - 0.009
  - model: GLNN
    model_plain: GLNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.378
    metric_stds:
    - 0.0047
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
    - 0.3769
    metric_stds:
    - 0.0157
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3743
    metric_stds:
    - 0.0137
  - model: SpaM
    model_plain: SpaM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.374
    metric_stds:
    - 0.0066
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
    - 0.3736
    metric_stds:
    - 0.0016
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.373
    metric_stds:
    - 0.014
  - model: PathNet+DiSRW
    model_plain: PathNet+DiSRW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3714
    metric_stds:
    - 0.0087
  - model: SG-FBGNN_N
    model_plain: SG-FBGNN_N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3707
    metric_stds:
    - 0.0013
  - model: HGRL
    model_plain: HGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3697
    metric_stds:
    - 0.0098
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3693
    metric_stds:
    - 0.0026
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.369
    metric_stds:
    - 0.01
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3689
    metric_stds:
    - 0.003
  - model: N.S.-GCN
    model_plain: N.S.-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3676
    metric_stds:
    - 0.0016
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.367
    metric_stds:
    - 0.012
  - model: FMLP-S
    model_plain: FMLP-S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.367
    metric_stds:
    - 0.0112
  - model: PathNet
    model_plain: PathNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3667
    metric_stds:
    - 0.0092
  - model: UDGNN*_SAGE
    model_plain: UDGNN*_SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3664
    metric_stds:
    - 0.0118
  - model: MUSE
    model_plain: MUSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3661
    metric_stds:
    - 0.0015
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.366
    metric_stds:
    - 0.01
  - model: GREET
    model_plain: GREET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3655
    metric_stds:
    - 0.0101
  - model: WRGAT
    model_plain: WRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3653
    metric_stds:
    - 0.0077
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.365
    metric_stds:
    - 0.01
  - model: Logistic Reg.-X
    model_plain: Logistic Reg.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3645
    metric_stds:
    - 0.006
  - model: ASGC
    model_plain: ASGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3645
    metric_stds:
    - 0.0079
  - model: S-GCN
    model_plain: S-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3645
    metric_stds:
    - 0.0018
  - model: DiSRW
    model_plain: DiSRW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3642
    metric_stds:
    - 0.0046
  - model: GADPN(SAGE)
    model_plain: GADPN(SAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.08230'
    title: 'GADPN: Graph Adaptive Denoising and Perturbation Networks via Singular
      Value Decomposition'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.364
    metric_stds:
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3639
    metric_stds:
    - 0.0035
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3638
    metric_stds:
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3637
    metric_stds:
    - 0.0021
  - model: GOAL
    model_plain: GOAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.363
    metric_stds:
    - 0.01
  - model: Raw
    model_plain: Raw
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3628
    metric_stds:
    - 0.0077
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.362
    metric_stds:
    - 0.01
  - model: SG-GCN_L
    model_plain: SG-GCN_L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3614
    metric_stds:
    - 0.0019
  - model: UDGNN*_GAT
    model_plain: UDGNN*_GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3613
    metric_stds:
    - 0.0102
  - model: UDGNN_GCN
    model_plain: UDGNN_GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3613
    metric_stds:
    - 0.0121
  - model: CHEV
    model_plain: CHEV
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.36
    metric_stds:
    - 0.011
  - model: Shift-MLP
    model_plain: Shift-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.36
    metric_stds:
    - 0.004
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3598
    metric_stds:
    - 0.0023
  - model: ARMA (GDC)
    model_plain: ARMA (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.359
    metric_stds:
    - 0.005
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.359
    metric_stds:
    - 0.01
  - model: SANE-hete
    model_plain: SANE-hete
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3588
    metric_stds:
    - 0.013
  - model: H2GCN-1
    model_plain: H2GCN-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3586
    metric_stds:
    - 0.0103
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3585
    metric_stds:
    - 0.0105
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3576
    metric_stds:
    - 0.0098
  - model: simple GNN model (3-hop)
    model_plain: simple GNN model (3-hop)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3575
    metric_stds:
    - 0.0096
  - model: MGC
    model_plain: MGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3575
    metric_stds:
    - 0.0041
  - model: APPNP (GDC)
    model_plain: APPNP (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.357
    metric_stds:
    - 0.005
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
    - 0.3564
    metric_stds:
    - 0.0098
  - model: H2GCN-2
    model_plain: H2GCN-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3562
    metric_stds:
    - 0.013
  - model: FOSSIL
    model_plain: FOSSIL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3561
    metric_stds:
    - 0.0015
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
    - 0.356
    metric_stds:
    - 0.0134
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3558
    metric_stds:
    - 0.0125
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3557
    metric_stds:
    - 0.0108
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3556
    metric_stds:
    - 0.0017
  - model: RAWGNN+DiSRW
    model_plain: RAWGNN+DiSRW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3555
    metric_stds:
    - 0.0039
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3551
    metric_stds:
    - 0.011
  - model: NeuralSparse
    model_plain: NeuralSparse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.355
    metric_stds:
    - 0.011
  - model: FOSSIL v2
    model_plain: FOSSIL v2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3541
    metric_stds:
    - 0.0018
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3541
    metric_stds:
    - 0.0118
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
    - 0.3531
    metric_stds:
    - 0.0129
  - model: ADPA
    model_plain: ADPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3529
    metric_stds:
    - 0.0082
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3527
    metric_stds:
    - 0.0104
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.352
    metric_stds:
    - 0.007
  - model: Cheby+JK
    model_plain: Cheby+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3514
    metric_stds:
    - 0.0137
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.351
    metric_stds:
    - 0.006
  - model: Acc(MLP)
    model_plain: Acc(MLP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.09125'
    title: arXiv:2401.09125
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    metric_stds:
    - null
  - model: GCN+GDC
    model_plain: GCN+GDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    metric_stds:
    - 0.005
  - model: CHEV(GDC)
    model_plain: CHEV(GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    metric_stds:
    - 0.006
  - model: GAT (GDC)
    model_plain: GAT (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    metric_stds:
    - 0.006
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
    - 0.3492
    metric_stds:
    - 0.0119
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.349
    metric_stds:
    - 0.007
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3484
    metric_stds:
    - 0.0014
  - model: RAWGNN
    model_plain: RAWGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3471
    metric_stds:
    - 0.008
  - model: Shift-GCN
    model_plain: Shift-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.347
    metric_stds:
    - 0.006
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3464
    metric_stds:
    - 0.0151
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.345
    metric_stds:
    - 0.007
  - model: GPRGNN (GDC)
    model_plain: GPRGNN (GDC)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.344
    metric_stds:
    - 0.01
  - model: SGC (GDC)
    model_plain: SGC (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.343
    metric_stds:
    - 0.006
  - model: DiGCN
    model_plain: DiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.343
    metric_stds:
    - 0.0089
  - model: GLR
    model_plain: GLR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3427
    metric_stds:
    - 0.009
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3423
    metric_stds:
    - 0.0099
  - model: GCN-JKNet
    model_plain: GCN-JKNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3418
    metric_stds:
    - 0.0085
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
    - 0.3404
    metric_stds:
    - 0.0125
  - model: Local-GCL
    model_plain: Local-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3391
    metric_stds:
    - 0.0057
  - model: Graphormer_UltrasSmall
    model_plain: Graphormer_UltrasSmall
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.339
    metric_stds:
    - 0.014
  - model: ECL-GSR
    model_plain: ECL-GSR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3371
    metric_stds:
    - 0.0096
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3348
    metric_stds:
    - 0.0035
  - model: SANE
    model_plain: SANE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3341
    metric_stds:
    - 0.0141
  - model: ASGC
    model_plain: ASGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3341
    metric_stds:
    - 0.008
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3341
    metric_stds:
    - 0.0025
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3329
    metric_stds:
    - 0.0139
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3326
    metric_stds:
    - 0.0115
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
    - 0.3315
    metric_stds:
    - 0.0114
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
    - 0.331
    metric_stds:
    - 0.0138
  - model: CoGSL
    model_plain: CoGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3295
    metric_stds:
    - 0.012
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
    - 0.3276
    metric_stds:
    - 0.0139
  - model: GraphTrans (small)
    model_plain: GraphTrans (small)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.326
    metric_stds:
    - 0.007
  - model: GSC+Cheb
    model_plain: GSC+Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3246
    metric_stds:
    - 0.0013
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3222
    metric_stds:
    - 0.0234
  - model: GraphTrans_UltrasSmall
    model_plain: GraphTrans_UltrasSmall
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.321
    metric_stds:
    - 0.008
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3209
    metric_stds:
    - 0.0107
  - model: Diffusion-X
    model_plain: Diffusion-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3209
    metric_stds:
    - 0.007
  - model: GeomGCN
    model_plain: GeomGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3181
    metric_stds:
    - 0.0024
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3176
    metric_stds:
    - 0.0073
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3163
    metric_stds:
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.316
    metric_stds:
    - null
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.314
    metric_stds:
    - 0.008
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3139
    metric_stds:
    - 0.0053
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.313
    metric_stds:
    - 0.015
  - model: L2DGCN
    model_plain: L2DGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.313
    metric_stds:
    - 0.0035
  - model: Geom-GCN-I-g
    model_plain: Geom-GCN-I-g
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3127
    metric_stds:
    - null
  - model: Geom-GCN-IP
    model_plain: Geom-GCN-IP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3116
    metric_stds:
    - null
  - model: NSTE
    model_plain: NSTE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3114
    metric_stds:
    - 0.0046
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3105
    metric_stds:
    - 0.0131
  - model: DiGCNappr
    model_plain: DiGCNappr
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3099
    metric_stds:
    - 0.0049
  - model: GCL
    model_plain: GCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3092
    metric_stds:
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3087
    metric_stds:
    - 0.0038
  - model: DIMPA
    model_plain: DIMPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3084
    metric_stds:
    - 0.0073
  - model: Pro-GNN
    model_plain: Pro-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3083
    metric_stds:
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.308
    metric_stds:
    - 0.007
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3079
    metric_stds:
    - 0.0068
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3078
    metric_stds:
    - 0.0061
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
    - 0.3071
    metric_stds:
    - 0.0082
  - model: Shift-GAT
    model_plain: Shift-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.306
    metric_stds:
    - 0.006
  - model: LightDiC
    model_plain: LightDiC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3059
    metric_stds:
    - 0.005
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.305
    metric_stds:
    - 0.012
  - model: Acc(GCN)
    model_plain: Acc(GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.09125'
    title: arXiv:2401.09125
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3033
    metric_stds:
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.303
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3026
    metric_stds:
    - 0.0079
  - model: SGSR
    model_plain: SGSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3023
    metric_stds:
    - 0.0038
  - model: DisGNN
    model_plain: DisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.302
    metric_stds:
    - 0.013
  - model: STABLE
    model_plain: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3018
    metric_stds:
    - 0.01
  - model: NWR-GAE
    model_plain: NWR-GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3017
    metric_stds:
    - 0.0017
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10320'
    title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/dhsiuu/DiRW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3012
    metric_stds:
    - 0.0065
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3011
    metric_stds:
    - 0.0192
  - model: FS-MLP
    model_plain: FS-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3008
    metric_stds:
    - 0.002
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3007
    metric_stds:
    - 0.0076
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3002
    metric_stds:
    - 0.007
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2997
    metric_stds:
    - 0.0071
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2982
    metric_stds:
    - 0.0069
  - model: KNN w/ sp.-X
    model_plain: KNN w/ sp.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2972
    metric_stds:
    - 0.008
  - model: FS-GCN
    model_plain: FS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2969
    metric_stds:
    - 0.0014
  - model: Geom-GCN-I-s
    model_plain: Geom-GCN-I-s
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2941
    metric_stds:
    - null
  - model: SSGC
    model_plain: SSGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2939
    metric_stds:
    - 0.0017
  - model: VEPM
    model_plain: VEPM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.293
    metric_stds:
    - 0.011
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
    - 0.2926
    metric_stds:
    - 0.0231
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2915
    metric_stds:
    - 0.007
  - model: NE
    model_plain: NE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2903
    metric_stds:
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.29
    metric_stds:
    - 0.014
  - model: AF-GCL
    model_plain: AF-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2894
    metric_stds:
    - 0.0069
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2891
    metric_stds:
    - 0.0018
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2889
    metric_stds:
    - 0.005
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
    - 0.2887
    metric_stds:
    - 0.0139
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.288
    metric_stds:
    - 0.0054
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2862
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2861
    metric_stds:
    - 0.0039
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2856
    metric_stds:
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2854
    metric_stds:
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2848
    metric_stds:
    - 0.0125
  - model: gfNN
    model_plain: gfNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2848
    metric_stds:
    - 0.0019
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2845
    metric_stds:
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2843
    metric_stds:
    - 0.0016
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2836
    metric_stds:
    - 0.0065
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.283
    metric_stds:
    - 0.0076
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
    - 0.2829
    metric_stds:
    - 0.0145
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2827
    metric_stds:
    - 0.0043
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2816
    metric_stds:
    - 0.0141
  - model: TFE-GNN
    model_plain: TFE-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.281
    metric_stds:
    - 0.0081
  - model: JK
    model_plain: JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2796
    metric_stds:
    - 0.01
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2793
    metric_stds:
    - 0.0017
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.279
    metric_stds:
    - 0.011
  - model: SNAG
    model_plain: SNAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2784
    metric_stds:
    - 0.0129
  - model: CGP (SGC)
    model_plain: CGP (SGC)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.277
    metric_stds:
    - null
  - model: DNNs
    model_plain: DNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.277
    metric_stds:
    - 0.004
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.276
    metric_stds:
    - 0.0018
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2757
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2753
    metric_stds:
    - 0.005
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.275
    metric_stds:
    - 0.0095
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.273
    metric_stds:
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2728
    metric_stds:
    - 0.0087
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2721
    metric_stds:
    - 0.0205
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.27
    metric_stds:
    - 0.0073
  - model: GCN
    model_plain: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2686
    metric_stds:
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2684
    metric_stds:
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.267
    metric_stds:
    - 0.008
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2666
    metric_stds:
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.266
    metric_stds:
    - 0.0014
  - model: PolyGCL
    model_plain: PolyGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2652
    metric_stds:
    - 0.0007
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.265
    metric_stds:
    - 0.0117
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.264
    metric_stds:
    - 0.0097
  - model: PCNet
    model_plain: PCNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.264
    metric_stds:
    - 0.008
  - model: DIFFormer
    model_plain: DIFFormer
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
    - 0.2631
    metric_stds:
    - 0.0119
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2628
    metric_stds:
    - 0.0173
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2618
    metric_stds:
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.261
    metric_stds:
    - 0.012
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.261
    metric_stds:
    - 0.009
  - model: TED-GCN
    model_plain: TED-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.26
    metric_stds:
    - 0.009
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
    - 0.2589
    metric_stds:
    - 0.008
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.258
    metric_stds:
    - null
  - model: GAuG-O
    model_plain: GAuG-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.258
    metric_stds:
    - 0.01
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.257
    metric_stds:
    - 0.012
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2561
    metric_stds:
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2555
    metric_stds:
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2555
    metric_stds:
    - 0.0167
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2551
    metric_stds:
    - 0.0117
  - model: AERO-GNN
    model_plain: AERO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.255
    metric_stds:
    - 0.01
  - model: GraphNAS
    model_plain: GraphNAS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2547
    metric_stds:
    - 0.0132
  - model: BNLL
    model_plain: BNLL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2533
    metric_stds:
    - 0.0034
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.00064'
    title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning via SVD-Guided Structural
      Perturbation'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2531
    metric_stds:
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.251
    metric_stds:
    - 0.005
  - model: N2V
    model_plain: N2V
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2502
    metric_stds:
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.249
    metric_stds:
    - 0.02
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.2473
    metric_stds:
    - null
  - model: GBT
    model_plain: GBT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2468
    metric_stds:
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.246
    metric_stds:
    - 0.008
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2426
    metric_stds:
    - null
  - model: AE
    model_plain: AE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2419
    metric_stds:
    - null
  - model: SDCN
    model_plain: SDCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2367
    metric_stds:
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2345
    metric_stds:
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2308
    metric_stds:
    - null
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2283
    metric_stds:
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.228
    metric_stds:
    - 0.003
  - model: Logistic Reg.-A
    model_plain: Logistic Reg.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2266
    metric_stds:
    - 0.003
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.225
    metric_stds:
    - 0.003
  - model: S2V
    model_plain: S2V
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.10866'
    title: Unsupervised Network Embedding Beyond Homophily
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: https://github.com/zhiqiangzhongddu/SELENE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2249
    metric_stds:
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2235
    metric_stds:
    - 0.0088
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.219
    metric_stds:
    - 0.004
  - model: GAM
    model_plain: GAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.217
    metric_stds:
    - 0.003
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.215
    metric_stds:
    - 0.002
  - model: PTDNet
    model_plain: PTDNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.215
    metric_stds:
    - 0.005
  - model: Ortho-GCN
    model_plain: Ortho-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.214
    metric_stds:
    - 0.016
  - model: KNN w/ sp.-A
    model_plain: KNN w/ sp.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2057
    metric_stds:
    - 0.01
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.204
    metric_stds:
    - 0.006
  - model: Diffusion-A
    model_plain: Diffusion-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1997
    metric_stds:
    - 0.01
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
    - 0.198
    metric_stds:
    - 0.0261
  milestones:
  - value: 0.3127
    std: null
    model: Geom-GCN-I-g
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: 2020-02
  - value: 0.3586
    std: 0.0103
    model: H2GCN-1
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: 2021-05
  - value: 0.393
    std: 0.0027
    model: GPRGNN
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: 2022-02
  - value: 0.4247
    std: 0.0007
    model: GNN-HF
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: 2023-05
  - value: 0.425
    std: 0.0019
    model: SpatUFG
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: 2023-07
  - value: 0.746
    std: 0.013
    model: Sage + DisamGCL
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: 2024-02
  - value: 0.7682
    std: 0.005
    model: Vicuna-7B
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: 2024-08
---

