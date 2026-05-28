---
title: Algorithmic Graph Tasks
arxiv_id: '2312.16560'
source_url: ''
authors: []
published_date: Dec 2023
published_date_iso: 2023-12
abstract: 'Long-range interactions are essential for the correct description of complex
  systems in many scientific fields. The price to pay for including them in the calculations,
  however, is a dramatic increase in the overall computational costs. Recently, deep
  graph networks have been employed as efficient, data-driven models for predicting
  properties of complex systems represented as graphs. These models rely on a message
  passing strategy that should, in principle, capture long-range information without
  explicitly modeling the corresponding interactions. In practice, most deep graph
  networks cannot really model long-range dependencies due to the intrinsic limitations
  of (synchronous) message passing, namely oversmoothing, oversquashing, and underreaching.
  This work proposes a general framework that learns to mitigate these limitations:
  within a variational inference framework, we endow message passing architectures
  with the ability to adapt their depth and filter messages along the way. With theoretical
  and empirical arguments, we show that this strategy better captures long-range interactions,
  by competing with the state of the art on five node and graph prediction datasets.'
codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
extraction_model: openai-gpt-oss-120b
has_results: true
paper_type: method
proposed_models:
- AMP_GCN
- AMP_GIN
- AMP_ADGN
- AMP
mrr: 0.0583
adjusted_mrr: 0.0389
mrr_dataset_count: 2
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- TU Dortmund
- Algorithmic Graph Tasks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id008
  dataset: Actor
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.4298
    std: 0.0148
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
    global_rank: 1
    sort_value: 0.4298
    sort_std: 0.0148
    is_best: true
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.4215
    std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.4215
    sort_std: 0.0129
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.4193
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.4193
    sort_std: 0.0104
    is_best: true
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.3222
    std: 0.023399999999999997
    paper_value: 0.3222
    paper_std: 0.023399999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abbasnejad et al. 2019
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 17
    true_value: 0.3776
    true_std: 0.01
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.055400000000000005
    value_note: ''
    paper_rank: 68
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.3776
    sort_std: 0.01
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.3576
    std: 0.0098
    paper_value: 0.3576
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Generic baseline
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 23
    true_value: 0.3736
    true_std: 0.0071
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016000000000000014
    value_note: ''
    paper_rank: 39
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.3736
    sort_std: 0.0071
    is_best: false
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.3586
    std: 0.0103
    paper_value: 0.3586
    paper_std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 38
    true_value: 0.3586
    true_std: 0.0103
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3586
    sort_std: 0.0103
    is_best: false
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.35619999999999996
    std: 0.013000000000000001
    paper_value: 0.35619999999999996
    paper_std: 0.013000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 40
    true_value: 0.35619999999999996
    true_std: 0.013000000000000001
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35619999999999996
    sort_std: 0.013000000000000001
    is_best: false
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.3514
    std: 0.0137
    paper_value: 0.3514
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard et al. 2016; Xu et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 44
    true_value: 0.3514
    true_std: 0.0137
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3514
    sort_std: 0.0137
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.3423
    std: 0.009899999999999999
    paper_value: 0.3423
    paper_std: 0.009899999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 45
    true_value: 0.3507
    true_std: 0.0015
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008400000000000019
    value_note: global 0.3507 within std
    paper_rank: 54
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.3507
    sort_std: 0.0015
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.3428
    std: 0.0101
    paper_value: 0.3428
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017; Xu et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 53
    true_value: 0.3428
    true_std: 0.0101
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3428
    sort_std: 0.0101
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.3418
    std: 0.0085
    paper_value: 0.3418
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2016; Xu et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 55
    true_value: 0.3418
    true_std: 0.0085
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3418
    sort_std: 0.0085
    is_best: false
  - model: AMP
    model_key: amp
    model_plain: AMP
    value: 0.3414
    std: 0.0070999999999999995
    paper_value: 0.3414
    paper_std: 0.0070999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 56
    true_value: 0.3414
    true_std: 0.0070999999999999995
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3414
    sort_std: 0.0070999999999999995
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.3411
    std: 0.0109
    paper_value: 0.3411
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard et al. 2016
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 57
    true_value: 0.3411
    true_std: 0.0109
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3411
    sort_std: 0.0109
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.26280000000000003
    std: 0.0173
    paper_value: 0.26280000000000003
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 59
    true_value: 0.3393
    true_std: 0.0247
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07649999999999996
    value_note: ''
    paper_rank: 87
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.3393
    sort_std: 0.0247
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2802
    std: 0.0059
    paper_value: 0.2802
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2016
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 66
    true_value: 0.3323
    true_std: 0.0116
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05209999999999998
    value_note: ''
    paper_rank: 83
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.3323
    sort_std: 0.0116
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.31629999999999997
    std: null
    paper_value: 0.31629999999999997
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 72
    true_value: 0.31629999999999997
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31629999999999997
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Chameleon
  rows:
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8051
    sort_std: 0.0125
    is_best: true
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8017
    sort_std: 0.0188
    is_best: true
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8002
    sort_std: 0.0087
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4189
    std: 0.0183
    paper_value: 0.4189
    paper_std: 0.0183
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2293
    value_note: ''
    paper_rank: 122
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.6342
    std: 0.02
    paper_value: 0.6342
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 49
    true_value: 0.6468
    true_std: 0.0285
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.012600000000000056
    value_note: global 0.6468 within std
    paper_rank: 52
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.6468
    sort_std: 0.0285
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5468999999999999
    std: 0.0195
    paper_value: 0.5468999999999999
    paper_std: 0.0195
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09210000000000007
    value_note: ''
    paper_rank: 88
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.6379
    std: 0.0227
    paper_value: 0.6379
    paper_std: 0.0227
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 52
    true_value: 0.6379
    true_std: 0.0227
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6379
    sort_std: 0.0227
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.5872999999999999
    std: 0.0168
    paper_value: 0.5872999999999999
    paper_std: 0.0168
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 60
    true_value: 0.6215
    true_std: 0.0042
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03420000000000012
    value_note: ''
    paper_rank: 77
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.6215
    sort_std: 0.0042
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.609
    std: null
    paper_value: 0.609
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 65
    true_value: 0.609
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.609
    sort_std: null
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.605
    std: 0.0253
    paper_value: 0.605
    paper_std: 0.0253
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 67
    true_value: 0.605
    true_std: 0.0253
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.0253
    is_best: false
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.5939
    std: 0.019799999999999998
    paper_value: 0.5939
    paper_std: 0.019799999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 72
    true_value: 0.5939
    true_std: 0.019799999999999998
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5939
    sort_std: 0.019799999999999998
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.5811
    std: 0.0197
    paper_value: 0.5811
    paper_std: 0.0197
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 80
    true_value: 0.5811
    true_std: 0.0197
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5811
    sort_std: 0.0197
    is_best: false
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.5710999999999999
    std: 0.0158
    paper_value: 0.5710999999999999
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 82
    true_value: 0.5710999999999999
    true_std: 0.0158
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5710999999999999
    sort_std: 0.0158
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.5524
    std: 0.0276
    paper_value: 0.5524
    paper_std: 0.0276
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 86
    true_value: 0.5524
    true_std: 0.0276
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5524
    sort_std: 0.0276
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.48560000000000003
    std: 0.017
    paper_value: 0.48560000000000003
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 105
    true_value: 0.48560000000000003
    true_std: 0.017
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48560000000000003
    sort_std: 0.017
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.4636
    std: 0.0252
    paper_value: 0.4636
    paper_std: 0.0252
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 111
    true_value: 0.4636
    true_std: 0.0252
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4636
    sort_std: 0.0252
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7271
    std: 0.0154
    paper_value: 0.7271
    paper_std: 0.0154
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08679999999999999
    value_note: ''
    paper_rank: 112
    rank_delta: 100
    rank_delta_abs: 100
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7545999999999999
    std: 0.0172
    paper_value: 0.7545999999999999
    paper_std: 0.0172
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05060000000000009
    value_note: ''
    paper_rank: 80
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7241
    std: 0.0218
    paper_value: 0.7241
    paper_std: 0.0218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.7939
    true_std: 0.0138
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06980000000000008
    value_note: ''
    paper_rank: 118
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.7939
    sort_std: 0.0138
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7604000000000001
    std: 0.013000000000000001
    paper_value: 0.7604000000000001
    paper_std: 0.013000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 34
    true_value: 0.7923
    true_std: 0.0053
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03189999999999993
    value_note: ''
    paper_rank: 68
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.7923
    sort_std: 0.0053
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.7798999999999999
    std: null
    paper_value: 0.7798999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 37
    true_value: 0.7799
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7799
    sort_std: null
    is_best: false
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.7706999999999999
    std: 0.016399999999999998
    paper_value: 0.7706999999999999
    paper_std: 0.016399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 46
    true_value: 0.7706999999999999
    true_std: 0.016399999999999998
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7706999999999999
    sort_std: 0.016399999999999998
    is_best: false
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.7687999999999999
    std: 0.0177
    paper_value: 0.7687999999999999
    paper_std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 51
    true_value: 0.7687999999999999
    true_std: 0.0177
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7687999999999999
    sort_std: 0.0177
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7626000000000001
    std: 0.013300000000000001
    paper_value: 0.7626000000000001
    paper_std: 0.013300000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 63
    true_value: 0.7626000000000001
    true_std: 0.013300000000000001
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7626000000000001
    sort_std: 0.013300000000000001
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.7605
    std: 0.0137
    paper_value: 0.7605
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 68
    true_value: 0.7605
    true_std: 0.0137
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7605
    sort_std: 0.0137
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.7582
    std: 0.015300000000000001
    paper_value: 0.7582
    paper_std: 0.015300000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 72
    true_value: 0.7582
    true_std: 0.015300000000000001
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7582
    sort_std: 0.015300000000000001
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.7506999999999999
    std: 0.0129
    paper_value: 0.7506999999999999
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 87
    true_value: 0.7506999999999999
    true_std: 0.0129
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7506999999999999
    sort_std: 0.0129
    is_best: false
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.7498
    std: 0.0118
    paper_value: 0.7498
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 90
    true_value: 0.7498
    true_std: 0.0118
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7498
    sort_std: 0.0118
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.7451000000000001
    std: 0.0175
    paper_value: 0.7451000000000001
    paper_std: 0.0175
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 94
    true_value: 0.7451000000000001
    true_std: 0.0175
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7451000000000001
    sort_std: 0.0175
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8268000000000001
    std: 0.018000000000000002
    paper_value: 0.8268000000000001
    paper_std: 0.018000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05569999999999986
    value_note: ''
    paper_rank: 132
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.8781
    std: 0.013500000000000002
    paper_value: 0.8781
    paper_std: 0.013500000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 47
    true_value: 0.8781
    true_std: 0.013500000000000002
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8781
    sort_std: 0.013500000000000002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8423999999999999
    std: 0.0144
    paper_value: 0.8423999999999999
    paper_std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0354000000000001
    value_note: ''
    paper_rank: 108
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.8761
    std: 0.0085
    paper_value: 0.8761
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abbasnejad et al. 2019
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 55
    true_value: 0.8761
    true_std: 0.0085
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8761
    sort_std: 0.0085
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7475
    std: 0.0222
    paper_value: 0.7475
    paper_std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Standard baseline
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 65
    true_value: 0.8709
    true_std: 0.0066
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12339999999999995
    value_note: ''
    paper_rank: 200
    rank_delta: 135
    rank_delta_abs: 135
    rank_delta_direction: worse
    sort_value: 0.8709
    sort_std: 0.0066
    is_best: false
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.8692
    std: 0.0137
    paper_value: 0.8692
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 69
    true_value: 0.8692
    true_std: 0.0137
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8692
    sort_std: 0.0137
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8690000000000001
    std: 0.0104
    paper_value: 0.8690000000000001
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 71
    true_value: 0.8690000000000001
    true_std: 0.0104
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8690000000000001
    sort_std: 0.0104
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.8579000000000001
    std: 0.0092
    paper_value: 0.8579000000000001
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 72
    true_value: 0.869
    true_std: 0.0151
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011099999999999888
    value_note: global 0.8690 within std
    paper_rank: 90
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.869
    sort_std: 0.0151
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.8676
    std: 0.0095
    paper_value: 0.8676
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard et al. 2016
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 74
    true_value: 0.8676
    true_std: 0.0095
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8676
    sort_std: 0.0095
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.8595999999999999
    std: 0.0083
    paper_value: 0.8595999999999999
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 89
    true_value: 0.8595999999999999
    true_std: 0.0083
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8595999999999999
    sort_std: 0.0083
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.8568000000000001
    std: 0.0152
    paper_value: 0.8568000000000001
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 93
    true_value: 0.8568000000000001
    true_std: 0.0152
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8568000000000001
    sort_std: 0.0152
    is_best: false
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.8549
    std: 0.0127
    paper_value: 0.8549
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 94
    true_value: 0.8549
    true_std: 0.0127
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8549
    sort_std: 0.0127
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.8527
    std: null
    paper_value: 0.8527
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 100
    true_value: 0.8527
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8527
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: D&D
  rows:
  - model: AMP_ADGN
    model_key: amp_adgn
    model_plain: AMP_ADGN
    value: -0.5891
    std: 0.072
    paper_value: -0.5891
    paper_std: 0.072
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: -0.5891
    sort_std: 0.072
    is_best: true
  - model: AMP_GIN
    model_key: amp_gin
    model_plain: AMP_GIN
    value: -0.4874
    std: 0.1111
    paper_value: -0.4874
    paper_std: 0.1111
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: -0.4874
    sort_std: 0.1111
    is_best: true
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: -0.453
    std: 0.0883
    paper_value: -0.453
    paper_std: 0.0883
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: -0.453
    sort_std: 0.0883
    is_best: true
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: -0.1072
    std: 0.0791
    paper_value: -0.1072
    paper_std: 0.0791
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: -0.1072
    sort_std: 0.0791
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2408
    std: 0.0154
    paper_value: 0.2408
    paper_std: 0.0154
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 1
    sort_value: 0.2408
    sort_std: 0.0154
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.271
    sort_std: 0.004
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.279
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.09008'
    title: City-Networks
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.279
    sort_std: 0.001
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.282
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.282
    sort_std: 0.03
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5057
    std: 0.0309
    paper_value: 0.5057
    paper_std: 0.0309
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 13
    sort_value: 0.5057
    sort_std: 0.0309
    is_best: false
  - model: DGC
    model_key: dgc
    model_plain: DGC
    value: 0.5601
    std: 0.022
    paper_value: 0.5601
    paper_std: 0.022
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: 0.5601
    sort_std: 0.022
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6146
    std: 0.0375
    paper_value: 0.6146
    paper_std: 0.0375
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 2
    sort_value: 0.6146
    sort_std: 0.0375
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.6146
    std: 0.0744
    paper_value: 0.6146
    paper_std: 0.0744
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 16
    sort_value: 0.6146
    sort_std: 0.0744
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.9477
    std: 0.216
    paper_value: 0.9477
    paper_std: 0.216
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: 0.9477
    sort_std: 0.216
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 1.4367
    std: 0.3558
    paper_value: 1.4367
    paper_std: 0.3558
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 9
    sort_value: 1.4367
    sort_std: 0.3558
    is_best: false
  metric: Accuracy
  higher_is_better: false
