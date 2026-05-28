---
title: Bundle Neural Networks for message diffusion on graphs
arxiv_id: '2405.15540'
source_url: ''
authors: []
published_date: May 2024
published_date_iso: 2024-05
abstract: The dominant paradigm for learning on graphs is message passing. Despite
  being a strong inductive bias, the local message passing mechanism faces challenges
  such as over-smoothing, over-squashing, and limited expressivity. To address these
  issues, we introduce Bundle Neural Networks (BuNNs), a novel graph neural network
  architecture that operates via message diffusion on flat vector bundles — geometrically
  inspired structures that assign to each node a vector space and an orthogonal map.
  A BuNN layer evolves node features through a diffusion-type partial differential
  equation, where its discrete form acts as a special case of the recently introduced
  Sheaf Neural Network (SNN), effectively alleviating over-smoothing. The continuous
  nature of message diffusion enables BuNNs to operate at larger scales, reducing
  over-squashing. We establish the universality of BuNNs in approximating feature
  transformations on infinite families of graphs with injective positional encodings,
  marking the first positive expressivity result of its kind. We support our claims
  with formal analysis and synthetic experiments. Empirically, BuNNs perform strongly
  on heterophilic and long-range tasks, which demonstrates their robustness on a diverse
  range of challenging real-world tasks.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- BuNN
mrr: 0.1264
adjusted_mrr: 0.1264
mrr_dataset_count: 7
benchmark_categories:
- Heterophilic Graphs
- LRGB
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id002
  dataset: Amazon-ratings
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.5592
    std: 0.0043
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
    sort_value: 0.5592
    sort_std: 0.0043
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4909
    std: 0.0063
    paper_value: 0.4909
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 2
    true_value: 0.5554
    true_std: 0.0051
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0645
    value_note: ''
    paper_rank: 53
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.5554
    sort_std: 0.0051
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.0021
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
    sort_value: 0.554
    sort_std: 0.0021
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.5496
    std: 0.0222
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
    sort_value: 0.5496
    sort_std: 0.0222
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.487
    std: 0.0063
    paper_value: 0.487
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 17
    true_value: 0.538
    true_std: 0.0
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.051000000000000045
    value_note: ''
    paper_rank: 58
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.538
    sort_std: 0.0
    is_best: false
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.5374
    std: 0.0051
    paper_value: 0.5374
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 18
    true_value: 0.5374
    true_std: 0.0051
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5374
    sort_std: 0.0051
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.5363
    std: 0.0039
    paper_value: 0.5363
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 20
    true_value: 0.5363
    true_std: 0.0039
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5363
    sort_std: 0.0039
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.5218
    std: 0.008
    paper_value: 0.5218
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 34
    true_value: 0.527
    true_std: 0.0062
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005199999999999982
    value_note: global 0.5270 within std
    paper_rank: 36
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.527
    sort_std: 0.0062
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5117
    std: 0.0066
    paper_value: 0.5117
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 43
    true_value: 0.5117
    true_std: 0.0066
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5117
    sort_std: 0.0066
    is_best: false
  - model: NSD
    model_key: nsd
    model_plain: NSD
    value: 0.4276
    std: 0.0054
    paper_value: 0.4276
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 86
    true_value: 0.4276
    true_std: 0.0054
    value_gap_source_arxiv: '2405.15540'
    value_gap_source_title: Bundle Neural Networks for message diffusion on graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4276
    sort_std: 0.0054
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9906999999999999
    std: 0.0025
    metric: ROC-AUC
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
    global_rank: 1
    sort_value: 0.9906999999999999
    sort_std: 0.0025
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9899
    std: 0.0016
    paper_value: 0.9899
    paper_std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 2
    true_value: 0.9899
    true_std: 0.0016
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9899
    sort_std: 0.0016
    is_best: true
  - model: Tango<sub>GPS</sub>
    model_key: tango\textsubscript{gps}
    model_plain: TangoGPS
    value: 0.9839
    std: 0.0054
    metric: ROC-AUC
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
    global_rank: 3
    sort_value: 0.9839
    sort_std: 0.0054
    is_best: true
  - model: Tango<sub>GatedGCN</sub>
    model_key: tango\textsubscript{gatedgcn}
    model_plain: TangoGatedGCN
    value: 0.9832
    std: 0.0059
    metric: ROC-AUC
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
    global_rank: 4
    sort_value: 0.9832
    sort_std: 0.0059
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8975
    std: 0.0052
    paper_value: 0.8975
    paper_std: 0.0052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 5
    true_value: 0.9786
    true_std: 0.0024
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08110000000000006
    value_note: ''
    paper_rank: 76
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.9786
    sort_std: 0.0024
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9201
    std: 0.0068
    paper_value: 0.9201
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 8
    true_value: 0.9773
    true_std: 0.0073
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05719999999999992
    value_note: ''
    paper_rank: 50
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.9773
    sort_std: 0.0073
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.9229
    std: 0.0047
    paper_value: 0.9229
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 32
    true_value: 0.9391
    true_std: 0.0035
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016199999999999992
    value_note: ''
    paper_rank: 48
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.9391
    sort_std: 0.0035
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.9351
    std: 0.0057
    paper_value: 0.9351
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 39
    true_value: 0.9351
    true_std: 0.0057
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9351
    sort_std: 0.0057
    is_best: false
  - model: NSD
    model_key: nsd
    model_plain: NSD
    value: 0.9215
    std: 0.0084
    paper_value: 0.9215
    paper_std: 0.0084
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 50
    true_value: 0.9215
    true_std: 0.0084
    value_gap_source_arxiv: '2405.15540'
    value_gap_source_title: Bundle Neural Networks for message diffusion on graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9215
    sort_std: 0.0084
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.9185
    std: 0.0076
    paper_value: 0.9185
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 52
    true_value: 0.9185
    true_std: 0.0076
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9185
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
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
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.7276
    std: 0.0065
    paper_value: 0.7276
    paper_std: 0.0065
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 7
    true_value: 0.7276
    true_std: 0.0065
    value_gap_source_arxiv: '2405.15540'
    value_gap_source_title: Bundle Neural Networks for message diffusion on graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7276
    sort_std: 0.0065
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.686
    std: 0.005
    paper_value: 0.686
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040099999999999913
    value_note: ''
    paper_rank: 87
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6765
    std: 0.0047
    paper_value: 0.6765
    paper_std: 0.0047
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02410000000000001
    value_note: ''
    paper_rank: 111
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.6621
    std: 0.0067
    paper_value: 0.6621
    paper_std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 142
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6534
    std: 0.0091
    paper_value: 0.6534
    paper_std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 154
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006700000000000039
    value_note: global 0.6601 within std
    paper_rank: 172
    rank_delta: 18
    rank_delta_abs: 18
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 202
    true_value: 0.6439
    true_std: 0.0075
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
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
  metric: AP
  higher_is_better: true
