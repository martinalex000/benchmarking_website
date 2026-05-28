---
title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting
  Power
arxiv_id: '2309.04941'
source_url: ''
authors: []
published_date: Sep 2023
published_date_iso: 2023-09
abstract: 'The ability of graph neural networks (GNNs) to count certain graph substructures,
  especially cycles, is important for the success of GNNs on a wide range of tasks.
  It has been recently used as a popular metric for evaluating the expressive power
  of GNNs. Many of the proposed GNN models with provable cycle counting power are
  based on subgraph GNNs, i.e., extracting a bag of subgraphs from the input graph,
  generating representations for each subgraph, and using them to augment the representation
  of the input graph. However, those methods require heavy preprocessing, and suffer
  from high time and memory costs. In this paper, we overcome the aforementioned limitations
  of subgraph GNNs by proposing a novel class of GNNs---$d$-Distance-Restricted FWL(2)
  GNNs, or $d$-DRFWL(2) GNNs, based on the well-known FWL(2) algorithm. As a heuristic
  method for graph isomorphism testing, FWL(2) colors all node pairs in a graph and
  performs message passing among those node pairs. In order to balance the expressive
  power and complexity, $d$-DRFWL(2) GNNs simplify FWL(2) by restricting the range
  of message passing to node pairs whose mutual distances are at most $d$. This way,
  $d$-DRFWL(2) GNNs exploit graph sparsity while avoiding the expensive subgraph extraction
  operations in subgraph GNNs, making both the time and space complexity lower. We
  theoretically investigate both the discriminative power and the cycle counting power
  of $d$-DRFWL(2) GNNs. Our most important finding is that $d$-DRFWL(2) GNNs have
  provably strong cycle counting power even with $d=2$: they can count all 3, 4, 5,
  6-cycles. Since 6-cycles (e.g., benzene rings) are ubiquitous in organic molecules,
  being able to detect and count them is crucial for achieving robust and generalizable
  performance on molecular tasks. Experiments on both synthetic datasets and molecular
  datasets verify our theory. To the best of our knowledge, 2-DRFWL(2) GNN is the
  most efficient GNN model to date (both theoretically and empirically) that can count
  up to 6-cycles.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Transformer+LapPE
