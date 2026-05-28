---
title: Invariant-Based Diagnostics for Graph Benchmarks
arxiv_id: '2605.06462'
source_url: ''
authors: []
published_date: May 2026
published_date_iso: 2026-05
abstract: Abstract Progress on graph foundation models is hindered by benchmark practices
  that conflate the contributions of node features and graph structure, making it
  hard to tell whether a model actually learns from connectivity, or whether it even
  needs to. We propose addressing this using graph invariants, i.e., permutation-invariant,
  task-agnostic structural descriptors that serve as a diagnostic framework for graph
  benchmarks. We show that (i) invariants are more expressive than standard GNNs,
  (ii) invariants characterize structural heterogeneity within and across benchmark
  datasets, (iii) invariants predict multi-task performance, and (iv) simple invariant-based
  models are competitive with, and sometimes exceed, transformer and message-passing
  baselines across 26 datasets. Our results suggest that expressivity is not the main
  driver of predictive performance, and that on tasks where structure matters, a non-trainable
  structural proxy often matches trained message-passing models. We thus posit that
  invariant baselines should become a standard for evaluating whether structure is
  required for a task and whether a model picks up on it, serving as a stepping stone
  towards graph foundation models.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- XGBoost (agg_+_i)
- XGBoost (agg_+_subset)
- XGBoost (all_invariants)
- XGBoost (feature_agg)
- XGBoost (feature_sum)
- XGBoost (invariants_subset)
- XGBoost (sum_+_i)
- XGBoost (sum_+_subset)
- agg + I
mrr: 0.0244
adjusted_mrr: 0.0081
mrr_dataset_count: 1
benchmark_categories:
- LRGB
- TU Dortmund
- OGB
- MoleculeNet
- GraphBench
- Quantum Chemistry
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id005
  dataset: BACE
  rows:
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.868
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.868
    sort_std: 0.004
    is_best: true
  - model: Uni-Mol
    model_key: uni-mol
    model_plain: Uni-Mol
    value: 0.857
    std: 0.002
    paper_value: 0.857
    paper_std: 0.002
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.857
    sort_std: 0.002
    is_best: false
  - model: GEM
    model_key: gem
    model_plain: GEM
    value: 0.856
    std: 0.011000000000000001
    paper_value: 0.856
    paper_std: 0.011000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.856
    sort_std: 0.011000000000000001
    is_best: true
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.85
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.85
    sort_std: 0.011
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.845
    std: 0.006999999999999999
    paper_value: 0.845
    paper_std: 0.006999999999999999
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 25
    sort_value: 0.845
    sort_std: 0.006999999999999999
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.8435
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8435
    sort_std: 0.0065
    is_best: false
  - model: GROVER_base
    model_key: grover_base
    model_plain: GROVER_base
    value: 0.826
    std: 0.006999999999999999
    paper_value: 0.826
    paper_std: 0.006999999999999999
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.826
    sort_std: 0.006999999999999999
    is_best: false
  - model: MolCLR
    model_key: molclr
    model_plain: MolCLR
    value: 0.8240000000000001
    std: 0.009000000000000001
    paper_value: 0.8240000000000001
    paper_std: 0.009000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.8240000000000001
    sort_std: 0.009000000000000001
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.8239
    std: 0.0053
    paper_value: 0.8239
    paper_std: 0.0053
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.8239
    sort_std: 0.0053
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.812
    std: 0.009000000000000001
    paper_value: 0.812
    paper_std: 0.009000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 31
    sort_value: 0.812
    sort_std: 0.009000000000000001
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.81
    std: 0.013999999999999999
    paper_value: 0.81
    paper_std: 0.013999999999999999
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 15
    sort_value: 0.81
    sort_std: 0.013999999999999999
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.809
    std: 0.006
    paper_value: 0.809
    paper_std: 0.006
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 16
    sort_value: 0.809
    sort_std: 0.006
    is_best: false
  - model: N-Gram_XGB
    model_key: n-gram_xgb
    model_plain: N-Gram_XGB
    value: 0.7909999999999999
    std: 0.013000000000000001
    paper_value: 0.7909999999999999
    paper_std: 0.013000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7909999999999999
    sort_std: 0.013000000000000001
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.784
    std: 0.0
    paper_value: 0.784
    paper_std: 0.0
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 41
    sort_value: 0.784
    sort_std: 0.0
    is_best: false
  - model: N-Gram_RF
    model_key: n-gram_rf
    model_plain: N-Gram_RF
    value: 0.779
    std: 0.015
    paper_value: 0.779
    paper_std: 0.015
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.779
    sort_std: 0.015
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
  dataset: BBBP
  rows:
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.7408
    std: 0.0
    paper_value: 0.7408
    paper_std: 0.0
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7408
    sort_std: 0.0
    is_best: true
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.738
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.738
    sort_std: 0.004
    is_best: true
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.736
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.736
    sort_std: null
    is_best: false
  - model: Uni-Mol
    model_key: uni-mol
    model_plain: Uni-Mol
    value: 0.7290000000000001
    std: 0.006
    paper_value: 0.7290000000000001
    paper_std: 0.006
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7290000000000001
    sort_std: 0.006
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.725
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.725
    sort_std: 0.008
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.7240000000000001
    std: 0.016
    paper_value: 0.7240000000000001
    paper_std: 0.016
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 16
    sort_value: 0.7240000000000001
    sort_std: 0.016
    is_best: false
  - model: GEM
    model_key: gem
    model_plain: GEM
    value: 0.7240000000000001
    std: 0.004
    paper_value: 0.7240000000000001
    paper_std: 0.004
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7240000000000001
    sort_std: 0.004
    is_best: false
  - model: MolCLR
    model_key: molclr
    model_plain: MolCLR
    value: 0.722
    std: 0.021
    paper_value: 0.722
    paper_std: 0.021
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.722
    sort_std: 0.021
    is_best: true
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.71
    std: 0.003
    paper_value: 0.71
    paper_std: 0.003
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 15
    sort_value: 0.71
    sort_std: 0.003
    is_best: false
  - model: GROVER_base
    model_key: grover_base
    model_plain: GROVER_base
    value: 0.7
    std: 0.001
    paper_value: 0.7
    paper_std: 0.001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7
    sort_std: 0.001
    is_best: false
  - model: N-Gram_RF
    model_key: n-gram_rf
    model_plain: N-Gram_RF
    value: 0.6970000000000001
    std: 0.006
    paper_value: 0.6970000000000001
    paper_std: 0.006
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.6970000000000001
    sort_std: 0.006
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.695
    std: 0.001
    paper_value: 0.695
    paper_std: 0.001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 26
    sort_value: 0.695
    sort_std: 0.001
    is_best: false
  - model: N-Gram_XGB
    model_key: n-gram_xgb
    model_plain: N-Gram_XGB
    value: 0.691
    std: 0.008
    paper_value: 0.691
    paper_std: 0.008
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.691
    sort_std: 0.008
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.687
    std: 0.013000000000000001
    paper_value: 0.687
    paper_std: 0.013000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 31
    sort_value: 0.687
    sort_std: 0.013000000000000001
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.643
    std: 0.018000000000000002
    paper_value: 0.643
    paper_std: 0.018000000000000002
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 51
    sort_value: 0.643
    sort_std: 0.018000000000000002
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id003
  dataset: D&D
  rows:
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.093
    std: null
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.093
    sort_std: null
    is_best: true
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.271
    sort_std: 0.004
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.279
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.09008'
    title: City-Networks
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.279
    sort_std: 0.001
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 5.26
    std: 0.03
    paper_value: 5.26
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 5.26
    sort_std: 0.03
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 6.48
    std: null
    paper_value: 6.48
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 6.48
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 9.51
    std: null
    paper_value: 9.51
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 1
    sort_value: 9.51
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
- &id007
  dataset: Flow
  rows:
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 1.45
    std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.45
    sort_std: 0.06
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 1.49
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.49
    sort_std: 0.02
    is_best: true
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 1.73
    std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.73
    sort_std: 0.09
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 1.83
    std: 0.01
    paper_value: 1.83
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 5
    true_value: 1.83
    true_std: 0.01
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.83
    sort_std: 0.01
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 5.3
    std: 0.12
    paper_value: 5.3
    paper_std: 0.12
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 5
    true_value: 1.83
    true_std: 0.01
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 3.4699999999999998
    value_note: ''
    paper_rank: 9
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 1.83
    sort_std: 0.01
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 5.26
    std: 0.03
    paper_value: 5.26
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 5
    true_value: 1.83
    true_std: 0.01
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 3.4299999999999997
    value_note: ''
    paper_rank: 9
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 1.83
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 3.44
    std: null
    paper_value: 3.44
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 3.4387
    true_std: 0.0631
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0013000000000000789
    value_note: global 3.4387 within std
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 3.4387
    sort_std: 0.0631
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 9.6
    std: null
    paper_value: 9.6
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 3.4387
    true_std: 0.0631
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 6.1613
    value_note: ''
    paper_rank: 9
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 3.4387
    sort_std: 0.0631
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 9.51
    std: null
    paper_value: 9.51
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 3.4387
    true_std: 0.0631
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 6.0713
    value_note: ''
    paper_rank: 9
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 3.4387
    sort_std: 0.0631
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 4.27
    std: null
    paper_value: 4.27
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 4.27
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.27
    sort_std: null
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 6.38
    std: null
    paper_value: 6.38
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 4.27
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 2.1100000000000003
    value_note: ''
    paper_rank: 9
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 4.27
    sort_std: null
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 6.48
    std: null
    paper_value: 6.48
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 4.27
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 2.210000000000001
    value_note: ''
    paper_rank: 9
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 4.27
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
- &id001
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 22
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
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
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.7074
    std: 0.0032
    paper_value: 0.7074
    paper_std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 37
    true_value: 0.7074
    true_std: 0.0032
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7074
    sort_std: 0.0032
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.6988
    std: 0.0082
    paper_value: 0.6988
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 53
    true_value: 0.6988
    true_std: 0.0082
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6988
    sort_std: 0.0082
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
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
  - model: G-MLPMixer
    model_key: g-mlpmixer
    model_plain: G-MLPMixer
    value: 0.6921
    std: 0.0054
    paper_value: 0.6921
    paper_std: 0.0054
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 62
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.004899999999999904
    value_note: global 0.6970 within std
    paper_rank: 78
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.6874
    std: 0.0022
    paper_value: 0.6874
    paper_std: 0.0022
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 87
    true_value: 0.6874
    true_std: 0.0022
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6874
    sort_std: 0.0022
    is_best: false
  - model: GCN
    model_key: gcn (retuned)
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
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 88
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn (retuned)
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
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 112
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6765
    sort_std: 0.0047
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
  - model: GINE
    model_key: gine (retuned)
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
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 143
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 154
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 168
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: GPS
    model_key: gps (retuned)
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
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 173
    true_value: 0.6534
    true_std: 0.0091
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 173
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6534
    sort_std: 0.0091
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
    source_ref: Tönschhoff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
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
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
- &id002
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
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
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.246
    std: 0.0012
    paper_value: 0.246
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 56
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0012
    is_best: false
  - model: GCN
    model_key: gcn (retuned)
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
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 55
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0007
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
  - model: GINE
    model_key: gine (retuned)
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
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 80
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: G-MLPMixer
    model_key: g-mlpmixer
    model_plain: G-MLPMixer
    value: 0.2475
    std: 0.0015
    paper_value: 0.2475
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 84
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0015
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.2476
    std: 0.0002
    paper_value: 0.2476
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 89
    true_value: 0.2476
    true_std: 0.0002
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2476
    sort_std: 0.0002
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn (retuned)
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
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 90
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.0009
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
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
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
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.2506
    std: 0.0022
    paper_value: 0.2506
    paper_std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 146
    true_value: 0.2506
    true_std: 0.0022
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2506
    sort_std: 0.0022
    is_best: false
  - model: GPS
    model_key: gps (retuned)
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
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 149
    true_value: 0.2509
    true_std: 0.0014
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2509
    sort_std: 0.0014
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Tönsheff et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 174
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
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
- &id008
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
  - model: XGBoost (agg_+_i)
    model_key: xgboost (agg_+_i)
    model_plain: XGBoost (agg_+_i)
    value: 0.5846
    std: 0.0012
    paper_value: 0.5846
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
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 41
    true_value: 0.5846
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5846
    sort_std: 0.0012
    is_best: false
  - model: XGBoost (agg_+_subset)
    model_key: xgboost (agg_+_subset)
    model_plain: XGBoost (agg_+_subset)
    value: 0.5961
    std: 0.0012
    paper_value: 0.5961
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
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 42
    true_value: 0.5961
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5961
    sort_std: 0.0012
    is_best: false
  - model: XGBoost (feature_agg)
    model_key: xgboost (feature_agg)
    model_plain: XGBoost (feature_agg)
    value: 0.6047
    std: 0.0009
    paper_value: 0.6047
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 44
    true_value: 0.6047
    true_std: 0.0009
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6047
    sort_std: 0.0009
    is_best: false
  - model: XGBoost (sum_+_i)
    model_key: xgboost (sum_+_i)
    model_plain: XGBoost (sum_+_i)
    value: 0.6509
    std: 0.0002
    paper_value: 0.6509
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 46
    true_value: 0.6509
    true_std: 0.0002
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6509
    sort_std: 0.0002
    is_best: false
  - model: XGBoost (sum_+_subset)
    model_key: xgboost (sum_+_subset)
    model_plain: XGBoost (sum_+_subset)
    value: 0.6948
    std: 0.0
    paper_value: 0.6948
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 47
    true_value: 0.6948
    true_std: 0.0
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6948
    sort_std: 0.0
    is_best: false
  - model: XGBoost (feature_sum)
    model_key: xgboost (feature_sum)
    model_plain: XGBoost (feature_sum)
    value: 0.7634
    std: 0.0006
    paper_value: 0.7634
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 49
    true_value: 0.7634
    true_std: 0.0006
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7634
    sort_std: 0.0006
    is_best: false
  - model: XGBoost (all_invariants)
    model_key: xgboost (all_invariants)
    model_plain: XGBoost (all_invariants)
    value: 0.794
    std: 0.0001
    paper_value: 0.794
    paper_std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 50
    true_value: 0.794
    true_std: 0.0001
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.0001
    is_best: false
  - model: XGBoost (invariants_subset)
    model_key: xgboost (invariants_subset)
    model_plain: XGBoost (invariants_subset)
    value: 0.8919
    std: 0.0003
    paper_value: 0.8919
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 51
    true_value: 0.8919
    true_std: 0.0003
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8919
    sort_std: 0.0003
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
  - model: Uni-Mol
    model_key: uni-mol
    model_plain: Uni-Mol
    value: 0.8079999999999999
    std: 0.003
    paper_value: 0.8079999999999999
    paper_std: 0.003
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.8079999999999999
    sort_std: 0.003
    is_best: false
  - model: GEM
    model_key: gem
    model_plain: GEM
    value: 0.8059999999999999
    std: 0.009000000000000001
    paper_value: 0.8059999999999999
    paper_std: 0.009000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.8059999999999999
    sort_std: 0.009000000000000001
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.799
    std: 0.006999999999999999
    paper_value: 0.799
    paper_std: 0.006999999999999999
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.799
    sort_std: 0.006999999999999999
    is_best: false
  - model: N-Gram_XGB
    model_key: n-gram_xgb
    model_plain: N-Gram_XGB
    value: 0.787
    std: 0.004
    paper_value: 0.787
    paper_std: 0.004
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.787
    sort_std: 0.004
    is_best: false
  - model: MolCLR
    model_key: molclr
    model_plain: MolCLR
    value: 0.7809999999999999
    std: 0.005
    paper_value: 0.7809999999999999
    paper_std: 0.005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7809999999999999
    sort_std: 0.005
    is_best: false
  - model: N-Gram_RF
    model_key: n-gram_rf
    model_plain: N-Gram_RF
    value: 0.772
    std: 0.001
    paper_value: 0.772
    paper_std: 0.001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.772
    sort_std: 0.001
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.7709999999999999
    std: 0.005
    paper_value: 0.7709999999999999
    paper_std: 0.005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7709999999999999
    sort_std: 0.005
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.77
    std: 0.012
    paper_value: 0.77
    paper_std: 0.012
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 164
    sort_value: 0.77
    sort_std: 0.012
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.7695000000000001
    std: 0.0034000000000000002
    paper_value: 0.7695000000000001
    paper_std: 0.0034000000000000002
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7695000000000001
    sort_std: 0.0034000000000000002
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.757
    std: 0.013999999999999999
    paper_value: 0.757
    paper_std: 0.013999999999999999
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.757
    sort_std: 0.013999999999999999
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.682
    std: 0.011000000000000001
    paper_value: 0.682
    paper_std: 0.011000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.682
    sort_std: 0.011000000000000001
    is_best: false
  - model: GROVER_base
    model_key: grover_base
    model_plain: GROVER_base
    value: 0.625
    std: 0.009000000000000001
    paper_value: 0.625
    paper_std: 0.009000000000000001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: ''
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.625
    sort_std: 0.009000000000000001
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
- benchmark: TU Dortmund
  datasets:
  - *id003
- benchmark: OGB
  datasets:
  - *id004
- benchmark: MoleculeNet
  datasets:
  - *id005
  - *id006
- benchmark: GraphBench
  datasets:
  - *id007
- benchmark: Quantum Chemistry
  datasets:
  - *id008
---

