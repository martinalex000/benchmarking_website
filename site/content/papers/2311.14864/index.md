---
title: Effective Structural Encodings via Local Curvature Profiles
arxiv_id: '2311.14864'
source_url: ''
authors: []
published_date: Nov 2023
published_date_iso: 2023-11
abstract: Structural and Positional Encodings can significantly improve the performance
  of Graph Neural Networks in downstream tasks. Recent literature has begun to systematically
  investigate differences in the structural properties that these approaches encode,
  as well as performance trade-offs between them. However, the question of which structural
  properties yield the most effective encoding remains open. In this paper, we investigate
  this question from a geometric perspective. We propose a novel structural encoding
  based on discrete Ricci curvature (Local Curvature Profiles, short LCP) and show
  that it significantly outperforms existing encoding approaches. We further show
  that combining local structural encodings, such as LCP, with global positional encodings
  improves downstream performance, suggesting that they capture complementary geometric
  information. Finally, we compare different encoding types with (curvature-based)
  rewiring techniques. Rewiring has recently received a surge of interest due to its
  ability to improve the performance of Graph Neural Networks by mitigating over-smoothing
  and over-squashing effects. Our results suggest that utilizing curvature information
  for structural encodings delivers significantly larger performance increases than
  rewiring. Code available at https://github.com/Weber-GeoML/Local_Curvature_Profile
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN (LCP)
- GIN (LCP)
- GAT (LCP)
- GCN (LCP, LA)
- GCN (LCP, RW)
- GAT (LCP, LA)
- GAT (LCP, RW)
mrr: 0.0178
adjusted_mrr: 0.0178
mrr_dataset_count: 7
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
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
    date: '2024-11-26'
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: GAT (LCP, RW)
    model_key: gat (lcp, rw)
    model_plain: GAT (LCP, RW)
    value: 0.774
    std: 0.015
    paper_value: 0.774
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 42
    true_value: 0.774
    true_std: 0.015
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.774
    sort_std: 0.015
    is_best: false
  - model: GAT (LCP, LA)
    model_key: gat (lcp, la)
    model_plain: GAT (LCP, LA)
    value: 0.772
    std: 0.013
    paper_value: 0.772
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 43
    true_value: 0.772
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.013
    is_best: false
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.771
    std: 0.012
    paper_value: 0.771
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 44
    true_value: 0.771
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.012
    is_best: false
  - model: GAT (SUB, RW)
    model_key: gat (sub, rw)
    model_plain: GAT (SUB, RW)
    value: 0.771
    std: 0.014
    paper_value: 0.771
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 45
    true_value: 0.771
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.014
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.769
    std: 0.011
    paper_value: 0.769
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 48
    true_value: 0.769
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: 0.011
    is_best: false
  - model: GAT (SUB, LA)
    model_key: gat (sub, la)
    model_plain: GAT (SUB, LA)
    value: 0.769
    std: 0.016
    paper_value: 0.769
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 49
    true_value: 0.769
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: 0.016
    is_best: false
  - model: GAT (LCP)
    model_key: gat (lcp)
    model_plain: GAT (LCP)
    value: 0.766
    std: 0.012
    paper_value: 0.766
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 55
    true_value: 0.766
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
    sort_std: 0.012
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.763
    std: 0.015
    paper_value: 0.763
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 61
    true_value: 0.763
    true_std: 0.015
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.015
    is_best: false
  - model: GAT (SUB)
    model_key: gat (sub)
    model_plain: GAT (SUB)
    value: 0.763
    std: 0.012
    paper_value: 0.763
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 62
    true_value: 0.763
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.012
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.759
    std: 0.012
    paper_value: 0.759
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 69
    true_value: 0.759
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.012
    is_best: false
  - model: GAT (RW)
    model_key: gat (rw)
    model_plain: GAT (RW)
    value: 0.758
    std: 0.014
    paper_value: 0.758
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 73
    true_value: 0.758
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.014
    is_best: false
  - model: GAT (LA)
    model_key: gat (la)
    model_plain: GAT (LA)
    value: 0.751
    std: 0.011
    paper_value: 0.751
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 86
    true_value: 0.751
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.011
    is_best: false
  - model: GAT (NO)
    model_key: gat (no)
    model_plain: GAT (NO)
    value: 0.726
    std: 0.008
    paper_value: 0.726
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 115
    true_value: 0.726
    true_std: 0.008
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.008
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.717
    std: 0.007
    paper_value: 0.717
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 124
    true_value: 0.717
    true_std: 0.007
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.007
    is_best: false
  - model: GCN (LCP, RW)
    model_key: gcn (lcp, rw)
    model_plain: GCN (LCP, RW)
    value: 0.663
    std: 0.011
    paper_value: 0.663
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 159
    true_value: 0.663
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.663
    sort_std: 0.011
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.643
    std: 0.011
    paper_value: 0.643
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 173
    true_value: 0.643
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 173
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.643
    sort_std: 0.011
    is_best: false
  - model: GCN (SUB, LA)
    model_key: gcn (sub, la)
    model_plain: GCN (SUB, LA)
    value: 0.641
    std: 0.012
    paper_value: 0.641
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 175
    true_value: 0.641
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.641
    sort_std: 0.012
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.638
    std: 0.01
    paper_value: 0.638
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 176
    true_value: 0.638
    true_std: 0.01
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.638
    sort_std: 0.01
    is_best: false
  - model: GCN (LCP, LA)
    model_key: gcn (lcp, la)
    model_plain: GCN (LCP, LA)
    value: 0.632
    std: 0.012
    paper_value: 0.632
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 179
    true_value: 0.632
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 179
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.632
    sort_std: 0.012
    is_best: false
  - model: GCN (SUB, RW)
    model_key: gcn (sub, rw)
    model_plain: GCN (SUB, RW)
    value: 0.623
    std: 0.014
    paper_value: 0.623
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 182
    true_value: 0.623
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.623
    sort_std: 0.014
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.621
    std: 0.013
    paper_value: 0.621
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 184
    true_value: 0.621
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.621
    sort_std: 0.013
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.614
    std: 0.013
    paper_value: 0.614
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 189
    true_value: 0.614
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.614
    sort_std: 0.013
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.599
    std: 0.006
    paper_value: 0.599
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 201
    true_value: 0.599
    true_std: 0.006
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.599
    sort_std: 0.006
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
    date: '2025-01-30'
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.889
    std: 0.01
    paper_value: 0.889
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 17
    true_value: 0.889
    true_std: 0.01
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.889
    sort_std: 0.01
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.881
    std: 0.009
    paper_value: 0.881
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 35
    true_value: 0.881
    true_std: 0.009
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.881
    sort_std: 0.009
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.88
    std: 0.009
    paper_value: 0.88
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 40
    true_value: 0.88
    true_std: 0.009
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.88
    sort_std: 0.009
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.876
    std: 0.011
    paper_value: 0.876
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 56
    true_value: 0.876
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.876
    sort_std: 0.011
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.866
    std: 0.008
    paper_value: 0.866
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 80
    true_value: 0.866
    true_std: 0.008
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.866
    sort_std: 0.008
    is_best: false
  - model: GAT (LCP, LA)
    model_key: gat (lcp, la)
    model_plain: GAT (LCP, LA)
    value: 0.866
    std: 0.014
    paper_value: 0.866
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 81
    true_value: 0.866
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.866
    sort_std: 0.014
    is_best: false
  - model: GAT (LCP, RW)
    model_key: gat (lcp, rw)
    model_plain: GAT (LCP, RW)
    value: 0.861
    std: 0.015
    paper_value: 0.861
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 88
    true_value: 0.861
    true_std: 0.015
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.861
    sort_std: 0.015
    is_best: false
  - model: GAT (LCP)
    model_key: gat (lcp)
    model_plain: GAT (LCP)
    value: 0.857
    std: 0.011
    paper_value: 0.857
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 91
    true_value: 0.857
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.857
    sort_std: 0.011
    is_best: false
  - model: GAT (SUB, RW)
    model_key: gat (sub, rw)
    model_plain: GAT (SUB, RW)
    value: 0.857
    std: 0.014
    paper_value: 0.857
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 92
    true_value: 0.857
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.857
    sort_std: 0.014
    is_best: false
  - model: GAT (SUB, LA)
    model_key: gat (sub, la)
    model_plain: GAT (SUB, LA)
    value: 0.853
    std: 0.013
    paper_value: 0.853
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 99
    true_value: 0.853
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.853
    sort_std: 0.013
    is_best: false
  - model: GAT (SUB)
    model_key: gat (sub)
    model_plain: GAT (SUB)
    value: 0.85
    std: 0.012
    paper_value: 0.85
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 104
    true_value: 0.85
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.012
    is_best: false
  - model: GAT (LA)
    model_key: gat (la)
    model_plain: GAT (LA)
    value: 0.847
    std: 0.01
    paper_value: 0.847
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 107
    true_value: 0.847
    true_std: 0.01
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.847
    sort_std: 0.01
    is_best: false
  - model: GAT (RW)
    model_key: gat (rw)
    model_plain: GAT (RW)
    value: 0.838
    std: 0.009
    paper_value: 0.838
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 116
    true_value: 0.838
    true_std: 0.009
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.838
    sort_std: 0.009
    is_best: false
  - model: GAT (NO)
    model_key: gat (no)
    model_plain: GAT (NO)
    value: 0.834
    std: 0.008
    paper_value: 0.834
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 121
    true_value: 0.834
    true_std: 0.008
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.834
    sort_std: 0.008
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.801
    std: 0.007
    paper_value: 0.801
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 155
    true_value: 0.801
    true_std: 0.007
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.801
    sort_std: 0.007
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.798
    std: 0.011
    paper_value: 0.798
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 157
    true_value: 0.798
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.798
    sort_std: 0.011
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.793
    std: 0.011
    paper_value: 0.793
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 164
    true_value: 0.793
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.011
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.781
    std: 0.01
    paper_value: 0.781
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 175
    true_value: 0.781
    true_std: 0.01
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.781
    sort_std: 0.01
    is_best: false
  - model: GCN (LCP, LA)
    model_key: gcn (lcp, la)
    model_plain: GCN (LCP, LA)
    value: 0.778
    std: 0.015
    paper_value: 0.778
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 179
    true_value: 0.778
    true_std: 0.015
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 179
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.778
    sort_std: 0.015
    is_best: false
  - model: GCN (SUB, LA)
    model_key: gcn (sub, la)
    model_plain: GCN (SUB, LA)
    value: 0.774
    std: 0.013
    paper_value: 0.774
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 182
    true_value: 0.774
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.774
    sort_std: 0.013
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.763
    std: 0.006
    paper_value: 0.763
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 190
    true_value: 0.763
    true_std: 0.006
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.006
    is_best: false
  - model: GCN (LCP, RW)
    model_key: gcn (lcp, rw)
    model_plain: GCN (LCP, RW)
    value: 0.761
    std: 0.016
    paper_value: 0.761
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 191
    true_value: 0.761
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 191
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.761
    sort_std: 0.016
    is_best: false
  - model: GCN (SUB, RW)
    model_key: gcn (sub, rw)
    model_plain: GCN (SUB, RW)
    value: 0.758
    std: 0.016
    paper_value: 0.758
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 193
    true_value: 0.758
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 193
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.016
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
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
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
    date: '2023-06-09'
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
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.354
    std: 0.026
    paper_value: 0.354
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 62
    true_value: 0.354
    true_std: 0.026
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.354
    sort_std: 0.026
    is_best: false
  - model: GAT (LCP, RW)
    model_key: gat (lcp, rw)
    model_plain: GAT (LCP, RW)
    value: 0.351
    std: 0.024
    paper_value: 0.351
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 64
    true_value: 0.351
    true_std: 0.024
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.351
    sort_std: 0.024
    is_best: false
  - model: GAT (LCP)
    model_key: gat (lcp)
    model_plain: GAT (LCP)
    value: 0.345
    std: 0.02
    paper_value: 0.345
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 66
    true_value: 0.345
    true_std: 0.02
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.345
    sort_std: 0.02
    is_best: false
  - model: GCN (LCP, LA)
    model_key: gcn (lcp, la)
    model_plain: GCN (LCP, LA)
    value: 0.336
    std: 0.027
    paper_value: 0.336
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 69
    true_value: 0.336
    true_std: 0.027
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.336
    sort_std: 0.027
    is_best: false
  - model: GAT (LCP, LA)
    model_key: gat (lcp, la)
    model_plain: GAT (LCP, LA)
    value: 0.336
    std: 0.021
    paper_value: 0.336
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 70
    true_value: 0.336
    true_std: 0.021
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.336
    sort_std: 0.021
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.327
    std: 0.016
    paper_value: 0.327
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 76
    true_value: 0.327
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.327
    sort_std: 0.016
    is_best: false
  - model: GCN (LCP, RW)
    model_key: gcn (lcp, rw)
    model_plain: GCN (LCP, RW)
    value: 0.317
    std: 0.024
    paper_value: 0.317
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 81
    true_value: 0.317
    true_std: 0.024
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.317
    sort_std: 0.024
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.31
    std: 0.022
    paper_value: 0.31
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 87
    true_value: 0.31
    true_std: 0.022
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31
    sort_std: 0.022
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.297
    std: 0.025
    paper_value: 0.297
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 95
    true_value: 0.297
    true_std: 0.025
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.297
    sort_std: 0.025
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.297
    std: 0.011
    paper_value: 0.297
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 96
    true_value: 0.297
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.297
    sort_std: 0.011
    is_best: false
  - model: GCN (SUB, RW)
    model_key: gcn (sub, rw)
    model_plain: GCN (SUB, RW)
    value: 0.287
    std: 0.024
    paper_value: 0.287
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 102
    true_value: 0.287
    true_std: 0.024
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.287
    sort_std: 0.024
    is_best: false
  - model: GCN (SUB, LA)
    model_key: gcn (sub, la)
    model_plain: GCN (SUB, LA)
    value: 0.283
    std: 0.019
    paper_value: 0.283
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 110
    true_value: 0.283
    true_std: 0.019
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.283
    sort_std: 0.019
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.277
    std: 0.014
    paper_value: 0.277
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 114
    true_value: 0.277
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.277
    sort_std: 0.014
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.275
    std: 0.021
    paper_value: 0.275
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 117
    true_value: 0.275
    true_std: 0.021
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.275
    sort_std: 0.021
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.266
    std: 0.019
    paper_value: 0.266
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 118
    true_value: 0.266
    true_std: 0.019
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.266
    sort_std: 0.019
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.265
    std: 0.011
    paper_value: 0.265
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 119
    true_value: 0.265
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.265
    sort_std: 0.011
    is_best: false
  - model: GAT (SUB, RW)
    model_key: gat (sub, rw)
    model_plain: GAT (SUB, RW)
    value: 0.265
    std: 0.013
    paper_value: 0.265
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 120
    true_value: 0.265
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.265
    sort_std: 0.013
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.254
    std: 0.013
    paper_value: 0.254
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 122
    true_value: 0.254
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.254
    sort_std: 0.013
    is_best: false
  - model: GAT (SUB)
    model_key: gat (sub)
    model_plain: GAT (SUB)
    value: 0.25
    std: 0.014
    paper_value: 0.25
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 124
    true_value: 0.25
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.014
    is_best: false
  - model: GAT (RW)
    model_key: gat (rw)
    model_plain: GAT (RW)
    value: 0.234
    std: 0.017
    paper_value: 0.234
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 125
    true_value: 0.234
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.234
    sort_std: 0.017
    is_best: false
  - model: GAT (LA)
    model_key: gat (la)
    model_plain: GAT (LA)
    value: 0.232
    std: 0.013
    paper_value: 0.232
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 126
    true_value: 0.232
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.232
    sort_std: 0.013
    is_best: false
  - model: GAT (SUB, LA)
    model_key: gat (sub, la)
    model_plain: GAT (SUB, LA)
    value: 0.229
    std: 0.018
    paper_value: 0.229
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 127
    true_value: 0.229
    true_std: 0.018
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.229
    sort_std: 0.018
    is_best: false
  - model: GAT (NO)
    model_key: gat (no)
    model_plain: GAT (NO)
    value: 0.225
    std: 0.017
    paper_value: 0.225
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 128
    true_value: 0.225
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.225
    sort_std: 0.017
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: GCN (LCP, RW)
    model_key: gcn (lcp, rw)
    model_plain: GCN (LCP, RW)
    value: 0.721
    std: 0.017
    paper_value: 0.721
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 63
    true_value: 0.721
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.017
    is_best: false
  - model: GCN (RW) [BORF]
    model_key: gcn (rw) [borf]
    model_plain: GCN (RW) [BORF]
    value: 0.717
    std: 0.024
    paper_value: 0.717
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 72
    true_value: 0.717
    true_std: 0.024
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.024
    is_best: false
  - model: GCN (LCP, LA)
    model_key: gcn (lcp, la)
    model_plain: GCN (LCP, LA)
    value: 0.708
    std: 0.011
    paper_value: 0.708
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 89
    true_value: 0.708
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: 0.011
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.706
    std: 0.013
    paper_value: 0.706
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 93
    true_value: 0.706
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.706
    sort_std: 0.013
    is_best: false
  - model: GCN (LA) [BORF]
    model_key: gcn (la) [borf]
    model_plain: GCN (LA) [BORF]
    value: 0.702
    std: 0.021
    paper_value: 0.702
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 98
    true_value: 0.702
    true_std: 0.021
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.702
    sort_std: 0.021
    is_best: false
  - model: GCN (SUB, RW)
    model_key: gcn (sub, rw)
    model_plain: GCN (SUB, RW)
    value: 0.699
    std: 0.011
    paper_value: 0.699
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 102
    true_value: 0.699
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.699
    sort_std: 0.011
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.693
    std: 0.022
    paper_value: 0.693
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 107
    true_value: 0.693
    true_std: 0.022
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.693
    sort_std: 0.022
    is_best: false
  - model: GCN (SUB, LA)
    model_key: gcn (sub, la)
    model_plain: GCN (SUB, LA)
    value: 0.683
    std: 0.014
    paper_value: 0.683
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 110
    true_value: 0.683
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.683
    sort_std: 0.014
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.682
    std: 0.021
    paper_value: 0.682
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 112
    true_value: 0.682
    true_std: 0.021
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.682
    sort_std: 0.021
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.681
    std: 0.028
    paper_value: 0.681
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 113
    true_value: 0.681
    true_std: 0.028
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.681
    sort_std: 0.028
    is_best: false
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.677
    std: 0.017
    paper_value: 0.677
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 114
    true_value: 0.677
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.677
    sort_std: 0.017
    is_best: false
  - model: GCN (NO) [BORF]
    model_key: gcn (no) [borf]
    model_plain: GCN (NO) [BORF]
    value: 0.677
    std: 0.015
    paper_value: 0.677
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 116
    true_value: 0.677
    true_std: 0.015
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.677
    sort_std: 0.015
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.671
    std: 0.013
    paper_value: 0.671
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 119
    true_value: 0.671
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.671
    sort_std: 0.013
    is_best: false
  - model: GAT (LCP)
    model_key: gat (lcp)
    model_plain: GAT (LCP)
    value: 0.662
    std: 0.011
    paper_value: 0.662
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 121
    true_value: 0.662
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.662
    sort_std: 0.011
    is_best: false
  - model: GAT (LCP, RW)
    model_key: gat (lcp, rw)
    model_plain: GAT (LCP, RW)
    value: 0.652
    std: 0.018
    paper_value: 0.652
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 122
    true_value: 0.652
    true_std: 0.018
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.652
    sort_std: 0.018
    is_best: false
  - model: GAT (LCP, LA)
    model_key: gat (lcp, la)
    model_plain: GAT (LCP, LA)
    value: 0.643
    std: 0.012
    paper_value: 0.643
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 127
    true_value: 0.643
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.643
    sort_std: 0.012
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.534
    std: 0.008
    paper_value: 0.534
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 148
    true_value: 0.534
    true_std: 0.008
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.534
    sort_std: 0.008
    is_best: false
  - model: GAT (LA) [BORF]
    model_key: gat (la) [borf]
    model_plain: GAT (LA) [BORF]
    value: 0.529
    std: 0.012
    paper_value: 0.529
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 149
    true_value: 0.529
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.529
    sort_std: 0.012
    is_best: false
  - model: GAT (RW) [BORF]
    model_key: gat (rw) [borf]
    model_plain: GAT (RW) [BORF]
    value: 0.521
    std: 0.009
    paper_value: 0.521
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 150
    true_value: 0.521
    true_std: 0.009
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.521
    sort_std: 0.009
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.512
    std: 0.01
    paper_value: 0.512
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 151
    true_value: 0.512
    true_std: 0.01
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.512
    sort_std: 0.01
    is_best: false
  - model: GAT (SUB)
    model_key: gat (sub)
    model_plain: GAT (SUB)
    value: 0.509
    std: 0.013
    paper_value: 0.509
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 152
    true_value: 0.509
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.509
    sort_std: 0.013
    is_best: false
  - model: GAT (SUB, LA)
    model_key: gat (sub, la)
    model_plain: GAT (SUB, LA)
    value: 0.504
    std: 0.016
    paper_value: 0.504
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 153
    true_value: 0.504
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.504
    sort_std: 0.016
    is_best: false
  - model: GAT (RW)
    model_key: gat (rw)
    model_plain: GAT (RW)
    value: 0.497
    std: 0.013
    paper_value: 0.497
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 159
    true_value: 0.497
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.497
    sort_std: 0.013
    is_best: false
  - model: GAT (LA)
    model_key: gat (la)
    model_plain: GAT (LA)
    value: 0.491
    std: 0.017
    paper_value: 0.491
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 162
    true_value: 0.491
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.491
    sort_std: 0.017
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.481
    std: 0.01
    paper_value: 0.481
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 164
    true_value: 0.481
    true_std: 0.01
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.481
    sort_std: 0.01
    is_best: false
  - model: GAT (SUB, RW)
    model_key: gat (sub, rw)
    model_plain: GAT (SUB, RW)
    value: 0.48
    std: 0.015
    paper_value: 0.48
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 165
    true_value: 0.48
    true_std: 0.015
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48
    sort_std: 0.015
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.478
    std: 0.012
    paper_value: 0.478
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 166
    true_value: 0.478
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.478
    sort_std: 0.012
    is_best: false
  - model: GAT (NO) [BORF]
    model_key: gat (no) [borf]
    model_plain: GAT (NO) [BORF]
    value: 0.471
    std: 0.016
    paper_value: 0.471
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 167
    true_value: 0.471
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.471
    sort_std: 0.016
    is_best: false
  - model: GAT (NO)
    model_key: gat (no)
    model_plain: GAT (NO)
    value: 0.47
    std: 0.014
    paper_value: 0.47
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 168
    true_value: 0.47
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.47
    sort_std: 0.014
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: GCN (LCP, RW)
    model_key: gcn (lcp, rw)
    model_plain: GCN (LCP, RW)
    value: 0.824
    std: 0.018
    paper_value: 0.824
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 83
    true_value: 0.824
    true_std: 0.018
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.824
    sort_std: 0.018
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.821
    std: 0.038
    paper_value: 0.821
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 87
    true_value: 0.821
    true_std: 0.038
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.821
    sort_std: 0.038
    is_best: false
  - model: GAT (LCP)
    model_key: gat (lcp)
    model_plain: GAT (LCP)
    value: 0.82
    std: 0.019
    paper_value: 0.82
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 90
    true_value: 0.82
    true_std: 0.019
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.82
    sort_std: 0.019
    is_best: false
  - model: GCN (SUB, RW)
    model_key: gcn (sub, rw)
    model_plain: GCN (SUB, RW)
    value: 0.812
    std: 0.024
    paper_value: 0.812
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 93
    true_value: 0.812
    true_std: 0.024
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.024
    is_best: false
  - model: GAT (LCP, RW)
    model_key: gat (lcp, rw)
    model_plain: GAT (LCP, RW)
    value: 0.812
    std: 0.024
    paper_value: 0.812
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 94
    true_value: 0.812
    true_std: 0.024
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.024
    is_best: false
  - model: GAT (LCP, LA)
    model_key: gat (lcp, la)
    model_plain: GAT (LCP, LA)
    value: 0.81
    std: 0.027
    paper_value: 0.81
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 96
    true_value: 0.81
    true_std: 0.027
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: 0.027
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.795
    std: 0.029
    paper_value: 0.795
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 109
    true_value: 0.795
    true_std: 0.029
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.029
    is_best: false
  - model: GCN (SUB, LA)
    model_key: gcn (sub, la)
    model_plain: GCN (SUB, LA)
    value: 0.793
    std: 0.019
    paper_value: 0.793
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 110
    true_value: 0.793
    true_std: 0.019
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.019
    is_best: false
  - model: GCN (LCP, LA)
    model_key: gcn (lcp, la)
    model_plain: GCN (LCP, LA)
    value: 0.792
    std: 0.019
    paper_value: 0.792
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 112
    true_value: 0.792
    true_std: 0.019
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.019
    is_best: false
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.79
    std: 0.029
    paper_value: 0.79
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 116
    true_value: 0.79
    true_std: 0.029
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79
    sort_std: 0.029
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.76
    std: 0.027
    paper_value: 0.76
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 134
    true_value: 0.76
    true_std: 0.027
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.027
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.74
    std: 0.014
    paper_value: 0.74
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 141
    true_value: 0.74
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.014
    is_best: false
  - model: GAT (SUB, LA)
    model_key: gat (sub, la)
    model_plain: GAT (SUB, LA)
    value: 0.725
    std: 0.029
    paper_value: 0.725
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 149
    true_value: 0.725
    true_std: 0.029
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.029
    is_best: false
  - model: GAT (SUB)
    model_key: gat (sub)
    model_plain: GAT (SUB)
    value: 0.724
    std: 0.027
    paper_value: 0.724
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 150
    true_value: 0.724
    true_std: 0.027
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.724
    sort_std: 0.027
    is_best: false
  - model: GAT (SUB, RW)
    model_key: gat (sub, rw)
    model_plain: GAT (SUB, RW)
    value: 0.712
    std: 0.028
    paper_value: 0.712
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 153
    true_value: 0.712
    true_std: 0.028
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.712
    sort_std: 0.028
    is_best: false
  - model: GAT (LA)
    model_key: gat (la)
    model_plain: GAT (LA)
    value: 0.71
    std: 0.026
    paper_value: 0.71
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 155
    true_value: 0.71
    true_std: 0.026
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.026
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.708
    std: 0.017
    paper_value: 0.708
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 157
    true_value: 0.708
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: 0.017
    is_best: false
  - model: GAT (RW)
    model_key: gat (rw)
    model_plain: GAT (RW)
    value: 0.708
    std: 0.024
    paper_value: 0.708
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 158
    true_value: 0.708
    true_std: 0.024
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: 0.024
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.69
    std: 0.028
    paper_value: 0.69
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 162
    true_value: 0.69
    true_std: 0.028
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.028
    is_best: false
  - model: GAT (NO)
    model_key: gat (no)
    model_plain: GAT (NO)
    value: 0.685
    std: 0.027
    paper_value: 0.685
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 164
    true_value: 0.685
    true_std: 0.027
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.685
    sort_std: 0.027
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.675
    std: 0.027
    paper_value: 0.675
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 166
    true_value: 0.675
    true_std: 0.027
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.675
    sort_std: 0.027
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.67
    std: 0.032
    paper_value: 0.67
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 167
    true_value: 0.67
    true_std: 0.032
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67
    sort_std: 0.032
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.627
    std: 0.021
    paper_value: 0.627
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 169
    true_value: 0.627
    true_std: 0.021
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.627
    sort_std: 0.021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: GAT (LCP, RW)
    model_key: gat (lcp, rw)
    model_plain: GAT (LCP, RW)
    value: 0.794
    std: 0.017
    paper_value: 0.794
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 7
    true_value: 0.794
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.017
    is_best: true
  - model: GAT (LCP, LA)
    model_key: gat (lcp, la)
    model_plain: GAT (LCP, LA)
    value: 0.787
    std: 0.016
    paper_value: 0.787
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 9
    true_value: 0.787
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.787
    sort_std: 0.016
    is_best: false
  - model: GAT (LCP)
    model_key: gat (lcp)
    model_plain: GAT (LCP)
    value: 0.785
    std: 0.014
    paper_value: 0.785
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 10
    true_value: 0.785
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.014
    is_best: false
  - model: GCN (LCP, RW)
    model_key: gcn (lcp, rw)
    model_plain: GCN (LCP, RW)
    value: 0.762
    std: 0.014
    paper_value: 0.762
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 35
    true_value: 0.762
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.014
    is_best: false
  - model: GAT (SUB, LA)
    model_key: gat (sub, la)
    model_plain: GAT (SUB, LA)
    value: 0.76
    std: 0.016
    paper_value: 0.76
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 42
    true_value: 0.76
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.016
    is_best: false
  - model: GAT (SUB, RW)
    model_key: gat (sub, rw)
    model_plain: GAT (SUB, RW)
    value: 0.758
    std: 0.017
    paper_value: 0.758
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 44
    true_value: 0.758
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.017
    is_best: false
  - model: GAT (SUB)
    model_key: gat (sub)
    model_plain: GAT (SUB)
    value: 0.757
    std: 0.015
    paper_value: 0.757
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 46
    true_value: 0.757
    true_std: 0.015
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.757
    sort_std: 0.015
    is_best: false
  - model: GCN (LCP, LA)
    model_key: gcn (lcp, la)
    model_plain: GCN (LCP, LA)
    value: 0.757
    std: 0.012
    paper_value: 0.757
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 47
    true_value: 0.757
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.757
    sort_std: 0.012
    is_best: false
  - model: GAT (LA)
    model_key: gat (la)
    model_plain: GAT (LA)
    value: 0.742
    std: 0.013
    paper_value: 0.742
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 84
    true_value: 0.742
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.013
    is_best: false
  - model: GCN (SUB, LA)
    model_key: gcn (sub, la)
    model_plain: GCN (SUB, LA)
    value: 0.734
    std: 0.011
    paper_value: 0.734
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 106
    true_value: 0.734
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.734
    sort_std: 0.011
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.732
    std: 0.012
    paper_value: 0.732
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 111
    true_value: 0.732
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: 0.012
    is_best: false
  - model: GAT (RW)
    model_key: gat (rw)
    model_plain: GAT (RW)
    value: 0.73
    std: 0.012
    paper_value: 0.73
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 120
    true_value: 0.73
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.012
    is_best: false
  - model: GAT (NO)
    model_key: gat (no)
    model_plain: GAT (NO)
    value: 0.726
    std: 0.012
    paper_value: 0.726
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 133
    true_value: 0.726
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.012
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.723
    std: 0.014
    paper_value: 0.723
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 141
    true_value: 0.723
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.014
    is_best: false
  - model: GCN (SUB, RW)
    model_key: gcn (sub, rw)
    model_plain: GCN (SUB, RW)
    value: 0.719
    std: 0.012
    paper_value: 0.719
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 149
    true_value: 0.719
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: 0.012
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.718
    std: 0.012
    paper_value: 0.718
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 151
    true_value: 0.718
    true_std: 0.012
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.012
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.715
    std: 0.011
    paper_value: 0.715
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 156
    true_value: 0.715
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.011
    is_best: false
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.709
    std: 0.016
    paper_value: 0.709
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 168
    true_value: 0.709
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.709
    sort_std: 0.016
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.694
    std: 0.011
    paper_value: 0.694
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 184
    true_value: 0.694
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.694
    sort_std: 0.011
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.659
    std: 0.007
    paper_value: 0.659
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 194
    true_value: 0.659
    true_std: 0.007
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: 0.007
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.611
    std: 0.008
    paper_value: 0.611
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 198
    true_value: 0.611
    true_std: 0.008
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 198
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.611
    sort_std: 0.008
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.596
    std: 0.009
    paper_value: 0.596
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 199
    true_value: 0.596
    true_std: 0.009
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 199
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.596
    sort_std: 0.009
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.559
    std: 0.011
    paper_value: 0.559
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 202
    true_value: 0.559
    true_std: 0.011
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 202
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.559
    sort_std: 0.011
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
    date: '2025-01-29'
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
    date: '2025-01-29'
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
    date: '2025-01-29'
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.496
    std: 0.022
    paper_value: 0.496
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.496
    sort_std: 0.022
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.488
    std: 0.016
    paper_value: 0.488
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.488
    sort_std: 0.016
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.48
    std: 0.021
    paper_value: 0.48
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.48
    sort_std: 0.021
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.473
    std: 0.024
    paper_value: 0.473
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.473
    sort_std: 0.024
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.462
    std: 0.022
    paper_value: 0.462
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.462
    sort_std: 0.022
    is_best: false
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.444
    std: 0.022
    paper_value: 0.444
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.444
    sort_std: 0.022
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.435
    std: 0.018
    paper_value: 0.435
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.435
    sort_std: 0.018
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.432
    std: 0.021
    paper_value: 0.432
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.432
    sort_std: 0.021
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.426
    std: 0.02
    paper_value: 0.426
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.426
    sort_std: 0.02
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.407
    std: 0.02
    paper_value: 0.407
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.407
    sort_std: 0.02
    is_best: false
  metric: AP
  higher_is_better: true
