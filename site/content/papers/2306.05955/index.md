---
title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
arxiv_id: '2306.05955'
source_url: ''
authors: []
published_date: '2023-06-09'
published_date_iso: '2023-06-09'
abstract: Graph neural networks (GNNs) have recently become the standard approach
  for learning with graph-structured data. Prior work has shed light into their potential,
  but also their limitations. Unfortunately, it was shown that standard GNNs are limited
  in their expressive power. These models are no more powerful than the 1-dimensional
  Weisfeiler-Leman (1-WL) algorithm in terms of distinguishing non-isomorphic graphs.
  In this paper, we propose Path Neural Networks (PathNNs), a model that updates node
  representations by aggregating paths emanating from nodes. We derive three different
  variants of the PathNN model that aggregate single shortest paths, all shortest
  paths and all simple paths of length up to K. We prove that two of these variants
  are strictly more powerful than the 1-WL algorithm, and we experimentally validate
  our theoretical results. We find that PathNNs can distinguish pairs of non-isomorphic
  graphs that are indistinguishable by 1-WL, while our most expressive PathNN variant
  can even distinguish between 3-WL indistinguishable graphs. The different PathNN
  variants are also evaluated on graph classification and graph regression datasets,
  where in most cases, they outperform the baseline methods.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- PathNN-SP
