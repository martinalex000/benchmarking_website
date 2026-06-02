---
title: Graph Inductive Biases in Transformers without Message Passing
arxiv_id: '2305.17589'
source_url: ''
authors: []
published_date: May 27, 2023
published_date_iso: '2023-05-27'
published_venue: ''
abstract: 'Transformers for graph data are increasingly widely studied and successful
  in numerous learning tasks. Graph inductive biases are crucial for Graph Transformers,
  and previous works incorporate them using message-passing modules and/or positional
  encodings. However, Graph Transformers that use message-passing inherit known issues
  of message-passing, and differ significantly from Transformers used in other domains,
  thus making transfer of research advances more difficult. On the other hand, Graph
  Transformers without message-passing often perform poorly on smaller datasets, where
  inductive biases are more crucial. To bridge this gap, we propose the Graph Inductive
  bias Transformer (GRIT) -- a new Graph Transformer that incorporates graph inductive
  biases without using message passing. GRIT is based on several architectural changes
  that are each theoretically and empirically justified, including: learned relative
  positional encodings initialized with random walk probabilities, a flexible attention
  mechanism that updates node and node-pair representations, and injection of degree
  information in each layer. We prove that GRIT is expressive -- it can express shortest
  path distances and various graph propagation matrices. GRIT achieves state-of-the-art
  empirical performance across a variety of graph datasets, thus showing the power
  that Graph Transformers without message-passing can deliver.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- ILLS
