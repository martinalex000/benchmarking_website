---
title: 'GSLB: The Graph Structure Learning Benchmark'
arxiv_id: '2310.05174'
source_url: ''
authors: []
published_date: Oct 2023
published_date_iso: 2023-10
abstract: 'Graph Structure Learning (GSL) has recently garnered considerable attention
  due to its ability to optimize both the parameters of Graph Neural Networks (GNNs)
  and the computation graph structure simultaneously. Despite the proliferation of
  GSL methods developed in recent years, there is no standard experimental setting
  or fair comparison for performance evaluation, which creates a great obstacle to
  understanding the progress in this field. To fill this gap, we systematically analyze
  the performance of GSL in different scenarios and develop a comprehensive Graph
  Structure Learning Benchmark (GSLB) curated from 20 diverse graph datasets and 16
  distinct GSL algorithms. Specifically, GSLB systematically investigates the characteristics
  of GSL in terms of three dimensions: effectiveness, robustness, and complexity.
  We comprehensively evaluate state-of-the-art GSL algorithms in node- and graph-level
  tasks, and analyze their performance in robust learning and model complexity. Further,
  to facilitate reproducible research, we have developed an easy-to-use library for
  training, evaluating, and visualizing different GSL methods. Empirical results of
  our extensive experiments demonstrate the ability of GSL and reveal its potential
  benefits on various downstream tasks, offering insights and opportunities for future
  research. The code of GSLB is available at: https://github.com/GSL-Benchmark/GSLB.'
