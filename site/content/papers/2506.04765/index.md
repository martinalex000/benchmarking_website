---
title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
arxiv_id: '2506.04765'
source_url: ''
authors: []
published_date: Jun 2025
published_date_iso: 2025-06
abstract: Graph Transformers (GTs) have recently demonstrated remarkable performance
  across diverse domains. By leveraging attention mechanisms, GTs are capable of modeling
  long-range dependencies and complex structural relationships beyond local neighborhoods.
  However, their applicable scenarios are still underexplored, this highlights the
  need to identify when and why they excel. Furthermore, unlike GNNs, which predominantly
  rely on message-passing mechanisms, GTs exhibit a diverse design space in areas
  such as positional encoding, attention mechanisms, and graph-specific adaptations.
  Yet, it remains unclear which of these design choices are truly effective and under
  what conditions. As a result, the community currently lacks a comprehensive benchmark
  and library to promote a deeper understanding and further development of GTs. To
  address this gap, this paper introduces OpenGT, a comprehensive benchmark for Graph
  Transformers. OpenGT enables fair comparisons and multidimensional analysis by establishing
  standardized experimental settings and incorporating a broad selection of state-of-the-art
  GNN and GTs. Our benchmark evaluates GTs from multiple perspectives, encompassing
  diverse tasks (both node-level and graph-level) and datasets with varying properties,
  such as scale, homophily, and sparsity. Through extensive experiments, our benchmark
  has uncovered several critical insights, including the difficulty of transferring
  models across task levels, the limitations of local attention, the efficiency trade-offs
  in several models, the application scenarios of specific positional encodings, and
  the preprocessing overhead of some positional encodings. We aspire for this work
  to establish a foundation for future graph transformer research emphasizing fairness,
  reproducibility, and generalizability. We have developed an easy-to-use library
  OpenGT for training and evaluating existing GTs. The benchmark code is available
  at https://github.com/eaglelab-zju/OpenGT.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GRIT
