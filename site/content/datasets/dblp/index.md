---
title: DBLP
slug: dblp
benchmark: Heterogeneous Graph Benchmarks
task_type: node_classification
description: Heterogeneous academic graph — classify author nodes (4 research areas).
primary_metric: Micro-F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.DBLP.html
stats:
  num_graphs: 1
  avg_nodes: null
  avg_edges: null
  num_classes: 4
result_count: 295
best_model:
  model: HetSANN.M.R
  value: 0.9563
  metric: Micro-F1
  arxiv_id: '1912.10832'
  paper_title: An Attention-based Graph Neural Network for Heterogeneous Structural
    Learning
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Micro-F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Micro-F1
  - AP
  - AUC
  - Accuracy
  - F1
  - MRR
  - MSE
  - NDCG
  - NMI
  - P@1
  - Weighted-F1
  rows:
  - model: HetSANN.M.R
    model_plain: HetSANN.M.R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9563
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HeSRN
    model_plain: HeSRN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.09767'
    title: 'HeSRN: Representation Learning On Heterogeneous Graphs via Slot-Aware
      Retentive Network'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/csyifan/HeSRN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PHGT
    model_plain: PHGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.09767'
    title: 'HeSRN: Representation Learning On Heterogeneous Graphs via Slot-Aware
      Retentive Network'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/csyifan/HeSRN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9533
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SlotGAT
    model_plain: SlotGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9531
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HINormer-GIN
    model_plain: HINormer-GIN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9511
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HINormer-GAT
    model_plain: HINormer-GAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9511
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HINormer-Transformer
    model_plain: HINormer-Transformer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9501
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HINormer
    model_plain: HINormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9494
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HetSANN
    model_plain: HetSANN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9489
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Fast-GTN
    model_plain: Fast-GTN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9485
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 3.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GTN_-I
    model_plain: GTN_-I
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9474
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 5.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SHGN HDHGR
    model_plain: SHGN HDHGR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9473
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT HDHGR
    model_plain: GAT HDHGR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.947
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
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
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9468
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 2.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: space4HGNN
    model_plain: space4HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9463
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HINormer-Adj
    model_plain: HINormer-Adj
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9457
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GTN
    model_plain: GTN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9447
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 3.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimpleHGN
    model_plain: SimpleHGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SHGN
    model_plain: SHGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Simple-HGN
    model_plain: Simple-HGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.09767'
    title: 'HeSRN: Representation Learning On Heterogeneous Graphs via Slot-Aware
      Retentive Network'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/csyifan/HeSRN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: simple model
    model_plain: simple model
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9429
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HINormer-SAGE
    model_plain: HINormer-SAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9426
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT
    model_plain: HGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9421
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 5.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisenHAN
    model_plain: DisenHAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9418
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9399
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RSHN
    model_plain: RSHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9381
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9376
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LINKX HDHGR
    model_plain: LINKX HDHGR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9369
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.09767'
    title: 'HeSRN: Representation Learning On Heterogeneous Graphs via Slot-Aware
      Retentive Network'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/csyifan/HeSRN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9368
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT
    model_plain: HGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9349
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
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
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9339
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9316
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 2.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.09767'
    title: 'HeSRN: Representation Learning On Heterogeneous Graphs via Slot-Aware
      Retentive Network'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/csyifan/HeSRN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9315
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9299
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN HDHGR
    model_plain: GCN HDHGR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9277
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
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
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9271
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN + DHGR
    model_plain: GCN + DHGR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9259
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN HDHGR
    model_plain: HAN HDHGR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9257
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9234
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HetGNN
    model_plain: HetGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9233
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9217
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 5.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9207
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9201
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9194
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Mp2vec
    model_plain: Mp2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9188
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9154
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06299'
    title: Homophily-oriented Heterogeneous Graph Rewiring
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9147
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HetGNN
    model_plain: HetGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9092
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HGT
    model_plain: HGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9087
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HERec
    model_plain: HERec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9049
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8911
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8835
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8827
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.877
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8709
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 1.0e-05
    - null
    - null
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
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8563
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 3.0e-05
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8546
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    - 0.813
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    - 0.811
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HetSANN
    model_plain: HetSANN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11329'
    title: 'HINormer: Representation Learning On Heterogeneous Information Networks
      with Graph Transformer'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8056
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCL
    model_plain: GCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0136
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.792
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06218'
    title: 'Graph Transformer Networks: Learning Meta-path Graphs to Improve GNNs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/seongjunyun/Graph_Transformer_Networks
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7918
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMGI
    model_plain: DMGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HDGI
    model_plain: HDGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.10024'
    title: Leveraging Meta-path Contexts for Classification in Heterogeneous Information
      Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/dingdanhao110/Conch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7733
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DyGC
    model_plain: DyGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.768
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DMGI
    model_plain: DMGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.766
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DFCN
    model_plain: DFCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
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
    - 0.746
    - null
    - null
    - null
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
    - null
    - null
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
    - 0.744
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7378
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0151
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.732
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7308
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0196
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGC
    model_plain: SimGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN/GAT
    model_plain: GCN/GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7135
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: mGCN
    model_plain: mGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7113
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6901
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0148
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Herding
    model_plain: Herding
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.689
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6864
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: SDCN
    model_plain: SDCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.677
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MetaPath2Vec
    model_plain: MetaPath2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: https://github.com/didi/hetsann
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6675
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.665
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM
    model_plain: GCDM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.663
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: SDCN_Q
    model_plain: SDCN_Q
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CGC
    model_plain: CGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.655
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.643
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: K-Center
    model_plain: K-Center
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.642
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOND
    model_plain: GCOND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.642
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.638
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.618
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.618
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.614
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDEC
    model_plain: IDEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.613
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DEC
    model_plain: DEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.594
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.587
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    - 0.56
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5469
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0081
    - null
    - null
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
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.537
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: AE
    model_plain: AE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.525
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Raw features
    model_plain: Raw features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.517
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.413
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    - 0.334
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.09600'
    title: Deep Fusion Clustering Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/WxTu/DFCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.319
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.269
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.8133
    - null
    - 0.8565
    - null
    - 0.7267
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
    - null
    - null
    - null
  - model: PLM
    model_plain: PLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6777
    - null
    - 0.7484
    - null
    - 0.5673
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
    - null
    - null
    - null
  - model: TNVE
    model_plain: TNVE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.4163
    - null
    - 0.5295
    - null
    - 0.2978
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
    - null
    - null
    - null
  - model: IFTN
    model_plain: IFTN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.4773
    - null
    - 0.5798
    - null
    - 0.3691
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
    - null
    - null
    - null
  - model: PLM+GAT
    model_plain: PLM+GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7667
    - null
    - 0.8204
    - null
    - 0.6633
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
    - null
    - null
    - null
  - model: PLM+Max
    model_plain: PLM+Max
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.79
    - null
    - 0.8386
    - null
    - 0.6934
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
    - null
    - null
    - null
  - model: PLM+Mean
    model_plain: PLM+Mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7866
    - null
    - 0.8359
    - null
    - 0.6896
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
    - null
    - null
    - null
  - model: PLM+Att
    model_plain: PLM+Att
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.02605'
    title: 'GraphFormers: GNN-nested Transformers for Representation Learning on Textual
      Graph'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/microsoft/GraphFormers
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7875
    - null
    - 0.8366
    - null
    - 0.691
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8393
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
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN
    model_plain: AD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8414
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
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN_fast
    model_plain: AD-GCN_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.839
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
    - 0.0097
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
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8061
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
    - 0.0121
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GAT
    model_plain: AD-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8394
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
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GAT_fast
    model_plain: AD-GAT_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8426
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
    - 0.0052
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
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8616
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GraphSAGE
    model_plain: AD-GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.85
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
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GraphSAGE_fast
    model_plain: AD-GraphSAGE_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8503
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
    - 0.0139
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8427
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
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-MixHop
    model_plain: AD-MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8426
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
    - 0.0081
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-MixHop_fast
    model_plain: AD-MixHop_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8446
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
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8485
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
    - 0.0061
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GATv2
    model_plain: AD-GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8426
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
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8122
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
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-DirGNN
    model_plain: AD-DirGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8352
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
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-DirGNN_fast
    model_plain: AD-DirGNN_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.828
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
    - 0.0065
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SC
    model_plain: SC
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
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.027
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
    - 0.003
    - null
    - null
  - model: MSC
    model_plain: MSC
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
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.005
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
    - 0.006
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
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
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.186
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
    - 0.014
    - null
    - null
  - model: MinCutPool
    model_plain: MinCutPool
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
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.334
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
    - 0.026
    - null
    - null
  - model: HP-1
    model_plain: HP-1
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
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.326
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
    - 0.027
    - null
    - null
  - model: HP-2
    model_plain: HP-2
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
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.284
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
    - 0.026
    - null
    - null
  - model: HoscPool
    model_plain: HoscPool
    is_baseline: false
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
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.312
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
    - 0.027
    - null
    - null
  - model: NGNN
    model_plain: NGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.808
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
    - 0.004
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
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.71
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
    - 0.015
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
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.724
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
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Self-training
    model_plain: Self-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.749
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
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Forward
    model_plain: Forward
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.731
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Coteaching+
    model_plain: Coteaching+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.735
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
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DS-GNN
    model_plain: DS-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.728
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
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CP
    model_plain: CP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.742
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Adamic Adar
    model_plain: Adamic Adar
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8248
    - 0.9113
    - null
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
    - null
    - null
    - null
  - model: DC-SBM
    model_plain: DC-SBM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9657
    - 0.9705
    - null
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
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9636
    - 0.9641
    - null
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
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9693
    - 0.9638
    - null
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
    - null
    - null
    - null
  - model: NetGAN (500K)
    model_plain: NetGAN (500K)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7028
    - 0.8245
    - null
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
    - null
    - null
    - null
  - model: NetGAN (100M)
    model_plain: NetGAN (100M)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.00816'
    title: arXiv:1803.00816
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8921
    - 0.8661
    - null
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
    - null
    - null
    - null
  - model: Scattering GCN
    model_plain: Scattering GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.815
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
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.661
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
    - null
    - null
    - null
  - model: Partially absorbing
    model_plain: Partially absorbing
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.569
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.593
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
    - null
    - null
    - null
  - model: Chebyshev
    model_plain: Chebyshev
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.573
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
    - null
    - null
    - null
  - model: Label Propagation
    model_plain: Label Propagation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.53
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
    - null
    - null
    - null
  - model: Graph scattering
    model_plain: Graph scattering
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.694
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
    - null
    - null
    - null
  - model: Node features (SVM)
    model_plain: Node features (SVM)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.482
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
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9207
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9205
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
    - 0.0062
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT
    model_plain: HGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9349
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
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SHGN
    model_plain: SHGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.942
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
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.941
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2GAE
    model_plain: S2GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.948
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
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MaskGAE
    model_plain: MaskGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.942
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
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: lrGAE (6)
    model_plain: lrGAE (6)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.944
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
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: lrGAE (7)
    model_plain: lrGAE (7)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.946
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: lrGAE (8)
    model_plain: lrGAE (8)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.943
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
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.64
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
    - 0.028
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
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.715
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
    - 0.027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.692
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
    - 0.028
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
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.681
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
    - 0.025
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
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.718
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
    - 0.026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.725
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
    - 0.025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC+DGCN
    model_plain: SGC+DGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.711
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
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoE
    model_plain: CoE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9227
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
    - 0.0024
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.807
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8128
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
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8717
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
    - 0.0081
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.911
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
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7929
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
    - 0.0058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.911
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
    - 0.0146
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9133
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
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8026
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
    - 0.0066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9149
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
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STABLE
    model_plain: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.79
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
    - 0.0198
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSR
    model_plain: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7783
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
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HDMI
    model_plain: HDMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9014
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
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InfoMGF
    model_plain: InfoMGF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9145
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
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMoE
    model_plain: GMoE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9118
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
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Mowst
    model_plain: Mowst
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8969
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
    - 0.0099
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RF
    model_plain: RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9148
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
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WRF
    model_plain: WRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9197
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
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SDCN
    model_plain: SDCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.6771
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
    - 0.0151
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SDCN_Q
    model_plain: SDCN_Q
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.6578
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
    - 0.0122
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.6175
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
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.5869
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
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.6141
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
    - 0.0223
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDEC
    model_plain: IDEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.6133
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
    - 0.0056
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DEC
    model_plain: DEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.5938
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
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AE
    model_plain: AE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.5253
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
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.3192
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
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SegTran
    model_plain: SegTran
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.08827'
    title: Semi-Supervised Graph-to-Graph Translation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.192
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
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5218
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5154
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7135
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7108
    metric_stds:
    - null
    - null
    - null
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
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7001
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6921
    metric_stds:
    - null
    - null
    - null
    - null
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
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7236
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7199
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAW
    model_plain: CAW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5564
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5138
    metric_stds:
    - null
    - null
    - null
    - null
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
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5748
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5196
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DySAT
    model_plain: DySAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5412
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5248
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MNCI
    model_plain: MNCI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6703
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6646
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6997
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.694
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7127
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7071
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7132
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7091
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6828
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.676
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLDG_node
    model_plain: CLDG_node
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.718
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7155
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLDG_graph
    model_plain: CLDG_graph
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7203
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7169
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8118
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
    - 0.002
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
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8758
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
    - 0.002
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
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8859
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
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DHGNN
    model_plain: DHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8832
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperConv
    model_plain: HyperConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8883
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
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HNHN
    model_plain: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8671
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
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperGCN
    model_plain: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7659
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
    - 0.076
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperSAGE
    model_plain: HyperSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7963
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
    - 0.086
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniGCN
    model_plain: UniGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9031
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
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AllSet
    model_plain: AllSet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9007
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7209
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.88
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
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2-HHGR
    model_plain: S2-HHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8869
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
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random-Init
    model_plain: Random-Init
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7657
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TriCL-N
    model_plain: TriCL-N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9094
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
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TriCL
    model_plain: TriCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9112
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
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.862
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
    - null
    - null
    - null
  - model: O2MAC
    model_plain: O2MAC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.901
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
    - null
    - null
    - null
  - model: HDMI
    model_plain: HDMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.865
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
    - null
    - null
    - null
  - model: CMGEC
    model_plain: CMGEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.904
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
    - null
    - null
    - null
  - model: MvAGC
    model_plain: MvAGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.923
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
    - null
    - null
    - null
  - model: MCGC
    model_plain: MCGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.925
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
    - null
    - null
    - null
  - model: DMG
    model_plain: DMG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.879
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
    - null
    - null
    - null
  - model: BTGF
    model_plain: BTGF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.873
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
    - null
    - null
    - null
  - model: CDC
    model_plain: CDC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.929
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
    - null
    - null
    - null
  - model: GNNExplainer
    model_plain: GNNExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.828
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
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGExplainer
    model_plain: PGExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.812
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGIB
    model_plain: VGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.805
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
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGIB
    model_plain: PGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.813
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
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCFExplainer
    model_plain: GCFExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.827
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphTrail
    model_plain: GraphTrail
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.792
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.776
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WWL
    model_plain: WWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.818
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FWL
    model_plain: FWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.819
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
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAWL
    model_plain: GAWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.811
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN+T
    model_plain: GNN+T
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.854
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WEGL
    model_plain: WEGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.804
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
    - 0.004
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
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.833
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
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DropGIN
    model_plain: DropGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.83
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
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SEP
    model_plain: SEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.855
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
    - 0.003
    - null
    - null
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
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.852
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MinCutPool
    model_plain: MinCutPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.849
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ASAP
    model_plain: ASAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.826
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WITTOPOPOOL
    model_plain: WITTOPOPOOL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.856
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
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRDL
    model_plain: GRDL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.862
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.848
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
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.859
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
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCBM
    model_plain: GCBM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.862
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
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCBM-E
    model_plain: GCBM-E
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.876
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
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SNS
    model_plain: SNS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.925
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
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + GraphENS
    model_plain: ie-HGCN + GraphENS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9162
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
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + Self-training
    model_plain: ie-HGCN + Self-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8934
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
    - 0.0157
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + ROS
    model_plain: ie-HGCN + ROS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9028
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
    - 0.0087
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + SMOTE
    model_plain: ie-HGCN + SMOTE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.897
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
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + Reweight
    model_plain: ie-HGCN + Reweight
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8995
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
    - 0.0082
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + Focal loss
    model_plain: ie-HGCN + Focal loss
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.9154
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
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + BS
    model_plain: ie-HGCN + BS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8935
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
    - 0.0176
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ie-HGCN + cRT
    model_plain: ie-HGCN + cRT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8987
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
    - 0.0062
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Vanilla ie-HGCN
    model_plain: Vanilla ie-HGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8932
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
    - 0.0102
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + GraphENS
    model_plain: HGT + GraphENS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8986
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
    - 0.0063
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + Self-training
    model_plain: HGT + Self-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8786
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
    - 0.0115
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + ROS
    model_plain: HGT + ROS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8794
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
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + SMOTE
    model_plain: HGT + SMOTE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8871
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
    - 0.0094
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + Reweight
    model_plain: HGT + Reweight
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8846
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
    - 0.0164
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + Focal loss
    model_plain: HGT + Focal loss
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8811
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
    - 0.0113
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + BS
    model_plain: HGT + BS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8897
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
    - 0.0086
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGT + cRT
    model_plain: HGT + cRT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8799
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
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + Vanilla
    model_plain: GAT + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14061'
    title: Semantic-aware Node Synthesis for Imbalanced Heterogeneous Information
      Networks
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.8774
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
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.9563
    std: null
    model: HetSANN.M.R
    arxiv_id: '1912.10832'
    title: An Attention-based Graph Neural Network for Heterogeneous Structural Learning
    date: 2019-12
---

