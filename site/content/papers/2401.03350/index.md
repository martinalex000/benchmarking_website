---
title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
  Networks
arxiv_id: '2401.03350'
authors: []
published_date: Jan 2024
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
results:
- &id001
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
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
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HAC (BFS)
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
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
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
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: VANILLA
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
    is_best: false
    global_rank: null
  - model: G-ΔUQ
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
    is_best: false
    global_rank: null
  - model: Pretr. G-ΔUQ
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
    is_best: false
    global_rank: null
  - model: No G-$\Delta$UQ
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
    is_best: false
    global_rank: null
  - model: G-$\Delta$UQ
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
    is_best: false
    global_rank: null
  - model: CAGCN
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
    is_best: false
    global_rank: null
  - model: Dirichlet
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
    is_best: false
    global_rank: null
  - model: ETS
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
    is_best: false
    global_rank: null
  - model: GATS
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
    is_best: false
    global_rank: null
  - model: IRM
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
    is_best: false
    global_rank: null
  - model: Orderinvariant
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
    is_best: false
    global_rank: null
  - model: Spline
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
    is_best: false
    global_rank: null
  - model: VS
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
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GSM++ (MoT)
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
    date_iso: ''
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: NeuralWalker
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
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GPS-DENS + LPE
    metric_values:
    - 0.98
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 61
  - model: GPS + LPE + G-$\Delta$UQ
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
    is_best: false
    global_rank: 69
  - model: GPS+LapPE
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
    is_best: false
    global_rank: 57
  - model: GPS (Pretrained) + LPE + G-$\Delta$UQ
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
    is_best: false
    global_rank: 76
  - model: GatedGCN-DENS + LPE
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
    is_best: false
    global_rank: 78
  - model: GatedGCN-DENS
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
    is_best: false
    global_rank: 80
  - model: GatedGCN-DENS + LPE + G-$\Delta$UQ
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
    is_best: false
    global_rank: 83
  - model: GatedGCN+LapPE
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
    params_millions: 0.502
    is_best: false
    global_rank: 86
  - model: GatedGCN + G-$\Delta$UQ
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
    is_best: false
    global_rank: 85
  - model: GatedGCN
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
    params_millions: 0.502
    is_best: false
    global_rank: 4
  - model: VANILLA
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
    is_best: false
    global_rank: null
  - model: G-$\Delta$UQ
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
    is_best: false
    global_rank: null
  - model: Pretr. G-\Delta UQ
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
    is_best: false
    global_rank: null
  - model: GatedGCN Ensembling
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
    is_best: false
    global_rank: null
  - model: GatedGCN + G-$\Delta$UQ Ensembling
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
    is_best: false
    global_rank: null
  - model: GPS + LPE Ensembling
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
    is_best: false
    global_rank: null
  - model: GPS + LPE + G-$\Delta$UQ Ensembling
    metric_values:
    - null
    - 0.014
    - null
    metric_stds:
    - null
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
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