mrr: 0.2213
adjusted_mrr: 0.2213
mrr_dataset_count: 26
benchmark_categories:
- Classic
- TU Dortmund
- OGB
- Quantum Chemistry
task_categories:
- graph_classification
- graph_regression
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id012
  dataset: AQSOL
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.49
    std: 0.01
    paper_value: 0.49
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.49
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49
    sort_std: 0.01
    is_best: true
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.51
    std: 0.02
    paper_value: 0.51
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.51
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.51
    sort_std: 0.02
    is_best: true
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.52
    std: 0.02
    paper_value: 0.52
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.52
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52
    sort_std: 0.02
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.53
    std: 0.02
    paper_value: 0.53
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.53
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.02
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.55
    std: 0.02
    paper_value: 0.55
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.55
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.55
    sort_std: 0.02
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.56
    std: 0.03
    paper_value: 0.56
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.58
    std: 0.02
    paper_value: 0.58
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.58
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.58
    sort_std: 0.02
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.59
    std: 0.02
    paper_value: 0.59
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 8
    true_value: 0.59
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.59
    sort_std: 0.02
    is_best: false
  - model: Ours(100K)
    model_key: ours(100k)
    model_plain: Ours(100K)
    value: 0.92
    std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 29, 2022
    date_display: Jan 2022
    date_iso: '2022-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.92
    sort_std: 0.009
    is_best: false
  - model: GatedGCN-PE/E(500K)
    model_key: gatedgcn-pe/e(500k)
    model_plain: GatedGCN-PE/E(500K)
    value: 0.996
    std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 29, 2022
    date_display: Jan 2022
    date_iso: '2022-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.996
    sort_std: 0.008
    is_best: false
  - model: PNA(100K)
    model_key: pna(100k)
    model_plain: PNA(100K)
    value: 1.083
    std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 29, 2022
    date_display: Jan 2022
    date_iso: '2022-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 1.083
    sort_std: 0.011
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: Amazon-Computers
  rows:
  - model: CoE
    model_key: coe
    model_plain: CoE
    value: 0.9801
    std: 0.0009
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
    sort_value: 0.9801
    sort_std: 0.0009
    is_best: true
  - model: Mowst
    model_key: mowst
    model_plain: Mowst
    value: 0.9789
    std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.9789
    sort_std: 0.0044
    is_best: true
  - model: InfoMGF
    model_key: infomgf
    model_plain: InfoMGF
    value: 0.9778
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 3
    sort_value: 0.9778
    sort_std: 0.0021
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.012
    paper_value: 0.815
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 16
    true_value: 0.9312
    true_std: 0.0028
    value_gap_source_arxiv: '2505.20853'
    value_gap_source_title: arXiv:2505.20853
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11620000000000008
    value_note: ''
    paper_rank: 174
    rank_delta: 158
    rank_delta_abs: 158
    rank_delta_direction: worse
    sort_value: 0.9312
    sort_std: 0.0028
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.828
    std: 0.014
    paper_value: 0.828
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 31
    true_value: 0.9131
    true_std: 0.0029
    value_gap_source_arxiv: '2406.19258'
    value_gap_source_title: Leveraging Contrastive Learning for Enhanced Node Representations
      in Tokenized Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08510000000000006
    value_note: ''
    paper_rank: 161
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.9131
    sort_std: 0.0029
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.823
    std: 0.015
    paper_value: 0.823
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 37
    true_value: 0.9078
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0848000000000001
    value_note: ''
    paper_rank: 167
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.9078
    sort_std: 0.0013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.809
    std: 0.011
    paper_value: 0.809
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 88
    true_value: 0.8854
    true_std: 0.0069
    value_gap_source_arxiv: '2306.07608'
    value_gap_source_title: 'Finding the Missing-half: Graph Complementary Learning
      for Homophily-prone and Heterophily-prone Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07639999999999991
    value_note: ''
    paper_rank: 177
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.8854
    sort_std: 0.0069
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.812
    std: 0.01
    paper_value: 0.812
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 114
    true_value: 0.8626
    true_std: 0.0056
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05059999999999998
    value_note: ''
    paper_rank: 176
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.8626
    sort_std: 0.0056
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.841
    std: 0.009
    paper_value: 0.841
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 138
    true_value: 0.841
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.841
    sort_std: 0.009
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.835
    std: 0.013
    paper_value: 0.835
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 151
    true_value: 0.835
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.013
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Amazon-Photo
  rows:
  - model: Joint
    model_key: joint
    model_plain: Joint
    value: 0.973
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.14439'
    title: 'PUMA: Efficient Continual Graph Learning for Node Classification with
      Graph Condensation'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/superallen13/PUMA
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.973
    sort_std: 0.001
    is_best: true
  - model: DAM-GT
    model_key: dam-gt
    model_plain: DAM-GT
    value: 0.9666
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9666
    sort_std: 0.0013
    is_best: false
  - model: novel graph MLP mixer
    model_key: novel graph mlp mixer
    model_plain: novel graph MLP mixer
    value: 0.9619
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9619
    sort_std: 0.0017
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.831
    std: 0.005
    paper_value: 0.831
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 19
    true_value: 0.9498
    true_std: 0.0041
    value_gap_source_arxiv: '2406.19258'
    value_gap_source_title: Leveraging Contrastive Learning for Enhanced Node Representations
      in Tokenized Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11880000000000002
    value_note: ''
    paper_rank: 208
    rank_delta: 189
    rank_delta_abs: 189
    rank_delta_direction: worse
    sort_value: 0.9498
    sort_std: 0.0041
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.821
    std: 0.004
    paper_value: 0.821
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 37
    true_value: 0.9423
    true_std: 0.0062
    value_gap_source_arxiv: '2306.07608'
    value_gap_source_title: 'Finding the Missing-half: Graph Complementary Learning
      for Homophily-prone and Heterophily-prone Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12130000000000007
    value_note: ''
    paper_rank: 209
    rank_delta: 172
    rank_delta_abs: 172
    rank_delta_direction: worse
    sort_value: 0.9423
    sort_std: 0.0062
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.835
    std: 0.006
    paper_value: 0.835
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 53
    true_value: 0.9387
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10370000000000001
    value_note: ''
    paper_rank: 207
    rank_delta: 154
    rank_delta_abs: 154
    rank_delta_direction: worse
    sort_value: 0.9387
    sort_std: 0.0011
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.828
    std: 0.005
    paper_value: 0.828
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 93
    true_value: 0.929
    true_std: 0.04
    value_gap_source_arxiv: '2511.06443'
    value_gap_source_title: How Wide and How Deep? Mitigating Over-Squashing of GNNs
      via Channel Capacity Constrained Estimation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10100000000000009
    value_note: ''
    paper_rank: 209
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.929
    sort_std: 0.04
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.839
    std: 0.004
    paper_value: 0.839
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 114
    true_value: 0.9211
    true_std: 0.0032
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08210000000000006
    value_note: ''
    paper_rank: 205
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.9211
    sort_std: 0.0032
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.851
    std: 0.003
    paper_value: 0.851
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 203
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 203
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.842
    std: 0.003
    paper_value: 0.842
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 205
    true_value: 0.842
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 205
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id018
  dataset: COLLAB
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.8672
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8615
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8615
    sort_std: 0.001
    is_best: true
  - model: PXGL-GNN
    model_key: pxgl-gnn
    model_plain: PXGL-GNN
    value: 0.8396
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8396
    sort_std: 0.0159
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.638
    std: 0.012
    paper_value: 0.638
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 16
    true_value: 0.826
    true_std: 0.022
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18799999999999994
    value_note: ''
    paper_rank: 180
    rank_delta: 164
    rank_delta_abs: 164
    rank_delta_direction: worse
    sort_value: 0.826
    sort_std: 0.022
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.649
    std: 0.013
    paper_value: 0.649
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 21
    true_value: 0.822
    true_std: 0.021
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17299999999999993
    value_note: ''
    paper_rank: 176
    rank_delta: 155
    rank_delta_abs: 155
    rank_delta_direction: worse
    sort_value: 0.822
    sort_std: 0.021
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.645
    std: 0.015
    paper_value: 0.645
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 88
    true_value: 0.797
    true_std: 0.017
    value_gap_source_arxiv: '2008.05089'
    value_gap_source_title: Quaternion Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15200000000000002
    value_note: ''
    paper_rank: 177
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.797
    sort_std: 0.017
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.652
    std: 0.011
    paper_value: 0.652
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 127
    true_value: 0.758
    true_std: 0.016
    value_gap_source_arxiv: '2008.05089'
    value_gap_source_title: Quaternion Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10599999999999998
    value_note: ''
    paper_rank: 176
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.758
    sort_std: 0.016
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.661
    std: 0.009
    paper_value: 0.661
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 138
    true_value: 0.7473
    true_std: 0.0109
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08629999999999993
    value_note: ''
    paper_rank: 172
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.7473
    sort_std: 0.0109
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.674
    std: 0.008
    paper_value: 0.674
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 168
    true_value: 0.674
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.674
    sort_std: 0.008
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.655
    std: 0.01
    paper_value: 0.655
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 175
    true_value: 0.655
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.655
    sort_std: 0.01
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.952
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.952
    sort_std: 0.002
    is_best: true
  - model: Policy-GNN
    model_key: policy-gnn
    model_plain: Policy-GNN
    value: 0.897
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_display: Jun 2020
    date_iso: 2020-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.897
    sort_std: 0.021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.721
    std: 0.015
    paper_value: 0.721
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.88
    true_std: null
    value_gap_source_arxiv: '1805.07984'
    value_gap_source_title: Adversarial Attacks on Neural Networks for Graph Data
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15900000000000003
    value_note: ''
    paper_rank: 362
    rank_delta: 359
    rank_delta_abs: 359
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: null
    is_best: false
  - model: AdaptKry
    model_key: adaptkry
    model_plain: AdaptKry
    value: 0.8378
    std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8378
    sort_std: 0.0038
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.715
    std: 0.018
    paper_value: 0.715
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.8269
    true_std: null
    value_gap_source_arxiv: '2106.09078'
    value_gap_source_title: 'Probing GNN Explainers: A Rigorous Theoretical and Empirical
      Analysis of GNN Explanation Methods'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1119
    value_note: ''
    paper_rank: 388
    rank_delta: 382
    rank_delta_abs: 382
    rank_delta_direction: worse
    sort_value: 0.8269
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.728
    std: 0.012
    paper_value: 0.728
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 8
    true_value: 0.8227
    true_std: 0.0068
    value_gap_source_arxiv: '2411.17676'
    value_gap_source_title: Instance-Aware Graph Prompt Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0947
    value_note: ''
    paper_rank: 320
    rank_delta: 312
    rank_delta_abs: 312
    rank_delta_direction: worse
    sort_value: 0.8227
    sort_std: 0.0068
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.735
    std: 0.011
    paper_value: 0.735
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 36
    true_value: 0.7933
    true_std: 0.0084
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05830000000000002
    value_note: ''
    paper_rank: 259
    rank_delta: 223
    rank_delta_abs: 223
    rank_delta_direction: worse
    sort_value: 0.7933
    sort_std: 0.0084
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.758
    std: 0.008
    paper_value: 0.758
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 131
    true_value: 0.758
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.008
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.742
    std: 0.009
    paper_value: 0.742
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 159
    true_value: 0.752
    true_std: 0.01
    value_gap_source_arxiv: '2202.13060'
    value_gap_source_title: Graph Attention Retrospective
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.010000000000000009
    value_note: ''
    paper_rank: 210
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.752
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.725
    std: 0.014
    paper_value: 0.725
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 321
    true_value: 0.728
    true_std: 0.013
    value_gap_source_arxiv: '2202.13060'
    value_gap_source_title: Graph Attention Retrospective
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0030000000000000027
    value_note: global 0.7280 within std
    paper_rank: 339
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.728
    sort_std: 0.013
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Coauthor-CS
  rows:
  - model: DAM-GT
    model_key: dam-gt
    model_plain: DAM-GT
    value: 0.9626
    std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9626
    sort_std: 0.0008
    is_best: true
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9589
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9577
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9577
    sort_std: 0.0015
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.835
    std: 0.005
    paper_value: 0.835
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 27
    true_value: 0.9461
    true_std: 0.0003
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11110000000000009
    value_note: ''
    paper_rank: 184
    rank_delta: 157
    rank_delta_abs: 157
    rank_delta_direction: worse
    sort_value: 0.9461
    sort_std: 0.0003
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.848
    std: 0.005
    paper_value: 0.848
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 31
    true_value: 0.9449
    true_std: 0.0007
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09689999999999999
    value_note: ''
    paper_rank: 178
    rank_delta: 147
    rank_delta_abs: 147
    rank_delta_direction: worse
    sort_value: 0.9449
    sort_std: 0.0007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.842
    std: 0.006
    paper_value: 0.842
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 45
    true_value: 0.9371
    true_std: 0.004
    value_gap_source_arxiv: '2411.12330'
    value_gap_source_title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09510000000000007
    value_note: ''
    paper_rank: 181
    rank_delta: 136
    rank_delta_abs: 136
    rank_delta_direction: worse
    sort_value: 0.9371
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.831
    std: 0.004
    paper_value: 0.831
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 65
    true_value: 0.9306
    true_std: 0.008
    value_gap_source_arxiv: '2102.03147'
    value_gap_source_title: Learning Conjoint Attentions for Graph Neural Nets
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09960000000000002
    value_note: ''
    paper_rank: 187
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.9306
    sort_std: 0.008
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.839
    std: 0.005
    paper_value: 0.839
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 67
    true_value: 0.9303
    true_std: 0.0074
    value_gap_source_arxiv: '2102.03147'
    value_gap_source_title: Learning Conjoint Attentions for Graph Neural Nets
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09130000000000005
    value_note: ''
    paper_rank: 182
    rank_delta: 115
    rank_delta_abs: 115
    rank_delta_direction: worse
    sort_value: 0.9303
    sort_std: 0.0074
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.003
    paper_value: 0.862
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 170
    true_value: 0.862
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.851
    std: 0.004
    paper_value: 0.851
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 177
    true_value: 0.851
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 177
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: Coauthor-Physics
  rows:
  - model: DAM-GT
    model_key: dam-gt
    model_plain: DAM-GT
    value: 0.974
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.974
    sort_std: 0.0004
    is_best: true
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.9734
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9734
    sort_std: 0.0003
    is_best: true
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.9734
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9734
    sort_std: 0.0004
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.938
    std: 0.004
    paper_value: 0.938
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 11
    true_value: 0.9654
    true_std: 0.0007
    value_gap_source_arxiv: '2505.17660'
    value_gap_source_title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking
      Graph Transformer for Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02740000000000009
    value_note: ''
    paper_rank: 75
    rank_delta: 64
    rank_delta_abs: 64
    rank_delta_direction: worse
    sort_value: 0.9654
    sort_std: 0.0007
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.932
    std: 0.005
    paper_value: 0.932
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 19
    true_value: 0.9618
    true_std: 0.0007
    value_gap_source_arxiv: '2505.17660'
    value_gap_source_title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking
      Graph Transformer for Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029799999999999938
    value_note: ''
    paper_rank: 86
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.9618
    sort_std: 0.0007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.935
    std: 0.004
    paper_value: 0.935
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 20
    true_value: 0.9617
    true_std: 0.0008
    value_gap_source_arxiv: '2505.17660'
    value_gap_source_title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking
      Graph Transformer for Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026699999999999946
    value_note: ''
    paper_rank: 79
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.9617
    sort_std: 0.0008
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.945
    std: 0.003
    paper_value: 0.945
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 63
    true_value: 0.945
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.945
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.941
    std: 0.003
    paper_value: 0.941
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 68
    true_value: 0.941
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.941
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.93
    std: 0.005
    paper_value: 0.93
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 76
    true_value: 0.9379
    true_std: 0.0049
    value_gap_source_arxiv: '2003.02228'
    value_gap_source_title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007899999999999907
    value_note: ''
    paper_rank: 87
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.9379
    sort_std: 0.0049
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.928
    std: 0.006
    paper_value: 0.928
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 87
    true_value: 0.931
    true_std: 0.004
    value_gap_source_arxiv: '2403.03483'
    value_gap_source_title: A Teacher-Free Graph Knowledge Distillation Framework
      with Dual Self-Distillation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0030000000000000027
    value_note: global 0.9310 within std
    paper_rank: 89
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.931
    sort_std: 0.004
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.925
    std: 0.007
    paper_value: 0.925
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 88
    true_value: 0.93
    true_std: 0.004
    value_gap_source_arxiv: '2403.03483'
    value_gap_source_title: A Teacher-Free Graph Knowledge Distillation Framework
      with Dual Self-Distillation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0050000000000000044
    value_note: global 0.9300 within std
    paper_rank: 94
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.93
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: Self-Explainable GNN
    model_key: self-explainable gnn
    model_plain: Self-Explainable GNN
    value: 0.977
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.977
    sort_std: 0.016
    is_best: true
  - model: GCN-K
    model_key: gcn-k
    model_plain: GCN-K
    value: 0.948
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.007
    is_best: false
  - model: KP-GIN
    model_key: kp-gin
    model_plain: KP-GIN
    value: 0.946
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.946
    sort_std: 0.007
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.005
    paper_value: 0.815
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 22
    true_value: 0.9004
    true_std: null
    value_gap_source_arxiv: '2401.09125'
    value_gap_source_title: arXiv:2401.09125
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08540000000000003
    value_note: ''
    paper_rank: 508
    rank_delta: 486
    rank_delta_abs: 486
    rank_delta_direction: worse
    sort_value: 0.9004
    sort_std: null
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.825
    std: 0.006
    paper_value: 0.825
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 24
    true_value: 0.8998
    true_std: null
    value_gap_source_arxiv: '2602.00064'
    value_gap_source_title: 'SPGCL: Simple yet Powerful Graph Contrastive Learning
      via SVD-Guided Structural Perturbation'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07480000000000009
    value_note: ''
    paper_rank: 440
    rank_delta: 416
    rank_delta_abs: 416
    rank_delta_direction: worse
    sort_value: 0.8998
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.828
    std: 0.007
    paper_value: 0.828
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 50
    true_value: 0.8904
    true_std: 0.015
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06240000000000001
    value_note: ''
    paper_rank: 421
    rank_delta: 371
    rank_delta_abs: 371
    rank_delta_direction: worse
    sort_value: 0.8904
    sort_std: 0.015
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.83
    std: 0.008
    paper_value: 0.83
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 54
    true_value: 0.8897
    true_std: null
    value_gap_source_arxiv: '2605.24867'
    value_gap_source_title: 'Clustering as Reasoning: A $k$-Means Interpretation of
      Chain-of-Thought Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059700000000000086
    value_note: ''
    paper_rank: 404
    rank_delta: 350
    rank_delta_abs: 350
    rank_delta_direction: worse
    sort_value: 0.8897
    sort_std: null
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.842
    std: 0.003
    paper_value: 0.842
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 287
    true_value: 0.842
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 287
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.835
    std: 0.004
    paper_value: 0.835
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 355
    true_value: 0.835
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 355
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: D&D
  rows:
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 25, 2025
    date_display: Nov 2025
    date_iso: '2025-11-25'
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: DC-GSAT
    model_key: dc-gsat
    model_plain: DC-GSAT
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: DC-SMGNN
    model_key: dc-smgnn
    model_plain: DC-SMGNN
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.798
    std: 0.013
    paper_value: 0.798
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.99
    true_std: 0.01
    value_gap_source_arxiv: '2502.02719'
    value_gap_source_title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability
      Perspective'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19199999999999995
    value_note: ''
    paper_rank: 78
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.99
    sort_std: 0.01
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.801
    std: 0.011
    paper_value: 0.801
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 27
    true_value: 0.9
    true_std: null
    value_gap_source_arxiv: '2511.20406'
    value_gap_source_title: Short-Range Oversquashing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09899999999999998
    value_note: ''
    paper_rank: 75
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.9
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.825
    std: 0.008
    paper_value: 0.825
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 54
    true_value: 0.825
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.008
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.814
    std: 0.009
    paper_value: 0.814
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 65
    true_value: 0.814
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.814
    sort_std: 0.009
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.795
    std: 0.012
    paper_value: 0.795
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 85
    true_value: 0.795
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.782
    std: 0.015
    paper_value: 0.782
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 90
    true_value: 0.7912
    true_std: 0.0307
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009199999999999986
    value_note: global 0.7912 within std
    paper_rank: 118
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.7912
    sort_std: 0.0307
    is_best: false
  - model: Jumping Knowledge
    model_key: jumping knowledge
    model_plain: Jumping Knowledge
    value: 0.788
    std: 0.014
    paper_value: 0.788
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 103
    true_value: 0.788
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.014
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.775
    std: 0.018
    paper_value: 0.775
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 133
    true_value: 0.775
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.018
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id019
  dataset: ENZYMES
  rows:
  - model: C-M
    model_key: c-m
    model_plain: C-M
    value: 0.802
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.802
    sort_std: 0.009
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.794
    std: 0.008
    paper_value: 0.794
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.794
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.008
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.756
    std: 0.011
    paper_value: 0.756
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.785
    true_std: 0.01
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029000000000000026
    value_note: ''
    paper_rank: 11
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.785
    sort_std: 0.01
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.78
    std: 0.0489
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_display: Dec 2020
    date_iso: 2020-12
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.78
    sort_std: 0.0489
    is_best: true
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.779
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.779
    sort_std: 0.011
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.778
    std: 0.009
    paper_value: 0.778
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.778
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.778
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.741
    std: 0.014
    paper_value: 0.741
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.771
    true_std: 0.012
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.030000000000000027
    value_note: ''
    paper_rank: 12
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.771
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.723
    std: 0.015
    paper_value: 0.723
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 9
    true_value: 0.762
    true_std: 0.015
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.039000000000000035
    value_note: ''
    paper_rank: 14
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.015
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.762
    std: 0.01
    paper_value: 0.762
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 10
    true_value: 0.762
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.01
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.735
    std: 0.012
    paper_value: 0.735
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 11
    true_value: 0.758
    true_std: 0.018
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02300000000000002
    value_note: ''
    paper_rank: 12
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.758
    sort_std: 0.018
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.718
    std: 0.018
    paper_value: 0.718
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 12
    true_value: 0.745
    true_std: 0.021
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.027000000000000024
    value_note: ''
    paper_rank: 14
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.745
    sort_std: 0.021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id016
  dataset: IMDB-BINARY
  rows:
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.722
    std: 0.015
    paper_value: 0.722
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.834
    true_std: 0.049
    value_gap_source_arxiv: '2205.12245'
    value_gap_source_title: Asynchronous Neural Networks for Learning in Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11199999999999999
    value_note: ''
    paper_rank: 155
    rank_delta: 154
    rank_delta_abs: 154
    rank_delta_direction: worse
    sort_value: 0.834
    sort_std: 0.049
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.83
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_display: Mar 2022
    date_iso: 2022-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.83
    sort_std: 0.032
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8267
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.811
    std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.785
    std: 0.006
    paper_value: 0.785
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 8
    true_value: 0.785
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.006
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.771
    std: 0.007
    paper_value: 0.771
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 18
    true_value: 0.771
    true_std: 0.007
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.007
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.745
    std: 0.013
    paper_value: 0.745
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 27
    true_value: 0.762
    true_std: 0.004
    value_gap_source_arxiv: '2110.09344'
    value_gap_source_title: 'ifMixup: Interpolating Graph Pair to Regularize Graph
      Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017000000000000015
    value_note: ''
    paper_rank: 71
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.004
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.762
    std: 0.008
    paper_value: 0.762
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 28
    true_value: 0.762
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.008
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.735
    std: 0.012
    paper_value: 0.735
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 35
    true_value: 0.76
    true_std: 0.033
    value_gap_source_arxiv: '2205.12245'
    value_gap_source_title: Asynchronous Neural Networks for Learning in Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.025000000000000022
    value_note: global 0.7600 within std
    paper_rank: 112
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.033
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.758
    std: 0.009
    paper_value: 0.758
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 40
    true_value: 0.758
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.741
    std: 0.011
    paper_value: 0.741
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 46
    true_value: 0.755
    true_std: 0.017
    value_gap_source_arxiv: '2110.09344'
    value_gap_source_title: 'ifMixup: Interpolating Graph Pair to Regularize Graph
      Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.014000000000000012
    value_note: global 0.7550 within std
    paper_rank: 89
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.755
    sort_std: 0.017
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id020
  dataset: IMDB-MULTI
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.724
    std: 0.009
    paper_value: 0.724
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.724
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.724
    sort_std: 0.009
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.712
    std: 0.011
    paper_value: 0.712
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.712
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.712
    sort_std: 0.011
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.705
    std: 0.01
    paper_value: 0.705
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.705
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.01
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.701
    std: 0.014
    paper_value: 0.701
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.701
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.014
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.698
    std: 0.013
    paper_value: 0.698
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.698
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.698
    sort_std: 0.013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.695
    std: 0.012
    paper_value: 0.695
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.695
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.682
    std: 0.015
    paper_value: 0.682
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.682
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.682
    sort_std: 0.015
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.5731
    std: 0.0219
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.5731
    sort_std: 0.0219
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.5632
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.5632
    sort_std: 0.0018
    is_best: false
  - model: HAP
    model_key: hap
    model_plain: HAP
    value: 0.5533
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_display: Apr 2021
    date_iso: 2021-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.5533
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: MUTAG
  rows:
  - model: RC-Explainer
    model_key: rc-explainer
    model_plain: RC-Explainer
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_display: Apr 2022
    date_iso: 2022-04
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.983
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_display: Mar 2022
    date_iso: 2022-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.983
    sort_std: 0.025
    is_best: true
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.9805
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08816'
    title: Learning and Evaluating Graph Neural Network Explanations based on Counterfactual
      and Factual Reasoning
    date: Feb 2022
    date_display: Feb 2022
    date_iso: 2022-02
    codebase_url: https://github.com/chrisjtan/gnn_cff
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9805
    sort_std: null
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.86
    std: 0.015
    paper_value: 0.86
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 17
    true_value: 0.9265
    true_std: 0.0153
    value_gap_source_arxiv: '2512.04530'
    value_gap_source_title: Explainable Graph Representation Learning via Graph Pattern
      Analysis
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0665
    value_note: ''
    paper_rank: 126
    rank_delta: 109
    rank_delta_abs: 109
    rank_delta_direction: worse
    sort_value: 0.9265
    sort_std: 0.0153
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.835
    std: 0.025
    paper_value: 0.835
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 59
    true_value: 0.8945
    true_std: 0.0614
    value_gap_source_arxiv: '2506.20362'
    value_gap_source_title: Self-Supervised Graph Learning via Spectral Bootstrapping
      and Laplacian-Based Augmentations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0595
    value_note: global 0.8945 within std
    paper_rank: 179
    rank_delta: 120
    rank_delta_abs: 120
    rank_delta_direction: worse
    sort_value: 0.8945
    sort_std: 0.0614
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.83
    std: 0.02
    paper_value: 0.83
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 62
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '1912.06058'
    value_gap_source_title: Coloring graph neural networks for node disambiguation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06400000000000006
    value_note: ''
    paper_rank: 192
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.885
    std: 0.01
    paper_value: 0.885
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 81
    true_value: 0.885
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.885
    sort_std: 0.01
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.825
    std: 0.021
    paper_value: 0.825
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 109
    true_value: 0.872
    true_std: 0.0511
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.04700000000000004
    value_note: global 0.8720 within std
    paper_rank: 210
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.872
    sort_std: 0.0511
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.87
    std: 0.012
    paper_value: 0.87
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 111
    true_value: 0.87
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87
    sort_std: 0.012
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.815
    std: 0.023
    paper_value: 0.815
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 117
    true_value: 0.8635
    true_std: 0.0131
    value_gap_source_arxiv: '2512.04530'
    value_gap_source_title: Explainable Graph Representation Learning via Graph Pattern
      Analysis
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0485000000000001
    value_note: ''
    paper_rank: 235
    rank_delta: 118
    rank_delta_abs: 118
    rank_delta_direction: worse
    sort_value: 0.8635
    sort_std: 0.0131
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.85
    std: 0.018
    paper_value: 0.85
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 149
    true_value: 0.85
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.018
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.84
    std: 0.022
    paper_value: 0.84
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 165
    true_value: 0.84
    true_std: 0.022
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.022
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id017
  dataset: NCI1
  rows:
  - model: MSA-AU
    model_key: msa-au
    model_plain: MSA-AU
    value: 0.962
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.962
    sort_std: null
    is_best: true
  - model: MSA-AD
    model_key: msa-ad
    model_plain: MSA-AD
    value: 0.947
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.947
    sort_std: null
    is_best: false
  - model: JbDA
    model_key: jbda
    model_plain: JbDA
    value: 0.912
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.912
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.874
    std: 0.003
    paper_value: 0.874
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.874
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.874
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.862
    std: 0.004
    paper_value: 0.862
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.862
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.004
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.858
    std: 0.005
    paper_value: 0.858
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 10
    true_value: 0.858
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.858
    sort_std: 0.005
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.851
    std: 0.003
    paper_value: 0.851
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 13
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.845
    std: 0.004
    paper_value: 0.845
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 15
    true_value: 0.845
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.838
    std: 0.006
    paper_value: 0.838
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 21
    true_value: 0.838
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.838
    sort_std: 0.006
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.832
    std: 0.005
    paper_value: 0.832
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 23
    true_value: 0.8365
    true_std: 0.0169
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0045000000000000595
    value_note: global 0.8365 within std
    paper_rank: 30
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8365
    sort_std: 0.0169
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id030
  dataset: PCQM4Mv2
  rows:
  - model: DeMol
    model_key: demol
    model_plain: DeMol
    value: 0.0603
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0603
    sort_std: null
    is_best: true
  - model: TGT-At
    model_key: tgt-at
    model_plain: TGT-At
    value: 0.0671
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0671
    sort_std: null
    is_best: false
  - model: Unimol+
    model_key: unimol+
    model_plain: Unimol+
    value: 0.0693
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0693
    sort_std: null
    is_best: false
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.124
    std: 0.001
    paper_value: 0.124
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 36
    true_value: 0.098
    true_std: 0.001
    value_gap_source_arxiv: '2107.09422'
    value_gap_source_title: Large-scale graph representation learning with very deep
      GNNs and self-supervision
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025999999999999995
    value_note: ''
    paper_rank: 51
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.098
    sort_std: 0.001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.128
    std: 0.001
    paper_value: 0.128
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 43
    true_value: 0.115
    true_std: 0.001
    value_gap_source_arxiv: '2107.09422'
    value_gap_source_title: Large-scale graph representation learning with very deep
      GNNs and self-supervision
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012999999999999998
    value_note: ''
    paper_rank: 53
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.115
    sort_std: 0.001
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.119
    std: 0.001
    paper_value: 0.119
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 45
    true_value: 0.119
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.119
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.132
    std: 0.002
    paper_value: 0.132
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 47
    true_value: 0.1195
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012500000000000011
    value_note: ''
    paper_rank: 54
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.1195
    sort_std: null
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.121
    std: 0.001
    paper_value: 0.121
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 48
    true_value: 0.121
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.121
    sort_std: 0.001
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.122
    std: 0.001
    paper_value: 0.122
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 49
    true_value: 0.122
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.122
    sort_std: 0.001
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.123
    std: 0.001
    paper_value: 0.123
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 51
    true_value: 0.123
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.123
    sort_std: 0.001
    is_best: false
  - model: PNA + RWSE
    model_key: pna + rwse
    model_plain: PNA + RWSE
    value: 0.125
    std: 0.001
    paper_value: 0.125
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 52
    true_value: 0.125
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.125
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.135
    std: 0.003
    paper_value: 0.135
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 54
    true_value: 0.1302
    true_std: null
    value_gap_source_arxiv: '2312.13136'
    value_gap_source_title: Molecular Hypergraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.004799999999999999
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1302
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.136
    std: 0.002
    paper_value: 0.136
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 55
    true_value: 0.135
    true_std: 0.002
    value_gap_source_arxiv: '2107.09422'
    value_gap_source_title: Large-scale graph representation learning with very deep
      GNNs and self-supervision
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010000000000000009
    value_note: global 0.1350 within std
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.135
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.138
    std: 0.004
    paper_value: 0.138
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 56
    true_value: 0.138
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.138
    sort_std: 0.004
    is_best: false
  metric: MAE
  higher_is_better: false
