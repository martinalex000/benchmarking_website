---
title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
arxiv_id: '2602.02268'
source_url: ''
authors: []
published_date: Feb 2, 2026
published_date_iso: '2026-02-02'
published_venue: ''
abstract: 'Graph Transformers typically rely on explicit positional or structural
  encodings and dense global attention to incorporate graph topology. In this work,
  we show that neither is essential. We introduce HopFormer, a graph Transformer that
  injects structure exclusively through head-specific $n$-hop masked sparse attention,
  without the use of positional encodings or architectural modifications. This design
  provides explicit and interpretable control over receptive fields while enabling
  genuinely sparse attention whose computational cost scales linearly with mask sparsity.
  Through extensive experiments on both node-level and graph-level benchmarks, we
  demonstrate that our approach achieves competitive or superior performance across
  diverse graph structures. Our results further reveal that dense global attention
  is often unnecessary: on graphs with strong small-world properties, localized attention
  yields more stable and consistently high performance, while on graphs with weaker
  small-world effects, global attention offers diminishing returns. Together, these
  findings challenge prevailing assumptions in graph Transformer design and highlight
  sparsity-controlled attention as a principled and efficient alternative.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- HopFormer
mrr: 0.0115
adjusted_mrr: 0.0115
mrr_dataset_count: 14
benchmark_categories:
- Classic
- Heterophilic Graphs
- OGB
- LRGB
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id010
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
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.3736
    std: 0.0016
    paper_value: 0.3736
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 64
    true_value: 0.3736
    true_std: 0.0016
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3736
    sort_std: 0.0016
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Chameleon
  rows:
  - model: RUNG
    model_key: rung
    model_plain: RUNG
    value: 0.9773
    std: 0.0328
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9773
    sort_std: 0.0328
    is_best: true
  - model: DHGNN
    model_key: dhgnn
    model_plain: DHGNN
    value: 0.8011
    std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8011
    sort_std: 0.0173
    is_best: false
  - model: NDDGNN
    model_key: nddgnn
    model_plain: NDDGNN
    value: 0.7979
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7979
    sort_std: 0.0104
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 24
    true_value: 0.723
    true_std: null
    value_gap_source_arxiv: '2101.00797'
    value_gap_source_title: Beyond Low-frequency Information in Graph Convolutional
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2815
    value_note: ''
    paper_rank: 201
    rank_delta: 177
    rank_delta_abs: 177
    rank_delta_direction: worse
    sort_value: 0.723
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 61
    true_value: 0.673
    true_std: 0.022
    value_gap_source_arxiv: '2205.13700'
    value_gap_source_title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily
      with Edge Splitting'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21170000000000005
    value_note: ''
    paper_rank: 193
    rank_delta: 132
    rank_delta_abs: 132
    rank_delta_direction: worse
    sort_value: 0.673
    sort_std: 0.022
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 70
    true_value: 0.667
    true_std: 0.027
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17140000000000005
    value_note: ''
    paper_rank: 174
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.667
    sort_std: 0.027
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.5738
    std: 0.0278
    paper_value: 0.5738
    paper_std: 0.0278
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 129
    true_value: 0.5738
    true_std: 0.0278
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5738
    sort_std: 0.0278
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.5623
    std: 0.0089
    paper_value: 0.5623
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 134
    true_value: 0.5623
    true_std: 0.0089
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5623
    sort_std: 0.0089
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 140
    true_value: 0.5453
    true_std: 0.0136
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5453
    sort_std: 0.0136
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 160
    true_value: 0.5161
    true_std: 0.0068
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 162
    true_value: 0.5124
    true_std: 0.0057
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5124
    sort_std: 0.0057
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 165
    true_value: 0.508
    true_std: 0.001
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.508
    sort_std: 0.001
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 177
    true_value: 0.492
    true_std: 0.0045
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 177
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 179
    true_value: 0.4905
    true_std: 0.0092
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 179
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 184
    true_value: 0.4854
    true_std: 0.0058
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4854
    sort_std: 0.0058
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 188
    true_value: 0.4788
    true_std: 0.0058
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4788
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 190
    true_value: 0.4722
    true_std: 0.026
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4722
    sort_std: 0.026
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 216
    true_value: 0.4189
    true_std: 0.0267
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 216
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4189
    sort_std: 0.0267
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 230
    true_value: 0.4006
    true_std: 0.0055
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 230
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4006
    sort_std: 0.0055
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
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.685
    std: 0.0346
    paper_value: 0.685
    paper_std: 0.0346
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 555
    true_value: 0.685
    true_std: 0.0346
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 555
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.685
    sort_std: 0.0346
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 22
    true_value: 0.9004
    true_std: null
    value_gap_source_arxiv: '2401.09125'
    value_gap_source_title: arXiv:2401.09125
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1824
    value_note: ''
    paper_rank: 728
    rank_delta: 706
    rank_delta_abs: 706
    rank_delta_direction: worse
    sort_value: 0.9004
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 50
    true_value: 0.8904
    true_std: 0.015
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11909999999999998
    value_note: ''
    paper_rank: 636
    rank_delta: 586
    rank_delta_abs: 586
    rank_delta_direction: worse
    sort_value: 0.8904
    sort_std: 0.015
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 54
    true_value: 0.8897
    true_std: null
    value_gap_source_arxiv: '2605.24867'
    value_gap_source_title: 'Clustering as Reasoning: A $k$-Means Interpretation of
      Chain-of-Thought Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14370000000000005
    value_note: ''
    paper_rank: 679
    rank_delta: 625
    rank_delta_abs: 625
    rank_delta_direction: worse
    sort_value: 0.8897
    sort_std: null
    is_best: false
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 71
    true_value: 0.8856
    true_std: 0.0101
    value_gap_source_arxiv: '2410.12096'
    value_gap_source_title: Bridging Large Language Models and Graph Structure Learning
      Models for Robust Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1753
    value_note: ''
    paper_rank: 739
    rank_delta: 668
    rank_delta_abs: 668
    rank_delta_direction: worse
    sort_value: 0.8856
    sort_std: 0.0101
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 96
    true_value: 0.8819
    true_std: 0.006
    value_gap_source_arxiv: '2404.15354'
    value_gap_source_title: 'Polynomial Selection in Spectral Graph Neural Networks:
      An Error-Sum of Function Slices Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3936
    value_note: ''
    paper_rank: 899
    rank_delta: 803
    rank_delta_abs: 803
    rank_delta_direction: worse
    sort_value: 0.8819
    sort_std: 0.006
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 170
    true_value: 0.8661
    true_std: 0.0304
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10109999999999997
    value_note: ''
    paper_rank: 644
    rank_delta: 474
    rank_delta_abs: 474
    rank_delta_direction: worse
    sort_value: 0.8661
    sort_std: 0.0304
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 182
    true_value: 0.8624
    true_std: 0.0158
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09210000000000007
    value_note: ''
    paper_rank: 636
    rank_delta: 454
    rank_delta_abs: 454
    rank_delta_direction: worse
    sort_value: 0.8624
    sort_std: 0.0158
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 236
    true_value: 0.851
    true_std: 0.008
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.41869999999999996
    value_note: ''
    paper_rank: 918
    rank_delta: 682
    rank_delta_abs: 682
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.008
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 295
    true_value: 0.841
    true_std: 0.008
    value_gap_source_arxiv: '2503.12563'
    value_gap_source_title: 'Diffusion on Graph: Augmentation of Graph Structure for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22899999999999998
    value_note: ''
    paper_rank: 826
    rank_delta: 531
    rank_delta_abs: 531
    rank_delta_direction: worse
    sort_value: 0.841
    sort_std: 0.008
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 590
    true_value: 0.7913
    true_std: 0.0052
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 590
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7913
    sort_std: 0.0052
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.785
    std: 0.0125
    paper_value: 0.785
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 604
    true_value: 0.785
    true_std: 0.0125
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 604
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.0125
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 666
    true_value: 0.7533
    true_std: 0.0056
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 666
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7533
    sort_std: 0.0056
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 715
    true_value: 0.7243
    true_std: 0.0118
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 715
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7243
    sort_std: 0.0118
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 733
    true_value: 0.715
    true_std: 0.0051
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 733
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0051
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 881
    true_value: 0.5403
    true_std: 0.054
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 881
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5403
    sort_std: 0.054
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Cornell
  rows:
  - model: FMP ode
    model_key: fmp ode
    model_plain: FMP ode
    value: 0.938
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 28, 2023
    date_display: Feb 2023
    date_iso: '2023-02-28'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.938
    sort_std: 0.015
    is_best: true
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.914
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.914
    sort_std: 0.017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.913
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 4
    true_value: 0.898
    true_std: 0.006
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4566
    value_note: ''
    paper_rank: 238
    rank_delta: 234
    rank_delta_abs: 234
    rank_delta_direction: worse
    sort_value: 0.898
    sort_std: 0.006
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 41
    true_value: 0.819
    true_std: 0.054
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.46769999999999995
    value_note: ''
    paper_rank: 251
    rank_delta: 210
    rank_delta_abs: 210
    rank_delta_direction: worse
    sort_value: 0.819
    sort_std: 0.054
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 57
    true_value: 0.792
    true_std: 0.063
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.46770000000000006
    value_note: ''
    paper_rank: 251
    rank_delta: 194
    rank_delta_abs: 194
    rank_delta_direction: worse
    sort_value: 0.792
    sort_std: 0.063
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.7657
    std: 0.0412
    paper_value: 0.7657
    paper_std: 0.0412
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 75
    true_value: 0.7657
    true_std: 0.0412
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7657
    sort_std: 0.0412
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 86
    true_value: 0.7478
    true_std: 0.0255
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 93
    true_value: 0.7297
    true_std: 0.0221
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 100
    true_value: 0.7207
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 106
    true_value: 0.7117
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 107
    true_value: 0.7117
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 127
    true_value: 0.6667
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 131
    true_value: 0.6577
    true_std: 0.0459
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 135
    true_value: 0.6486
    true_std: 0.0584
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 134
    true_value: 0.6486
    true_std: 0.0441
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 188
    true_value: 0.5405
    true_std: 0.0441
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 194
    true_value: 0.5315
    true_std: 0.0459
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5315
    sort_std: 0.0459
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 249
    true_value: 0.3874
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 249
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3874
    sort_std: 0.0127
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: Peptides-func
  rows:
  - model: S2GCN +PE
    model_key: s2gcn +pe
    model_plain: S2GCN +PE
    value: 0.7311
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7311
    sort_std: 0.0066
    is_best: true
  - model: S2GCN
    model_key: s2gcn
    model_plain: S2GCN
    value: 0.7275
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7275
    sort_std: 0.0066
    is_best: true
  - model: gLSTM
    model_key: glstm
    model_plain: gLSTM
    value: 0.725
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.725
    sort_std: 0.0023
    is_best: true
  - model: Graph-MLPMixer
    model_key: graph-mlpmixer
    model_plain: Graph-MLPMixer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 25
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27449999999999997
    value_note: ''
    paper_rank: 102
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 33
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.32460000000000006
    value_note: ''
    paper_rank: 108
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 57
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0036000000000000476
    value_note: global 0.6601 within std
    paper_rank: 60
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 68
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25239999999999996
    value_note: ''
    paper_rank: 103
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.6467
    std: 0.0124
    paper_value: 0.6467
    paper_std: 0.0124
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 72
    true_value: 0.6467
    true_std: 0.0124
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6467
    sort_std: 0.0124
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 77
    true_value: 0.6427
    true_std: 0.0035
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6427
    sort_std: 0.0035
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 103
    true_value: 0.401
    true_std: 0.015
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029100000000000015
    value_note: ''
    paper_rank: 107
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.401
    sort_std: 0.015
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 104
    true_value: 0.3964
    true_std: 0.0022
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 106
    true_value: 0.381
    true_std: 0.0013
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 107
    true_value: 0.3726
    true_std: 0.0018
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3726
    sort_std: 0.0018
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 108
    true_value: 0.3622
    true_std: 0.0036
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3622
    sort_std: 0.0036
    is_best: false
  metric: AP
  higher_is_better: true
