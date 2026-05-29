---
title: Learning Efficient Positional Encodings with Graph Neural Networks
arxiv_id: '2502.01122'
source_url: ''
authors: []
published_date: Feb 2025
published_date_iso: 2025-02
abstract: 'Positional encodings (PEs) are essential for effective graph representation
  learning because they provide position awareness in inherently position-agnostic
  transformer architectures and increase the expressive capacity of Graph Neural Networks
  (GNNs). However, designing powerful and efficient PEs for graphs poses significant
  challenges due to the absence of canonical node ordering and the scale of the graph.
  In this work, we identify four key properties that graph PEs should satisfy: stability,
  expressive power, scalability, and genericness. We find that existing eigenvector-based
  PE methods often fall short of jointly satisfying these criteria. To address this
  gap, we introduce, a novel framework of learnable PEs for graphs. Our primary insight
  is that message-passing GNNs function as nonlinear mappings of eigenvectors, enabling
  the design of GNN architectures for generating powerful and efficient PEs. A crucial
  challenge lies in initializing node attributes in a manner that is both expressive
  and permutation equivariant. We tackle this by initializing GNNs with random node
  inputs or standard basis vectors, thereby unlocking the expressive power of message-passing
  operations, while employing statistical pooling functions to maintain permutation
  equivariance. Our analysis demonstrates that approximates equivariant functions
  of eigenvectors with linear complexity, while rigorously establishing its stability
  and high expressive power. Experimental evaluations show that outperforms lightweight
  versions of eigenvector-based PEs and achieves comparable performance to full eigenvector-based
  PEs, but with one or two orders of magnitude lower complexity. Our code is available
  at.'