- &id010
  dataset: PPI
  rows:
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.9956
    std: 0.0002
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 4, 2020
    date_display: Jul 2020
    date_iso: '2020-07-04'
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9956
    sort_std: 0.0002
    is_best: true
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.9936
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 4, 2020
    date_display: Jul 2020
    date_iso: '2020-07-04'
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9936
    sort_std: null
    is_best: false
  - model: GBP
    model_key: gbp
    model_plain: GBP
    value: 0.993
    std: 0.0002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 29, 2020
    date_display: Oct 2020
    date_iso: '2020-10-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.993
    sort_std: 0.0002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.931
    std: 0.003
    paper_value: 0.931
    paper_std: 0.003
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 21
    true_value: 0.9732
    true_std: 0.0032
    value_gap_source_arxiv: '2301.12063'
    value_gap_source_title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical
      Adaptive Masking and Trainable Corruption'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042199999999999904
    value_note: ''
    paper_rank: 39
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.9732
    sort_std: 0.0032
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.935
    std: 0.001
    paper_value: 0.935
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 27
    true_value: 0.965
    true_std: 0.001
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029999999999999916
    value_note: ''
    paper_rank: 38
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.965
    sort_std: 0.001
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.928
    std: 0.001
    paper_value: 0.928
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 28
    true_value: 0.963
    true_std: 0.001
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03499999999999992
    value_note: ''
    paper_rank: 39
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.963
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.929
    std: 0.002
    paper_value: 0.929
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 30
    true_value: 0.962
    true_std: 0.002
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03299999999999992
    value_note: ''
    paper_rank: 39
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.962
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.926
    std: 0.002
    paper_value: 0.926
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 31
    true_value: 0.961
    true_std: 0.002
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03499999999999992
    value_note: ''
    paper_rank: 40
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.961
    sort_std: 0.002
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.942
    std: 0.001
    paper_value: 0.942
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 38
    true_value: 0.942
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.942
    sort_std: 0.001
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.933
    std: 0.002
    paper_value: 0.933
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 39
    true_value: 0.933
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.933
    sort_std: 0.002
    is_best: false
  metric: F1
  higher_is_better: true