- DIFFormer
- DIFFormer+GE
mrr: 0.1111
adjusted_mrr: 0.037
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- OGB
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id009
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
    value: 0.3647
    std: 0.0087
    paper_value: 0.3647
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: De Bie et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.4193
    true_std: 0.0104
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05459999999999998
    value_note: ''
    paper_rank: 33
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.4193
    sort_std: 0.0104
    is_best: true
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.4181
    std: 0.0052
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
    global_rank: 4
    sort_value: 0.4181
    sort_std: 0.0052
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.3746
    std: 0.0084
    paper_value: 0.3746
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.4169
    true_std: 0.0063
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042300000000000004
    value_note: ''
    paper_rank: 20
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.4169
    sort_std: 0.0063
    is_best: true
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.3719
    std: 0.0088
    paper_value: 0.3719
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 22
    true_value: 0.374
    true_std: 0.01
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0020999999999999908
    value_note: global 0.3740 within std
    paper_rank: 25
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.374
    sort_std: 0.01
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.3721
    std: 0.0117
    paper_value: 0.3721
    paper_std: 0.0117
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Beaini et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 25
    true_value: 0.3721
    true_std: 0.0117
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3721
    sort_std: 0.0117
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.3713
    std: 0.0057
    paper_value: 0.3713
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 27
    true_value: 0.3713
    true_std: 0.0057
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3713
    sort_std: 0.0057
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.352
    std: 0.0047
    paper_value: 0.352
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 28
    true_value: 0.369
    true_std: 0.01
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017000000000000015
    value_note: ''
    paper_rank: 42
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.369
    sort_std: 0.01
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.3682
    std: 0.011
    paper_value: 0.3682
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 29
    true_value: 0.3682
    true_std: 0.011
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3682
    sort_std: 0.011
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3577
    std: 0.0045
    paper_value: 0.3577
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tay et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 39
    true_value: 0.3577
    true_std: 0.0045
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3577
    sort_std: 0.0045
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.2798
    std: 0.0017
    paper_value: 0.2798
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 42
    true_value: 0.3532
    true_std: 0.0053
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07340000000000002
    value_note: ''
    paper_rank: 83
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.3532
    sort_std: 0.0053
    is_best: false
  - model: DeGTA
    model_key: degta
    model_plain: DeGTA
    value: 0.3507
    std: 0.0067
    paper_value: 0.3507
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 46
    true_value: 0.3507
    true_std: 0.0067
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3507
    sort_std: 0.0067
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.2842
    std: 0.0121
    paper_value: 0.2842
    paper_std: 0.0121
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 59
    true_value: 0.3393
    true_std: 0.0247
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05509999999999998
    value_note: ''
    paper_rank: 82
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.3393
    sort_std: 0.0247
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2713
    std: 0.0089
    paper_value: 0.2713
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 66
    true_value: 0.3323
    true_std: 0.0116
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.061
    value_note: ''
    paper_rank: 86
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.3323
    sort_std: 0.0116
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.2873
    std: 0.0006
    paper_value: 0.2873
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 82
    true_value: 0.2873
    true_std: 0.0006
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2873
    sort_std: 0.0006
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.6623
    std: 0.0089
    paper_value: 0.6623
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 15
    true_value: 0.7472
    true_std: 0.0129
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08489999999999998
    value_note: ''
    paper_rank: 38
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.7472
    sort_std: 0.0129
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4415
    std: 0.0169
    paper_value: 0.4415
    paper_std: 0.0169
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2067
    value_note: ''
    paper_rank: 117
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4613
    std: 0.0021
    paper_value: 0.4613
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17770000000000002
    value_note: ''
    paper_rank: 111
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.508
    std: 0.001
    paper_value: 0.508
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 62
    true_value: 0.6144
    true_std: 0.0137
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10639999999999994
    value_note: ''
    paper_rank: 99
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.6144
    sort_std: 0.0137
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4788
    std: 0.0058
    paper_value: 0.4788
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 84
    true_value: 0.5634
    true_std: 0.0111
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08460000000000001
    value_note: ''
    paper_rank: 106
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.5634
    sort_std: 0.0111
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.4189
    std: 0.0267
    paper_value: 0.4189
    paper_std: 0.0267
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 85
    true_value: 0.5562
    true_std: 0.0043
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13730000000000003
    value_note: ''
    paper_rank: 122
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.5562
    sort_std: 0.0043
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.5453
    std: 0.0136
    paper_value: 0.5453
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 90
    true_value: 0.5453
    true_std: 0.0136
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5453
    sort_std: 0.0136
    is_best: false
  - model: DIFFormer+GE
    model_key: difformer+ge
    model_plain: DIFFormer+GE
    value: 0.5446
    std: 0.001
    paper_value: 0.5446
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 91
    true_value: 0.5446
    true_std: 0.001
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5446
    sort_std: 0.001
    is_best: false
  - model: SGFormer+GE
    model_key: sgformer+ge
    model_plain: SGFormer+GE
    value: 0.5446
    std: 0.0075
    paper_value: 0.5446
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 92
    true_value: 0.5446
    true_std: 0.0075
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5446
    sort_std: 0.0075
    is_best: false
  - model: GPS+GE
    model_key: gps+ge
    model_plain: GPS+GE
    value: 0.5395
    std: 0.0142
    paper_value: 0.5395
    paper_std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 93
    true_value: 0.5395
    true_std: 0.0142
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5395
    sort_std: 0.0142
    is_best: false
  - model: GPS+GESP
    model_key: gps+gesp
    model_plain: GPS+GESP
    value: 0.5387
    std: 0.0152
    paper_value: 0.5387
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 94
    true_value: 0.5387
    true_std: 0.0152
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5387
    sort_std: 0.0152
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.4956
    std: 0.01
    paper_value: 0.4956
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 96
    true_value: 0.5191
    true_std: 0.0056
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02350000000000002
    value_note: ''
    paper_rank: 100
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.5191
    sort_std: 0.0056
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.5161
    std: 0.0068
    paper_value: 0.5161
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 97
    true_value: 0.5161
    true_std: 0.0068
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5161
    sort_std: 0.0068
    is_best: false
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.5124
    std: 0.0057
    paper_value: 0.5124
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 99
    true_value: 0.5124
    true_std: 0.0057
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5124
    sort_std: 0.0057
    is_best: false
  - model: DeGTA
    model_key: degta
    model_plain: DeGTA
    value: 0.492
    std: 0.0045
    paper_value: 0.492
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 103
    true_value: 0.492
    true_std: 0.0045
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.492
    sort_std: 0.0045
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.4905
    std: 0.0092
    paper_value: 0.4905
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 104
    true_value: 0.4905
    true_std: 0.0092
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4905
    sort_std: 0.0092
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.4854
    std: 0.0058
    paper_value: 0.4854
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 106
    true_value: 0.4854
    true_std: 0.0058
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4854
    sort_std: 0.0058
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.4722
    std: 0.026
    paper_value: 0.4722
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 107
    true_value: 0.4722
    true_std: 0.026
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4722
    sort_std: 0.026
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.4006
    std: 0.0055
    paper_value: 0.4006
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 125
    true_value: 0.4006
    true_std: 0.0055
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4006
    sort_std: 0.0055
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7103
    std: 0.0175
    paper_value: 0.7103
    paper_std: 0.0175
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 20
    true_value: 0.887
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17669999999999997
    value_note: ''
    paper_rank: 237
    rank_delta: 217
    rank_delta_abs: 217
    rank_delta_direction: worse
    sort_value: 0.887
    sort_std: 0.002
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.4883
    std: 0.0084
    paper_value: 0.4883
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 26
    true_value: 0.8857
    true_std: 0.0101
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.39740000000000003
    value_note: ''
    paper_rank: 297
    rank_delta: 271
    rank_delta_abs: 271
    rank_delta_direction: worse
    sort_value: 0.8857
    sort_std: 0.0101
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.746
    std: 0.0116
    paper_value: 0.746
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13649999999999995
    value_note: ''
    paper_rank: 202
    rank_delta: 171
    rank_delta_abs: 171
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.7243
    std: 0.0118
    paper_value: 0.7243
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 34
    true_value: 0.882
    true_std: 0.012
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15769999999999995
    value_note: ''
    paper_rank: 224
    rank_delta: 190
    rank_delta_abs: 190
    rank_delta_direction: worse
    sort_value: 0.882
    sort_std: 0.012
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7703
    std: 0.0021
    paper_value: 0.7703
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 37
    true_value: 0.8809999999999999
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11069999999999991
    value_note: ''
    paper_rank: 183
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.006999999999999999
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.7713
    std: 0.0101
    paper_value: 0.7713
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 39
    true_value: 0.88
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10870000000000002
    value_note: ''
    paper_rank: 182
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.718
    std: 0.0298
    paper_value: 0.718
    paper_std: 0.0298
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15980000000000005
    value_note: ''
    paper_rank: 232
    rank_delta: 184
    rank_delta_abs: 184
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.612
    std: 0.0213
    paper_value: 0.612
    paper_std: 0.0213
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 124
    true_value: 0.8329
    true_std: 0.0136
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22089999999999999
    value_note: ''
    paper_rank: 279
    rank_delta: 155
    rank_delta_abs: 155
    rank_delta_direction: worse
    sort_value: 0.8329
    sort_std: 0.0136
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.5403
    std: 0.054
    paper_value: 0.5403
    paper_std: 0.054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 143
    true_value: 0.8191
    true_std: 0.0342
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27880000000000005
    value_note: ''
    paper_rank: 295
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.8191
    sort_std: 0.0342
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.7913
    std: 0.0052
    paper_value: 0.7913
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 166
    true_value: 0.7913
    true_std: 0.0052
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7913
    sort_std: 0.0052
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.765
    std: 0.0099
    paper_value: 0.765
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 188
    true_value: 0.765
    true_std: 0.0099
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.765
    sort_std: 0.0099
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.4323
    std: 0.0455
    paper_value: 0.4323
    paper_std: 0.0455
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 192
    true_value: 0.758
    true_std: 0.011
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3257
    value_note: ''
    paper_rank: 299
    rank_delta: 107
    rank_delta_abs: 107
    rank_delta_direction: worse
    sort_value: 0.758
    sort_std: 0.011
    is_best: false
  - model: DeGTA
    model_key: degta
    model_plain: DeGTA
    value: 0.7533
    std: 0.0056
    paper_value: 0.7533
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 197
    true_value: 0.7533
    true_std: 0.0056
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7533
    sort_std: 0.0056
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.715
    std: 0.0051
    paper_value: 0.715
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 234
    true_value: 0.715
    true_std: 0.0051
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 234
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0051
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
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
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
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
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
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
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.4414
    std: 0.0127
    paper_value: 0.4414
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 8
    true_value: 0.918
    true_std: 0.0063
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4766
    value_note: ''
    paper_rank: 141
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.918
    sort_std: 0.0063
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3243
    std: 0.0441
    paper_value: 0.3243
    paper_std: 0.0441
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.5003
    value_note: ''
    paper_rank: 148
    rank_delta: 121
    rank_delta_abs: 121
    rank_delta_direction: worse
    sort_value: 0.8246
    sort_std: 0.0311
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3513
    std: 0.0441
    paper_value: 0.3513
    paper_std: 0.0441
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 37
    true_value: 0.76
    true_std: 0.0101
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4087
    value_note: ''
    paper_rank: 148
    rank_delta: 111
    rank_delta_abs: 111
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.0101
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.7478
    std: 0.0255
    paper_value: 0.7478
    paper_std: 0.0255
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 40
    true_value: 0.7478
    true_std: 0.0255
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7478
    sort_std: 0.0255
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7297
    std: 0.0221
    paper_value: 0.7297
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 46
    true_value: 0.7297
    true_std: 0.0221
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7297
    sort_std: 0.0221
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7207
    std: 0.0127
    paper_value: 0.7207
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 51
    true_value: 0.7207
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7207
    sort_std: 0.0127
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.7117
    std: 0.0127
    paper_value: 0.7117
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 56
    true_value: 0.7117
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7117
    sort_std: 0.0127
    is_best: false
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.7117
    std: 0.0337
    paper_value: 0.7117
    paper_std: 0.0337
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 57
    true_value: 0.7117
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7117
    sort_std: 0.0337
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.6667
    std: 0.0337
    paper_value: 0.6667
    paper_std: 0.0337
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 80
    true_value: 0.6667
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6667
    sort_std: 0.0337
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6577
    std: 0.0459
    paper_value: 0.6577
    paper_std: 0.0459
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 87
    true_value: 0.6577
    true_std: 0.0459
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6577
    sort_std: 0.0459
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.6486
    std: 0.0584
    paper_value: 0.6486
    paper_std: 0.0584
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 91
    true_value: 0.6486
    true_std: 0.0584
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6486
    sort_std: 0.0584
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.6486
    std: 0.0441
    paper_value: 0.6486
    paper_std: 0.0441
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 90
    true_value: 0.6486
    true_std: 0.0441
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6486
    sort_std: 0.0441
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.5405
    std: 0.0441
    paper_value: 0.5405
    paper_std: 0.0441
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 116
    true_value: 0.5405
    true_std: 0.0441
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5405
    sort_std: 0.0441
    is_best: false
  - model: DeGTA
    model_key: degta
    model_plain: DeGTA
    value: 0.5315
    std: 0.0459
    paper_value: 0.5315
    paper_std: 0.0459
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 121
    true_value: 0.5315
    true_std: 0.0459
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5315
    sort_std: 0.0459
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.3874
    std: 0.0127
    paper_value: 0.3874
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 146
    true_value: 0.3874
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3874
    sort_std: 0.0127
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
    value: 0.3614
    std: 0.0036
    paper_value: 0.3614
    paper_std: 0.0036
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.36469999999999997
    value_note: ''
    paper_rank: 315
    rank_delta: 306
    rank_delta_abs: 306
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GraphMLPMixer
    model_key: graphmlpmixer
    model_plain: GraphMLPMixer
    value: 0.4225
    std: 0.0095
    paper_value: 0.4225
    paper_std: 0.0095
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 64
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27449999999999997
    value_note: ''
    paper_rank: 309
    rank_delta: 245
    rank_delta_abs: 245
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3719
    std: 0.0041
    paper_value: 0.3719
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 78
    true_value: 0.6924
    true_std: 0.0044
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3205
    value_note: ''
    paper_rank: 314
    rank_delta: 236
    rank_delta_abs: 236
    rank_delta_direction: worse
    sort_value: 0.6924
    sort_std: 0.0044
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6565
    std: 0.0038
    paper_value: 0.6565
    paper_std: 0.0038
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 154
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0036000000000000476
    value_note: global 0.6601 within std
    paper_rank: 165
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.3622
    std: 0.0036
    paper_value: 0.3622
    paper_std: 0.0036
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 174
    true_value: 0.6534
    true_std: 0.0091
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.29119999999999996
    value_note: ''
    paper_rank: 314
    rank_delta: 140
    rank_delta_abs: 140
    rank_delta_direction: worse
    sort_value: 0.6534
    sort_std: 0.0091
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.4003
    std: 0.0058
    paper_value: 0.4003
    paper_std: 0.0058
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25239999999999996
    value_note: ''
    paper_rank: 310
    rank_delta: 132
    rank_delta_abs: 132
    rank_delta_direction: worse
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.6427
    std: 0.0035
    paper_value: 0.6427
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 206
    true_value: 0.6427
    true_std: 0.0035
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 206
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6427
    sort_std: 0.0035
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.3964
    std: 0.0022
    paper_value: 0.3964
    paper_std: 0.0022
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 311
    true_value: 0.3964
    true_std: 0.0022
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 311
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3964
    sort_std: 0.0022
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.381
    std: 0.0013
    paper_value: 0.381
    paper_std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 313
    true_value: 0.381
    true_std: 0.0013
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 313
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.381
    sort_std: 0.0013
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.3726
    std: 0.0018
    paper_value: 0.3726
    paper_std: 0.0018
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 314
    true_value: 0.3726
    true_std: 0.0018
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 314
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3726
    sort_std: 0.0018
    is_best: false
  metric: AP
  higher_is_better: true