- &id013
  dataset: Eccentricity
  rows:
  - model: AMP_ADGN
    model_key: amp_adgn
    model_plain: AMP_ADGN
    value: 0.0515
    std: 0.1819
    paper_value: 0.0515
    paper_std: 0.1819
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 1
    true_value: 0.0515
    true_std: 0.1819
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0515
    sort_std: 0.1819
    is_best: true
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 0.0547
    std: 0.0732
    paper_value: 0.0547
    paper_std: 0.0732
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 2
    true_value: 0.0547
    true_std: 0.0732
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0547
    sort_std: 0.0732
    is_best: true
  - model: AMP_GIN
    model_key: amp_gin
    model_plain: AMP_GIN
    value: 0.4093
    std: 0.0546
    paper_value: 0.4093
    paper_std: 0.0546
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 3
    true_value: 0.4093
    true_std: 0.0546
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4093
    sort_std: 0.0546
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.6054
    std: 0.0919
    paper_value: 0.6054
    paper_std: 0.0919
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 4
    true_value: 0.6054
    true_std: 0.0919
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6054
    sort_std: 0.0919
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.7112
    std: 0.0255
    paper_value: 0.7112
    paper_std: 0.0255
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 5
    true_value: 0.7112
    true_std: 0.0255
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7112
    sort_std: 0.0255
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7398
    std: 0.0705
    paper_value: 0.7398
    paper_std: 0.0705
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 6
    true_value: 0.7398
    true_std: 0.0705
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7398
    sort_std: 0.0705
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.745
    std: 0.1369
    paper_value: 0.745
    paper_std: 0.1369
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 7
    true_value: 0.745
    true_std: 0.1369
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.1369
    is_best: false
  - model: DGC
    model_key: dgc
    model_plain: DGC
    value: 0.8051
    std: 0.0017
    paper_value: 0.8051
    paper_std: 0.0017
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 8
    true_value: 0.8051
    true_std: 0.0017
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8051
    sort_std: 0.0017
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9229
    std: 0.0002
    paper_value: 0.9229
    paper_std: 0.0002
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 9
    true_value: 0.9229
    true_std: 0.0002
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9229
    sort_std: 0.0002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 1.0714
    std: 0.0616
    paper_value: 1.0714
    paper_std: 0.0616
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 10
    true_value: 1.0714
    true_std: 0.0616
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0714
    sort_std: 0.0616
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 1.0859
    std: 0.0001
    paper_value: 1.0859
    paper_std: 0.0001
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 11
    true_value: 1.0859
    true_std: 0.0001
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0859
    sort_std: 0.0001
    is_best: false
  metric: MSE
  higher_is_better: false