- &id013
  dataset: Peptides-struct
  rows:
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
    date: Aug 7, 2025
    date_display: Aug 2025
    date_iso: '2025-08-07'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: true
  - model: B-PEARL+SRF
    model_key: b-pearl+srf
    model_plain: B-PEARL+SRF
    value: 0.243
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.03824'
    title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
      Neural Networks
    date: Nov 5, 2025
    date_display: Nov 2025
    date_iso: '2025-11-05'
    codebase_url: https://github.com/ryienh/sketched-random-features
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.243
    sort_std: null
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.2436
    std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.2436
    sort_std: 0.0022
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 16
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18869999999999998
    value_note: ''
    paper_rank: 108
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: Graph-MLPMixer
    model_key: graph-mlpmixer
    model_plain: Graph-MLPMixer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 30
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059
    value_note: ''
    paper_rank: 101
    rank_delta: 71
    rank_delta_abs: 71
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 42
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0816
    value_note: ''
    paper_rank: 102
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.2481
    sort_std: 0.0007
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 50
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0011999999999999789
    value_note: ''
    paper_rank: 61
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.2503
    std: 0.0016
    paper_value: 0.2503
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 55
    true_value: 0.2503
    true_std: 0.0016
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2503
    sort_std: 0.0016
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.2851
    std: 0.0012
    paper_value: 0.2851
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 97
    true_value: 0.2851
    true_std: 0.0012
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2851
    sort_std: 0.0012
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 107
    true_value: 0.4231
    true_std: 0.0049
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4231
    sort_std: 0.0049
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 108
    true_value: 0.4345
    true_std: 0.0026
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4345
    sort_std: 0.0026
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 109
    true_value: 0.4374
    true_std: 0.005
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 110
    true_value: 0.4492
    true_std: 0.0002
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 111
    true_value: 0.4541
    true_std: 0.0005
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
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
  - model: AIO
    model_key: aio
    model_plain: AIO
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.96
    std: 0.001
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
    global_rank: 2
    sort_value: 0.96
    sort_std: 0.001
    is_best: false
  - model: SAGN
    model_key: sagn
    model_plain: SAGN
    value: 0.9517
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9517
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 6
    true_value: 0.9490000000000001
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25370000000000004
    value_note: ''
    paper_rank: 672
    rank_delta: 666
    rank_delta_abs: 666
    rank_delta_direction: worse
    sort_value: 0.9490000000000001
    sort_std: null
    is_best: false
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 29
    true_value: 0.9296
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2146
    value_note: ''
    paper_rank: 653
    rank_delta: 624
    rank_delta_abs: 624
    rank_delta_direction: worse
    sort_value: 0.9296
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 31
    true_value: 0.9233
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1643
    value_note: ''
    paper_rank: 596
    rank_delta: 565
    rank_delta_abs: 565
    rank_delta_direction: worse
    sort_value: 0.9233
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 93
    true_value: 0.894
    true_std: null
    value_gap_source_arxiv: '2206.14418'
    value_gap_source_title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.119
    value_note: ''
    paper_rank: 553
    rank_delta: 460
    rank_delta_abs: 460
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 102
    true_value: 0.8931
    true_std: 0.0017
    value_gap_source_arxiv: '2505.17660'
    value_gap_source_title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking
      Graph Transformer for Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15839999999999999
    value_note: ''
    paper_rank: 633
    rank_delta: 531
    rank_delta_abs: 531
    rank_delta_direction: worse
    sort_value: 0.8931
    sort_std: 0.0017
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 123
    true_value: 0.8874
    true_std: 0.002
    value_gap_source_arxiv: '2404.15354'
    value_gap_source_title: 'Polynomial Selection in Spectral Graph Neural Networks:
      An Error-Sum of Function Slices Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19009999999999994
    value_note: ''
    paper_rank: 671
    rank_delta: 548
    rank_delta_abs: 548
    rank_delta_direction: worse
    sort_value: 0.8874
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 183
    true_value: 0.871
    true_std: null
    value_gap_source_arxiv: '2510.22555'
    value_gap_source_title: Cross-Paradigm Graph Backdoor Attacks with Promptable
      Subgraph Triggers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.129
    value_note: ''
    paper_rank: 622
    rank_delta: 439
    rank_delta_abs: 439
    rank_delta_direction: worse
    sort_value: 0.871
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 269
    true_value: 0.832
    true_std: 0.006
    value_gap_source_arxiv: '2503.12563'
    value_gap_source_title: 'Diffusion on Graph: Augmentation of Graph Structure for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13329999999999997
    value_note: ''
    paper_rank: 668
    rank_delta: 399
    rank_delta_abs: 399
    rank_delta_direction: worse
    sort_value: 0.832
    sort_std: 0.006
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 343
    true_value: 0.805
    true_std: 0.012
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04630000000000001
    value_note: ''
    paper_rank: 598
    rank_delta: 255
    rank_delta_abs: 255
    rank_delta_direction: worse
    sort_value: 0.805
    sort_std: 0.012
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.763
    std: 0.0122
    paper_value: 0.763
    paper_std: 0.0122
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 587
    true_value: 0.763
    true_std: 0.0122
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 587
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.0122
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 636
    true_value: 0.7327
    true_std: 0.0184
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 636
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7327
    sort_std: 0.0184
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 645
    true_value: 0.7203
    true_std: 0.0133
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 645
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7203
    sort_std: 0.0133
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Squirrel
  rows:
  - model: RUNG
    model_key: rung
    model_plain: RUNG
    value: 0.9787
    std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9787
    sort_std: 0.0177
    is_best: true
  - model: DHGNN
    model_key: dhgnn
    model_plain: DHGNN
    value: 0.7684
    std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7684
    sort_std: 0.0161
    is_best: false
  - model: NDDGNN
    model_key: nddgnn
    model_plain: NDDGNN
    value: 0.7538
    std: 0.0195
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7538
    sort_std: 0.0195
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 32
    true_value: 0.619
    true_std: null
    value_gap_source_arxiv: '2101.00797'
    value_gap_source_title: Beyond Low-frequency Information in Graph Convolutional
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3273
    value_note: ''
    paper_rank: 201
    rank_delta: 169
    rank_delta_abs: 169
    rank_delta_direction: worse
    sort_value: 0.619
    sort_std: null
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 55
    true_value: 0.563
    true_std: 0.022
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.26139999999999997
    value_note: ''
    paper_rank: 199
    rank_delta: 144
    rank_delta_abs: 144
    rank_delta_direction: worse
    sort_value: 0.563
    sort_std: 0.022
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 57
    true_value: 0.559
    true_std: 0.029
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22570000000000007
    value_note: ''
    paper_rank: 183
    rank_delta: 126
    rank_delta_abs: 126
    rank_delta_direction: worse
    sort_value: 0.559
    sort_std: 0.029
    is_best: false
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 103
    true_value: 0.4454
    true_std: 0.0141
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4454
    sort_std: 0.0141
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 106
    true_value: 0.431
    true_std: 0.012
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.431
    sort_std: 0.012
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 134
    true_value: 0.3854
    true_std: 0.0151
    value_gap_source_arxiv: '2411.02279'
    value_gap_source_title: arXiv:2411.02279
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.041200000000000014
    value_note: ''
    paper_rank: 178
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.3854
    sort_std: 0.0151
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.3748
    std: 0.0033
    paper_value: 0.3748
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 143
    true_value: 0.3748
    true_std: 0.0033
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3748
    sort_std: 0.0033
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 144
    true_value: 0.3737
    true_std: 0.0049
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 161
    true_value: 0.3602
    true_std: 0.007
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 169
    true_value: 0.3535
    true_std: 0.0062
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3535
    sort_std: 0.0062
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 175
    true_value: 0.349
    true_std: 0.0071
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.349
    sort_std: 0.0071
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 178
    true_value: 0.3454
    true_std: 0.0296
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005299999999999971
    value_note: global 0.3454 within std
    paper_rank: 180
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.3454
    sort_std: 0.0296
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 190
    true_value: 0.3164
    true_std: 0.0079
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3164
    sort_std: 0.0079
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 208
    true_value: 0.2767
    true_std: 0.0077
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 208
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2767
    sort_std: 0.0077
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Texas
  rows:
  - model: DoG (ACM-GCN)
    model_key: dog (acm-gcn)
    model_plain: DoG (ACM-GCN)
    value: 0.966
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 16, 2025
    date_display: Mar 2025
    date_iso: '2025-03-16'
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.966
    sort_std: 0.021
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.951
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 16, 2025
    date_display: Mar 2025
    date_iso: '2025-03-16'
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.951
    sort_std: 0.032
    is_best: true
  - model: AD-MixHop
    model_key: ad-mixhop
    model_plain: AD-MixHop
    value: 0.9443
    std: 0.0256
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9443
    sort_std: 0.0256
    is_best: true
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 15
    true_value: 0.9118
    true_std: 0.007
    value_gap_source_arxiv: '2202.04139'
    value_gap_source_title: Simplified Graph Convolution with Heterophily
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3713000000000001
    value_note: ''
    paper_rank: 244
    rank_delta: 229
    rank_delta_abs: 229
    rank_delta_direction: worse
    sort_value: 0.9118
    sort_std: 0.007
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 99
    true_value: 0.798
    true_std: 0.043
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.43760000000000004
    value_note: ''
    paper_rank: 268
    rank_delta: 169
    rank_delta_abs: 169
    rank_delta_direction: worse
    sort_value: 0.798
    sort_std: 0.043
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.7937
    std: 0.027
    paper_value: 0.7937
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
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 103
    true_value: 0.7937
    true_std: 0.027
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7937
    sort_std: 0.027
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 108
    true_value: 0.784
    true_std: 0.054
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3335
    value_note: ''
    paper_rank: 261
    rank_delta: 153
    rank_delta_abs: 153
    rank_delta_direction: worse
    sort_value: 0.784
    sort_std: 0.054
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 110
    true_value: 0.7838
    true_std: 0.0221
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7838
    sort_std: 0.0221
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 118
    true_value: 0.7748
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7748
    sort_std: 0.0127
    is_best: false
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 131
    true_value: 0.7568
    true_std: 0.0221
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7568
    sort_std: 0.0221
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 135
    true_value: 0.7478
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7478
    sort_std: 0.0127
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 138
    true_value: 0.7387
    true_std: 0.0637
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 143
    true_value: 0.7207
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 152
    true_value: 0.7027
    true_std: 0.0382
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7027
    sort_std: 0.0382
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 161
    true_value: 0.6937
    true_std: 0.0255
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6937
    sort_std: 0.0255
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 174
    true_value: 0.6667
    true_std: 0.0337
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 202
    true_value: 0.6126
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 202
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6126
    sort_std: 0.0127
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 208
    true_value: 0.6036
    true_std: 0.0255
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 208
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 266
    true_value: 0.3784
    true_std: 0.0221
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 266
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3784
    sort_std: 0.0221
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: Wisconsin
  rows:
  - model: FMP ode
    model_key: fmp ode
    model_plain: FMP ode
    value: 0.937
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 28, 2023
    date_display: Feb 2023
    date_iso: '2023-02-28'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.937
    sort_std: 0.012
    is_best: true
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 6
    true_value: 0.901
    true_std: 0.035
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4369
    value_note: ''
    paper_rank: 241
    rank_delta: 235
    rank_delta_abs: 235
    rank_delta_direction: worse
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 61
    true_value: 0.843
    true_std: 0.037
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4639
    value_note: ''
    paper_rank: 255
    rank_delta: 194
    rank_delta_abs: 194
    rank_delta_direction: worse
    sort_value: 0.843
    sort_std: 0.037
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 72
    true_value: 0.831
    true_std: 0.032
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.39309999999999995
    value_note: ''
    paper_rank: 244
    rank_delta: 172
    rank_delta_abs: 172
    rank_delta_direction: worse
    sort_value: 0.831
    sort_std: 0.032
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.8169
    std: 0.0113
    paper_value: 0.8169
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 79
    true_value: 0.8169
    true_std: 0.0113
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8169
    sort_std: 0.0113
    is_best: false
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 83
    true_value: 0.8039
    true_std: 0.016
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 89
    true_value: 0.7974
    true_std: 0.0092
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7974
    sort_std: 0.0092
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 100
    true_value: 0.7843
    true_std: 0.016
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 101
    true_value: 0.7843
    true_std: 0.0
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7843
    sort_std: 0.0
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 106
    true_value: 0.7778
    true_std: 0.0092
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7778
    sort_std: 0.0092
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 110
    true_value: 0.7647
    true_std: 0.032
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7647
    sort_std: 0.032
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 115
    true_value: 0.7582
    true_std: 0.0244
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7582
    sort_std: 0.0244
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 119
    true_value: 0.7451
    true_std: 0.032
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 125
    true_value: 0.7386
    true_std: 0.0403
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 141
    true_value: 0.6994
    true_std: 0.0333
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6994
    sort_std: 0.0333
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 217
    true_value: 0.5229
    true_std: 0.0462
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 218
    true_value: 0.5229
    true_std: 0.0092
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5229
    sort_std: 0.0092
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: ZINC
  rows:
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.004
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.004
    sort_std: null
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.006
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.006
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.014
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.014
    sort_std: null
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 7
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2406.08210'
    value_gap_source_title: arXiv:2406.08210
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0377
    value_note: ''
    paper_rank: 32
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 11
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.585
    value_note: ''
    paper_rank: 156
    rank_delta: 145
    rank_delta_abs: 145
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 13
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10550000000000001
    value_note: ''
    paper_rank: 91
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 16
    true_value: 0.0262
    true_std: 0.0025
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1706
    value_note: ''
    paper_rank: 126
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.0262
    sort_std: 0.0025
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 45
    true_value: 0.0681
    true_std: 0.0004
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0681
    sort_std: 0.0004
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 80
    true_value: 0.111
    true_std: 0.002
    value_gap_source_arxiv: '2301.09505'
    value_gap_source_title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.5115000000000001
    value_note: ''
    paper_rank: 156
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.111
    sort_std: 0.002
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 81
    true_value: 0.111
    true_std: 0.007
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0795
    value_note: ''
    paper_rank: 125
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.111
    sort_std: 0.007
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.1306
    std: 0.0194
    paper_value: 0.1306
    paper_std: 0.0194
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 92
    true_value: 0.1306
    true_std: 0.0194
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1306
    sort_std: 0.0194
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 97
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 122
    true_value: 0.1789
    true_std: 0.0071
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1789
    sort_std: 0.0071
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 131
    true_value: 0.226
    true_std: 0.014
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3778
    value_note: ''
    paper_rank: 156
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.226
    sort_std: 0.014
    is_best: false
  - model: Graph-MLPMixer
    model_key: graph-mlpmixer
    model_plain: Graph-MLPMixer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 143
    true_value: 0.3617
    true_std: 0.0222
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3617
    sort_std: 0.0222
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 157
    true_value: 0.6602
    true_std: 0.0294
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 158
    true_value: 0.6619
    true_std: 0.0067
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6619
    sort_std: 0.0067
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 161
    true_value: 0.6703
    true_std: 0.0033
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6703
    sort_std: 0.0033
    is_best: false
  metric: MAE
  higher_is_better: false