- &id014
  dataset: PROTEINS
  rows:
  - model: HGP-SL
    model_key: hgp-sl
    model_plain: HGP-SL
    value: 0.8491
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8491
    sort_std: 0.0162
    is_best: true
  - model: rLap
    model_key: rlap
    model_plain: rLap
    value: 0.8434
    std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8434
    sort_std: 0.0403
    is_best: true
  - model: HGP-SL_DEN
    model_key: hgp-sl_den
    model_plain: HGP-SL_DEN
    value: 0.8312
    std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8312
    sort_std: 0.0084
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.802
    std: 0.009
    paper_value: 0.802
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 20
    true_value: 0.802
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.802
    sort_std: 0.009
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.795
    std: 0.01
    paper_value: 0.795
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 27
    true_value: 0.795
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.01
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.791
    std: 0.011
    paper_value: 0.791
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 33
    true_value: 0.791
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.011
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.788
    std: 0.013
    paper_value: 0.788
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 36
    true_value: 0.788
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.013
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.785
    std: 0.012
    paper_value: 0.785
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 38
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.012
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.779
    std: 0.014
    paper_value: 0.779
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 47
    true_value: 0.779
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.014
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.772
    std: 0.015
    paper_value: 0.772
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 67
    true_value: 0.772
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.015
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.768
    std: 0.018
    paper_value: 0.768
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 79
    true_value: 0.768
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.018
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: AIO
    model_key: aio
    model_plain: AIO
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.96
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.96
    sort_std: 0.001
    is_best: false
  - model: SAGN
    model_key: sagn
    model_plain: SAGN
    value: 0.9517
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9517
    sort_std: null
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.808
    std: 0.004
    paper_value: 0.808
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.9487000000000001
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14070000000000005
    value_note: ''
    paper_rank: 332
    rank_delta: 325
    rank_delta_abs: 325
    rank_delta_direction: worse
    sort_value: 0.9487000000000001
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.812
    std: 0.005
    paper_value: 0.812
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 29
    true_value: 0.9296
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11759999999999993
    value_note: ''
    paper_rank: 320
    rank_delta: 291
    rank_delta_abs: 291
    rank_delta_direction: worse
    sort_value: 0.9296
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.815
    std: 0.006
    paper_value: 0.815
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 31
    true_value: 0.9233
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10830000000000006
    value_note: ''
    paper_rank: 311
    rank_delta: 280
    rank_delta_abs: 280
    rank_delta_direction: worse
    sort_value: 0.9233
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.818
    std: 0.005
    paper_value: 0.818
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 93
    true_value: 0.894
    true_std: null
    value_gap_source_arxiv: '2206.14418'
    value_gap_source_title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07600000000000007
    value_note: ''
    paper_rank: 304
    rank_delta: 211
    rank_delta_abs: 211
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.825
    std: 0.003
    paper_value: 0.825
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 282
    true_value: 0.825
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 282
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.821
    std: 0.004
    paper_value: 0.821
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 294
    true_value: 0.821
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 294
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.821
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id036
  dataset: QM9
  rows:
  - model: TensorNet 0L
    model_key: tensornet 0l
    model_plain: TensorNet 0L
    value: 0.0039
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.17660'
    title: 'TorchMD-Net 2.0: Fast Neural Network Potentials for Molecular Simulations'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/torchmd/torchmd-net
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0039
    sort_std: null
    is_best: true
  - model: MACE
    model_key: mace
    model_plain: MACE
    value: 0.0041
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.17660'
    title: 'TorchMD-Net 2.0: Fast Neural Network Potentials for Molecular Simulations'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/torchmd/torchmd-net
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0041
    sort_std: null
    is_best: false
  - model: Allegro
    model_key: allegro
    model_plain: Allegro
    value: 0.0047
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.17660'
    title: 'TorchMD-Net 2.0: Fast Neural Network Potentials for Molecular Simulations'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/torchmd/torchmd-net
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0047
    sort_std: null
    is_best: false
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.028
    std: 0.001
    paper_value: 0.028
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.0059
    true_std: null
    value_gap_source_arxiv: '2402.17660'
    value_gap_source_title: 'TorchMD-Net 2.0: Fast Neural Network Potentials for Molecular
      Simulations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0221
    value_note: ''
    paper_rank: 42
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.0059
    sort_std: null
    is_best: false
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.033
    std: 0.001
    paper_value: 0.033
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.0063
    true_std: null
    value_gap_source_arxiv: '2402.17660'
    value_gap_source_title: 'TorchMD-Net 2.0: Fast Neural Network Potentials for Molecular
      Simulations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0267
    value_note: ''
    paper_rank: 47
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.0063
    sort_std: null
    is_best: false
  - model: SphereNet
    model_key: spherenet
    model_plain: SphereNet
    value: 0.026
    std: 0.001
    paper_value: 0.026
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 8
    true_value: 0.0063
    true_std: null
    value_gap_source_arxiv: '2402.17660'
    value_gap_source_title: 'TorchMD-Net 2.0: Fast Neural Network Potentials for Molecular
      Simulations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0197
    value_note: ''
    paper_rank: 40
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.0063
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.025
    std: 0.001
    paper_value: 0.025
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 38
    true_value: 0.025
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.025
    sort_std: 0.001
    is_best: false
  - model: EquiBind
    model_key: equibind
    model_plain: EquiBind
    value: 0.045
    std: 0.002
    paper_value: 0.045
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 56
    true_value: 0.045
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.045
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.048
    std: 0.002
    paper_value: 0.048
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 59
    true_value: 0.048
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.048
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.051
    std: 0.002
    paper_value: 0.051
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 60
    true_value: 0.051
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.051
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.056
    std: 0.003
    paper_value: 0.056
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 63
    true_value: 0.056
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.056
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
- &id022
  dataset: REDDIT-BINARY
  rows:
  - model: PEs
    model_key: pes
    model_plain: PEs
    value: 0.945
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 3, 2025
    date_display: Feb 2025
    date_iso: '2025-02-03'
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.881
    std: 0.004
    paper_value: 0.881
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.936
    true_std: null
    value_gap_source_arxiv: '2209.03473'
    value_gap_source_title: Higher-order Clustering and Pooling for Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05500000000000005
    value_note: ''
    paper_rank: 36
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.936
    sort_std: null
    is_best: false
  - model: Base
    model_key: base
    model_plain: Base
    value: 0.936
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_display: Sep 2022
    date_iso: 2022-09
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.936
    sort_std: null
    is_best: false
  - model: CapsNets
    model_key: capsnets
    model_plain: CapsNets
    value: 0.9315
    std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_display: Dec 2020
    date_iso: 2020-12
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9315
    sort_std: 0.0158
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.878
    std: 0.003
    paper_value: 0.878
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 10
    true_value: 0.915
    true_std: null
    value_gap_source_arxiv: '2209.03473'
    value_gap_source_title: Higher-order Clustering and Pooling for Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03700000000000003
    value_note: ''
    paper_rank: 39
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.915
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.894
    std: 0.002
    paper_value: 0.894
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 29
    true_value: 0.894
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.889
    std: 0.002
    paper_value: 0.889
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 33
    true_value: 0.889
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.889
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.885
    std: 0.003
    paper_value: 0.885
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 35
    true_value: 0.885
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.885
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.872
    std: 0.004
    paper_value: 0.872
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 41
    true_value: 0.872
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.872
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.865
    std: 0.005
    paper_value: 0.865
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 44
    true_value: 0.865
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.865
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id021
  dataset: REDDIT-MULTI-5K
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.871
    std: 0.002
    paper_value: 0.871
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.871
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.871
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.862
    std: 0.003
    paper_value: 0.862
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.862
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.856
    std: 0.002
    paper_value: 0.856
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.856
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.856
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.851
    std: 0.003
    paper_value: 0.851
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.848
    std: 0.004
    paper_value: 0.848
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.848
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.848
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.842
    std: 0.002
    paper_value: 0.842
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.842
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.835
    std: 0.003
    paper_value: 0.835
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.835
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.003
    is_best: false
  - model: R-PEs
    model_key: r-pes
    model_plain: R-PEs
    value: 0.606
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 3, 2025
    date_display: Feb 2025
    date_iso: '2025-02-03'
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.606
    sort_std: 0.003
    is_best: false
  - model: SRF (RBF, AG)
    model_key: srf (rbf, ag)
    model_plain: SRF (RBF, AG)
    value: 0.6053
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.03824'
    title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
      Neural Networks
    date: Nov 5, 2025
    date_display: Nov 2025
    date_iso: '2025-11-05'
    codebase_url: https://github.com/ryienh/sketched-random-features
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.6053
    sort_std: 0.0029
    is_best: false
  - model: SRF (L, AG)
    model_key: srf (l, ag)
    model_plain: SRF (L, AG)
    value: 0.6033
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.03824'
    title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
      Neural Networks
    date: Nov 5, 2025
    date_display: Nov 2025
    date_iso: '2025-11-05'
    codebase_url: https://github.com/ryienh/sketched-random-features
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.6033
    sort_std: 0.0037
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Reddit
  rows:
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.968
    std: 0.0
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 23, 2020
    date_display: Apr 2020
    date_iso: '2020-04-23'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.968
    sort_std: 0.0
    is_best: true
  - model: Neighbor2Seq+Conv
    model_key: neighbor2seq+conv
    model_plain: Neighbor2Seq+Conv
    value: 0.967
    std: 0.0
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 7, 2022
    date_display: Feb 2022
    date_iso: '2022-02-07'
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.967
    sort_std: 0.0
    is_best: false
  - model: Neighbor2Seq+Attn
    model_key: neighbor2seq+attn
    model_plain: Neighbor2Seq+Attn
    value: 0.967
    std: 0.0
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 7, 2022
    date_display: Feb 2022
    date_iso: '2022-02-07'
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.967
    sort_std: 0.0
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.935
    std: 0.001
    paper_value: 0.935
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 17
    true_value: 0.957
    true_std: null
    value_gap_source_arxiv: '2206.07161'
    value_gap_source_title: arXiv:2206.07161
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02199999999999991
    value_note: ''
    paper_rank: 37
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.957
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.941
    std: 0.001
    paper_value: 0.941
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 31
    true_value: 0.941
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.941
    sort_std: 0.001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.938
    std: 0.001
    paper_value: 0.938
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 33
    true_value: 0.938
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.938
    sort_std: 0.001
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.937
    std: 0.001
    paper_value: 0.937
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 34
    true_value: 0.937
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.937
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.936
    std: 0.001
    paper_value: 0.936
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 36
    true_value: 0.936
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.936
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.934
    std: 0.002
    paper_value: 0.934
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 38
    true_value: 0.934
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.934
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.933
    std: 0.002
    paper_value: 0.933
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 39
    true_value: 0.933
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.933
    sort_std: 0.002
    is_best: false
  metric: F1
  higher_is_better: true