- &id009
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1331
    value_note: ''
    paper_rank: 261
    rank_delta: 252
    rank_delta_abs: 252
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.721
    std: 0.0039
    paper_value: 0.721
    paper_std: 0.0039
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 12
    true_value: 0.721
    true_std: 0.0039
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.0039
    is_best: false
  - model: NBA
    model_key: nba
    model_plain: NBA
    value: 0.7207
    std: 0.0028
    paper_value: 0.7207
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 14
    true_value: 0.7207
    true_std: 0.0028
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7207
    sort_std: 0.0028
    is_best: false
  - model: AMP
    model_key: amp
    model_plain: AMP
    value: 0.7161
    std: 0.0047
    paper_value: 0.7161
    paper_std: 0.0047
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 20
    true_value: 0.7163
    true_std: 0.0058
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.000200000000000089
    value_note: global 0.7163 within std
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7163
    sort_std: 0.0058
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.715
    std: 0.0044
    paper_value: 0.715
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 22
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.7041
    std: 0.0049
    paper_value: 0.7041
    paper_std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.7133
    true_std: 0.0011
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009200000000000097
    value_note: ''
    paper_rank: 43
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.7133
    sort_std: 0.0011
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.7074
    std: 0.0032
    paper_value: 0.7074
    paper_std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 37
    true_value: 0.7074
    true_std: 0.0032
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7074
    sort_std: 0.0032
    is_best: false
  - model: PH-DGN
    model_key: ph-dgn
    model_plain: PH-DGN
    value: 0.7012
    std: 0.0045
    paper_value: 0.7012
    paper_std: 0.0045
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 48
    true_value: 0.7012
    true_std: 0.0045
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7012
    sort_std: 0.0045
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6069
    std: 0.0035
    paper_value: 0.6069
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0937
    value_note: ''
    paper_rank: 239
    rank_delta: 190
    rank_delta_abs: 190
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.699
    std: 0.0093
    paper_value: 0.699
    paper_std: 0.0093
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 52
    true_value: 0.699
    true_std: 0.0093
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.699
    sort_std: 0.0093
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.6988
    std: 0.0082
    paper_value: 0.6988
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 53
    true_value: 0.6988
    true_std: 0.0082
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6988
    sort_std: 0.0082
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6942
    std: 0.0075
    paper_value: 0.6942
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 61
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0027999999999999137
    value_note: global 0.6970 within std
    paper_rank: 74
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: G-MLPMixer
    model_key: g-mlpmixer
    model_plain: G-MLPMixer
    value: 0.6921
    std: 0.0054
    paper_value: 0.6921
    paper_std: 0.0054
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 62
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.004899999999999904
    value_note: global 0.6970 within std
    paper_rank: 78
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.6825
    std: 0.0086
    paper_value: 0.6825
    paper_std: 0.0086
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 98
    true_value: 0.6825
    true_std: 0.0086
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6825
    sort_std: 0.0086
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 142
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 288
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 154
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 168
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6527
    std: 0.0043
    paper_value: 0.6527
    paper_std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.644
    std: 0.001
    paper_value: 0.644
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 201
    true_value: 0.644
    true_std: 0.001
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.644
    sort_std: 0.001
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.6439
    std: 0.0075
    paper_value: 0.6439
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 202
    true_value: 0.6439
    true_std: 0.0075
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 202
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6439
    sort_std: 0.0075
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.6326
    std: 0.0126
    paper_value: 0.6326
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
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 218
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  metric: AP
  higher_is_better: true