- &id007
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
    value: 0.246
    std: 0.0007
    paper_value: 0.246
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.003899999999999987
    value_note: ''
    paper_rank: 54
    rank_delta: 51
    rank_delta_abs: 51
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
    value: 0.2477
    std: 0.0009
    paper_value: 0.2477
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.004599999999999993
    value_note: ''
    paper_rank: 89
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.2463
    std: 0.0012
    paper_value: 0.2463
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 61
    true_value: 0.2463
    true_std: 0.0012
    value_gap_source_arxiv: '2405.15540'
    value_gap_source_title: Bundle Neural Networks for message diffusion on graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2463
    sort_std: 0.0012
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.2473
    std: 0.0017
    paper_value: 0.2473
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0017
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
    value: 0.2509
    std: 0.0014
    paper_value: 0.2509
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.2500 within std
    paper_rank: 148
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 189
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
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
  metric: MAE
  higher_is_better: false
- &id005
  dataset: Questions
  rows:
  - model: IM-CO-GNN(Σ,Σ)
    model_key: im-co-gnn(σ,σ)
    model_plain: IM-CO-GNN(Σ,Σ)
    value: 0.8049
    std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_display: May 2025
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.8049
    sort_std: 0.0092
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.8039000000000001
    std: 0.0104
    metric: ROC-AUC
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
    global_rank: 2
    sort_value: 0.8039000000000001
    sort_std: 0.0104
    is_best: true
  - model: Tango<sub>GatedGCN</sub>
    model_key: tango\textsubscript{gatedgcn}
    model_plain: TangoGatedGCN
    value: 0.8039
    std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    global_rank: 3
    sort_value: 0.8039
    sort_std: 0.0104
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7609
    std: 0.0127
    paper_value: 0.7609
    paper_std: 0.0127
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 13
    true_value: 0.7902
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029299999999999993
    value_note: ''
    paper_rank: 46
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.7902
    sort_std: 0.006
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.7875
    std: 0.0109
    paper_value: 0.7875
    paper_std: 0.0109
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 17
    true_value: 0.7875
    true_std: 0.0109
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7875
    sort_std: 0.0109
    is_best: true
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.7805
    std: 0.0093
    paper_value: 0.7805
    paper_std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 21
    true_value: 0.7805
    true_std: 0.0093
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7805
    sort_std: 0.0093
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.7795
    std: 0.0068
    paper_value: 0.7795
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 23
    true_value: 0.7795000000000001
    true_std: 0.0068000000000000005
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7795000000000001
    sort_std: 0.0068000000000000005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7743
    std: 0.012
    paper_value: 0.7743
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 24
    true_value: 0.7795
    true_std: 0.0051
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005199999999999982
    value_note: global 0.7795 within std
    paper_rank: 31
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7795
    sort_std: 0.0051
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.7644
    std: 0.0062
    paper_value: 0.7644
    paper_std: 0.0062
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 46
    true_value: 0.7644
    true_std: 0.0062
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7644
    sort_std: 0.0062
    is_best: false
  - model: NSD
    model_key: nsd
    model_plain: NSD
    value: 0.6969
    std: 0.0146
    paper_value: 0.6969
    paper_std: 0.0146
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 58
    true_value: 0.6969
    true_std: 0.0146
    value_gap_source_arxiv: '2405.15540'
    value_gap_source_title: Bundle Neural Networks for message diffusion on graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6969
    sort_std: 0.0146
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
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
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9175
    std: 0.0039
    paper_value: 0.9175
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 13
    true_value: 0.9175
    true_std: 0.0039000000000000003
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9175
    sort_std: 0.0039000000000000003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7369
    std: 0.0074
    paper_value: 0.7369
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 19
    true_value: 0.9127
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17579999999999996
    value_note: ''
    paper_rank: 79
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.9127
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8087
    std: 0.003
    paper_value: 0.8087
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09760000000000002
    value_note: ''
    paper_rank: 67
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8732
    std: 0.0039
    paper_value: 0.8732
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 32
    true_value: 0.8875
    true_std: 0.0041
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01429999999999998
    value_note: ''
    paper_rank: 36
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.8875
    sort_std: 0.0041
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8651
    std: 0.0073
    paper_value: 0.8651
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 44
    true_value: 0.8651000000000001
    true_std: 0.0073
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8651000000000001
    sort_std: 0.0073
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8574
    std: 0.0067
    paper_value: 0.8574
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 47
    true_value: 0.8574
    true_std: 0.0067
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8574
    sort_std: 0.0067
    is_best: false
  - model: NSD
    model_key: nsd
    model_plain: NSD
    value: 0.8041
    std: 0.0072
    paper_value: 0.8041
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 68
    true_value: 0.8041
    true_std: 0.0072
    value_gap_source_arxiv: '2405.15540'
    value_gap_source_title: Bundle Neural Networks for message diffusion on graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8041
    sort_std: 0.0072
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Tolokers
  rows:
  - model: GRAMA<sub>GCN</sub>
    model_key: grama$_{gcn}$
    model_plain: GRAMAGCN
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8591
    std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    global_rank: 3
    sort_value: 0.8591
    sort_std: 0.0074
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.8478
    std: 0.008
    paper_value: 0.8478
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 29
    true_value: 0.8478
    true_std: 0.008
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8478
    sort_std: 0.008
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8364
    std: 0.0067
    paper_value: 0.8364
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 44
    true_value: 0.838
    true_std: 0.0034
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015999999999999348
    value_note: global 0.8380 within std
    paper_rank: 49
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.0034
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8252
    std: 0.0092
    paper_value: 0.8252
    paper_std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 45
    true_value: 0.8378
    true_std: 0.0043
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012599999999999945
    value_note: ''
    paper_rank: 58
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.8378
    sort_std: 0.0043
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.837
    std: 0.0047
    paper_value: 0.837
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 48
    true_value: 0.8370000000000001
    true_std: 0.004699999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8370000000000001
    sort_std: 0.004699999999999999
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8323
    std: 0.0064
    paper_value: 0.8323
    paper_std: 0.0064
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 55
    true_value: 0.8323
    true_std: 0.0064
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8323
    sort_std: 0.0064
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8243
    std: 0.0044
    paper_value: 0.8243
    paper_std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 61
    true_value: 0.8243
    true_std: 0.0044
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.0044
    is_best: false
  - model: NSD
    model_key: nsd
    model_plain: NSD
    value: 0.7883
    std: 0.0076
    paper_value: 0.7883
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 68
    true_value: 0.7883
    true_std: 0.0076
    value_gap_source_arxiv: '2405.15540'
    value_gap_source_title: Bundle Neural Networks for message diffusion on graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7883
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
- benchmark: LRGB
  datasets:
  - *id006
  - *id007
single_proposed_model: BuNN
main_figure: /figures/2405.15540/main_figure.png
---