- &id009
  dataset: WikiCS
  rows:
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9589
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: true
  - model: GCL-LR-Attention
    model_key: gcl-lr-attention
    model_plain: GCL-LR-Attention
    value: 0.931
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.931
    sort_std: 0.006
    is_best: false
  - model: LFP
    model_key: lfp
    model_plain: LFP
    value: 0.931
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.931
    sort_std: 0.006
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.735
    std: 0.012
    paper_value: 0.735
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 19
    true_value: 0.918
    true_std: 0.001
    value_gap_source_arxiv: '2402.09600'
    value_gap_source_title: Graph Contrastive Learning with Low-Rank Regularization
      and Low-Rank Attention for Noisy Node Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18300000000000005
    value_note: ''
    paper_rank: 117
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.918
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.745
    std: 0.016
    paper_value: 0.745
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 34
    true_value: 0.8303
    true_std: 0.0021
    value_gap_source_arxiv: '2405.18581'
    value_gap_source_title: 'Unleashing the Potential of Text-attributed Graphs: Automatic
      Relation Decomposition via Large Language Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08530000000000004
    value_note: ''
    paper_rank: 113
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.8303
    sort_std: 0.0021
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.741
    std: 0.015
    paper_value: 0.741
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 37
    true_value: 0.8279
    true_std: 0.0016
    value_gap_source_arxiv: '2405.18581'
    value_gap_source_title: 'Unleashing the Potential of Text-attributed Graphs: Automatic
      Relation Decomposition via Large Language Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08689999999999998
    value_note: ''
    paper_rank: 116
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.8279
    sort_std: 0.0016
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.728
    std: 0.011
    paper_value: 0.728
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 50
    true_value: 0.815
    true_std: 0.0027
    value_gap_source_arxiv: '2509.21489'
    value_gap_source_title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08699999999999997
    value_note: ''
    paper_rank: 118
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.815
    sort_std: 0.0027
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.752
    std: 0.014
    paper_value: 0.752
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 62
    true_value: 0.7984
    true_std: 0.001
    value_gap_source_arxiv: '2007.02901'
    value_gap_source_title: 'Wiki-CS: A Wikipedia-Based Benchmark for Graph Neural
      Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0464
    value_note: ''
    paper_rank: 110
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.7984
    sort_std: 0.001
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.789
    std: 0.01
    paper_value: 0.789
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 74
    true_value: 0.789
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.789
    sort_std: 0.01
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.763
    std: 0.013
    paper_value: 0.763
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 105
    true_value: 0.763
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.013
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ZINC
  rows:
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.004
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.004
    sort_std: null
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.278
    std: 0.006
    paper_value: 0.278
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.006
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.272
    value_note: ''
    paper_rank: 134
    rank_delta: 132
    rank_delta_abs: 132
    rank_delta_direction: worse
    sort_value: 0.006
    sort_std: null
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.014
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.014
    sort_std: null
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.02
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.296
    std: 0.005
    paper_value: 0.296
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 11
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27199999999999996
    value_note: ''
    paper_rank: 136
    rank_delta: 125
    rank_delta_abs: 125
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.245
    std: 0.003
    paper_value: 0.245
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 42
    true_value: 0.067
    true_std: 0.009
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.178
    value_note: ''
    paper_rank: 134
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.067
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.285
    std: 0.004
    paper_value: 0.285
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 80
    true_value: 0.111
    true_std: 0.002
    value_gap_source_arxiv: '2301.09505'
    value_gap_source_title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.174
    value_note: ''
    paper_rank: 135
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.111
    sort_std: 0.002
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.195
    std: 0.004
    paper_value: 0.195
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 94
    true_value: 0.132
    true_std: 0.003
    value_gap_source_arxiv: '1805.09076'
    value_gap_source_title: Constrained Graph Variational Autoencoders for Molecule
      Design
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.063
    value_note: ''
    paper_rank: 126
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.132
    sort_std: 0.003
    is_best: false
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.172
    std: 0.002
    paper_value: 0.172
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 98
    true_value: 0.135
    true_std: 0.004
    value_gap_source_arxiv: '1805.09076'
    value_gap_source_title: Constrained Graph Variational Autoencoders for Molecule
      Design
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03699999999999998
    value_note: ''
    paper_rank: 120
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.135
    sort_std: 0.004
    is_best: false
  - model: SphereNet
    model_key: spherenet
    model_plain: SphereNet
    value: 0.185
    std: 0.003
    paper_value: 0.185
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 99
    true_value: 0.138
    true_std: 0.003
    value_gap_source_arxiv: '1805.09076'
    value_gap_source_title: Constrained Graph Variational Autoencoders for Molecule
      Design
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046999999999999986
    value_note: ''
    paper_rank: 122
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.138
    sort_std: 0.003
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.142
    std: 0.001
    paper_value: 0.142
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 104
    true_value: 0.142
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.142
    sort_std: 0.001
    is_best: false
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.198
    std: 0.002
    paper_value: 0.198
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 107
    true_value: 0.145
    true_std: 0.004
    value_gap_source_arxiv: '1805.09076'
    value_gap_source_title: Constrained Graph Variational Autoencoders for Molecule
      Design
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05300000000000002
    value_note: ''
    paper_rank: 126
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.145
    sort_std: 0.004
    is_best: false
  - model: DimeNet++ (large)
    model_key: dimenet++ (large)
    model_plain: DimeNet++ (large)
    value: 0.158
    std: 0.002
    paper_value: 0.158
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 115
    true_value: 0.158
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.158
    sort_std: 0.002
    is_best: false
  - model: PaiNN (large)
    model_key: painn (large)
    model_plain: PaiNN (large)
    value: 0.165
    std: 0.002
    paper_value: 0.165
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 118
    true_value: 0.165
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.165
    sort_std: 0.002
    is_best: false
  - model: SE(3)-Transformer
    model_key: se(3)-transformer
    model_plain: SE(3)-Transformer
    value: 0.188
    std: 0.003
    paper_value: 0.188
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 123
    true_value: 0.188
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.188
    sort_std: 0.003
    is_best: false
  - model: EquiBind
    model_key: equibind
    model_plain: EquiBind
    value: 0.21
    std: 0.005
    paper_value: 0.21
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 129
    true_value: 0.21
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.21
    sort_std: 0.005
    is_best: false
  metric: MAE
  higher_is_better: false