- &id010
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
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
    paper_rank: 304
    rank_delta: 301
    rank_delta_abs: 301
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.2422
    std: 0.0007
    paper_value: 0.2422
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 5
    true_value: 0.2422
    true_std: 0.0007
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2422
    sort_std: 0.0007
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
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3357
    std: 0.0006
    paper_value: 0.3357
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09259999999999999
    value_note: ''
    paper_rank: 289
    rank_delta: 277
    rank_delta_abs: 277
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: AMP
    model_key: amp
    model_plain: AMP
    value: 0.2446
    std: 0.0026
    paper_value: 0.2446
    paper_std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 15
    true_value: 0.2431
    true_std: 0.0004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015000000000000013
    value_note: global 0.2431 within std
    paper_rank: 29
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.0004
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.2449
    std: 0.0016
    paper_value: 0.2449
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.2584
    std: 0.0015
    paper_value: 0.2584
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 43
    true_value: 0.2455
    true_std: 0.0013
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012900000000000023
    value_note: ''
    paper_rank: 209
    rank_delta: 166
    rank_delta_abs: 166
    rank_delta_direction: worse
    sort_value: 0.2455
    sort_std: 0.0013
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.246
    std: 0.0012
    paper_value: 0.246
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 56
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0012
    is_best: false
  - model: PH-DGN
    model_key: ph-dgn
    model_plain: PH-DGN
    value: 0.2465
    std: 0.002
    paper_value: 0.2465
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 66
    true_value: 0.2465
    true_std: 0.002
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2465
    sort_std: 0.002
    is_best: false
  - model: NBA
    model_key: nba
    model_plain: NBA
    value: 0.2472
    std: 0.0008
    paper_value: 0.2472
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 76
    true_value: 0.2472
    true_std: 0.0008
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2472
    sort_std: 0.0008
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 311
    rank_delta: 232
    rank_delta_abs: 232
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: G-MLPMixer
    model_key: g-mlpmixer
    model_plain: G-MLPMixer
    value: 0.2475
    std: 0.0015
    paper_value: 0.2475
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 84
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0015
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.2477
    std: 0.0005
    paper_value: 0.2477
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 91
    true_value: 0.2477
    true_std: 0.0005
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.0005
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2481
    std: 0.0007
    paper_value: 0.2481
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.2506
    std: 0.0022
    paper_value: 0.2506
    paper_std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 146
    true_value: 0.2506
    true_std: 0.0022
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2506
    sort_std: 0.0022
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.2529
    std: 0.0016
    paper_value: 0.2529
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 169
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.2536
    std: 0.0015
    paper_value: 0.2536
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 174
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2545
    std: 0.0012
    paper_value: 0.2545
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 189
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.3043
    std: 0.0019
    paper_value: 0.3043
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 273
    true_value: 0.3043
    true_std: 0.0019
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 273
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3043
    sort_std: 0.0019
    is_best: false
  metric: MAE
  higher_is_better: false
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
    value: 0.8665
    std: 0.0034999999999999996
    paper_value: 0.8665
    paper_std: 0.0034999999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 3
    true_value: 0.9476
    true_std: 0.001
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08109999999999995
    value_note: ''
    paper_rank: 95
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: ND
    model_key: nd
    model_plain: ND
    value: 0.9256
    std: 0.0071
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
    global_rank: 4
    sort_value: 0.9256
    sort_std: 0.0071
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8762000000000001
    std: 0.0059
    paper_value: 0.8762000000000001
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04619999999999991
    value_note: ''
    paper_rank: 78
    rank_delta: 73
    rank_delta_abs: 73
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8468000000000001
    std: 0.0044
    paper_value: 0.8468000000000001
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07329999999999992
    value_note: ''
    paper_rank: 101
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.8841
    std: 0.0045000000000000005
    paper_value: 0.8841
    paper_std: 0.0045000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 19
    true_value: 0.9009
    true_std: 0.0068
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016800000000000037
    value_note: ''
    paper_rank: 58
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.9009
    sort_std: 0.0068
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.9005
    std: null
    paper_value: 0.9005
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 20
    true_value: 0.9005
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9005
    sort_std: null
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.8967
    std: 0.0129
    paper_value: 0.8967
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 28
    true_value: 0.8967
    true_std: 0.0129
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8967
    sort_std: 0.0129
    is_best: false
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.8959
    std: 0.0033
    paper_value: 0.8959
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.8959
    true_std: 0.0033
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8959
    sort_std: 0.0033
    is_best: false
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.894
    std: 0.0034000000000000002
    paper_value: 0.894
    paper_std: 0.0034000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 36
    true_value: 0.894
    true_std: 0.0034000000000000002
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.0034000000000000002
    is_best: false
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.8906999999999999
    std: 0.003
    paper_value: 0.8906999999999999
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 42
    true_value: 0.8906999999999999
    true_std: 0.003
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8906999999999999
    sort_std: 0.003
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.8872
    std: 0.0055000000000000005
    paper_value: 0.8872
    paper_std: 0.0055000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 51
    true_value: 0.8872
    true_std: 0.0055000000000000005
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8872
    sort_std: 0.0055000000000000005
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8845000000000001
    std: 0.005
    paper_value: 0.8845000000000001
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 54
    true_value: 0.8864
    true_std: 0.003
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0018999999999999018
    value_note: global 0.8864 within std
    paper_rank: 57
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.8864
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.8834000000000001
    std: 0.0062
    paper_value: 0.8834000000000001
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 59
    true_value: 0.8834000000000001
    true_std: 0.0062
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8834000000000001
    sort_std: 0.0062
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.8531
    std: 0.0060999999999999995
    paper_value: 0.8531
    paper_std: 0.0060999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abbasnejad et al. 2019
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 90
    true_value: 0.8704
    true_std: 0.041
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.017299999999999982
    value_note: global 0.8704 within std
    paper_rank: 100
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.8704
    sort_std: 0.041
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: SSSP
  rows:
  - model: AMP_ADGN
    model_key: amp_adgn
    model_plain: AMP_ADGN
    value: -3.9579
    std: 0.0769
    paper_value: -3.9579
    paper_std: 0.0769
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 1
    true_value: -3.9579
    true_std: 0.0769
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: -3.9579
    sort_std: 0.0769
    is_best: true
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: -3.5448
    std: 0.2749
    paper_value: -3.5448
    paper_std: 0.2749
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 2
    true_value: -3.5448
    true_std: 0.2749
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: -3.5448
    sort_std: 0.2749
    is_best: false
  - model: AMP_GIN
    model_key: amp_gin
    model_plain: AMP_GIN
    value: -3.0628
    std: 0.3159
    paper_value: -3.0628
    paper_std: 0.3159
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 3
    true_value: -3.0628
    true_std: 0.3159
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: -3.0628
    sort_std: 0.3159
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: -1.0139
    std: 0.012
    paper_value: -1.0139
    paper_std: 0.012
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 4
    true_value: -1.0139
    true_std: 0.012
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: -1.0139
    sort_std: 0.012
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: -0.9172
    std: 0.4396
    paper_value: -0.9172
    paper_std: 0.4396
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 5
    true_value: -0.9172
    true_std: 0.4396
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: -0.9172
    sort_std: 0.4396
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: -0.2648
    std: 0.4437
    paper_value: -0.2648
    paper_std: 0.4437
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 6
    true_value: -0.2648
    true_std: 0.4437
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: -0.2648
    sort_std: 0.4437
    is_best: false
  - model: DGC
    model_key: dgc
    model_plain: DGC
    value: -0.0254
    std: 0.0077
    paper_value: -0.0254
    paper_std: 0.0077
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 7
    true_value: -0.0254
    true_std: 0.0077
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: -0.0254
    sort_std: 0.0077
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.1909
    std: 0.3103
    paper_value: 0.1909
    paper_std: 0.3103
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 8
    true_value: 0.1909
    true_std: 0.3103
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1909
    sort_std: 0.3103
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.544
    std: 0.0108
    paper_value: 0.544
    paper_std: 0.0108
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 9
    true_value: 0.544
    true_std: 0.0108
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.544
    sort_std: 0.0108
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.607
    std: 0.0375
    paper_value: 0.607
    paper_std: 0.0375
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 10
    true_value: 0.607
    true_std: 0.0375
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.607
    sort_std: 0.0375
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9132
    std: 0.0051
    paper_value: 0.9132
    paper_std: 0.0051
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 11
    true_value: 0.9132
    true_std: 0.0051
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9132
    sort_std: 0.0051
    is_best: false
  metric: MSE
  higher_is_better: false
