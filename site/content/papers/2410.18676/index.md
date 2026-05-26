---
title: Homomorphism Counts as Structural Encodings for Graph Learning
arxiv_id: '2410.18676'
source_url: ''
authors: []
published_date: Oct 2024
published_date_iso: 2024-10
abstract: Graph Transformers are popular neural networks that extend the well-known
  Transformer architecture to the graph domain. These architectures operate by applying
  self-attention on graph nodes and incorporating graph structure through the use
  of positional encodings (e.g., Laplacian positional encoding) or structural encodings
  (e.g., random-walk structural encoding). The quality of such encodings is critical,
  since they provide the necessary graph inductive biases to condition the model on
  graph structure. In this work, we propose motif structural encoding ( ) as a flexible
  and powerful structural encoding framework based on counting graph homomorphisms.
  Theoretically, we compare the expressive power of to random-walk structural encoding
  and relate both encodings to the expressive power of standard message passing neural
  networks. Empirically, we observe that outperforms other well-known positional and
  structural encodings across a range of architectures, and it achieves state-of-the-art
  performance on a widely studied molecular property prediction dataset.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- MOSE
- MLP-E (MoSE)
- GIN-E (MoSE)
- GIN-E+VN (MoSE)
- GT-E (MoSE)
- GPS (MoSE)
- GRIT+MoSE
- R-GCN (MoSE)
- GPS_small+MoSE_S
- GPS_big+MoSE_S
- GPS_small+MoSE_Omega
- GPS_big+MoSE_Omega
- GT+MoSE_S
- GT+MoSE_Omega
mrr: 0.025
adjusted_mrr: 0.025
mrr_dataset_count: 3
benchmark_categories:
- Classic
- LRGB
- GNNBenchmark
- OGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id004
  dataset: CIFAR10
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.8375
    std: 0.00141
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.8375
    sort_std: 0.00141
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.80027
    std: 0.00185
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
    global_rank: 2
    sort_value: 0.80027
    sort_std: 0.00185
    is_best: false
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.79067
    std: 0.00269
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.79067
    sort_std: 0.00269
    is_best: false
  - model: GPS_big+MoSE_S
    model_key: gps_big+mose_s
    model_plain: GPS_big+MoSE_S
    value: 0.75
    std: 0.0059
    paper_value: 0.75
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.75
    true_std: 0.0059
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.0059
    is_best: false
  - model: GPS_big+MoSE_Omega
    model_key: gps_big+mose_omega
    model_plain: GPS_big+MoSE_Omega
    value: 0.7473
    std: 0.0064
    paper_value: 0.7473
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 33
    true_value: 0.7473
    true_std: 0.0064
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7473
    sort_std: 0.0064
    is_best: false
  - model: MOSE
    model_key: mose
    model_plain: MOSE
    value: 0.735
    std: 0.0044
    paper_value: 0.735
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 41
    true_value: 0.735
    true_std: 0.0044
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.0044
    is_best: false
  - model: GPS_small+MoSE_Omega
    model_key: gps_small+mose_omega
    model_plain: GPS_small+MoSE_Omega
    value: 0.735
    std: 0.0044
    paper_value: 0.735
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 42
    true_value: 0.735
    true_std: 0.0044
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.0044
    is_best: false
  - model: GT+MoSE_Omega
    model_key: gt+mose_omega
    model_plain: GT+MoSE_Omega
    value: 0.735
    std: 0.0044
    paper_value: 0.735
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 43
    true_value: 0.735
    true_std: 0.0044
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.0044
    is_best: false
  - model: GPS_small+MoSE_S
    model_key: gps_small+mose_s
    model_plain: GPS_small+MoSE_S
    value: 0.7334
    std: 0.005
    paper_value: 0.7334
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 45
    true_value: 0.7334
    true_std: 0.005
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7334
    sort_std: 0.005
    is_best: false
  - model: SignNet DeepSets
    model_key: signnet deepsets
    model_plain: SignNet DeepSets
    value: 0.7237
    std: 0.0034
    paper_value: 0.7237
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 52
    true_value: 0.7237
    true_std: 0.0034
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7237
    sort_std: 0.0034
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.7231
    std: 0.0034
    paper_value: 0.7231
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: gps
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 56
    true_value: 0.7231
    true_std: 0.0034
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7231
    sort_std: 0.0034
    is_best: false
  - model: LapPE
    model_key: lappe
    model_plain: LapPE
    value: 0.7231
    std: 0.0034
    paper_value: 0.7231
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 55
    true_value: 0.7231
    true_std: 0.0034
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7231
    sort_std: 0.0034
    is_best: false
  - model: PEG^LapEig
    model_key: peg^lapeig
    model_plain: PEG^LapEig
    value: 0.721
    std: 0.0046
    paper_value: 0.721
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 62
    true_value: 0.721
    true_std: 0.0046
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.0046
    is_best: false
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.7196
    std: 0.004
    paper_value: 0.7196
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 65
    true_value: 0.7196
    true_std: 0.004
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7196
    sort_std: 0.004
    is_best: false
  - model: SignNet MLP
    model_key: signnet mlp
    model_plain: SignNet MLP
    value: 0.7174
    std: 0.006
    paper_value: 0.7174
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 71
    true_value: 0.7174
    true_std: 0.006
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7174
    sort_std: 0.006
    is_best: false
  - model: None
    model_key: none
    model_plain: None
    value: 0.7149
    std: 0.0019
    paper_value: 0.7149
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 73
    true_value: 0.7149
    true_std: 0.0019
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7149
    sort_std: 0.0019
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: MNIST
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.98932
    std: 0.00076
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.98932
    sort_std: 0.00076
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9884
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.9884
    sort_std: 0.0015
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9876
    std: 0.00079
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
    global_rank: 3
    sort_value: 0.9876
    sort_std: 0.00079
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.96485
    std: 0.00252
    paper_value: 0.96485
    paper_std: 0.00252
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 28
    true_value: 0.98285
    true_std: 0.00103
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018000000000000016
    value_note: ''
    paper_rank: 84
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.98285
    sort_std: 0.00103
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.98173
    std: 0.00087
    paper_value: 0.98173
    paper_std: 0.00087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 41
    true_value: 0.98173
    true_std: 0.00087
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98173
    sort_std: 0.00087
    is_best: false
  - model: GPS (MoSE)
    model_key: gps (mose)
    model_plain: GPS (MoSE)
    value: 0.98135
    std: 2.0e-05
    paper_value: 0.98135
    paper_std: 2.0e-05
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.98135
    true_std: 2.0e-05
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98135
    sort_std: 2.0e-05
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.98108
    std: 0.00111
    paper_value: 0.98108
    paper_std: 0.00111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 54
    true_value: 0.98108
    true_std: 0.00111
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98108
    sort_std: 0.00111
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.98051
    std: 0.00126
    paper_value: 0.98051
    paper_std: 0.00126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 61
    true_value: 0.98051
    true_std: 0.00126
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98051
    sort_std: 0.00126
    is_best: false
  - model: CRaW1
    model_key: craw1
    model_plain: CRaW1
    value: 0.97944
    std: 0.0005
    paper_value: 0.97944
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 69
    true_value: 0.97944
    true_std: 0.0005
    value_gap_source_arxiv: '2504.12588'
    value_gap_source_title: Plain Transformers Can be Powerful Graph Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.97944
    sort_std: 0.0005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.95535
    std: 0.00205
    paper_value: 0.95535
    paper_std: 0.00205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 87
    true_value: 0.9554
    true_std: 0.0021
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 4.999999999999449e-05
    value_note: global 0.9554 within std
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9554
    sort_std: 0.0021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: PCQM4Mv2
  rows:
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.0831
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_display: Feb 2025
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0831
    sort_std: null
    is_best: true
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.0838
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_display: Feb 2025
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0838
    sort_std: null
    is_best: false
  - model: GRIT 2-QiQRW
    model_key: grit 2-qiqrw
    model_plain: GRIT 2-QiQRW
    value: 0.0838
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0838
    sort_std: null
    is_best: false
  - model: MOSE
    model_key: mose
    model_plain: MOSE
    value: 0.1133
    std: 0.0014
    paper_value: 0.1133
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 29
    true_value: 0.1133
    true_std: 0.0014
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1133
    sort_std: 0.0014
    is_best: false
  - model: SignNet DeepSets
    model_key: signnet deepsets
    model_plain: SignNet DeepSets
    value: 0.1144
    std: 0.0002
    paper_value: 0.1144
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 30
    true_value: 0.1144
    true_std: 0.0002
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1144
    sort_std: 0.0002
    is_best: false
  - model: SignNet MLP
    model_key: signnet mlp
    model_plain: SignNet MLP
    value: 0.1158
    std: 0.0008
    paper_value: 0.1158
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.1158
    true_std: 0.0008
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1158
    sort_std: 0.0008
    is_best: false
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.1159
    std: 0.0004
    paper_value: 0.1159
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 32
    true_value: 0.1159
    true_std: 0.0004
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1159
    sort_std: 0.0004
    is_best: false
  - model: LapPE
    model_key: lappe
    model_plain: LapPE
    value: 0.1201
    std: 0.0003
    paper_value: 0.1201
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 36
    true_value: 0.1201
    true_std: 0.0003
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1201
    sort_std: 0.0003
    is_best: false
  - model: PEG^LapEig
    model_key: peg^lapeig
    model_plain: PEG^LapEig
    value: 0.1209
    std: 0.0003
    paper_value: 0.1209
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 37
    true_value: 0.1209
    true_std: 0.0003
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1209
    sort_std: 0.0003
    is_best: false
  - model: None
    model_key: none
    model_plain: None
    value: 0.1355
    std: 0.0035
    paper_value: 0.1355
    paper_std: 0.0035
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.1355
    true_std: 0.0035
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1355
    sort_std: 0.0035
    is_best: false
  metric: MAE
  higher_is_better: false
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
  - model: GT+MoSE_S
    model_key: gt+mose_s
    model_plain: GT+MoSE_S
    value: 0.635
    std: 0.011
    paper_value: 0.635
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 213
    true_value: 0.635
    true_std: 0.011
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 213
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.635
    sort_std: 0.011
    is_best: false
  - model: GT+MoSE_Omega
    model_key: gt+mose_omega
    model_plain: GT+MoSE_Omega
    value: 0.629
    std: 0.011
    paper_value: 0.629
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 222
    true_value: 0.629
    true_std: 0.011
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 222
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.629
    sort_std: 0.011
    is_best: false
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.625
    std: 0.012
    paper_value: 0.625
    paper_std: 0.012
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 228
    true_value: 0.625
    true_std: 0.012
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 228
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.625
    sort_std: 0.012
    is_best: false
  - model: GT-E
    model_key: gt-e (none)
    model_plain: GT-E
    value: 0.447
    std: 0.017
    paper_value: 0.447
    paper_std: 0.017
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 305
    true_value: 0.447
    true_std: 0.017
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 305
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.447
    sort_std: 0.017
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
  - model: GT+MoSE_Omega
    model_key: gt+mose_omega
    model_plain: GT+MoSE_Omega
    value: 0.318
    std: 0.01
    paper_value: 0.318
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 281
    true_value: 0.318
    true_std: 0.01
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 281
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.318
    sort_std: 0.01
    is_best: false
  - model: GT+MoSE_S
    model_key: gt+mose_s
    model_plain: GT+MoSE_S
    value: 0.339
    std: 0.007
    paper_value: 0.339
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 288
    true_value: 0.339
    true_std: 0.007
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 288
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.339
    sort_std: 0.007
    is_best: false
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.344
    std: 0.009
    paper_value: 0.344
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 294
    true_value: 0.344
    true_std: 0.009
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 294
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.344
    sort_std: 0.009
    is_best: false
  - model: GT-E
    model_key: gt-e (none)
    model_plain: GT-E
    value: 0.454
    std: 0.027
    paper_value: 0.454
    paper_std: 0.027
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 332
    true_value: 0.454
    true_std: 0.027
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 332
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.454
    sort_std: 0.027
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
    date: '2024-05-05'
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
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
    paper_rank: 137
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.063
    std: 0.001
    paper_value: 0.063
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04
    value_note: ''
    paper_rank: 64
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.002
    paper_value: 0.07
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 104
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: GRIT+MoSE
    model_key: grit+mose
    model_plain: GRIT+MoSE
    value: 0.056
    std: 0.001
    paper_value: 0.056
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 44
    true_value: 0.056
    true_std: 0.001
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.056
    sort_std: 0.001
    is_best: false
  - model: GRIT+RRWP
    model_key: grit+rrwp
    model_plain: GRIT+RRWP
    value: 0.059
    std: 0.002
    paper_value: 0.059
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 57
    true_value: 0.059
    true_std: 0.002
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.059
    sort_std: 0.002
    is_best: false
  - model: MOSE
    model_key: mose
    model_plain: MOSE
    value: 0.062
    std: 0.002
    paper_value: 0.062
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 62
    true_value: 0.062
    true_std: 0.002
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.062
    sort_std: 0.002
    is_best: false
  - model: GPS (MoSE)
    model_key: gps (mose)
    model_plain: GPS (MoSE)
    value: 0.062
    std: 0.002
    paper_value: 0.062
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 63
    true_value: 0.062
    true_std: 0.002
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.062
    sort_std: 0.002
    is_best: false
  - model: GIN-E+VN (MoSE)
    model_key: gin-e+vn (mose)
    model_plain: GIN-E+VN (MoSE)
    value: 0.068
    std: 0.004
    paper_value: 0.068
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 88
    true_value: 0.068
    true_std: 0.004
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.068
    sort_std: 0.004
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.069
    std: 0.001
    paper_value: 0.069
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 93
    true_value: 0.0681
    true_std: 0.0004
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.0681 within std
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0681
    sort_std: 0.0004
    is_best: false
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.07
    std: 0.002
    paper_value: 0.07
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 105
    true_value: 0.07
    true_std: 0.002
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.07
    sort_std: 0.002
    is_best: false
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 0.122
    std: 0.003
    paper_value: 0.122
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 121
    true_value: 0.074
    true_std: 0.003
    value_gap_source_arxiv: '2310.19285'
    value_gap_source_title: Facilitating Graph Neural Networks with Random Walk on
      Simplicial Complexes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.048
    value_note: ''
    paper_rank: 198
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.074
    sort_std: 0.003
    is_best: false
  - model: SignNet DeepSets
    model_key: signnet deepsets
    model_plain: SignNet DeepSets
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
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 138
    true_value: 0.079
    true_std: 0.006
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.079
    sort_std: 0.006
    is_best: false
  - model: GIN-E+VN (RWSE)
    model_key: gin-e+vn (rwse)
    model_plain: GIN-E+VN (RWSE)
    value: 0.085
    std: 0.003
    paper_value: 0.085
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 154
    true_value: 0.085
    true_std: 0.003
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.085
    sort_std: 0.003
    is_best: false
  - model: GT-E (MoSE)
    model_key: gt-e (mose)
    model_plain: GT-E (MoSE)
    value: 0.089
    std: 0.018
    paper_value: 0.089
    paper_std: 0.018
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 162
    true_value: 0.089
    true_std: 0.018
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.089
    sort_std: 0.018
    is_best: false
  - model: SignNet MLP
    model_key: signnet mlp
    model_plain: SignNet MLP
    value: 0.09
    std: 0.007
    paper_value: 0.09
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 164
    true_value: 0.09
    true_std: 0.007
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.09
    sort_std: 0.007
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.101
    std: 0.01
    paper_value: 0.101
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 176
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: GT-E (RWSE)
    model_key: gt-e (rwse)
    model_plain: GT-E (RWSE)
    value: 0.104
    std: 0.025
    paper_value: 0.104
    paper_std: 0.025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 180
    true_value: 0.104
    true_std: 0.025
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.104
    sort_std: 0.025
    is_best: false
  - model: None
    model_key: none
    model_plain: None
    value: 0.113
    std: 0.007
    paper_value: 0.113
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 187
    true_value: 0.113
    true_std: 0.007
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 187
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.113
    sort_std: 0.007
    is_best: false
  - model: LapPE
    model_key: lappe
    model_plain: LapPE
    value: 0.116
    std: 0.009
    paper_value: 0.116
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 190
    true_value: 0.116
    true_std: 0.009
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.116
    sort_std: 0.009
    is_best: false
  - model: GIN-E (MoSE)
    model_key: gin-e (mose)
    model_plain: GIN-E (MoSE)
    value: 0.118
    std: 0.007
    paper_value: 0.118
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 192
    true_value: 0.118
    true_std: 0.007
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 192
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.118
    sort_std: 0.007
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.119
    std: 0.011
    paper_value: 0.119
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 194
    true_value: 0.119
    true_std: 0.011
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.119
    sort_std: 0.011
    is_best: false
  - model: GIN-E+VN
    model_key: gin-e+vn (none)
    model_plain: GIN-E+VN
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 219
    true_value: 0.151
    true_std: 0.006
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 219
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.151
    sort_std: 0.006
    is_best: false
  - model: PEG
    model_key: peg
    model_plain: PEG
    value: 0.161
    std: 0.006
    paper_value: 0.161
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 231
    true_value: 0.161
    true_std: 0.006
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 231
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.161
    sort_std: 0.006
    is_best: false
  - model: R-GCN (RWSE+MoSE)
    model_key: r-gcn (rwse+mose)
    model_plain: R-GCN (RWSE+MoSE)
    value: 0.188
    std: 0.005
    paper_value: 0.188
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 239
    true_value: 0.188
    true_std: 0.005
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 239
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.188
    sort_std: 0.005
    is_best: false
  - model: GT-E
    model_key: gt-e (none)
    model_plain: GT-E
    value: 0.195
    std: 0.025
    paper_value: 0.195
    paper_std: 0.025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 242
    true_value: 0.195
    true_std: 0.025
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.195
    sort_std: 0.025
    is_best: false
  - model: GT-E
    model_key: gt-e
    model_plain: GT-E
    value: 0.195
    std: 0.025
    paper_value: 0.195
    paper_std: 0.025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 243
    true_value: 0.195
    true_std: 0.025
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 243
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.195
    sort_std: 0.025
    is_best: false
  - model: R-GCN (MoSE)
    model_key: r-gcn (mose)
    model_plain: R-GCN (MoSE)
    value: 0.197
    std: 0.004
    paper_value: 0.197
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 244
    true_value: 0.197
    true_std: 0.004
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 244
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.197
    sort_std: 0.004
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.207
    std: 0.007
    paper_value: 0.207
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 247
    true_value: 0.207
    true_std: 0.007
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 247
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.207
    sort_std: 0.007
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.243
    std: 0.006
    paper_value: 0.243
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 252
    true_value: 0.243
    true_std: 0.006
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 252
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.243
    sort_std: 0.006
    is_best: false
  - model: MLP-E (MoSE)
    model_key: mlp-e (mose)
    model_plain: MLP-E (MoSE)
    value: 0.347
    std: 0.003
    paper_value: 0.347
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 265
    true_value: 0.347
    true_std: 0.003
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 265
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.347
    sort_std: 0.003
    is_best: false
  - model: MLP-E (RWSE)
    model_key: mlp-e (rwse)
    model_plain: MLP-E (RWSE)
    value: 0.361
    std: 0.01
    paper_value: 0.361
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 270
    true_value: 0.361
    true_std: 0.01
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 270
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.361
    sort_std: 0.01
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.413
    std: 0.005
    paper_value: 0.413
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 276
    true_value: 0.413
    true_std: 0.005
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 276
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.413
    sort_std: 0.005
    is_best: false
  - model: MLP-E
    model_key: mlp-e (none)
    model_plain: MLP-E
    value: 0.606
    std: 0.002
    paper_value: 0.606
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 285
    true_value: 0.606
    true_std: 0.002
    value_gap_source_arxiv: '2410.18676'
    value_gap_source_title: Homomorphism Counts as Structural Encodings for Graph
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 285
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.002
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: GNNBenchmark
  datasets:
  - *id004
  - *id005
- benchmark: OGB
  datasets:
  - *id006
main_figure: /figures/2410.18676/main_figure.png
---

