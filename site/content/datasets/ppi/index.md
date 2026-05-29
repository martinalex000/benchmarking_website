---
title: PPI
slug: ppi
benchmark: Classic
task_type: node_classification
description: Protein-protein interaction node classification (121 GO labels, multi-label).
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.PPI.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 121
result_count: 163
best_model:
  model: GCNII
  value: 0.9956
  metric: F1
  arxiv_id: '2007.02133'
  paper_title: arXiv:2007.02133
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - AUROC
  - Accuracy
  - ROC-AUC
  rows:
  - model: GCNII
    model_plain: GCNII
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9956
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.995
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9936
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GBP
    model_plain: GBP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.993
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.992
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
  - model: GaAN
    model_plain: GaAN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9871
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
  - model: Full Prec. GAT
    model_plain: Full Prec. GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.987
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GeniePath
    model_plain: GeniePath
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.985
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Attention-only
    model_plain: Attention-only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9846
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
  - model: GIND
    model_plain: GIND
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.984
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Max pooling
    model_plain: Max pooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9839
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
  - model: Pairwise+sigmoid
    model_plain: Pairwise+sigmoid
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9839
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
  - model: Pairwise+tanh
    model_plain: Pairwise+tanh
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9832
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.981
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GraphSAINT-EDGE
    model_plain: GraphSAINT-EDGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.981
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
  - model: GraphSAINT + RWSE
    model_plain: GraphSAINT + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.981
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.978
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: ANA
    model_plain: ANA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9771
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Teacher
    model_plain: Teacher
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.10477'
    title: Distilling Knowledge from Graph Convolutional Networks
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/ihollywhy/DistillGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.976
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.976
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GNA
    model_plain: GNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9752
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.973
    - null
    - null
    - null
    metric_stds:
    - 0.002
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
    - 0.971
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Supervised GCN MeanPooling
    model_plain: Supervised GCN MeanPooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.969
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GaAN
    model_plain: GaAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.969
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: Avg. pooling
    model_plain: Avg. pooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9685
    - null
    - null
    - null
    metric_stds:
    - 0.0019
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
    - 0.965
    - null
    - null
    - null
    metric_stds:
    - 0.001
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
    - 0.964
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: Stochastic-GCN
    model_plain: Stochastic-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.963
    - null
    - null
    - null
    metric_stds:
    - 0.01
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
    - 0.963
    - null
    - null
    - null
    metric_stds:
    - 0.001
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
    - 0.962
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: Student_LSP
    model_plain: Student_LSP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.10477'
    title: Distilling Knowledge from Graph Convolutional Networks
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/ihollywhy/DistillGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.961
    - null
    - null
    - null
    metric_stds:
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
    - 0.961
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
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
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
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
    - 0.958
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: Student_Full
    model_plain: Student_Full
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.10477'
    title: Distilling Knowledge from Graph Convolutional Networks
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/ihollywhy/DistillGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.957
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Student_FitNet
    model_plain: Student_FitNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.10477'
    title: Distilling Knowledge from Graph Convolutional Networks
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/ihollywhy/DistillGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.956
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Student_AT
    model_plain: Student_AT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.10477'
    title: Distilling Knowledge from Graph Convolutional Networks
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/ihollywhy/DistillGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.954
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
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
    - 0.942
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
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
    - 0.935
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
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
    - 0.933
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.931
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 0.929
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.928
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: Vanilla Binarized GNN
    model_plain: Vanilla Binarized GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9268
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.926
    - null
    - null
    - null
    metric_stds:
    - 0.002
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.905
    - null
    - null
    - null
    metric_stds:
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
    - 0.898
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: S-GCN
    model_plain: S-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.892
    - null
    - null
    - null
    metric_stds:
    - 0.015
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
    - 0.881
    - null
    - null
    - null
    metric_stds:
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
    - 0.879
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.875
    - null
    - null
    - null
    metric_stds:
    - 0.004
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
    - 0.87
    - null
    - null
    - null
    metric_stds:
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
    - 0.86
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: LGCN_sub
    model_plain: LGCN_sub
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.772
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: LaplaceGNN
    model_plain: LaplaceGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7573
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7565
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7483
    - null
    - null
    - null
    metric_stds:
    - 0.0033
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
    - 0.748
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: HAT-GAE
    model_plain: HAT-GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7472
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7439
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
  - model: BGRL GAT encoder
    model_plain: BGRL GAT encoder
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7361
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7352
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
  - model: GATNE
    model_plain: GATNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7325
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7321
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: InfoGCL
    model_plain: InfoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7314
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7276
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
  - model: GRACE GAT encoder
    model_plain: GRACE GAT encoder
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6971
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
  - model: GRACE MeanPooling encoder
    model_plain: GRACE MeanPooling encoder
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6966
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: Parallelized Graph Sampling
    model_plain: Parallelized Graph Sampling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.696
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6959
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: BGRL MeanPooling encoder
    model_plain: BGRL MeanPooling encoder
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6941
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: AS-GCN
    model_plain: AS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.687
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.685
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6751
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.669
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.659
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.657
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
  - model: NS-SAGE
    model_plain: NS-SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.638
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
  - model: Random-Init
    model_plain: Random-Init
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.626
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GZoom(GSAGE-mean, l=1)
    model_plain: GZoom(GSAGE-mean, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.617
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: PPRGo
    model_plain: PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.615
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
  - model: GZoom(GSAGE-LSTM, l=1)
    model_plain: GZoom(GSAGE-LSTM, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.615
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GZoom(GSAGE-pool, l=1)
    model_plain: GZoom(GSAGE-pool, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.614
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-LSTM
    model_plain: GraphSAGE-LSTM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: SAGE-LSTM
    model_plain: SAGE-LSTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GZoom(GSAGE-GCN, l=1)
    model_plain: GZoom(GSAGE-GCN, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-pool
    model_plain: GraphSAGE-pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.602
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-GCN
    model_plain: GraphSAGE-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.601
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-pool
    model_plain: GraphSAGE-pool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: AS-GCN
    model_plain: AS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.599
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GraphSAGE-mean
    model_plain: GraphSAGE-mean
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.598
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: SAGE (our implementation)
    model_plain: SAGE (our implementation)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.598
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-LSTM
    model_plain: GraphSAGE-LSTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.596
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.592
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: LADIES
    model_plain: LADIES
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.579
    - null
    - null
    - null
    metric_stds:
    - 0.003
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
    - 0.569
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
  - model: 2-Layer FNN
    model_plain: 2-Layer FNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5407
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
  - model: IA-GPL
    model_plain: IA-GPL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5313
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.529
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GPF-plus
    model_plain: GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5256
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.515
    - null
    - null
    - null
    metric_stds:
    - 0.006
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
    - 0.515
    - null
    - null
    - null
    metric_stds:
    - 0.008
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
    - 0.515
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.513
    - null
    - null
    - null
    metric_stds:
    - 0.032
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.513
    - null
    - null
    - null
    metric_stds:
    - 0.032
    - null
    - null
    - null
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5064
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-pool
    model_plain: GraphSAGE-pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.502
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-GCN
    model_plain: GraphSAGE-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Linear Probing
    model_plain: Linear Probing
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.497
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-mean
    model_plain: GraphSAGE-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.486
    - null
    - null
    - null
    metric_stds:
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
    - 0.484
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GraphSAGE-LSTM
    model_plain: GraphSAGE-LSTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.482
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.468
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GraphSAGE-GCN
    model_plain: GraphSAGE-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.465
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: Fine Tuning
    model_plain: Fine Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.4623
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: DCNN (our implementation)
    model_plain: DCNN (our implementation)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.462
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46
    - null
    - null
    - null
    metric_stds:
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
    - 0.4295
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: All-In-One
    model_plain: All-In-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.429
    - null
    - null
    - null
    metric_stds:
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
    - 0.4264
    - null
    - null
    - null
    metric_stds:
    - 0.003
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
    - 0.4256
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: MixHop
    model_plain: MixHop
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
    - 0.4252
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: Raw features
    model_plain: Raw features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.425
    - null
    - null
    - null
    metric_stds:
    - 0.003
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
    - 0.424
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
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
    - 0.4238
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
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
    - 0.4236
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: Raw features
    model_plain: Raw features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.422
    - null
    - null
    - null
    metric_stds:
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
    - 0.4087
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.4075
    - null
    - null
    - null
    metric_stds:
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
    - 0.4063
    - null
    - null
    - null
    metric_stds:
    - 0.013
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
    - 0.4038
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.3956
    - null
    - null
    - null
    metric_stds:
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
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.372
    - null
    - null
    - null
    metric_stds:
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
    - 0.312
    - null
    - null
    - null
    metric_stds:
    - 0.002
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
    - 0.306
    - null
    - null
    - null
    metric_stds:
    - 0.005
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
    - 0.281
    - null
    - null
    - null
    metric_stds:
    - 0.002
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
    - 0.263
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.769
    metric_stds:
    - null
    - null
    - null
    - 0.002
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.803
    metric_stds:
    - null
    - null
    - null
    - 0.005
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.783
    metric_stds:
    - null
    - null
    - null
    - 0.004
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.782
    metric_stds:
    - null
    - null
    - null
    - 0.01
  - model: P-GNN-F-1L
    model_plain: P-GNN-F-1L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.775
    metric_stds:
    - null
    - null
    - null
    - 0.029
  - model: P-GNN-E-2L
    model_plain: P-GNN-E-2L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.808
    metric_stds:
    - null
    - null
    - null
    - 0.003
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
    is_best: false
    metric_values:
    - null
    - null
    - 0.561
    - null
    metric_stds:
    - null
    - null
    - 0.059
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
    - null
    - null
    - 0.433
    - null
    metric_stds:
    - null
    - null
    - 0.034
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
    - null
    - null
    - 0.376
    - null
    metric_stds:
    - null
    - null
    - 0.017
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
    - null
    - null
    - 0.37
    - null
    metric_stds:
    - null
    - null
    - 0.022
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
    is_best: false
    metric_values:
    - null
    - null
    - 0.382
    - null
    metric_stds:
    - null
    - null
    - 0.031
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
    is_best: false
    metric_values:
    - null
    - null
    - 0.482
    - null
    metric_stds:
    - null
    - null
    - 0.062
    - null
  - model: GVP-GNN
    model_plain: GVP-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.03843'
    title: arXiv:2106.03843
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/drorlab/gvp-pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.866
    - null
    - null
    metric_stds:
    - null
    - 0.004
    - null
    - null
  - model: CNN
    model_plain: CNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.03843'
    title: arXiv:2106.03843
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/drorlab/gvp-pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.844
    - null
    - null
    metric_stds:
    - null
    - 0.002
    - null
    - null
  - model: GNN
    model_plain: GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.03843'
    title: arXiv:2106.03843
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/drorlab/gvp-pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.669
    - null
    - null
    metric_stds:
    - null
    - 0.001
    - null
    - null
  milestones:
  - value: 0.971
    std: 0.001
    model: GraphGPS
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
  - value: 0.9871
    std: 0.0002
    model: GaAN
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: 2018-03
  - value: 0.9956
    std: 0.0002
    model: GCNII
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: 2020-07
---