- PathNN-AP
- PathNN-P (K=1)
- PathNN-SP (K=2)
- PathNN-AP (K=2)
- PathNN-\mathcal{SP}
mrr: 0.0704
adjusted_mrr: 0.0704
mrr_dataset_count: 4
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- GNNBenchmark
- OGB
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id010
  dataset: CSL
  rows:
  - model: PathNN-SP
    model_key: pathnn-sp
    model_plain: PathNN-SP
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 15
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: PathNN-AP
    model_key: pathnn-ap
    model_plain: PathNN-AP
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 16
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: PathNN-\mathcal{SP}
    model_key: pathnn-\mathcal{sp}
    model_plain: PathNN-\mathcal{SP}
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 17
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: PathNN-\mathcal{AP}
    model_key: pathnn-\mathcal{ap}
    model_plain: PathNN-\mathcal{AP}
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 18
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: B-method
    model_key: b-method
    model_plain: B-method
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: 3WLGNN
    model_key: 3wlgnn
    model_plain: 3WLGNN
    value: 0.978
    std: 0.109
    paper_value: 0.978
    paper_std: 0.109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Maron et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 22
    true_value: 0.978
    true_std: 0.109
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.978
    sort_std: 0.109
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1
    std: 0.0
    paper_value: 0.1
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 31
    true_value: 0.1
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: D&D
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.989
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.989
    sort_std: null
    is_best: true
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    value: 0.981
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.981
    sort_std: null
    is_best: false
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    value: 0.976
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: PathNN-AP
    model_key: pathnn-ap
    model_plain: PathNN-AP
    value: 0.6807
    std: 0.0072
    paper_value: 0.6807
    paper_std: 0.0072
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.6807
    sort_std: 0.0072
    is_best: false
  - model: PathNN-\mathcal{AP}
    model_key: pathnn-\mathcal{ap}
    model_plain: PathNN-\mathcal{AP}
    value: 0.6807
    std: 0.0072
    paper_value: 0.6807
    paper_std: 0.0072
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.6807
    sort_std: 0.0072
    is_best: false
  - model: PathNN-SP
    model_key: pathnn-sp
    model_plain: PathNN-SP
    value: 0.6784
    std: 0.0052
    paper_value: 0.6784
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.6784
    sort_std: 0.0052
    is_best: false
  - model: PathNN-\mathcal{SP}
    model_key: pathnn-\mathcal{sp}
    model_plain: PathNN-\mathcal{SP}
    value: 0.6784
    std: 0.0052
    paper_value: 0.6784
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.6784
    sort_std: 0.0052
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 39
    sort_value: 0.593
    sort_std: 0.0023
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 75
    sort_value: 0.5864
    sort_std: 0.0077
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5498
    std: 0.0079
    paper_value: 0.5498
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 38
    sort_value: 0.5498
    sort_std: 0.0079
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.73
    std: 0.052
    paper_value: 0.73
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 1
    true_value: 0.73
    true_std: 0.052
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    model_key: pathnn-\mathcal{p\phantom{s}}\phantom{^+} \, (k=1)
    model_plain: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    value: 0.73
    std: 0.052
    paper_value: 0.73
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 2
    true_value: 0.73
    true_std: 0.052
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.718
    std: 0.048
    paper_value: 0.718
    paper_std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 3
    true_value: 0.718
    true_std: 0.048
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: PathNN-SP (K=2)
    model_key: pathnn-sp (k=2)
    model_plain: PathNN-SP (K=2)
    value: 0.704
    std: 0.031
    paper_value: 0.704
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 4
    true_value: 0.704
    true_std: 0.031
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.704
    sort_std: 0.031
    is_best: true
  - model: PathNN-\mathcal{SP}
    model_key: pathnn-\mathcal{sp}
    model_plain: PathNN-\mathcal{SP}
    value: 0.704
    std: 0.031
    paper_value: 0.704
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 5
    true_value: 0.704
    true_std: 0.031
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.704
    sort_std: 0.031
    is_best: true
  - model: SPN(k=5)
    model_key: spn(k=5)
    model_plain: SPN(k=5)
    value: 0.694
    std: 0.062
    paper_value: 0.694
    paper_std: 0.062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 6
    true_value: 0.694
    true_std: 0.062
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.694
    sort_std: 0.062
    is_best: true
  - model: PathNet (N=10, K=2)
    model_key: pathnet (n=10, k=2)
    model_plain: PathNet (N=10, K=2)
    value: 0.693
    std: 0.054
    paper_value: 0.693
    paper_std: 0.054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 7
    true_value: 0.693
    true_std: 0.054
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.693
    sort_std: 0.054
    is_best: true
  - model: PathNN-AP (K=2)
    model_key: pathnn-ap (k=2)
    model_plain: PathNN-AP (K=2)
    value: 0.69
    std: 0.053
    paper_value: 0.69
    paper_std: 0.053
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 8
    true_value: 0.69
    true_std: 0.053
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.053
    is_best: true
  - model: PathNN-\mathcal{AP}\phantom{*} \, (K=3)
    model_key: pathnn-\mathcal{ap}\phantom{*} \, (k=3)
    model_plain: PathNN-\mathcal{AP}\phantom{*} \, (K=3)
    value: 0.69
    std: 0.053
    paper_value: 0.69
    paper_std: 0.053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 9
    true_value: 0.69
    true_std: 0.053
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.053
    is_best: true
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.683
    std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_display: Oct 2023
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.683
    sort_std: 0.057
    is_best: true
  - model: SPN (K=1)
    model_key: spn (k=1)
    model_plain: SPN (K=1)
    value: 0.675
    std: 0.055
    paper_value: 0.675
    paper_std: 0.055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 11
    true_value: 0.675
    true_std: 0.055
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.675
    sort_std: 0.055
    is_best: true
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.657
    std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_display: Oct 2023
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    sort_value: 0.657
    sort_std: 0.049
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.596
    std: 0.045
    paper_value: 0.596
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 13
    true_value: 0.606
    true_std: 0.034
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010000000000000009
    value_note: global 0.6060 within std
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.034
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.595
    std: 0.056
    paper_value: 0.595
    paper_std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 14
    true_value: 0.595
    true_std: 0.056
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.595
    sort_std: 0.056
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.584
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 15
    sort_value: 0.584
    sort_std: 0.021
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.582
    std: 0.06
    paper_value: 0.582
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 16
    true_value: 0.582
    true_std: 0.06
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.582
    sort_std: 0.06
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.495
    std: 0.089
    paper_value: 0.495
    paper_std: 0.089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Velickovic et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 26
    true_value: 0.495
    true_std: 0.089
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.495
    sort_std: 0.089
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.389
    std: 0.057
    paper_value: 0.389
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 49
    true_value: 0.389
    true_std: 0.057
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.389
    sort_std: 0.057
    is_best: false
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.312
    std: 0.067
    paper_value: 0.312
    paper_std: 0.067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 80
    true_value: 0.312
    true_std: 0.067
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.312
    sort_std: 0.067
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.295
    std: 0.082
    paper_value: 0.295
    paper_std: 0.082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Simonovsky et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 95
    true_value: 0.295
    true_std: 0.082
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.295
    sort_std: 0.082
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: IMDB-BINARY
  rows:
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
    date: '2025-01-30'
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
    date: '2025-01-30'
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7995
    std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.712
    std: 0.039
    paper_value: 0.712
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.039000000000000035
    value_note: global 0.7510 within std
    paper_rank: 79
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.684
    std: 0.033
    paper_value: 0.684
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 46
    true_value: 0.7314
    true_std: 0.007
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0474
    value_note: ''
    paper_rank: 105
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.7314
    sort_std: 0.007
    is_best: false
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.726
    std: 0.033
    paper_value: 0.726
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 56
    true_value: 0.726
    true_std: 0.033
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.033
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.692
    std: 0.048
    paper_value: 0.692
    paper_std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 61
    true_value: 0.723
    true_std: 0.0226
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.031000000000000028
    value_note: global 0.7230 within std
    paper_rank: 104
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.723
    sort_std: 0.0226
    is_best: false
  - model: PathNN-AP (K=2)
    model_key: pathnn-ap (k=2)
    model_plain: PathNN-AP (K=2)
    value: 0.717
    std: 0.036
    paper_value: 0.717
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 71
    true_value: 0.717
    true_std: 0.036
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.036
    is_best: false
  - model: PathNN-SP (K=2)
    model_key: pathnn-sp (k=2)
    model_plain: PathNN-SP (K=2)
    value: 0.705
    std: 0.034
    paper_value: 0.705
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 92
    true_value: 0.705
    true_std: 0.034
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.034
    is_best: false
  - model: PathNet (N=10, K=2)
    model_key: pathnet (n=10, k=2)
    model_plain: PathNet (N=10, K=2)
    value: 0.704
    std: 0.038
    paper_value: 0.704
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 94
    true_value: 0.704
    true_std: 0.038
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.704
    sort_std: 0.038
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.692
    std: 0.03
    paper_value: 0.692
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 97
    true_value: 0.7
    true_std: 0.009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008000000000000007
    value_note: global 0.7000 within std
    paper_rank: 104
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7
    sort_std: 0.009
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.688
    std: 0.045
    paper_value: 0.688
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 105
    true_value: 0.688
    true_std: 0.045
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.688
    sort_std: 0.045
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.677
    std: 0.028
    paper_value: 0.677
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Simonovsky et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 110
    true_value: 0.677
    true_std: 0.028
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.677
    sort_std: 0.028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.63
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.63
    sort_std: 0.02
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.62
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.62
    sort_std: 0.03
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.61
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.456
    std: 0.034
    paper_value: 0.456
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 10
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10400000000000004
    value_note: ''
    paper_rank: 68
    rank_delta: 58
    rank_delta_abs: 58
    rank_delta_direction: worse
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.485
    std: 0.033
    paper_value: 0.485
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 22
    true_value: 0.523
    true_std: 0.028
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.038000000000000034
    value_note: ''
    paper_rank: 60
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: 0.028
    is_best: false
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.508
    std: 0.045
    paper_value: 0.508
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 30
    true_value: 0.508
    true_std: 0.045
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.508
    sort_std: 0.045
    is_best: false
  - model: PathNN-SP (K=2)
    model_key: pathnn-sp (k=2)
    model_plain: PathNN-SP (K=2)
    value: 0.507
    std: 0.045
    paper_value: 0.507
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 32
    true_value: 0.507
    true_std: 0.045
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.507
    sort_std: 0.045
    is_best: false
  - model: PathNN-AP (K=2)
    model_key: pathnn-ap (k=2)
    model_plain: PathNN-AP (K=2)
    value: 0.498
    std: 0.042
    paper_value: 0.498
    paper_std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 44
    true_value: 0.498
    true_std: 0.042
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.498
    sort_std: 0.042
    is_best: false
  - model: PathNet
    model_key: pathnet
    model_plain: PathNet
    value: 0.491
    std: 0.036
    paper_value: 0.491
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 48
    true_value: 0.491
    true_std: 0.036
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.491
    sort_std: 0.036
    is_best: false
  - model: PathNet (N=10, K=2)
    model_key: pathnet (n=10, k=2)
    model_plain: PathNet (N=10, K=2)
    value: 0.491
    std: 0.036
    paper_value: 0.491
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 49
    true_value: 0.491
    true_std: 0.036
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.491
    sort_std: 0.036
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.482
    std: 0.049
    paper_value: 0.482
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Velickovic et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 54
    true_value: 0.489
    true_std: 0.0298
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007000000000000006
    value_note: global 0.4890 within std
    paper_rank: 63
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.489
    sort_std: 0.0298
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.456
    std: 0.034
    paper_value: 0.456
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 66
    true_value: 0.478
    true_std: 0.009
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.021999999999999964
    value_note: global 0.4780 within std
    paper_rank: 68
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.478
    sort_std: 0.009
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.476
    std: 0.035
    paper_value: 0.476
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 67
    true_value: 0.476
    true_std: 0.035
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.476
    sort_std: 0.035
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.435
    std: 0.031
    paper_value: 0.435
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Simonovsky et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 73
    true_value: 0.435
    true_std: 0.031
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.435
    sort_std: 0.031
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: NCI1
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.865
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.865
    sort_std: 0.014
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.86
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.86
    sort_std: 0.018
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8583
    std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8583
    sort_std: 0.0086
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8
    std: 0.014
    paper_value: 0.8
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 18
    true_value: 0.827
    true_std: 0.017
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026999999999999913
    value_note: ''
    paper_rank: 30
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.017
    is_best: false
  - model: PathNN-SP (K=2)
    model_key: pathnn-sp (k=2)
    model_plain: PathNN-SP (K=2)
    value: 0.823
    std: 0.019
    paper_value: 0.823
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 22
    true_value: 0.823
    true_std: 0.019
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.019
    is_best: false
  - model: PathNN-AP (K=2)
    model_key: pathnn-ap (k=2)
    model_plain: PathNN-AP (K=2)
    value: 0.823
    std: 0.017
    paper_value: 0.823
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 23
    true_value: 0.823
    true_std: 0.017
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.017
    is_best: false
  - model: SPN (K=1)
    model_key: spn (k=1)
    model_plain: SPN (K=1)
    value: 0.8
    std: 0.015
    paper_value: 0.8
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 32
    true_value: 0.8
    true_std: 0.015
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.015
    is_best: false
  - model: SPN(k=5)
    model_key: spn(k=5)
    model_plain: SPN(k=5)
    value: 0.786
    std: 0.038
    paper_value: 0.786
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 39
    true_value: 0.786
    true_std: 0.017
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.786
    sort_std: 0.017
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.76
    std: 0.018
    paper_value: 0.76
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 44
    true_value: 0.777
    true_std: 0.015
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.017000000000000015
    value_note: global 0.7770 within std
    paper_rank: 61
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.777
    sort_std: 0.015
    is_best: false
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.775
    std: 0.016
    paper_value: 0.775
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 45
    true_value: 0.775
    true_std: 0.016
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.016
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.773
    std: 0.025
    paper_value: 0.773
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 47
    true_value: 0.773
    true_std: 0.025
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.025
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.769
    std: 0.019
    paper_value: 0.769
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 51
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: 0.019
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.764
    std: 0.017
    paper_value: 0.764
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 57
    true_value: 0.764
    true_std: 0.017
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.017
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.762
    std: 0.014
    paper_value: 0.762
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Simonovsky et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 60
    true_value: 0.762
    true_std: 0.014
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.014
    is_best: false
  - model: PathNet (N=10, K=2)
    model_key: pathnet (n=10, k=2)
    model_plain: PathNet (N=10, K=2)
    value: 0.641
    std: 0.023
    paper_value: 0.641
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 82
    true_value: 0.641
    true_std: 0.023
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.641
    sort_std: 0.023
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.854
    std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.854
    sort_std: 0.044
    is_best: true
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.709
    std: 0.027
    paper_value: 0.709
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 28
    true_value: 0.7634
    true_std: 0.0166
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.054400000000000004
    value_note: ''
    paper_rank: 167
    rank_delta: 139
    rank_delta_abs: 139
    rank_delta_direction: worse
    sort_value: 0.7634
    sort_std: 0.0166
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.737
    std: 0.035
    paper_value: 0.737
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 31
    true_value: 0.7625
    true_std: 0.01
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.025499999999999967
    value_note: global 0.7625 within std
    paper_rank: 101
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.7625
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.733
    std: 0.04
    paper_value: 0.733
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.029000000000000026
    value_note: global 0.7620 within std
    paper_rank: 110
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.73
    std: 0.045
    paper_value: 0.73
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 43
    true_value: 0.759
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.029000000000000026
    value_note: global 0.7590 within std
    paper_rank: 117
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.759
    sort_std: 0.032
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.729
    std: 0.035
    paper_value: 0.729
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 50
    true_value: 0.755
    true_std: 0.009
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.026000000000000023
    value_note: global 0.7550 within std
    paper_rank: 125
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.755
    sort_std: 0.009
    is_best: false
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.752
    std: 0.039
    paper_value: 0.752
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 58
    true_value: 0.752
    true_std: 0.039
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
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
    sort_std: 0.039
    is_best: false
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.742
    std: 0.037
    paper_value: 0.742
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 86
    true_value: 0.742
    true_std: 0.037
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
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
    sort_std: 0.037
    is_best: false
  - model: SPN(k=5)
    model_key: spn(k=5)
    model_plain: SPN(k=5)
    value: 0.742
    std: 0.027
    paper_value: 0.742
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 85
    true_value: 0.742
    true_std: 0.027
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.027
    is_best: false
  - model: PathNN-SP (K=2)
    model_key: pathnn-sp (k=2)
    model_plain: PathNN-SP (K=2)
    value: 0.732
    std: 0.033
    paper_value: 0.732
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 112
    true_value: 0.732
    true_std: 0.033
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: 0.033
    is_best: false
  - model: PathNN-AP (K=2)
    model_key: pathnn-ap (k=2)
    model_plain: PathNN-AP (K=2)
    value: 0.731
    std: 0.04
    paper_value: 0.731
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 115
    true_value: 0.731
    true_std: 0.04
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.04
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.723
    std: 0.034
    paper_value: 0.723
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Simonovsky et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 142
    true_value: 0.723
    true_std: 0.034
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.034
    is_best: false
  - model: SPN (K=1)
    model_key: spn (k=1)
    model_plain: SPN (K=1)
    value: 0.71
    std: 0.037
    paper_value: 0.71
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 165
    true_value: 0.71
    true_std: 0.037
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.037
    is_best: false
  - model: PathNet (N=10, K=2)
    model_key: pathnet (n=10, k=2)
    model_plain: PathNet (N=10, K=2)
    value: 0.705
    std: 0.039
    paper_value: 0.705
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 173
    true_value: 0.705
    true_std: 0.039
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 173
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.039
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3496
    std: 0.0013
    paper_value: 0.3496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 299
    rank_delta: 296
    rank_delta_abs: 296
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3547
    std: 0.0045
    paper_value: 0.3547
    paper_std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 9
    true_value: 0.2429
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11180000000000001
    value_note: ''
    paper_rank: 306
    rank_delta: 297
    rank_delta_abs: 297
    rank_delta_direction: worse
    sort_value: 0.2429
    sort_std: 0.0019
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.342
    std: 0.0013
    paper_value: 0.342
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 292
    rank_delta: 280
    rank_delta_abs: 280
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: PathNN-SP
    model_key: pathnn-sp
    model_plain: PathNN-SP
    value: 0.254
    std: 0.0046
    paper_value: 0.254
    paper_std: 0.0046
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 182
    true_value: 0.254
    true_std: 0.0046
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.254
    sort_std: 0.0046
    is_best: false
  - model: PathNN-AP
    model_key: pathnn-ap
    model_plain: PathNN-AP
    value: 0.2569
    std: 0.003
    paper_value: 0.2569
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 199
    true_value: 0.2569
    true_std: 0.003
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 199
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2569
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: Reddit
  rows:
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
    is_best: true
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
    is_best: true
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
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.778
    std: 0.039
    paper_value: 0.778
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.778
    sort_std: 0.039
    is_best: false
  - model: SPN(k=5)
    model_key: spn(k=5)
    model_plain: SPN(k=5)
    value: 0.774
    std: 0.038
    paper_value: 0.774
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.774
    sort_std: 0.038
    is_best: false
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.769
    std: 0.037
    paper_value: 0.769
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.769
    sort_std: 0.037
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.766
    std: 0.045
    paper_value: 0.766
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.766
    sort_std: 0.045
    is_best: false
  - model: PathNN-SP (K=2)
    model_key: pathnn-sp (k=2)
    model_plain: PathNN-SP (K=2)
    value: 0.765
    std: 0.046
    paper_value: 0.765
    paper_std: 0.046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.765
    sort_std: 0.046
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.753
    std: 0.029
    paper_value: 0.753
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.753
    sort_std: 0.029
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.75
    std: 0.043
    paper_value: 0.75
    paper_std: 0.043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.75
    sort_std: 0.043
    is_best: false
  - model: PathNN-AP (K=2)
    model_key: pathnn-ap (k=2)
    model_plain: PathNN-AP (K=2)
    value: 0.75
    std: 0.044
    paper_value: 0.75
    paper_std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.75
    sort_std: 0.044
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.739
    std: 0.034
    paper_value: 0.739
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.739
    sort_std: 0.034
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.729
    std: 0.02
    paper_value: 0.729
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.729
    sort_std: 0.02
    is_best: false
  - model: SPN (K=1)
    model_key: spn (k=1)
    model_plain: SPN (K=1)
    value: 0.727
    std: 0.026
    paper_value: 0.727
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.727
    sort_std: 0.026
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.726
    std: 0.041
    paper_value: 0.726
    paper_std: 0.041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Simonovsky et al. 2017
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: null
    sort_value: 0.726
    sort_std: 0.041
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.016
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.016
    sort_std: null
    is_best: true
  - model: ESA (PE)
    model_key: esa (pe)
    model_plain: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.017331929457918168
    sort_std: 0.0009253668251948539
    is_best: false
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.079
    std: 0.006
    paper_value: 0.079
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057
    value_note: ''
    paper_rank: 137
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.079
    std: 0.006
    paper_value: 0.079
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar 2021
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057
    value_note: ''
    paper_rank: 137
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 198
    rank_delta: 180
    rank_delta_abs: 180
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying 2021
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 198
    rank_delta: 180
    rank_delta_abs: 180
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: ESAN
    model_key: esan
    model_plain: ESAN
    value: 0.102
    std: 0.003
    paper_value: 0.102
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 30
    true_value: 0.029
    true_std: 0.003
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.073
    value_note: ''
    paper_rank: 176
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.003
    is_best: false
  - model: ESAN
    model_key: esan
    model_plain: ESAN
    value: 0.102
    std: 0.003
    paper_value: 0.102
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua 2022
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 30
    true_value: 0.029
    true_std: 0.003
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.073
    value_note: ''
    paper_rank: 176
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.003
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.258
    std: 0.033
    paper_value: 0.258
    paper_std: 0.033
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus 2023
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 38
    true_value: 0.04
    true_std: 0.006
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.218
    value_note: ''
    paper_rank: 254
    rank_delta: 216
    rank_delta_abs: 216
    rank_delta_direction: worse
    sort_value: 0.04
    sort_std: 0.006
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.258
    std: 0.033
    paper_value: 0.258
    paper_std: 0.033
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus 2023
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 38
    true_value: 0.04
    true_std: 0.006
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.218
    value_note: ''
    paper_rank: 254
    rank_delta: 216
    rank_delta_abs: 216
    rank_delta_direction: worse
    sort_value: 0.04
    sort_std: 0.006
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.387
    std: 0.015
    paper_value: 0.387
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.322
    value_note: ''
    paper_rank: 271
    rank_delta: 198
    rank_delta_abs: 198
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.387
    std: 0.015
    paper_value: 0.387
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.322
    value_note: ''
    paper_rank: 271
    rank_delta: 198
    rank_delta_abs: 198
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.278
    std: 0.003
    paper_value: 0.278
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 126
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.202
    value_note: ''
    paper_rank: 255
    rank_delta: 129
    rank_delta_abs: 129
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.278
    std: 0.003
    paper_value: 0.278
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 126
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.202
    value_note: ''
    paper_rank: 255
    rank_delta: 129
    rank_delta_abs: 129
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.435
    std: 0.011
    paper_value: 0.435
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 127
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.358
    value_note: ''
    paper_rank: 279
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.435
    std: 0.011
    paper_value: 0.435
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 127
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.358
    value_note: ''
    paper_rank: 279
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.384
    std: 0.007
    paper_value: 0.384
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 135
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3063645103769521
    value_note: ''
    paper_rank: 271
    rank_delta: 136
    rank_delta_abs: 136
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.384
    std: 0.007
    paper_value: 0.384
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 135
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3063645103769521
    value_note: ''
    paper_rank: 271
    rank_delta: 136
    rank_delta_abs: 136
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: PathNN-AP
    model_key: pathnn-ap
    model_plain: PathNN-AP
    value: 0.09
    std: 0.004
    paper_value: 0.09
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 167
    true_value: 0.09
    true_std: 0.004
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.09
    sort_std: 0.004
    is_best: false
  - model: PathNN-\mathcal{AP}
    model_key: pathnn-\mathcal{ap}
    model_plain: PathNN-\mathcal{AP}
    value: 0.09
    std: 0.004
    paper_value: 0.09
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
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 168
    true_value: 0.09
    true_std: 0.004
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.09
    sort_std: 0.004
    is_best: false
  - model: KP-GIN+
    model_key: kp-gin+
    model_plain: KP-GIN+
    value: 0.093
    std: 0.007
    paper_value: 0.093
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Feng 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 170
    true_value: 0.093
    true_std: 0.007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.007
    is_best: false
  - model: KP-GIN+
    model_key: kp-gin+
    model_plain: KP-GIN+
    value: 0.093
    std: 0.007
    paper_value: 0.093
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Feng 2022
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 170
    true_value: 0.093
    true_std: 0.007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.007
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.398
    std: 0.002
    paper_value: 0.398
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 202
    true_value: 0.126
    true_std: 0.003
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.272
    value_note: ''
    paper_rank: 274
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.126
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.398
    std: 0.002
    paper_value: 0.398
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton 2017
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 202
    true_value: 0.126
    true_std: 0.003
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.272
    value_note: ''
    paper_rank: 274
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.126
    sort_std: 0.003
    is_best: false
  - model: PathNN-SP
    model_key: pathnn-sp
    model_plain: PathNN-SP
    value: 0.131
    std: 0.008
    paper_value: 0.131
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 209
    true_value: 0.131
    true_std: 0.008
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 209
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.131
    sort_std: 0.008
    is_best: false
  - model: PathNN-\mathcal{SP}
    model_key: pathnn-\mathcal{sp}
    model_plain: PathNN-\mathcal{SP}
    value: 0.131
    std: 0.008
    paper_value: 0.131
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 210
    true_value: 0.131
    true_std: 0.008
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 210
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.131
    sort_std: 0.008
    is_best: false
  - model: GNNML3
    model_key: gnnml3
    model_plain: GNNML3
    value: 0.161
    std: 0.006
    paper_value: 0.161
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Balcılar 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 232
    true_value: 0.161
    true_std: 0.006
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 232
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.161
    sort_std: 0.006
    is_best: false
  - model: GNNML3
    model_key: gnnml3
    model_plain: GNNML3
    value: 0.161
    std: 0.006
    paper_value: 0.161
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Balcilar 2021
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 232
    true_value: 0.161
    true_std: 0.006
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 232
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.161
    sort_std: 0.006
    is_best: false
  - model: 3WLGNN-E
    model_key: 3wlgnn-e
    model_plain: 3WLGNN-E
    value: 0.256
    std: 0.054
    paper_value: 0.256
    paper_std: 0.054
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Maron 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 254
    true_value: 0.256
    true_std: 0.054
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 254
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.256
    sort_std: 0.054
    is_best: false
  - model: 3WLGNN-E
    model_key: 3wlgnn-e
    model_plain: 3WLGNN-E
    value: 0.256
    std: 0.054
    paper_value: 0.256
    paper_std: 0.054
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Maron 2019
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 254
    true_value: 0.256
    true_std: 0.054
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 254
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.256
    sort_std: 0.054
    is_best: false
  - model: GatedGCN + CSE
    model_key: gatedgcn + cse
    model_plain: GatedGCN + CSE
    value: 0.282
    std: 0.015
    paper_value: 0.282
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 257
    true_value: 0.282
    true_std: 0.015
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 257
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.282
    sort_std: 0.015
    is_best: false
  - model: GatedGCN + CSE
    model_key: gatedgcn + cse
    model_plain: GatedGCN + CSE
    value: 0.282
    std: 0.015
    paper_value: 0.282
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 257
    true_value: 0.282
    true_std: 0.015
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 257
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.282
    sort_std: 0.015
    is_best: false
  - model: MoNet
    model_key: monet
    model_plain: MoNet
    value: 0.292
    std: 0.006
    paper_value: 0.292
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Monti 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 258
    true_value: 0.292
    true_std: 0.006
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 258
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.292
    sort_std: 0.006
    is_best: false
  - model: MoNet
    model_key: monet
    model_plain: MoNet
    value: 0.292
    std: 0.006
    paper_value: 0.292
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Monti 2017
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 258
    true_value: 0.292
    true_std: 0.006
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 258
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.292
    sort_std: 0.006
    is_best: false
  - model: RingGNN
    model_key: ringgnn
    model_plain: RingGNN
    value: 0.353
    std: 0.019
    paper_value: 0.353
    paper_std: 0.019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 267
    true_value: 0.353
    true_std: 0.019
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 267
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.353
    sort_std: 0.019
    is_best: false
  - model: RingGNN
    model_key: ringgnn
    model_plain: RingGNN
    value: 0.353
    std: 0.019
    paper_value: 0.353
    paper_std: 0.019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2019
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 267
    true_value: 0.353
    true_std: 0.019
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 267
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.353
    sort_std: 0.019
    is_best: false
  - model: 3WLGNN
    model_key: 3wlgnn
    model_plain: 3WLGNN
    value: 0.407
    std: 0.028
    paper_value: 0.407
    paper_std: 0.028
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Maron 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 275
    true_value: 0.407
    true_std: 0.028
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 275
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.407
    sort_std: 0.028
    is_best: false
  - model: 3WLGNN
    model_key: 3wlgnn
    model_plain: 3WLGNN
    value: 0.407
    std: 0.028
    paper_value: 0.407
    paper_std: 0.028
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Maron 2019
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 275
    true_value: 0.407
    true_std: 0.028
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 275
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.407
    sort_std: 0.028
    is_best: false
  metric: MAE
  higher_is_better: false
