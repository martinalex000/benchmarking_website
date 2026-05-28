---
title: Spatio-Spectral Graph Neural Networks
arxiv_id: '2405.19121'
source_url: ''
authors: []
published_date: May 29, 2024
published_date_iso: '2024-05-29'
abstract: Spatial Message Passing Graph Neural Networks (MPGNNs) are widely used for
  learning on graph-structured data. However, key limitations of l-step MPGNNs are
  that their "receptive field" is typically limited to the l-hop neighborhood of a
  node and that information exchange between distant nodes is limited by over-squashing.
  Motivated by these limitations, we propose Spatio-Spectral Graph Neural Networks
  (S$^2$GNNs) -- a new modeling paradigm for Graph Neural Networks (GNNs) that synergistically
  combines spatially and spectrally parametrized graph filters. Parameterizing filters
  partially in the frequency domain enables global yet efficient information propagation.
  We show that S$^2$GNNs vanquish over-squashing and yield strictly tighter approximation-theoretic
  error bounds than MPGNNs. Further, rethinking graph convolutions at a fundamental
  level unlocks new design spaces. For example, S$^2$GNNs allow for free positional
  encodings that make them strictly more expressive than the 1-Weisfeiler-Lehman (WL)
  test. Moreover, to obtain general-purpose S$^2$GNNs, we propose spectrally parametrized
  filters for directed graphs. S$^2$GNNs outperform spatial MPGNNs, graph transformers,
  and graph rewirings, e.g., on the peptide long-range benchmark tasks, and are competitive
  with state-of-the-art sequence modeling. On a 40 GB GPU, S$^2$GNNs scale to millions
  of nodes.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- S$^2$GAT
- S² DirGCN
- S² GCN
- S² GCN (+PE)
- S²GNN s (Trees, direc, PE, Spec)
mrr: 0.0833
adjusted_mrr: 0.0278
mrr_dataset_count: 1
benchmark_categories:
- GNNBenchmark
- OGB
- LINKX Benchmarks
- CosmoBench
task_categories:
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id001
  dataset: CLUSTER
  rows:
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.80113
    std: 0.0013800000000000002
    metric: Accuracy
    higher_is_better: true
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
    global_rank: 1
    sort_value: 0.80113
    sort_std: 0.0013800000000000002
    is_best: true
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.8003
    std: 0.0028
    paper_value: 0.8003
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ma_graph_2023
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 2
    true_value: 0.8003
    true_std: 0.0028
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8003
    sort_std: 0.0028
    is_best: true
  - model: PPGT
    model_key: ppgt
    model_plain: PPGT
    value: 0.80027
    std: 0.00114
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_display: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.80027
    sort_std: 0.00114
    is_best: true
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.79965
    std: 0.00203
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
    sort_value: 0.79965
    sort_std: 0.00203
    is_best: true
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.7923
    std: 0.0035
    paper_value: 0.7923
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hussain_global_2022
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 14
    true_value: 0.79232
    true_std: 0.00348
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.7923 within std
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79232
    sort_std: 0.00348
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7808
    std: 0.0005
    paper_value: 0.7808
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
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 16
    true_value: 0.79128
    true_std: 0.00235
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.010479999999999934
    value_note: ''
    paper_rank: 36
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.79128
    sort_std: 0.00235
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7807
    std: 0.0004
    paper_value: 0.7807
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: shirzad_exphormer_2023
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 37
    true_value: 0.78071
    true_std: 0.00037
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 1.0000000000065512e-05
    value_note: global 0.7807 within std
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78071
    sort_std: 0.00037
    is_best: false
  - model: GPTrans-Nano
    model_key: gptrans-nano
    model_plain: GPTrans-Nano
    value: 0.7807
    std: 0.0015
    paper_value: 0.7807
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen_graph_2023
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 38
    true_value: 0.7807
    true_std: 0.0015
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7807
    sort_std: 0.0015
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.7803
    std: 0.0022
    paper_value: 0.7803
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: choi_topology-informed_2024
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 39
    true_value: 0.7803
    true_std: 0.0022
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7803
    sort_std: 0.0022
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7802
    std: 0.0018
    paper_value: 0.7802
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek_recipe_2022
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 40
    true_value: 0.7802
    true_std: 0.0018
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7802
    sort_std: 0.0018
    is_best: false
  - model: ARGNP
    model_key: argnp
    model_plain: ARGNP
    value: 0.7735
    std: 0.0005
    paper_value: 0.7735
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: cai_automatic_2022
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 51
    true_value: 0.7735
    true_std: 0.0005
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7735
    sort_std: 0.0005
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.27
    std: 0.0002
    paper_value: 0.27
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 53
    true_value: 0.77109
    true_std: 0.00872
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.50109
    value_note: ''
    paper_rank: 72
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.77109
    sort_std: 0.00872
    is_best: false
  - model: S² GCN
    model_key: s² gcn
    model_plain: S² GCN
    value: 0.4546
    std: 0.0002
    paper_value: 0.4546
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 70
    true_value: 0.4546
    true_std: 0.0002
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4546
    sort_std: 0.0002
    is_best: false
  - model: S² GCN (+PE)
    model_key: s² gcn (+pe)
    model_plain: S² GCN (+PE)
    value: 0.4546
    std: 0.0002
    paper_value: 0.4546
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 71
    true_value: 0.4546
    true_std: 0.0002
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4546
    sort_std: 0.0002
    is_best: false
  - model: GCN (+PE)
    model_key: gcn (+pe)
    model_plain: GCN (+PE)
    value: 0.2684
    std: 0.0005
    paper_value: 0.2684
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 73
    true_value: 0.2684
    true_std: 0.0005
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2684
    sort_std: 0.0005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: CS-Trees
  rows:
  - model: DeepSet (M)
    model_key: deepset (m)
    model_plain: DeepSet (M)
    value: 0.12
    std: 0.009
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.12
    sort_std: 0.009
    is_best: true
  - model: GNN (M)
    model_key: gnn (m)
    model_plain: GNN (M)
    value: 0.16
    std: 0.01
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.16
    sort_std: 0.01
    is_best: false
  - model: DeepSet (c)
    model_key: deepset (c)
    model_plain: DeepSet (c)
    value: 0.23
    std: 0.012
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.23
    sort_std: 0.012
    is_best: false
  - model: S²GNN s (Trees, direc, PE, Spec)
    model_key: s²gnn s (trees, direc, pe, spec)
    model_plain: S²GNN s (Trees, direc, PE, Spec)
    value: 0.7767
    std: 0.3306
    paper_value: 0.7767
    paper_std: 0.3306
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (app:source_dist)
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: null
    sort_value: 0.7767
    sort_std: 0.3306
    is_best: false
  - model: DirGCN (Trees, direc, no PE, no Spec)
    model_key: dirgcn (trees, direc, no pe, no spec)
    model_plain: DirGCN (Trees, direc, no PE, no Spec)
    value: 0.8166
    std: 0.5012
    paper_value: 0.8166
    paper_std: 0.5012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (app:source_dist)
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: null
    sort_value: 0.8166
    sort_std: 0.5012
    is_best: false
  - model: DirGCN (Trees, undir, no PE, no Spec)
    model_key: dirgcn (trees, undir, no pe, no spec)
    model_plain: DirGCN (Trees, undir, no PE, no Spec)
    value: 1.2887
    std: 0.1195
    paper_value: 1.2887
    paper_std: 0.1195
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (app:source_dist)
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: null
    sort_value: 1.2887
    sort_std: 0.1195
    is_best: false
  metric: R2
  higher_is_better: false
