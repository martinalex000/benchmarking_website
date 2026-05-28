---
title: Asynchronous Message Passing for Addressing Oversquashing in Graph Neural Networks
arxiv_id: '2509.06777'
source_url: ''
authors: []
published_date: Sep 2025
published_date_iso: 2025-09
abstract: Graph Neural Networks (GNNs) suffer from Oversquashing, which occurs when
  tasks require long-range interactions. The problem arises from the presence of bottlenecks
  that limit the propagation of messages among distant nodes. Recently, graph rewiring
  methods modify edge connectivity and are expected to perform well on long-range
  tasks. Yet, graph rewiring compromises the inductive bias, incurring significant
  information loss in solving the downstream task. Furthermore, increasing channel
  capacity may overcome information bottlenecks but enhance the parameter complexity
  of the model. To alleviate these shortcomings, we propose an efficient model-agnostic
  framework that asynchronously updates node features, unlike traditional synchronous
  message passing GNNs. Our framework creates node batches in every layer based on
  the node centrality values. The features of the nodes belonging to these batches
  will only get updated. Asynchronous message updates process information sequentially
  across layers, avoiding simultaneous compression into fixed-capacity channels. We
  also theoretically establish that our proposed framework maintains higher feature
  sensitivity bounds compared to standard synchronous approaches. Our framework is
  applied to six standard graph datasets and two long-range datasets to perform graph
  classification and achieves impressive performances with a $5\
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CAMP (Ours) with GCN
- CAMP-GCN (Closeness)
- + CAMP
- AMP_GIN
- GCN + CAMP
mrr: 0.0049
adjusted_mrr: 0.0049
mrr_dataset_count: 3
benchmark_categories:
- LRGB
- TU Dortmund
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id006
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    model_key: pathnn-\mathcal{p\phantom{s}}\phantom{^+} \, (k=1)
    model_plain: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.718
    std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.355
    std: 0.012
    paper_value: 0.355
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 15
    true_value: 0.584
    true_std: 0.021
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22899999999999998
    value_note: ''
    paper_rank: 61
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.584
    sort_std: 0.021
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.2836
    std: 0.011699999999999999
    paper_value: 0.2836
    paper_std: 0.011699999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 22
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21939999999999998
    value_note: ''
    paper_rank: 109
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.35810000000000003
    std: 0.01
    paper_value: 0.35810000000000003
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 23
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14489999999999997
    value_note: ''
    paper_rank: 61
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: CAMP-GCN (Closeness)
    model_key: camp-gcn (closeness)
    model_plain: CAMP-GCN (Closeness)
    value: 0.466
    std: 0.0226
    paper_value: 0.466
    paper_std: 0.0226
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 34
    true_value: 0.466
    true_std: 0.0226
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.466
    sort_std: 0.0226
    is_best: false
  - model: AMP_GIN
    model_key: amp_gin
    model_plain: AMP_GIN
    value: 0.466
    std: 0.0226
    paper_value: 0.466
    paper_std: 0.0226
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 35
    true_value: 0.466
    true_std: 0.0226
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.466
    sort_std: 0.0226
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.462
    std: 0.0141
    paper_value: 0.462
    paper_std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 36
    true_value: 0.462
    true_std: 0.0141
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.462
    sort_std: 0.0141
    is_best: false
  - model: CAMP-GCN (Degree)
    model_key: camp-gcn (degree)
    model_plain: CAMP-GCN (Degree)
    value: 0.4313
    std: 0.0288
    paper_value: 0.4313
    paper_std: 0.0288
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 39
    true_value: 0.4313
    true_std: 0.0288
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4313
    sort_std: 0.0288
    is_best: false
  - model: CAMP-GCN (Betweenness)
    model_key: camp-gcn (betweenness)
    model_plain: CAMP-GCN (Betweenness)
    value: 0.41869999999999996
    std: 0.0262
    paper_value: 0.41869999999999996
    paper_std: 0.0262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 43
    true_value: 0.41869999999999996
    true_std: 0.0262
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.41869999999999996
    sort_std: 0.0262
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.35710000000000003
    std: 0.011899999999999999
    paper_value: 0.35710000000000003
    paper_std: 0.011899999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 44
    true_value: 0.415
    true_std: 0.03063
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05789999999999995
    value_note: ''
    paper_rank: 61
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.415
    sort_std: 0.03063
    is_best: false
  - model: CAMP-GCN (PageRank)
    model_key: camp-gcn (pagerank)
    model_plain: CAMP-GCN (PageRank)
    value: 0.41
    std: 0.0254
    paper_value: 0.41
    paper_std: 0.0254
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 46
    true_value: 0.41
    true_std: 0.0254
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.41
    sort_std: 0.0254
    is_best: false
  - model: CAMP-GCN (Load)
    model_key: camp-gcn (load)
    model_plain: CAMP-GCN (Load)
    value: 0.3993
    std: 0.024399999999999998
    paper_value: 0.3993
    paper_std: 0.024399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 49
    true_value: 0.3993
    true_std: 0.024399999999999998
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3993
    sort_std: 0.024399999999999998
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.33799999999999997
    std: 0.0011
    paper_value: 0.33799999999999997
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
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 68
    true_value: 0.338
    true_std: 0.00115
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.338
    sort_std: 0.00115
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.3057
    std: 0.014199999999999999
    paper_value: 0.3057
    paper_std: 0.014199999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 79
    true_value: 0.3175
    true_std: 0.02466
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011799999999999977
    value_note: global 0.3175 within std
    paper_rank: 91
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.3175
    sort_std: 0.02466
    is_best: false
  - model: GCN + CAMP
    model_key: gcn + camp
    model_plain: GCN + CAMP
    value: 0.3173
    std: 0.023
    paper_value: 0.3173
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 80
    true_value: 0.3173
    true_std: 0.023
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3173
    sort_std: 0.023
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.292
    std: 0.013600000000000001
    paper_value: 0.292
    paper_std: 0.013600000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 99
    true_value: 0.292
    true_std: 0.013600000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.292
    sort_std: 0.013600000000000001
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.2766
    std: 0.0116
    paper_value: 0.2766
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 104
    true_value: 0.286
    true_std: 0.01186
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009399999999999964
    value_note: global 0.2860 within std
    paper_rank: 114
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.286
    sort_std: 0.01186
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.2752
    std: 0.009899999999999999
    paper_value: 0.2752
    paper_std: 0.009899999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 116
    true_value: 0.2752
    true_std: 0.009899999999999999
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2752
    sort_std: 0.009899999999999999
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.2506
    std: 0.009899999999999999
    paper_value: 0.2506
    paper_std: 0.009899999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 123
    true_value: 0.25067
    true_std: 0.00994
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 7.00000000000145e-05
    value_note: global 0.2507 within std
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25067
    sort_std: 0.00994
    is_best: false
  - model: GCN + CT-Layer
    model_key: gcn + ct-layer
    model_plain: GCN + CT-Layer
    value: 0.16579999999999998
    std: 0.009000000000000001
    paper_value: 0.16579999999999998
    paper_std: 0.009000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 129
    true_value: 0.16583
    true_std: 0.00907
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 3.0000000000030003e-05
    value_note: global 0.1658 within std
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.16583
    sort_std: 0.00907
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
    date: Jan 30, 2025
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
    date: Jan 30, 2025
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
  - model: CAMP-GCN (PageRank)
    model_key: camp-gcn (pagerank)
    model_plain: CAMP-GCN (PageRank)
    value: 0.7148
    std: 0.0147
    paper_value: 0.7148
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 78
    true_value: 0.7148
    true_std: 0.0147
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7148
    sort_std: 0.0147
    is_best: false
  - model: CAMP-GCN (Closeness)
    model_key: camp-gcn (closeness)
    model_plain: CAMP-GCN (Closeness)
    value: 0.71
    std: 0.0199
    paper_value: 0.71
    paper_std: 0.0199
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 83
    true_value: 0.71
    true_std: 0.0199
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.0199
    is_best: false
  - model: CAMP-GCN (Degree)
    model_key: camp-gcn (degree)
    model_plain: CAMP-GCN (Degree)
    value: 0.7064
    std: 0.0168
    paper_value: 0.7064
    paper_std: 0.0168
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 92
    true_value: 0.7064
    true_std: 0.0168
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7064
    sort_std: 0.0168
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.49920000000000003
    std: 0.009899999999999999
    paper_value: 0.49920000000000003
    paper_std: 0.009899999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 97
    true_value: 0.7020000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20280000000000004
    value_note: ''
    paper_rank: 156
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.7020000000000001
    sort_std: null
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.7018000000000001
    std: 0.009899999999999999
    paper_value: 0.7018000000000001
    paper_std: 0.009899999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 99
    true_value: 0.7018000000000001
    true_std: 0.009899999999999999
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7018000000000001
    sort_std: 0.009899999999999999
    is_best: false
  - model: CAMP-GCN (Load)
    model_key: camp-gcn (load)
    model_plain: CAMP-GCN (Load)
    value: 0.6984
    std: 0.0194
    paper_value: 0.6984
    paper_std: 0.0194
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 104
    true_value: 0.6984
    true_std: 0.0194
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6984
    sort_std: 0.0194
    is_best: false
  - model: CAMP-GCN (Betweenness)
    model_key: camp-gcn (betweenness)
    model_plain: CAMP-GCN (Betweenness)
    value: 0.6976
    std: 0.0215
    paper_value: 0.6976
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 105
    true_value: 0.6976
    true_std: 0.0215
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6976
    sort_std: 0.0215
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.6376
    std: 0.0101
    paper_value: 0.6376
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 130
    true_value: 0.6376
    true_std: 0.0101
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6376
    sort_std: 0.0101
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.494
    std: 0.009000000000000001
    paper_value: 0.494
    paper_std: 0.009000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 132
    true_value: 0.629
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.135
    value_note: ''
    paper_rank: 159
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.629
    sort_std: null
    is_best: false
  - model: + CAMP
    model_key: + camp
    model_plain: + CAMP
    value: 0.6244
    std: 0.0215
    paper_value: 0.6244
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 133
    true_value: 0.6244
    true_std: 0.0215
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6244
    sort_std: 0.0215
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.501
    std: 0.009000000000000001
    paper_value: 0.501
    paper_std: 0.009000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 136
    true_value: 0.6082
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10719999999999996
    value_note: ''
    paper_rank: 154
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.6082
    sort_std: null
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.4966
    std: 0.0086
    paper_value: 0.4966
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 138
    true_value: 0.604
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1074
    value_note: ''
    paper_rank: 159
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.604
    sort_std: null
    is_best: false
  - model: + CT-Layer
    model_key: + ct-layer
    model_plain: + CT-Layer
    value: 0.5032
    std: 0.009399999999999999
    paper_value: 0.5032
    paper_std: 0.009399999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 154
    true_value: 0.5032
    true_std: 0.009399999999999999
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5032
    sort_std: 0.009399999999999999
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.4991
    std: 0.0084
    paper_value: 0.4991
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 157
    true_value: 0.4991
    true_std: 0.0084
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4991
    sort_std: 0.0084
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.49770000000000003
    std: 0.008100000000000001
    paper_value: 0.49770000000000003
    paper_std: 0.008100000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 158
    true_value: 0.49770000000000003
    true_std: 0.008100000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49770000000000003
    sort_std: 0.008100000000000001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.984
    std: 0.024
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
    global_rank: 1
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
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
    global_rank: 2
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.98
    std: 0.034
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
    global_rank: 3
    sort_value: 0.98
    sort_std: 0.034
    is_best: true
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.7105
    std: 0.0187
    paper_value: 0.7105
    paper_std: 0.0187
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 26
    true_value: 0.895
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1845
    value_note: ''
    paper_rank: 153
    rank_delta: 127
    rank_delta_abs: 127
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.784
    std: 0.027999999999999997
    paper_value: 0.784
    paper_std: 0.027999999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 27
    true_value: 0.895
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11099999999999999
    value_note: ''
    paper_rank: 118
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.026000000000000002
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.8875
    std: 0.015700000000000002
    paper_value: 0.8875
    paper_std: 0.015700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 36
    true_value: 0.8875
    true_std: 0.015700000000000002
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8875
    sort_std: 0.015700000000000002
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.8079999999999999
    std: 0.025
    paper_value: 0.8079999999999999
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 42
    true_value: 0.8809999999999999
    true_std: 0.027000000000000003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07299999999999995
    value_note: ''
    paper_rank: 97
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.027000000000000003
    is_best: false
  - model: CAMP (Ours) with GCN
    model_key: camp (ours) with gcn
    model_plain: CAMP (Ours) with GCN
    value: 0.8340000000000001
    std: 0.0395
    paper_value: 0.8340000000000001
    paper_std: 0.0395
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 75
    true_value: 0.8340000000000001
    true_std: 0.0395
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8340000000000001
    sort_std: 0.0395
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.784
    std: 0.027999999999999997
    paper_value: 0.784
    paper_std: 0.027999999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 98
    true_value: 0.805
    true_std: 0.04738
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02100000000000002
    value_note: global 0.8050 within std
    paper_rank: 118
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.805
    sort_std: 0.04738
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.8
    std: 0.015700000000000002
    paper_value: 0.8
    paper_std: 0.015700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 104
    true_value: 0.8
    true_std: 0.015700000000000002
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.015700000000000002
    is_best: false
  - model: CAMP-GCN (Degree)
    model_key: camp-gcn (degree)
    model_plain: CAMP-GCN (Degree)
    value: 0.8
    std: 0.0436
    paper_value: 0.8
    paper_std: 0.0436
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 105
    true_value: 0.8
    true_std: 0.0436
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.0436
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.797
    std: 0.0215
    paper_value: 0.797
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 106
    true_value: 0.797
    true_std: 0.0215
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.797
    sort_std: 0.0215
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.7909999999999999
    std: 0.018600000000000002
    paper_value: 0.7909999999999999
    paper_std: 0.018600000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 113
    true_value: 0.7909999999999999
    true_std: 0.018600000000000002
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7909999999999999
    sort_std: 0.018600000000000002
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.7759999999999999
    std: 0.028399999999999998
    paper_value: 0.7759999999999999
    paper_std: 0.028399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 114
    true_value: 0.79
    true_std: 0.03847
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.014000000000000123
    value_note: global 0.7900 within std
    paper_rank: 123
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.79
    sort_std: 0.03847
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.777
    std: 0.0036
    paper_value: 0.777
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 123
    true_value: 0.777
    true_std: 0.0036
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.777
    sort_std: 0.0036
    is_best: false
  - model: CAMP-GCN (Betweenness)
    model_key: camp-gcn (betweenness)
    model_plain: CAMP-GCN (Betweenness)
    value: 0.77
    std: 0.0416
    paper_value: 0.77
    paper_std: 0.0416
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 127
    true_value: 0.77
    true_std: 0.0416
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.0416
    is_best: false
  - model: CAMP-GCN (Closeness)
    model_key: camp-gcn (closeness)
    model_plain: CAMP-GCN (Closeness)
    value: 0.762
    std: 0.0296
    paper_value: 0.762
    paper_std: 0.0296
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 129
    true_value: 0.762
    true_std: 0.0296
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.0296
    is_best: false
  - model: CAMP-GCN (Load)
    model_key: camp-gcn (load)
    model_plain: CAMP-GCN (Load)
    value: 0.76
    std: 0.042800000000000005
    paper_value: 0.76
    paper_std: 0.042800000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 132
    true_value: 0.76
    true_std: 0.042800000000000005
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.042800000000000005
    is_best: false
  - model: CAMP-GCN (PageRank)
    model_key: camp-gcn (pagerank)
    model_plain: CAMP-GCN (PageRank)
    value: 0.74
    std: 0.0408
    paper_value: 0.74
    paper_std: 0.0408
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 140
    true_value: 0.74
    true_std: 0.0408
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.0408
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.7215
    std: 0.024399999999999998
    paper_value: 0.7215
    paper_std: 0.024399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 151
    true_value: 0.7215
    true_std: 0.024399999999999998
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7215
    sort_std: 0.024399999999999998
    is_best: false
  - model: GCN + CT-Layer
    model_key: gcn + ct-layer
    model_plain: GCN + CT-Layer
    value: 0.5685
    std: 0.0425
    paper_value: 0.5685
    paper_std: 0.0425
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 171
    true_value: 0.5685
    true_std: 0.0425
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5685
    sort_std: 0.0425
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.7575
    std: 0.0085
    paper_value: 0.7575
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 37
    true_value: 0.76
    true_std: 0.00774
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0025000000000000577
    value_note: global 0.7600 within std
    paper_rank: 45
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.00774
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.731
    std: 0.008100000000000001
    paper_value: 0.731
    paper_std: 0.008100000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 63
    true_value: 0.75107
    true_std: 0.00817
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020070000000000032
    value_note: ''
    paper_rank: 113
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.75107
    sort_std: 0.00817
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.737
    std: 0.008
    paper_value: 0.737
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 83
    true_value: 0.742
    true_std: 0.008
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0050000000000000044
    value_note: global 0.7420 within std
    paper_rank: 101
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.008
    is_best: false
  - model: CAMP (Ours) with GCN
    model_key: camp (ours) with gcn
    model_plain: CAMP (Ours) with GCN
    value: 0.7406999999999999
    std: 0.0173
    paper_value: 0.7406999999999999
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 92
    true_value: 0.7406999999999999
    true_std: 0.0173
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7406999999999999
    sort_std: 0.0173
    is_best: false
  - model: CAMP-GCN (Closeness)
    model_key: camp-gcn (closeness)
    model_plain: CAMP-GCN (Closeness)
    value: 0.7406999999999999
    std: 0.0173
    paper_value: 0.7406999999999999
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 93
    true_value: 0.7406999999999999
    true_std: 0.0173
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7406999999999999
    sort_std: 0.0173
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.7342
    std: 0.008100000000000001
    paper_value: 0.7342
    paper_std: 0.008100000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 105
    true_value: 0.7342
    true_std: 0.008100000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7342
    sort_std: 0.008100000000000001
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.7313
    std: 0.0069
    paper_value: 0.7313
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 113
    true_value: 0.7313
    true_std: 0.0069
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7313
    sort_std: 0.0069
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.7259
    std: 0.0248
    paper_value: 0.7259
    paper_std: 0.0248
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 122
    true_value: 0.72991
    true_std: 0.01956
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.004009999999999958
    value_note: global 0.7299 within std
    paper_rank: 133
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.72991
    sort_std: 0.01956
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.7092
    std: 0.0079
    paper_value: 0.7092
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 124
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01980000000000004
    value_note: ''
    paper_rank: 167
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.6981
    std: 0.0079
    paper_value: 0.6981
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 125
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03090000000000004
    value_note: ''
    paper_rank: 179
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: CAMP-GCN (PageRank)
    model_key: camp-gcn (pagerank)
    model_plain: CAMP-GCN (PageRank)
    value: 0.7268000000000001
    std: 0.0155
    paper_value: 0.7268000000000001
    paper_std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 131
    true_value: 0.7268000000000001
    true_std: 0.0155
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7268000000000001
    sort_std: 0.0155
    is_best: false
  - model: CAMP-GCN (Load)
    model_key: camp-gcn (load)
    model_plain: CAMP-GCN (Load)
    value: 0.7264
    std: 0.0226
    paper_value: 0.7264
    paper_std: 0.0226
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 132
    true_value: 0.7264
    true_std: 0.0226
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7264
    sort_std: 0.0226
    is_best: false
  - model: CAMP-GCN (Degree)
    model_key: camp-gcn (degree)
    model_plain: CAMP-GCN (Degree)
    value: 0.7239
    std: 0.0189
    paper_value: 0.7239
    paper_std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 137
    true_value: 0.7239
    true_std: 0.0189
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7239
    sort_std: 0.0189
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.7075
    std: 0.0077
    paper_value: 0.7075
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 138
    true_value: 0.72321
    true_std: 0.0144
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.015710000000000002
    value_note: ''
    paper_rank: 171
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.72321
    sort_std: 0.0144
    is_best: false
  - model: CAMP-GCN (Betweenness)
    model_key: camp-gcn (betweenness)
    model_plain: CAMP-GCN (Betweenness)
    value: 0.7206999999999999
    std: 0.0202
    paper_value: 0.7206999999999999
    paper_std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 144
    true_value: 0.7206999999999999
    true_std: 0.0202
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7206999999999999
    sort_std: 0.0202
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.7098
    std: 0.0073
    paper_value: 0.7098
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 167
    true_value: 0.70982
    true_std: 0.00737
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.7098 within std
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.70982
    sort_std: 0.00737
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.708
    std: 0.008199999999999999
    paper_value: 0.708
    paper_std: 0.008199999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 170
    true_value: 0.70804
    true_std: 0.00827
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 4.0000000000040004e-05
    value_note: global 0.7080 within std
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.70804
    sort_std: 0.00827
    is_best: false
  - model: GCN + CT-Layer
    model_key: gcn + ct-layer
    model_plain: GCN + CT-Layer
    value: 0.611
    std: 0.0118
    paper_value: 0.611
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 197
    true_value: 0.61107
    true_std: 0.01184
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 7.00000000000145e-05
    value_note: global 0.6111 within std
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61107
    sort_std: 0.01184
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.6028
    std: 0.0031
    paper_value: 0.6028
    paper_std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 244
    true_value: 0.6028
    true_std: 0.0031
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 244
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6028
    sort_std: 0.0031
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.5993999999999999
    std: 0.0037
    paper_value: 0.5993999999999999
    paper_std: 0.0037
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 251
    true_value: 0.5993999999999999
    true_std: 0.0037
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 251
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5993999999999999
    sort_std: 0.0037
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.5947
    std: 0.0126
    paper_value: 0.5947
    paper_std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 257
    true_value: 0.5947
    true_std: 0.0126
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 257
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5947
    sort_std: 0.0126
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.5947
    std: 0.0034999999999999996
    paper_value: 0.5947
    paper_std: 0.0034999999999999996
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 258
    true_value: 0.5947
    true_std: 0.0034999999999999996
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 258
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5947
    sort_std: 0.0034999999999999996
    is_best: false
  - model: GCN
    model_key: gcn (none)
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 262
    true_value: 0.593
    true_std: 0.0023
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 262
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.593
    sort_std: 0.0023
    is_best: false
  - model: + CAMP
    model_key: + camp
    model_plain: + CAMP
    value: 0.5667
    std: 0.0076
    paper_value: 0.5667
    paper_std: 0.0076
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 282
    true_value: 0.5667
    true_std: 0.0076
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 282
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5667
    sort_std: 0.0076
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
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
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: + CAMP
    model_key: + camp
    model_plain: + CAMP
    value: 0.3138
    std: 0.0041
    paper_value: 0.3138
    paper_std: 0.0041
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 281
    true_value: 0.3138
    true_std: 0.0041
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 281
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3138
    sort_std: 0.0041
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.3272
    std: 0.0001
    paper_value: 0.3272
    paper_std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 288
    true_value: 0.3272
    true_std: 0.0001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 288
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3272
    sort_std: 0.0001
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.3473
    std: 0.0007
    paper_value: 0.3473
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 302
    true_value: 0.3473
    true_std: 0.0007
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 302
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3473
    sort_std: 0.0007
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.3478
    std: 0.0013
    paper_value: 0.3478
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 303
    true_value: 0.3478
    true_std: 0.0013
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 303
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3478
    sort_std: 0.0013
    is_best: false
  - model: GCN
    model_key: gcn (none)
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 305
    true_value: 0.3496
    true_std: 0.0013
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 305
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3496
    sort_std: 0.0013
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.3514
    std: 0.0009
    paper_value: 0.3514
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 308
    true_value: 0.3514
    true_std: 0.0009
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 308
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3514
    sort_std: 0.0009
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
- benchmark: TU Dortmund
  datasets:
  - *id003
  - *id004
  - *id005
  - *id006
main_figure: /figures/2509.06777/main_figure.png
---

