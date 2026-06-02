---
title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for Graph
  Neural Networks'
arxiv_id: '2306.08385'
source_url: ''
authors: []
published_date: Jun 14, 2023
published_date_iso: '2023-06-14'
published_venue: ''
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
mrr: 0.0115
adjusted_mrr: 0.0115
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 1
    true_value: 0.836
    true_std: 0.004
    value_gap_source_arxiv: '2006.13009'
    value_gap_source_title: 'Iterative Deep Graph Learning for Graph Neural Networks:
      Better and Robust Node Embeddings'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18509999999999993
    value_note: ''
    paper_rank: 22
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.836
    sort_std: 0.004
    is_best: true
  - model: IDGL-Anch
    model_key: idgl-anch
    model_plain: IDGL-Anch
    value: 0.829
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 1, 2020
    date_display: Jun 2020
    date_iso: '2020-06-01'
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.829
    sort_std: 0.003
    is_best: true
  - model: GCN_kNN
    model_key: gcn_knn
    model_plain: GCN_kNN
    value: 0.813
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 1, 2020
    date_display: Jun 2020
    date_iso: '2020-06-01'
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.813
    sort_std: 0.006
    is_best: false
  - model: UniGCN
    model_key: unigcn
    model_plain: UniGCN
    value: 0.8024
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_display: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8024
    sort_std: 0.004
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 18
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
    paper_rank: 18
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 19
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
    paper_rank: 19
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 20
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
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6598
    sort_std: 0.0068
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 24
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
    paper_rank: 24
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 25
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
    paper_rank: 25
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
  - model: Vicuna-7B
    model_key: vicuna-7b
    model_plain: Vicuna-7B
    value: 0.7682
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.7682
    sort_std: 0.005
    is_best: true
  - model: Bloom 560M
    model_key: bloom 560m
    model_plain: Bloom 560M
    value: 0.7616
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.7616
    sort_std: 0.006
    is_best: true
  - model: 7B-to-560M
    model_key: 7b-to-560m
    model_plain: 7B-to-560M
    value: 0.7578
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7578
    sort_std: 0.002
    is_best: false
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 106
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
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3531
    sort_std: 0.0129
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
    value: 0.88
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.07984'
    title: Adversarial Attacks on Neural Networks for Graph Data
    date: May 21, 2018
    date_display: May 2018
    date_iso: '2018-05-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.88
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 102
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
    paper_rank: 102
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
    global_rank: 65
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
    paper_rank: 65
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
    date: Jun 14, 2023
    date_display: Jun 2023
    date_iso: '2023-06-14'
    published_venue: null
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
---

