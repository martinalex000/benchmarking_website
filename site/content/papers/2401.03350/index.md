---
title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
  Networks
arxiv_id: '2401.03350'
source_url: ''
authors: []
published_date: Jan 2024
published_date_iso: 2024-01
abstract: While graph neural networks (GNNs) are widely used for node and graph representation
  learning tasks, the reliability of GNN uncertainty estimates under distribution
  shifts remains relatively under-explored. Indeed, while post-hoc calibration strategies
  can be used to improve in-distribution calibration, they need not also improve calibration
  under distribution shift. However, techniques which produce GNNs with better intrinsic
  uncertainty estimates are particularly valuable, as they can always be combined
  with post-hoc strategies later. Therefore, in this work, we propose G-$ $UQ, a novel
  training framework designed to improve intrinsic GNN uncertainty estimates. Our
  framework adapts the principle of stochastic data centering to graph data through
  novel graph anchoring strategies, and is able to support partially stochastic GNNs.
  While, the prevalent wisdom is that fully stochastic networks are necessary to obtain
  reliable estimates, we find that the functional diversity induced by our anchoring
  strategies when sampling hypotheses renders this unnecessary and allows us to support
  G-$ $UQ on pretrained models. Indeed, through extensive evaluation under covariate,
  concept and graph size shifts, we show that G-$ $UQ leads to better calibrated GNNs
  for node and graph classification. Further, it also improves performance on the
  uncertainty-based tasks of out-of-distribution detection and generalization gap
  estimation. Overall, our work provides insights into uncertainty estimation for
  GNNs, and demonstrates the utility of G-$ $UQ in obtaining reliable estimates.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- G-$\Delta$UQ
- Pretr. G-\Delta UQ
- G-ΔUQ
- Pretr. G-ΔUQ
- GatedGCN + G-$\Delta$UQ
- GatedGCN + G-$\Delta$UQ Ensembling
- GPS + LPE + G-$\Delta$UQ
- GPS + LPE + G-$\Delta$UQ Ensembling
- GPS (Pretrained) + LPE + G-$\Delta$UQ
- GatedGCN-DENS + LPE + G-$\Delta$UQ
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
- GNNBenchmark
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    metric_values:
    - 0.989
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.989
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    metric_values:
    - 0.981
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.981
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    metric_values:
    - 0.976
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.976
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: VS
    model_key: vs
    model_plain: VS
    metric_values:
    - null
    - 0.602
    metric_stds:
    - null
    - 0.044
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.602
    sort_std: 0.044
    true_value: null
    true_std: null
    paper_value: 0.602
    paper_std: 0.044
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: No G-\DeltaUQ
    model_key: no g-$\delta$uq
    model_plain: No G-\DeltaUQ
    metric_values:
    - null
    - 0.599
    metric_stds:
    - null
    - 0.091
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.599
    sort_std: 0.091
    true_value: null
    true_std: null
    paper_value: 0.599
    paper_std: 0.091
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Orderinvariant
    model_key: orderinvariant
    model_plain: Orderinvariant
    metric_values:
    - null
    - 0.545
    metric_stds:
    - null
    - 0.079
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.545
    sort_std: 0.079
    true_value: null
    true_std: null
    paper_value: 0.545
    paper_std: 0.079
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: ETS
    model_key: ets
    model_plain: ETS
    metric_values:
    - null
    - 0.539
    metric_stds:
    - null
    - 0.112
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.539
    sort_std: 0.112
    true_value: null
    true_std: null
    paper_value: 0.539
    paper_std: 0.112
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: G-\DeltaUQ
    model_key: g-$\delta$uq
    model_plain: G-\DeltaUQ
    metric_values:
    - null
    - 0.525
    metric_stds:
    - null
    - 0.033
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.525
    sort_std: 0.033
    true_value: null
    true_std: null
    paper_value: 0.525
    paper_std: 0.033
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Spline
    model_key: spline
    model_plain: Spline
    metric_values:
    - null
    - 0.472
    metric_stds:
    - null
    - 0.031
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.472
    sort_std: 0.031
    true_value: null
    true_std: null
    paper_value: 0.472
    paper_std: 0.031
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GATS
    model_key: gats
    model_plain: GATS
    metric_values:
    - null
    - 0.455
    metric_stds:
    - null
    - 0.057
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.455
    sort_std: 0.057
    true_value: null
    true_std: null
    paper_value: 0.455
    paper_std: 0.057
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: CAGCN
    model_key: cagcn
    model_plain: CAGCN
    metric_values:
    - null
    - 0.355
    metric_stds:
    - null
    - 0.227
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.355
    sort_std: 0.227
    true_value: null
    true_std: null
    paper_value: 0.355
    paper_std: 0.227
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: IRM
    model_key: irm
    model_plain: IRM
    metric_values:
    - null
    - 0.352
    metric_stds:
    - null
    - 0.037
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.352
    sort_std: 0.037
    true_value: null
    true_std: null
    paper_value: 0.352
    paper_std: 0.037
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: VANILLA
    model_key: vanilla
    model_plain: VANILLA
    metric_values:
    - 0.35
    - null
    metric_stds:
    - 0.014
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.35
    sort_std: 0.014
    true_value: null
    true_std: null
    paper_value: 0.35
    paper_std: 0.014
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: G-ΔUQ
    model_key: g-δuq
    model_plain: G-ΔUQ
    metric_values:
    - 0.338
    - null
    metric_stds:
    - 0.023
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.338
    sort_std: 0.023
    true_value: null
    true_std: null
    paper_value: 0.338
    paper_std: 0.023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Pretr. G-ΔUQ
    model_key: pretr. g-δuq
    model_plain: Pretr. G-ΔUQ
    metric_values:
    - 0.324
    - null
    metric_stds:
    - 0.055
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.324
    sort_std: 0.055
    true_value: null
    true_std: null
    paper_value: 0.324
    paper_std: 0.055
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Dirichlet
    model_key: dirichlet
    model_plain: Dirichlet
    metric_values:
    - null
    - 0.299
    metric_stds:
    - null
    - 0.092
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.299
    sort_std: 0.092
    true_value: null
    true_std: null
    paper_value: 0.299
    paper_std: 0.092
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - AUROC
  - ECE
  primary_metric: Accuracy
  higher_is_better: true
