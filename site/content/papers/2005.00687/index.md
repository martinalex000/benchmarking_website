---
title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
arxiv_id: '2005.00687'
source_url: ''
authors: []
published_date: May 2, 2020
published_date_iso: '2020-05-02'
published_venue: ''
abstract: We present the Open Graph Benchmark (OGB), a diverse set of challenging
  and realistic benchmark datasets to facilitate scalable, robust, and reproducible
  graph machine learning (ML) research. OGB datasets are large-scale, encompass multiple
  important graph ML tasks, and cover a diverse range of domains, ranging from social
  and information networks to biological networks, molecular graphs, source code ASTs,
  and knowledge graphs. For each dataset, we provide a unified evaluation protocol
  using meaningful application-specific data splits and evaluation metrics. In addition
  to building the datasets, we also perform extensive benchmark experiments for each
  dataset. Our experiments suggest that OGB datasets present significant challenges
  of scalability to large-scale graphs and out-of-distribution generalization under
  realistic data splits, indicating fruitful opportunities for future research. Finally,
  OGB provides an automated end-to-end graph ML pipeline that simplifies and standardizes
  the process of graph data loading, experimental setup, and model evaluation. OGB
  will be regularly updated and welcomes inputs from the community. OGB datasets as
  well as data loaders, evaluation scripts, baseline code, and leaderboards are publicly
  available at.
codebase_url: https://github.com/snap-stanford/ogb
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- OGB
task_categories:
- graph_classification
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id011
  dataset: Code
  rows:
  - model: ExpC-s
    model_key: expc-s
    model_plain: ExpC-s
    value: 0.3318
    std: 0.0017
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_display: Dec 2020
    date_iso: 2020-12
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3318
    sort_std: 0.0017
    is_best: true
  - model: CombC
    model_key: combc
    model_plain: CombC
    value: 0.3276
    std: 0.0015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_display: Dec 2020
    date_iso: 2020-12
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3276
    sort_std: 0.0015
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1507
    std: 0.0018
    paper_value: 0.1507
    paper_std: 0.0018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 3
    true_value: 0.3163
    true_std: 0.0018
    value_gap_source_arxiv: '2012.07219'
    value_gap_source_title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16560000000000002
    value_note: ''
    paper_rank: 25
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.3163
    sort_std: 0.0018
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1495
    std: 0.0023
    paper_value: 0.1495
    paper_std: 0.0023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 4
    true_value: 0.3163
    true_std: 0.002
    value_gap_source_arxiv: '2012.07219'
    value_gap_source_title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16680000000000003
    value_note: ''
    paper_rank: 26
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.3163
    sort_std: 0.002
    is_best: false
  - model: multi-head GAT
    model_key: multi-head gat
    model_plain: multi-head GAT
    value: 0.311
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_display: Dec 2020
    date_iso: 2020-12
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.311
    sort_std: null
    is_best: false
  - model: GCN+virtual node
    model_key: gcn+virtual node
    model_plain: GCN+virtual node
    value: 0.1581
    std: 0.0026
    paper_value: 0.1581
    paper_std: 0.0026
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 24
    true_value: 0.1581
    true_std: 0.0026
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1581
    sort_std: 0.0026
    is_best: false
  metric: F1
  higher_is_better: true