- &id003
  dataset: arxiv-year
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.6603
    std: 0.002
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
    global_rank: 1
    sort_value: 0.6603
    sort_std: 0.002
    is_best: true
  - model: S² DirGCN
    model_key: s² dirgcn
    model_plain: S² DirGCN
    value: 0.6495
    std: 0.0033
    paper_value: 0.6495
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 2
    true_value: 0.6495
    true_std: 0.0033
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6495
    sort_std: 0.0033
    is_best: false
  - model: FaberNet
    model_key: fabernet
    model_plain: FaberNet
    value: 0.6462
    std: 0.0101
    paper_value: 0.6462
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Koke et al. 2024
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 3
    true_value: 0.6462
    true_std: 0.0101
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6462
    sort_std: 0.0101
    is_best: false
  - model: DirGCN (tuned)
    model_key: dirgcn (tuned)
    model_plain: DirGCN (tuned)
    value: 0.6444
    std: 0.0027
    paper_value: 0.6444
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
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 4
    true_value: 0.6444
    true_std: 0.0027
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6444
    sort_std: 0.0027
    is_best: false
  - model: DiGCN
    model_key: digcn
    model_plain: DiGCN
    value: 0.6408
    std: 0.0026
    paper_value: 0.6408
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 5
    true_value: 0.6408
    true_std: 0.0026
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6408
    sort_std: 0.0026
    is_best: false
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.6408
    std: 0.003
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
    global_rank: 6
    sort_value: 0.6408
    sort_std: 0.003
    is_best: false
  - model: Grad. Gating
    model_key: grad. gating
    model_plain: Grad. Gating
    value: 0.633
    std: 0.0184
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
    global_rank: 7
    sort_value: 0.633
    sort_std: 0.0184
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: ogbn-products
  rows:
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.9334
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 1
    sort_value: 0.9334
    sort_std: 0.0006
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9115
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.9115
    sort_std: 0.0004
    is_best: false
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.8736
    std: 0.0007
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
    global_rank: 3
    sort_value: 0.8736
    sort_std: 0.0007
    is_best: false
  - model: S^2GAT
    model_key: s$^2$gat
    model_plain: S^2GAT
    value: 0.811
    std: 0.007
    paper_value: 0.811
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 12
    true_value: 0.811
    true_std: 0.007
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.811
    sort_std: 0.007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.798
    std: 0.003
    paper_value: 0.798
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
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    global_rank: 19
    true_value: 0.798
    true_std: 0.003
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.798
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: GNNBenchmark
  datasets:
  - *id001
- benchmark: OGB
  datasets:
  - *id002
- benchmark: LINKX Benchmarks
  datasets:
  - *id003
- benchmark: CosmoBench
  datasets:
  - *id004
main_figure: /figures/2405.19121/main_figure.png
---

