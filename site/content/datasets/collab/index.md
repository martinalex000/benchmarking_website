---
title: COLLAB
slug: collab
benchmark: TU Dortmund
task_type: graph_classification
description: Graph classification of scientific collaboration networks (3 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 5000
  avg_nodes: 74.5
  avg_edges: 2457.8
  num_classes: 2
result_count: 253
best_model:
  model: novel dynamic message-passing mechanism
  value: 0.8672
  metric: Accuracy
  arxiv_id: '2410.23686'
  paper_title: Towards Dynamic Message Passing on Graphs
variants:
- slug: 10-fold-cv
  name: 10-fold CV
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
  rows:
  - model: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8672
    - null
    metric_stds:
    - 0.0162
    - null
  - model: CoCN
    model_plain: CoCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8615
    - null
    metric_stds:
    - 0.001
    - null
  - model: PXGL-GNN
    model_plain: PXGL-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8396
    - null
    metric_stds:
    - 0.0159
    - null
  - model: GFL-att
    model_plain: GFL-att
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8379
    - null
    metric_stds:
    - 0.0039
    - null
  - model: GNTK
    model_plain: GNTK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.836
    - null
    metric_stds:
    - 0.01
    - null
  - model: GFL-mean
    model_plain: GFL-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8351
    - null
    metric_stds:
    - 0.0038
    - null
  - model: SE2P-C3
    model_plain: SE2P-C3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.835
    - null
    metric_stds:
    - 0.017
    - null
  - model: SE2P-C2
    model_plain: SE2P-C2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.833
    - null
    metric_stds:
    - 0.021
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
    - 0.83
    - null
    metric_stds:
    - 0.0143
    - null
  - model: EGG
    model_plain: EGG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8294
    - null
    metric_stds:
    - 0.0106
    - null
  - model: GraphAug
    model_plain: GraphAug
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    metric_stds:
    - 0.002
    - null
  - model: CapsNets
    model_plain: CapsNets
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8286
    - null
    metric_stds:
    - 0.0181
    - null
  - model: SE2P-C4
    model_plain: SE2P-C4
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    metric_stds:
    - 0.021
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
    - 0.828
    - null
    metric_stds:
    - 0.014
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8273
    - null
    metric_stds:
    - 0.0192
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
    - 0.824
    - null
    metric_stds:
    - 0.016
    - null
  - model: S2GAE
    model_plain: S2GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8235
    - null
    metric_stds:
    - 0.0234
    - null
  - model: MAX
    model_plain: MAX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8228
    - null
    metric_stds:
    - 0.021
    - null
  - model: gPool
    model_plain: gPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8225
    - null
    metric_stds:
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8213
    - null
    metric_stds:
    - 0.0043
    - null
  - model: DiffPool-Det
    model_plain: DiffPool-Det
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8213
    - null
    metric_stds:
    - null
    - null
  - model: ExpC-s
    model_plain: ExpC-s
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    metric_stds:
    - 0.016
    - null
  - model: CombC
    model_plain: CombC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    metric_stds:
    - 0.0175
    - null
  - model: AGFormer(GCN)
    model_plain: AGFormer(GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8188
    - null
    metric_stds:
    - 0.0098
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8172
    - null
    metric_stds:
    - 0.0164
    - null
  - model: M-Evolve (GCS)
    model_plain: M-Evolve (GCS)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.817
    - null
    metric_stds:
    - 0.011
    - null
  - model: GraphTrans (GIN)
    model_plain: GraphTrans (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8168
    - null
    metric_stds:
    - 0.0173
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
    - 0.8166
    - null
    metric_stds:
    - 0.0012
    - null
  - model: Uniform PerturbEdge
    model_plain: Uniform PerturbEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    metric_stds:
    - 0.003
    - null
  - model: DropN (GCS)
    model_plain: DropN (GCS)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    metric_stds:
    - 0.008
    - null
  - model: PermE (GCS)
    model_plain: PermE (GCS)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    metric_stds:
    - 0.006
    - null
  - model: Attention
    model_plain: Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8158
    - null
    metric_stds:
    - 0.0172
    - null
  - model: Uniform MaskNF
    model_plain: Uniform MaskNF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    metric_stds:
    - 0.002
    - null
  - model: Uniform DropNode
    model_plain: Uniform DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    metric_stds:
    - 0.004
    - null
  - model: Uniform Mixture
    model_plain: Uniform Mixture
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    metric_stds:
    - 0.003
    - null
  - model: GFN
    model_plain: GFN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    metric_stds:
    - 0.0242
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
    - 0.815
    - null
    metric_stds:
    - 0.02
    - null
  - model: ICL
    model_plain: ICL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8145
    - null
    metric_stds:
    - 0.0121
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
    - 0.814
    - null
    metric_stds:
    - 0.021
    - null
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8138
    - null
    metric_stds:
    - 0.0142
    - null
  - model: QGNN
    model_plain: QGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8136
    - null
    metric_stds:
    - 0.0131
    - null
  - model: GFN-light
    model_plain: GFN-light
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8134
    - null
    metric_stds:
    - 0.0173
    - null
  - model: Graph Transplant_DP (GCS)
    model_plain: Graph Transplant_DP (GCS)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    - null
    metric_stds:
    - 0.01
    - null
  - model: Graph Transplant_EP (GIN)
    model_plain: Graph Transplant_EP (GIN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    - null
    metric_stds:
    - 0.009
    - null
  - model: SEP
    model_plain: SEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8128
    - null
    metric_stds:
    - 0.0015
    - null
  - model: SubGNN
    model_plain: SubGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8126
    - null
    metric_stds:
    - 0.0153
    - null
  - model: AVG
    model_plain: AVG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8124
    - null
    metric_stds:
    - 0.0134
    - null
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    metric_stds:
    - 0.003
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    metric_stds:
    - 0.014
    - null
  - model: SubG (GCS)
    model_plain: SubG (GCS)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    metric_stds:
    - 0.01
    - null
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8118
    - null
    metric_stds:
    - 0.0089
    - null
  - model: M-Mixup
    model_plain: M-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.811
    - null
    metric_stds:
    - 0.005
    - null
  - model: G-Mixup
    model_plain: G-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.811
    - null
    metric_stds:
    - 0.009
    - null
  - model: PG
    model_plain: PG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.809
    - null
    metric_stds:
    - 0.008
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
    - 0.809
    - null
    metric_stds:
    - 0.003
    - null
  - model: M-Evolve (GIN)
    model_plain: M-Evolve (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.809
    - null
    metric_stds:
    - 0.007
    - null
  - model: PermE (GIN)
    model_plain: PermE (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.809
    - null
    metric_stds:
    - 0.008
    - null
  - model: M-Evolve (GAT)
    model_plain: M-Evolve (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.809
    - null
    metric_stds:
    - 0.008
    - null
  - model: Matchingnet
    model_plain: Matchingnet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8087
    - null
    metric_stds:
    - 0.0076
    - null
  - model: SUM
    model_plain: SUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8076
    - null
    metric_stds:
    - 0.0156
    - null
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8074
    - null
    metric_stds:
    - 0.0054
    - null
  - model: WL-OA
    model_plain: WL-OA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8074
    - null
    metric_stds:
    - null
    - null
  - model: GMTPool
    model_plain: GMTPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8074
    - null
    metric_stds:
    - 0.0054
    - null
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
    is_best: false
    metric_values:
    - 0.807
    - null
    metric_stds:
    - 0.0074
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
    - 0.807
    - null
    metric_stds:
    - 0.029
    - null
  - model: DropGIN
    model_plain: DropGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.807
    - null
    metric_stds:
    - 0.014
    - null
  - model: No augmentation
    model_plain: No augmentation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    metric_stds:
    - 0.003
    - null
  - model: RetGK_I
    model_plain: RetGK_I
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    metric_stds:
    - 0.003
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
    - 0.806
    - null
    metric_stds:
    - 0.006
    - null
  - model: ASAP
    model_plain: ASAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8052
    - null
    metric_stds:
    - null
    - null
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    metric_stds:
    - 0.007
    - null
  - model: Manifold-Mixup
    model_plain: Manifold-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    metric_stds:
    - 0.01
    - null
  - model: SubG (GIN)
    model_plain: SubG (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    metric_stds:
    - 0.01
    - null
  - model: ProtoNet
    model_plain: ProtoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8049
    - null
    metric_stds:
    - 0.0055
    - null
  - model: GAT + Vanilla
    model_plain: GAT + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    metric_stds:
    - 0.013
    - null
  - model: PermE (GAT)
    model_plain: PermE (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    metric_stds:
    - 0.009
    - null
  - model: FLAG
    model_plain: FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    metric_stds:
    - 0.006
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    - null
    metric_stds:
    - 0.019
    - null
  - model: GIN-0
    model_plain: GIN-0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    - null
    metric_stds:
    - 0.019
    - null
  - model: DropN (GAT)
    model_plain: DropN (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    - null
    metric_stds:
    - 0.012
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
    - 0.801
    - null
    metric_stds:
    - 0.016
    - null
  - model: InfoGCL
    model_plain: InfoGCL
    is_baseline: true
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
    - 0.8
    - null
    metric_stds:
    - 0.013
    - null
  - model: PSAGNN
    model_plain: PSAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7994
    - null
    metric_stds:
    - 0.0183
    - null
  - model: JOAOv2
    model_plain: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7988
    - null
    metric_stds:
    - 0.0017
    - null
  - model: SE2P-C1
    model_plain: SE2P-C1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    metric_stds:
    - 0.015
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
    - 0.798
    - null
    metric_stds:
    - 0.009
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    metric_stds:
    - 0.017
    - null
  - model: CapsGNN
    model_plain: CapsGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7962
    - null
    metric_stds:
    - 0.0091
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
    - 0.796
    - null
    metric_stds:
    - 0.005
    - null
  - model: MAML
    model_plain: MAML
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7937
    - null
    metric_stds:
    - 0.0041
    - null
  - model: SubG (GAT)
    model_plain: SubG (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    metric_stds:
    - 0.008
    - null
  - model: AttPool-global
    model_plain: AttPool-global
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7912
    - null
    metric_stds:
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7902
    - null
    metric_stds:
    - 0.0177
    - null
  - model: GMT
    model_plain: GMT
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
    - 0.7894
    - null
    metric_stds:
    - 0.0044
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
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
    - 0.789
    - null
    metric_stds:
    - 0.023
    - null
  - model: GCC
    model_plain: GCC
    is_baseline: true
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
    - 0.789
    - null
    metric_stds:
    - null
    - null
  - model: WL subtree
    model_plain: WL subtree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    metric_stds:
    - 0.019
    - null
  - model: Graphormer
    model_plain: Graphormer
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
    - 0.7882
    - null
    metric_stds:
    - 0.0121
    - null
  - model: Graph-ViT
    model_plain: Graph-ViT
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
    - 0.7879
    - null
    metric_stds:
    - 0.0074
    - null
  - model: GLA
    model_plain: GLA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7878
    - null
    metric_stds:
    - 0.0012
    - null
  - model: SimGRACE
    model_plain: SimGRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7866
    - null
    metric_stds:
    - 0.0024
    - null
  - model: 1-WL
    model_plain: 1-WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7861
    - null
    metric_stds:
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
    - 0.786
    - null
    metric_stds:
    - 0.005
    - null
  - model: SAT
    model_plain: SAT
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
    - 0.7835
    - null
    metric_stds:
    - 0.0085
    - null
  - model: IGN
    model_plain: IGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    metric_stds:
    - 0.025
    - null
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7822
    - null
    metric_stds:
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
    - 0.781
    - null
    metric_stds:
    - 0.012
    - null
  - model: IEGN
    model_plain: IEGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7792
    - null
    metric_stds:
    - 0.017
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.779
    - null
    metric_stds:
    - 0.002
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7784
    - null
    metric_stds:
    - 0.0148
    - null
  - model: GCAPS-CNN
    model_plain: GCAPS-CNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7771
    - null
    metric_stds:
    - 0.0251
    - null
  - model: GCAPS
    model_plain: GCAPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7771
    - null
    metric_stds:
    - 0.0251
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
    - 0.776
    - null
    metric_stds:
    - 0.05
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
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
    - 0.7759
    - null
    metric_stds:
    - 0.0022
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7759
    - null
    metric_stds:
    - 0.0224
    - null
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7758
    - null
    metric_stds:
    - 0.0085
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
    - 0.7756
    - null
    metric_stds:
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
    - 0.775
    - null
    metric_stds:
    - 0.052
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7746
    - null
    metric_stds:
    - 0.0011
    - null
  - model: GIN + GTR
    model_plain: GIN + GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7745
    - null
    metric_stds:
    - 0.0039
    - null
  - model: GPS
    model_plain: GPS
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
    - 0.7741
    - null
    metric_stds:
    - 0.0056
    - null
  - model: WLSK
    model_plain: WLSK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7739
    - null
    metric_stds:
    - 0.0035
    - null
  - model: GNN-AK
    model_plain: GNN-AK
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
    - 0.7735
    - null
    metric_stds:
    - 0.0093
    - null
  - model: AgentNet
    model_plain: AgentNet
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
    - 0.773
    - null
    metric_stds:
    - 0.0198
    - null
  - model: Infomax
    model_plain: Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    metric_stds:
    - 0.0019
    - null
  - model: StructPool
    model_plain: StructPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7727
    - null
    metric_stds:
    - 0.0051
    - null
  - model: R-GIN + FoSR
    model_plain: R-GIN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.772
    - null
    metric_stds:
    - 0.0038
    - null
  - model: CRaWl
    model_plain: CRaWl
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
    - 0.7717
    - null
    metric_stds:
    - 0.0078
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    metric_stds:
    - 0.0084
    - null
  - model: R-GIN + SDRF
    model_plain: R-GIN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7648
    - null
    metric_stds:
    - 0.0039
    - null
  - model: All-Graph-Finetune (AGF)
    model_plain: All-Graph-Finetune (AGF)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7609
    - null
    metric_stds:
    - 0.0056
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    metric_stds:
    - 0.016
    - null
  - model: PANPool
    model_plain: PANPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7578
    - null
    metric_stds:
    - 0.0203
    - null
  - model: GLN
    model_plain: GLN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7572
    - null
    metric_stds:
    - 0.0251
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
    - 0.757
    - null
    metric_stds:
    - 0.045
    - null
  - model: DiffPool-NoLP
    model_plain: DiffPool-NoLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7558
    - null
    metric_stds:
    - null
    - null
  - model: R-GIN + None
    model_plain: R-GIN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7554
    - null
    metric_stds:
    - 0.0032
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
    - 0.755
    - null
    metric_stds:
    - 0.0058
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7548
    - null
    metric_stds:
    - null
    - null
  - model: R-GIN + Last FA
    model_plain: R-GIN + Last FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7543
    - null
    metric_stds:
    - 0.0049
    - null
  - model: R-GIN + Every FA
    model_plain: R-GIN + Every FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7543
    - null
    metric_stds:
    - 0.0048
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7528
    - null
    metric_stds:
    - 0.0012
    - null
  - model: EdgePool
    model_plain: EdgePool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7509
    - null
    metric_stds:
    - 0.0081
    - null
  - model: PNA
    model_plain: PNA
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
    - 0.7473
    - null
    metric_stds:
    - 0.0109
    - null
  - model: AutoGCL
    model_plain: AutoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    - null
    metric_stds:
    - 0.002
    - null
  - model: SAN
    model_plain: SAN
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
    - 0.7445
    - null
    metric_stds:
    - 0.0246
    - null
  - model: GCN + GTR
    model_plain: GCN + GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7434
    - null
    metric_stds:
    - 0.0041
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    metric_stds:
    - 0.018
    - null
  - model: GIN0
    model_plain: GIN0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    - null
    metric_stds:
    - 0.016
    - null
  - model: HAP
    model_plain: HAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7395
    - null
    metric_stds:
    - null
    - null
  - model: AWE
    model_plain: AWE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7393
    - null
    metric_stds:
    - 0.0194
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    - null
    metric_stds:
    - 0.017
    - null
  - model: AWL
    model_plain: AWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    - null
    metric_stds:
    - 0.019
    - null
  - model: SortPool
    model_plain: SortPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7376
    - null
    metric_stds:
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7376
    - null
    metric_stds:
    - 0.0049
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
    - 0.732
    - null
    metric_stds:
    - 0.049
    - null
  - model: DGK
    model_plain: DGK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7309
    - null
    metric_stds:
    - 0.0025
    - null
  - model: SortPooling
    model_plain: SortPooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7294
    - null
    metric_stds:
    - null
    - null
  - model: GK
    model_plain: GK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7284
    - null
    metric_stds:
    - 0.0028
    - null
  - model: SumPool
    model_plain: SumPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7283
    - null
    metric_stds:
    - null
    - null
  - model: MeanAttPool
    model_plain: MeanAttPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7265
    - null
    metric_stds:
    - null
    - null
  - model: PATCHY-SAN
    model_plain: PATCHY-SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    - null
    metric_stds:
    - null
    - null
  - model: PSCN
    model_plain: PSCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    - null
    metric_stds:
    - 0.0215
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
    - 0.723
    - null
    metric_stds:
    - 0.048
    - null
  - model: GCN + EdgePool
    model_plain: GCN + EdgePool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.722
    - null
    metric_stds:
    - 0.016
    - null
  - model: Set2Set
    model_plain: Set2Set
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7175
    - null
    metric_stds:
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
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
    - 0.7136
    - null
    metric_stds:
    - 0.0115
    - null
  - model: MeanPool
    model_plain: MeanPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7126
    - null
    metric_stds:
    - null
    - null
  - model: ORC
    model_plain: ORC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    metric_stds:
    - 0.02
    - null
  - model: StructPool
    model_plain: StructPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7085
    - null
    metric_stds:
    - null
    - null
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
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
    - 0.7065
    - null
    metric_stds:
    - 0.0113
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    metric_stds:
    - 0.015
    - null
  - model: Diff
    model_plain: Diff
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    - null
    metric_stds:
    - 0.02
    - null
  - model: TV
    model_plain: TV
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    - null
    metric_stds:
    - 0.02
    - null
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
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
    - 0.695
    - null
    metric_stds:
    - 0.0036
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
    - 0.693
    - null
    metric_stds:
    - 0.086
    - null
  - model: JOAOv2
    model_plain: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.688
    - null
    metric_stds:
    - 0.003
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6825
    - null
    metric_stds:
    - null
    - null
  - model: DMoN
    model_plain: DMoN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    - null
    metric_stds:
    - 0.02
    - null
  - model: MLP + EdgePool
    model_plain: MLP + EdgePool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    - null
    metric_stds:
    - 0.032
    - null
  - model: ECC
    model_plain: ECC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6779
    - null
    metric_stds:
    - null
    - null
  - model: K-NN
    model_plain: K-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6753
    - null
    metric_stds:
    - 0.0133
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
    - 0.674
    - null
    metric_stds:
    - 0.008
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
    - 0.673
    - null
    metric_stds:
    - 0.042
    - null
  - model: EdgePool
    model_plain: EdgePool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.671
    - null
    metric_stds:
    - 0.027
    - null
  - model: Weak-sup
    model_plain: Weak-sup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    metric_stds:
    - 0.017
    - null
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    metric_stds:
    - 0.008
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    metric_stds:
    - 0.022
    - null
  - model: Mincut
    model_plain: Mincut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    metric_stds:
    - 0.02
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
    - 0.661
    - null
    metric_stds:
    - 0.009
    - null
  - model: Global max
    model_plain: Global max
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.659
    - null
    metric_stds:
    - 0.034
    - null
  - model: Unsup, ours
    model_plain: Unsup, ours
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.02850'
    title: Understanding Attention and Generalization in Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/bknyaz/graph_attention_pool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.657
    - null
    metric_stds:
    - 0.035
    - null
  - model: DGN
    model_plain: DGN
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
    - 0.655
    - null
    metric_stds:
    - 0.01
    - null
  - model: Base Model
    model_plain: Base Model
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.654
    - null
    metric_stds:
    - 0.015
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
    - 0.652
    - null
    metric_stds:
    - 0.011
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
    - 0.649
    - null
    metric_stds:
    - 0.013
    - null
  - model: Graphlet
    model_plain: Graphlet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6466
    - null
    metric_stds:
    - null
    - null
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.646
    - null
    metric_stds:
    - 0.021
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
    - 0.645
    - null
    metric_stds:
    - 0.015
    - null
  - model: SAGE + EdgePool
    model_plain: SAGE + EdgePool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.643
    - null
    metric_stds:
    - 0.019
    - null
  - model: Set2Set
    model_plain: Set2Set
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6423
    - null
    metric_stds:
    - null
    - null
  - model: SAGE nacc
    model_plain: SAGE nacc
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    - null
    metric_stds:
    - 0.021
    - null
  - model: SAGE nacc + EdgePool
    model_plain: SAGE nacc + EdgePool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    - null
    metric_stds:
    - 0.023
    - null
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.639
    - null
    metric_stds:
    - 0.025
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.636
    - null
    metric_stds:
    - 0.024
    - null
  - model: GCN-concat
    model_plain: GCN-concat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6322
    - null
    metric_stds:
    - null
    - null
  - model: Non-transfer-GCN
    model_plain: Non-transfer-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6316
    - null
    metric_stds:
    - 0.0147
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6295
    - null
    metric_stds:
    - 0.0123
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6187
    - null
    metric_stds:
    - null
    - null
  - model: DGLC
    model_plain: DGLC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6115
    - null
    metric_stds:
    - 0.0144
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6109
    - null
    metric_stds:
    - 0.0136
    - null
  - model: InfoGraph+SC
    model_plain: InfoGraph+SC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6092
    - null
    metric_stds:
    - 0.0249
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5977
    - null
    metric_stds:
    - 0.0167
    - null
  - model: InfoGraph+KM
    model_plain: InfoGraph+KM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5964
    - null
    metric_stds:
    - 0.0178
    - null
  - model: Shortest-path
    model_plain: Shortest-path
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.591
    - null
    metric_stds:
    - null
    - null
  - model: JOAO+KM
    model_plain: JOAO+KM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5834
    - null
    metric_stds:
    - 0.0146
    - null
  - model: GraphCL+KM
    model_plain: GraphCL+KM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5802
    - null
    metric_stds:
    - 0.0122
    - null
  - model: JOAO+SC
    model_plain: JOAO+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5784
    - null
    metric_stds:
    - 0.0088
    - null
  - model: GraphCL+SC
    model_plain: GraphCL+SC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5783
    - null
    metric_stds:
    - 0.0061
    - null
  - model: OOD-GMixup
    model_plain: OOD-GMixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.575
    - null
    metric_stds:
    - 0.0181
    - null
  - model: R-GIN + DIGL
    model_plain: R-GIN + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5471
    - null
    metric_stds:
    - 0.0042
    - null
  - model: GCN + DIGL
    model_plain: GCN + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.545
    - null
    metric_stds:
    - 0.0041
    - null
  - model: WL+SC
    model_plain: WL+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.532
    - null
    metric_stds:
    - 0.0
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.10990'
    title: Edge Contraction Pooling for Graph Neural Networks
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.52
    - null
    metric_stds:
    - 0.025
    - null
  - model: GCN + Every FA
    model_plain: GCN + Every FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.518
    - null
    metric_stds:
    - 0.0042
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5174
    - null
    metric_stds:
    - 0.0159
    - null
  - model: FLAG
    model_plain: FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.512
    - null
    metric_stds:
    - 0.0188
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5101
    - null
    metric_stds:
    - 0.015
    - null
  - model: OOD-GNN
    model_plain: OOD-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4951
    - null
    metric_stds:
    - 0.0346
    - null
  - model: SP+SC
    model_plain: SP+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4872
    - null
    metric_stds:
    - 0.0
    - null
  - model: CAD
    model_plain: CAD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4822
    - null
    metric_stds:
    - 0.0245
    - null
  - model: MixUp
    model_plain: MixUp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4756
    - null
    metric_stds:
    - 0.0428
    - null
  - model: Top-K Pooling
    model_plain: Top-K Pooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4702
    - null
    metric_stds:
    - 0.0417
    - null
  - model: Virtual Node
    model_plain: Virtual Node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4645
    - null
    metric_stds:
    - 0.0466
    - null
  - model: SAGPooling
    model_plain: SAGPooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4629
    - null
    metric_stds:
    - 0.0405
    - null
  - model: SizeShiftReg
    model_plain: SizeShiftReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4578
    - null
    metric_stds:
    - 0.0351
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4361
    - null
    metric_stds:
    - 0.0419
    - null
  - model: Attention
    model_plain: Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4346
    - null
    metric_stds:
    - 0.048
    - null
  - model: DropoutNode
    model_plain: DropoutNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4342
    - null
    metric_stds:
    - 0.0427
    - null
  - model: IB-IRM
    model_plain: IB-IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4234
    - null
    metric_stds:
    - 0.0986
    - null
  - model: IRM
    model_plain: IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3447
    - null
    metric_stds:
    - 0.0607
    - null
  - model: GCN + FoSR
    model_plain: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3384
    - null
    metric_stds:
    - 0.0058
    - null
  - model: GCN + None
    model_plain: GCN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3378
    - null
    metric_stds:
    - 0.0049
    - null
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3345
    - null
    metric_stds:
    - 0.0047
    - null
  - model: GCN + Last FA
    model_plain: GCN + Last FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3332
    - null
    metric_stds:
    - 0.0044
    - null
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.326
    - null
    metric_stds:
    - 0.0517
    - null
  - model: DropoutEdge
    model_plain: DropoutEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3126
    - null
    metric_stds:
    - 0.0468
    - null
  - model: Group DRO
    model_plain: Group DRO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3017
    - null
    metric_stds:
    - 0.0577
    - null
  - model: VGRNN
    model_plain: VGRNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12753'
    title: Contrastive Representation Learning for Dynamic Link Prediction in Temporal
      Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/amrhssn/teneNCE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8656
    metric_stds:
    - null
    - 0.004
  - model: DySAT
    model_plain: DySAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12753'
    title: Contrastive Representation Learning for Dynamic Link Prediction in Temporal
      Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/amrhssn/teneNCE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.861
    metric_stds:
    - null
    - 0.003
  - model: EvolveGCN-H
    model_plain: EvolveGCN-H
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12753'
    title: Contrastive Representation Learning for Dynamic Link Prediction in Temporal
      Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/amrhssn/teneNCE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8063
    metric_stds:
    - null
    - 0.009
  - model: Euler
    model_plain: Euler
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12753'
    title: Contrastive Representation Learning for Dynamic Link Prediction in Temporal
      Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/amrhssn/teneNCE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8593
    metric_stds:
    - null
    - 0.01
  - model: teneNCE
    model_plain: teneNCE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12753'
    title: Contrastive Representation Learning for Dynamic Link Prediction in Temporal
      Networks
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/amrhssn/teneNCE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8825
    metric_stds:
    - null
    - 0.007
  milestones:
  - value: 0.8213
    std: null
    model: DiffPool-Det
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: 2018-06
  - value: 0.836
    std: 0.01
    model: GNTK
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: 2019-05
  - value: 0.8379
    std: 0.0039
    model: GFL-att
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: 2019-10
  - value: 0.8672
    std: 0.0162
    model: novel dynamic message-passing mechanism
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: 2024-10
---