- &id007
  dataset: Squirrel
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7601
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7601
    sort_std: 0.019
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7531
    std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7531
    sort_std: 0.0192
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.741
    std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2773
    std: 0.0091
    paper_value: 0.2773
    paper_std: 0.0091
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.257
    value_note: ''
    paper_rank: 109
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.4045
    std: 0.0161
    paper_value: 0.4045
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 32
    true_value: 0.534
    true_std: 0.019
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1295
    value_note: ''
    paper_rank: 76
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.534
    sort_std: 0.019
    is_best: false
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.45030000000000003
    std: 0.0173
    paper_value: 0.45030000000000003
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 49
    true_value: 0.45030000000000003
    true_std: 0.0173
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.45030000000000003
    sort_std: 0.0173
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3062
    std: 0.021099999999999997
    paper_value: 0.3062
    paper_std: 0.021099999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1387
    value_note: ''
    paper_rank: 109
    rank_delta: 58
    rank_delta_abs: 58
    rank_delta_direction: worse
    sort_value: 0.4449
    sort_std: 0.0088
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.4386
    std: 0.016399999999999998
    paper_value: 0.4386
    paper_std: 0.016399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 52
    true_value: 0.4386
    true_std: 0.016399999999999998
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4386
    sort_std: 0.016399999999999998
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.43799999999999994
    std: 0.0148
    paper_value: 0.43799999999999994
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abbasnejad et al. 2019
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 54
    true_value: 0.438
    true_std: 0.0148
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.438
    sort_std: 0.0148
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.41609999999999997
    std: 0.0074
    paper_value: 0.41609999999999997
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 69
    true_value: 0.41609999999999997
    true_std: 0.0074
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.41609999999999997
    sort_std: 0.0074
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.40850000000000003
    std: 0.0129
    paper_value: 0.40850000000000003
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 73
    true_value: 0.40850000000000003
    true_std: 0.0129
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.40850000000000003
    sort_std: 0.0129
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.3814
    std: null
    paper_value: 0.3814
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 85
    true_value: 0.3815
    true_std: 0.0092
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.3815 within std
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3815
    sort_std: 0.0092
    is_best: false
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.379
    std: 0.0202
    paper_value: 0.379
    paper_std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 87
    true_value: 0.379
    true_std: 0.0202
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.379
    sort_std: 0.0202
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.2968
    std: 0.0181
    paper_value: 0.2968
    paper_std: 0.0181
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 96
    true_value: 0.366
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06919999999999998
    value_note: ''
    paper_rank: 109
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.366
    sort_std: 0.018000000000000002
    is_best: false
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.3642
    std: 0.0189
    paper_value: 0.3642
    paper_std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 97
    true_value: 0.3642
    true_std: 0.0189
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3642
    sort_std: 0.0189
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.3528
    std: 0.0095
    paper_value: 0.3528
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 102
    true_value: 0.3528
    true_std: 0.0095
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3528
    sort_std: 0.0095
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
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
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
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
    global_rank: 2
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
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
    global_rank: 3
    sort_value: 0.9475
    sort_std: 0.0309
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.8189
    std: 0.0478
    paper_value: 0.8189
    paper_std: 0.0478
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baseline
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 14
    true_value: 0.923
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10410000000000008
    value_note: ''
    paper_rank: 54
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.923
    sort_std: 0.007
    is_best: false
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.8486
    std: 0.0677
    paper_value: 0.8486
    paper_std: 0.0677
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 38
    true_value: 0.8486
    true_std: 0.0677
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8486
    sort_std: 0.0677
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.8378
    std: 0.022099999999999998
    paper_value: 0.8378
    paper_std: 0.022099999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 43
    true_value: 0.8378
    true_std: 0.022099999999999998
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8378
    sort_std: 0.022099999999999998
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5273
    std: 0.059800000000000006
    paper_value: 0.5273
    paper_std: 0.059800000000000006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.30379999999999996
    value_note: ''
    paper_rank: 162
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8243
    std: 0.061399999999999996
    paper_value: 0.8243
    paper_std: 0.061399999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 51
    true_value: 0.8243
    true_std: 0.061399999999999996
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.061399999999999996
    is_best: false
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.8216
    std: 0.0528
    paper_value: 0.8216
    paper_std: 0.0528
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 53
    true_value: 0.8216
    true_std: 0.0528
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8216
    sort_std: 0.0528
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.8146
    std: 0.030600000000000002
    paper_value: 0.8146
    paper_std: 0.030600000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 55
    true_value: 0.8146
    true_std: 0.030600000000000002
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8146
    sort_std: 0.030600000000000002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5838
    std: 0.044500000000000005
    paper_value: 0.5838
    paper_std: 0.044500000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22440000000000004
    value_note: ''
    paper_rank: 150
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.6648999999999999
    std: 0.0664
    paper_value: 0.6648999999999999
    paper_std: 0.0664
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 63
    true_value: 0.8066
    true_std: 0.0191
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14170000000000005
    value_note: ''
    paper_rank: 124
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.8066
    sort_std: 0.0191
    is_best: false
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.7837999999999999
    std: 0.0637
    paper_value: 0.7837999999999999
    paper_std: 0.0637
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 69
    true_value: 0.7837999999999999
    true_std: 0.0637
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7837999999999999
    sort_std: 0.0637
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7784
    std: 0.07730000000000001
    paper_value: 0.7784
    paper_std: 0.07730000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abbasnejad et al. 2019
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 70
    true_value: 0.7784
    true_std: 0.07730000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7784
    sort_std: 0.07730000000000001
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.773
    std: 0.0407
    paper_value: 0.773
    paper_std: 0.0407
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard et al. 2016
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 78
    true_value: 0.773
    true_std: 0.0407
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.0407
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6757
    std: null
    paper_value: 0.6757
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 119
    true_value: 0.676
    true_std: null
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.000300000000000078
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.676
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Wisconsin
  rows:
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.8529000000000001
    std: 0.0361
    paper_value: 0.8529000000000001
    paper_std: 0.0361
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baseline
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 2
    true_value: 0.918
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06509999999999994
    value_note: ''
    paper_rank: 21
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9
    std: 0.028300000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9
    sort_std: 0.028300000000000002
    is_best: true
  - model: H2GCN-1
    model_key: h2gcn-1
    model_plain: H2GCN-1
    value: 0.8667
    std: 0.046900000000000004
    paper_value: 0.8667
    paper_std: 0.046900000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 20
    true_value: 0.8667
    true_std: 0.046900000000000004
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8667
    sort_std: 0.046900000000000004
    is_best: true
  - model: H2GCN-2
    model_key: h2gcn-2
    model_plain: H2GCN-2
    value: 0.8588
    std: 0.042199999999999994
    paper_value: 0.8588
    paper_std: 0.042199999999999994
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 21
    true_value: 0.8588
    true_std: 0.042199999999999994
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8588
    sort_std: 0.042199999999999994
    is_best: true
  - model: Cheby+JK
    model_key: cheby+jk
    model_plain: Cheby+JK
    value: 0.8255
    std: 0.045700000000000005
    paper_value: 0.8255
    paper_std: 0.045700000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 28
    true_value: 0.8255
    true_std: 0.045700000000000005
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8255
    sort_std: 0.045700000000000005
    is_best: false
  - model: GraphSAGE+JK
    model_key: graphsage+jk
    model_plain: GraphSAGE+JK
    value: 0.8195999999999999
    std: 0.0496
    paper_value: 0.8195999999999999
    paper_std: 0.0496
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 32
    true_value: 0.8195999999999999
    true_std: 0.0496
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8195999999999999
    sort_std: 0.0496
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8118000000000001
    std: 0.0556
    paper_value: 0.8118000000000001
    paper_std: 0.0556
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 36
    true_value: 0.8136
    true_std: 0.0391
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0017999999999999128
    value_note: global 0.8136 within std
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8136
    sort_std: 0.0391
    is_best: false
  - model: AMP_GCN
    model_key: amp_gcn
    model_plain: AMP_GCN
    value: 0.8045
    std: 0.0447
    paper_value: 0.8045
    paper_std: 0.0447
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 37
    true_value: 0.8045
    true_std: 0.0447
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8045
    sort_std: 0.0447
    is_best: false
  - model: GCN-Cheby
    model_key: gcn-cheby
    model_plain: GCN-Cheby
    value: 0.7940999999999999
    std: 0.0446
    paper_value: 0.7940999999999999
    paper_std: 0.0446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 49
    true_value: 0.7940999999999999
    true_std: 0.0446
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7940999999999999
    sort_std: 0.0446
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.449
    std: 0.0738
    paper_value: 0.449
    paper_std: 0.0738
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3373
    value_note: ''
    paper_rank: 139
    rank_delta: 86
    rank_delta_abs: 86
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5529
    std: 0.08710000000000001
    paper_value: 0.5529
    paper_std: 0.08710000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 61
    true_value: 0.7817
    true_std: 0.057
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2288
    value_note: ''
    paper_rank: 127
    rank_delta: 66
    rank_delta_abs: 66
    rank_delta_direction: worse
    sort_value: 0.7817
    sort_std: 0.057
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7587999999999999
    std: 0.049
    paper_value: 0.7587999999999999
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abbasnejad et al. 2019
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 66
    true_value: 0.7745
    true_std: 0.031
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.015700000000000047
    value_note: global 0.7745 within std
    paper_rank: 76
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.7745
    sort_std: 0.031
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.7431
    std: 0.0643
    paper_value: 0.7431
    paper_std: 0.0643
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 89
    true_value: 0.7431
    true_std: 0.0643
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7431
    sort_std: 0.0643
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6412
    std: null
    paper_value: 0.6412
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 111
    true_value: 0.6451
    true_std: 0.0366
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0039000000000000146
    value_note: global 0.6451 within std
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6451
    sort_std: 0.0366
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterophilic Graphs
  datasets:
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
- benchmark: LRGB
  datasets:
  - *id009
  - *id010
- benchmark: TU Dortmund
  datasets:
  - *id011
- benchmark: Algorithmic Graph Tasks
  datasets:
  - *id012
  - *id013
main_figure: /figures/2312.16560/main_figure.png
---

