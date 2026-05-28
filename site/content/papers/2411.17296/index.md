---
title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
arxiv_id: '2411.17296'
source_url: ''
authors: []
published_date: Nov 26, 2024
published_date_iso: '2024-11-26'
abstract: Graph Transformers (GTs) have demonstrated remarkable performance in graph
  representation learning over popular graph neural networks (GNNs). However, self--attention,
  the core module of GTs, preserves only low-frequency signals in graph features,
  leading to ineffectiveness in capturing other important signals like high-frequency
  ones. Some recent GT models help alleviate this issue, but their flexibility and
  expressiveness are still limited since the filters they learn are fixed on predefined
  graph spectrum or spectral order. To tackle this challenge, we propose a Graph Fourier
  Kolmogorov-Arnold Transformer (GrokFormer), a novel GT model that learns highly
  expressive spectral filters with adaptive graph spectrum and spectral order through
  a Fourier series modeling over learnable activation functions. We demonstrate theoretically
  and empirically that the proposed GrokFormer filter offers better expressiveness
  than other spectral methods. Comprehensive experiments on 10 real-world node classification
  datasets across various domains, scales, and graph properties, as well as 5 graph
  classification datasets, show that GrokFormer outperforms state-of-the-art GTs and
  GNNs. Our code is available at https://github.com/GGA23/GrokFormer
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- GrokFormer
mrr: 0.4125
adjusted_mrr: 0.4125
mrr_dataset_count: 10
benchmark_categories:
- Classic
- Heterophilic Graphs
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id010
  dataset: Actor
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.4298
    std: 0.0148
    paper_value: 0.4298
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 1
    true_value: 0.4298
    true_std: 0.0148
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4298
    sort_std: 0.0148
    is_best: true
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.4215
    std: 0.0129
    paper_value: 0.4215
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 2
    true_value: 0.4215
    true_std: 0.0129
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4215
    sort_std: 0.0129
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.4193
    std: 0.0104
    paper_value: 0.4193
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 3
    true_value: 0.4193
    true_std: 0.0104
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4193
    sort_std: 0.0104
    is_best: true
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.4181
    std: 0.0052
    paper_value: 0.4181
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 4
    true_value: 0.4181
    true_std: 0.0052
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4181
    sort_std: 0.0052
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.4179
    std: 0.0101
    paper_value: 0.4179
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 5
    true_value: 0.4179
    true_std: 0.0101
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4179
    sort_std: 0.0101
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4169
    std: 0.0063
    paper_value: 0.4169
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 6
    true_value: 0.4169
    true_std: 0.0063
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4169
    sort_std: 0.0063
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.4151
    std: 0.0071
    paper_value: 0.4151
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 7
    true_value: 0.4151
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4151
    sort_std: 0.0071
    is_best: true
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.4117
    std: 0.0064
    paper_value: 0.4117
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 8
    true_value: 0.4117
    true_std: 0.0064
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4117
    sort_std: 0.0064
    is_best: true
  - model: '*-w/o-GrokFilter'
    model_key: '*-w/o-grokfilter'
    model_plain: '*-w/o-GrokFilter'
    value: 0.4095
    std: 0.0205
    paper_value: 0.4095
    paper_std: 0.0205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 9
    true_value: 0.4095
    true_std: 0.0205
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4095
    sort_std: 0.0205
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.4008
    std: 0.015
    paper_value: 0.4008
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 10
    true_value: 0.4008
    true_std: 0.015
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4008
    sort_std: 0.015
    is_best: true
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.3995
    std: 0.0064
    paper_value: 0.3995
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 11
    true_value: 0.3995
    true_std: 0.0064
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3995
    sort_std: 0.0064
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.3992
    std: 0.0067
    paper_value: 0.3992
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 12
    true_value: 0.3992
    true_std: 0.0067
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3992
    sort_std: 0.0067
    is_best: false
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.3933
    std: 0.0279
    paper_value: 0.3933
    paper_std: 0.0279
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 13
    true_value: 0.3933
    true_std: 0.0279
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3933
    sort_std: 0.0279
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.3855
    std: 0.0135
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
    global_rank: 14
    sort_value: 0.3855
    sort_std: 0.0135
    is_best: false
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.38
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 15
    sort_value: 0.38
    sort_std: 0.015
    is_best: false
  - model: GNN-Diff
    model_key: gnn-diff
    model_plain: GNN-Diff
    value: 0.3789
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 16
    sort_value: 0.3789
    sort_std: 0.0033
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3768
    std: 0.0094
    paper_value: 0.3768
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 18
    true_value: 0.3768
    true_std: 0.0094
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3768
    sort_std: 0.0094
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.3761
    std: 0.0089
    paper_value: 0.3761
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 19
    true_value: 0.3761
    true_std: 0.0089
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3761
    sort_std: 0.0089
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.3462
    std: 0.0182
    paper_value: 0.3462
    paper_std: 0.0182
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 28
    true_value: 0.369
    true_std: 0.01
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022799999999999987
    value_note: ''
    paper_rank: 50
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.369
    sort_std: 0.01
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.3631
    std: 0.0258
    paper_value: 0.3631
    paper_std: 0.0258
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 36
    true_value: 0.3631
    true_std: 0.0258
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3631
    sort_std: 0.0258
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3393
    std: 0.0247
    paper_value: 0.3393
    paper_std: 0.0247
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 59
    true_value: 0.3393
    true_std: 0.0247
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3393
    sort_std: 0.0247
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3323
    std: 0.0116
    paper_value: 0.3323
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 66
    true_value: 0.3323
    true_std: 0.0116
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3323
    sort_std: 0.0116
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Amazon-Photo
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9712
    std: 0.0024
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.9712
    sort_std: 0.0024
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9678
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.9678
    sort_std: 0.0023
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9094
    std: 0.0068
    paper_value: 0.9094
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 3
    true_value: 0.966
    true_std: 0.0033
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056599999999999984
    value_note: ''
    paper_rank: 42
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9408
    std: 0.0137
    paper_value: 0.9408
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 4
    true_value: 0.9657
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.024900000000000033
    value_note: ''
    paper_rank: 26
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.9657
    sort_std: 0.0023
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9549
    std: 0.0011
    paper_value: 0.9549
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 5
    true_value: 0.9614
    true_std: 0.0016
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006500000000000061
    value_note: ''
    paper_rank: 10
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.9614
    sort_std: 0.0016
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8826
    std: 0.0073
    paper_value: 0.8826
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 6
    true_value: 0.961
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07839999999999991
    value_note: ''
    paper_rank: 44
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.961
    sort_std: 0.0046
    is_best: false
  - model: CARIBOU
    model_key: caribou
    model_plain: CARIBOU
    value: 0.958
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.958
    sort_std: null
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9434
    std: 0.0023
    paper_value: 0.9434
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 9
    true_value: 0.9558
    true_std: 0.0036
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012399999999999967
    value_note: ''
    paper_rank: 22
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.9558
    sort_std: 0.0036
    is_best: false
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9552
    std: 0.0052
    paper_value: 0.9552
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 10
    true_value: 0.9552
    true_std: 0.0052
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9552
    sort_std: 0.0052
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.9548
    std: 0.0032
    paper_value: 0.9548
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 11
    true_value: 0.9548
    true_std: 0.0032
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9548
    sort_std: 0.0032
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.9545
    std: 0.0067
    paper_value: 0.9545
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 12
    true_value: 0.9545
    true_std: 0.0067
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9545
    sort_std: 0.0067
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.9543
    std: 0.0023
    paper_value: 0.9543
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 13
    true_value: 0.9543
    true_std: 0.0023
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9543
    sort_std: 0.0023
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.9533
    std: 0.0037
    paper_value: 0.9533
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 15
    true_value: 0.9533
    true_std: 0.0037
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9533
    sort_std: 0.0037
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.9527
    std: 0.0022
    paper_value: 0.9527
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 16
    true_value: 0.9527
    true_std: 0.0022
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9527
    sort_std: 0.0022
    is_best: false
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.951
    std: 0.0078
    paper_value: 0.951
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 17
    true_value: 0.951
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.951
    sort_std: 0.0078
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9435
    std: 0.0025
    paper_value: 0.9435
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 18
    true_value: 0.9489
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00539999999999996
    value_note: ''
    paper_rank: 20
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.9489
    sort_std: 0.0014
    is_best: false
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.9449
    std: 0.0033
    paper_value: 0.9449
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 19
    true_value: 0.9449
    true_std: 0.0033
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9449
    sort_std: 0.0033
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.9385
    std: 0.0028
    paper_value: 0.9385
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 27
    true_value: 0.9385
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9385
    sort_std: 0.0028
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.9377
    std: 0.0032
    paper_value: 0.9377
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 28
    true_value: 0.9377
    true_std: 0.0032
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9377
    sort_std: 0.0032
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.9363
    std: 0.0035
    paper_value: 0.9363
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 29
    true_value: 0.9363
    true_std: 0.0035
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9363
    sort_std: 0.0035
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.8958
    std: 0.0105
    paper_value: 0.8958
    paper_std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 43
    true_value: 0.8958
    true_std: 0.0105
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8958
    sort_std: 0.0105
    is_best: false
  - model: '*-w/o-GrokFilter'
    model_key: '*-w/o-grokfilter'
    model_plain: '*-w/o-GrokFilter'
    value: 0.8958
    std: 0.0105
    paper_value: 0.8958
    paper_std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 44
    true_value: 0.8958
    true_std: 0.0105
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8958
    sort_std: 0.0105
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.7558
    std: 0.0173
    paper_value: 0.7558
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 10
    true_value: 0.7558
    true_std: 0.0173
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7558
    sort_std: 0.0173
    is_best: false
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.7497
    std: 0.0167
    paper_value: 0.7497
    paper_std: 0.0167
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 14
    true_value: 0.7497
    true_std: 0.0167
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7497
    sort_std: 0.0167
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.7472
    std: 0.0129
    paper_value: 0.7472
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 15
    true_value: 0.7472
    true_std: 0.0129
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7472
    sort_std: 0.0129
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.742
    std: 0.0103
    paper_value: 0.742
    paper_std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 18
    true_value: 0.742
    true_std: 0.0103
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.0103
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.6847
    std: 0.0045
    paper_value: 0.6847
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 29
    true_value: 0.6847
    true_std: 0.0045
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6847
    sort_std: 0.0045
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.6829
    std: 0.0158
    paper_value: 0.6829
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 31
    true_value: 0.6829
    true_std: 0.0158
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6829
    sort_std: 0.0158
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.6728
    std: 0.0109
    paper_value: 0.6728
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 36
    true_value: 0.6748
    true_std: 0.004
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0020000000000000018
    value_note: global 0.6748 within std
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6748
    sort_std: 0.004
    is_best: false
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.6525
    std: 0.0349
    paper_value: 0.6525
    paper_std: 0.0349
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 45
    true_value: 0.6525
    true_std: 0.0349
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6525
    sort_std: 0.0349
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5961
    std: 0.0221
    paper_value: 0.5961
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.052100000000000035
    value_note: ''
    paper_rank: 70
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6313
    std: 0.0193
    paper_value: 0.6313
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00770000000000004
    value_note: global 0.6390 within std
    paper_rank: 52
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.6144
    std: 0.0137
    paper_value: 0.6144
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 62
    true_value: 0.6144
    true_std: 0.0137
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6144
    sort_std: 0.0137
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.612
    std: 0.0428
    paper_value: 0.612
    paper_std: 0.0428
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 64
    true_value: 0.612
    true_std: 0.0428
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.612
    sort_std: 0.0428
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.6017
    std: 0.0139
    paper_value: 0.6017
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 70
    true_value: 0.6017
    true_std: 0.0139
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6017
    sort_std: 0.0139
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.5928
    std: 0.0125
    paper_value: 0.5928
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 75
    true_value: 0.5928
    true_std: 0.0125
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5928
    sort_std: 0.0125
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.5634
    std: 0.0111
    paper_value: 0.5634
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 84
    true_value: 0.5634
    true_std: 0.0111
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5634
    sort_std: 0.0111
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.5492
    std: 0.0111
    paper_value: 0.5492
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 87
    true_value: 0.5492
    true_std: 0.0111
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5492
    sort_std: 0.0111
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.4607
    std: 0.0151
    paper_value: 0.4607
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 112
    true_value: 0.4607
    true_std: 0.0151
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4607
    sort_std: 0.0151
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.4521
    std: 0.0201
    paper_value: 0.4521
    paper_std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 116
    true_value: 0.4521
    true_std: 0.0201
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4521
    sort_std: 0.0201
    is_best: false
  - model: '*-w/o-GrokFilter'
    model_key: '*-w/o-grokfilter'
    model_plain: '*-w/o-GrokFilter'
    value: 0.4503
    std: 0.018
    paper_value: 0.4503
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 117
    true_value: 0.4503
    true_std: 0.018
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4503
    sort_std: 0.018
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
    paper_value: 0.8192
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 3
    true_value: 0.8192
    true_std: 0.0125
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8183
    std: 0.0178
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
    global_rank: 4
    sort_value: 0.8183
    sort_std: 0.0178
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.818
    std: 0.0076
    paper_value: 0.818
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 6
    true_value: 0.818
    true_std: 0.0076
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.818
    sort_std: 0.0076
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.8149
    std: 0.0094
    paper_value: 0.8149
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 11
    true_value: 0.8149
    true_std: 0.0094
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8149
    sort_std: 0.0094
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7986
    std: 0.0067
    paper_value: 0.7986
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01529999999999998
    value_note: ''
    paper_rank: 27
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.8112
    std: 0.0028
    paper_value: 0.8112
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 13
    true_value: 0.8112
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8112
    sort_std: 0.0028
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.809
    std: 0.0121
    paper_value: 0.809
    paper_std: 0.0121
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 16
    true_value: 0.809
    true_std: 0.0121
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.809
    sort_std: 0.0121
    is_best: true
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.8078
    std: 0.0079
    paper_value: 0.8078
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 17
    true_value: 0.8078
    true_std: 0.0079
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8078
    sort_std: 0.0079
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8052
    std: 0.0071
    paper_value: 0.8052
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8038
    std: 0.0068
    paper_value: 0.8038
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 21
    true_value: 0.8038
    true_std: 0.0068
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8038
    sort_std: 0.0068
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8012
    std: 0.0124
    paper_value: 0.8012
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 26
    true_value: 0.8012
    true_std: 0.0124
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8012
    sort_std: 0.0124
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8012
    std: 0.0083
    paper_value: 0.8012
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 25
    true_value: 0.8012
    true_std: 0.0083
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8012
    sort_std: 0.0083
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.8009
    std: 0.0079
    paper_value: 0.8009
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 27
    true_value: 0.8009
    true_std: 0.0079
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8009
    sort_std: 0.0079
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7962
    std: 0.0163
    paper_value: 0.7962
    paper_std: 0.0163
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 29
    true_value: 0.7962
    true_std: 0.0163
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7962
    sort_std: 0.0163
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7956
    std: 0.011
    paper_value: 0.7956
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 30
    true_value: 0.7956
    true_std: 0.011
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7956
    sort_std: 0.011
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.7911
    std: 0.0075
    paper_value: 0.7911
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 35
    true_value: 0.7911
    true_std: 0.0075
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7911
    sort_std: 0.0075
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7587
    std: 0.0071
    paper_value: 0.7587
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 47
    true_value: 0.7699
    true_std: 0.0112
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011199999999999988
    value_note: global 0.7699 within std
    paper_rank: 69
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.7699
    sort_std: 0.0112
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.7055
    std: 0.012
    paper_value: 0.7055
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 135
    true_value: 0.7055
    true_std: 0.012
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7055
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Coauthor-Physics
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9831
    std: 0.0018
    paper_value: 0.9831
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 1
    true_value: 0.9831
    true_std: 0.0018
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9831
    sort_std: 0.0018
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9808
    std: 0.0027
    paper_value: 0.9808
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 2
    true_value: 0.9808
    true_std: 0.0027
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9808
    sort_std: 0.0027
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9796
    std: 0.0081
    paper_value: 0.9796
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 3
    true_value: 0.9796
    true_std: 0.0081
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9796
    sort_std: 0.0081
    is_best: true
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.9786
    std: 0.0016
    paper_value: 0.9786
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 4
    true_value: 0.9786
    true_std: 0.0016
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9786
    sort_std: 0.0016
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9785
    std: 0.0026
    paper_value: 0.9785
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 5
    true_value: 0.9785
    true_std: 0.0026
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9785
    sort_std: 0.0026
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9782
    std: 0.0028
    paper_value: 0.9782
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 6
    true_value: 0.9782
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9782
    sort_std: 0.0028
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.9775
    std: 0.0053
    paper_value: 0.9775
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 7
    true_value: 0.9775
    true_std: 0.0053
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9775
    sort_std: 0.0053
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9774
    std: 0.0035
    paper_value: 0.9774
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 8
    true_value: 0.9774
    true_std: 0.0035
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9774
    sort_std: 0.0035
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.9765
    std: 0.0035
    paper_value: 0.9765
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 9
    true_value: 0.9765
    true_std: 0.0035
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9765
    sort_std: 0.0035
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.976
    std: 0.0005
    paper_value: 0.976
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 10
    true_value: 0.976
    true_std: 0.0005
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.976
    sort_std: 0.0005
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.9756
    std: 0.0028
    paper_value: 0.9756
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 11
    true_value: 0.9756
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9756
    sort_std: 0.0028
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.9736
    std: 0.003
    paper_value: 0.9736
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 12
    true_value: 0.9736
    true_std: 0.003
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9736
    sort_std: 0.003
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.9725
    std: 0.0013
    paper_value: 0.9725
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 14
    true_value: 0.9725
    true_std: 0.0013
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9725
    sort_std: 0.0013
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.9725
    std: 0.0078
    paper_value: 0.9725
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 13
    true_value: 0.9725
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9725
    sort_std: 0.0078
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.9719
    std: 0.0013
    paper_value: 0.9719
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 16
    true_value: 0.9719
    true_std: 0.0013
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9719
    sort_std: 0.0013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9719
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 15
    sort_value: 0.9719
    sort_std: 0.0005
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9706
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 17
    sort_value: 0.9706
    sort_std: 0.0013
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.9645
    std: 0.0028
    paper_value: 0.9645
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 18
    true_value: 0.9648
    true_std: 0.0034
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.9648 within std
    paper_rank: 19
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.9648
    sort_std: 0.0034
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9647
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 19
    sort_value: 0.9647
    sort_std: 0.0016
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
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8957
    std: 0.0143
    paper_value: 0.8957
    paper_std: 0.0143
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 5
    true_value: 0.8957
    true_std: 0.0143
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8957
    sort_std: 0.0143
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.8923
    std: 0.0023
    paper_value: 0.8923
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 12
    true_value: 0.8923
    true_std: 0.0023
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8923
    sort_std: 0.0023
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.8898
    std: 0.0046
    paper_value: 0.8898
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 14
    true_value: 0.8898
    true_std: 0.0046
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8898
    sort_std: 0.0046
    is_best: false
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.8898
    std: 0.0125
    paper_value: 0.8898
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 15
    true_value: 0.8898
    true_std: 0.0125
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8898
    sort_std: 0.0125
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8732
    std: 0.0092
    paper_value: 0.8732
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 20
    true_value: 0.887
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013800000000000034
    value_note: ''
    paper_rank: 60
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.887
    sort_std: 0.002
    is_best: false
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8868
    std: 0.0106
    paper_value: 0.8868
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 24
    true_value: 0.8868
    true_std: 0.0106
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8868
    sort_std: 0.0106
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.8857
    std: 0.0101
    paper_value: 0.8857
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 26
    true_value: 0.8857
    true_std: 0.0101
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8857
    sort_std: 0.0101
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8857
    std: 0.0069
    paper_value: 0.8857
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 25
    true_value: 0.8857
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8857
    sort_std: 0.0069
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.8852
    std: 0.0095
    paper_value: 0.8852
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 28
    true_value: 0.8852
    true_std: 0.0095
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8852
    sort_std: 0.0095
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8803
    std: 0.0079
    paper_value: 0.8803
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0021999999999999797
    value_note: global 0.8825 within std
    paper_rank: 38
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8815
    std: 0.0135
    paper_value: 0.8815
    paper_std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 33
    true_value: 0.882
    true_std: 0.005
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.000500000000000056
    value_note: global 0.8820 within std
    paper_rank: 34
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.882
    sort_std: 0.005
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8787
    std: 0.0267
    paper_value: 0.8787
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 37
    true_value: 0.8809999999999999
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0022999999999998577
    value_note: global 0.8810 within std
    paper_rank: 45
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.006999999999999999
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8796
    std: 0.0037
    paper_value: 0.8796
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 41
    true_value: 0.8796
    true_std: 0.0037
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8796
    sort_std: 0.0037
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8767
    std: 0.0128
    paper_value: 0.8767
    paper_std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 45
    true_value: 0.879
    true_std: 0.012
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0022999999999999687
    value_note: global 0.8790 within std
    paper_rank: 51
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8714
    std: 0.0101
    paper_value: 0.8714
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006400000000000072
    value_note: global 0.8778 within std
    paper_rank: 64
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.8667
    std: 0.0082
    paper_value: 0.8667
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 77
    true_value: 0.8667
    true_std: 0.0082
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8667
    sort_std: 0.0082
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8342
    std: 0.0122
    paper_value: 0.8342
    paper_std: 0.0122
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 114
    true_value: 0.8387
    true_std: 0.0096
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0044999999999999485
    value_note: global 0.8387 within std
    paper_rank: 120
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8387
    sort_std: 0.0096
    is_best: false
  - model: '*-w/o-GrokFilter'
    model_key: '*-w/o-grokfilter'
    model_plain: '*-w/o-GrokFilter'
    value: 0.7742
    std: 0.0177
    paper_value: 0.7742
    paper_std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 181
    true_value: 0.7742
    true_std: 0.0177
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 181
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7742
    sort_std: 0.0177
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.7183
    std: 0.0168
    paper_value: 0.7183
    paper_std: 0.0168
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 231
    true_value: 0.7183
    true_std: 0.0168
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 231
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7183
    sort_std: 0.0168
    is_best: false
  metric: Accuracy
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8674
    std: 0.0027
    paper_value: 0.8674
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05500000000000005
    value_note: ''
    paper_rank: 92
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8704
    std: 0.0024
    paper_value: 0.8704
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04970000000000008
    value_note: ''
    paper_rank: 89
    rank_delta: 83
    rank_delta_abs: 83
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9139
    std: 0.0051
    paper_value: 0.9139
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 8
    true_value: 0.9139
    true_std: 0.0051
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9139
    sort_std: 0.0051
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9068
    std: 0.0031
    paper_value: 0.9068
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 11
    true_value: 0.9068
    true_std: 0.0031
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9068
    sort_std: 0.0031
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.9061
    std: 0.0023
    paper_value: 0.9061
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 13
    true_value: 0.9061
    true_std: 0.0023
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9061
    sort_std: 0.0023
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.8995
    std: 0.0013
    paper_value: 0.8995
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 24
    true_value: 0.8995
    true_std: 0.0013
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8995
    sort_std: 0.0013
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.897
    std: 0.0019
    paper_value: 0.897
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 27
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8907
    std: 0.0014
    paper_value: 0.8907
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 26
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006299999999999972
    value_note: ''
    paper_rank: 41
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.8962
    std: 0.0041
    paper_value: 0.8962
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 29
    true_value: 0.8962
    true_std: 0.0041
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8962
    sort_std: 0.0041
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8918
    std: 0.0028
    paper_value: 0.8918
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 34
    true_value: 0.895
    true_std: 0.004
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0031999999999999806
    value_note: global 0.8950 within std
    paper_rank: 38
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.004
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8846
    std: 0.0033
    paper_value: 0.8846
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 37
    true_value: 0.8934
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008799999999999919
    value_note: ''
    paper_rank: 57
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.8934
    sort_std: 0.0025
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8924
    std: 0.0023
    paper_value: 0.8924
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 38
    true_value: 0.8932
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0008000000000000229
    value_note: global 0.8932 within std
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8932
    sort_std: 0.0025
    is_best: false
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8915
    std: 0.0035
    paper_value: 0.8915
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 40
    true_value: 0.8915
    true_std: 0.0035
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8915
    sort_std: 0.0035
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8662
    std: 0.0053
    paper_value: 0.8662
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 45
    true_value: 0.8894
    true_std: 0.0016
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0232
    value_note: ''
    paper_rank: 95
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.8894
    sort_std: 0.0016
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.8848
    std: 0.0041
    paper_value: 0.8848
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 56
    true_value: 0.8848
    true_std: 0.0041
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8848
    sort_std: 0.0041
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.8795
    std: 0.0028
    paper_value: 0.8795
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 72
    true_value: 0.8795
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8795
    sort_std: 0.0028
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.8666
    std: 0.005
    paper_value: 0.8666
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 95
    true_value: 0.8666
    true_std: 0.005
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8666
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.6512
    std: 0.0159
    paper_value: 0.6512
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 15
    true_value: 0.6512
    true_std: 0.0159
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6512
    sort_std: 0.0159
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.6464
    std: 0.0081
    paper_value: 0.6464
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 16
    true_value: 0.6464
    true_std: 0.0081
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6464
    sort_std: 0.0081
    is_best: false
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.5783
    std: 0.0211
    paper_value: 0.5783
    paper_std: 0.0211
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 25
    true_value: 0.5783
    true_std: 0.0211
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5783
    sort_std: 0.0211
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.5738
    std: 0.0125
    paper_value: 0.5738
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 26
    true_value: 0.5738
    true_std: 0.0125
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5738
    sort_std: 0.0125
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4678
    std: 0.0087
    paper_value: 0.4678
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0665
    value_note: ''
    paper_rank: 45
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.5186
    std: 0.0042
    paper_value: 0.5186
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 37
    true_value: 0.5186
    true_std: 0.0042
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5186
    sort_std: 0.0042
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.5135
    std: 0.0073
    paper_value: 0.5135
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 38
    true_value: 0.5135
    true_std: 0.0073
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5135
    sort_std: 0.0073
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.5015
    std: 0.0192
    paper_value: 0.5015
    paper_std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 41
    true_value: 0.5015
    true_std: 0.0192
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5015
    sort_std: 0.0192
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.4855
    std: 0.0256
    paper_value: 0.4855
    paper_std: 0.0256
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 43
    true_value: 0.4855
    true_std: 0.0256
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4855
    sort_std: 0.0256
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4582
    std: 0.0217
    paper_value: 0.4582
    paper_std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 48
    true_value: 0.4582
    true_std: 0.0217
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4582
    sort_std: 0.0217
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.4498
    std: 0.0303
    paper_value: 0.4498
    paper_std: 0.0303
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 50
    true_value: 0.4498
    true_std: 0.0303
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4498
    sort_std: 0.0303
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4449
    std: 0.0088
    paper_value: 0.4449
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4449
    sort_std: 0.0088
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.4055
    std: 0.0042
    paper_value: 0.4055
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 53
    true_value: 0.4386
    true_std: 0.0164
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03309999999999996
    value_note: ''
    paper_rank: 75
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.4386
    sort_std: 0.0164
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4342
    std: 0.0162
    paper_value: 0.4342
    paper_std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 56
    true_value: 0.4342
    true_std: 0.0162
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4342
    sort_std: 0.0162
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3414
    std: 0.0073
    paper_value: 0.3414
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 77
    true_value: 0.3981
    true_std: 0.0228
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05670000000000003
    value_note: ''
    paper_rank: 105
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.3981
    sort_std: 0.0228
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.3953
    std: 0.0088
    paper_value: 0.3953
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 78
    true_value: 0.3953
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3953
    sort_std: 0.0088
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.3317
    std: 0.0132
    paper_value: 0.3317
    paper_std: 0.0132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 107
    true_value: 0.3317
    true_std: 0.0132
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3317
    sort_std: 0.0132
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9459
    std: 0.0208
    paper_value: 0.9459
    paper_std: 0.0208
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 5
    true_value: 0.9459
    true_std: 0.0208
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9459
    sort_std: 0.0208
    is_best: true
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.9362
    std: 0.0304
    paper_value: 0.9362
    paper_std: 0.0304
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 6
    true_value: 0.9362
    true_std: 0.0304
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9362
    sort_std: 0.0304
    is_best: true
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.9344
    std: 0.0213
    paper_value: 0.9344
    paper_std: 0.0213
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 8
    true_value: 0.9344
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9344
    sort_std: 0.0213
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.9312
    std: 0.0065
    paper_value: 0.9312
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 10
    true_value: 0.9312
    true_std: 0.0065
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9312
    sort_std: 0.0065
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.9295
    std: 0.0131
    paper_value: 0.9295
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 11
    true_value: 0.9295
    true_std: 0.0131
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9295
    sort_std: 0.0131
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9246
    std: 0.0148
    paper_value: 0.9246
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 13
    true_value: 0.9246
    true_std: 0.0148
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9246
    sort_std: 0.0148
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.9215
    std: 0.0073
    paper_value: 0.9215
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 16
    true_value: 0.9215
    true_std: 0.0073
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9215
    sort_std: 0.0073
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.9189
    std: 0.0393
    paper_value: 0.9189
    paper_std: 0.0393
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 17
    true_value: 0.9189
    true_std: 0.0393
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9189
    sort_std: 0.0393
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.918
    std: 0.0185
    paper_value: 0.918
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 18
    true_value: 0.918
    true_std: 0.0185
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.0185
    is_best: false
  - model: '*-w/o-GrokFilter'
    model_key: '*-w/o-grokfilter'
    model_plain: '*-w/o-GrokFilter'
    value: 0.9033
    std: 0.0236
    paper_value: 0.9033
    paper_std: 0.0236
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 20
    true_value: 0.9033
    true_std: 0.0236
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9033
    sort_std: 0.0236
    is_best: false
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8915
    std: 0.0404
    paper_value: 0.8915
    paper_std: 0.0404
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 23
    true_value: 0.8915
    true_std: 0.0404
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8915
    sort_std: 0.0404
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8902
    std: 0.0544
    paper_value: 0.8902
    paper_std: 0.0544
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 24
    true_value: 0.8902
    true_std: 0.0544
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8902
    sort_std: 0.0544
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.8875
    std: 0.063
    paper_value: 0.8875
    paper_std: 0.063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 26
    true_value: 0.8875
    true_std: 0.063
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8875
    sort_std: 0.063
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.8823
    std: 0.0038
    paper_value: 0.8823
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 29
    true_value: 0.8823
    true_std: 0.0038
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8823
    sort_std: 0.0038
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.8622
    std: 0.0245
    paper_value: 0.8622
    paper_std: 0.0245
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 32
    true_value: 0.8622
    true_std: 0.0245
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8622
    sort_std: 0.0245
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8463
    std: 0.0347
    paper_value: 0.8463
    paper_std: 0.0347
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 39
    true_value: 0.8463
    true_std: 0.0347
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8463
    sort_std: 0.0347
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8371
    std: 0.0585
    paper_value: 0.8371
    paper_std: 0.0585
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 44
    true_value: 0.8371
    true_std: 0.0585
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8371
    sort_std: 0.0585
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7738
    std: 0.0328
    paper_value: 0.7738
    paper_std: 0.0328
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05729999999999991
    value_note: ''
    paper_rank: 76
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8082
    std: 0.0213
    paper_value: 0.8082
    paper_std: 0.0213
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: WikiCS
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8557
    std: 0.0065
    paper_value: 0.8557
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 1
    true_value: 0.8557
    true_std: 0.0065
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8557
    sort_std: 0.0065
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.8515
    std: 0.0063
    paper_value: 0.8515
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 2
    true_value: 0.8515
    true_std: 0.0063
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8515
    sort_std: 0.0063
    is_best: true
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8473
    std: 0.0059
    paper_value: 0.8473
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 3
    true_value: 0.8473
    true_std: 0.0059
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8473
    sort_std: 0.0059
    is_best: true
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.8413
    std: 0.0049
    paper_value: 0.8413
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 4
    true_value: 0.8413
    true_std: 0.0049
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8413
    sort_std: 0.0049
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8362
    std: 0.0017
    paper_value: 0.8362
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 5
    true_value: 0.8362
    true_std: 0.0017
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8362
    sort_std: 0.0017
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.8356
    std: 0.0061
    paper_value: 0.8356
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 6
    true_value: 0.8356
    true_std: 0.0061
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8356
    sort_std: 0.0061
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8345
    std: 0.0026
    paper_value: 0.8345
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 7
    true_value: 0.8345
    true_std: 0.0026
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8345
    sort_std: 0.0026
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8341
    std: 0.0034
    paper_value: 0.8341
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 8
    true_value: 0.8341
    true_std: 0.0034
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8341
    sort_std: 0.0034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8322
    std: 0.0078
    paper_value: 0.8322
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 9
    true_value: 0.8322
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8322
    sort_std: 0.0078
    is_best: false
  - model: HiGCN
    model_key: higcn
    model_plain: HiGCN
    value: 0.8314
    std: 0.0078
    paper_value: 0.8314
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 10
    true_value: 0.8314
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8314
    sort_std: 0.0078
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.8295
    std: 0.0045
    paper_value: 0.8295
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 11
    true_value: 0.8295
    true_std: 0.0045
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8295
    sort_std: 0.0045
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8271
    std: 0.0056
    paper_value: 0.8271
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 12
    true_value: 0.8271
    true_std: 0.0056
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8271
    sort_std: 0.0056
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8258
    std: 0.0089
    paper_value: 0.8258
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 13
    true_value: 0.8258
    true_std: 0.0089
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8258
    sort_std: 0.0089
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8232
    std: 0.0069
    paper_value: 0.8232
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 14
    true_value: 0.8232
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8232
    sort_std: 0.0069
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.8148
    std: 0.0046
    metric: Accuracy
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
    global_rank: 15
    sort_value: 0.8148
    sort_std: 0.0046
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8103
    std: 0.0094
    paper_value: 0.8103
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 16
    true_value: 0.8103
    true_std: 0.0094
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8103
    sort_std: 0.0094
    is_best: false
  - model: RWPT (Edge feat. input)
    model_key: rwpt (edge feat. input)
    model_plain: RWPT (Edge feat. input)
    value: 0.8093
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 17
    sort_value: 0.8093
    sort_std: 0.0026
    is_best: false
  - model: RWPT (Walk, k=16, l=2)
    model_key: rwpt (walk, k=16, l=2)
    model_plain: RWPT (Walk, k=16, l=2)
    value: 0.808
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 18
    sort_value: 0.808
    sort_std: null
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7926
    std: 0.0057
    paper_value: 0.7926
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 39
    true_value: 0.7926
    true_std: 0.0057
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7926
    sort_std: 0.0057
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.7736
    std: 0.0125
    paper_value: 0.7736
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    global_rank: 49
    true_value: 0.7736
    true_std: 0.0125
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7736
    sort_std: 0.0125
    is_best: false
  metric: Accuracy
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
- benchmark: Heterophilic Graphs
  datasets:
  - *id007
  - *id008
  - *id009
  - *id010
single_proposed_model: GrokFormer
main_figure: /figures/2411.17296/main_figure.png
---