codebase_url: https://github.com/ehejin/Pearl-PE
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- PEs
mrr: 0.525
adjusted_mrr: 0.35
mrr_dataset_count: 2
benchmark_categories:
- Classic
- TU Dortmund
- LRGB
- GNNBenchmark
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id006
  dataset: CSL
  rows:
  - model: R-PEs
    model_key: r-pes
    model_plain: R-PEs
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 5
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: B-PEs
    model_key: b-pes
    model_plain: B-PEs
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 1.0
    std: null
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: ESC-GNN
    model_key: esc-gnn
    model_plain: ESC-GNN
    value: 1.0
    std: null
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 1.0
    std: null
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: null
    is_best: true
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: D&D
  rows:
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: VRN Ensemble
    model_key: vrn ensemble
    model_plain: VRN Ensemble
    value: 0.9554
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9554
    sort_std: null
    is_best: false
  - model: MVCNN
    model_key: mvcnn
    model_plain: MVCNN
    value: 0.901
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: null
    is_best: false
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.7253
    std: 0.0066
    paper_value: 0.7253
    paper_std: 0.0066
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7253
    sort_std: 0.0066
    is_best: false
  - model: SignNet
    model_key: signnet
    model_plain: SignNet
    value: 0.7227
    std: 0.0097
    paper_value: 0.7227
    paper_std: 0.0097
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7227
    sort_std: 0.0097
    is_best: false
  - model: R-PEs
    model_key: r-pes
    model_plain: R-PEs
    value: 0.7224
    std: 0.003
    paper_value: 0.7224
    paper_std: 0.003
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7224
    sort_std: 0.003
    is_best: false
  - model: PEG
    model_key: peg
    model_plain: PEG
    value: 0.7198
    std: 0.0065
    paper_value: 0.7198
    paper_std: 0.0065
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7198
    sort_std: 0.0065
    is_best: false
  - model: SPE-8S
    model_key: spe-8s
    model_plain: SPE-8S
    value: 0.7172
    std: 0.0071
    paper_value: 0.7172
    paper_std: 0.0071
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7172
    sort_std: 0.0071
    is_best: false
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 0.7168
    std: 0.011
    paper_value: 0.7168
    paper_std: 0.011
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7168
    sort_std: 0.011
    is_best: false
  - model: BasisNet
    model_key: basisnet
    model_plain: BasisNet
    value: 0.7166
    std: 0.0005
    paper_value: 0.7166
    paper_std: 0.0005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7166
    sort_std: 0.0005
    is_best: false
  - model: B-PEs
    model_key: b-pes
    model_plain: B-PEs
    value: 0.7122
    std: 0.0042
    paper_value: 0.7122
    paper_std: 0.0042
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.7122
    sort_std: 0.0042
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.2436
    sort_std: 0.0022
    is_best: true
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.245
    std: 0.002
    paper_value: 0.245
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 6
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.2449 within std
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: true
  - model: PEs
    model_key: pes
    model_plain: PEs
    value: 0.247
    std: 0.001
    paper_value: 0.247
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 20
    true_value: 0.247
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.247
    sort_std: 0.001
    is_best: false
  - model: B-PEs
    model_key: b-pes
    model_plain: B-PEs
    value: 0.248
    std: 0.001
    paper_value: 0.248
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
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 35
    true_value: 0.248
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.248
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.252
    std: 0.001
    paper_value: 0.252
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 44
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0020000000000000018
    value_note: ''
    paper_rank: 53
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.25
    std: 0.001
    paper_value: 0.25
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Frasca et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 48
    true_value: 0.25
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.001
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.255
    std: 0.001
    paper_value: 0.255
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Krüger et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 64
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005000000000000004
    value_note: global 0.2545 within std
    paper_rank: 65
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.268
    std: 0.004
    paper_value: 0.268
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Krüger et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 78
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.274
    std: 0.0
    paper_value: 0.274
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 82
    true_value: 0.274
    true_std: 0.0
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.274
    sort_std: 0.0
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: REDDIT-BINARY
  rows:
  - model: PEs
    model_key: pes
    model_plain: PEs
    value: 0.945
    std: 0.004
    paper_value: 0.945
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 1
    true_value: 0.945
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.918
    std: 0.01
    paper_value: 0.918
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 2
    true_value: 0.918
    true_std: 0.01
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.01
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.918
    std: 0.016
    paper_value: 0.918
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.918
    true_std: 0.016
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.016
    is_best: false
  - model: GSN with cliques
    model_key: gsn with cliques
    model_plain: GSN with cliques
    value: 0.911
    std: 0.018
    paper_value: 0.911
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.911
    true_std: 0.018
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.911
    sort_std: 0.018
    is_best: false
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.9094
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9094
    sort_std: 0.0047
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.9041
    std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.9041
    sort_std: 0.0041
    is_best: false
  - model: R-GIN + Last FA
    model_key: r-gin + last fa
    model_plain: R-GIN + Last FA
    value: 0.9
    std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.9
    sort_std: 0.0065
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.89
    std: 0.052
    paper_value: 0.89
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.89
    true_std: 0.052
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.89
    sort_std: 0.052
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5
    std: 0.0
    paper_value: 0.5
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 16
    true_value: 0.865
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.365
    value_note: ''
    paper_rank: 24
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.865
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: REDDIT-MULTI-5K
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.871
    std: 0.002
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.871
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.862
    std: 0.003
    metric: Accuracy
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
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.856
    std: 0.002
    metric: Accuracy
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
    sort_value: 0.856
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.569
    std: 0.02
    paper_value: 0.569
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.28200000000000003
    value_note: ''
    paper_rank: 15
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2
    std: 0.0
    paper_value: 0.2
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.835
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.635
    value_note: ''
    paper_rank: 46
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.835
    sort_std: 0.003
    is_best: false
  - model: R-PEs
    model_key: r-pes
    model_plain: R-PEs
    value: 0.606
    std: 0.003
    paper_value: 0.606
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 8
    true_value: 0.606
    true_std: 0.003
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.003
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.57
    std: 0.021
    paper_value: 0.57
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.57
    true_std: 0.021
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: GSN with cliques
    model_key: gsn with cliques
    model_plain: GSN with cliques
    value: 0.562
    std: 0.018
    paper_value: 0.562
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 17
    true_value: 0.562
    true_std: 0.018
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.562
    sort_std: 0.018
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.552
    std: 0.029
    paper_value: 0.552
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 18
    true_value: 0.552
    true_std: 0.029
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.552
    sort_std: 0.029
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
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
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
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
    value: 0.209
    std: 0.018
    paper_value: 0.209
    paper_std: 0.018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19499999999999998
    value_note: ''
    paper_rank: 102
    rank_delta: 99
    rank_delta_abs: 99
    rank_delta_direction: worse
    sort_value: 0.014
    sort_std: null
    is_best: true
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.02
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.469
    std: 0.002
    paper_value: 0.469
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.44499999999999995
    value_note: ''
    paper_rank: 117
    rank_delta: 108
    rank_delta_abs: 108
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
    is_best: false
  - model: B-PEs
    model_key: b-pes
    model_plain: B-PEs
    value: 0.0644
    std: 0.001
    paper_value: 0.0644
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 29
    true_value: 0.0644
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0644
    sort_std: 0.001
    is_best: false
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.0693
    std: 0.004
    paper_value: 0.0693
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 34
    true_value: 0.0693
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0693
    sort_std: 0.004
    is_best: false
  - model: R-PEs
    model_key: r-pes
    model_plain: R-PEs
    value: 0.0699
    std: 0.002
    paper_value: 0.0699
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 36
    true_value: 0.0699
    true_std: 0.002
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0699
    sort_std: 0.002
    is_best: false
  - model: SPE-8S
    model_key: spe-8s
    model_plain: SPE-8S
    value: 0.0736
    std: 0.0007
    paper_value: 0.0736
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 40
    true_value: 0.0736
    true_std: 0.0007
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0736
    sort_std: 0.0007
    is_best: false
  - model: SignNet
    model_key: signnet
    model_plain: SignNet
    value: 0.0853
    std: 0.0026
    paper_value: 0.0853
    paper_std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 48
    true_value: 0.0853
    true_std: 0.0026
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0853
    sort_std: 0.0026
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.1034
    std: 0.0056
    paper_value: 0.1034
    paper_std: 0.0056
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 62
    true_value: 0.1034
    true_std: 0.0056
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1034
    sort_std: 0.0056
    is_best: false
  - model: GSN with cycles
    model_key: gsn with cycles
    model_plain: GSN with cycles
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
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 70
    true_value: 0.115
    true_std: 0.012
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.115
    sort_std: 0.012
    is_best: false
  - model: BasisNet-8S
    model_key: basisnet-8s
    model_plain: BasisNet-8S
    value: 0.1554
    std: 0.0048
    paper_value: 0.1554
    paper_std: 0.0048
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 87
    true_value: 0.1554
    true_std: 0.0048
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1554
    sort_std: 0.0048
    is_best: false
  - model: BasisNet
    model_key: basisnet
    model_plain: BasisNet
    value: 0.1555
    std: 0.0124
    paper_value: 0.1555
    paper_std: 0.0124
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 88
    true_value: 0.1555
    true_std: 0.0124
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1555
    sort_std: 0.0124
    is_best: false
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 0.1772
    std: 0.004
    paper_value: 0.1772
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 95
    true_value: 0.1772
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1772
    sort_std: 0.004
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.279
    std: 0.023
    paper_value: 0.279
    paper_std: 0.023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 107
    true_value: 0.279
    true_std: 0.023
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.279
    sort_std: 0.023
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
  - *id003
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
- benchmark: GNNBenchmark
  datasets:
  - *id006
single_proposed_model: PEs
main_figure: /figures/2502.01122/main_figure.png
---

