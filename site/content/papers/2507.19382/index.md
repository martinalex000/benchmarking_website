---
title: Learning Long-Range Representations with Equivariant Messages
arxiv_id: '2507.19382'
source_url: ''
authors: []
published_date: Jul 2025
published_date_iso: 2025-07
abstract: Machine learning interatomic potentials trained on first-principles reference
  data are becoming valuable tools for computational physics, biology, and chemistry.
  Equivariant message-passing neural networks, including transformers, achieve state-of-the-art
  accuracy but rely on cutoff-based graphs, limiting their ability to capture long-range
  effects such as electrostatics or dispersion, as well as electron delocalization.
  While long-range correction schemes based on inverse power laws of interatomic distances
  have been proposed, they are unable to communicate higher-order geometric information
  and are thus limited in applicability. To address this shortcoming, we propose the
  use of equivariant, rather than scalar, charges for long-range interactions, and
  design a graph neural network architecture,, around this long-range message passing
  mechanism. We consider several datasets specifically designed to highlight non-local
  physical effects, and compare short-range message passing with different receptive
  fields to invariant and equivariant long-range message passing. Even though most
  approaches work for careful dataset-specific choices of their model hyperparameters,
  works consistently without such changes, with excellent benchmark performance.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Lorem
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
- GNNBenchmark
- MoleculeNet
- Hypergraph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id003
  dataset: BACE
  is_multi_metric: true
  rows:
  - model: Lorem
    model_key: lorem
    model_plain: Lorem
    metric_values:
    - 0.064
    - 0.064
    - 4.076
    metric_stds:
    - null
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.021
    sort_value: 0.064
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.064
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: true
    global_rank: null
  - model: Cace-Les
    model_key: cace-les
    model_plain: Cace-Les
    metric_values:
    - 0.071
    - 0.071
    - 7.913
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.071
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.071
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: SpookyNet
    model_key: spookynet
    model_plain: SpookyNet
    metric_values:
    - 0.107
    - 0.107
    - 5.337
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.107
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.107
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Pet
    model_key: pet
    model_plain: Pet
    metric_values:
    - 0.21
    - 0.21
    - 6.261
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.21
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.21
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: 4G-NN
    model_key: 4g-nn
    model_plain: 4G-NN
    metric_values:
    - 0.219
    - 0.219
    - 66.0
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.219
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.219
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Mace
    model_key: mace
    model_plain: Mace
    metric_values:
    - 0.376
    - 0.376
    - 5.971
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.376
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.376
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GAT
    model_key: gat
    model_plain: GAT
    metric_values:
    - 0.5746
    - null
    - null
    metric_stds:
    - 0.0362
    - null
    - null
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: false
    sort_value: 0.5746
    sort_std: 0.0362
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.5877
    - null
    - null
    metric_stds:
    - 0.0913
    - null
    - null
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
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.5877
    sort_std: 0.0913
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - 0.5899
    - null
    - null
    metric_stds:
    - 0.0552
    - null
    - null
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
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.5899
    sort_std: 0.0552
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  metrics:
  - RMSE
  - RMSE E
  - RMSE F
  primary_metric: ROC-AUC
  higher_is_better: false
