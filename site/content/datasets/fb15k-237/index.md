---
title: FB15k-237
slug: fb15k-237
benchmark: Knowledge Graphs
task_type: link_prediction
description: Knowledge graph link prediction on Freebase (14,541 entities, 237 relations).
primary_metric: MRR
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.FB15k_237.html
stats:
  num_graphs: 1
  avg_nodes: 14541.0
  avg_edges: 272115.0
  num_classes: 237
result_count: 104
best_model:
  model: ANALOGY
  value: 0.725
  metric: MRR
  arxiv_id: '1707.01476'
  paper_title: Convolutional 2D Knowledge Graph Embeddings
variants:
- slug: standard-split
  name: Standard split
  notes: Toutanova & Chen 2015 split. Also reports Hits@1, Hits@3, Hits@10.
  is_standard: true
  primary_metric: MRR
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MRR
  - AUC-PR
  - Hits@10
  rows:
  - model: ANALOGY
    model_plain: ANALOGY
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1707.01476'
    title: Convolutional 2D Knowledge Graph Embeddings
    date: Jul 2017
    date_iso: 2017-07
    date_display: Jul 2017
    codebase_url: https://github.com/TimDettmers/ConvE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.725
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ADRL
    model_plain: ADRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TransR
    model_plain: TransR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.532
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HolE
    model_plain: HolE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.10197'
    title: 'RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/DeepGraphLearning/KnowledgeGraphEmbedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.524
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RGHAT
    model_plain: RGHAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.522
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.494
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RLH
    model_plain: RLH
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.46
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Zheng et al.
    model_plain: Zheng et al.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.422
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: KGCF
    model_plain: KGCF
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.421
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: NBFNet
    model_plain: NBFNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.415
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ConvE
    model_plain: ConvE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.41
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.374
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RED-GNN
    model_plain: RED-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.374
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ComplEX-DURA-SymCL
    model_plain: ComplEX-DURA-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.371
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ComplEX-DURA
    model_plain: ComplEX-DURA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.37
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: MAGNA + DistMult
    model_plain: MAGNA + DistMult
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.369
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DPMPN
    model_plain: DPMPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.369
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: QuatE
    model_plain: QuatE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.366
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ConEx
    model_plain: ConEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.366
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: OTE
    model_plain: OTE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.361
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CoKE
    model_plain: CoKE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.361
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HousE
    model_plain: HousE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.361
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: AutoSF
    model_plain: AutoSF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.36
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LowFER
    model_plain: LowFER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.359
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TuckER
    model_plain: TuckER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.358
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: COMPGCN-SymCL
    model_plain: COMPGCN-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.354
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: InteractE
    model_plain: InteractE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.354
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RESCAL
    model_plain: RESCAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
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
  - model: CompGCN
    model_plain: CompGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.352
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LTE + ConvE
    model_plain: LTE + ConvE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.352
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CompGCN + ConvE
    model_plain: CompGCN + ConvE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.351
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SACN
    model_plain: SACN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ConvR
    model_plain: ConvR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: KBGAT
    model_plain: KBGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.35
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HAKE-SymCL
    model_plain: HAKE-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.346
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.346
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HAKE
    model_plain: HAKE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.346
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ROTH
    model_plain: ROTH
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.344
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DRUM
    model_plain: DRUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.343
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CompGCN + DistMult
    model_plain: CompGCN + DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.342
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HypER
    model_plain: HypER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.341
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RotatE
    model_plain: RotatE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.10197'
    title: 'RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/DeepGraphLearning/KnowledgeGraphEmbedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.338
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RGCN + ConvE
    model_plain: RGCN + ConvE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.336
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HAKE
    model_plain: HAKE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: MuRP
    model_plain: MuRP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CompGCN + TransE
    model_plain: CompGCN + TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LTE + DistMult
    model_plain: LTE + DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LTE + TransE
    model_plain: LTE + TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.334
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: pLogicNet
    model_plain: pLogicNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.332
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DistMult + GCN
    model_plain: DistMult + GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.332
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DualE
    model_plain: DualE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.33
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ConvE
    model_plain: ConvE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1707.01476'
    title: Convolutional 2D Knowledge Graph Embeddings
    date: Jul 2017
    date_iso: 2017-07
    date_display: Jul 2017
    codebase_url: https://github.com/TimDettmers/ConvE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.325
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SimKGC-SymCL
    model_plain: SimKGC-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.324
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RGCN + TransE
    model_plain: RGCN + TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.324
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SimGC
    model_plain: SimGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.322
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ConvE
    model_plain: ConvE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.319
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: A2N
    model_plain: A2N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.317
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: QuatE
    model_plain: QuatE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.311
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CURL
    model_plain: CURL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.306
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.10197'
    title: 'RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/DeepGraphLearning/KnowledgeGraphEmbedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.294
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: MINERVA
    model_plain: MINERVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.293
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TransE-SymCL
    model_plain: TransE-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.29
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.289
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ConvKB
    model_plain: ConvKB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.289
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: MINERVA
    model_plain: MINERVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.271
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DisMult-SymCL
    model_plain: DisMult-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.26
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.249
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RGCN-SymCL
    model_plain: RGCN-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.249
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1707.01476'
    title: Convolutional 2D Knowledge Graph Embeddings
    date: Jul 2017
    date_iso: 2017-07
    date_display: Jul 2017
    codebase_url: https://github.com/TimDettmers/ConvE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.248
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.248
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1707.01476'
    title: Convolutional 2D Knowledge Graph Embeddings
    date: Jul 2017
    date_iso: 2017-07
    date_display: Jul 2017
    codebase_url: https://github.com/TimDettmers/ConvE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.247
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DistMult
    model_plain: DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.243
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DistMult
    model_plain: DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1707.01476'
    title: Convolutional 2D Knowledge Graph Embeddings
    date: Jul 2017
    date_iso: 2017-07
    date_display: Jul 2017
    codebase_url: https://github.com/TimDettmers/ConvE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.241
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: NeuralLP
    model_plain: NeuralLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.24
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: M-walk
    model_plain: M-walk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.234
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.233
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: NeuralLP
    model_plain: NeuralLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.227
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HolE
    model_plain: HolE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.222
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.201
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DistMult
    model_plain: DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.191
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CP
    model_plain: CP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.182
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Path Ranking
    model_plain: Path Ranking
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.13083'
    title: Knowledge Graph Completion with Counterfactual Augmentation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.174
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: LinkFeat
    model_plain: LinkFeat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.063
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Inverse Model
    model_plain: Inverse Model
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1707.01476'
    title: Convolutional 2D Knowledge Graph Embeddings
    date: Jul 2017
    date_iso: 2017-07
    date_display: Jul 2017
    codebase_url: https://github.com/TimDettmers/ConvE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.01
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GraIL
    model_plain: GraIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9391
    - 0.6415
    metric_stds:
    - null
    - null
    - null
  - model: Neural-LP
    model_plain: Neural-LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6964
    - 0.5292
    metric_stds:
    - null
    - null
    - null
  - model: DRUM
    model_plain: DRUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6971
    - 0.5292
    metric_stds:
    - null
    - null
    - null
  - model: RuleN
    model_plain: RuleN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7524
    - 0.4976
    metric_stds:
    - null
    - null
    - null
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9854
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DistMult
    model_plain: DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9841
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9845
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RotatE
    model_plain: RotatE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.06962'
    title: arXiv:1911.06962
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/kkteru/grail
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9855
    - null
    metric_stds:
    - null
    - null
    - null
  - model: IKRL
    model_plain: IKRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.458
    metric_stds:
    - null
    - null
    - null
  - model: MTRL
    model_plain: MTRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.494
    metric_stds:
    - null
    - null
    - null
  - model: MKBE
    model_plain: MKBE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.532
    metric_stds:
    - null
    - null
    - null
  - model: RSME
    model_plain: RSME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.467
    metric_stds:
    - null
    - null
    - null
  - model: MoSE
    model_plain: MoSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.565
    metric_stds:
    - null
    - null
    - null
  - model: KBLRN
    model_plain: KBLRN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.493
    metric_stds:
    - null
    - null
    - null
  - model: VisualBERT
    model_plain: VisualBERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.439
    metric_stds:
    - null
    - null
    - null
  - model: ViLBERT
    model_plain: ViLBERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.457
    metric_stds:
    - null
    - null
    - null
  - model: VBKGC
    model_plain: VBKGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.478
    metric_stds:
    - null
    - null
    - null
  - model: HRGAT
    model_plain: HRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.542
    metric_stds:
    - null
    - null
    - null
  - model: MKGformer
    model_plain: MKGformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.499
    metric_stds:
    - null
    - null
    - null
  - model: IMF
    model_plain: IMF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.05767'
    title: 'A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic,
      and Multi-Modal'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.593
    metric_stds:
    - null
    - null
    - null
  milestones:
  - value: 0.249
    std: null
    model: R-GCN
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: 2017-03
  - value: 0.725
    std: null
    model: ANALOGY
    arxiv_id: '1707.01476'
    title: Convolutional 2D Knowledge Graph Embeddings
    date: 2017-07
---