- &id004
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
  - model: GCN (LCP)
    model_key: gcn (lcp)
    model_plain: GCN (LCP)
    value: 0.352
    std: 0.017
    paper_value: 0.352
    paper_std: 0.017
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 309
    true_value: 0.352
    true_std: 0.017
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 309
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.352
    sort_std: 0.017
    is_best: false
  - model: GCN (RW)
    model_key: gcn (rw)
    model_plain: GCN (RW)
    value: 0.354
    std: 0.019
    paper_value: 0.354
    paper_std: 0.019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 311
    true_value: 0.354
    true_std: 0.019
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 311
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.354
    sort_std: 0.019
    is_best: false
  - model: GCN (LA)
    model_key: gcn (la)
    model_plain: GCN (LA)
    value: 0.356
    std: 0.014
    paper_value: 0.356
    paper_std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 316
    true_value: 0.356
    true_std: 0.014
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 316
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.356
    sort_std: 0.014
    is_best: false
  - model: GCN (SUB)
    model_key: gcn (sub)
    model_plain: GCN (SUB)
    value: 0.36
    std: 0.016
    paper_value: 0.36
    paper_std: 0.016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 319
    true_value: 0.36
    true_std: 0.016
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 319
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.36
    sort_std: 0.016
    is_best: false
  - model: GIN (LCP)
    model_key: gin (lcp)
    model_plain: GIN (LCP)
    value: 0.361
    std: 0.022
    paper_value: 0.361
    paper_std: 0.022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 320
    true_value: 0.361
    true_std: 0.022
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 320
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.361
    sort_std: 0.022
    is_best: false
  - model: GIN (LA)
    model_key: gin (la)
    model_plain: GIN (LA)
    value: 0.364
    std: 0.021
    paper_value: 0.364
    paper_std: 0.021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 322
    true_value: 0.364
    true_std: 0.021
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 322
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.364
    sort_std: 0.021
    is_best: false
  - model: GIN (RW)
    model_key: gin (rw)
    model_plain: GIN (RW)
    value: 0.368
    std: 0.023
    paper_value: 0.368
    paper_std: 0.023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 325
    true_value: 0.368
    true_std: 0.023
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 325
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.368
    sort_std: 0.023
    is_best: false
  - model: GIN (SUB)
    model_key: gin (sub)
    model_plain: GIN (SUB)
    value: 0.375
    std: 0.02
    paper_value: 0.375
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 327
    true_value: 0.375
    true_std: 0.02
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 327
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.375
    sort_std: 0.02
    is_best: false
  - model: GCN (NO)
    model_key: gcn (no)
    model_plain: GCN (NO)
    value: 0.379
    std: 0.013
    paper_value: 0.379
    paper_std: 0.013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 328
    true_value: 0.379
    true_std: 0.013
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 328
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.379
    sort_std: 0.013
    is_best: false
  - model: GIN (NO)
    model_key: gin (no)
    model_plain: GIN (NO)
    value: 0.387
    std: 0.023
    paper_value: 0.387
    paper_std: 0.023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 329
    true_value: 0.387
    true_std: 0.023
    value_gap_source_arxiv: '2311.14864'
    value_gap_source_title: Effective Structural Encodings via Local Curvature Profiles
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 329
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.387
    sort_std: 0.023
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
  - *id004
- benchmark: TU Dortmund
  datasets:
  - *id005
  - *id006
  - *id007
  - *id008
main_figure: /figures/2311.14864/main_figure.png
---

