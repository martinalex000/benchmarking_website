---
title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for Graph
  Neural Networks'
arxiv_id: '2306.08385'
source_url: ''
authors: []
published_date: Jun 2023
published_date_iso: 2023-06
abstract: Graph neural networks have been extensively studied for learning with inter-connected
  data. Despite this, recent evidence has revealed GNNs' deficiencies related to over-squashing,
  heterophily, handling long-range dependencies, edge incompleteness and particularly,
  the absence of graphs altogether. While a plausible solution is to learn new adaptive
  topology for message passing, issues concerning quadratic complexity hinder simultaneous
  guarantees for scalability and precision in large networks. In this paper, we introduce
  a novel all-pair message passing scheme for efficiently propagating node signals
  between arbitrary nodes, as an important building block for a pioneering Transformer-style
  network for node classification on large graphs, dubbed as NodeFormer. Specifically,
  the efficient computation is enabled by a kernerlized Gumbel-Softmax operator that
  reduces the algorithmic complexity to linearity w.r.t. node numbers for learning
  latent graph structures from large, potentially fully-connected graphs in a differentiable
  manner. We also provide accompanying theory as justification for our design. Extensive
  experiments demonstrate the promising efficacy of the method in various tasks including
  node classification on graphs (with up to 2M nodes) and graph-enhanced applications
  (e.g., image classification) where input graphs are missing. The codes are available
  at.
codebase_url: https://github.com/qitianwu/NodeFormer
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- novel all-pair message passing scheme
mrr: 0.0778
adjusted_mrr: 0.0778
mrr_dataset_count: 3
benchmark_categories:
- Classic
- Heterophilic Graphs
- Other Graph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id005
  dataset: 20News
  rows:
  - model: Multinomial Naive Bayes
    model_key: multinomial naive bayes
    model_plain: Multinomial Naive Bayes
    value: 0.6851
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_display: Jun 2016
    date_iso: 2016-06
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.6851
    sort_std: null
    is_best: true
  - model: GC32
    model_key: gc32
    model_plain: GC32
    value: 0.6826
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_display: Jun 2016
    date_iso: 2016-06
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.6826
    sort_std: null
    is_best: false
  - model: Softmax
    model_key: softmax
    model_plain: Softmax
    value: 0.6628
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_display: Jun 2016
    date_iso: 2016-06
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.6628
    sort_std: null
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.6615
    std: 0.0036
    paper_value: 0.6615
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to 20news (score=90)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 4
    true_value: 0.6615
    true_std: 0.0036
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6615
    sort_std: 0.0036
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6601
    std: 0.0118
    paper_value: 0.6601
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to 20news (score=90)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 5
    true_value: 0.6601
    true_std: 0.0118
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6601
    sort_std: 0.0118
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6598
    std: 0.0068
    paper_value: 0.6598
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to 20news (score=90)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 6
    true_value: 0.6598
    true_std: 0.0068
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6598
    sort_std: 0.0068
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.6509
    std: 0.0123
    paper_value: 0.6509
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to 20news (score=90)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 9
    true_value: 0.6509
    true_std: 0.0123
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6509
    sort_std: 0.0123
    is_best: false
  - model: DropEdge
    model_key: dropedge
    model_plain: DropEdge
    value: 0.6446
    std: 0.0043
    paper_value: 0.6446
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to 20news (score=90)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 11
    true_value: 0.6446
    true_std: 0.0043
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6446
    sort_std: 0.0043
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6406
    std: 0.0044
    paper_value: 0.6406
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to 20news (score=90)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 12
    true_value: 0.6406
    true_std: 0.0044
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6406
    sort_std: 0.0044
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Actor
  rows:
  - model: GRAPHITE
    model_key: graphite
    model_plain: GRAPHITE
    value: 0.3769
    std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3769
    sort_std: 0.0157
    is_best: true
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.3736
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3736
    sort_std: 0.0016
    is_best: true
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.3735
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_display: May 2022
    date_iso: '2022-05-15'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.3735
    sort_std: null
    is_best: true
  - model: novel all-pair message passing scheme
    model_key: novel all-pair message passing scheme
    model_plain: novel all-pair message passing scheme
    value: 0.3531
    std: 0.0129
    paper_value: 0.3531
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4 (Ablation study results on transductive datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 9
    true_value: 0.3531
    true_std: 0.0129
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3531
    sort_std: 0.0129
    is_best: true
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.8285
    std: 0.0038
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8285
    sort_std: 0.0038
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.8114
    std: 0.0034
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8114
    sort_std: 0.0034
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.7741
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_display: May 2022
    date_iso: '2022-05-15'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7741
    sort_std: null
    is_best: false
  - model: novel all-pair message passing scheme
    model_key: novel all-pair message passing scheme
    model_plain: novel all-pair message passing scheme
    value: 0.7633
    std: 0.0059
    paper_value: 0.7633
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 18
    true_value: 0.7633
    true_std: 0.0059
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7633
    sort_std: 0.0059
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9285
    std: 0.0054
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
    global_rank: 1
    sort_value: 0.9285
    sort_std: 0.0054
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9171
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9171
    sort_std: 0.0029
    is_best: false
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: false
  - model: novel all-pair message passing scheme
    model_key: novel all-pair message passing scheme
    model_plain: novel all-pair message passing scheme
    value: 0.8869
    std: 0.0046
    paper_value: 0.8869
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 15
    true_value: 0.8869
    true_std: 0.0046
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8869
    sort_std: 0.0046
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Deezer
  rows:
  - model: novel all-pair message passing scheme
    model_key: novel all-pair message passing scheme
    model_plain: novel all-pair message passing scheme
    value: 0.7124
    std: 0.0032
    paper_value: 0.7124
    paper_std: 0.0032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3 (Ablation study)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 1
    true_value: 0.7124
    true_std: 0.0032
    value_gap_source_arxiv: '2306.08385'
    value_gap_source_title: 'Align All the Nodes: Scalable Learning of Flexible Latent
      Structure for Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7124
    sort_std: 0.0032
    is_best: true
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: Heterophilic Graphs
  datasets:
  - *id003
  - *id004
- benchmark: Other Graph Benchmarks
  datasets:
  - *id005
single_proposed_model: novel all-pair message passing scheme
main_figure: /figures/2306.08385/main_figure.png
---