codebase_url: ''
extraction_model: glm-4.7
has_results: true
paper_type: method
proposed_models:
- HES-GSL
- HGSL
- VIB-GSL (GCN)
- HGP-SL (GCN)
- VIB-GSL (GAT)
- VIB-GSL (SAGE)
- HGP-SL (SAGE)
mrr: 0.0153
adjusted_mrr: 0.0153
mrr_dataset_count: 6
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- TU Dortmund
- OGB
- Heterogeneous Graph Benchmarks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id016
  dataset: ACM
  rows:
  - model: HGSL
    model_key: hgsl
    model_plain: HGSL
    value: 0.9313
    std: 0.0051
    paper_value: 0.9313
    paper_std: 0.0051
    metric: Micro-F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 1
    true_value: 0.9313
    true_std: 0.0051
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9313
    sort_std: 0.0051
    is_best: true
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.9294
    std: 0.0018
    paper_value: 0.9294
    paper_std: 0.0018
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 2
    true_value: 0.9294
    true_std: 0.0018
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9294
    sort_std: 0.0018
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.9213
    std: 0.0037
    paper_value: 0.9213
    paper_std: 0.0037
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.9213
    true_std: 0.0037
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9213
    sort_std: 0.0037
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.9211
    std: 0.0099
    paper_value: 0.9211
    paper_std: 0.0099
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.9211
    true_std: 0.0099
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9211
    sort_std: 0.0099
    is_best: true
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.9205
    std: 0.0026
    paper_value: 0.9205
    paper_std: 0.0026
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.9205
    true_std: 0.0026
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9205
    sort_std: 0.0026
    is_best: false
  - model: GTN
    model_key: gtn
    model_plain: GTN
    value: 0.9194
    std: 0.0039
    paper_value: 0.9194
    paper_std: 0.0039
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.9194
    true_std: 0.0039
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9194
    sort_std: 0.0039
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.9163
    std: 0.0124
    paper_value: 0.9163
    paper_std: 0.0124
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.9163
    true_std: 0.0124
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9163
    sort_std: 0.0124
    is_best: true
  - model: HAN
    model_key: han
    model_plain: HAN
    value: 0.9147
    std: 0.0022
    paper_value: 0.9147
    paper_std: 0.0022
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.9147
    true_std: 0.0022
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9147
    sort_std: 0.0022
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9146
    std: 0.0062
    paper_value: 0.9146
    paper_std: 0.0062
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.9146
    true_std: 0.0062
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9146
    sort_std: 0.0062
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.906
    std: 0.0095
    paper_value: 0.906
    paper_std: 0.0095
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 10
    true_value: 0.906
    true_std: 0.0095
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.906
    sort_std: 0.0095
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.905
    std: 0.0129
    paper_value: 0.905
    paper_std: 0.0129
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 11
    true_value: 0.905
    true_std: 0.0129
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.905
    sort_std: 0.0129
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9018
    std: 0.0061
    paper_value: 0.9018
    paper_std: 0.0061
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.9018
    true_std: 0.0061
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9018
    sort_std: 0.0061
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.8788
    std: 0.0261
    paper_value: 0.8788
    paper_std: 0.0261
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 13
    true_value: 0.8788
    true_std: 0.0261
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8788
    sort_std: 0.0261
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.8338
    std: 0.0451
    paper_value: 0.8338
    paper_std: 0.0451
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.8338
    true_std: 0.0451
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8338
    sort_std: 0.0451
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id006
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
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.3409
    std: 0.0109
    paper_value: 0.3409
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.3992
    true_std: 0.0067
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05830000000000002
    value_note: ''
    paper_rank: 57
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.3992
    sort_std: 0.0067
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.3549
    std: 0.0104
    paper_value: 0.3549
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 23
    true_value: 0.3736
    true_std: 0.0071
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018699999999999994
    value_note: ''
    paper_rank: 41
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.3736
    sort_std: 0.0071
    is_best: false
  - model: SLAPS
    model_key: slaps
    model_plain: SLAPS
    value: 0.3716
    std: 0.0091
    paper_value: 0.3716
    paper_std: 0.0091
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 26
    true_value: 0.3716
    true_std: 0.0091
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3716
    sort_std: 0.0091
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.2551
    std: 0.0177
    paper_value: 0.2551
    paper_std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 28
    true_value: 0.369
    true_std: 0.01
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1139
    value_note: ''
    paper_rank: 88
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.369
    sort_std: 0.01
    is_best: false
  - model: HES-GSL
    model_key: hes-gsl
    model_plain: HES-GSL
    value: 0.3673
    std: 0.0076
    paper_value: 0.3673
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 30
    true_value: 0.3673
    true_std: 0.0076
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3673
    sort_std: 0.0076
    is_best: false
  - model: GPRGNN_knn
    model_key: gprgnn_knn
    model_plain: GPRGNN_knn
    value: 0.3471
    std: 0.0151
    paper_value: 0.3471
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.3471
    true_std: 0.0151
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.0151
    is_best: false
  - model: CoGSL_knn
    model_key: cogsl_knn
    model_plain: CoGSL_knn
    value: 0.3452
    std: 0.0156
    paper_value: 0.3452
    paper_std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 51
    true_value: 0.3452
    true_std: 0.0156
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3452
    sort_std: 0.0156
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.2891
    std: 0.0083
    paper_value: 0.2891
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 59
    true_value: 0.3393
    true_std: 0.0247
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05019999999999997
    value_note: ''
    paper_rank: 81
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.3393
    sort_std: 0.0247
    is_best: false
  - model: GSR_knn
    model_key: gsr_knn
    model_plain: GSR_knn
    value: 0.3373
    std: 0.0112
    paper_value: 0.3373
    paper_std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.3373
    true_std: 0.0112
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3373
    sort_std: 0.0112
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.3357
    std: 0.0068
    paper_value: 0.3357
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 62
    true_value: 0.3357
    true_std: 0.0068
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3357
    sort_std: 0.0068
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3001
    std: 0.0077
    paper_value: 0.3001
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 66
    true_value: 0.3323
    true_std: 0.0116
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.032200000000000006
    value_note: ''
    paper_rank: 80
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.3323
    sort_std: 0.0116
    is_best: false
  - model: IDGL_knn
    model_key: idgl_knn
    model_plain: IDGL_knn
    value: 0.3307
    std: 0.0137
    paper_value: 0.3307
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 67
    true_value: 0.3307
    true_std: 0.0137
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3307
    sort_std: 0.0137
    is_best: false
  - model: CoGSL
    model_key: cogsl
    model_plain: CoGSL
    value: 0.3295
    std: 0.012
    paper_value: 0.3295
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 68
    true_value: 0.3295
    true_std: 0.012
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3295
    sort_std: 0.012
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.3167
    std: 0.0119
    paper_value: 0.3167
    paper_std: 0.0119
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 70
    true_value: 0.3167
    true_std: 0.0119
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3167
    sort_std: 0.0119
    is_best: false
  - model: ProGNN_knn
    model_key: prognn_knn
    model_plain: ProGNN_knn
    value: 0.3156
    std: 0.0114
    paper_value: 0.3156
    paper_std: 0.0114
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 74
    true_value: 0.3156
    true_std: 0.0114
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3156
    sort_std: 0.0114
    is_best: false
  - model: GEN_knn
    model_key: gen_knn
    model_plain: GEN_knn
    value: 0.3128
    std: 0.0106
    paper_value: 0.3128
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 75
    true_value: 0.3128
    true_std: 0.0106
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3128
    sort_std: 0.0106
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.3105
    std: 0.0131
    paper_value: 0.3105
    paper_std: 0.0131
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 76
    true_value: 0.3105
    true_std: 0.0131
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3105
    sort_std: 0.0131
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 0.3083
    std: 0.0076
    paper_value: 0.3083
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 77
    true_value: 0.3083
    true_std: 0.0076
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3083
    sort_std: 0.0076
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.3023
    std: 0.0038
    paper_value: 0.3023
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 79
    true_value: 0.3023
    true_std: 0.0038
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3023
    sort_std: 0.0038
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.3018
    std: 0.01
    paper_value: 0.3018
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 80
    true_value: 0.3018
    true_std: 0.01
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3018
    sort_std: 0.01
    is_best: false
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.2997
    std: 0.0071
    paper_value: 0.2997
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 81
    true_value: 0.2997
    true_std: 0.0071
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2997
    sort_std: 0.0071
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.2816
    std: 0.0141
    paper_value: 0.2816
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 83
    true_value: 0.2816
    true_std: 0.0141
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2816
    sort_std: 0.0141
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.2721
    std: 0.0205
    paper_value: 0.2721
    paper_std: 0.0205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 86
    true_value: 0.2721
    true_std: 0.0205
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2721
    sort_std: 0.0205
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.2235
    std: 0.0088
    paper_value: 0.2235
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 89
    true_value: 0.2235
    true_std: 0.0088
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2235
    sort_std: 0.0088
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8722
    std: 0.0013
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
    global_rank: 1
    sort_value: 0.8722
    sort_std: 0.0013
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7696
    std: 0.0228
    paper_value: 0.7696
    paper_std: 0.0228
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.827
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05740000000000001
    value_note: ''
    paper_rank: 31
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7908
    std: 0.0136
    paper_value: 0.7908
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.821
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.030200000000000005
    value_note: ''
    paper_rank: 15
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.821
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7986
    std: 0.0164
    paper_value: 0.7986
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.8059
    true_std: 0.0027
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007299999999999973
    value_note: global 0.8059 within std
    paper_rank: 15
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.8059
    sort_std: 0.0027
    is_best: false
  - model: HGP-SL (GCN)
    model_key: hgp-sl (gcn)
    model_plain: HGP-SL (GCN)
    value: 0.8014
    std: 0.0151
    paper_value: 0.8014
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 15
    true_value: 0.8014
    true_std: 0.0151
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8014
    sort_std: 0.0151
    is_best: false
  - model: HGP-SL (SAGE)
    model_key: hgp-sl (sage)
    model_plain: HGP-SL (SAGE)
    value: 0.7864
    std: 0.0147
    paper_value: 0.7864
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.7864
    true_std: 0.0147
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7864
    sort_std: 0.0147
    is_best: false
  - model: VIB-GSL (SAGE)
    model_key: vib-gsl (sage)
    model_plain: VIB-GSL (SAGE)
    value: 0.7774
    std: 0.0152
    paper_value: 0.7774
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 23
    true_value: 0.7774
    true_std: 0.0152
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7774
    sort_std: 0.0152
    is_best: false
  - model: VIB-GSL (GAT)
    model_key: vib-gsl (gat)
    model_plain: VIB-GSL (GAT)
    value: 0.7754
    std: 0.0185
    paper_value: 0.7754
    paper_std: 0.0185
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 25
    true_value: 0.7754
    true_std: 0.0185
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7754
    sort_std: 0.0185
    is_best: false
  - model: VIB-GSL (GCN)
    model_key: vib-gsl (gcn)
    model_plain: VIB-GSL (GCN)
    value: 0.7725
    std: 0.0234
    paper_value: 0.7725
    paper_std: 0.0234
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 30
    true_value: 0.7725
    true_std: 0.0234
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7725
    sort_std: 0.0234
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.7558
    std: 0.0204
    paper_value: 0.7558
    paper_std: 0.0204
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 33
    true_value: 0.7558
    true_std: 0.0204
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7558
    sort_std: 0.0204
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
    value: 0.7136
    std: 0.0031
    paper_value: 0.7136
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10029999999999994
    value_note: ''
    paper_rank: 125
    rank_delta: 113
    rank_delta_abs: 113
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7069
    std: 0.0058
    paper_value: 0.7069
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09830000000000005
    value_note: ''
    paper_rank: 131
    rank_delta: 112
    rank_delta_abs: 112
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7164
    std: 0.0049
    paper_value: 0.7164
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 25
    true_value: 0.8012
    true_std: 0.0083
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08479999999999999
    value_note: ''
    paper_rank: 124
    rank_delta: 99
    rank_delta_abs: 99
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0083
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7131
    std: 0.0098
    paper_value: 0.7131
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 30
    true_value: 0.7956
    true_std: 0.011
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08250000000000002
    value_note: ''
    paper_rank: 125
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.7956
    sort_std: 0.011
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.5952
    std: 0.0064
    paper_value: 0.5952
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 31
    true_value: 0.7939
    true_std: 0.0138
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1987000000000001
    value_note: ''
    paper_rank: 203
    rank_delta: 172
    rank_delta_abs: 172
    rank_delta_direction: worse
    sort_value: 0.7939
    sort_std: 0.0138
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.7355
    std: 0.0054
    paper_value: 0.7355
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 105
    true_value: 0.7355
    true_std: 0.0054
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7355
    sort_std: 0.0054
    is_best: false
  - model: CoGSL
    model_key: cogsl
    model_plain: CoGSL
    value: 0.7309
    std: 0.0042
    paper_value: 0.7309
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 111
    true_value: 0.7309
    true_std: 0.0042
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7309
    sort_std: 0.0042
    is_best: false
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.7243
    std: 0.0061
    paper_value: 0.7243
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 117
    true_value: 0.7243
    true_std: 0.0061
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7243
    sort_std: 0.0061
    is_best: false
  - model: LDS_knn
    model_key: lds_knn
    model_plain: LDS_knn
    value: 0.7243
    std: 0.0061
    paper_value: 0.7243
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 118
    true_value: 0.7243
    true_std: 0.0061
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7243
    sort_std: 0.0061
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.723
    std: 0.0109
    paper_value: 0.723
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 120
    true_value: 0.723
    true_std: 0.0109
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.0109
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.722
    std: 0.0118
    paper_value: 0.722
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 121
    true_value: 0.722
    true_std: 0.0118
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.722
    sort_std: 0.0118
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.7115
    std: 0.0181
    paper_value: 0.7115
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 127
    true_value: 0.7115
    true_std: 0.0181
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7115
    sort_std: 0.0181
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.711
    std: 0.0025
    paper_value: 0.711
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 128
    true_value: 0.711
    true_std: 0.0025
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.711
    sort_std: 0.0025
    is_best: false
  - model: SLAPS
    model_key: slaps
    model_plain: SLAPS
    value: 0.7071
    std: 0.0113
    paper_value: 0.7071
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 131
    true_value: 0.7071
    true_std: 0.0113
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7071
    sort_std: 0.0113
    is_best: false
  - model: GPRGNN_knn
    model_key: gprgnn_knn
    model_plain: GPRGNN_knn
    value: 0.7029
    std: 0.0054
    paper_value: 0.7029
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 136
    true_value: 0.7029
    true_std: 0.0054
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7029
    sort_std: 0.0054
    is_best: false
  - model: HES-GSL
    model_key: hes-gsl
    model_plain: HES-GSL
    value: 0.7012
    std: 0.0111
    paper_value: 0.7012
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 138
    true_value: 0.7012
    true_std: 0.0111
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7012
    sort_std: 0.0111
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.6891
    std: 0.0101
    paper_value: 0.6891
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 141
    true_value: 0.6891
    true_std: 0.0101
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6891
    sort_std: 0.0101
    is_best: false
  - model: CoGSL_knn
    model_key: cogsl_knn
    model_plain: CoGSL_knn
    value: 0.6872
    std: 0.0084
    paper_value: 0.6872
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 142
    true_value: 0.6872
    true_std: 0.0084
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6872
    sort_std: 0.0084
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.6851
    std: 0.0052
    paper_value: 0.6851
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 143
    true_value: 0.6851
    true_std: 0.0052
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6851
    sort_std: 0.0052
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 0.6841
    std: 0.005
    paper_value: 0.6841
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 146
    true_value: 0.6841
    true_std: 0.005
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6841
    sort_std: 0.005
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.6805
    std: 0.0112
    paper_value: 0.6805
    paper_std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 150
    true_value: 0.6805
    true_std: 0.0112
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6805
    sort_std: 0.0112
    is_best: false
  - model: GEN_knn
    model_key: gen_knn
    model_plain: GEN_knn
    value: 0.6729
    std: 0.0117
    paper_value: 0.6729
    paper_std: 0.0117
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 151
    true_value: 0.6729
    true_std: 0.0117
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6729
    sort_std: 0.0117
    is_best: false
  - model: GSR_knn
    model_key: gsr_knn
    model_plain: GSR_knn
    value: 0.6677
    std: 0.0062
    paper_value: 0.6677
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 155
    true_value: 0.6677
    true_std: 0.0062
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6677
    sort_std: 0.0062
    is_best: false
  - model: IDGL_knn
    model_key: idgl_knn
    model_plain: IDGL_knn
    value: 0.6633
    std: 0.0084
    paper_value: 0.6633
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 158
    true_value: 0.6633
    true_std: 0.0084
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6633
    sort_std: 0.0084
    is_best: false
  - model: ProGNN_knn
    model_key: prognn_knn
    model_plain: ProGNN_knn
    value: 0.6455
    std: 0.0095
    paper_value: 0.6455
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 172
    true_value: 0.6455
    true_std: 0.0095
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6455
    sort_std: 0.0095
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
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8028
    std: 0.0082
    paper_value: 0.8028
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 20
    true_value: 0.887
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08420000000000005
    value_note: ''
    paper_rank: 152
    rank_delta: 132
    rank_delta_abs: 132
    rank_delta_direction: worse
    sort_value: 0.887
    sort_std: 0.002
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8366
    std: 0.0077
    paper_value: 0.8366
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 25
    true_value: 0.8857
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04910000000000003
    value_note: ''
    paper_rank: 116
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.8857
    sort_std: 0.0069
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8141
    std: 0.0077
    paper_value: 0.8141
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0683999999999999
    value_note: ''
    paper_rank: 148
    rank_delta: 117
    rank_delta_abs: 117
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8146
    std: 0.0058
    paper_value: 0.8146
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06320000000000003
    value_note: ''
    paper_rank: 147
    rank_delta: 99
    rank_delta_abs: 99
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.5855
    std: 0.008
    paper_value: 0.5855
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 65
    true_value: 0.8709
    true_std: 0.0066
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2854
    value_note: ''
    paper_rank: 287
    rank_delta: 222
    rank_delta_abs: 222
    rank_delta_direction: worse
    sort_value: 0.8709
    sort_std: 0.0066
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.8388
    std: 0.0042
    paper_value: 0.8388
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 113
    true_value: 0.8388
    true_std: 0.0042
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8388
    sort_std: 0.0042
    is_best: false
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.8387
    std: 0.0049
    paper_value: 0.8387
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 115
    true_value: 0.8387
    true_std: 0.0049
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8387
    sort_std: 0.0049
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.834
    std: 0.0042
    paper_value: 0.834
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 122
    true_value: 0.834
    true_std: 0.0042
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.834
    sort_std: 0.0042
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.8301
    std: 0.0041
    paper_value: 0.8301
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 129
    true_value: 0.8301
    true_std: 0.0041
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8301
    sort_std: 0.0041
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.8248
    std: 0.0043
    paper_value: 0.8248
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 138
    true_value: 0.8248
    true_std: 0.0043
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8248
    sort_std: 0.0043
    is_best: false
  - model: CoGSL
    model_key: cogsl
    model_plain: CoGSL
    value: 0.8176
    std: 0.0024
    paper_value: 0.8176
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 145
    true_value: 0.8176
    true_std: 0.0024
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8176
    sort_std: 0.0024
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.803
    std: 0.0057
    paper_value: 0.803
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 152
    true_value: 0.803
    true_std: 0.0057
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.803
    sort_std: 0.0057
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.8021
    std: 0.0172
    paper_value: 0.8021
    paper_std: 0.0172
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 153
    true_value: 0.8021
    true_std: 0.0172
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8021
    sort_std: 0.0172
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.802
    std: 0.0068
    paper_value: 0.802
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 154
    true_value: 0.802
    true_std: 0.0068
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.802
    sort_std: 0.0068
    is_best: false
  - model: HES-GSL
    model_key: hes-gsl
    model_plain: HES-GSL
    value: 0.7368
    std: 0.0104
    paper_value: 0.7368
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 210
    true_value: 0.7368
    true_std: 0.0104
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 210
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7368
    sort_std: 0.0104
    is_best: false
  - model: SLAPS
    model_key: slaps
    model_plain: SLAPS
    value: 0.7228
    std: 0.0097
    paper_value: 0.7228
    paper_std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 227
    true_value: 0.7228
    true_std: 0.0097
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 227
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7228
    sort_std: 0.0097
    is_best: false
  - model: IDGL_knn
    model_key: idgl_knn
    model_plain: IDGL_knn
    value: 0.6974
    std: 0.0057
    paper_value: 0.6974
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 245
    true_value: 0.6974
    true_std: 0.0057
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 245
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6974
    sort_std: 0.0057
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 0.6948
    std: 0.0066
    paper_value: 0.6948
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 248
    true_value: 0.6948
    true_std: 0.0066
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 248
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6948
    sort_std: 0.0066
    is_best: false
  - model: GPRGNN_knn
    model_key: gprgnn_knn
    model_plain: GPRGNN_knn
    value: 0.6927
    std: 0.0062
    paper_value: 0.6927
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 250
    true_value: 0.6927
    true_std: 0.0062
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 250
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6927
    sort_std: 0.0062
    is_best: false
  - model: ProGNN_knn
    model_key: prognn_knn
    model_plain: ProGNN_knn
    value: 0.6711
    std: 0.0056
    paper_value: 0.6711
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 264
    true_value: 0.6711
    true_std: 0.0056
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 264
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6711
    sort_std: 0.0056
    is_best: false
  - model: GEN_knn
    model_key: gen_knn
    model_plain: GEN_knn
    value: 0.6695
    std: 0.014
    paper_value: 0.6695
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 265
    true_value: 0.6695
    true_std: 0.014
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 265
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6695
    sort_std: 0.014
    is_best: false
  - model: CoGSL_knn
    model_key: cogsl_knn
    model_plain: CoGSL_knn
    value: 0.6665
    std: 0.0037
    paper_value: 0.6665
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 269
    true_value: 0.6665
    true_std: 0.0037
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 269
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6665
    sort_std: 0.0037
    is_best: false
  - model: GSR_knn
    model_key: gsr_knn
    model_plain: GSR_knn
    value: 0.6628
    std: 0.0059
    paper_value: 0.6628
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 270
    true_value: 0.6628
    true_std: 0.0059
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 270
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6628
    sort_std: 0.0059
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.6462
    std: 0.0104
    paper_value: 0.6462
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 274
    true_value: 0.6462
    true_std: 0.0104
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 274
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6462
    sort_std: 0.0104
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
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
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7676
    std: 0.053
    paper_value: 0.7676
    paper_std: 0.053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 10
    true_value: 0.9136
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14600000000000002
    value_note: ''
    paper_rank: 33
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.9136
    sort_std: 0.007
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7135
    std: 0.0619
    paper_value: 0.7135
    paper_std: 0.0619
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 11
    true_value: 0.913
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1995
    value_note: ''
    paper_rank: 54
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4784
    std: 0.0555
    paper_value: 0.4784
    paper_std: 0.0555
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3462
    value_note: ''
    paper_rank: 130
    rank_delta: 103
    rank_delta_abs: 103
    rank_delta_direction: worse
    sort_value: 0.8246
    sort_std: 0.0311
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4622
    std: 0.0633
    paper_value: 0.4622
    paper_std: 0.0633
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 37
    true_value: 0.76
    true_std: 0.0101
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2978
    value_note: ''
    paper_rank: 135
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.0101
    is_best: false
  - model: GPRGNN_knn
    model_key: gprgnn_knn
    model_plain: GPRGNN_knn
    value: 0.7568
    std: 0.027
    paper_value: 0.7568
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 38
    true_value: 0.7568
    true_std: 0.027
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7568
    sort_std: 0.027
    is_best: false
  - model: SLAPS
    model_key: slaps
    model_plain: SLAPS
    value: 0.7459
    std: 0.0367
    paper_value: 0.7459
    paper_std: 0.0367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 41
    true_value: 0.7459
    true_std: 0.0367
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7459
    sort_std: 0.0367
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.7405
    std: 0.0516
    paper_value: 0.7405
    paper_std: 0.0516
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 44
    true_value: 0.7405
    true_std: 0.0516
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7405
    sort_std: 0.0516
    is_best: false
  - model: IDGL_knn
    model_key: idgl_knn
    model_plain: IDGL_knn
    value: 0.727
    std: 0.0475
    paper_value: 0.727
    paper_std: 0.0475
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.727
    true_std: 0.0475
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.0475
    is_best: false
  - model: ProGNN_knn
    model_key: prognn_knn
    model_plain: ProGNN_knn
    value: 0.7135
    std: 0.0404
    paper_value: 0.7135
    paper_std: 0.0404
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 55
    true_value: 0.7135
    true_std: 0.0404
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7135
    sort_std: 0.0404
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 0.7108
    std: 0.0684
    paper_value: 0.7108
    paper_std: 0.0684
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 58
    true_value: 0.7108
    true_std: 0.0684
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7108
    sort_std: 0.0684
    is_best: false
  - model: GEN_knn
    model_key: gen_knn
    model_plain: GEN_knn
    value: 0.7108
    std: 0.0554
    paper_value: 0.7108
    paper_std: 0.0554
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 59
    true_value: 0.7108
    true_std: 0.0554
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7108
    sort_std: 0.0554
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.7054
    std: 0.0598
    paper_value: 0.7054
    paper_std: 0.0598
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 63
    true_value: 0.7054
    true_std: 0.0598
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7054
    sort_std: 0.0598
    is_best: false
  - model: CoGSL_knn
    model_key: cogsl_knn
    model_plain: CoGSL_knn
    value: 0.7027
    std: 0.0342
    paper_value: 0.7027
    paper_std: 0.0342
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 65
    true_value: 0.7027
    true_std: 0.0342
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7027
    sort_std: 0.0342
    is_best: false
  - model: GSR_knn
    model_key: gsr_knn
    model_plain: GSR_knn
    value: 0.7027
    std: 0.0362
    paper_value: 0.7027
    paper_std: 0.0362
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 66
    true_value: 0.7027
    true_std: 0.0362
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7027
    sort_std: 0.0362
    is_best: false
  - model: HES-GSL
    model_key: hes-gsl
    model_plain: HES-GSL
    value: 0.6622
    std: 0.0619
    paper_value: 0.6622
    paper_std: 0.0619
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 83
    true_value: 0.6622
    true_std: 0.0619
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6622
    sort_std: 0.0619
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.427
    std: 0.0551
    paper_value: 0.427
    paper_std: 0.0551
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 87
    true_value: 0.6577
    true_std: 0.0459
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23069999999999996
    value_note: ''
    paper_rank: 144
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.6577
    sort_std: 0.0459
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.5702
    std: 0.0719
    paper_value: 0.5702
    paper_std: 0.0719
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 112
    true_value: 0.5702
    true_std: 0.0719
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5702
    sort_std: 0.0719
    is_best: false
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.5432
    std: 0.0824
    paper_value: 0.5432
    paper_std: 0.0824
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 114
    true_value: 0.5432
    true_std: 0.0824
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5432
    sort_std: 0.0824
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.5405
    std: 0.0616
    paper_value: 0.5405
    paper_std: 0.0616
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 117
    true_value: 0.5405
    true_std: 0.0616
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5405
    sort_std: 0.0616
    is_best: false
  - model: CoGSL
    model_key: cogsl
    model_plain: CoGSL
    value: 0.5216
    std: 0.0321
    paper_value: 0.5216
    paper_std: 0.0321
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 123
    true_value: 0.5216
    true_std: 0.0321
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5216
    sort_std: 0.0321
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.5
    std: 0.0898
    paper_value: 0.5
    paper_std: 0.0898
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 128
    true_value: 0.5
    true_std: 0.0898
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5
    sort_std: 0.0898
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.4787
    std: 0.0714
    paper_value: 0.4787
    paper_std: 0.0714
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 130
    true_value: 0.4787
    true_std: 0.0714
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4787
    sort_std: 0.0714
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.4432
    std: 0.0216
    paper_value: 0.4432
    paper_std: 0.0216
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 141
    true_value: 0.4432
    true_std: 0.0216
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4432
    sort_std: 0.0216
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.4403
    std: 0.0405
    paper_value: 0.4403
    paper_std: 0.0405
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 142
    true_value: 0.4403
    true_std: 0.0405
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4403
    sort_std: 0.0405
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: DBLP
  rows:
  - model: HGSL
    model_key: hgsl
    model_plain: HGSL
    value: 0.9249
    std: 0.0035
    paper_value: 0.9249
    paper_std: 0.0035
    metric: Micro-F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 1
    true_value: 0.9249
    true_std: 0.0035
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9249
    sort_std: 0.0035
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.9182
    std: 0.0027
    paper_value: 0.9182
    paper_std: 0.0027
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 2
    true_value: 0.9182
    true_std: 0.0027
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9182
    sort_std: 0.0027
    is_best: false
  - model: GTN
    model_key: gtn
    model_plain: GTN
    value: 0.9148
    std: 0.0039
    paper_value: 0.9148
    paper_std: 0.0039
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.9148
    true_std: 0.0039
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9148
    sort_std: 0.0039
    is_best: false
  - model: HAN
    model_key: han
    model_plain: HAN
    value: 0.9147
    std: 0.0022
    paper_value: 0.9147
    paper_std: 0.0022
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.9147
    true_std: 0.0022
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9147
    sort_std: 0.0022
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9113
    std: 0.004
    paper_value: 0.9113
    paper_std: 0.004
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.9113
    true_std: 0.004
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9113
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9099
    std: 0.0028
    paper_value: 0.9099
    paper_std: 0.0028
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.9099
    true_std: 0.0028
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9099
    sort_std: 0.0028
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.9065
    std: 0.0071
    paper_value: 0.9065
    paper_std: 0.0071
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.9065
    true_std: 0.0071
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9065
    sort_std: 0.0071
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.9061
    std: 0.0056
    paper_value: 0.9061
    paper_std: 0.0056
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.9061
    true_std: 0.0056
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9061
    sort_std: 0.0056
    is_best: false
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.8943
    std: 0.0044
    paper_value: 0.8943
    paper_std: 0.0044
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.8943
    true_std: 0.0044
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8943
    sort_std: 0.0044
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.8874
    std: 0.0085
    paper_value: 0.8874
    paper_std: 0.0085
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 10
    true_value: 0.8874
    true_std: 0.0085
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8874
    sort_std: 0.0085
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.8483
    std: 0.0136
    paper_value: 0.8483
    paper_std: 0.0136
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 11
    true_value: 0.8483
    true_std: 0.0136
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8483
    sort_std: 0.0136
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8056
    std: 0.0062
    paper_value: 0.8056
    paper_std: 0.0062
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.8056
    true_std: 0.0062
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8056
    sort_std: 0.0062
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.7769
    std: 0.0042
    paper_value: 0.7769
    paper_std: 0.0042
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 13
    true_value: 0.7769
    true_std: 0.0042
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7769
    sort_std: 0.0042
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.7642
    std: 0.0195
    paper_value: 0.7642
    paper_std: 0.0195
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.7642
    true_std: 0.0195
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7642
    sort_std: 0.0195
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id011
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.732
    std: 0.0429
    paper_value: 0.732
    paper_std: 0.0429
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.769
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03700000000000003
    value_note: global 0.7690 within std
    paper_rank: 44
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.73
    std: 0.0267
    paper_value: 0.73
    paper_std: 0.0267
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02100000000000002
    value_note: global 0.7510 within std
    paper_rank: 48
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: HGP-SL (GCN)
    model_key: hgp-sl (gcn)
    model_plain: HGP-SL (GCN)
    value: 0.735
    std: 0.0625
    paper_value: 0.735
    paper_std: 0.0625
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 42
    true_value: 0.735
    true_std: 0.0625
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.0625
    is_best: false
  - model: VIB-GSL (SAGE)
    model_key: vib-gsl (sage)
    model_plain: VIB-GSL (SAGE)
    value: 0.73
    std: 0.0478
    paper_value: 0.73
    paper_std: 0.0478
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 51
    true_value: 0.73
    true_std: 0.0478
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.0478
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.726
    std: 0.0369
    paper_value: 0.726
    paper_std: 0.0369
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 55
    true_value: 0.726
    true_std: 0.0369
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.0369
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.723
    std: 0.0226
    paper_value: 0.723
    paper_std: 0.0226
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.723
    true_std: 0.0226
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.0226
    is_best: false
  - model: VIB-GSL (GAT)
    model_key: vib-gsl (gat)
    model_plain: VIB-GSL (GAT)
    value: 0.721
    std: 0.0569
    paper_value: 0.721
    paper_std: 0.0569
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.721
    true_std: 0.0569
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.0569
    is_best: false
  - model: HGP-SL (SAGE)
    model_key: hgp-sl (sage)
    model_plain: HGP-SL (SAGE)
    value: 0.715
    std: 0.0524
    paper_value: 0.715
    paper_std: 0.0524
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 77
    true_value: 0.715
    true_std: 0.0524
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0524
    is_best: false
  - model: VIB-GSL (GCN)
    model_key: vib-gsl (gcn)
    model_plain: VIB-GSL (GCN)
    value: 0.699
    std: 0.039
    paper_value: 0.699
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 103
    true_value: 0.699
    true_std: 0.039
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.699
    sort_std: 0.039
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4985
    std: 0.0384
    paper_value: 0.4985
    paper_std: 0.0384
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 21
    true_value: 0.523
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.024500000000000022
    value_note: global 0.5230 within std
    paper_rank: 43
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.503
    std: 0.0352
    paper_value: 0.503
    paper_std: 0.0352
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 22
    true_value: 0.523
    true_std: 0.028
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.020000000000000018
    value_note: global 0.5230 within std
    paper_rank: 36
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: 0.028
    is_best: false
  - model: VIB-GSL (GCN)
    model_key: vib-gsl (gcn)
    model_plain: VIB-GSL (GCN)
    value: 0.4997
    std: 0.0365
    paper_value: 0.4997
    paper_std: 0.0365
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 41
    true_value: 0.4997
    true_std: 0.0365
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4997
    sort_std: 0.0365
    is_best: false
  - model: HGP-SL (SAGE)
    model_key: hgp-sl (sage)
    model_plain: HGP-SL (SAGE)
    value: 0.4967
    std: 0.0309
    paper_value: 0.4967
    paper_std: 0.0309
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 45
    true_value: 0.4967
    true_std: 0.0309
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4967
    sort_std: 0.0309
    is_best: false
  - model: VIB-GSL (GAT)
    model_key: vib-gsl (gat)
    model_plain: VIB-GSL (GAT)
    value: 0.4906
    std: 0.0455
    paper_value: 0.4906
    paper_std: 0.0455
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 50
    true_value: 0.4906
    true_std: 0.0455
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4906
    sort_std: 0.0455
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.489
    std: 0.0298
    paper_value: 0.489
    paper_std: 0.0298
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 54
    true_value: 0.489
    true_std: 0.0298
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.489
    sort_std: 0.0298
    is_best: false
  - model: VIB-GSL (SAGE)
    model_key: vib-gsl (sage)
    model_plain: VIB-GSL (SAGE)
    value: 0.4879
    std: 0.0506
    paper_value: 0.4879
    paper_std: 0.0506
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 55
    true_value: 0.4879
    true_std: 0.0506
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4879
    sort_std: 0.0506
    is_best: false
  - model: HGP-SL (GCN)
    model_key: hgp-sl (gcn)
    model_plain: HGP-SL (GCN)
    value: 0.4867
    std: 0.0258
    paper_value: 0.4867
    paper_std: 0.0258
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 57
    true_value: 0.4867
    true_std: 0.0258
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4867
    sort_std: 0.0258
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.4855
    std: 0.0203
    paper_value: 0.4855
    paper_std: 0.0203
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 60
    true_value: 0.4855
    true_std: 0.0203
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4855
    sort_std: 0.0203
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7392
    std: 0.0884
    paper_value: 0.7392
    paper_std: 0.0884
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 22
    true_value: 0.901
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16180000000000005
    value_note: ''
    paper_rank: 141
    rank_delta: 119
    rank_delta_abs: 119
    rank_delta_direction: worse
    sort_value: 0.901
    sort_std: null
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8719
    std: 0.0805
    paper_value: 0.8719
    paper_std: 0.0805
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02210000000000001
    value_note: global 0.8940 within std
    paper_rank: 47
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: VIB-GSL (GCN)
    model_key: vib-gsl (gcn)
    model_plain: VIB-GSL (GCN)
    value: 0.8518
    std: 0.1011
    paper_value: 0.8518
    paper_std: 0.1011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.8518
    true_std: 0.1011
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8518
    sort_std: 0.1011
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7871
    std: 0.0751
    paper_value: 0.7871
    paper_std: 0.0751
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 117
    true_value: 0.7871
    true_std: 0.0751
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7871
    sort_std: 0.0751
    is_best: false
  - model: VIB-GSL (GAT)
    model_key: vib-gsl (gat)
    model_plain: VIB-GSL (GAT)
    value: 0.7713
    std: 0.0995
    paper_value: 0.7713
    paper_std: 0.0995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 124
    true_value: 0.7713
    true_std: 0.0995
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7713
    sort_std: 0.0995
    is_best: false
  - model: HGP-SL (SAGE)
    model_key: hgp-sl (sage)
    model_plain: HGP-SL (SAGE)
    value: 0.7713
    std: 0.0329
    paper_value: 0.7713
    paper_std: 0.0329
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 125
    true_value: 0.7713
    true_std: 0.0329
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7713
    sort_std: 0.0329
    is_best: false
  - model: HGP-SL (GCN)
    model_key: hgp-sl (gcn)
    model_plain: HGP-SL (GCN)
    value: 0.7392
    std: 0.0624
    paper_value: 0.7392
    paper_std: 0.0624
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 142
    true_value: 0.7392
    true_std: 0.0624
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7392
    sort_std: 0.0624
    is_best: false
  - model: VIB-GSL (SAGE)
    model_key: vib-gsl (sage)
    model_plain: VIB-GSL (SAGE)
    value: 0.7281
    std: 0.1141
    paper_value: 0.7281
    paper_std: 0.1141
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 148
    true_value: 0.7281
    true_std: 0.1141
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7281
    sort_std: 0.1141
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6865
    std: 0.0431
    paper_value: 0.6865
    paper_std: 0.0431
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 163
    true_value: 0.6865
    true_std: 0.0431
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6865
    sort_std: 0.0431
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
    value: 0.6863
    std: 0.0624
    paper_value: 0.6863
    paper_std: 0.0624
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 28
    true_value: 0.7634
    true_std: 0.0166
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07709999999999995
    value_note: ''
    paper_rank: 187
    rank_delta: 159
    rank_delta_abs: 159
    rank_delta_direction: worse
    sort_value: 0.7634
    sort_std: 0.0166
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6907
    std: 0.0562
    paper_value: 0.6907
    paper_std: 0.0562
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07130000000000003
    value_note: ''
    paper_rank: 185
    rank_delta: 153
    rank_delta_abs: 153
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6752
    std: 0.0671
    paper_value: 0.6752
    paper_std: 0.0671
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 38
    true_value: 0.76
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08479999999999999
    value_note: ''
    paper_rank: 189
    rank_delta: 151
    rank_delta_abs: 151
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.032
    is_best: false
  - model: VIB-GSL (GCN)
    model_key: vib-gsl (gcn)
    model_plain: VIB-GSL (GCN)
    value: 0.7515
    std: 0.0572
    paper_value: 0.7515
    paper_std: 0.0572
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 60
    true_value: 0.7515
    true_std: 0.0572
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7515
    sort_std: 0.0572
    is_best: false
  - model: HGP-SL (SAGE)
    model_key: hgp-sl (sage)
    model_plain: HGP-SL (SAGE)
    value: 0.7332
    std: 0.0206
    paper_value: 0.7332
    paper_std: 0.0206
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 109
    true_value: 0.7332
    true_std: 0.0206
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7332
    sort_std: 0.0206
    is_best: false
  - model: HGP-SL (GCN)
    model_key: hgp-sl (gcn)
    model_plain: HGP-SL (GCN)
    value: 0.6937
    std: 0.0395
    paper_value: 0.6937
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 185
    true_value: 0.6937
    true_std: 0.0395
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 185
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6937
    sort_std: 0.0395
    is_best: false
  - model: VIB-GSL (GAT)
    model_key: vib-gsl (gat)
    model_plain: VIB-GSL (GAT)
    value: 0.6709
    std: 0.0843
    paper_value: 0.6709
    paper_std: 0.0843
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 190
    true_value: 0.6709
    true_std: 0.0843
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6709
    sort_std: 0.0843
    is_best: false
  - model: VIB-GSL (SAGE)
    model_key: vib-gsl (sage)
    model_plain: VIB-GSL (SAGE)
    value: 0.6661
    std: 0.0448
    paper_value: 0.6661
    paper_std: 0.0448
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 192
    true_value: 0.6661
    true_std: 0.0448
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 192
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6661
    sort_std: 0.0448
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6447
    std: 0.0715
    paper_value: 0.6447
    paper_std: 0.0715
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 195
    true_value: 0.6447
    true_std: 0.0715
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 195
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6447
    sort_std: 0.0715
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
    value: 0.5831
    std: 0.0028
    paper_value: 0.5831
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14300000000000002
    value_note: ''
    paper_rank: 275
    rank_delta: 266
    rank_delta_abs: 266
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6092
    std: 0.0088
    paper_value: 0.6092
    paper_std: 0.0088
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 41
    true_value: 0.7059
    true_std: 0.0089
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09670000000000001
    value_note: ''
    paper_rank: 238
    rank_delta: 197
    rank_delta_abs: 197
    rank_delta_direction: worse
    sort_value: 0.7059
    sort_std: 0.0089
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4559
    std: 0.0035
    paper_value: 0.4559
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 78
    true_value: 0.6924
    true_std: 0.0044
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2365
    value_note: ''
    paper_rank: 305
    rank_delta: 227
    rank_delta_abs: 227
    rank_delta_direction: worse
    sort_value: 0.6924
    sort_std: 0.0044
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.5941
    std: 0.0057
    paper_value: 0.5941
    paper_std: 0.0057
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 254
    true_value: 0.5971
    true_std: 0.0041
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0030000000000000027
    value_note: global 0.5971 within std
    paper_rank: 260
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.5971
    sort_std: 0.0041
    is_best: false
  - model: HGP-SL (GCN)
    model_key: hgp-sl (gcn)
    model_plain: HGP-SL (GCN)
    value: 0.553
    std: 0.0088
    paper_value: 0.553
    paper_std: 0.0088
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 287
    true_value: 0.553
    true_std: 0.0088
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 287
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.553
    sort_std: 0.0088
    is_best: false
  - model: VIB-GSL (SAGE)
    model_key: vib-gsl (sage)
    model_plain: VIB-GSL (SAGE)
    value: 0.5411
    std: 0.0074
    paper_value: 0.5411
    paper_std: 0.0074
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 291
    true_value: 0.5411
    true_std: 0.0074
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 291
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5411
    sort_std: 0.0074
    is_best: false
  - model: HGP-SL (SAGE)
    model_key: hgp-sl (sage)
    model_plain: HGP-SL (SAGE)
    value: 0.5348
    std: 0.0071
    paper_value: 0.5348
    paper_std: 0.0071
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 293
    true_value: 0.5348
    true_std: 0.0071
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 293
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5348
    sort_std: 0.0071
    is_best: false
  - model: VIB-GSL (GCN)
    model_key: vib-gsl (gcn)
    model_plain: VIB-GSL (GCN)
    value: 0.4761
    std: 0.0093
    paper_value: 0.4761
    paper_std: 0.0093
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 303
    true_value: 0.4761
    true_std: 0.0093
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 303
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4761
    sort_std: 0.0093
    is_best: false
  - model: VIB-GSL (GAT)
    model_key: vib-gsl (gat)
    model_plain: VIB-GSL (GAT)
    value: 0.4264
    std: 0.0033
    paper_value: 0.4264
    paper_std: 0.0033
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 309
    true_value: 0.4264
    true_std: 0.0033
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 309
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4264
    sort_std: 0.0033
    is_best: false
  metric: AP
  higher_is_better: true