- &id002
  dataset: ogbg-molhiv
  rows:
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.997
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08443'
    title: 'CLEAR: Generative Counterfactual Explanations on Graphs'
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.997
    sort_std: 0.002
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.002
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.858
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.858
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.752
    std: 0.013
    paper_value: 0.752
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 9
    true_value: 0.848
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09599999999999997
    value_note: ''
    paper_rank: 143
    rank_delta: 134
    rank_delta_abs: 134
    rank_delta_direction: worse
    sort_value: 0.848
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7418
    std: 0.0122
    paper_value: 0.7418
    paper_std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 13
    true_value: 0.839
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09719999999999995
    value_note: ''
    paper_rank: 153
    rank_delta: 140
    rank_delta_abs: 140
    rank_delta_direction: worse
    sort_value: 0.839
    sort_std: 0.006
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
  dataset: ogbg-molpcba
  is_multi_metric: true
  rows:
  - model: GCN+virtual node
    model_key: gcn+virtual node
    model_plain: GCN+virtual node
    metric_values:
    - null
    - 0.7037
    metric_stds:
    - null
    - 0.0107
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7037
    sort_std: 0.0107
    true_value: null
    true_std: null
    paper_value: 0.7037
    paper_std: 0.0107
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: true
    global_rank: 37
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    metric_values:
    - 0.339
    - null
    metric_stds:
    - 0.0073
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    published_venue: ''
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
    sort_value: 0.339
    sort_std: 0.0073
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: unified method + FLAG
    model_key: unified method + flag
    model_plain: unified method + FLAG
    metric_values:
    - 0.3174
    - null
    metric_stds:
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    published_venue: ''
    date: Jul 2022
    date_display: Jul 2022
    date_iso: 2022-07
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.3174
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: TGT-Ag+TGT-At-DP
    model_key: tgt-ag+tgt-at-dp
    model_plain: TGT-Ag+TGT-At-DP
    metric_values:
    - 0.3167
    - null
    metric_stds:
    - 0.0031
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    published_venue: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.3167
    sort_std: 0.0031
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - 0.2661
    - 0.6892
    metric_stds:
    - 0.0017
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2703
    sort_std: 0.0023
    true_value: 0.2703
    true_std: 0.0023
    paper_value: 0.2661
    paper_std: 0.0017
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0041999999999999815
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 35
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.2291
    - 0.6839
    metric_stds:
    - 0.0037
    - 0.0084
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2424
    sort_std: 0.0034
    true_value: 0.2424
    true_std: 0.0034
    paper_value: 0.2291
    paper_std: 0.0037
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013300000000000006
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 46
  metrics:
  - AP
  - Accuracy
  primary_metric: AP
  higher_is_better: true
- &id012
  dataset: ogbl-biokg
  rows:
  - model: ComplEx
    model_key: complex
    model_plain: ComplEx
    value: 0.8095
    std: 0.0007
    paper_value: 0.8095
    paper_std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Trouillon et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 1
    true_value: 0.8095
    true_std: 0.0007
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8095
    sort_std: 0.0007
    is_best: true
  - model: DistMult
    model_key: distmult
    model_plain: DistMult
    value: 0.8043
    std: 0.0003
    paper_value: 0.8043
    paper_std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2014
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 2
    true_value: 0.8043
    true_std: 0.0003
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8043
    sort_std: 0.0003
    is_best: false
  - model: RotatE
    model_key: rotate
    model_plain: RotatE
    value: 0.7989
    std: 0.0004
    paper_value: 0.7989
    paper_std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 3
    true_value: 0.7989
    true_std: 0.0004
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7989
    sort_std: 0.0004
    is_best: false
  - model: TransE
    model_key: transe
    model_plain: TransE
    value: 0.7452
    std: 0.0004
    paper_value: 0.7452
    paper_std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bordes et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 4
    true_value: 0.7452
    true_std: 0.0004
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7452
    sort_std: 0.0004
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.512
    std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.512
    sort_std: 0.003
    is_best: false
  - model: GAIN
    model_key: gain
    model_plain: GAIN
    value: 0.485
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.485
    sort_std: null
    is_best: false
  - model: CompGCN
    model_key: compgcn
    model_plain: CompGCN
    value: 0.468
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.468
    sort_std: null
    is_best: false
  metric: MRR
  higher_is_better: true
