---
title: PubMed
slug: pubmed
benchmark: Classic
task_type: node_classification
description: Citation network node classification (3 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 3
result_count: 113
best_model:
  model: Flan-T5-large
  value: 0.9462
  metric: Accuracy
  arxiv_id: '2308.07134'
  paper_title: Language is All a Graph Needs
variants:
- slug: planetoid-split
  name: Planetoid split
  notes: Yang et al. 2016 fixed split.
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
    is_best: true
    metric_values:
    - 0.9462
    metric_stds:
    - 0.0013
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
    is_best: true
    metric_values:
    - 0.9445
    metric_stds:
    - 0.0012
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
    - 0.9384
    metric_stds:
    - 0.0025
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
    - 0.9144
    metric_stds:
    - 0.0059
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
    - 0.9096
    metric_stds:
    - 0.0062
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
    - 0.9005
    metric_stds:
    - 0.0014
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
    - 0.9004
    metric_stds:
    - 0.0141
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
    - 0.8998
    metric_stds:
    - 0.0054
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
    - 0.898
    metric_stds:
    - 0.003
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
    - 0.8975
    metric_stds:
    - 0.0031
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
    - 0.8962
    metric_stds:
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
    - 0.889
    metric_stds:
    - 0.0032
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
    - 0.8875
    metric_stds:
    - 0.0016
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
    - 0.885
    metric_stds:
    - 0.0005
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
    - 0.8848
    metric_stds:
    - 0.0041
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
    - 0.8824
    metric_stds:
    - 0.015
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
    - 0.8685
    metric_stds:
    - 0.0011
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
    - 0.8668
    metric_stds:
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
    - 0.8545
    metric_stds:
    - 0.0026
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
    - 0.8536
    metric_stds:
    - 0.0052
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
    - 0.8507
    metric_stds:
    - 0.0034
  - model: GCN
    model_plain: GCN
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
    - 0.8421
    metric_stds:
    - 0.0026
  - model: SAIL
    model_plain: SAIL
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
    - 0.838
    metric_stds:
    - 0.001
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
    - 0.8367
    metric_stds:
    - 0.0046
  - model: GAT
    model_plain: GAT
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
    - 0.8328
    metric_stds:
    - 0.0012
  - model: APPNP
    model_plain: APPNP
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
    - 0.8286
    metric_stds:
    - 0.0029
  - model: GRAND
    model_plain: GRAND
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
    - 0.827
    metric_stds:
    - 0.006
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
    - 0.825
    metric_stds:
    - 0.003
  - model: ALT-OPT
    model_plain: ALT-OPT
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
    - 0.825
    metric_stds:
    - 0.017
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
    - 0.821
    metric_stds:
    - 0.004
  - model: SGC
    model_plain: SGC
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
    - 0.82
    metric_stds:
    - 0.0027
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
    - 0.8187
    metric_stds:
    - null
  - model: APPNP
    model_plain: APPNP
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
    - 0.818
    metric_stds:
    - 0.005
  - model: SuperGAT
    model_plain: SuperGAT
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
    - 0.817
    metric_stds:
    - 0.005
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
    - 0.816
    metric_stds:
    - 0.005
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
    - 0.815
    metric_stds:
    - 0.006
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
    - 0.815
    metric_stds:
    - 0.004
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
    - 0.812
    metric_stds:
    - 0.005
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
    - 0.808
    metric_stds:
    - 0.004
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
    - 0.805
    metric_stds:
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
    - 0.805
    metric_stds:
    - 0.012
  - model: SGFormer
    model_plain: SGFormer
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
    - 0.803
    metric_stds:
    - 0.006
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
    - 0.8
    metric_stds:
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    metric_stds:
    - 0.001
  - model: NodeFormer
    model_plain: NodeFormer
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
    - 0.799
    metric_stds:
    - 0.01
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
    - 0.799
    metric_stds:
    - 0.003
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
    - 0.796
    metric_stds:
    - 0.002
  - model: ANS-GT
    model_plain: ANS-GT
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
    - 0.796
    metric_stds:
    - 0.01
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
    - 0.795
    metric_stds:
    - 0.002
  - model: GCDE-rk4 (4)
    model_plain: GCDE-rk4 (4)
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
    - 0.795
    metric_stds:
    - 0.004
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
    - 0.794
    metric_stds:
    - 0.003
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
    - 0.793
    metric_stds:
    - null
  - model: Snowball
    model_plain: Snowball
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
    - 0.792
    metric_stds:
    - 0.003
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
    - 0.792
    metric_stds:
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
    - 0.791
    metric_stds:
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
    - 0.791
    metric_stds:
    - 0.003
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.79
    metric_stds:
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
    - 0.79
    metric_stds:
    - 0.017
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
    - 0.79
    metric_stds:
    - 0.004
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.789
    metric_stds:
    - 0.007
  - model: GLN
    model_plain: GLN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    metric_stds:
    - 0.001
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
    - 0.789
    metric_stds:
    - 0.0
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
    - 0.7881
    metric_stds:
    - 0.0044
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
    - 0.786
    metric_stds:
    - 0.016
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.785
    metric_stds:
    - null
  - model: GCDE-dpr5 (158)
    model_plain: GCDE-dpr5 (158)
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
    - 0.785
    metric_stds:
    - 0.007
  - model: LNet
    model_plain: LNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    metric_stds:
    - 0.003
  - model: AdaLNet
    model_plain: AdaLNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.781
    metric_stds:
    - 0.004
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.778
    metric_stds:
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
    - 0.777
    metric_stds:
    - 0.018
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.775
    metric_stds:
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.774
    metric_stds:
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
    - 0.774
    metric_stds:
    - 0.02
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    metric_stds:
    - 0.003
  - model: GS-mean
    model_plain: GS-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    metric_stds:
    - 0.022
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.772
    metric_stds:
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    metric_stds:
    - 0.012
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
    - 0.768
    metric_stds:
    - 0.015
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    metric_stds:
    - 0.006
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
    - 0.768
    metric_stds:
    - 0.006
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
    - 0.765
    metric_stds:
    - 0.019
  - model: GS-meanpool
    model_plain: GS-meanpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    metric_stds:
    - 0.024
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
    - 0.763
    metric_stds:
    - 0.0122
  - model: GS-maxpool
    model_plain: GS-maxpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.761
    metric_stds:
    - 0.023
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
    - 0.7587
    metric_stds:
    - 0.0066
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
    - 0.757
    metric_stds:
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
    - 0.744
    metric_stds:
    - null
  - model: ChebNet
    model_plain: ChebNet
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
    - 0.744
    metric_stds:
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
    - 0.742
    metric_stds:
    - 0.0099
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.739
    metric_stds:
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
    - 0.739
    metric_stds:
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
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
    - 0.7347
    metric_stds:
    - 0.0034
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
    - 0.7327
    metric_stds:
    - 0.0184
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
    - 0.73
    metric_stds:
    - 0.0052
  - model: LabelProp NL
    model_plain: LabelProp NL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.723
    metric_stds:
    - 0.029
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
    - 0.721
    metric_stds:
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
    - 0.7203
    metric_stds:
    - 0.0133
  - model: GCN
    model_plain: GCN
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
    metric_stds:
    - 0.0297
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.714
    metric_stds:
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
    - 0.711
    metric_stds:
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
    - 0.707
    metric_stds:
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    metric_stds:
    - 0.053
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - 0.021
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
    - 0.6987
    metric_stds:
    - 0.017
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
    - 0.698
    metric_stds:
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
    - 0.6973
    metric_stds:
    - 0.0079
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
    - 0.6953
    metric_stds:
    - 0.0144
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.653
    metric_stds:
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
    - 0.653
    metric_stds:
    - null
  - model: LogReg
    model_plain: LogReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    metric_stds:
    - 0.031
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
    - 0.63
    metric_stds:
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
    - 0.622
    metric_stds:
    - null
  milestones:
  - value: 0.79
    std: 0.017
    model: CNNs
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: '2013-12-21'
  - value: 0.8
    std: null
    model: DGCNN
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: 2018-12
  - value: 0.805
    std: null
    model: GraphHeat
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: 2021-01
  - value: 0.8962
    std: null
    model: GloGNN
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: '2022-05-15'
  - value: 0.9462
    std: 0.0013
    model: Flan-T5-large
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: 2023-08
---