- &id011
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
    value: 0.4347
    std: 0.0033
    paper_value: 0.4347
    paper_std: 0.0033
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19259999999999997
    value_note: ''
    paper_rank: 333
    rank_delta: 330
    rank_delta_abs: 330
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
  - model: GraphMLPMixer
    model_key: graphmlpmixer
    model_plain: GraphMLPMixer
    value: 0.3065
    std: 0.0019
    paper_value: 0.3065
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 88
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059
    value_note: ''
    paper_rank: 275
    rank_delta: 187
    rank_delta_abs: 187
    rank_delta_direction: worse
    sort_value: 0.2475
    sort_std: 0.0015
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3297
    std: 0.0085
    paper_value: 0.3297
    paper_std: 0.0085
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0816
    value_note: ''
    paper_rank: 288
    rank_delta: 186
    rank_delta_abs: 186
    rank_delta_direction: worse
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4231
    std: 0.0049
    paper_value: 0.4231
    paper_std: 0.0049
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 120
    true_value: 0.2488
    true_std: 0.0018
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17429999999999998
    value_note: ''
    paper_rank: 332
    rank_delta: 212
    rank_delta_abs: 212
    rank_delta_direction: worse
    sort_value: 0.2488
    sort_std: 0.0018
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2512
    std: 0.0008
    paper_value: 0.2512
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0011999999999999789
    value_note: ''
    paper_rank: 155
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.4345
    std: 0.0026
    paper_value: 0.4345
    paper_std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 150
    true_value: 0.2509
    true_std: 0.0014
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18359999999999999
    value_note: ''
    paper_rank: 333
    rank_delta: 183
    rank_delta_abs: 183
    rank_delta_direction: worse
    sort_value: 0.2509
    sort_std: 0.0014
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.2851
    std: 0.0112
    paper_value: 0.2851
    paper_std: 0.0112
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 261
    true_value: 0.2851
    true_std: 0.0112
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 261
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2851
    sort_std: 0.0112
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.4374
    std: 0.005
    paper_value: 0.4374
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 335
    true_value: 0.4374
    true_std: 0.005
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 335
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4374
    sort_std: 0.005
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4492
    std: 0.0002
    paper_value: 0.4492
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 336
    true_value: 0.4492
    true_std: 0.0002
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 336
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4492
    sort_std: 0.0002
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.4541
    std: 0.0005
    paper_value: 0.4541
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 338
    true_value: 0.4541
    true_std: 0.0005
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 338
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4541
    sort_std: 0.0005
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.715
    std: 0.0297
    paper_value: 0.715
    paper_std: 0.0297
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20740000000000003
    value_note: ''
    paper_rank: 153
    rank_delta: 148
    rank_delta_abs: 148
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.759
    std: 0.0184
    paper_value: 0.759
    paper_std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16110000000000002
    value_note: ''
    paper_rank: 129
    rank_delta: 123
    rank_delta_abs: 123
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.6973
    std: 0.0079
    paper_value: 0.6973
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 13
    true_value: 0.9061
    true_std: 0.0023
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20879999999999999
    value_note: ''
    paper_rank: 155
    rank_delta: 142
    rank_delta_abs: 142
    rank_delta_direction: worse
    sort_value: 0.9061
    sort_std: 0.0023
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7347
    std: 0.0034
    paper_value: 0.7347
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 26
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1623
    value_note: ''
    paper_rank: 149
    rank_delta: 123
    rank_delta_abs: 123
    rank_delta_direction: worse
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6987
    std: 0.017
    paper_value: 0.6987
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 32
    true_value: 0.8952
    true_std: 0.0054
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1965
    value_note: ''
    paper_rank: 154
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.8952
    sort_std: 0.0054
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.7587
    std: 0.0066
    paper_value: 0.7587
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 33
    true_value: 0.8951
    true_std: 0.0067
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13639999999999997
    value_note: ''
    paper_rank: 129
    rank_delta: 96
    rank_delta_abs: 96
    rank_delta_direction: worse
    sort_value: 0.8951
    sort_std: 0.0067
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6953
    std: 0.0144
    paper_value: 0.6953
    paper_std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 38
    true_value: 0.8932
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19789999999999996
    value_note: ''
    paper_rank: 155
    rank_delta: 117
    rank_delta_abs: 117
    rank_delta_direction: worse
    sort_value: 0.8932
    sort_std: 0.0025
    is_best: false
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.7203
    std: 0.0133
    paper_value: 0.7203
    paper_std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 43
    true_value: 0.89
    true_std: 0.004
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16969999999999996
    value_note: ''
    paper_rank: 152
    rank_delta: 109
    rank_delta_abs: 109
    rank_delta_direction: worse
    sort_value: 0.89
    sort_std: 0.004
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.775
    std: 0.0046
    paper_value: 0.775
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 58
    true_value: 0.8843
    true_std: 0.0015
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10929999999999995
    value_note: ''
    paper_rank: 125
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.8843
    sort_std: 0.0015
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.742
    std: 0.0099
    paper_value: 0.742
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 148
    true_value: 0.742
    true_std: 0.0099
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.0099
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7327
    std: 0.0184
    paper_value: 0.7327
    paper_std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 150
    true_value: 0.7327
    true_std: 0.0184
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7327
    sort_std: 0.0184
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.4454
    std: 0.0141
    paper_value: 0.4454
    paper_std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 16
    true_value: 0.6464
    true_std: 0.0081
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20099999999999996
    value_note: ''
    paper_rank: 50
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.6464
    sort_std: 0.0081
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2917
    std: 0.0094
    paper_value: 0.2917
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.24259999999999998
    value_note: ''
    paper_rank: 109
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.3401
    std: 0.0068
    paper_value: 0.3401
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 48
    true_value: 0.4582
    true_std: 0.0217
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11809999999999998
    value_note: ''
    paper_rank: 105
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.4582
    sort_std: 0.0217
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3016
    std: 0.0086
    paper_value: 0.3016
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14330000000000004
    value_note: ''
    paper_rank: 109
    rank_delta: 58
    rank_delta_abs: 58
    rank_delta_direction: worse
    sort_value: 0.4449
    sort_std: 0.0088
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.3442
    std: 0.0063
    paper_value: 0.3442
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 56
    true_value: 0.4342
    true_std: 0.0162
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08999999999999997
    value_note: ''
    paper_rank: 104
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.4342
    sort_std: 0.0162
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.431
    std: 0.012
    paper_value: 0.431
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 60
    true_value: 0.431
    true_std: 0.012
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.431
    sort_std: 0.012
    is_best: false
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.3737
    std: 0.0049
    paper_value: 0.3737
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 94
    true_value: 0.3737
    true_std: 0.0049
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3737
    sort_std: 0.0049
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.3602
    std: 0.007
    paper_value: 0.3602
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 99
    true_value: 0.3602
    true_std: 0.007
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3602
    sort_std: 0.007
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.3535
    std: 0.0062
    paper_value: 0.3535
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 100
    true_value: 0.3535
    true_std: 0.0062
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3535
    sort_std: 0.0062
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.3333
    std: 0.0088
    paper_value: 0.3333
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 101
    true_value: 0.353
    true_std: 0.019
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019699999999999995
    value_note: ''
    paper_rank: 106
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.353
    sort_std: 0.019
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.349
    std: 0.0071
    paper_value: 0.349
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 103
    true_value: 0.349
    true_std: 0.0071
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.349
    sort_std: 0.0071
    is_best: false
  - model: DeGTA
    model_key: degta
    model_plain: DeGTA
    value: 0.3164
    std: 0.0079
    paper_value: 0.3164
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 108
    true_value: 0.3164
    true_std: 0.0079
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3164
    sort_std: 0.0079
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.2767
    std: 0.0077
    paper_value: 0.2767
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 110
    true_value: 0.2767
    true_std: 0.0077
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2767
    sort_std: 0.0077
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
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7568
    std: 0.0221
    paper_value: 0.7568
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 13
    true_value: 0.9246
    true_std: 0.0148
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16779999999999995
    value_note: ''
    paper_rank: 87
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.9246
    sort_std: 0.0148
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.5405
    std: 0.0
    paper_value: 0.5405
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 19
    true_value: 0.9118
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3713000000000001
    value_note: ''
    paper_rank: 161
    rank_delta: 142
    rank_delta_abs: 142
    rank_delta_direction: worse
    sort_value: 0.9118
    sort_std: 0.007
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.7838
    std: 0.0221
    paper_value: 0.7838
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 29
    true_value: 0.8823
    true_std: 0.0038
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09849999999999992
    value_note: ''
    paper_rank: 68
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.8823
    sort_std: 0.0038
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6937
    std: 0.0255
    paper_value: 0.6937
    paper_std: 0.0255
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 39
    true_value: 0.8463
    true_std: 0.0347
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15260000000000007
    value_note: ''
    paper_rank: 116
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.8463
    sort_std: 0.0347
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4505
    std: 0.0709
    paper_value: 0.4505
    paper_std: 0.0709
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.38059999999999994
    value_note: ''
    paper_rank: 168
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3604
    std: 0.1469
    paper_value: 0.3604
    paper_std: 0.1469
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.44780000000000003
    value_note: ''
    paper_rank: 172
    rank_delta: 111
    rank_delta_abs: 111
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.7748
    std: 0.0127
    paper_value: 0.7748
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 76
    true_value: 0.7748
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7748
    sort_std: 0.0127
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7478
    std: 0.0127
    paper_value: 0.7478
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 77
    true_value: 0.773
    true_std: 0.013
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0252
    value_note: ''
    paper_rank: 93
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.773
    sort_std: 0.013
    is_best: false
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.7387
    std: 0.0637
    paper_value: 0.7387
    paper_std: 0.0637
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 98
    true_value: 0.7387
    true_std: 0.0637
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7387
    sort_std: 0.0637
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.7207
    std: 0.0337
    paper_value: 0.7207
    paper_std: 0.0337
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 109
    true_value: 0.7207
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7207
    sort_std: 0.0337
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.7027
    std: 0.0382
    paper_value: 0.7027
    paper_std: 0.0382
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 115
    true_value: 0.7027
    true_std: 0.0382
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7027
    sort_std: 0.0382
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.6667
    std: 0.0337
    paper_value: 0.6667
    paper_std: 0.0337
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 124
    true_value: 0.6667
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6667
    sort_std: 0.0337
    is_best: false
  - model: DeGTA
    model_key: degta
    model_plain: DeGTA
    value: 0.6126
    std: 0.0127
    paper_value: 0.6126
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 143
    true_value: 0.6126
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6126
    sort_std: 0.0127
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.6036
    std: 0.0255
    paper_value: 0.6036
    paper_std: 0.0255
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 146
    true_value: 0.6036
    true_std: 0.0255
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6036
    sort_std: 0.0255
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3784
    std: 0.0221
    paper_value: 0.3784
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 171
    true_value: 0.3784
    true_std: 0.0221
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3784
    sort_std: 0.0221
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
    value: 0.918
    std: 0.031
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
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.4641
    std: 0.0092
    paper_value: 0.4641
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.901
    true_std: 0.035
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4369
    value_note: ''
    paper_rank: 139
    rank_delta: 136
    rank_delta_abs: 136
    rank_delta_direction: worse
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
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.8039
    std: 0.016
    paper_value: 0.8039
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 40
    true_value: 0.8039
    true_std: 0.016
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.016
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7974
    std: 0.0092
    paper_value: 0.7974
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 45
    true_value: 0.798
    true_std: 0.09
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0006000000000000449
    value_note: global 0.7980 within std
    paper_rank: 47
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.798
    sort_std: 0.09
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4379
    std: 0.0515
    paper_value: 0.4379
    paper_std: 0.0515
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3484
    value_note: ''
    paper_rank: 141
    rank_delta: 88
    rank_delta_abs: 88
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7843
    std: 0.016
    paper_value: 0.7843
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 57
    true_value: 0.7843
    true_std: 0.016
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7843
    sort_std: 0.016
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7843
    std: 0.0
    paper_value: 0.7843
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 58
    true_value: 0.7843
    true_std: 0.0
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7843
    sort_std: 0.0
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3791
    std: 0.0606
    paper_value: 0.3791
    paper_std: 0.0606
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 61
    true_value: 0.7817
    true_std: 0.057
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.40259999999999996
    value_note: ''
    paper_rank: 143
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.7817
    sort_std: 0.057
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.7778
    std: 0.0092
    paper_value: 0.7778
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 63
    true_value: 0.7778
    true_std: 0.0092
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7778
    sort_std: 0.0092
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.7582
    std: 0.0244
    paper_value: 0.7582
    paper_std: 0.0244
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 70
    true_value: 0.77
    true_std: 0.019
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011800000000000033
    value_note: global 0.7700 within std
    paper_rank: 76
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.77
    sort_std: 0.019
    is_best: false
  - model: CoBFormer
    model_key: cobformer
    model_plain: CoBFormer
    value: 0.7647
    std: 0.032
    paper_value: 0.7647
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 73
    true_value: 0.7647
    true_std: 0.032
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7647
    sort_std: 0.032
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.7451
    std: 0.032
    paper_value: 0.7451
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 87
    true_value: 0.7451
    true_std: 0.032
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7451
    sort_std: 0.032
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7386
    std: 0.0403
    paper_value: 0.7386
    paper_std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 91
    true_value: 0.7386
    true_std: 0.0403
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7386
    sort_std: 0.0403
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6994
    std: 0.0333
    paper_value: 0.6994
    paper_std: 0.0333
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 98
    true_value: 0.6994
    true_std: 0.0333
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6994
    sort_std: 0.0333
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.5229
    std: 0.0462
    paper_value: 0.5229
    paper_std: 0.0462
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 131
    true_value: 0.5229
    true_std: 0.0462
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5229
    sort_std: 0.0462
    is_best: false
  - model: DeGTA
    model_key: degta
    model_plain: DeGTA
    value: 0.5229
    std: 0.0092
    paper_value: 0.5229
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 132
    true_value: 0.5229
    true_std: 0.0092
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5229
    sort_std: 0.0092
    is_best: false
  metric: Accuracy
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
    date: May 5, 2024
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.0607
    std: 0.0
    paper_value: 0.0607
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 9
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0377
    value_note: ''
    paper_rank: 59
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.0607
    std: 0.0
    paper_value: 0.0607
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 9
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0377
    value_note: ''
    paper_rank: 59
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.1968
    std: 0.012
    paper_value: 0.1968
    paper_std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.172958
    value_note: ''
    paper_rank: 257
    rank_delta: 244
    rank_delta_abs: 244
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.1305
    std: 0.0072
    paper_value: 0.1305
    paper_std: 0.0072
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10550000000000001
    value_note: ''
    paper_rank: 216
    rank_delta: 198
    rank_delta_abs: 198
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.1905
    std: 0.0276
    paper_value: 0.1905
    paper_std: 0.0276
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 77
    true_value: 0.066
    true_std: 0.003
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1245
    value_note: ''
    paper_rank: 254
    rank_delta: 177
    rank_delta_abs: 177
    rank_delta_direction: worse
    sort_value: 0.066
    sort_std: 0.003
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.0681
    std: 0.0004
    paper_value: 0.0681
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 95
    true_value: 0.0681
    true_std: 0.0004
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0681
    sort_std: 0.0004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.609
    std: 0.0155
    paper_value: 0.609
    paper_std: 0.0155
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.533
    value_note: ''
    paper_rank: 299
    rank_delta: 168
    rank_delta_abs: 168
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6225
    std: 0.0096
    paper_value: 0.6225
    paper_std: 0.0096
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 142
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.5448645103769522
    value_note: ''
    paper_rank: 299
    rank_delta: 157
    rank_delta_abs: 157
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.1341
    std: 0.0063
    paper_value: 0.1341
    paper_std: 0.0063
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 224
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 224
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: GPS+GE
    model_key: gps+ge
    model_plain: GPS+GE
    value: 0.1789
    std: 0.0071
    paper_value: 0.1789
    paper_std: 0.0071
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 249
    true_value: 0.1789
    true_std: 0.0071
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 249
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1789
    sort_std: 0.0071
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.6703
    std: 0.0033
    paper_value: 0.6703
    paper_std: 0.0033
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 275
    true_value: 0.306
    true_std: 0.023
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3643
    value_note: ''
    paper_rank: 303
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.306
    sort_std: 0.023
    is_best: false
  - model: GraphMLPMixer
    model_key: graphmlpmixer
    model_plain: GraphMLPMixer
    value: 0.3617
    std: 0.0222
    paper_value: 0.3617
    paper_std: 0.0222
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 285
    true_value: 0.3617
    true_std: 0.0222
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 285
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3617
    sort_std: 0.0222
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.6038
    std: 0.0151
    paper_value: 0.6038
    paper_std: 0.0151
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 298
    true_value: 0.6038
    true_std: 0.0151
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 298
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6038
    sort_std: 0.0151
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.6602
    std: 0.0294
    paper_value: 0.6602
    paper_std: 0.0294
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 302
    true_value: 0.6602
    true_std: 0.0294
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 302
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6602
    sort_std: 0.0294
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.6619
    std: 0.0067
    paper_value: 0.6619
    paper_std: 0.0067
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 303
    true_value: 0.6619
    true_std: 0.0067
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 303
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6619
    sort_std: 0.0067
    is_best: false
  metric: MAE
  higher_is_better: false