- &id006
  dataset: ogbl-citation2
  is_multi_metric: true
  rows:
  - model: MPLP
    model_key: mplp
    model_plain: MPLP
    metric_values:
    - 0.9072
    - null
    metric_stds:
    - 0.0012
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    published_venue: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.9072
    sort_std: 0.0012
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: NCNC
    model_key: ncnc
    model_plain: NCNC
    metric_values:
    - 0.8912
    - null
    metric_stds:
    - 0.004
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    published_venue: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.8912
    sort_std: 0.004
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: SEAL
    model_key: seal
    model_plain: SEAL
    metric_values:
    - 0.8767
    - null
    metric_stds:
    - 0.0032
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    published_venue: ''
    date: Mar 2023
    date_display: Mar 2023
    date_iso: 2023-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.8767
    sort_std: 0.0032
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.8474
    - 0.1867
    metric_stds:
    - 0.0021
    - 0.0132
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8479
    sort_std: 0.0024
    true_value: 0.8479
    true_std: 0.0024
    paper_value: 0.8474
    paper_std: 0.0021
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0004999999999999449
    value_gap_source_arxiv: '2206.04216'
    value_gap_source_title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks
      for Link Prediction'
    value_note: global 0.8479 within std
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 12
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    metric_values:
    - 0.826
    - 0.1655
    metric_stds:
    - 0.0036
    - 0.024
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8264
    sort_std: 0.0001
    true_value: 0.8264
    true_std: 0.0001
    paper_value: 0.826
    paper_std: 0.0036
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00040000000000006697
    value_gap_source_arxiv: '2206.04216'
    value_gap_source_title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks
      for Link Prediction'
    value_note: global 0.8264 within std
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 16
  - model: Neighbor Sampling (NS)
    model_key: neighbor sampling (ns)
    model_plain: Neighbor Sampling (NS)
    metric_values:
    - 0.8044
    - null
    metric_stds:
    - 0.001
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8044
    sort_std: 0.001
    true_value: 0.8044
    true_std: 0.001
    paper_value: 0.8044
    paper_std: 0.001
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 20
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    metric_values:
    - 0.8004
    - null
    metric_stds:
    - 0.0025
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8004
    sort_std: 0.0025
    true_value: 0.8004
    true_std: 0.0025
    paper_value: 0.8004
    paper_std: 0.0025
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 22
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    metric_values:
    - 0.7985
    - null
    metric_stds:
    - 0.004
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7985
    sort_std: 0.004
    true_value: 0.7985
    true_std: 0.004
    paper_value: 0.7985
    paper_std: 0.004
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 23
  - model: Node2Vec
    model_key: node2vec
    model_plain: Node2Vec
    metric_values:
    - 0.6141
    - 0.2226
    metric_stds:
    - 0.0011
    - 0.0083
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.6141
    sort_std: 0.0011
    true_value: 0.6141
    true_std: 0.0011
    paper_value: 0.6141
    paper_std: 0.0011
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 37
  - model: MatrixFactorization
    model_key: matrixfactorization
    model_plain: MatrixFactorization
    metric_values:
    - 0.5186
    - 0.3229
    metric_stds:
    - 0.0443
    - 0.0094
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.5186
    sort_std: 0.0443
    true_value: 0.5186
    true_std: 0.0443
    paper_value: 0.5186
    paper_std: 0.0443
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_note: ''
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 42
  - model: MLP
    model_key: mlp
    model_plain: MLP
    metric_values:
    - 0.2895
    - 0.46
    metric_stds:
    - 0.0014
    - 0.0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2899
    sort_std: 0.0016
    true_value: 0.2899
    true_std: 0.0016
    paper_value: 0.2895
    paper_std: 0.0014
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00040000000000001146
    value_gap_source_arxiv: '2206.04216'
    value_gap_source_title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks
      for Link Prediction'
    value_note: global 0.2899 within std
    arxiv_id: ''
    title: ''
    published_venue: null
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 47
  metrics:
  - MRR
  - Hits@100
  primary_metric: MRR
  higher_is_better: true
- &id010
  dataset: ogbl-ddi
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.784
    std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.784
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.771
    std: 0.003
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.771
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.765
    std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.765
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.539
    std: 0.0474
    paper_value: 0.539
    paper_std: 0.0474
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 6
    true_value: 0.741
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20199999999999996
    value_note: ''
    paper_rank: 12
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3707
    std: 0.0507
    paper_value: 0.3707
    paper_std: 0.0507
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 7
    true_value: 0.735
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3643
    value_note: ''
    paper_rank: 15
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.735
    sort_std: 0.003
    is_best: false
  - model: Node2Vec
    model_key: node2vec
    model_plain: Node2Vec
    value: 0.2326
    std: 0.0209
    paper_value: 0.2326
    paper_std: 0.0209
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 22
    true_value: 0.2326
    true_std: 0.0209
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2326
    sort_std: 0.0209
    is_best: false
  - model: MatrixFactorization
    model_key: matrixfactorization
    model_plain: MatrixFactorization
    value: 0.1368
    std: 0.0475
    paper_value: 0.1368
    paper_std: 0.0475
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 28
    true_value: 0.1368
    true_std: 0.0475
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1368
    sort_std: 0.0475
    is_best: false
  metric: Hits@20
  higher_is_better: true