- &id011
  dataset: ogbg-molhiv
  rows:
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.997
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08443'
    title: 'CLEAR: Generative Counterfactual Explanations on Graphs'
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.997
    sort_std: 0.002
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.002
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.858
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.858
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 6
    true_value: 0.853
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21799999999999997
    value_note: ''
    paper_rank: 178
    rank_delta: 172
    rank_delta_abs: 172
    rank_delta_direction: worse
    sort_value: 0.853
    sort_std: 0.003
    is_best: false
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 11
    true_value: 0.845
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10649999999999993
    value_note: ''
    paper_rank: 155
    rank_delta: 144
    rank_delta_abs: 144
    rank_delta_direction: worse
    sort_value: 0.845
    sort_std: 0.004
    is_best: false
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 13
    true_value: 0.839
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1502
    value_note: ''
    paper_rank: 170
    rank_delta: 157
    rank_delta_abs: 157
    rank_delta_direction: worse
    sort_value: 0.839
    sort_std: 0.006
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.7997
    std: 0.0078
    paper_value: 0.7997
    paper_std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 32
    true_value: 0.7997
    true_std: 0.0078
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7997
    sort_std: 0.0078
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 52
    true_value: 0.788
    true_std: 0.0101
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01650000000000007
    value_note: ''
    paper_rank: 98
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.788
    sort_std: 0.0101
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 99
    true_value: 0.7713
    true_std: 0.0105
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7713
    sort_std: 0.0105
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 120
    true_value: 0.7608
    true_std: 0.0165
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7608
    sort_std: 0.0165
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.755
    std: 0.0
    paper_value: 0.755
    paper_std: 0.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 137
    true_value: 0.755
    true_std: 0.0
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.0
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 164
    true_value: 0.7169
    true_std: 0.0103
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7169
    sort_std: 0.0103
    is_best: false
  - model: Graph-MLPMixer
    model_key: graph-mlpmixer
    model_plain: Graph-MLPMixer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 170
    true_value: 0.6889
    true_std: 0.0146
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 172
    true_value: 0.6794
    true_std: 0.0076
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6794
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id012
  dataset: ogbg-molpcba
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.339
    std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.339
    sort_std: 0.0073
    is_best: true
  - model: unified method + FLAG
    model_key: unified method + flag
    model_plain: unified method + FLAG
    value: 0.3174
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_display: Jul 2022
    date_iso: 2022-07
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3174
    sort_std: null
    is_best: false
  - model: TGT-Ag+TGT-At-DP
    model_key: tgt-ag+tgt-at-dp
    model_plain: TGT-Ag+TGT-At-DP
    value: 0.3167
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.3167
    sort_std: 0.0031
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 21
    true_value: 0.2888
    true_std: 0.0019
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2888
    sort_std: 0.0019
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 46
    true_value: 0.2424
    true_std: 0.0034
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1471
    value_note: ''
    paper_rank: 65
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.2424
    sort_std: 0.0034
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 58
    true_value: 0.227
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12580000000000002
    value_note: ''
    paper_rank: 63
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.227
    sort_std: 0.001
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 61
    true_value: 0.1931
    true_std: 0.0018
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1931
    sort_std: 0.0018
    is_best: false
  - model: HopFormer
    model_key: hopformer
    model_plain: HopFormer
    value: 0.1849
    std: 0.0116
    paper_value: 0.1849
    paper_std: 0.0116
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 62
    true_value: 0.1849
    true_std: 0.0116
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1849
    sort_std: 0.0116
    is_best: false
  - model: Graph-MLPMixer
    model_key: graph-mlpmixer
    model_plain: Graph-MLPMixer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 63
    true_value: 0.1386
    true_std: 0.0018
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1386
    sort_std: 0.0018
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 64
    true_value: 0.0973
    true_std: 0.0011
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0973
    sort_std: 0.0011
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.0968
    std: 0.0001
    paper_value: 0.0968
    paper_std: 0.0001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 65
    true_value: 0.0968
    true_std: 0.0001
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0968
    sort_std: 0.0001
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 66
    true_value: 0.0933
    true_std: 0.004
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2, 2026
    date_display: Feb 2026
    date_iso: '2026-02-02'
    published_venue: null
    global_rank: 67
    true_value: 0.0785
    true_std: 0.0021
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
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
  - *id004
- benchmark: Heterophilic Graphs
  datasets:
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
  - *id010
- benchmark: OGB
  datasets:
  - *id011
  - *id012
- benchmark: LRGB
  datasets:
  - *id013
  - *id014
single_proposed_model: HopFormer
---