- &id024
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
    paper_value: 0.862
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.862
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.002
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.858
    std: 0.002
    paper_value: 0.858
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.858
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.858
    sort_std: 0.002
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.855
    std: 0.002
    paper_value: 0.855
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.855
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.855
    sort_std: 0.002
    is_best: false
  - model: AI
    model_key: ai
    model_plain: AI
    value: 0.855
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_display: Sep 2022
    date_iso: 2022-09
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.855
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.853
    std: 0.003
    paper_value: 0.853
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.853
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.853
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.851
    std: 0.004
    paper_value: 0.851
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.851
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.851
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_display: Sep 2022
    date_iso: 2022-09
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.851
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.848
    std: 0.003
    paper_value: 0.848
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 9
    true_value: 0.848
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.848
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.845
    std: 0.004
    paper_value: 0.845
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 11
    true_value: 0.845
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.842
    std: 0.005
    paper_value: 0.842
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 12
    true_value: 0.842
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.005
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.839
    std: 0.006
    paper_value: 0.839
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 13
    true_value: 0.839
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.006
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id026
  dataset: ogbg-molpcba
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.339
    std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.339
    sort_std: 0.0073
    is_best: true
  - model: unified method + FLAG
    model_key: unified method + flag
    model_plain: unified method + FLAG
    value: 0.3174
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_display: Jul 2022
    date_iso: 2022-07
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3174
    sort_std: null
    is_best: false
  - model: TGT-Ag+TGT-At-DP
    model_key: tgt-ag+tgt-at-dp
    model_plain: TGT-Ag+TGT-At-DP
    value: 0.3167
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.3167
    sort_std: 0.0031
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.232
    std: 0.001
    paper_value: 0.232
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.314
    true_std: null
    value_gap_source_arxiv: '2207.08806'
    value_gap_source_title: Unified 2D and 3D Pre-Training of Molecular Representations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08199999999999999
    value_note: ''
    paper_rank: 53
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.314
    sort_std: null
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.225
    std: 0.002
    paper_value: 0.225
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 27
    true_value: 0.2838
    true_std: 0.0035
    value_gap_source_arxiv: '2110.07875'
    value_gap_source_title: Graph Neural Networks with Learnable Structural and Positional
      Representations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05879999999999999
    value_note: ''
    paper_rank: 58
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.2838
    sort_std: 0.0035
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.221
    std: 0.001
    paper_value: 0.221
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 35
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04929999999999998
    value_note: ''
    paper_rank: 59
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.213
    std: 0.002
    paper_value: 0.213
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 46
    true_value: 0.2424
    true_std: 0.0034
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02940000000000001
    value_note: ''
    paper_rank: 59
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.2424
    sort_std: 0.0034
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.241
    std: 0.001
    paper_value: 0.241
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 47
    true_value: 0.241
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.241
    sort_std: 0.001
    is_best: false
  - model: MolFormer
    model_key: molformer
    model_plain: MolFormer
    value: 0.235
    std: 0.002
    paper_value: 0.235
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 49
    true_value: 0.235
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.235
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.215
    std: 0.003
    paper_value: 0.215
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 56
    true_value: 0.228
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013000000000000012
    value_note: ''
    paper_rank: 59
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.228
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.218
    std: 0.002
    paper_value: 0.218
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 58
    true_value: 0.227
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009000000000000008
    value_note: ''
    paper_rank: 59
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.227
    sort_std: 0.001
    is_best: false
  metric: AP
  higher_is_better: true