- &id007
  dataset: ogbl-wikikg2
  rows:
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 0.7983
    std: 0.0042
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7983
    sort_std: 0.0042
    is_best: true
  - model: TCL
    model_key: tcl
    model_plain: TCL
    value: 0.7811
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7811
    sort_std: 0.002
    is_best: false
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.746
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 17, 2021
    date_display: Mar 2021
    date_iso: '2021-03-17'
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.746
    sort_std: 0.001
    is_best: false
  - model: RotatE
    model_key: rotate
    model_plain: RotatE
    value: 0.253
    std: 0.0034
    paper_value: 0.253
    paper_std: 0.0034
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 8
    true_value: 0.728
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.475
    value_note: ''
    paper_rank: 35
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.728
    sort_std: 0.003
    is_best: false
  - model: ComplEx
    model_key: complex
    model_plain: ComplEx
    value: 0.3804
    std: 0.0022
    paper_value: 0.3804
    paper_std: 0.0022
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Trouillon et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 9
    true_value: 0.725
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.34459999999999996
    value_note: ''
    paper_rank: 34
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.725
    sort_std: 0.003
    is_best: false
  - model: DistMult
    model_key: distmult
    model_plain: DistMult
    value: 0.3447
    std: 0.0082
    paper_value: 0.3447
    paper_std: 0.0082
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2014
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 10
    true_value: 0.721
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.37629999999999997
    value_note: ''
    paper_rank: 35
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.721
    sort_std: 0.003
    is_best: false
  - model: TransE
    model_key: transe
    model_plain: TransE
    value: 0.2622
    std: 0.0045
    paper_value: 0.2622
    paper_std: 0.0045
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bordes et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 12
    true_value: 0.685
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.42280000000000006
    value_note: ''
    paper_rank: 35
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.685
    sort_std: 0.004
    is_best: false
  - model: RotatE (5x dim)
    model_key: rotate (5x dim)
    model_plain: RotatE (5x dim)
    value: 0.4332
    std: 0.0025
    paper_value: 0.4332
    paper_std: 0.0025
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 32
    true_value: 0.4332
    true_std: 0.0025
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4332
    sort_std: 0.0025
    is_best: false
  - model: TransE (5x dim)
    model_key: transe (5x dim)
    model_plain: TransE (5x dim)
    value: 0.4256
    std: 0.003
    paper_value: 0.4256
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bordes et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 33
    true_value: 0.4256
    true_std: 0.003
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4256
    sort_std: 0.003
    is_best: false
  - model: ComplEx (5x dim)
    model_key: complex (5x dim)
    model_plain: ComplEx (5x dim)
    value: 0.4027
    std: 0.0027
    paper_value: 0.4027
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Trouillon et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 34
    true_value: 0.4027
    true_std: 0.0027
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4027
    sort_std: 0.0027
    is_best: false
  - model: DistMult (5x dim)
    model_key: distmult (5x dim)
    model_plain: DistMult (5x dim)
    value: 0.3729
    std: 0.0045
    paper_value: 0.3729
    paper_std: 0.0045
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2014
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 35
    true_value: 0.3729
    true_std: 0.0045
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3729
    sort_std: 0.0045
    is_best: false
  metric: MRR
  higher_is_better: true
