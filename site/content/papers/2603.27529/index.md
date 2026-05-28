---
title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in GNNs
arxiv_id: '2603.27529'
source_url: ''
authors: []
published_date: Mar 2026
published_date_iso: 2026-03
abstract: Abstract Graph neural networks (GNNs) have achieved strong performance across
  various real-world domains. Nevertheless, they suffer from oversquashing, where
  long-range information is distorted as it is compressed through limited message-passing
  pathways. This bottleneck limits their ability to capture essential global context
  and decreases their performance, particularly in dense and heterophilic regions
  of graphs. To address this issue, we propose a novel graph learning framework that
  enriches node embeddings via cross-attentive cohesive subgraph representations to
  mitigate the impact of excessive long-range dependencies. This framework enhances
  the node representation by emphasizing cohesive structure in long-range information
  but removing noisy or irrelevant connections. Additionally, It preserves essential
  global context without overloading the narrow bottlenecked channels, thereby enhancing
  message aggregation across vertices. Extensive experiments on multiple benchmark
  datasets demonstrate that our model achieves consistent improvements in classification
  accuracy over standard baseline methods.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CaCoSE
mrr: 0.0194
adjusted_mrr: 0.0194
mrr_dataset_count: 10
benchmark_categories:
- Classic
- Heterophilic Graphs
- TU Dortmund
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id003
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
    value: 0.9201
    std: null
    paper_value: 0.9201
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 3
    true_value: 0.966
    true_std: 0.0033
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04589999999999994
    value_note: ''
    paper_rank: 37
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9657
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
    global_rank: 4
    sort_value: 0.9657
    sort_std: 0.0023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9212
    std: null
    paper_value: 0.9212
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 6
    true_value: 0.961
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03979999999999995
    value_note: ''
    paper_rank: 36
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.961
    sort_std: 0.0046
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.9298000000000001
    std: null
    paper_value: 0.9298000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 33
    true_value: 0.9298000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9298000000000001
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.9251
    std: null
    paper_value: 0.9251
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 34
    true_value: 0.9251
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9251
    sort_std: null
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.9193000000000001
    std: null
    paper_value: 0.9193000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 38
    true_value: 0.9193000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9193000000000001
    sort_std: null
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.9183
    std: null
    paper_value: 0.9183
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 39
    true_value: 0.9183
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9183
    sort_std: null
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.9176000000000001
    std: null
    paper_value: 0.9176000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 40
    true_value: 0.9176000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9176000000000001
    sort_std: null
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.9170999999999999
    std: null
    paper_value: 0.9170999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 41
    true_value: 0.9170999999999999
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9170999999999999
    sort_std: null
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.9158
    std: null
    paper_value: 0.9158
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 42
    true_value: 0.9158
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9158
    sort_std: null
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.7986
    std: null
    paper_value: 0.7986
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 48
    true_value: 0.7986
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7986
    sort_std: null
    is_best: false
  - model: LRGB
    model_key: lrgb
    model_plain: LRGB
    value: 0.7404000000000001
    std: null
    paper_value: 0.7404000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 50
    true_value: 0.7404000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7404000000000001
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.6736
    std: null
    paper_value: 0.6736
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 51
    true_value: 0.6736
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6736
    sort_std: null
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
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.2787
    std: null
    paper_value: 0.2787
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 17
    true_value: 0.7428
    true_std: 0.0048
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4641
    value_note: ''
    paper_rank: 127
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.7428
    sort_std: 0.0048
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.6899
    std: null
    paper_value: 0.6899
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 27
    true_value: 0.6899
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6899
    sort_std: null
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.6378
    std: null
    paper_value: 0.6378
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 33
    true_value: 0.6803
    true_std: 0.0060999999999999995
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04249999999999998
    value_note: ''
    paper_rank: 52
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.6803
    sort_std: 0.0060999999999999995
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.6031
    std: null
    paper_value: 0.6031
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 34
    true_value: 0.6798000000000001
    true_std: 0.004
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0767000000000001
    value_note: ''
    paper_rank: 68
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.6798000000000001
    sort_std: 0.004
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.659
    std: null
    paper_value: 0.659
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 39
    true_value: 0.659
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: null
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.6024
    std: null
    paper_value: 0.6024
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 43
    true_value: 0.6535
    true_std: 0.0051
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05109999999999992
    value_note: ''
    paper_rank: 68
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.6535
    sort_std: 0.0051
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6332
    std: null
    paper_value: 0.6332
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.015000000000000013
    value_note: global 0.6482 within std
    paper_rank: 52
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.617
    std: null
    paper_value: 0.617
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02200000000000002
    value_note: ''
    paper_rank: 60
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6264
    std: null
    paper_value: 0.6264
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 56
    true_value: 0.6264
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6264
    sort_std: null
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.6074
    std: null
    paper_value: 0.6074
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 66
    true_value: 0.6074
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6074
    sort_std: null
    is_best: false
  - model: LRGB
    model_key: lrgb
    model_plain: LRGB
    value: 0.4693
    std: null
    paper_value: 0.4693
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 109
    true_value: 0.4693
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4693
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.419
    std: null
    paper_value: 0.419
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 122
    true_value: 0.419
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.419
    sort_std: null
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
    value: 0.691
    std: null
    paper_value: 0.691
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12290000000000001
    value_note: ''
    paper_rank: 140
    rank_delta: 128
    rank_delta_abs: 128
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6794
    std: null
    paper_value: 0.6794
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12580000000000002
    value_note: ''
    paper_rank: 150
    rank_delta: 131
    rank_delta_abs: 131
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.6708
    std: null
    paper_value: 0.6708
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 102
    true_value: 0.738
    true_std: 0.002
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06720000000000004
    value_note: ''
    paper_rank: 153
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.738
    sort_std: 0.002
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.6724
    std: null
    paper_value: 0.6724
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 106
    true_value: 0.735
    true_std: 0.02
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06259999999999999
    value_note: ''
    paper_rank: 151
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.735
    sort_std: 0.02
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.6742
    std: null
    paper_value: 0.6742
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 113
    true_value: 0.726
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05179999999999996
    value_note: ''
    paper_rank: 150
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.726
    sort_std: 0.003
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6776000000000001
    std: null
    paper_value: 0.6776000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 134
    true_value: 0.7056
    true_std: 0.0058
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.027999999999999914
    value_note: ''
    paper_rank: 150
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.7056
    sort_std: 0.0058
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.6942
    std: null
    paper_value: 0.6942
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 139
    true_value: 0.6942
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6942
    sort_std: null
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.6915
    std: null
    paper_value: 0.6915
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 140
    true_value: 0.6915
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6915
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.6607999999999999
    std: null
    paper_value: 0.6607999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 161
    true_value: 0.6607999999999999
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6607999999999999
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.6426000000000001
    std: null
    paper_value: 0.6426000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 174
    true_value: 0.6426000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6426000000000001
    sort_std: null
    is_best: false
  - model: LRGB
    model_key: lrgb
    model_plain: LRGB
    value: 0.5758
    std: null
    paper_value: 0.5758
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 207
    true_value: 0.5758
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 207
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5758
    sort_std: null
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.249
    std: null
    paper_value: 0.249
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 219
    true_value: 0.249
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 219
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.249
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Coauthor-CS
  rows:
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9638
    std: 0.0011
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
    sort_value: 0.9638
    sort_std: 0.0011
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8713
    std: null
    paper_value: 0.8713
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.9621
    true_std: 0.0014
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09079999999999999
    value_note: ''
    paper_rank: 28
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.9621
    sort_std: 0.0014
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8886
    std: null
    paper_value: 0.8886
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 3
    true_value: 0.9617
    true_std: 0.0006
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07310000000000005
    value_note: ''
    paper_rank: 27
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.9617
    sort_std: 0.0006
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9592
    std: 0.0025
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
    global_rank: 4
    sort_value: 0.9592
    sort_std: 0.0025
    is_best: false
  - model: M
    model_key: m
    model_plain: M
    value: 0.9589
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.9073
    std: null
    paper_value: 0.9073
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 22
    true_value: 0.9073
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9073
    sort_std: null
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.9056000000000001
    std: null
    paper_value: 0.9056000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 23
    true_value: 0.9056000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9056000000000001
    sort_std: null
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.9052
    std: null
    paper_value: 0.9052
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 24
    true_value: 0.9052
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9052
    sort_std: null
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.9044
    std: null
    paper_value: 0.9044
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 25
    true_value: 0.9044
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9044
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.9004000000000001
    std: null
    paper_value: 0.9004000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 26
    true_value: 0.9004000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9004000000000001
    sort_std: null
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.8887
    std: null
    paper_value: 0.8887
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 27
    true_value: 0.8887
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8887
    sort_std: null
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8842
    std: null
    paper_value: 0.8842
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 28
    true_value: 0.8842
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8842
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.769
    std: null
    paper_value: 0.769
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 29
    true_value: 0.769
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: null
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.725
    std: null
    paper_value: 0.725
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 30
    true_value: 0.725
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: null
    is_best: false
  - model: LRGB
    model_key: lrgb
    model_plain: LRGB
    value: 0.595
    std: null
    paper_value: 0.595
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 37
    true_value: 0.595
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.595
    sort_std: null
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
    value: 0.4435
    std: null
    paper_value: 0.4435
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.9139
    true_std: 0.0024
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.47040000000000004
    value_note: ''
    paper_rank: 299
    rank_delta: 297
    rank_delta_abs: 297
    rank_delta_direction: worse
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
  - model: ANS-GT + HDSE
    model_key: ans-gt + hdse
    model_plain: ANS-GT + HDSE
    value: 0.8967
    std: 0.0039
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
    global_rank: 4
    sort_value: 0.8967
    sort_std: 0.0039
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.85
    std: null
    paper_value: 0.85
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03249999999999997
    value_note: ''
    paper_rank: 102
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.8366
    std: null
    paper_value: 0.8366
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 43
    true_value: 0.8794
    true_std: 0.0026
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04279999999999995
    value_note: ''
    paper_rank: 116
    rank_delta: 73
    rank_delta_abs: 73
    rank_delta_direction: worse
    sort_value: 0.8794
    sort_std: 0.0026
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.8368000000000001
    std: null
    paper_value: 0.8368000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 44
    true_value: 0.879
    true_std: 0.007
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042199999999999904
    value_note: ''
    paper_rank: 116
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.007
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.8406999999999999
    std: null
    paper_value: 0.8406999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 46
    true_value: 0.8786
    true_std: 0.0028000000000000004
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.037900000000000156
    value_note: ''
    paper_rank: 111
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.8786
    sort_std: 0.0028000000000000004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8423999999999999
    std: null
    paper_value: 0.8423999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
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
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.8404
    std: null
    paper_value: 0.8404
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 86
    true_value: 0.864
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.023599999999999954
    value_note: ''
    paper_rank: 111
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.864
    sort_std: 0.021
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.85
    std: null
    paper_value: 0.85
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 103
    true_value: 0.85
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: null
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.836
    std: null
    paper_value: 0.836
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 117
    true_value: 0.836
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.836
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.8266
    std: null
    paper_value: 0.8266
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 133
    true_value: 0.8266
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8266
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.7576999999999999
    std: null
    paper_value: 0.7576999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 194
    true_value: 0.7576999999999999
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7576999999999999
    sort_std: null
    is_best: false
  - model: LRGB
    model_key: lrgb
    model_plain: LRGB
    value: 0.7101999999999999
    std: null
    paper_value: 0.7101999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 238
    true_value: 0.7101999999999999
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 238
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7101999999999999
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
  - model: CaCoSE (SAGE)
    model_key: cacose (sage)
    model_plain: CaCoSE (SAGE)
    value: 0.7390000000000001
    std: null
    paper_value: 0.7390000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 32
    true_value: 0.7390000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7390000000000001
    sort_std: null
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.732
    std: null
    paper_value: 0.732
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 45
    true_value: 0.732
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: null
    is_best: false
  - model: CaCoSE (without CaEF)
    model_key: cacose (without caef)
    model_plain: CaCoSE (without CaEF)
    value: 0.731
    std: null
    paper_value: 0.731
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 48
    true_value: 0.731
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: null
    is_best: false
  - model: CaCoSE (without Attention)
    model_key: cacose (without attention)
    model_plain: CaCoSE (without Attention)
    value: 0.73
    std: null
    paper_value: 0.73
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 49
    true_value: 0.73
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: null
    is_best: false
  - model: CaCoSE (TopkPool)
    model_key: cacose (topkpool)
    model_plain: CaCoSE (TopkPool)
    value: 0.7290000000000001
    std: null
    paper_value: 0.7290000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 52
    true_value: 0.7290000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7290000000000001
    sort_std: null
    is_best: false
  - model: CaCoSE (GMT)
    model_key: cacose (gmt)
    model_plain: CaCoSE (GMT)
    value: 0.7170000000000001
    std: null
    paper_value: 0.7170000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 70
    true_value: 0.7170000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7170000000000001
    sort_std: null
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.7020000000000001
    std: null
    paper_value: 0.7020000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 97
    true_value: 0.7020000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7020000000000001
    sort_std: null
    is_best: false
  - model: CaCoSE (DMon)
    model_key: cacose (dmon)
    model_plain: CaCoSE (DMon)
    value: 0.675
    std: null
    paper_value: 0.675
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 117
    true_value: 0.675
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.675
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.6729999999999999
    std: null
    paper_value: 0.6729999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 118
    true_value: 0.6729999999999999
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6729999999999999
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.648
    std: null
    paper_value: 0.648
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 125
    true_value: 0.648
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.648
    sort_std: null
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.629
    std: null
    paper_value: 0.629
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 132
    true_value: 0.629
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.629
    sort_std: null
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.6082
    std: null
    paper_value: 0.6082
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 136
    true_value: 0.6082
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6082
    sort_std: null
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.604
    std: null
    paper_value: 0.604
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 138
    true_value: 0.604
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.604
    sort_std: null
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.536
    std: null
    paper_value: 0.536
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 147
    true_value: 0.536
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.536
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.4914
    std: null
    paper_value: 0.4914
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 47
    true_value: 0.4914
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4914
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.45399999999999996
    std: null
    paper_value: 0.45399999999999996
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 69
    true_value: 0.45399999999999996
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.45399999999999996
    sort_std: null
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.4533
    std: null
    paper_value: 0.4533
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 70
    true_value: 0.4533
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4533
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.424
    std: null
    paper_value: 0.424
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 74
    true_value: 0.424
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.424
    sort_std: null
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.4153
    std: null
    paper_value: 0.4153
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 75
    true_value: 0.4153
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4153
    sort_std: null
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.382
    std: null
    paper_value: 0.382
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 76
    true_value: 0.382
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.382
    sort_std: null
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.37329999999999997
    std: null
    paper_value: 0.37329999999999997
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 77
    true_value: 0.37329999999999997
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.37329999999999997
    sort_std: null
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.35600000000000004
    std: null
    paper_value: 0.35600000000000004
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 78
    true_value: 0.35600000000000004
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35600000000000004
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.7589
    std: null
    paper_value: 0.7589
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 56
    true_value: 0.862
    true_std: 0.015
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10309999999999997
    value_note: ''
    paper_rank: 134
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.862
    sort_std: 0.015
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.68
    std: null
    paper_value: 0.68
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 86
    true_value: 0.82204
    true_std: 0.06728
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14203999999999994
    value_note: ''
    paper_rank: 164
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.82204
    sort_std: 0.06728
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.64
    std: null
    paper_value: 0.64
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 91
    true_value: 0.81684
    true_std: 0.07964
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17684
    value_note: ''
    paper_rank: 168
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.81684
    sort_std: 0.07964
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.76
    std: null
    paper_value: 0.76
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 118
    true_value: 0.78632
    true_std: 0.06201
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02632000000000001
    value_note: global 0.7863 within std
    paper_rank: 131
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.78632
    sort_std: 0.06201
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.7698999999999999
    std: null
    paper_value: 0.7698999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 128
    true_value: 0.7698999999999999
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7698999999999999
    sort_std: null
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.7453
    std: null
    paper_value: 0.7453
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 138
    true_value: 0.7453
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7453
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.745
    std: null
    paper_value: 0.745
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 139
    true_value: 0.745
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: null
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.71
    std: null
    paper_value: 0.71
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 154
    true_value: 0.71
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.667
    std: null
    paper_value: 0.667
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 64
    true_value: 0.751
    true_std: 0.008
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08399999999999996
    value_note: ''
    paper_rank: 191
    rank_delta: 127
    rank_delta_abs: 127
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.008
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.7106999999999999
    std: null
    paper_value: 0.7106999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 81
    true_value: 0.74381
    true_std: 0.03443
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.033110000000000084
    value_note: global 0.7438 within std
    paper_rank: 163
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.74381
    sort_std: 0.03443
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.7152
    std: null
    paper_value: 0.7152
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 140
    true_value: 0.72303
    true_std: 0.04658
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007830000000000004
    value_note: global 0.7230 within std
    paper_rank: 155
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.72303
    sort_std: 0.04658
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.7223
    std: null
    paper_value: 0.7223
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 143
    true_value: 0.7223
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7223
    sort_std: null
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.7179000000000001
    std: null
    paper_value: 0.7179000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 152
    true_value: 0.7179000000000001
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7179000000000001
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.708
    std: null
    paper_value: 0.708
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 171
    true_value: 0.708
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: null
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.6688
    std: null
    paper_value: 0.6688
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 187
    true_value: 0.68714
    true_std: 0.04233
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.018340000000000023
    value_note: global 0.6871 within std
    paper_rank: 191
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.68714
    sort_std: 0.04233
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.6840999999999999
    std: null
    paper_value: 0.6840999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 188
    true_value: 0.68411
    true_std: 0.04122
    value_gap_source_arxiv: '2310.01668'
    value_gap_source_title: Locality-Aware Graph Rewiring in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 1.0000000000065512e-05
    value_note: global 0.6841 within std
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68411
    sort_std: 0.04122
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5236
    std: null
    paper_value: 0.5236
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3075
    value_note: ''
    paper_rank: 162
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5236999999999999
    std: null
    paper_value: 0.5236999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2845000000000001
    value_note: ''
    paper_rank: 162
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.5605
    std: null
    paper_value: 0.5605
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 65
    true_value: 0.793
    true_std: 0.012
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23250000000000004
    value_note: ''
    paper_rank: 157
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.793
    sort_std: 0.012
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.6945
    std: null
    paper_value: 0.6945
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 113
    true_value: 0.7045999999999999
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010099999999999887
    value_note: global 0.7046 within std
    paper_rank: 116
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.7045999999999999
    sort_std: 0.0161
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.5263
    std: null
    paper_value: 0.5263
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 131
    true_value: 0.644
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11770000000000003
    value_note: ''
    paper_rank: 162
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.644
    sort_std: 0.004
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.5236999999999999
    std: null
    paper_value: 0.5236999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 141
    true_value: 0.6135
    true_std: 0.0125
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0898000000000001
    value_note: ''
    paper_rank: 162
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.6135
    sort_std: 0.0125
    is_best: false
  - model: LRGB
    model_key: lrgb
    model_plain: LRGB
    value: 0.5736
    std: null
    paper_value: 0.5736
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 152
    true_value: 0.5736
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5736
    sort_std: null
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.5236999999999999
    std: null
    paper_value: 0.5236999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 153
    true_value: 0.5718
    true_std: 0.016399999999999998
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04810000000000003
    value_note: ''
    paper_rank: 162
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.5718
    sort_std: 0.016399999999999998
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.5421
    std: null
    paper_value: 0.5421
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 155
    true_value: 0.563
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02089999999999992
    value_note: ''
    paper_rank: 161
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.563
    sort_std: 0.0161
    is_best: false
  - model: CaCoSE
    model_key: cacose
    model_plain: CaCoSE
    value: 0.5447
    std: null
    paper_value: 0.5447
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 161
    true_value: 0.5447
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5447
    sort_std: null
    is_best: false
  - model: GOKU
    model_key: goku
    model_plain: GOKU
    value: 0.371
    std: null
    paper_value: 0.371
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 172
    true_value: 0.371
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.371
    sort_std: null
    is_best: false
  - model: LASER
    model_key: laser
    model_plain: LASER
    value: 0.32630000000000003
    std: null
    paper_value: 0.32630000000000003
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 173
    true_value: 0.32630000000000003
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 173
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.32630000000000003
    sort_std: null
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
- benchmark: Heterophilic Graphs
  datasets:
  - *id005
  - *id006
- benchmark: TU Dortmund
  datasets:
  - *id007
  - *id008
  - *id009
  - *id010
single_proposed_model: CaCoSE
---

