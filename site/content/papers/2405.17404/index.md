---
title: Spectral Greedy Coresets for Graph Neural Networks
arxiv_id: '2405.17404'
source_url: ''
authors: []
published_date: May 2024
published_date_iso: 2024-05
abstract: The ubiquity of large-scale graphs in node-classification tasks significantly
  hinders the real-world applications of Graph Neural Networks (GNNs). Node sampling,
  graph coarsening, and dataset condensation are effective strategies for enhancing
  data efficiency. However, owing to the interdependence of graph nodes, coreset selection,
  which selects subsets of the data examples, has not been successfully applied to
  speed up GNN training on large graphs, warranting special treatment. This paper
  studies graph coresets for GNNs and avoids the interdependence issue by selecting
  ego-graphs (i.e., neighborhood subgraphs around a node) based on their spectral
  embeddings. We decompose the coreset selection problem for GNNs into two phases,
  a coarse selection of widely spread ego graphs and a refined selection to diversify
  their topologies. We design a greedy algorithm that approximately optimizes both
  objectives. Our spectral greedy graph coreset (SGGC) scales to graphs with millions
  of nodes, obviates the need for model pre-training, and is applicable to low-homophily
  graphs. Extensive experiments on ten datasets demonstrate that SGGC outperforms
  other coreset methods by a wide margin, generalizes well across GNN architectures,
  and is much faster than graph condensation.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- SGGC
mrr: 0.0072
adjusted_mrr: 0.0072
mrr_dataset_count: 4
benchmark_categories:
- Classic
- LRGB
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: Full Graph
    model_key: full graph
    model_plain: Full Graph
    value: 0.706
    std: 0.009
    paper_value: 0.706
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 133
    true_value: 0.706
    true_std: 0.009
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.706
    sort_std: 0.009
    is_best: false
  - model: SGGC
    model_key: sggc
    model_plain: SGGC
    value: 0.672
    std: 0.024
    paper_value: 0.672
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 152
    true_value: 0.672
    true_std: 0.024
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.672
    sort_std: 0.024
    is_best: false
  - model: CRAIG-Linear
    model_key: craig-linear
    model_plain: CRAIG-Linear
    value: 0.666
    std: 0.019
    paper_value: 0.666
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 156
    true_value: 0.666
    true_std: 0.019
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.666
    sort_std: 0.019
    is_best: false
  - model: SCGIGA
    model_key: scgiga
    model_plain: SCGIGA
    value: 0.546
    std: 0.028
    paper_value: 0.546
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 210
    true_value: 0.546
    true_std: 0.028
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 210
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.546
    sort_std: 0.028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: Full Graph
    model_key: full graph
    model_plain: Full Graph
    value: 0.812
    std: 0.004
    paper_value: 0.812
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 150
    true_value: 0.812
    true_std: 0.004
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.004
    is_best: false
  - model: SGGC
    model_key: sggc
    model_plain: SGGC
    value: 0.786
    std: 0.01
    paper_value: 0.786
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 169
    true_value: 0.786
    true_std: 0.01
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.786
    sort_std: 0.01
    is_best: false
  - model: SCGIGA
    model_key: scgiga
    model_plain: SCGIGA
    value: 0.767
    std: 0.014
    paper_value: 0.767
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: vahidian2020coresets
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 184
    true_value: 0.767
    true_std: 0.014
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.014
    is_best: false
  - model: CRAIG-Linear
    model_key: craig-linear
    model_plain: CRAIG-Linear
    value: 0.727
    std: 0.029
    paper_value: 0.727
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: mirzasoleiman2020coresets
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 217
    true_value: 0.727
    true_std: 0.029
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.029
    is_best: false
  - model: GCond
    model_key: gcond
    model_plain: GCond
    value: 0.706
    std: 0.037
    paper_value: 0.706
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 240
    true_value: 0.706
    true_std: 0.037
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 240
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.706
    sort_std: 0.037
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: PascalVOC-SP
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.567
    std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.567
    sort_std: 0.0049
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4912
    std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4912
    sort_std: 0.0042
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.4653
    std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
  - model: Full Graph (Oracle)
    model_key: full graph (oracle)
    model_plain: Full Graph (Oracle)
    value: 0.263
    std: 0.006
    paper_value: 0.263
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 86
    true_value: 0.263
    true_std: 0.006
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.263
    sort_std: 0.006
    is_best: false
  - model: SGGC
    model_key: sggc
    model_plain: SGGC
    value: 0.069
    std: 0.011
    paper_value: 0.069
    paper_std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 117
    true_value: 0.069
    true_std: 0.011
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.011
    is_best: false
  - model: Uniform
    model_key: uniform
    model_plain: Uniform
    value: 0.06
    std: 0.015
    paper_value: 0.06
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 119
    true_value: 0.06
    true_std: 0.015
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.06
    sort_std: 0.015
    is_best: false
  - model: k-Center
    model_key: k-center
    model_plain: k-Center
    value: 0.05
    std: 0.013
    paper_value: 0.05
    paper_std: 0.013
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 124
    true_value: 0.05
    true_std: 0.013
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.05
    sort_std: 0.013
    is_best: false
  - model: Forgetting
    model_key: forgetting
    model_plain: Forgetting
    value: 0.044
    std: 0.009
    paper_value: 0.044
    paper_std: 0.009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 125
    true_value: 0.044
    true_std: 0.009
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.044
    sort_std: 0.009
    is_best: false
  - model: Herding
    model_key: herding
    model_plain: Herding
    value: 0.04
    std: 0.006
    paper_value: 0.04
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 126
    true_value: 0.04
    true_std: 0.006
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.04
    sort_std: 0.006
    is_best: false
  metric: F1
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9476
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: Full Graph
    model_key: full graph
    model_plain: Full Graph
    value: 0.793
    std: 0.006
    paper_value: 0.793
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 121
    true_value: 0.793
    true_std: 0.006
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.006
    is_best: false
  - model: SGGC
    model_key: sggc
    model_plain: SGGC
    value: 0.758
    std: 0.016
    paper_value: 0.758
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 130
    true_value: 0.758
    true_std: 0.016
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.016
    is_best: false
  - model: CRAIG-Linear
    model_key: craig-linear
    model_plain: CRAIG-Linear
    value: 0.716
    std: 0.038
    paper_value: 0.716
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 153
    true_value: 0.716
    true_std: 0.038
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.716
    sort_std: 0.038
    is_best: false
  - model: SCGIGA
    model_key: scgiga
    model_plain: SCGIGA
    value: 0.698
    std: 0.007
    paper_value: 0.698
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 155
    true_value: 0.698
    true_std: 0.007
    value_gap_source_arxiv: '2405.17404'
    value_gap_source_title: Spectral Greedy Coresets for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.698
    sort_std: 0.007
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: LRGB
  datasets:
  - *id004
single_proposed_model: SGGC
main_figure: /figures/2405.17404/main_figure.png
---

