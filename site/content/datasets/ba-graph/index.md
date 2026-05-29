---
title: BA graph
slug: ba-graph
benchmark: GraphBench
task_type: graph_classification
description: Node classification on Barabási–Albert random graphs (GraphBench algorithmic
  reasoning).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 132
best_model:
  model: DyGFormer
  value: 1.0
  metric: Accuracy
  arxiv_id: '2406.02740'
  paper_title: Long Range Propagation on Continuous-Time Dynamic Graphs
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
  - AUC
  - AUROC
  - F1
  - MAE
  - PRAUC
  - RMSE
  - V.U.N.
  rows:
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: false
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
    - 0.98
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
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
    - 0.968
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: SAN
    model_plain: SAN
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
    - 0.96
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GradInput
    model_plain: GradInput
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.08621'
    title: 'Zorro: Valid, Sparse, and Stable Explanations in Graph Neural Networks'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/funket/zorro
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.96
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
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
    - 0.955
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DGN
    model_plain: DGN
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
    - 0.95
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.08621'
    title: 'Zorro: Valid, Sparse, and Stable Explanations in Graph Neural Networks'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/funket/zorro
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAN
    model_plain: SAN
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
    - 0.948
    - null
    - null
    - null
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
    - null
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
    - 0.94
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: SubgraphX
    model_plain: SubgraphX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.08621'
    title: 'Zorro: Valid, Sparse, and Stable Explanations in Graph Neural Networks'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/funket/zorro
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.94
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
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
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.93
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: PGM
    model_plain: PGM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.08621'
    title: 'Zorro: Valid, Sparse, and Stable Explanations in Graph Neural Networks'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/funket/zorro
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.93
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.92
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.91
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Zorro (tau=.85)
    model_plain: Zorro (tau=.85)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.08621'
    title: 'Zorro: Valid, Sparse, and Stable Explanations in Graph Neural Networks'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/funket/zorro
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
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
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.89
    - null
    - null
    - null
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
    - 0.888
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: G-Meta
    model_plain: G-Meta
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.867
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.147
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtoNet
    model_plain: ProtoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.858
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.144
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MAML
    model_plain: MAML
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.848
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.212
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNNExplainer
    model_plain: GNNExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.08621'
    title: 'Zorro: Valid, Sparse, and Stable Explanations in Graph Neural Networks'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/funket/zorro
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KNN
    model_plain: KNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Oracle
    model_plain: Oracle
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7838
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FS-GIN
    model_plain: FS-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.749
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.106
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GALA
    model_plain: GALA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0106
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FS-SGC
    model_plain: FS-SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Meta-GNN
    model_plain: Meta-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Finetune
    model_plain: Finetune
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.671
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SCM
    model_plain: SCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6687
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0089
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RCGRL
    model_plain: RCGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6658
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IGM
    model_plain: IGM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6623
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0158
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DCSGL-A
    model_plain: DCSGL-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6532
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisC
    model_plain: DisC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6528
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6514
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0137
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CIGA
    model_plain: CIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6445
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0199
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G-Mixup
    model_plain: G-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6391
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0301
    - null
    - null
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
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6357
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IRM
    model_plain: IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0123
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Top-k Pool
    model_plain: Top-k Pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6341
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0195
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DCS-Only-L
    model_plain: DCS-Only-L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.633
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0109
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DCSGL-T
    model_plain: DCSGL-T
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6326
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Average
    model_plain: Average
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6325
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6321
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0157
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DCS-Only-D
    model_plain: DCS-Only-D
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.632
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6319
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0113
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSN
    model_plain: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6318
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0189
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EIIL
    model_plain: EIIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6276
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0172
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Manifold-Mixup
    model_plain: Manifold-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.626
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0187
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSAT
    model_plain: GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.625
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0144
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Group DRO
    model_plain: Group DRO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08709'
    title: Introducing Diminutive Causal Structure into Graph Representation Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6223
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0143
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6081
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0205
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5985
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0298
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: No-Finetune
    model_plain: No-Finetune
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.07889'
    title: Graph Meta Learning via Local Subgraphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/mims-harvard/G-Meta
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.567
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAL+
    model_plain: CAL+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4623
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0393
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CIGA
    model_plain: CIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4362
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4273
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0382
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IB-IRM
    model_plain: IB-IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4205
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4165
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0278
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IRM
    model_plain: IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIL
    model_plain: GIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0261
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EIIL
    model_plain: EIIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3971
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0264
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisC
    model_plain: DisC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3942
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0859
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GREA
    model_plain: GREA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3901
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0121
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: XGNN
    model_plain: XGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3828
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSAT
    model_plain: GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3662
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoleOOD
    model_plain: MoleOOD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19035'
    title: Does Invariant Graph Learning via Environment Augmentation Learn Invariance?
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/LFhase/GALA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3481
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0165
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGE
    model_plain: PGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.08621'
    title: 'Zorro: Valid, Sparse, and Stable Explanations in Graph Neural Networks'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/funket/zorro
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.21
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Stable-ChebNet
    model_plain: Stable-ChebNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.5656
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.1211
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.7051
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.1235
    - null
    - null
    - null
  - model: A-DGN w/ GCN backbone
    model_plain: A-DGN w/ GCN backbone
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.1913
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0731
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 5.5313
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.3516
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 6.6362
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.6015
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 7.3165
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.3269
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 4.1086
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.6653
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 3.3753
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.3627
    - null
    - null
    - null
  - model: DGC
    model_plain: DGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 4.0051
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.0345
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 4.6896
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.3465
    - null
    - null
    - null
  - model: PGExplainer
    model_plain: PGExplainer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.945
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNNExplainer
    model_plain: GNNExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.836
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.75
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ATT
    model_plain: ATT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.739
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - 0.173
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.002
    - null
    - null
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
    - null
    - 0.145
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.004
    - null
    - null
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
    - null
    - 0.218
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - 0.186
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.006
    - null
    - null
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
    - null
    - 0.22
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.01
    - null
    - null
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
    - null
    - 0.744
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.008
    - null
    - null
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
    - null
    - 0.936
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.003
    - null
    - null
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
    - null
    - 0.95
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.006
    - null
    - null
    - null
    - null
  - model: GraphSNN
    model_plain: GraphSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SPECTRE
    model_plain: SPECTRE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.25
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiGress
    model_plain: DiGress
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.775
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EDGE
    model_plain: EDGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BwR (EDP-GNN)
    model_plain: BwR (EDP-GNN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BiGG
    model_plain: BiGG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.05
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGen
    model_plain: GraphGen
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 1.0
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBM (one-shot)
    model_plain: SBM (one-shot)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.675
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBM
    model_plain: SBM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11529'
    title: Efficient and Scalable Graph Generation through Iterative Local Expansion
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/AndreasBergmeister/graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.95
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GFM-1
    model_plain: GFM-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6477
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.017
    - null
    - null
  - model: GFM-2
    model_plain: GFM-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6981
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0151
    - null
    - null
  - model: GFM-3
    model_plain: GFM-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7442
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0174
    - null
    - null
  - model: NN
    model_plain: NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6561
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0101
    - null
    - null
  - model: HGT-1
    model_plain: HGT-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6123
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0195
    - null
    - null
  - model: HAN-1
    model_plain: HAN-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6173
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0185
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7564
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0167
    - null
    - null
  - model: HGT-2
    model_plain: HGT-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6473
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0061
    - null
    - null
  - model: HAN-2
    model_plain: HAN-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6165
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0188
    - null
    - null
  - model: HGT-3
    model_plain: HGT-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7688
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0214
    - null
    - null
  - model: HAN-3
    model_plain: HAN-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.04768'
    title: Billion-Scale Graph Foundation Models
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7432
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0096
    - null
    - null
  - model: GCN
    model_plain: GCN
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
    - null
    - 0.74
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0151
    - null
    - null
    - null
    - null
    - null
  - model: Nifty-GCN
    model_plain: Nifty-GCN
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
    - null
    - 0.6946
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0399
    - null
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
    - null
    - 0.7269
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0102
    - null
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
    - null
    - 0.7454
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0086
    - null
    - null
    - null
    - null
    - null
  - model: Nifty-GraphSAGE
    model_plain: Nifty-GraphSAGE
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
    - null
    - 0.7054
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0203
    - null
    - null
    - null
    - null
    - null
  - model: Infomax
    model_plain: Infomax
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
    - null
    - 0.6798
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0394
    - null
    - null
    - null
    - null
    - null
  - model: Nifty-Infomax
    model_plain: Nifty-Infomax
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
    - null
    - 0.7201
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0205
    - null
    - null
    - null
    - null
    - null
  - model: JK
    model_plain: JK
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
    - null
    - 0.7149
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0264
    - null
    - null
    - null
    - null
    - null
  - model: Nifty-JK
    model_plain: Nifty-JK
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
    - null
    - 0.7042
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0203
    - null
    - null
    - null
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
    - null
    - 0.7521
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0036
    - null
    - null
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
    - null
    - 0.7106
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0148
    - null
    - null
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
    - null
    - null
    - 0.95
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - null
    - 0.97
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - null
    - 1.16
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - null
    - 0.96
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.98
    std: 0.005
    model: GraphGPS
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
  - value: 1.0
    std: null
    model: DyGFormer
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
---