- &id035
  dataset: ogbl-biokg
  rows:
  - model: ComplEx
    model_key: complex
    model_plain: ComplEx
    value: 0.418
    std: null
    paper_value: 0.418
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Trouillon et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.8095
    true_std: 0.0007
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3915
    value_note: ''
    paper_rank: 8
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8095
    sort_std: 0.0007
    is_best: true
  - model: DistMult
    model_key: distmult
    model_plain: DistMult
    value: 0.395
    std: null
    paper_value: 0.395
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2014
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.8043
    true_std: 0.0003
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4093
    value_note: ''
    paper_rank: 8
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8043
    sort_std: 0.0003
    is_best: false
  - model: RotatE
    model_key: rotate
    model_plain: RotatE
    value: 0.432
    std: null
    paper_value: 0.432
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.7989
    true_std: 0.0004
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.36690000000000006
    value_note: ''
    paper_rank: 8
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.7989
    sort_std: 0.0004
    is_best: false
  - model: TransE
    model_key: transe
    model_plain: TransE
    value: 0.365
    std: null
    paper_value: 0.365
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bordes et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.7452
    true_std: 0.0004
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3802
    value_note: ''
    paper_rank: 8
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7452
    sort_std: 0.0004
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.512
    std: 0.003
    paper_value: 0.512
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.512
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.512
    sort_std: 0.003
    is_best: false
  - model: GAIN
    model_key: gain
    model_plain: GAIN
    value: 0.485
    std: null
    paper_value: 0.485
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.485
    true_std: null
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.485
    sort_std: null
    is_best: false
  - model: CompGCN
    model_key: compgcn
    model_plain: CompGCN
    value: 0.468
    std: null
    paper_value: 0.468
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Vashishth et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.468
    true_std: null
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.468
    sort_std: null
    is_best: false
  - model: R-GCN
    model_key: r-gcn
    model_plain: R-GCN
    value: 0.451
    std: null
    paper_value: 0.451
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Schlichtkrull et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 8
    true_value: 0.451
    true_std: null
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.451
    sort_std: null
    is_best: false
  metric: MRR
  higher_is_better: true
- &id028
  dataset: ogbl-citation2
  rows:
  - model: MPLP
    model_key: mplp
    model_plain: MPLP
    value: 0.9072
    std: 0.0012
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9072
    sort_std: 0.0012
    is_best: true
  - model: NCNC
    model_key: ncnc
    model_plain: NCNC
    value: 0.8912
    std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8912
    sort_std: 0.004
    is_best: false
  - model: SEAL
    model_key: seal
    model_plain: SEAL
    value: 0.8767
    std: 0.0032
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.00170'
    title: Asymmetric Learning for Graph Neural Network based Link Prediction
    date: Mar 2023
    date_display: Mar 2023
    date_iso: 2023-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8767
    sort_std: 0.0032
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.765
    std: 0.003
    paper_value: 0.765
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 12
    true_value: 0.8479
    true_std: 0.0024
    value_gap_source_arxiv: '2206.04216'
    value_gap_source_title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks
      for Link Prediction'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08289999999999997
    value_note: ''
    paper_rank: 30
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.8479
    sort_std: 0.0024
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.768
    std: 0.002
    paper_value: 0.768
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 16
    true_value: 0.8264
    true_std: 0.0001
    value_gap_source_arxiv: '2206.04216'
    value_gap_source_title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks
      for Link Prediction'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05840000000000001
    value_note: ''
    paper_rank: 30
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.8264
    sort_std: 0.0001
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.812
    std: 0.001
    paper_value: 0.812
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 18
    true_value: 0.812
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.001
    is_best: false
  - model: OpenGNN
    model_key: opengnn
    model_plain: OpenGNN
    value: 0.805
    std: 0.001
    paper_value: 0.805
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 19
    true_value: 0.805
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.805
    sort_std: 0.001
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.801
    std: 0.002
    paper_value: 0.801
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 21
    true_value: 0.801
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.801
    sort_std: 0.002
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.795
    std: 0.002
    paper_value: 0.795
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 24
    true_value: 0.795
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.792
    std: 0.003
    paper_value: 0.792
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 25
    true_value: 0.792
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.003
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.788
    std: 0.002
    paper_value: 0.788
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 27
    true_value: 0.788
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.785
    std: 0.002
    paper_value: 0.785
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 28
    true_value: 0.785
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.772
    std: 0.004
    paper_value: 0.772
    paper_std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 29
    true_value: 0.772
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.77
    std: 0.003
    paper_value: 0.77
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 30
    true_value: 0.77
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.003
    is_best: false
  metric: MRR
  higher_is_better: true
- &id033
  dataset: ogbl-collab
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.785
    std: 0.002
    paper_value: 0.785
    paper_std: 0.002
    metric: Hits@50
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.785
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.768
    std: 0.003
    paper_value: 0.768
    paper_std: 0.003
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.768
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.762
    std: 0.002
    paper_value: 0.762
    paper_std: 0.002
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.762
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.758
    std: 0.003
    paper_value: 0.758
    paper_std: 0.003
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.758
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.751
    std: 0.004
    paper_value: 0.751
    paper_std: 0.004
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.751
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.745
    std: 0.003
    paper_value: 0.745
    paper_std: 0.003
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.745
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.736
    std: 0.002
    paper_value: 0.736
    paper_std: 0.002
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.736
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.736
    sort_std: 0.002
    is_best: false
  - model: MPLP
    model_key: mplp
    model_plain: MPLP
    value: 0.6699
    std: 0.004
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.6699
    sort_std: 0.004
    is_best: false
  - model: BUDDY-SIGN (MLP Decoder)
    model_key: buddy-sign (mlp decoder)
    model_plain: BUDDY-SIGN (MLP Decoder)
    value: 0.6664
    std: 0.0064
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.17475'
    title: On the Impact of Feature Heterophily on Link Prediction with Graph Neural
      Networks
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: https://github.com/tensor-gales/HeteLinkPred
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.6664
    sort_std: 0.0064
    is_best: false
  - model: NCNC
    model_key: ncnc
    model_plain: NCNC
    value: 0.6661
    std: 0.0071
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00976'
    title: Pure Message Passing Can Estimate Common Neighbor for Link Prediction
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/Barcavin/efficient-node-labelling
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.6661
    sort_std: 0.0071
    is_best: false
  metric: Hits@50
  higher_is_better: true
- &id034
  dataset: ogbl-ddi
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.784
    std: 0.002
    paper_value: 0.784
    paper_std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.784
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.771
    std: 0.003
    paper_value: 0.771
    paper_std: 0.003
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.771
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.765
    std: 0.002
    paper_value: 0.765
    paper_std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.765
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.765
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.752
    std: 0.003
    paper_value: 0.752
    paper_std: 0.003
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.752
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.748
    std: 0.004
    paper_value: 0.748
    paper_std: 0.004
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.748
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.748
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.741
    std: 0.002
    paper_value: 0.741
    paper_std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.741
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.735
    std: 0.003
    paper_value: 0.735
    paper_std: 0.003
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.735
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.003
    is_best: false
  - model: MGAE-SAGE
    model_key: mgae-sage
    model_plain: MGAE-SAGE
    value: 0.66
    std: 0.0949
    metric: Hits@20
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_display: Jan 2022
    date_iso: 2022-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.66
    sort_std: 0.0949
    is_best: false
  - model: MGAE-GCN
    model_key: mgae-gcn
    model_plain: MGAE-GCN
    value: 0.6591
    std: 0.035
    metric: Hits@20
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_display: Jan 2022
    date_iso: 2022-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.6591
    sort_std: 0.035
    is_best: false
  - model: Neo-GNN
    model_key: neo-gnn
    model_plain: Neo-GNN
    value: 0.6357
    std: 0.0352
    metric: Hits@20
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04216'
    title: 'Neo-GNNs: Neighborhood Overlap-aware Graph Neural Networks for Link Prediction'
    date: Jun 9, 2022
    date_display: Jun 2022
    date_iso: '2022-06-09'
    codebase_url: https://github.com/seongjunyun/Neo_GNNs
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.6357
    sort_std: 0.0352
    is_best: false
  metric: Hits@20
  higher_is_better: true