- &id008
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
    value: 0.3566
    std: 0.0014
    paper_value: 0.3566
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11449999999999996
    value_note: ''
    paper_rank: 317
    rank_delta: 314
    rank_delta_abs: 314
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
    value: 0.3647
    std: 0.0028
    paper_value: 0.3647
    paper_std: 0.0028
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.2429
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12180000000000002
    value_note: ''
    paper_rank: 322
    rank_delta: 313
    rank_delta_abs: 313
    rank_delta_direction: worse
    sort_value: 0.2429
    sort_std: 0.0019
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4375
    std: 0.0036
    paper_value: 0.4375
    paper_std: 0.0036
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 120
    true_value: 0.2488
    true_std: 0.0018
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1887
    value_note: ''
    paper_rank: 335
    rank_delta: 215
    rank_delta_abs: 215
    rank_delta_direction: worse
    sort_value: 0.2488
    sort_std: 0.0018
    is_best: false
  - model: HGP-SL (GCN)
    model_key: hgp-sl (gcn)
    model_plain: HGP-SL (GCN)
    value: 0.2786
    std: 0.0018
    paper_value: 0.2786
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 257
    true_value: 0.2786
    true_std: 0.0018
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 257
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2786
    sort_std: 0.0018
    is_best: false
  - model: HGP-SL (SAGE)
    model_key: hgp-sl (sage)
    model_plain: HGP-SL (SAGE)
    value: 0.2794
    std: 0.0058
    paper_value: 0.2794
    paper_std: 0.0058
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 258
    true_value: 0.2794
    true_std: 0.0058
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 258
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2794
    sort_std: 0.0058
    is_best: false
  - model: VIB-GSL (GCN)
    model_key: vib-gsl (gcn)
    model_plain: VIB-GSL (GCN)
    value: 0.3032
    std: 0.0011
    paper_value: 0.3032
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 271
    true_value: 0.3032
    true_std: 0.0011
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 271
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3032
    sort_std: 0.0011
    is_best: false
  - model: VIB-GSL (SAGE)
    model_key: vib-gsl (sage)
    model_plain: VIB-GSL (SAGE)
    value: 0.3063
    std: 0.0014
    paper_value: 0.3063
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 275
    true_value: 0.3063
    true_std: 0.0014
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 275
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3063
    sort_std: 0.0014
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.3716
    std: 0.0011
    paper_value: 0.3716
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 304
    true_value: 0.348
    true_std: 0.0007
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02360000000000001
    value_note: ''
    paper_rank: 325
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.348
    sort_std: 0.0007
    is_best: false
  - model: VIB-GSL (GAT)
    model_key: vib-gsl (gat)
    model_plain: VIB-GSL (GAT)
    value: 0.3992
    std: 0.0129
    paper_value: 0.3992
    paper_std: 0.0129
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 331
    true_value: 0.3992
    true_std: 0.0129
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 331
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3992
    sort_std: 0.0129
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
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
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8514
    std: 0.0368
    paper_value: 0.8514
    paper_std: 0.0368
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 11
    true_value: 0.9295
    true_std: 0.0131
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07809999999999995
    value_note: ''
    paper_rank: 35
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.9295
    sort_std: 0.0131
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.8027
    std: 0.0593
    paper_value: 0.8027
    paper_std: 0.0593
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.923
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12030000000000007
    value_note: ''
    paper_rank: 63
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.923
    sort_std: 0.007
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.5892
    std: 0.0432
    paper_value: 0.5892
    paper_std: 0.0432
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 39
    true_value: 0.8463
    true_std: 0.0347
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2571000000000001
    value_note: ''
    paper_rank: 149
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.8463
    sort_std: 0.0347
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5783
    std: 0.0276
    paper_value: 0.5783
    paper_std: 0.0276
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2527999999999999
    value_note: ''
    paper_rank: 150
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GPRGNN_knn
    model_key: gprgnn_knn
    model_plain: GPRGNN_knn
    value: 0.8108
    std: 0.0418
    paper_value: 0.8108
    paper_std: 0.0418
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 60
    true_value: 0.8108
    true_std: 0.0418
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8108
    sort_std: 0.0418
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5405
    std: 0.0735
    paper_value: 0.5405
    paper_std: 0.0735
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.26770000000000005
    value_note: ''
    paper_rank: 161
    rank_delta: 100
    rank_delta_abs: 100
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: SLAPS
    model_key: slaps
    model_plain: SLAPS
    value: 0.7919
    std: 0.0499
    paper_value: 0.7919
    paper_std: 0.0499
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 66
    true_value: 0.7919
    true_std: 0.0499
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7919
    sort_std: 0.0499
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.7703
    std: 0.0423
    paper_value: 0.7703
    paper_std: 0.0423
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 81
    true_value: 0.7703
    true_std: 0.0423
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7703
    sort_std: 0.0423
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.7649
    std: 0.0499
    paper_value: 0.7649
    paper_std: 0.0499
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 86
    true_value: 0.7649
    true_std: 0.0499
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7649
    sort_std: 0.0499
    is_best: false
  - model: IDGL_knn
    model_key: idgl_knn
    model_plain: IDGL_knn
    value: 0.754
    std: 0.0475
    paper_value: 0.754
    paper_std: 0.0475
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 91
    true_value: 0.754
    true_std: 0.0475
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.754
    sort_std: 0.0475
    is_best: false
  - model: GSR_knn
    model_key: gsr_knn
    model_plain: GSR_knn
    value: 0.7486
    std: 0.0363
    paper_value: 0.7486
    paper_std: 0.0363
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 93
    true_value: 0.7486
    true_std: 0.0363
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7486
    sort_std: 0.0363
    is_best: false
  - model: GEN_knn
    model_key: gen_knn
    model_plain: GEN_knn
    value: 0.7459
    std: 0.0346
    paper_value: 0.7459
    paper_std: 0.0346
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 95
    true_value: 0.7459
    true_std: 0.0346
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7459
    sort_std: 0.0346
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 0.7432
    std: 0.0502
    paper_value: 0.7432
    paper_std: 0.0502
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 96
    true_value: 0.7432
    true_std: 0.0502
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7432
    sort_std: 0.0502
    is_best: false
  - model: HES-GSL
    model_key: hes-gsl
    model_plain: HES-GSL
    value: 0.7405
    std: 0.0642
    paper_value: 0.7405
    paper_std: 0.0642
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 97
    true_value: 0.7405
    true_std: 0.0642
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7405
    sort_std: 0.0642
    is_best: false
  - model: CoGSL_knn
    model_key: cogsl_knn
    model_plain: CoGSL_knn
    value: 0.727
    std: 0.0426
    paper_value: 0.727
    paper_std: 0.0426
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 107
    true_value: 0.727
    true_std: 0.0426
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.0426
    is_best: false
  - model: ProGNN_knn
    model_key: prognn_knn
    model_plain: ProGNN_knn
    value: 0.7189
    std: 0.0569
    paper_value: 0.7189
    paper_std: 0.0569
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 110
    true_value: 0.7189
    true_std: 0.0569
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7189
    sort_std: 0.0569
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.6594
    std: 0.0138
    paper_value: 0.6594
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 128
    true_value: 0.6594
    true_std: 0.0138
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6594
    sort_std: 0.0138
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.6243
    std: 0.0609
    paper_value: 0.6243
    paper_std: 0.0609
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 137
    true_value: 0.6243
    true_std: 0.0609
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6243
    sort_std: 0.0609
    is_best: false
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.6216
    std: 0.0705
    paper_value: 0.6216
    paper_std: 0.0705
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 139
    true_value: 0.6216
    true_std: 0.0705
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6216
    sort_std: 0.0705
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.6081
    std: 0.0487
    paper_value: 0.6081
    paper_std: 0.0487
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 145
    true_value: 0.6081
    true_std: 0.0487
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6081
    sort_std: 0.0487
    is_best: false
  - model: CoGSL
    model_key: cogsl
    model_plain: CoGSL
    value: 0.5946
    std: 0.0436
    paper_value: 0.5946
    paper_std: 0.0436
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 149
    true_value: 0.5946
    true_std: 0.0436
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5946
    sort_std: 0.0436
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.5892
    std: 0.0432
    paper_value: 0.5892
    paper_std: 0.0432
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 150
    true_value: 0.5892
    true_std: 0.0432
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5892
    sort_std: 0.0432
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.5524
    std: 0.0604
    paper_value: 0.5524
    paper_std: 0.0604
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 160
    true_value: 0.5524
    true_std: 0.0604
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5524
    sort_std: 0.0604
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.4837
    std: 0.1217
    paper_value: 0.4837
    paper_std: 0.1217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 166
    true_value: 0.4837
    true_std: 0.1217
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4837
    sort_std: 0.1217
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
    value: 0.8471
    std: 0.0314
    paper_value: 0.8471
    paper_std: 0.0314
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 2
    true_value: 0.918
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07090000000000007
    value_note: ''
    paper_rank: 23
    rank_delta: 21
    rank_delta_abs: 21
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
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8333
    std: 0.0342
    paper_value: 0.8333
    paper_std: 0.0342
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.899
    true_std: 0.03
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06569999999999998
    value_note: ''
    paper_rank: 25
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.899
    sort_std: 0.03
    is_best: true
  - model: GPRGNN_knn
    model_key: gprgnn_knn
    model_plain: GPRGNN_knn
    value: 0.8412
    std: 0.0322
    paper_value: 0.8412
    paper_std: 0.0322
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 24
    true_value: 0.8412
    true_std: 0.0322
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8412
    sort_std: 0.0322
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.8216
    std: 0.0406
    paper_value: 0.8216
    paper_std: 0.0406
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 30
    true_value: 0.8216
    true_std: 0.0406
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8216
    sort_std: 0.0406
    is_best: false
  - model: SLAPS
    model_key: slaps
    model_plain: SLAPS
    value: 0.8196
    std: 0.0326
    paper_value: 0.8196
    paper_std: 0.0326
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 31
    true_value: 0.8196
    true_std: 0.0326
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8196
    sort_std: 0.0326
    is_best: false
  - model: GEN_knn
    model_key: gen_knn
    model_plain: GEN_knn
    value: 0.8176
    std: 0.0291
    paper_value: 0.8176
    paper_std: 0.0291
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 33
    true_value: 0.8176
    true_std: 0.0291
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8176
    sort_std: 0.0291
    is_best: false
  - model: HES-GSL
    model_key: hes-gsl
    model_plain: HES-GSL
    value: 0.7961
    std: 0.0528
    paper_value: 0.7961
    paper_std: 0.0528
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.7961
    true_std: 0.0528
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7961
    sort_std: 0.0528
    is_best: false
  - model: IDGL_knn
    model_key: idgl_knn
    model_plain: IDGL_knn
    value: 0.7921
    std: 0.0394
    paper_value: 0.7921
    paper_std: 0.0394
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 50
    true_value: 0.7921
    true_std: 0.0394
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7921
    sort_std: 0.0394
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.7882
    std: 0.0655
    paper_value: 0.7882
    paper_std: 0.0655
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 52
    true_value: 0.7882
    true_std: 0.0655
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7882
    sort_std: 0.0655
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5745
    std: 0.043
    paper_value: 0.5745
    paper_std: 0.043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2118
    value_note: ''
    paper_rank: 120
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 0.7863
    std: 0.0492
    paper_value: 0.7863
    paper_std: 0.0492
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 55
    true_value: 0.7863
    true_std: 0.0492
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7863
    sort_std: 0.0492
    is_best: false
  - model: GSR_knn
    model_key: gsr_knn
    model_plain: GSR_knn
    value: 0.7862
    std: 0.0591
    paper_value: 0.7862
    paper_std: 0.0591
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 56
    true_value: 0.7862
    true_std: 0.0591
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7862
    sort_std: 0.0591
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5765
    std: 0.0775
    paper_value: 0.5765
    paper_std: 0.0775
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.7817
    true_std: 0.057
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20519999999999994
    value_note: ''
    paper_rank: 120
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.7817
    sort_std: 0.057
    is_best: false
  - model: CoGSL_knn
    model_key: cogsl_knn
    model_plain: CoGSL_knn
    value: 0.7696
    std: 0.0525
    paper_value: 0.7696
    paper_std: 0.0525
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 71
    true_value: 0.7696
    true_std: 0.0525
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7696
    sort_std: 0.0525
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4843
    std: 0.0702
    paper_value: 0.4843
    paper_std: 0.0702
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 91
    true_value: 0.7386
    true_std: 0.0403
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2543
    value_note: ''
    paper_rank: 136
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.7386
    sort_std: 0.0403
    is_best: false
  - model: ProGNN_knn
    model_key: prognn_knn
    model_plain: ProGNN_knn
    value: 0.7294
    std: 0.0793
    paper_value: 0.7294
    paper_std: 0.0793
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 94
    true_value: 0.7294
    true_std: 0.0793
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7294
    sort_std: 0.0793
    is_best: false
  - model: GEN
    model_key: gen
    model_plain: GEN
    value: 0.6607
    std: 0.0372
    paper_value: 0.6607
    paper_std: 0.0372
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 109
    true_value: 0.6607
    true_std: 0.0372
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6607
    sort_std: 0.0372
    is_best: false
  - model: ProGNN
    model_key: prognn
    model_plain: ProGNN
    value: 0.6254
    std: 0.0756
    paper_value: 0.6254
    paper_std: 0.0756
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 113
    true_value: 0.6254
    true_std: 0.0756
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6254
    sort_std: 0.0756
    is_best: false
  - model: LDS
    model_key: lds
    model_plain: LDS
    value: 0.617
    std: 0.0358
    paper_value: 0.617
    paper_std: 0.0358
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 114
    true_value: 0.617
    true_std: 0.0358
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.617
    sort_std: 0.0358
    is_best: false
  - model: IDGL
    model_key: idgl
    model_plain: IDGL
    value: 0.5941
    std: 0.0411
    paper_value: 0.5941
    paper_std: 0.0411
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 116
    true_value: 0.5941
    true_std: 0.0411
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5941
    sort_std: 0.0411
    is_best: false
  - model: CoGSL
    model_key: cogsl
    model_plain: CoGSL
    value: 0.5882
    std: 0.0152
    paper_value: 0.5882
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 117
    true_value: 0.5882
    true_std: 0.0152
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5882
    sort_std: 0.0152
    is_best: false
  - model: GSR
    model_key: gsr
    model_plain: GSR
    value: 0.5686
    std: 0.0124
    paper_value: 0.5686
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 123
    true_value: 0.5686
    true_std: 0.0124
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5686
    sort_std: 0.0124
    is_best: false
  - model: GRCN
    model_key: grcn
    model_plain: GRCN
    value: 0.5608
    std: 0.0719
    paper_value: 0.5608
    paper_std: 0.0719
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 124
    true_value: 0.5608
    true_std: 0.0719
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5608
    sort_std: 0.0719
    is_best: false
  - model: STABLE
    model_key: stable
    model_plain: STABLE
    value: 0.53
    std: 0.0527
    paper_value: 0.53
    paper_std: 0.0527
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 130
    true_value: 0.53
    true_std: 0.0527
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.0527
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7593
    sort_std: 0.0019
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7077
    std: 0.0019
    paper_value: 0.7077
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.027599999999999958
    value_note: ''
    paper_rank: 75
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.699
    std: 0.0025
    paper_value: 0.699
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03400000000000003
    value_note: ''
    paper_rank: 79
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.7175
    std: 0.0036
    paper_value: 0.7175
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.7175
    true_std: 0.0036
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7175
    sort_std: 0.0036
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.508
    std: 0.0029
    paper_value: 0.508
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 75
    true_value: 0.711
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20299999999999996
    value_note: ''
    paper_rank: 108
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.711
    sort_std: 0.0012
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.554
    std: 0.0023
    paper_value: 0.554
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 89
    true_value: 0.6778
    true_std: 0.0028
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12379999999999991
    value_note: ''
    paper_rank: 98
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.6778
    sort_std: 0.0028
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.5521
    std: 0.0011
    paper_value: 0.5521
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 91
    true_value: 0.666
    true_std: 0.0025
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1139
    value_note: ''
    paper_rank: 98
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.666
    sort_std: 0.0025
    is_best: false
  - model: HES-GSL
    model_key: hes-gsl
    model_plain: HES-GSL
    value: 0.5646
    std: 0.0027
    paper_value: 0.5646
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 97
    true_value: 0.5646
    true_std: 0.0027
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5646
    sort_std: 0.0027
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.5592
    std: 0.003
    paper_value: 0.5592
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 98
    true_value: 0.5592
    true_std: 0.003
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5592
    sort_std: 0.003
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 0.5521
    std: 0.0022
    paper_value: 0.5521
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 99
    true_value: 0.5521
    true_std: 0.0022
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5521
    sort_std: 0.0022
    is_best: false
  - model: SLAPS
    model_key: slaps
    model_plain: SLAPS
    value: 0.5519
    std: 0.0021
    paper_value: 0.5519
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 100
    true_value: 0.5519
    true_std: 0.0021
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5519
    sort_std: 0.0021
    is_best: false
  - model: GPRGNN_knn
    model_key: gprgnn_knn
    model_plain: GPRGNN_knn
    value: 0.5139
    std: 0.0013
    paper_value: 0.5139
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 108
    true_value: 0.5139
    true_std: 0.0013
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5139
    sort_std: 0.0013
    is_best: false
  metric: Accuracy
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
  - *id005
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
  - *id008
- benchmark: TU Dortmund
  datasets:
  - *id009
  - *id010
  - *id011
  - *id012
  - *id013
- benchmark: OGB
  datasets:
  - *id014
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id015
  - *id016
main_figure: /figures/2310.05174/main_figure.png
---