- &id001
  dataset: ogbn-arxiv
  rows:
  - model: KCoT
    model_key: kcot
    model_plain: KCoT
    value: 0.7925
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.24867'
    title: 'Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought
      Graph Learning'
    date: May 24, 2026
    date_display: May 2026
    date_iso: '2026-05-24'
    codebase_url: https://github.com/Uncnbb/KCoT
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.7925
    sort_std: null
    is_best: true
  - model: TAPE + SimTeG
    model_key: tape + simteg
    model_plain: TAPE + SimTeG
    value: 0.7803
    std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.02565'
    title: 'SimTeG: A Frustratingly ple Approach Improves xtual raph Learning'
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: https://github.com/vermouthdky/SimTeG
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.7803
    sort_std: 0.0007
    is_best: false
  - model: OFA
    model_key: ofa
    model_plain: OFA
    value: 0.7751
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.19211'
    title: 'Large Language Models Meet Graph Neural Networks: A Perspective of Graph
      Mining'
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7751
    sort_std: 0.0017
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7149
    std: 0.0027
    paper_value: 0.7149
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 26
    true_value: 0.7629
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04800000000000004
    value_note: ''
    paper_rank: 252
    rank_delta: 226
    rank_delta_abs: 226
    rank_delta_direction: worse
    sort_value: 0.7629
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7174
    std: 0.0029
    paper_value: 0.7174
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 57
    true_value: 0.752
    true_std: 0.0003
    value_gap_source_arxiv: '2509.14863'
    value_gap_source_title: 'Exploring the Global-to-Local Attention Scheme in Graph
      Transformers: An Empirical Study'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.034599999999999964
    value_note: ''
    paper_rank: 234
    rank_delta: 177
    rank_delta_abs: 177
    rank_delta_direction: worse
    sort_value: 0.752
    sort_std: 0.0003
    is_best: false
  - model: Node2Vec
    model_key: node2vec
    model_plain: Node2Vec
    value: 0.7007
    std: 0.0013
    paper_value: 0.7007
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 260
    true_value: 0.713
    true_std: 0.001
    value_gap_source_arxiv: '2111.12952'
    value_gap_source_title: 'AutoHEnsGNN: Winning Solution to AutoGraph Challenge
      for KDD Cup 2020'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012299999999999978
    value_note: ''
    paper_rank: 295
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.713
    sort_std: 0.001
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.555
    std: 0.0023
    paper_value: 0.555
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 356
    true_value: 0.6291
    true_std: 0.006
    value_gap_source_arxiv: '2304.10668'
    value_gap_source_title: 'Train Your Own GNN Teacher: Graph-Aware Distillation
      on Textual Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07409999999999994
    value_note: ''
    paper_rank: 389
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.6291
    sort_std: 0.006
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: ogbn-mag
  rows:
  - model: CoE
    model_key: coe
    model_plain: CoE
    value: 0.7837
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7837
    sort_std: 0.0016
    is_best: true
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.781
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.781
    sort_std: 0.003
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.775
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.3153
    std: 0.0015
    paper_value: 0.3153
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 10
    true_value: 0.761
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4457
    value_note: ''
    paper_rank: 45
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.761
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3043
    std: 0.0025
    paper_value: 0.3043
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 12
    true_value: 0.753
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4487
    value_note: ''
    paper_rank: 45
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.753
    sort_std: 0.002
    is_best: false
  - model: R-GCN
    model_key: r-gcn
    model_plain: R-GCN
    value: 0.3977
    std: 0.0046
    paper_value: 0.3977
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 39
    true_value: 0.5
    true_std: 0.001
    value_gap_source_arxiv: '2011.09679'
    value_gap_source_title: Scalable Graph Neural Networks for Heterogeneous Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1023
    value_note: ''
    paper_rank: 42
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.5
    sort_std: 0.001
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.4751
    std: 0.0022
    paper_value: 0.4751
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 41
    true_value: 0.4751
    true_std: 0.0022
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4751
    sort_std: 0.0022
    is_best: false
  - model: Neighbor Sampling (NS)
    model_key: neighbor sampling (ns)
    model_plain: Neighbor Sampling (NS)
    value: 0.4678
    std: 0.0067
    paper_value: 0.4678
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 42
    true_value: 0.4678
    true_std: 0.0067
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4678
    sort_std: 0.0067
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.3732
    std: 0.0037
    paper_value: 0.3732
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 43
    true_value: 0.3732
    true_std: 0.0037
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3732
    sort_std: 0.0037
    is_best: false
  - model: MetaPath2Vec
    model_key: metapath2vec
    model_plain: MetaPath2Vec
    value: 0.3544
    std: 0.0036
    paper_value: 0.3544
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 45
    true_value: 0.3544
    true_std: 0.0036
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3544
    sort_std: 0.0036
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.2692
    std: 0.0026
    paper_value: 0.2692
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 46
    true_value: 0.2692
    true_std: 0.0026
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2692
    sort_std: 0.0026
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: ogbn-papers100M
  rows:
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.782
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.782
    sort_std: 0.001
    is_best: true
  - model: Graver
    model_key: graver
    model_plain: Graver
    value: 0.7762
    std: 0.0294
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 5, 2025
    date_display: Nov 2025
    date_iso: '2025-11-05'
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.7762
    sort_std: 0.0294
    is_best: true
  - model: GraphSAINT + RWSE
    model_key: graphsaint + rwse
    model_plain: GraphSAINT + RWSE
    value: 0.775
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.6329
    std: 0.0019
    paper_value: 0.6329
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 30
    true_value: 0.679
    true_std: 0.0
    value_gap_source_arxiv: '2511.06443'
    value_gap_source_title: How Wide and How Deep? Mitigating Over-Squashing of GNNs
      via Channel Capacity Constrained Estimation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04610000000000003
    value_note: ''
    paper_rank: 57
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.679
    sort_std: 0.0
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.4724
    std: 0.0031
    paper_value: 0.4724
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 68
    true_value: 0.4724
    true_std: 0.0031
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4724
    sort_std: 0.0031
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: ogbn-products
  rows:
  - model: GTs
    model_key: gts
    model_plain: GTs
    value: 0.9037
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9037
    sort_std: 0.0005
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9017
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9017
    sort_std: 0.0016
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8909
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8909
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7564
    std: 0.0021
    paper_value: 0.7564
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 22
    true_value: 0.8435
    true_std: 0.0009
    value_gap_source_arxiv: '2210.14709'
    value_gap_source_title: Learning on Large-scale Text-attributed Graphs via Variational
      Inference
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08710000000000007
    value_note: ''
    paper_rank: 86
    rank_delta: 64
    rank_delta_abs: 64
    rank_delta_direction: worse
    sort_value: 0.8435
    sort_std: 0.0009
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.785
    std: 0.0014
    paper_value: 0.785
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 27
    true_value: 0.8316
    true_std: 0.0019
    value_gap_source_arxiv: '2210.14709'
    value_gap_source_title: Learning on Large-scale Text-attributed Graphs via Variational
      Inference
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046599999999999975
    value_note: ''
    paper_rank: 73
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.8316
    sort_std: 0.0019
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.7908
    std: 0.0024
    paper_value: 0.7908
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 54
    true_value: 0.8027
    true_std: 0.0026
    value_gap_source_arxiv: '2009.03509'
    value_gap_source_title: 'Masked Label Prediction: Unified Message Passing Model
      for Semi-Supervised Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.011900000000000022
    value_note: ''
    paper_rank: 69
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.8027
    sort_std: 0.0026
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.7897
    std: 0.0033
    paper_value: 0.7897
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 63
    true_value: 0.7962
    true_std: null
    value_gap_source_arxiv: '2502.19693'
    value_gap_source_title: Accurate and Scalable Graph Neural Networks via Message
      Invariance
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006500000000000061
    value_note: ''
    paper_rank: 69
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.7962
    sort_std: null
    is_best: false
  - model: Neighbor Sampling (NS)
    model_key: neighbor sampling (ns)
    model_plain: Neighbor Sampling (NS)
    value: 0.787
    std: 0.0036
    paper_value: 0.787
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 70
    true_value: 0.787
    true_std: 0.0036
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.787
    sort_std: 0.0036
    is_best: false
  - model: Node2Vec
    model_key: node2vec
    model_plain: Node2Vec
    value: 0.7249
    std: 0.001
    paper_value: 0.7249
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 119
    true_value: 0.7249
    true_std: 0.001
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7249
    sort_std: 0.001
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.6106
    std: 0.0008
    paper_value: 0.6106
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 137
    true_value: 0.6106
    true_std: 0.0008
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6106
    sort_std: 0.0008
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: ogbn-proteins
  rows:
  - model: RevGNN-Wide
    model_key: revgnn-wide
    model_plain: RevGNN-Wide
    value: 0.8824
    std: 0.0015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8824
    sort_std: 0.0015
    is_best: true
  - model: RevGNN-Deep
    model_key: revgnn-deep
    model_plain: RevGNN-Deep
    value: 0.8774
    std: 0.0013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8774
    sort_std: 0.0013
    is_best: false
  - model: UniMP+CEF
    model_key: unimp+cef
    model_plain: UniMP+CEF
    value: 0.8691
    std: 0.0018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8691
    sort_std: 0.0018
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7768
    std: 0.002
    paper_value: 0.7768
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 12
    true_value: 0.818
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0411999999999999
    value_note: ''
    paper_rank: 19
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.818
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7251
    std: 0.0035
    paper_value: 0.7251
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 13
    true_value: 0.815
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08989999999999998
    value_note: ''
    paper_rank: 27
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.815
    sort_std: 0.003
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7204
    std: 0.0048
    paper_value: 0.7204
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 29
    true_value: 0.7204
    true_std: 0.0048
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7204
    sort_std: 0.0048
    is_best: false
  - model: Node2Vec
    model_key: node2vec
    model_plain: Node2Vec
    value: 0.6881
    std: 0.0065
    paper_value: 0.6881
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2, 2020
    date_display: May 2020
    date_iso: '2020-05-02'
    published_venue: null
    global_rank: 33
    true_value: 0.6881
    true_std: 0.0065
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6881
    sort_std: 0.0065
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
  - *id010
  - *id011
  - *id012
---

