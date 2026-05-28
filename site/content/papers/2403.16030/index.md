---
title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual Connections'
arxiv_id: '2403.16030'
source_url: ''
authors: []
published_date: Mar 2024
published_date_iso: 2024-03
abstract: -2mm Graph transformer has been proven as an effective graph learning method
  for its adoption of attention mechanism that is capable of capturing expressive
  representations from complex topological and feature information of graphs. Graph
  transformer conventionally performs dense attention (or global attention) for every
  pair of nodes to learn node representation vectors, resulting in quadratic computational
  costs that are unaffordable for large-scale graph data. Therefore, mini-batch training
  for graph transformers is a promising direction, but limited samples in each mini-batch
  can not support effective dense attention to encode informative representations.
  Facing this bottleneck, (1) we start by assigning each node a token list that is
  sampled by personalized PageRank (PPR) and then apply standard multi-head self-attention
  only on this list to compute its node representations. This PPR tokenization method
  decouples model training from complex graph topological information and makes heavy
  feature engineering offline and independent, such that mini-batch training of graph
  transformers is possible by loading each node's token list in batches. We further
  prove this PPR tokenization is viable as a graph convolution network with a fixed
  polynomial filter and jumping knowledge. However, only using personalized PageRank
  may limit information carried by a token list, which could not support different
  graph inductive biases for model training. To this end, (2) we rewire graphs by
  introducing multiple types of virtual connections through structure- and content-based
  super nodes that enable PPR tokenization to encode local and global contexts, long-range
  interaction, and heterophilous information into each node's token list, and then
  formalize our Virtual Connection Ranking based Graph Trans former (VCR-Graphormer).
  Overall, VCR-Graphormer needs $O(m+klogk)$ complexity for graph tokenization as
  compared to $O(n^3)$ of previous works. The code is provided https://github.com/DongqiFu/VCR-Graphormer.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- VCR-Graphormer
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- Classic
- Other Graph Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
  dataset: Amazon2M
  rows:
  - model: ParaFormer (a)
    model_key: paraformer (a)
    model_plain: ParaFormer (a)
    value: 0.8936
    std: 0.0014000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8936
    sort_std: 0.0014000000000000002
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
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8909
    sort_std: 0.001
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8785
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8785
    sort_std: 0.0024
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7743
    std: 0.0011
    paper_value: 0.7743
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 9
    true_value: 0.7743
    true_std: 0.0011
    value_gap_source_arxiv: '2403.16030'
    value_gap_source_title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual
      Connections'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7743
    sort_std: 0.0011
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.7609
    std: 0.0016
    paper_value: 0.7609
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 10
    true_value: 0.7609
    true_std: 0.0016
    value_gap_source_arxiv: '2403.16030'
    value_gap_source_title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual
      Connections'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7609
    sort_std: 0.0016
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.7549
    std: 0.0011
    paper_value: 0.7549
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 11
    true_value: 0.7549
    true_std: 0.0011
    value_gap_source_arxiv: '2403.16030'
    value_gap_source_title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual
      Connections'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7549
    sort_std: 0.0011
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.7521
    std: 0.0015
    paper_value: 0.7521
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 12
    true_value: 0.7521
    true_std: 0.0015
    value_gap_source_arxiv: '2403.16030'
    value_gap_source_title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual
      Connections'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7521
    sort_std: 0.0015
    is_best: false
  - model: PPRGo
    model_key: pprgo
    model_plain: PPRGo
    value: 0.6612
    std: 0.0059
    paper_value: 0.6612
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 13
    true_value: 0.6612
    true_std: 0.0059
    value_gap_source_arxiv: '2403.16030'
    value_gap_source_title: 'VCR-Graphormer: A Mini-batch Graph Transformer via Virtual
      Connections'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6612
    sort_std: 0.0059
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Reddit
  rows:
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.9369
    std: 0.0008
    paper_value: 0.9369
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: null
    sort_value: 0.9369
    sort_std: 0.0008
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9358
    std: 0.0005
    paper_value: 0.9358
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: null
    sort_value: 0.9358
    sort_std: 0.0005
    is_best: true
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.9281
    std: 0.0003
    paper_value: 0.9281
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: null
    sort_value: 0.9281
    sort_std: 0.0003
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.9235
    std: 0.0008
    paper_value: 0.9235
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: null
    sort_value: 0.9235
    sort_std: 0.0008
    is_best: false
  - model: PPRGo
    model_key: pprgo
    model_plain: PPRGo
    value: 0.9038
    std: 0.0011
    paper_value: 0.9038
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: null
    sort_value: 0.9038
    sort_std: 0.0011
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8719
    sort_std: 0.0156
    is_best: false
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8482
    sort_std: 0.0162
    is_best: false
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8425
    sort_std: 0.0113
    is_best: false
  metric: F1
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: Other Graph Benchmarks
  datasets:
  - *id002
single_proposed_model: VCR-Graphormer
main_figure: /figures/2403.16030/main_figure.png
---