- &id029
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
    value: 0.482
    std: 0.0
    paper_value: 0.482
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
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
    value_gap: 0.246
    value_note: ''
    paper_rank: 31
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.728
    sort_std: 0.003
    is_best: false
  - model: ComplEx
    model_key: complex
    model_plain: ComplEx
    value: 0.451
    std: 0.0
    paper_value: 0.451
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Trouillon et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
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
    value_gap: 0.27399999999999997
    value_note: ''
    paper_rank: 31
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.725
    sort_std: 0.003
    is_best: false
  - model: DistMult
    model_key: distmult
    model_plain: DistMult
    value: 0.438
    std: 0.0
    paper_value: 0.438
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2014
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
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
    value_gap: 0.283
    value_note: ''
    paper_rank: 31
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.721
    sort_std: 0.003
    is_best: false
  - model: TransE
    model_key: transe
    model_plain: TransE
    value: 0.365
    std: 0.0
    paper_value: 0.365
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bordes et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
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
    value_gap: 0.32000000000000006
    value_note: ''
    paper_rank: 35
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.685
    sort_std: 0.004
    is_best: false
  - model: R-GCN
    model_key: r-gcn
    model_plain: R-GCN
    value: 0.495
    std: 0.0
    paper_value: 0.495
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Schlichtkrull et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 13
    true_value: 0.678
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18300000000000005
    value_note: ''
    paper_rank: 31
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.678
    sort_std: 0.004
    is_best: false
  - model: CompGCN
    model_key: compgcn
    model_plain: CompGCN
    value: 0.501
    std: 0.0
    paper_value: 0.501
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Vashishth et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 14
    true_value: 0.675
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17400000000000004
    value_note: ''
    paper_rank: 31
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.675
    sort_std: 0.004
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.538
    std: 0.002
    paper_value: 0.538
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 26
    true_value: 0.538
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.538
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.524
    std: 0.0
    paper_value: 0.524
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 29
    true_value: 0.524
    true_std: 0.0
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.524
    sort_std: 0.0
    is_best: false
  - model: HGT
    model_key: hgt
    model_plain: HGT
    value: 0.512
    std: 0.0
    paper_value: 0.512
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 31
    true_value: 0.512
    true_std: 0.0
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.512
    sort_std: 0.0
    is_best: false
  metric: MRR
  higher_is_better: true
- &id023
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
    value: 0.728
    std: 0.005
    paper_value: 0.728
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 26
    true_value: 0.7629
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03490000000000004
    value_note: ''
    paper_rank: 164
    rank_delta: 138
    rank_delta_abs: 138
    rank_delta_direction: worse
    sort_value: 0.7629
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.731
    std: 0.003
    paper_value: 0.731
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
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
    value_gap: 0.02100000000000002
    value_note: ''
    paper_rank: 142
    rank_delta: 85
    rank_delta_abs: 85
    rank_delta_direction: worse
    sort_value: 0.752
    sort_std: 0.0003
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.752
    std: 0.002
    paper_value: 0.752
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 58
    true_value: 0.752
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.745
    std: 0.003
    paper_value: 0.745
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 75
    true_value: 0.745
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.735
    std: 0.004
    paper_value: 0.735
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 77
    true_value: 0.7439
    true_std: null
    value_gap_source_arxiv: '2603.01385'
    value_gap_source_title: Toward Graph-Tokenizing Large Language Models with Reconstructive
      Graph Instruction Tuning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008900000000000019
    value_note: ''
    paper_rank: 126
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.7439
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.742
    std: 0.002
    paper_value: 0.742
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 86
    true_value: 0.742
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.002
    is_best: false
  - model: JK-Net
    model_key: jk-net
    model_plain: JK-Net
    value: 0.74
    std: 0.003
    paper_value: 0.74
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 100
    true_value: 0.74
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.738
    std: 0.004
    paper_value: 0.738
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 112
    true_value: 0.738
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.004
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.725
    std: 0.006
    paper_value: 0.725
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 136
    true_value: 0.733
    true_std: 0.0
    value_gap_source_arxiv: '2511.06443'
    value_gap_source_title: How Wide and How Deep? Mitigating Over-Squashing of GNNs
      via Channel Capacity Constrained Estimation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008000000000000007
    value_note: ''
    paper_rank: 185
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id032
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
    paper_value: 0.781
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 2
    true_value: 0.781
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.781
    sort_std: 0.003
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.775
    std: 0.002
    paper_value: 0.775
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.775
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: Mowst
    model_key: mowst
    model_plain: Mowst
    value: 0.774
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 4
    sort_value: 0.774
    sort_std: 0.0011
    is_best: false
  - model: InfoMGF
    model_key: infomgf
    model_plain: InfoMGF
    value: 0.7732
    std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 5
    sort_value: 0.7732
    sort_std: 0.0009
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.772
    std: 0.003
    paper_value: 0.772
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.772
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.768
    std: 0.004
    paper_value: 0.768
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 9
    true_value: 0.768
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.761
    std: 0.003
    paper_value: 0.761
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 10
    true_value: 0.761
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.761
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.759
    std: 0.002
    paper_value: 0.759
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 11
    true_value: 0.759
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.753
    std: 0.002
    paper_value: 0.753
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 12
    true_value: 0.753
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.002
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id027
  dataset: ogbn-papers100M
  rows:
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.782
    std: 0.001
    paper_value: 0.782
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 1
    true_value: 0.782
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    paper_value: 0.775
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 3
    true_value: 0.775
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: Neighbor Sampling (NS)
    model_key: neighbor sampling (ns)
    model_plain: Neighbor Sampling (NS)
    value: 0.773
    std: 0.001
    paper_value: 0.773
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.773
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.001
    is_best: false
  - model: LADIES
    model_key: ladies
    model_plain: LADIES
    value: 0.771
    std: 0.002
    paper_value: 0.771
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zeng et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 5
    true_value: 0.771
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.002
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.768
    std: 0.003
    paper_value: 0.768
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 6
    true_value: 0.768
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.765
    std: 0.002
    paper_value: 0.765
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 7
    true_value: 0.765
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.765
    sort_std: 0.002
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.762
    std: 0.004
    paper_value: 0.762
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 8
    true_value: 0.762
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.76
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 9, 2025
    date_display: Nov 2025
    date_iso: '2025-11-09'
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.76
    sort_std: 0.0
    is_best: false
  - model: FastGCN
    model_key: fastgcn
    model_plain: FastGCN
    value: 0.759
    std: 0.005
    paper_value: 0.759
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 10
    true_value: 0.759
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.005
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.759
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 9, 2025
    date_display: Nov 2025
    date_iso: '2025-11-09'
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.759
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id025
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
    value: 0.823
    std: 0.001
    paper_value: 0.823
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
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
    value_gap: 0.020500000000000074
    value_note: ''
    paper_rank: 35
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.8435
    sort_std: 0.0009
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.835
    std: 0.001
    paper_value: 0.835
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 25
    true_value: 0.835
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.001
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.825
    std: 0.001
    paper_value: 0.825
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
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
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 33
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8316
    sort_std: 0.0019
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.83
    std: 0.001
    paper_value: 0.83
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 28
    true_value: 0.83
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.001
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.827
    std: 0.001
    paper_value: 0.827
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 30
    true_value: 0.827
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.826
    std: 0.001
    paper_value: 0.826
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 31
    true_value: 0.8263
    true_std: 0.0007
    value_gap_source_arxiv: '2509.14863'
    value_gap_source_title: 'Exploring the Global-to-Local Attention Scheme in Graph
      Transformers: An Empirical Study'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.000300000000000078
    value_note: global 0.8263 within std
    paper_rank: 32
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.8263
    sort_std: 0.0007
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.824
    std: 0.001
    paper_value: 0.824
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 34
    true_value: 0.824
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.824
    sort_std: 0.001
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.822
    std: 0.001
    paper_value: 0.822
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 36
    true_value: 0.822
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.822
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id031
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.821
    std: 0.002
    paper_value: 0.821
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 4
    true_value: 0.8682
    true_std: 0.0021
    value_gap_source_arxiv: '2106.07476'
    value_gap_source_title: Training Graph Neural Networks with 1000 Layers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04720000000000002
    value_note: ''
    paper_rank: 11
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8682
    sort_std: 0.0021
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.841
    std: 0.002
    paper_value: 0.841
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 8
    true_value: 0.841
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.841
    sort_std: 0.002
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.835
    std: 0.001
    paper_value: 0.835
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 9
    true_value: 0.835
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.832
    std: 0.002
    paper_value: 0.832
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 10
    true_value: 0.832
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.832
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.824
    std: 0.003
    paper_value: 0.824
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 11
    true_value: 0.824
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.824
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.818
    std: 0.004
    paper_value: 0.818
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 12
    true_value: 0.818
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.818
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.003
    paper_value: 0.815
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    published_venue: null
    global_rank: 13
    true_value: 0.815
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.815
    sort_std: 0.003
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
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
- benchmark: TU Dortmund
  datasets:
  - *id013
  - *id014
  - *id015
  - *id016
  - *id017
  - *id018
  - *id019
  - *id020
  - *id021
  - *id022
- benchmark: OGB
  datasets:
  - *id023
  - *id024
  - *id025
  - *id026
  - *id027
  - *id028
  - *id029
  - *id030
  - *id031
  - *id032
  - *id033
  - *id034
  - *id035
- benchmark: Quantum Chemistry
  datasets:
  - *id036
single_proposed_model: ILLS
---