- &id002
  dataset: MNIST
  is_multi_metric: true
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    metric_values:
    - 0.98932
    - null
    - null
    metric_stds:
    - 0.00076
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.98932
    sort_std: 0.00076
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    metric_values:
    - 0.9884
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
    sort_value: 0.9884
    sort_std: 0.0015
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    metric_values:
    - 0.9876
    - null
    - null
    metric_stds:
    - 0.00079
    - null
    - null
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
    global_rank: 3
    is_best: false
    sort_value: 0.9876
    sort_std: 0.00079
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    metric_values:
    - 0.947
    - 0.038
    - null
    metric_stds:
    - 0.002
    - 0.001
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.98712
    sort_std: 0.00137
    true_value: 0.98712
    true_std: 0.00137
    paper_value: 0.947
    paper_std: 0.002
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040120000000000045
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 4
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    metric_values:
    - 0.97
    - 0.026
    - null
    metric_stds:
    - 0.001
    - 0.001
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.98051
    sort_std: 0.00126
    true_value: 0.98051
    true_std: 0.00126
    paper_value: 0.97
    paper_std: 0.001
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01051000000000002
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 64
  - model: GPS-DENS + LPE
    model_key: gps-dens + lpe
    model_plain: GPS-DENS + LPE
    metric_values:
    - 0.98
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.98
    sort_std: 0.0
    true_value: 0.98
    true_std: 0.0
    paper_value: 0.98
    paper_std: 0.0
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 68
  - model: GPS + LPE + G-\DeltaUQ
    model_key: gps + lpe + g-$\delta$uq
    model_plain: GPS + LPE + G-\DeltaUQ
    metric_values:
    - 0.978
    - 0.022
    - null
    metric_stds:
    - 0.001
    - 0.001
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.978
    sort_std: 0.001
    true_value: 0.978
    true_std: 0.001
    paper_value: 0.978
    paper_std: 0.001
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 76
  - model: GPS (Pretrained) + LPE + G-\DeltaUQ
    model_key: gps (pretrained) + lpe + g-$\delta$uq
    model_plain: GPS (Pretrained) + LPE + G-\DeltaUQ
    metric_values:
    - 0.967
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.967
    sort_std: 0.002
    true_value: 0.967
    true_std: 0.002
    paper_value: 0.967
    paper_std: 0.002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 86
  - model: GatedGCN-DENS + LPE
    model_key: gatedgcn-dens + lpe
    model_plain: GatedGCN-DENS + LPE
    metric_values:
    - 0.965
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.965
    sort_std: 0.001
    true_value: 0.965
    true_std: 0.001
    paper_value: 0.965
    paper_std: 0.001
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 88
  - model: GatedGCN-DENS
    model_key: gatedgcn-dens
    model_plain: GatedGCN-DENS
    metric_values:
    - 0.963
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.963
    sort_std: 0.0002
    true_value: 0.963
    true_std: 0.0002
    paper_value: 0.963
    paper_std: 0.0002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 90
  - model: GatedGCN-DENS + LPE + G-\DeltaUQ
    model_key: gatedgcn-dens + lpe + g-$\delta$uq
    model_plain: GatedGCN-DENS + LPE + G-\DeltaUQ
    metric_values:
    - 0.954
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.954
    sort_std: 0.005
    true_value: 0.954
    true_std: 0.005
    paper_value: 0.954
    paper_std: 0.005
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 95
  - model: GatedGCN+LapPE
    model_key: gatedgcn+lappe
    model_plain: GatedGCN+LapPE
    metric_values:
    - 0.949
    - 0.036
    - null
    metric_stds:
    - 0.002
    - 0.003
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.949
    sort_std: 0.002
    true_value: 0.949
    true_std: 0.002
    paper_value: 0.949
    paper_std: 0.002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 98
  - model: GatedGCN + G-\DeltaUQ
    model_key: gatedgcn + g-$\delta$uq
    model_plain: GatedGCN + G-\DeltaUQ
    metric_values:
    - 0.949
    - 0.022
    - null
    metric_stds:
    - 0.008
    - 0.007
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.949
    sort_std: 0.008
    true_value: 0.949
    true_std: 0.008
    paper_value: 0.949
    paper_std: 0.008
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2401.03350'
    value_gap_source_title: Accurate and Scalable Estimation of Epistemic Uncertainty
      for Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 97
  - model: Pretr. G-\Delta UQ
    model_key: pretr. g-\delta uq
    model_plain: Pretr. G-\Delta UQ
    metric_values:
    - null
    - null
    - 0.774
    metric_stds:
    - null
    - null
    - 0.016
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.774
    sort_std: 0.016
    true_value: null
    true_std: null
    paper_value: 0.774
    paper_std: 0.016
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: G-\DeltaUQ
    model_key: g-$\delta$uq
    model_plain: G-\DeltaUQ
    metric_values:
    - null
    - null
    - 0.771
    metric_stds:
    - null
    - null
    - 0.002
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.771
    sort_std: 0.002
    true_value: null
    true_std: null
    paper_value: 0.771
    paper_std: 0.002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: VANILLA
    model_key: vanilla
    model_plain: VANILLA
    metric_values:
    - null
    - null
    - 0.759
    metric_stds:
    - null
    - null
    - 0.006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.759
    sort_std: 0.006
    true_value: null
    true_std: null
    paper_value: 0.759
    paper_std: 0.006
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GatedGCN Ensembling
    model_key: gatedgcn ensembling
    model_plain: GatedGCN Ensembling
    metric_values:
    - null
    - 0.024
    - null
    metric_stds:
    - null
    - 0.001
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.024
    sort_std: 0.001
    true_value: null
    true_std: null
    paper_value: 0.024
    paper_std: 0.001
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GatedGCN + G-\DeltaUQ Ensembling
    model_key: gatedgcn + g-$\delta$uq ensembling
    model_plain: GatedGCN + G-\DeltaUQ Ensembling
    metric_values:
    - null
    - 0.017
    - null
    metric_stds:
    - null
    - 0.002
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.017
    sort_std: 0.002
    true_value: null
    true_std: null
    paper_value: 0.017
    paper_std: 0.002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GPS + LPE Ensembling
    model_key: gps + lpe ensembling
    model_plain: GPS + LPE Ensembling
    metric_values:
    - null
    - 0.016
    - null
    metric_stds:
    - null
    - 0.001
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.016
    sort_std: 0.001
    true_value: null
    true_std: null
    paper_value: 0.016
    paper_std: 0.001
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GPS + LPE + G-\DeltaUQ Ensembling
    model_key: gps + lpe + g-$\delta$uq ensembling
    model_plain: GPS + LPE + G-\DeltaUQ Ensembling
    metric_values:
    - null
    - 0.014
    - null
    metric_stds:
    - null
    - 0.0
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.014
    sort_std: 0.0
    true_value: null
    true_std: null
    paper_value: 0.014
    paper_std: 0.0
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - Accuracy
  - ECE
  - AUROC
  primary_metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: GNNBenchmark
  datasets:
  - *id002
main_figure: /figures/2401.03350/main_figure.png
---

