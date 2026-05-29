---
title: Texas
slug: texas
benchmark: Heterophilic Graphs
task_type: node_classification
description: WebKB node classification on Texas university webpages (5 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.WebKB.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 5
result_count: 348
best_model:
  model: DoG (ACM-GCN)
  value: 0.966
  metric: Accuracy
  arxiv_id: '2503.12563'
  paper_title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
variants:
- slug: standard-split
  name: Standard split
  notes: Geom-GCN 10 fixed splits; results typically averaged.
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
  - model: DoG (ACM-GCN)
    model_plain: DoG (ACM-GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.966
    metric_stds:
    - 0.021
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.951
    metric_stds:
    - 0.032
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
    is_best: true
    metric_values:
    - 0.9443
    metric_stds:
    - 0.0256
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
    is_best: true
    metric_values:
    - 0.9295
    metric_stds:
    - 0.0284
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
    is_best: true
    metric_values:
    - 0.9295
    metric_stds:
    - 0.0221
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
    - 0.9292
    metric_stds:
    - 0.0061
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
    is_best: true
    metric_values:
    - 0.9279
    metric_stds:
    - 0.0295
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
    is_best: true
    metric_values:
    - 0.9279
    metric_stds:
    - 0.0304
  - model: DMD++
    model_plain: DMD++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.926
    metric_stds:
    - 0.034
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
    is_best: true
    metric_values:
    - 0.9246
    metric_stds:
    - 0.0447
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
    is_best: true
    metric_values:
    - 0.923
    metric_stds:
    - 0.0452
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
    - 0.9226
    metric_stds:
    - 0.0071
  - model: Our (APPNP) vs. APPNP
    model_plain: Our (APPNP) vs. APPNP
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
    - 0.9189
    metric_stds:
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
    is_best: true
    metric_values:
    - 0.9164
    metric_stds:
    - 0.0516
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
    - 0.9118
    metric_stds:
    - 0.007
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
    is_best: true
    metric_values:
    - 0.9049
    metric_stds:
    - 0.0572
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
    is_best: true
    metric_values:
    - 0.9016
    metric_stds:
    - 0.0469
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
    is_best: true
    metric_values:
    - 0.9
    metric_stds:
    - 0.0565
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
    - 0.8973
    metric_stds:
    - 0.0279
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
    is_best: true
    metric_values:
    - 0.897
    metric_stds:
    - 0.049
  - model: DMD-ACMP
    model_plain: DMD-ACMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.894
    metric_stds:
    - 0.038
  - model: Our (GCN) vs. GCN
    model_plain: Our (GCN) vs. GCN
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
    - 0.8919
    metric_stds:
    - null
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
    is_best: false
    metric_values:
    - 0.8909
    metric_stds:
    - 0.033
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
    - 0.8818
    metric_stds:
    - 0.022
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
    - 0.8818
    metric_stds:
    - 0.04
  - model: DL
    model_plain: DL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8784
    metric_stds:
    - 0.0
  - model: FMP ode
    model_plain: FMP ode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.876
    metric_stds:
    - 0.052
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8757
    metric_stds:
    - 0.0486
  - model: CSNN
    model_plain: CSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.873
    metric_stds:
    - 0.0593
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
    - 0.873
    metric_stds:
    - 0.0528
  - model: NewtonNet
    model_plain: NewtonNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8711
    metric_stds:
    - 0.038
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
    - 0.8703
    metric_stds:
    - 0.0236
  - model: Ours-Log
    model_plain: Ours-Log
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8703
    metric_stds:
    - 0.0524
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
    - 0.8676
    metric_stds:
    - 0.046
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
    - 0.8676
    metric_stds:
    - 0.0358
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
    - 0.8649
    metric_stds:
    - 0.0288
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8622
    metric_stds:
    - 0.0519
  - model: Conn-NSD
    model_plain: Conn-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8616
    metric_stds:
    - 0.022
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
    - 0.8608
    metric_stds:
    - 0.0096
  - model: O(d)-NSD
    model_plain: O(d)-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8595
    metric_stds:
    - 0.0551
  - model: AAGCN-N_H
    model_plain: AAGCN-N_H
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.857
    metric_stds:
    - 0.051
  - model: GraphSAGE + HR
    model_plain: GraphSAGE + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8568
    metric_stds:
    - 0.0272
  - model: Diag-NSD
    model_plain: Diag-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8567
    metric_stds:
    - 0.0695
  - model: GPNN
    model_plain: GPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8523
    metric_stds:
    - 0.064
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
    - 0.85
    metric_stds:
    - 0.023
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
    - 0.85
    metric_stds:
    - 0.02
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
    - 0.8486
    metric_stds:
    - 0.0677
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8486
    metric_stds:
    - 0.0677
  - model: GGCN
    model_plain: GGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8486
    metric_stds:
    - 0.046
  - model: H2GCN + HR
    model_plain: H2GCN + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8486
    metric_stds:
    - 0.0501
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8474
    metric_stds:
    - 0.031
  - model: ASGAT
    model_plain: ASGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.846
    metric_stds:
    - 0.058
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
    - 0.846
    metric_stds:
    - 0.0532
  - model: EGNN
    model_plain: EGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.10720'
    title: 'EIGNN: Efficient Infinite-Depth Graph Neural Networks'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.846
    metric_stds:
    - 0.0541
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8459
    metric_stds:
    - 0.0453
  - model: GRAFF
    model_plain: GRAFF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8432
    metric_stds:
    - 0.0551
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
    - 0.8421
    metric_stds:
    - 0.0088
  - model: DMD-GCN
    model_plain: DMD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.842
    metric_stds:
    - 0.026
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8417
    metric_stds:
    - 0.068
  - model: Ours-Expn
    model_plain: Ours-Expn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8406
    metric_stds:
    - 0.0459
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
    - 0.8405
    metric_stds:
    - 0.0411
  - model: GPRGNN + HR
    model_plain: GPRGNN + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8398
    metric_stds:
    - 0.0254
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
    - 0.8395
    metric_stds:
    - 0.0095
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
    - 0.8386
    metric_stds:
    - 0.028
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
    - 0.838
    metric_stds:
    - 0.0044
  - model: AAGCN
    model_plain: AAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.838
    metric_stds:
    - 0.055
  - model: GAT + HR
    model_plain: GAT + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8378
    metric_stds:
    - 0.0337
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
    - 0.8343
    metric_stds:
    - 0.0433
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
    - 0.832
    metric_stds:
    - 0.065
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
    - 0.8316
    metric_stds:
    - 0.0134
  - model: Gen-NSD
    model_plain: Gen-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8297
    metric_stds:
    - 0.0513
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
    - 0.8243
    metric_stds:
    - 0.0614
  - model: Framelets
    model_plain: Framelets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    metric_stds:
    - 0.025
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
    - 0.823
    metric_stds:
    - 0.057
  - model: EE-UFG
    model_plain: EE-UFG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    metric_stds:
    - 0.032
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
    - 0.822
    metric_stds:
    - 0.059
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
    - 0.8216
    metric_stds:
    - 0.06
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
    - 0.8216
    metric_stds:
    - 0.0528
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
    - 0.8212
    metric_stds:
    - 0.0772
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
    - 0.8211
    metric_stds:
    - 0.0115
  - model: DHGR \ feat_dist
    model_plain: DHGR \ feat_dist
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8202
    metric_stds:
    - 0.0106
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8178
    metric_stds:
    - 0.0089
  - model: HR
    model_plain: HR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8178
    metric_stds:
    - 0.0089
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
    - 0.817
    metric_stds:
    - 0.049
  - model: LLM-BP
    model_plain: LLM-BP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8166
    metric_stds:
    - null
  - model: APPNP + DHGR
    model_plain: APPNP + DHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8158
    metric_stds:
    - 0.0436
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
    - 0.814
    metric_stds:
    - 0.056
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
    - 0.8132
    metric_stds:
    - 0.0121
  - model: DMD-SGC
    model_plain: DMD-SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    metric_stds:
    - 0.025
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
    - 0.811
    metric_stds:
    - 0.042
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8108
    metric_stds:
    - 0.0382
  - model: GCNII + HR
    model_plain: GCNII + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8108
    metric_stds:
    - 0.0602
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
    - 0.81
    metric_stds:
    - 0.025
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
    - 0.808
    metric_stds:
    - 0.049
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
    - 0.805
    metric_stds:
    - 0.061
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
    - 0.803
    metric_stds:
    - 0.055
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
    - 0.8
    metric_stds:
    - 0.048
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
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.04
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
    - 0.8
    metric_stds:
    - 0.03
  - model: FB-GCN-N_A
    model_plain: FB-GCN-N_A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    metric_stds:
    - 0.022
  - model: DHGR \ label_dist
    model_plain: DHGR \ label_dist
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7967
    metric_stds:
    - 0.0179
  - model: LLM-BP (appr.)
    model_plain: LLM-BP (appr.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7939
    metric_stds:
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
    - 0.7937
    metric_stds:
    - 0.027
  - model: UFG
    model_plain: UFG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    metric_stds:
    - 0.028
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
    - 0.792
    metric_stds:
    - 0.03
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
    - 0.7903
    metric_stds:
    - 0.012
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
    - 0.7887
    metric_stds:
    - 0.0086
  - model: GCL-LR-Attention
    model_plain: GCL-LR-Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    metric_stds:
    - 0.018
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
    - 0.784
    metric_stds:
    - 0.032
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
    - 0.7838
    metric_stds:
    - 0.0221
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
    - 0.7838
    metric_stds:
    - 0.0637
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
    - 0.7838
    metric_stds:
    - null
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
    - 0.7837
    metric_stds:
    - 0.0601
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
    - 0.783
    metric_stds:
    - 0.08
  - model: GCL-LRR
    model_plain: GCL-LRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    metric_stds:
    - 0.013
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
    - 0.7784
    metric_stds:
    - 0.0773
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
    - 0.7784
    metric_stds:
    - 0.0781
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
    is_best: false
    metric_values:
    - 0.7784
    metric_stds:
    - null
  - model: CO-GNN
    model_plain: CO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7757
    metric_stds:
    - 0.0541
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
    - 0.7748
    metric_stds:
    - 0.0127
  - model: SeHGNN + TAGs (8b)
    model_plain: SeHGNN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7745
    metric_stds:
    - 0.0115
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
    - 0.771
    metric_stds:
    - 0.083
  - model: TEDGCN
    model_plain: TEDGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    metric_stds:
    - 0.025
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
    - 0.767
    metric_stds:
    - 0.0277
  - model: LLM2Vec
    model_plain: LLM2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7668
    metric_stds:
    - null
  - model: GFMate
    model_plain: GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7663
    metric_stds:
    - 0.0781
  - model: LP+FT +GFMate
    model_plain: LP+FT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7663
    metric_stds:
    - 0.0781
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    metric_stds:
    - null
  - model: UniMP + TAGs (8b)
    model_plain: UniMP + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7647
    metric_stds:
    - 0.0173
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
    - 0.762
    metric_stds:
    - 0.046
  - model: MDGPT +GFMate
    model_plain: MDGPT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7589
    metric_stds:
    - 0.096
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
    - 0.7574
    metric_stds:
    - 0.0161
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    metric_stds:
    - 0.033
  - model: FB-GCN
    model_plain: FB-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    metric_stds:
    - 0.048
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
    - 0.7568
    metric_stds:
    - 0.0221
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
    - 0.7553
    metric_stds:
    - 0.0116
  - model: Text-Embedding-3-Large
    model_plain: Text-Embedding-3-Large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7542
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.7516
    metric_stds:
    - 0.0096
  - model: DGI+FT +GFMate
    model_plain: DGI+FT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    metric_stds:
    - 0.0997
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
    - 0.7478
    metric_stds:
    - 0.0127
  - model: GIN + TAGs (8b)
    model_plain: GIN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7451
    metric_stds:
    - 0.0213
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
    - 0.744
    metric_stds:
    - 0.06
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
    - 0.7387
    metric_stds:
    - 0.0637
  - model: RGCN + TAGs (8b)
    model_plain: RGCN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7353
    metric_stds:
    - 0.0142
  - model: FAGCN
    model_plain: FAGCN
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
    - 0.7297
    metric_stds:
    - null
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
    - 0.7297
    metric_stds:
    - 0.0339
  - model: HAN + TAGs (8b)
    model_plain: HAN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7294
    metric_stds:
    - 0.0164
  - model: HAN + TAGs (70b)
    model_plain: HAN + TAGs (70b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7294
    metric_stds:
    - 0.0158
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
    - 0.7207
    metric_stds:
    - 0.0337
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
    - 0.72
    metric_stds:
    - 0.074
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
    - 0.7162
    metric_stds:
    - null
  - model: SeHGNN
    model_plain: SeHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7137
    metric_stds:
    - 0.0128
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
    - 0.713
    metric_stds:
    - 0.057
  - model: UniMP
    model_plain: UniMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7118
    metric_stds:
    - 0.02
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
    - 0.7046
    metric_stds:
    - 0.0161
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
    - 0.7042
    metric_stds:
    - null
  - model: SDRF
    model_plain: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7035
    metric_stds:
    - 0.006
  - model: GRIT
    model_plain: GRIT
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
    - 0.7027
    metric_stds:
    - 0.0382
  - model: DeepGCNs
    model_plain: DeepGCNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7027
    metric_stds:
    - 0.071
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
    - 0.7027
    metric_stds:
    - 0.0493
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
    - 0.7027
    metric_stds:
    - 0.0709
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
    - 0.7021
    metric_stds:
    - 0.0232
  - model: GCL+FT +GFMate
    model_plain: GCL+FT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6982
    metric_stds:
    - 0.1136
  - model: FAGCN
    model_plain: FAGCN
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
    - 0.697
    metric_stds:
    - 0.0141
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
    - 0.6962
    metric_stds:
    - 0.0666
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
    - 0.6956
    metric_stds:
    - 0.0171
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
    - 0.695
    metric_stds:
    - 0.065
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
    - 0.6937
    metric_stds:
    - 0.0255
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6937
    metric_stds:
    - 0.0127
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6882
    metric_stds:
    - 0.0212
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
    - 0.688
    metric_stds:
    - 0.0157
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6863
    metric_stds:
    - 0.0173
  - model: DAGPrompt
    model_plain: DAGPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6827
    metric_stds:
    - 0.1002
  - model: DHGR \ feat_self
    model_plain: DHGR \ feat_self
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6785
    metric_stds:
    - 0.0102
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
    - 0.6784
    metric_stds:
    - 0.0475
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
    - 0.6784
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
    - 0.676
    metric_stds:
    - null
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
    - 0.6757
    metric_stds:
    - null
  - model: Our (SGC) vs. SGC
    model_plain: Our (SGC) vs. SGC
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
    - 0.6757
    metric_stds:
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6757
    metric_stds:
    - 0.0585
  - model: Auto-HeG
    model_plain: Auto-HeG
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
    - 0.674
    metric_stds:
    - 0.0165
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
    - 0.672
    metric_stds:
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6686
    metric_stds:
    - 0.0148
  - model: SAMGPT
    model_plain: SAMGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6679
    metric_stds:
    - 0.1077
  - model: RandDropEdge
    model_plain: RandDropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6676
    metric_stds:
    - 0.0152
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
    - 0.6667
    metric_stds:
    - 0.0337
  - model: MO-SFL
    model_plain: MO-SFL
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
    - 0.665
    metric_stds:
    - null
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
    - 0.6649
    metric_stds:
    - 0.0664
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
    - 0.664
    metric_stds:
    - 0.057
  - model: H2GCN
    model_plain: H2GCN
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
    - 0.663
    metric_stds:
    - 0.046
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
    - 0.6622
    metric_stds:
    - 0.1062
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
    - 0.6594
    metric_stds:
    - 0.0413
  - model: ACMGCN
    model_plain: ACMGCN
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
    - 0.659
    metric_stds:
    - 0.0152
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6588
    metric_stds:
    - 0.0186
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
    - 0.658
    metric_stds:
    - 0.05
  - model: APPNP
    model_plain: APPNP
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
    - 0.6541
    metric_stds:
    - null
  - model: CL
    model_plain: CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6531
    metric_stds:
    - 0.0129
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
    - 0.653
    metric_stds:
    - 0.0146
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
    - 0.6523
    metric_stds:
    - null
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
    - 0.65
    metric_stds:
    - 0.012
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
    - 0.6486
    metric_stds:
    - null
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6476
    metric_stds:
    - 0.1484
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6458
    metric_stds:
    - null
  - model: SF
    model_plain: SF
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
    - 0.642
    metric_stds:
    - null
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
    - 0.638
    metric_stds:
    - 0.0111
  - model: All-In-One
    model_plain: All-In-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6379
    metric_stds:
    - 0.1591
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.10720'
    title: 'EIGNN: Efficient Infinite-Depth Graph Neural Networks'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6378
    metric_stds:
    - 0.063
  - model: Node2Seq
    model_plain: Node2Seq
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
    metric_stds:
    - 0.061
  - model: GPT-4o
    model_plain: GPT-4o
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.631
    metric_stds:
    - null
  - model: GREET
    model_plain: GREET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6279
    metric_stds:
    - 0.0257
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
    - 0.627
    metric_stds:
    - 0.0552
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
    - 0.625
    metric_stds:
    - 0.0121
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6245
    metric_stds:
    - 0.0296
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6243
    metric_stds:
    - 0.0737
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6225
    metric_stds:
    - null
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
    - 0.6216
    metric_stds:
    - 0.0705
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
    - 0.6211
    metric_stds:
    - 0.0153
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6196
    metric_stds:
    - 0.0127
  - model: GRACEIS
    model_plain: GRACEIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.619
    metric_stds:
    - 0.024
  - model: CGC
    model_plain: CGC
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
    - 0.615
    metric_stds:
    - null
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
    - 0.614
    metric_stds:
    - 0.008
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
    - 0.6135
    metric_stds:
    - 0.0125
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
    - 0.6126
    metric_stds:
    - 0.0127
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
    - 0.612
    metric_stds:
    - 0.076
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
    - 0.612
    metric_stds:
    - 0.009
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6082
    metric_stds:
    - 0.0249
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
    - 0.6081
    metric_stds:
    - 0.0487
  - model: GPRGNN
    model_plain: GPRGNN
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
    - 0.607
    metric_stds:
    - 0.0128
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
    - 0.606
    metric_stds:
    - 0.039
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
    - 0.6036
    metric_stds:
    - 0.0255
  - model: PairNorm
    model_plain: PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.603
    metric_stds:
    - 0.043
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
    - 0.603
    metric_stds:
    - 0.063
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
    - 0.602
    metric_stds:
    - 0.03
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
    - 0.602
    metric_stds:
    - 0.024
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
    - 0.601
    metric_stds:
    - 0.009
  - model: RandAddEdge_train
    model_plain: RandAddEdge_train
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6008
    metric_stds:
    - 0.0213
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    metric_stds:
    - 0.0027
  - model: CDRS
    model_plain: CDRS
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
    - 0.599
    metric_stds:
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
    - 0.5979
    metric_stds:
    - 0.0171
  - model: MDGPT
    model_plain: MDGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5976
    metric_stds:
    - 0.1244
  - model: Geom-GCN
    model_plain: Geom-GCN
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
    - 0.5973
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
    - 0.5946
    metric_stds:
    - 0.0525
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
    - 0.5946
    metric_stds:
    - null
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
    - 0.5946
    metric_stds:
    - 0.0436
  - model: N-GCN_a
    model_plain: N-GCN_a
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.592
    metric_stds:
    - 0.055
  - model: BGRL
    model_plain: BGRL
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
    - 0.5919
    metric_stds:
    - 0.0585
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
    - 0.59
    metric_stds:
    - 0.048
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
    - 0.5892
    metric_stds:
    - 0.0432
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
    - 0.589
    metric_stds:
    - 0.026
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
    - 0.588
    metric_stds:
    - null
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5875
    metric_stds:
    - 0.0557
  - model: RiemannGFM
    model_plain: RiemannGFM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.586
    metric_stds:
    - 0.1527
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5857
    metric_stds:
    - 0.021
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
    - 0.5856
    metric_stds:
    - 0.0177
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
    - 0.5838
    metric_stds:
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.10720'
    title: 'EIGNN: Efficient Infinite-Depth Graph Neural Networks'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5837
    metric_stds:
    - 0.0582
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
    - 0.5792
    metric_stds:
    - null
  - model: Incep(Drop)
    model_plain: Incep(Drop)
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
    - 0.5784
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
    - 0.578
    metric_stds:
    - 0.041
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
    - 0.577
    metric_stds:
    - 0.036
  - model: GRACE
    model_plain: GRACE
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
    - 0.5757
    metric_stds:
    - 0.0568
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
    - 0.5757
    metric_stds:
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
    - 0.575
    metric_stds:
    - null
  - model: JKNet(Drop)
    model_plain: JKNet(Drop)
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
    - 0.573
    metric_stds:
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
    - 0.5718
    metric_stds:
    - 0.0164
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
    - 0.569
    metric_stds:
    - 0.036
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
    - 0.5684
    metric_stds:
    - 0.0161
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
    - 0.5683
    metric_stds:
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
    - 0.5649
    metric_stds:
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
    - 0.563
    metric_stds:
    - 0.0161
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
    - 0.5622
    metric_stds:
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
    - 0.5619
    metric_stds:
    - 0.0161
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5619
    metric_stds:
    - 0.0216
  - model: GPT-3.5-turbo
    model_plain: GPT-3.5-turbo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5614
    metric_stds:
    - null
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
    - 0.561
    metric_stds:
    - 0.002
  - model: SBert + NA
    model_plain: SBert + NA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5604
    metric_stds:
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
    - 0.5593
    metric_stds:
    - 0.0176
  - model: RandAddEdge
    model_plain: RandAddEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5585
    metric_stds:
    - 0.0168
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
    - 0.558
    metric_stds:
    - 0.043
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
    - 0.5574
    metric_stds:
    - null
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
    - 0.5568
    metric_stds:
    - 0.0571
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
    - 0.5546
    metric_stds:
    - null
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
    - 0.5524
    metric_stds:
    - 0.0604
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
    - 0.5486
    metric_stds:
    - 0.0698
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
    - 0.5405
    metric_stds:
    - 0.0
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
    - 0.538
    metric_stds:
    - 0.012
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
    - 0.535
    metric_stds:
    - 0.03
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5348
    metric_stds:
    - null
  - model: BRIDGE
    model_plain: BRIDGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5335
    metric_stds:
    - 0.119
  - model: Sparse PCA
    model_plain: Sparse PCA
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
    - 0.533
    metric_stds:
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5327
    metric_stds:
    - 0.0995
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
    - 0.531
    metric_stds:
    - 0.039
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
    - 0.5263
    metric_stds:
    - 0.0148
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
    - 0.5216
    metric_stds:
    - null
  - model: SVD
    model_plain: SVD
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
    - 0.51
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
    - 0.5049
    metric_stds:
    - null
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
    - 0.5049
    metric_stds:
    - 0.0221
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
    - 0.504
    metric_stds:
    - 0.035
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
    - 0.5026
    metric_stds:
    - 0.0161
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
    - 0.4973
    metric_stds:
    - null
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
    - 0.492
    metric_stds:
    - 0.044
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
    - 0.488
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
    - 0.4837
    metric_stds:
    - 0.0875
  - model: ProNoG
    model_plain: ProNoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4825
    metric_stds:
    - 0.096
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
    - 0.476
    metric_stds:
    - 0.007
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4734
    metric_stds:
    - 0.1272
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
    - 0.4595
    metric_stds:
    - 0.0158
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
    - 0.4404
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
    - 0.4202
    metric_stds:
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4038
    metric_stds:
    - 0.0821
  - model: GOFA
    model_plain: GOFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3837
    metric_stds:
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
    - 0.3784
    metric_stds:
    - 0.0221
  - model: GPR
    model_plain: GPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.376
    metric_stds:
    - 0.0954
  - model: LP+FT
    model_plain: LP+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3693
    metric_stds:
    - 0.119
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
    - 0.3519
    metric_stds:
    - null
  - model: DGI+FT
    model_plain: DGI+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3446
    metric_stds:
    - 0.1292
  - model: SimGRACE SpikingGPF
    model_plain: SimGRACE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3354
    metric_stds:
    - 0.1378
  - model: GraphCL SpikingGPF
    model_plain: GraphCL SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.318
    metric_stds:
    - 0.1583
  - model: EdgePred All-in-One
    model_plain: EdgePred All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3168
    metric_stds:
    - 0.1838
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2944
    metric_stds:
    - 0.1481
  - model: EdgePred SpikingGPF
    model_plain: EdgePred SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2932
    metric_stds:
    - 0.1462
  - model: GCL+FT
    model_plain: GCL+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2881
    metric_stds:
    - 0.1532
  - model: EdgePred GPF
    model_plain: EdgePred GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2845
    metric_stds:
    - 0.1742
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2832
    metric_stds:
    - 0.147
  - model: SimGRACE GPF
    model_plain: SimGRACE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2758
    metric_stds:
    - 0.1799
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2733
    metric_stds:
    - 0.1479
  - model: GraphCL GPF
    model_plain: GraphCL GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2733
    metric_stds:
    - 0.1654
  - model: SimGRACE Fine-Tuning
    model_plain: SimGRACE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2733
    metric_stds:
    - 0.1451
  - model: GraphMAE All-in-One
    model_plain: GraphMAE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2658
    metric_stds:
    - 0.1831
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2646
    metric_stds:
    - 0.1907
  - model: GraphCL GPF-plus
    model_plain: GraphCL GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2634
    metric_stds:
    - 0.1775
  - model: GraphMAE GPF
    model_plain: GraphMAE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2596
    metric_stds:
    - 0.1622
  - model: GraphMAE SpikingGPF
    model_plain: GraphMAE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2596
    metric_stds:
    - 0.1561
  - model: EdgePred GPF-plus
    model_plain: EdgePred GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2547
    metric_stds:
    - 0.1758
  - model: GraphMAE GPF-plus
    model_plain: GraphMAE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2534
    metric_stds:
    - 0.1808
  - model: GraphCL All-in-One
    model_plain: GraphCL All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2522
    metric_stds:
    - 0.0604
  - model: GraphCL Fine-Tuning
    model_plain: GraphCL Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2509
    metric_stds:
    - 0.1661
  - model: SimGRACE GPF-plus
    model_plain: SimGRACE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2497
    metric_stds:
    - 0.154
  - model: GraphMAE Fine-Tuning
    model_plain: GraphMAE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2497
    metric_stds:
    - 0.1728
  - model: SimGRACE All-in-One
    model_plain: SimGRACE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2447
    metric_stds:
    - 0.1138
  - model: UniGLM
    model_plain: UniGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2139
    metric_stds:
    - null
  - model: EdgePred Fine-Tuning
    model_plain: EdgePred Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2075
    metric_stds:
    - 0.1428
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1848
    metric_stds:
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1765
    metric_stds:
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1551
    metric_stds:
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1177
    metric_stds:
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1123
    metric_stds:
    - null
  - model: Average Reduction
    model_plain: Average Reduction
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.09041'
    title: Graph Neural Networks with Diverse Spectral Filtering
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jingweio/DSF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0784
    metric_stds:
    - null
  milestones:
  - value: 0.7162
    std: null
    model: Geom-GCN-I-g
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: 2020-02
  - value: 0.7784
    std: null
    model: GCNII
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: 2020-07
  - value: 0.873
    std: 0.0528
    model: simple GNN model (3-hop)
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: 2021-05
  - value: 0.9292
    std: 0.0061
    model: GPRGNN
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: 2022-02
  - value: 0.966
    std: 0.021
    model: DoG (ACM-GCN)
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: 2025-03
---