- &id002
  dataset: CLUSTER
  is_multi_metric: true
  rows:
  - model: Lorem
    model_key: lorem
    model_plain: Lorem
    metric_values:
    - 0.09
    - 0.112
    - 0.112
    - 1.155
    metric_stds:
    - null
    - null
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.021
    sort_value: 0.09
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.09
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: true
    global_rank: null
  - model: SpookyNet
    model_key: spookynet
    model_plain: SpookyNet
    metric_values:
    - null
    - 0.135
    - 0.135
    - 1.052
    metric_stds:
    - null
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.135
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.135
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Cace-Les
    model_key: cace-les
    model_plain: Cace-Les
    metric_values:
    - 0.161
    - 0.21
    - 0.21
    - 9.784
    metric_stds:
    - null
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.161
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.161
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GCN (+PE)
    model_key: gcn (+pe)
    model_plain: GCN (+PE)
    metric_values:
    - 0.2684
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
    sort_value: 0.2684
    sort_std: 0.0005
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.27
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.27
    sort_std: 0.0002
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: RingGNN
    model_key: ringgnn
    model_plain: RingGNN
    metric_values:
    - 0.42418
    - null
    - null
    - null
    metric_stds:
    - 0.20063
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_display: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.42418
    sort_std: 0.20063
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: 4G-NN
    model_key: 4g-nn
    model_plain: 4G-NN
    metric_values:
    - null
    - 0.481
    - 0.481
    - 32.78
    metric_stds:
    - null
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.481
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.481
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Pet
    model_key: pet
    model_plain: Pet
    metric_values:
    - 1.249
    - 1.517
    - 1.517
    - 42.438
    metric_stds:
    - null
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 1.249
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 1.249
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Mace
    model_key: mace
    model_plain: Mace
    metric_values:
    - 1.345
    - 1.681
    - 1.681
    - 40.219
    metric_stds:
    - null
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 1.345
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 1.345
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - MAE
  - RMSE
  - RMSE E
  - RMSE F
  primary_metric: Accuracy
  higher_is_better: false
- &id001
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - 0.05
    - null
    metric_stds:
    - 0.021
    - null
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
    global_rank: 1
    is_best: true
    sort_value: 0.05
    sort_std: 0.021
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.093
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
    sort_value: 0.093
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: Lorem
    model_key: lorem
    model_plain: Lorem
    metric_values:
    - 0.222
    - 1.646
    metric_stds:
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.021
    sort_value: 0.222
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.222
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MF
    model_key: mf
    model_plain: MF
    metric_values:
    - 0.271
    - null
    metric_stds:
    - 0.004
    - null
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
    is_best: false
    sort_value: 0.271
    sort_std: 0.004
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: Cace-Les
    model_key: cace-les
    model_plain: Cace-Les
    metric_values:
    - 2.259
    - 3.163
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 2.259
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 2.259
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Pet
    model_key: pet
    model_plain: Pet
    metric_values:
    - 6.758
    - 16.47
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 6.758
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 6.758
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Mace
    model_key: mace
    model_plain: Mace
    metric_values:
    - 7.793
    - 16.15
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 7.793
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 7.793
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - RMSE E
  - RMSE F
  primary_metric: Accuracy
  higher_is_better: false
- &id004
  dataset: LEN
  is_multi_metric: true
  rows:
  - model: GIN (NF)
    model_key: gin (nf)
    model_plain: GIN (NF)
    metric_values:
    - 0.633
    - null
    metric_stds:
    - 0.065
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.633
    sort_std: 0.065
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GCN (NF)
    model_key: gcn (nf)
    model_plain: GCN (NF)
    metric_values:
    - 0.702
    - null
    metric_stds:
    - 0.018
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
    sort_value: 0.702
    sort_std: 0.018
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: SAGE (NF)
    model_key: sage (nf)
    model_plain: SAGE (NF)
    metric_values:
    - 0.729
    - null
    metric_stds:
    - 0.006
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.729
    sort_std: 0.006
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: Pet
    model_key: pet
    model_plain: Pet
    metric_values:
    - 3.205
    - 46.905
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 3.205
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 3.205
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Lorem
    model_key: lorem
    model_plain: Lorem
    metric_values:
    - 3.309
    - 50.084
    metric_stds:
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.021
    sort_value: 3.309
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 3.309
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Mace
    model_key: mace
    model_plain: Mace
    metric_values:
    - 12.592
    - 104.318
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 12.592
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 12.592
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Cace-Les
    model_key: cace-les
    model_plain: Cace-Les
    metric_values:
    - 17.803
    - 147.616
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 17.803
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 17.803
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - RMSE E
  - RMSE F
  primary_metric: Accuracy
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: GNNBenchmark
  datasets:
  - *id002
- benchmark: MoleculeNet
  datasets:
  - *id003
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id004
single_proposed_model: Lorem
main_figure: /figures/2507.19382/main_figure.png
---