- &id011
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7606
    std: 0.0097
    paper_value: 0.7606
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2074999999999999
    value_note: ''
    paper_rank: 150
    rank_delta: 147
    rank_delta_abs: 147
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7558
    std: 0.014
    paper_value: 0.7558
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21219999999999994
    value_note: ''
    paper_rank: 158
    rank_delta: 154
    rank_delta_abs: 154
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.8094
    std: 0.0057
    paper_value: 0.8094
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 9
    true_value: 0.8094
    true_std: 0.0057
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8094
    sort_std: 0.0057
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.8051
    std: 0.0053
    paper_value: 0.8051
    paper_std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 15
    true_value: 0.8051
    true_std: 0.0053
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8051
    sort_std: 0.0053
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.7799
    std: 0.01
    paper_value: 0.7799
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bouritsas 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 19
    true_value: 0.8039
    true_std: 0.009
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02399999999999991
    value_note: ''
    paper_rank: 104
    rank_delta: 85
    rank_delta_abs: 85
    rank_delta_direction: worse
    sort_value: 0.8039
    sort_std: 0.009
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.797
    std: 0.0097
    paper_value: 0.797
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Beaini 2021
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 42
    true_value: 0.797
    true_std: 0.0097
    value_gap_source_arxiv: '2404.09774'
    value_gap_source_title: 'RandAlign: A Parameter-Free Method for Regularizing Graph
      Convolutional Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.797
    sort_std: 0.0097
    is_best: false
  - model: PathNN-SP (K=2)
    model_key: pathnn-sp (k=2)
    model_plain: PathNN-SP (K=2)
    value: 0.7917
    std: 0.0109
    paper_value: 0.7917
    paper_std: 0.0109
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 54
    true_value: 0.7917
    true_std: 0.0109
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7917
    sort_std: 0.0109
    is_best: false
  - model: PathNN-\mathcal{SP}
    model_key: pathnn-\mathcal{sp}
    model_plain: PathNN-\mathcal{SP}
    value: 0.7917
    std: 0.0109
    paper_value: 0.7917
    paper_std: 0.0109
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 55
    true_value: 0.7917
    true_std: 0.0109
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7917
    sort_std: 0.0109
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7905
    std: 0.0132
    paper_value: 0.7905
    paper_std: 0.0132
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso 2020
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 58
    true_value: 0.7905
    true_std: 0.0132
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7905
    sort_std: 0.0132
    is_best: false
  - model: PathNN-AP (K=2)
    model_key: pathnn-ap (k=2)
    model_plain: PathNN-AP (K=2)
    value: 0.7884
    std: 0.0146
    paper_value: 0.7884
    paper_std: 0.0146
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 67
    true_value: 0.7884
    true_std: 0.0146
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7884
    sort_std: 0.0146
    is_best: false
  - model: PathNN-\mathcal{AP}\phantom{*} \, (K=3)
    model_key: pathnn-\mathcal{ap}\phantom{*} \, (k=3)
    model_plain: PathNN-\mathcal{AP}\phantom{*} \, (K=3)
    value: 0.7884
    std: 0.0146
    paper_value: 0.7884
    paper_std: 0.0146
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 68
    true_value: 0.7884
    true_std: 0.0146
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7884
    sort_std: 0.0146
    is_best: false
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.788
    std: 0.0082
    paper_value: 0.788
    paper_std: 0.0082
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Fey 2020
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 74
    true_value: 0.788
    true_std: 0.0082
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.0082
    is_best: false
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.7862
    std: 0.013
    paper_value: 0.7862
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
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 79
    true_value: 0.7862
    true_std: 0.013
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7862
    sort_std: 0.013
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.7838
    std: 0.0099
    paper_value: 0.7838
    paper_std: 0.0099
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Nikolentzos 2023
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 85
    true_value: 0.7838
    true_std: 0.0099
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7838
    sort_std: 0.0099
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.7833
    std: 0.0069
    paper_value: 0.7833
    paper_std: 0.0069
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus 2023
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 89
    true_value: 0.7833
    true_std: 0.0069
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7833
    sort_std: 0.0069
    is_best: false
  - model: ESAN
    model_key: esan
    model_plain: ESAN
    value: 0.78
    std: 0.0142
    paper_value: 0.78
    paper_std: 0.0142
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 91
    true_value: 0.7825
    true_std: 0.0098
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0024999999999999467
    value_note: global 0.7825 within std
    paper_rank: 96
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.7825
    sort_std: 0.0098
    is_best: false
  - model: E-SPN
    model_key: e-spn
    model_plain: E-SPN
    value: 0.771
    std: 0.012
    paper_value: 0.771
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud 2022
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 126
    true_value: 0.771
    true_std: 0.012
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.012
    is_best: false
  - model: GCN+FLAG
    model_key: gcn+flag
    model_plain: GCN+FLAG
    value: 0.7654
    std: 0.0114
    paper_value: 0.7654
    paper_std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong 2020
    variant_inference_reason: 'dataset: exact match'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    global_rank: 140
    true_value: 0.7654
    true_std: 0.0114
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7654
    sort_std: 0.0114
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: GNNBenchmark
  datasets:
  - *id010
- benchmark: OGB
  datasets:
  - *id011
main_figure: /figures/2306.05955/main_figure.png
---

