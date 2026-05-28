---
title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
arxiv_id: '2601.07419'
source_url: ''
authors: []
published_date: Jan 2026
published_date_iso: 2026-01
abstract: Over-smoothing and over-squashing have been extensively studied in the literature
  on Graph Neural Networks (GNNs) over the past years. We challenge this prevailing
  focus in GNN research, arguing that these phenomena are less critical for practical
  applications than assumed. We suggest that performance decreases often stem from
  uninformative receptive fields rather than over-smoothing. We support this position
  with extensive experiments on several standard benchmark datasets, demonstrating
  that accuracy and over-smoothing are mostly uncorrelated and that optimal model
  depths remain small even with mitigation techniques, thus highlighting the negligible
  role of over-smoothing. Similarly, we challenge that over-squashing is always detrimental
  in practical applications. Instead, we posit that the distribution of relevant information
  over the graph frequently factorises and is often localised within a small k-hop
  neighbourhood, questioning the necessity of jointly observing entire receptive fields
  or engaging in an extensive search for long-range interactions. The results of our
  experiments show that architectural interventions designed to mitigate over-squashing
  fail to yield significant performance gains. This position paper advocates for a
  paradigm shift in theoretical research, urging a diligent analysis of learning tasks
  and datasets using statistics that measure the underlying distribution of label-relevant
  information to better understand their localisation and factorisation.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN
- GIN
- G²
- G² (GATv2)
- EGP (GCN)
- GCN + SDRF
- EGP (GIN)
- EGP (GraphSAGE)
- GIN-SDRF-R
mrr: 0.2
adjusted_mrr: 0.0667
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- TU Dortmund
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id005
  dataset: Amazon-Computers
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9409
    std: 0.0037
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
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9409
    sort_std: 0.0037
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.777
    std: 0.037000000000000005
    paper_value: 0.777
    paper_std: 0.037000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 2
    true_value: 0.9399
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16289999999999993
    value_note: ''
    paper_rank: 39
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.9399
    sort_std: 0.0012
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9378
    std: 0.001
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
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9378
    sort_std: 0.001
    is_best: true
  - model: GCN* (-) Dropout
    model_key: gcn* (-) dropout
    model_plain: GCN* (-) Dropout
    value: 0.9378
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9378
    sort_std: 0.0026
    is_best: true
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.813
    std: 0.016
    paper_value: 0.813
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 36
    true_value: 0.813
    true_std: 0.016
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.813
    sort_std: 0.016
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.7609999999999999
    std: 0.026000000000000002
    paper_value: 0.7609999999999999
    paper_std: 0.026000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 41
    true_value: 0.7609999999999999
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7609999999999999
    sort_std: 0.026000000000000002
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
    value: 0.966
    std: 0.0033
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
    global_rank: 3
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.86
    std: 0.045
    paper_value: 0.86
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 6
    true_value: 0.961
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10099999999999998
    value_note: ''
    paper_rank: 44
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.961
    sort_std: 0.0046
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.858
    std: 0.040999999999999995
    paper_value: 0.858
    paper_std: 0.040999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 45
    true_value: 0.858
    true_std: 0.040999999999999995
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.858
    sort_std: 0.040999999999999995
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.82
    std: 0.057
    paper_value: 0.82
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 47
    true_value: 0.82
    true_std: 0.057
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.82
    sort_std: 0.057
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.779
    std: 0.131
    paper_value: 0.779
    paper_std: 0.131
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 49
    true_value: 0.779
    true_std: 0.131
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.131
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
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.7759999999999999
    std: 0.002
    paper_value: 0.7759999999999999
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 4
    true_value: 0.8183
    true_std: 0.0178
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042300000000000115
    value_note: ''
    paper_rank: 40
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.8183
    sort_std: 0.0178
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.755
    std: 0.008
    paper_value: 0.755
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05889999999999995
    value_note: ''
    paper_rank: 76
    rank_delta: 64
    rank_delta_abs: 64
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.755
    std: 0.004
    paper_value: 0.755
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 34
    true_value: 0.7923
    true_std: 0.0053
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0373
    value_note: ''
    paper_rank: 76
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.7923
    sort_std: 0.0053
    is_best: false
  - model: EGP (GraphSAGE)
    model_key: egp (graphsage)
    model_plain: EGP (GraphSAGE)
    value: 0.768
    std: 0.003
    paper_value: 0.768
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 53
    true_value: 0.768
    true_std: 0.003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.003
    is_best: false
  - model: G²
    model_key: g²
    model_plain: G²
    value: 0.765
    std: 0.004
    paper_value: 0.765
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 57
    true_value: 0.765
    true_std: 0.004
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.765
    sort_std: 0.004
    is_best: false
  - model: G² (GATv2)
    model_key: g² (gatv2)
    model_plain: G² (GATv2)
    value: 0.763
    std: 0.006999999999999999
    paper_value: 0.763
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 60
    true_value: 0.763
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.006999999999999999
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.75
    std: 0.006
    paper_value: 0.75
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 88
    true_value: 0.75
    true_std: 0.006
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.006
    is_best: false
  - model: GraphSAGE + Pairnorm
    model_key: graphsage + pairnorm
    model_plain: GraphSAGE + Pairnorm
    value: 0.7020000000000001
    std: 0.01
    paper_value: 0.7020000000000001
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 137
    true_value: 0.7020000000000001
    true_std: 0.01
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7020000000000001
    sort_std: 0.01
    is_best: false
  - model: GATv2 + Pairnorm
    model_key: gatv2 + pairnorm
    model_plain: GATv2 + Pairnorm
    value: 0.684
    std: 0.008
    paper_value: 0.684
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 147
    true_value: 0.684
    true_std: 0.008
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.684
    sort_std: 0.008
    is_best: false
  - model: GCN + Pairnorm
    model_key: gcn + pairnorm
    model_plain: GCN + Pairnorm
    value: 0.6829999999999999
    std: 0.016
    paper_value: 0.6829999999999999
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 149
    true_value: 0.6829999999999999
    true_std: 0.016
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6829999999999999
    sort_std: 0.016
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
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.763
    std: 0.023
    paper_value: 0.763
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 16
    true_value: 0.8893
    true_std: 0.0137
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12629999999999997
    value_note: ''
    paper_rank: 189
    rank_delta: 173
    rank_delta_abs: 173
    rank_delta_direction: worse
    sort_value: 0.8893
    sort_std: 0.0137
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7709999999999999
    std: 0.033
    paper_value: 0.7709999999999999
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10680000000000012
    value_note: ''
    paper_rank: 183
    rank_delta: 135
    rank_delta_abs: 135
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.821
    std: 0.051
    paper_value: 0.821
    paper_std: 0.051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 71
    true_value: 0.8690000000000001
    true_std: 0.0104
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.048000000000000154
    value_note: global 0.8690 within std
    paper_rank: 141
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.8690000000000001
    sort_std: 0.0104
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.755
    std: 0.027999999999999997
    paper_value: 0.755
    paper_std: 0.027999999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 119
    true_value: 0.835
    true_std: 0.005
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07999999999999996
    value_note: ''
    paper_rank: 195
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.835
    sort_std: 0.005
    is_best: false
  - model: G2-GCN (GraphSAGE)
    model_key: g2-gcn (graphsage)
    model_plain: G2-GCN (GraphSAGE)
    value: 0.7859999999999999
    std: 0.05
    paper_value: 0.7859999999999999
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 170
    true_value: 0.7859999999999999
    true_std: 0.05
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7859999999999999
    sort_std: 0.05
    is_best: false
  - model: G2-GCN (GATv2)
    model_key: g2-gcn (gatv2)
    model_plain: G2-GCN (GATv2)
    value: 0.785
    std: 0.06
    paper_value: 0.785
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 171
    true_value: 0.785
    true_std: 0.06
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.06
    is_best: false
  - model: G2-GCN
    model_key: g2-gcn
    model_plain: G2-GCN
    value: 0.7559999999999999
    std: 0.011000000000000001
    paper_value: 0.7559999999999999
    paper_std: 0.011000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 195
    true_value: 0.7559999999999999
    true_std: 0.011000000000000001
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 195
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7559999999999999
    sort_std: 0.011000000000000001
    is_best: false
  - model: GraphSAGE + Pairnorm
    model_key: graphsage + pairnorm
    model_plain: GraphSAGE + Pairnorm
    value: 0.735
    std: 0.049
    paper_value: 0.735
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 211
    true_value: 0.735
    true_std: 0.049
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 211
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.049
    is_best: false
  - model: GATv2 + Pairnorm
    model_key: gatv2 + pairnorm
    model_plain: GATv2 + Pairnorm
    value: 0.6970000000000001
    std: 0.015
    paper_value: 0.6970000000000001
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 246
    true_value: 0.6970000000000001
    true_std: 0.015
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 246
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6970000000000001
    sort_std: 0.015
    is_best: false
  - model: GCN + Pairnorm
    model_key: gcn + pairnorm
    model_plain: GCN + Pairnorm
    value: 0.696
    std: 0.055
    paper_value: 0.696
    paper_std: 0.055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 247
    true_value: 0.696
    true_std: 0.055
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 247
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.696
    sort_std: 0.055
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.606
    std: 0.034
    paper_value: 0.606
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 13
    true_value: 0.606
    true_std: 0.034
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.034
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.584
    std: 0.021
    paper_value: 0.584
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 15
    true_value: 0.584
    true_std: 0.021
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.584
    sort_std: 0.021
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.503
    std: 0.026000000000000002
    paper_value: 0.503
    paper_std: 0.026000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 22
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.503
    std: 0.026000000000000002
    paper_value: 0.503
    paper_std: 0.026000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 23
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.502
    std: 0.027000000000000003
    paper_value: 0.502
    paper_std: 0.027000000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 24
    true_value: 0.502
    true_std: 0.027000000000000003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.502
    sort_std: 0.027000000000000003
    is_best: false
  - model: EGP (GraphSAGE)
    model_key: egp (graphsage)
    model_plain: EGP (GraphSAGE)
    value: 0.42700000000000005
    std: 0.033
    paper_value: 0.42700000000000005
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 41
    true_value: 0.42700000000000005
    true_std: 0.033
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.42700000000000005
    sort_std: 0.033
    is_best: false
  - model: GraphSAGE + SDRF
    model_key: graphsage + sdrf
    model_plain: GraphSAGE + SDRF
    value: 0.387
    std: 0.022000000000000002
    paper_value: 0.387
    paper_std: 0.022000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 53
    true_value: 0.387
    true_std: 0.022000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.387
    sort_std: 0.022000000000000002
    is_best: false
  - model: G² (GATv2)
    model_key: g² (gatv2)
    model_plain: G² (GATv2)
    value: 0.385
    std: 0.022000000000000002
    paper_value: 0.385
    paper_std: 0.022000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 54
    true_value: 0.385
    true_std: 0.022000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.385
    sort_std: 0.022000000000000002
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.377
    std: 0.027999999999999997
    paper_value: 0.377
    paper_std: 0.027999999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 56
    true_value: 0.377
    true_std: 0.027999999999999997
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.377
    sort_std: 0.027999999999999997
    is_best: false
  - model: GATv2 + BORF
    model_key: gatv2 + borf
    model_plain: GATv2 + BORF
    value: 0.374
    std: 0.040999999999999995
    paper_value: 0.374
    paper_std: 0.040999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 58
    true_value: 0.374
    true_std: 0.040999999999999995
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.374
    sort_std: 0.040999999999999995
    is_best: false
  - model: GATv2 + SDRF
    model_key: gatv2 + sdrf
    model_plain: GATv2 + SDRF
    value: 0.353
    std: 0.031
    paper_value: 0.353
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 63
    true_value: 0.353
    true_std: 0.031
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.353
    sort_std: 0.031
    is_best: false
  - model: GraphSAGE + BORF
    model_key: graphsage + borf
    model_plain: GraphSAGE + BORF
    value: 0.31
    std: 0.025
    paper_value: 0.31
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 85
    true_value: 0.31
    true_std: 0.025
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31
    sort_std: 0.025
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.9109999999999999
    std: 0.013999999999999999
    paper_value: 0.9109999999999999
    paper_std: 0.013999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 9
    true_value: 0.9109999999999999
    true_std: 0.013999999999999999
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9109999999999999
    sort_std: 0.013999999999999999
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.904
    std: 0.043
    paper_value: 0.904
    paper_std: 0.043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 16
    true_value: 0.904
    true_std: 0.043
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.904
    sort_std: 0.043
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.895
    std: 0.026000000000000002
    paper_value: 0.895
    paper_std: 0.026000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 26
    true_value: 0.895
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.895
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.895
    std: 0.026000000000000002
    paper_value: 0.895
    paper_std: 0.026000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 27
    true_value: 0.895
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.895
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.882
    std: 0.037000000000000005
    paper_value: 0.882
    paper_std: 0.037000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.01200000000000001
    value_note: global 0.8940 within std
    paper_rank: 40
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.889
    std: 0.015
    paper_value: 0.889
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 35
    true_value: 0.889
    true_std: 0.015
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.889
    sort_std: 0.015
    is_best: false
  - model: EGP (GraphSAGE)
    model_key: egp (graphsage)
    model_plain: EGP (GraphSAGE)
    value: 0.8859999999999999
    std: 0.012
    paper_value: 0.8859999999999999
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 37
    true_value: 0.8859999999999999
    true_std: 0.012
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8859999999999999
    sort_std: 0.012
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.8809999999999999
    std: 0.027000000000000003
    paper_value: 0.8809999999999999
    paper_std: 0.027000000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 42
    true_value: 0.8809999999999999
    true_std: 0.027000000000000003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8809999999999999
    sort_std: 0.027000000000000003
    is_best: false
  - model: GraphSAGE + SDRF
    model_key: graphsage + sdrf
    model_plain: GraphSAGE + SDRF
    value: 0.8809999999999999
    std: 0.03
    paper_value: 0.8809999999999999
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 43
    true_value: 0.8809999999999999
    true_std: 0.03
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8809999999999999
    sort_std: 0.03
    is_best: false
  - model: GATv2 + SDRF
    model_key: gatv2 + sdrf
    model_plain: GATv2 + SDRF
    value: 0.872
    std: 0.027000000000000003
    paper_value: 0.872
    paper_std: 0.027000000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 47
    true_value: 0.872
    true_std: 0.027000000000000003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.872
    sort_std: 0.027000000000000003
    is_best: false
  - model: G² (GATv2)
    model_key: g² (gatv2)
    model_plain: G² (GATv2)
    value: 0.868
    std: 0.039
    paper_value: 0.868
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 53
    true_value: 0.868
    true_std: 0.039
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.868
    sort_std: 0.039
    is_best: false
  - model: GraphSAGE + BORF
    model_key: graphsage + borf
    model_plain: GraphSAGE + BORF
    value: 0.856
    std: 0.024
    paper_value: 0.856
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 60
    true_value: 0.856
    true_std: 0.024
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.856
    sort_std: 0.024
    is_best: false
  - model: GATv2 + BORF
    model_key: gatv2 + borf
    model_plain: GATv2 + BORF
    value: 0.828
    std: 0.033
    paper_value: 0.828
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 81
    true_value: 0.828
    true_std: 0.033
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.828
    sort_std: 0.033
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.665
    std: 0.022000000000000002
    paper_value: 0.665
    paper_std: 0.022000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09699999999999998
    value_note: ''
    paper_rank: 192
    rank_delta: 160
    rank_delta_abs: 160
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.701
    std: 0.005
    paper_value: 0.701
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 43
    true_value: 0.759
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05800000000000005
    value_note: ''
    paper_rank: 176
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.759
    sort_std: 0.032
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.726
    std: 0.019
    paper_value: 0.726
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 83
    true_value: 0.742
    true_std: 0.008
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.016000000000000014
    value_note: global 0.7420 within std
    paper_rank: 132
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.008
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.7290000000000001
    std: 0.018000000000000002
    paper_value: 0.7290000000000001
    paper_std: 0.018000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 124
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.7290000000000001
    std: 0.018000000000000002
    paper_value: 0.7290000000000001
    paper_std: 0.018000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 125
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.6809999999999999
    std: 0.086
    paper_value: 0.6809999999999999
    paper_std: 0.086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 169
    true_value: 0.70848
    true_std: 0.01568
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02748000000000006
    value_note: global 0.7085 within std
    paper_rank: 188
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.70848
    sort_std: 0.01568
    is_best: false
  - model: GraphSAGE + BORF
    model_key: graphsage + borf
    model_plain: GraphSAGE + BORF
    value: 0.703
    std: 0.009000000000000001
    paper_value: 0.703
    paper_std: 0.009000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 176
    true_value: 0.703
    true_std: 0.009000000000000001
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.703
    sort_std: 0.009000000000000001
    is_best: false
  - model: G² (GATv2)
    model_key: g² (gatv2)
    model_plain: G² (GATv2)
    value: 0.701
    std: 0.019
    paper_value: 0.701
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 177
    true_value: 0.701
    true_std: 0.019
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 177
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.019
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.6990000000000001
    std: 0.006999999999999999
    paper_value: 0.6990000000000001
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 179
    true_value: 0.6990000000000001
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 179
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6990000000000001
    sort_std: 0.006999999999999999
    is_best: false
  - model: GATv2 + SDRF
    model_key: gatv2 + sdrf
    model_plain: GATv2 + SDRF
    value: 0.698
    std: 0.006999999999999999
    paper_value: 0.698
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 180
    true_value: 0.698
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.698
    sort_std: 0.006999999999999999
    is_best: false
  - model: GraphSAGE + SDRF
    model_key: graphsage + sdrf
    model_plain: GraphSAGE + SDRF
    value: 0.6970000000000001
    std: 0.006
    paper_value: 0.6970000000000001
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 181
    true_value: 0.6970000000000001
    true_std: 0.006
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 181
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6970000000000001
    sort_std: 0.006
    is_best: false
  - model: GATv2 + BORF
    model_key: gatv2 + borf
    model_plain: GATv2 + BORF
    value: 0.6940000000000001
    std: 0.015
    paper_value: 0.6940000000000001
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 183
    true_value: 0.6940000000000001
    true_std: 0.015
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 183
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6940000000000001
    sort_std: 0.015
    is_best: false
  - model: EGP (GraphSAGE)
    model_key: egp (graphsage)
    model_plain: EGP (GraphSAGE)
    value: 0.6759999999999999
    std: 0.002
    paper_value: 0.6759999999999999
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 189
    true_value: 0.6759999999999999
    true_std: 0.002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6759999999999999
    sort_std: 0.002
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.607
    std: 0.01
    paper_value: 0.607
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 41
    true_value: 0.7059
    true_std: 0.0089
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09889999999999999
    value_note: ''
    paper_rank: 239
    rank_delta: 198
    rank_delta_abs: 198
    rank_delta_direction: worse
    sort_value: 0.7059
    sort_std: 0.0089
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.5670000000000001
    std: 0.006
    paper_value: 0.5670000000000001
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 236
    true_value: 0.6131
    true_std: 0.0084
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04609999999999992
    value_note: ''
    paper_rank: 281
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.6131
    sort_std: 0.0084
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.597
    std: 0.006
    paper_value: 0.597
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 251
    true_value: 0.5993999999999999
    true_std: 0.0037
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0023999999999999577
    value_note: global 0.5994 within std
    paper_rank: 254
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.5993999999999999
    sort_std: 0.0037
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.5670000000000001
    std: 0.006
    paper_value: 0.5670000000000001
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 257
    true_value: 0.5947
    true_std: 0.0126
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.027699999999999947
    value_note: ''
    paper_rank: 281
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.5947
    sort_std: 0.0126
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.429
    std: 0.006
    paper_value: 0.429
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 308
    true_value: 0.429
    true_std: 0.006
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 308
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.429
    sort_std: 0.006
    is_best: false
  metric: AP
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
    value: 0.877
    std: 0.004
    paper_value: 0.877
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.045399999999999996
    value_note: ''
    paper_rank: 75
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8859999999999999
    std: 0.002
    paper_value: 0.8859999999999999
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 22
    true_value: 0.8998
    true_std: 0.0052
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013800000000000145
    value_note: ''
    paper_rank: 55
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.8998
    sort_std: 0.0052
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.883
    std: 0.004
    paper_value: 0.883
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 54
    true_value: 0.8864
    true_std: 0.003
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0033999999999999586
    value_note: global 0.8864 within std
    paper_rank: 60
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8864
    sort_std: 0.003
    is_best: false
  - model: G2-GCN (GATv2)
    model_key: g2-gcn (gatv2)
    model_plain: G2-GCN (GATv2)
    value: 0.882
    std: 0.003
    paper_value: 0.882
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 69
    true_value: 0.882
    true_std: 0.003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.882
    sort_std: 0.003
    is_best: false
  - model: GCN + Pairnorm
    model_key: gcn + pairnorm
    model_plain: GCN + Pairnorm
    value: 0.879
    std: 0.004
    paper_value: 0.879
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 73
    true_value: 0.879
    true_std: 0.004
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.879
    sort_std: 0.004
    is_best: false
  - model: G^2-GCN
    model_key: g^2-gcn
    model_plain: G^2-GCN
    value: 0.8759999999999999
    std: 0.011000000000000001
    paper_value: 0.8759999999999999
    paper_std: 0.011000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 79
    true_value: 0.8759999999999999
    true_std: 0.011000000000000001
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8759999999999999
    sort_std: 0.011000000000000001
    is_best: false
  - model: GATv2 + Pairnorm
    model_key: gatv2 + pairnorm
    model_plain: GATv2 + Pairnorm
    value: 0.872
    std: 0.005
    paper_value: 0.872
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 88
    true_value: 0.872
    true_std: 0.005
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.872
    sort_std: 0.005
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.867
    std: 0.008
    paper_value: 0.867
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 94
    true_value: 0.867
    true_std: 0.008
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.867
    sort_std: 0.008
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Roman-empire
  rows:
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9292
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9292
    sort_std: 0.0036
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9266
    std: 0.006
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
    sort_value: 0.9266
    sort_std: 0.006
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9262999999999999
    std: 0.005
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
    global_rank: 3
    sort_value: 0.9262999999999999
    sort_std: 0.005
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.415
    std: 0.006999999999999999
    paper_value: 0.415
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 19
    true_value: 0.9127
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4977
    value_note: ''
    paper_rank: 100
    rank_delta: 81
    rank_delta_abs: 81
    rank_delta_direction: worse
    sort_value: 0.9127
    sort_std: 0.002
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.419
    std: 0.002
    paper_value: 0.419
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 99
    true_value: 0.419
    true_std: 0.002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.419
    sort_std: 0.002
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.41600000000000004
    std: 0.006999999999999999
    paper_value: 0.41600000000000004
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 100
    true_value: 0.41600000000000004
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.41600000000000004
    sort_std: 0.006999999999999999
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.409
    std: 0.006999999999999999
    paper_value: 0.409
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 101
    true_value: 0.409
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.409
    sort_std: 0.006999999999999999
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
- benchmark: Heterophilic Graphs
  datasets:
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
- benchmark: TU Dortmund
  datasets:
  - *id008
  - *id009
  - *id010
main_figure: /figures/2601.07419/main_figure.png
---