- SAN+RWSE
- d-DRFWL(2) GNN
mrr: 0.0293
adjusted_mrr: 0.0293
mrr_dataset_count: 4
benchmark_categories:
- Classic
- LRGB
- OGB
- Quantum Chemistry
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
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
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11419999999999997
    value_note: ''
    paper_rank: 273
    rank_delta: 224
    rank_delta_abs: 224
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
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
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 133
    true_value: 0.6685
    true_std: 0.0062
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06159999999999999
    value_note: ''
    paper_rank: 239
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
    sort_value: 0.6685
    sort_std: 0.0062
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
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
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
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.6439
    std: 0.0075
    paper_value: 0.6439
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 200
    true_value: 0.644
    true_std: 0.008
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.6440 within std
    paper_rank: 201
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.644
    sort_std: 0.008
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: 0.0121
    paper_value: 0.6384
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 212
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
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
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 217
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: d-DRFWL(2) GNN
    model_key: d-drfwl(2) gnn
    model_plain: d-DRFWL(2) GNN
    value: 0.5953
    std: 0.0048
    paper_value: 0.5953
    paper_std: 0.0048
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 256
    true_value: 0.5953
    true_std: 0.0048
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 256
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5953
    sort_std: 0.0048
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5543
    std: 0.0078
    paper_value: 0.5543
    paper_std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 285
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 285
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5543
    sort_std: 0.0078
    is_best: false
  metric: AP
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
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
    paper_rank: 297
    rank_delta: 285
    rank_delta_abs: 285
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
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
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    paper_value: 0.2529
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 168
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 167
    true_value: 0.2529
    true_std: 0.0009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08279999999999998
    value_note: ''
    paper_rank: 289
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.2529
    sort_std: 0.0009
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 188
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: d-DRFWL(2) GNN
    model_key: d-drfwl(2) gnn
    model_plain: d-DRFWL(2) GNN
    value: 0.2594
    std: 0.0038
    paper_value: 0.2594
    paper_std: 0.0038
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 213
    true_value: 0.2594
    true_std: 0.0038
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 213
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2594
    sort_std: 0.0038
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: 0.0043
    paper_value: 0.2683
    paper_std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 242
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.2680 within std
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3471
    std: 0.001
    paper_value: 0.3471
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 300
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 300
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id006
  dataset: QM9
  rows:
  - model: Mace
    model_key: mace
    model_plain: Mace
    value: 0.02
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.02
    sort_std: null
    is_best: true
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.023
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
    global_rank: 2
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    value: 0.02578744427174226
    std: 0.000867405321348238
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
    global_rank: 3
    sort_value: 0.02578744427174226
    sort_std: 0.000867405321348238
    is_best: false
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.231
    std: null
    paper_value: 0.231
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 19
    true_value: 0.231
    true_std: null
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.231
    sort_std: null
    is_best: false
  - model: DTNN*
    model_key: dtnn*
    model_plain: DTNN*
    value: 0.244
    std: null
    paper_value: 0.244
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 20
    true_value: 0.244
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.244
    sort_std: null
    is_best: false
  - model: d-DRFWL(2) GNN
    model_key: d-drfwl(2) gnn
    model_plain: d-DRFWL(2) GNN
    value: 0.346
    std: null
    paper_value: 0.346
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 23
    true_value: 0.346
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.346
    sort_std: null
    is_best: false
  - model: Deep LRP
    model_key: deep lrp
    model_plain: Deep LRP
    value: 0.364
    std: null
    paper_value: 0.364
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 28
    true_value: 0.364
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.364
    sort_std: null
    is_best: false
  - model: SSWL+
    model_key: sswl+
    model_plain: SSWL+
    value: 0.418
    std: null
    paper_value: 0.418
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 32
    true_value: 0.418
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.418
    sort_std: null
    is_best: false
  - model: I^2GNN
    model_key: i$^2$gnn
    model_plain: I^2GNN
    value: 0.428
    std: null
    paper_value: 0.428
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 34
    true_value: 0.428
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.428
    sort_std: null
    is_best: false
  - model: NGNN
    model_key: ngnn
    model_plain: NGNN
    value: 0.428
    std: null
    paper_value: 0.428
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 33
    true_value: 0.428
    true_std: null
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.428
    sort_std: null
    is_best: false
  - model: LFWL(2)
    model_key: lfwl(2)
    model_plain: LFWL(2)
    value: 0.435
    std: null
    paper_value: 0.435
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 36
    true_value: 0.435
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.435
    sort_std: null
    is_best: false
  - model: 1-GNN
    model_key: 1-gnn
    model_plain: 1-GNN
    value: 0.493
    std: null
    paper_value: 0.493
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 39
    true_value: 0.493
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.493
    sort_std: null
    is_best: false
  - model: 1-2-3-GNN
    model_key: 1-2-3-gnn
    model_plain: 1-2-3-GNN
    value: 0.493
    std: null
    paper_value: 0.493
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 40
    true_value: 0.493
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.493
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
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
    paper_rank: 144
    rank_delta: 137
    rank_delta_abs: 137
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.022
    std: 0.002
    paper_value: 0.022
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=100)'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: I^2GNN
    model_key: i$^2$gnn
    model_plain: I^2GNN
    value: 0.083
    std: 0.001
    paper_value: 0.083
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 10
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.060000000000000005
    value_note: ''
    paper_rank: 150
    rank_delta: 140
    rank_delta_abs: 140
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: I^2GNN
    model_key: i$^2$gnn
    model_plain: I^2GNN
    value: 0.023
    std: 0.001
    paper_value: 0.023
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=100)'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 10
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: d-DRFWL(2) GNN
    model_key: d-drfwl(2) gnn
    model_plain: d-DRFWL(2) GNN
    value: 0.077
    std: 0.002
    paper_value: 0.077
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 23
    true_value: 0.025
    true_std: 0.003
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.052
    value_note: ''
    paper_rank: 131
    rank_delta: 108
    rank_delta_abs: 108
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.003
    is_best: false
  - model: d-DRFWL(2) GNN
    model_key: d-drfwl(2) gnn
    model_plain: d-DRFWL(2) GNN
    value: 0.025
    std: 0.003
    paper_value: 0.025
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=100)'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 23
    true_value: 0.025
    true_std: 0.003
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.025
    sort_std: 0.003
    is_best: false
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.111
    std: 0.003
    paper_value: 0.111
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 31
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.082
    value_note: ''
    paper_rank: 198
    rank_delta: 167
    rank_delta_abs: 167
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.029
    std: 0.001
    paper_value: 0.029
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=100)'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 31
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.151
    std: 0.006
    paper_value: 0.151
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 37
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11499999999999999
    value_note: ''
    paper_rank: 231
    rank_delta: 194
    rank_delta_abs: 194
    rank_delta_direction: worse
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.036
    std: 0.002
    paper_value: 0.036
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=100)'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 37
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: CIN (small)
    model_key: cin (small)
    model_plain: CIN (small)
    value: 0.094
    std: 0.004
    paper_value: 0.094
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 39
    true_value: 0.044
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05
    value_note: ''
    paper_rank: 181
    rank_delta: 142
    rank_delta_abs: 142
    rank_delta_direction: worse
    sort_value: 0.044
    sort_std: 0.003
    is_best: false
  - model: CIN (small)
    model_key: cin (small)
    model_plain: CIN (small)
    value: 0.044
    std: 0.003
    paper_value: 0.044
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=100)'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 39
    true_value: 0.044
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.044
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.188
    std: 0.004
    paper_value: 0.188
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13072978921109524
    value_note: ''
    paper_rank: 252
    rank_delta: 204
    rank_delta_abs: 204
    rank_delta_direction: worse
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.163
    std: 0.004
    paper_value: 0.163
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.098
    value_note: ''
    paper_rank: 246
    rank_delta: 171
    rank_delta_abs: 171
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.088
    std: 0.002
    paper_value: 0.088
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=100)'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022999999999999993
    value_note: ''
    paper_rank: 170
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GNNAK+
    model_key: gnnak+
    model_plain: GNNAK+
    value: 0.08
    std: 0.001
    paper_value: 0.08
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 149
    true_value: 0.08
    true_std: 0.001
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.08
    sort_std: 0.001
    is_best: false
  - model: SUN (EGO)
    model_key: sun (ego)
    model_plain: SUN (EGO)
    value: 0.083
    std: 0.003
    paper_value: 0.083
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 153
    true_value: 0.083
    true_std: 0.003
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.083
    sort_std: 0.003
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.115
    std: 0.012
    paper_value: 0.115
    paper_std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 188
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013999999999999999
    value_note: ''
    paper_rank: 199
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.168
    std: 0.003
    paper_value: 0.168
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 247
    true_value: 0.168
    true_std: 0.003
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 247
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.168
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
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
    value: 0.9681
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
    global_rank: 3
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7707
    std: 0.0149
    paper_value: 0.7707
    paper_std: 0.0149
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19729999999999992
    value_note: ''
    paper_rank: 137
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
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
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.8039
    std: 0.009
    paper_value: 0.8039
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 20
    true_value: 0.8039
    true_std: 0.009
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.009
    is_best: false
  - model: CIN (small)
    model_key: cin (small)
    model_plain: CIN (small)
    value: 0.8005
    std: 0.0104
    paper_value: 0.8005
    paper_std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 27
    true_value: 0.8026
    true_std: 0.0102
    value_gap_source_arxiv: '2306.03561'
    value_gap_source_title: 'CIN++: Enhancing Topological Message Passing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0020999999999999908
    value_note: global 0.8026 within std
    paper_rank: 31
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.8026
    sort_std: 0.0102
    is_best: false
  - model: SUN (EGO)
    model_key: sun (ego)
    model_plain: SUN (EGO)
    value: 0.8003
    std: 0.0055
    paper_value: 0.8003
    paper_std: 0.0055
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 33
    true_value: 0.8003
    true_std: 0.0055
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8003
    sort_std: 0.0055
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 43
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
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.797
    sort_std: 0.0097
    is_best: false
  - model: GNNAK+
    model_key: gnnak+
    model_plain: GNNAK+
    value: 0.7961
    std: 0.0119
    paper_value: 0.7961
    paper_std: 0.0119
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 47
    true_value: 0.7961
    true_std: 0.0119
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7961
    sort_std: 0.0119
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 63
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
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7905
    sort_std: 0.0132
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 80
    true_value: 0.788
    true_std: 0.0082
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.0082
    is_best: false
  - model: I^2GNN
    model_key: i$^2$gnn
    model_plain: I^2GNN
    value: 0.7868
    std: 0.0093
    paper_value: 0.7868
    paper_std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 84
    true_value: 0.7868
    true_std: 0.0093
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7868
    sort_std: 0.0093
    is_best: false
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.7834
    std: 0.0186
    paper_value: 0.7834
    paper_std: 0.0186
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 93
    true_value: 0.7834
    true_std: 0.0186
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7834
    sort_std: 0.0186
    is_best: false
  - model: d-DRFWL(2) GNN
    model_key: d-drfwl(2) gnn
    model_plain: d-DRFWL(2) GNN
    value: 0.7818
    std: 0.0219
    paper_value: 0.7818
    paper_std: 0.0219
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 103
    true_value: 0.7818
    true_std: 0.0219
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7818
    sort_std: 0.0219
    is_best: false
  - model: Deep LRP
    model_key: deep lrp
    model_plain: Deep LRP
    value: 0.7719
    std: 0.014
    paper_value: 0.7719
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 132
    true_value: 0.7719
    true_std: 0.014
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7719
    sort_std: 0.014
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id005
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
  - model: GNNAK+
    model_key: gnnak+
    model_plain: GNNAK+
    value: 0.293
    std: 0.0044
    paper_value: 0.293
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (labeled exp-zinc in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 16
    true_value: 0.293
    true_std: 0.0044
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.293
    sort_std: 0.0044
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.2885
    std: 0.003
    paper_value: 0.2885
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (labeled exp-zinc in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 24
    true_value: 0.2885
    true_std: 0.003
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2885
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.2838
    std: 0.0035
    paper_value: 0.2838
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (labeled exp-zinc in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 29
    true_value: 0.2838
    true_std: 0.0035
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2838
    sort_std: 0.0035
    is_best: false
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.2832
    std: 0.0041
    paper_value: 0.2832
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (labeled exp-zinc in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 30
    true_value: 0.2832
    true_std: 0.0041
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2832
    sort_std: 0.0041
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2703
    std: 0.0023
    paper_value: 0.2703
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (labeled exp-zinc in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 41
    true_value: 0.2703
    true_std: 0.0024
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2703
    sort_std: 0.0024
    is_best: false
  - model: d-DRFWL(2) GNN
    model_key: d-drfwl(2) gnn
    model_plain: d-DRFWL(2) GNN
    value: 0.2538
    std: 0.0019
    paper_value: 0.2538
    paper_std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (labeled exp-zinc in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 49
    true_value: 0.2538
    true_std: 0.0019
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2538
    sort_std: 0.0019
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: OGB
  datasets:
  - *id004
  - *id005
- benchmark: Quantum Chemistry
  datasets:
  - *id006
main_figure: /figures/2309.04941/main_figure.png
---