- &id012
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
    value: 0.7385
    std: 0.03
    paper_value: 0.7385
    paper_std: 0.03
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.9682
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2296999999999999
    value_note: ''
    paper_rank: 197
    rank_delta: 195
    rank_delta_abs: 195
    rank_delta_direction: worse
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6888
    std: 0.0127
    paper_value: 0.6888
    paper_std: 0.0127
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2793
    value_note: ''
    paper_rank: 213
    rank_delta: 210
    rank_delta_abs: 210
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.968
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
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
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7715
    std: 0.0135
    paper_value: 0.7715
    paper_std: 0.0135
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 76
    true_value: 0.788
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01650000000000007
    value_note: ''
    paper_rank: 133
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.788
    sort_std: 0.01
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.7608
    std: 0.0165
    paper_value: 0.7608
    paper_std: 0.0165
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 92
    true_value: 0.7835
    true_std: 0.0054
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022699999999999942
    value_note: ''
    paper_rank: 160
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.7835
    sort_std: 0.0054
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.7713
    std: 0.0105
    paper_value: 0.7713
    paper_std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 134
    true_value: 0.7713
    true_std: 0.0105
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7713
    sort_std: 0.0105
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.755
    std: 0.005
    paper_value: 0.755
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 174
    true_value: 0.755
    true_std: 0.005
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.005
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.7169
    std: 0.0103
    paper_value: 0.7169
    paper_std: 0.0103
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 209
    true_value: 0.7169
    true_std: 0.0103
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 209
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7169
    sort_std: 0.0103
    is_best: false
  - model: GraphMLPMixer
    model_key: graphmlpmixer
    model_plain: GraphMLPMixer
    value: 0.6889
    std: 0.0146
    paper_value: 0.6889
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 213
    true_value: 0.6889
    true_std: 0.0146
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 213
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6889
    sort_std: 0.0146
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.6794
    std: 0.0076
    paper_value: 0.6794
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 215
    true_value: 0.6794
    true_std: 0.0076
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 215
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6794
    sort_std: 0.0076
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.635
    std: 0.0112
    paper_value: 0.635
    paper_std: 0.0112
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 219
    true_value: 0.635
    true_std: 0.0112
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 219
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.635
    sort_std: 0.0112
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id013
  dataset: ogbg-molpcba
  rows:
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3141
    sort_std: 0.0019
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3086
    sort_std: 0.0031
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.2888
    std: 0.0019
    paper_value: 0.2888
    paper_std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 22
    true_value: 0.2907
    true_std: 0.0028
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0019000000000000128
    value_note: global 0.2907 within std
    paper_rank: 23
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.2907
    sort_std: 0.0028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.0953
    std: 0.0012
    paper_value: 0.0953
    paper_std: 0.0012
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 40
    true_value: 0.2721
    true_std: 0.0046
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1768
    value_note: ''
    paper_rank: 59
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.2721
    sort_std: 0.0046
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.1931
    std: 0.0018
    paper_value: 0.1931
    paper_std: 0.0018
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 52
    true_value: 0.2362
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0431
    value_note: ''
    paper_rank: 54
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.2362
    sort_std: 0.002
    is_best: false
  - model: GraphMLPMixer
    model_key: graphmlpmixer
    model_plain: GraphMLPMixer
    value: 0.1386
    std: 0.0018
    paper_value: 0.1386
    paper_std: 0.0018
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 56
    true_value: 0.1386
    true_std: 0.0018
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1386
    sort_std: 0.0018
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.1012
    std: 0.0015
    paper_value: 0.1012
    paper_std: 0.0015
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 57
    true_value: 0.1012
    true_std: 0.0015
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1012
    sort_std: 0.0015
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.0973
    std: 0.0011
    paper_value: 0.0973
    paper_std: 0.0011
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 58
    true_value: 0.0973
    true_std: 0.0011
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0973
    sort_std: 0.0011
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.0968
    std: 0.0
    paper_value: 0.0968
    paper_std: 0.0
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 59
    true_value: 0.0968
    true_std: 0.0
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0968
    sort_std: 0.0
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.0933
    std: 0.004
    paper_value: 0.0933
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 60
    true_value: 0.0933
    true_std: 0.004
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0933
    sort_std: 0.004
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.0785
    std: 0.0021
    paper_value: 0.0785
    paper_std: 0.0021
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 61
    true_value: 0.0785
    true_std: 0.0021
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0785
    sort_std: 0.0021
    is_best: false
  metric: AP
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
  - *id009
- benchmark: LRGB
  datasets:
  - *id010
  - *id011
- benchmark: OGB
  datasets:
  - *id012
  - *id013
main_figure: /figures/2506.04765/main_figure.png
---

