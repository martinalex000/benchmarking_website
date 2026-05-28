---
title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
arxiv_id: '2405.13526'
source_url: ''
authors: []
published_date: May 2024
published_date_iso: 2024-05
abstract: While message passing neural networks (MPNNs) have convincing success in
  a range of applications, they exhibit limitations such as the oversquashing problem
  and their inability to capture long-range interactions. Augmenting MPNNs with a
  virtual node (VN) removes the locality constraint of the layer aggregation and has
  been found to improve performance on a range of benchmarks. We provide a comprehensive
  theoretical analysis of the role of VNs and benefits thereof, through the lenses
  of oversquashing and sensitivity analysis. First, we characterize, precisely, how
  the improvement afforded by VNs on the mixing abilities of the network and hence
  in mitigating oversquashing, depends on the underlying topology. We then highlight
  that, unlike Graph-Transformers (GTs), classical instantiations of the VN are often
  constrained to assign uniform importance to different nodes. Consequently, we propose
  a variant of VN with the same computational complexity, which can have different
  sensitivity to nodes based on the graph structure. We show that this is an extremely
  effective and computationally efficient baseline for graph-level tasks.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GatedGCN+PE+VN_G
mrr: 0.0115
adjusted_mrr: 0.0038
mrr_dataset_count: 1
benchmark_categories:
- LRGB
- GNNBenchmark
- OGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
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
  - model: RandAlign (4 layers)
    model_key: randalign (4 layers)
    model_plain: RandAlign (4 layers)
    value: 0.7942
    std: 0.00072
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    sort_value: 0.7942
    sort_std: 0.00072
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.67312
    std: 0.00311
    paper_value: 0.67312
    paper_std: 0.00311
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 12
    true_value: 0.77218
    true_std: 0.00381
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09905999999999993
    value_note: ''
    paper_rank: 104
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.77218
    sort_std: 0.00381
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.76468
    std: 0.00881
    paper_value: 0.76468
    paper_std: 0.00881
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 20
    true_value: 0.76468
    true_std: 0.00881
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76468
    sort_std: 0.00881
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7469
    std: 0.00125
    paper_value: 0.7469
    paper_std: 0.00125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 36
    true_value: 0.74754
    true_std: 0.00194
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0006399999999999739
    value_note: global 0.7475 within std
    paper_rank: 37
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.74754
    sort_std: 0.00194
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.72298
    std: 0.00356
    paper_value: 0.72298
    paper_std: 0.00356
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 57
    true_value: 0.72356
    true_std: 0.0032300000000000002
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005800000000000249
    value_note: global 0.7236 within std
    paper_rank: 61
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.72356
    sort_std: 0.0032300000000000002
    is_best: false
  - model: GatedGCN+PE-ViT
    model_key: gatedgcn+pe-vit
    model_plain: GatedGCN+PE-ViT
    value: 0.7158
    std: 0.0009
    paper_value: 0.7158
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 77
    true_value: 0.7158
    true_std: 0.0009
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7158
    sort_std: 0.0009
    is_best: false
  - model: GPS + projection
    model_key: gps + projection
    model_plain: GPS + projection
    value: 0.71455
    std: 0.00513
    paper_value: 0.71455
    paper_std: 0.00513
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
    global_rank: 79
    true_value: 0.71455
    true_std: 0.00513
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71455
    sort_std: 0.00513
    is_best: false
  - model: GatedGCN+PE-Mixer
    model_key: gatedgcn+pe-mixer
    model_plain: GatedGCN+PE-Mixer
    value: 0.706
    std: 0.0022
    paper_value: 0.706
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 84
    true_value: 0.706
    true_std: 0.0022
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.706
    sort_std: 0.0022
    is_best: false
  - model: GatedGCN+PE+VN_G
    model_key: gatedgcn+pe+vn_g
    model_plain: GatedGCN+PE+VN_G
    value: 0.7028
    std: 0.0038
    paper_value: 0.7028
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 87
    true_value: 0.7028
    true_std: 0.0038
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7028
    sort_std: 0.0038
    is_best: false
  - model: GatedGCN+LapPE
    model_key: gatedgcn+lappe
    model_plain: GatedGCN+LapPE
    value: 0.69948
    std: 0.00499
    paper_value: 0.69948
    paper_std: 0.00499
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 91
    true_value: 0.69948
    true_std: 0.00499
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69948
    sort_std: 0.00499
    is_best: false
  - model: GatedGCN+GPSE
    model_key: gatedgcn+gpse
    model_plain: GatedGCN+GPSE
    value: 0.69948
    std: 0.00499
    paper_value: 0.69948
    paper_std: 0.00499
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 92
    true_value: 0.69948
    true_std: 0.00499
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69948
    sort_std: 0.00499
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.6901
    std: 0.00259
    paper_value: 0.6901
    paper_std: 0.00259
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 100
    true_value: 0.69013
    true_std: 0.00259
    value_gap_source_arxiv: '2407.02758'
    value_gap_source_title: Differential Encoding for Improved Representation Learning
      over Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.6901 within std
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69013
    sort_std: 0.00259
    is_best: false
  - model: GCN+PE+VN
    model_key: gcn+pe+vn
    model_plain: GCN+PE+VN
    value: 0.68756
    std: 0.00172
    paper_value: 0.68756
    paper_std: 0.00172
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 101
    true_value: 0.68756
    true_std: 0.00172
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68756
    sort_std: 0.00172
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.68702
    std: 0.00409
    paper_value: 0.68702
    paper_std: 0.00409
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 102
    true_value: 0.68702
    true_std: 0.00409
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68702
    sort_std: 0.00409
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
    table_ref: Table 2
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
    table_ref: Table 2
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
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 297
    rank_delta: 285
    rank_delta_abs: 285
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GCN+PE+VN
    model_key: gcn+pe+vn
    model_plain: GCN+PE+VN
    value: 0.2456
    std: 0.001
    paper_value: 0.2456
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 46
    true_value: 0.2456
    true_std: 0.001
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2456
    sort_std: 0.001
    is_best: false
  - model: GatedGCN+PE+VN_G
    model_key: gatedgcn+pe+vn_g
    model_plain: GatedGCN+PE+VN_G
    value: 0.2458
    std: 0.0006
    paper_value: 0.2458
    paper_std: 0.0006
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
    global_rank: 49
    true_value: 0.2458
    true_std: 0.0006
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2458
    sort_std: 0.0006
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 56
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
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
  - model: GatedGCN+PE-ViT
    model_key: gatedgcn+pe-vit
    model_plain: GatedGCN+PE-ViT
    value: 0.2465
    std: 0.0015
    paper_value: 0.2465
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 67
    true_value: 0.2465
    true_std: 0.0015
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2465
    sort_std: 0.0015
    is_best: false
  - model: GatedGCN+LapPE
    model_key: gatedgcn+lappe
    model_plain: GatedGCN+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 68
    true_value: 0.2466
    true_std: 0.0012
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010999999999999899
    value_note: global 0.2466 within std
    paper_rank: 89
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.2466
    sort_std: 0.0012
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
    table_ref: Table 2
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
  - model: GatedGCN+GPSE
    model_key: gatedgcn+gpse
    model_plain: GatedGCN+GPSE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 94
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
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
    table_ref: Table 2
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
  - model: GPS + projection
    model_key: gps + projection
    model_plain: GPS + projection
    value: 0.2487
    std: 0.0011
    paper_value: 0.2487
    paper_std: 0.0011
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
    global_rank: 115
    true_value: 0.2487
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2487
    sort_std: 0.0011
    is_best: false
  - model: GCN + VN
    model_key: gcn + vn
    model_plain: GCN + VN
    value: 0.2488
    std: 0.0021
    paper_value: 0.2488
    paper_std: 0.0021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 122
    true_value: 0.2488
    true_std: 0.0021
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2488
    sort_std: 0.0021
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 146
    true_value: 0.2506
    true_std: 0.0022
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
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
  - model: GatedGCN+PE-Mixer
    model_key: gatedgcn+pe-mixer
    model_plain: GatedGCN+PE-Mixer
    value: 0.2508
    std: 0.0007
    paper_value: 0.2508
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 148
    true_value: 0.2508
    true_std: 0.0007
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2508
    sort_std: 0.0007
    is_best: false
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.2523
    std: 0.0016
    paper_value: 0.2523
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 164
    true_value: 0.2523
    true_std: 0.0016
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2523
    sort_std: 0.0016
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
    table_ref: Table 2
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
  - model: GINE + VN
    model_key: gine + vn
    model_plain: GINE + VN
    value: 0.2584
    std: 0.0011
    paper_value: 0.2584
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 210
    true_value: 0.2584
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 210
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2584
    sort_std: 0.0011
    is_best: false
  - model: GatedGCN + PairNorm
    model_key: gatedgcn + pairnorm
    model_plain: GatedGCN + PairNorm
    value: 0.3551
    std: 0.0008
    paper_value: 0.3551
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 314
    true_value: 0.3551
    true_std: 0.0008
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 314
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3551
    sort_std: 0.0008
    is_best: false
  - model: GatedGCN with PairNorm
    model_key: gatedgcn with pairnorm
    model_plain: GatedGCN with PairNorm
    value: 0.3551
    std: 0.0008
    paper_value: 0.3551
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 315
    true_value: 0.3551
    true_std: 0.0008
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 315
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3551
    sort_std: 0.0008
    is_best: false
  - model: GCN + Pairnorm
    model_key: gcn + pairnorm
    model_plain: GCN + Pairnorm
    value: 0.3562
    std: 0.0007
    paper_value: 0.3562
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 317
    true_value: 0.3562
    true_std: 0.0007
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 317
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3562
    sort_std: 0.0007
    is_best: false
  - model: GatedGCN + mean
    model_key: gatedgcn + mean
    model_plain: GatedGCN + mean
    value: 0.3566
    std: 0.0007
    paper_value: 0.3566
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 318
    true_value: 0.3566
    true_std: 0.0007
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 318
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3566
    sort_std: 0.0007
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
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
    value: 0.7606
    std: 0.0097
    paper_value: 0.7606
    paper_std: 0.0097
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
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2074999999999999
    value_note: ''
    paper_rank: 161
    rank_delta: 158
    rank_delta_abs: 158
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7558
    std: 0.014
    paper_value: 0.7558
    paper_std: 0.014
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
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21219999999999994
    value_note: ''
    paper_rank: 172
    rank_delta: 168
    rank_delta_abs: 168
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7827
    std: 0.0111
    paper_value: 0.7827
    paper_std: 0.0111
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 19
    true_value: 0.804
    true_std: 0.0164
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021300000000000097
    value_note: ''
    paper_rank: 97
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.804
    sort_std: 0.0164
    is_best: false
  - model: GatedGCN+PE+VN_G
    model_key: gatedgcn+pe+vn_g
    model_plain: GatedGCN+PE+VN_G
    value: 0.791
    std: 0.0086
    paper_value: 0.791
    paper_std: 0.0086
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
    true_value: 0.791
    true_std: 0.0086
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.0086
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.788
    std: 0.0101
    paper_value: 0.788
    paper_std: 0.0101
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
    global_rank: 76
    true_value: 0.788
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.01
    is_best: false
  - model: DeeperGCN
    model_key: deepergcn
    model_plain: DeeperGCN
    value: 0.7858
    std: 0.0117
    paper_value: 0.7858
    paper_std: 0.0117
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
    global_rank: 87
    true_value: 0.7858
    true_std: 0.01
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7858
    sort_std: 0.01
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7785
    std: 0.0028
    paper_value: 0.7785
    paper_std: 0.0028
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
    global_rank: 122
    true_value: 0.7785
    true_std: 0.247
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7785
    sort_std: 0.247
    is_best: true
  - model: GINE + VN
    model_key: gine + vn
    model_plain: GINE + VN
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
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 138
    true_value: 0.7707
    true_std: 0.0149
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7707
    sort_std: 0.0149
    is_best: false
  - model: GCN+PE+VN
    model_key: gcn+pe+vn
    model_plain: GCN+PE+VN
    value: 0.7678
    std: 0.0111
    paper_value: 0.7678
    paper_std: 0.0111
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 146
    true_value: 0.7678
    true_std: 0.0111
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7678
    sort_std: 0.0111
    is_best: false
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.7676
    std: 0.0172
    paper_value: 0.7676
    paper_std: 0.0172
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 147
    true_value: 0.7676
    true_std: 0.0172
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7676
    sort_std: 0.0172
    is_best: false
  - model: GatedGCN with PairNorm
    model_key: gatedgcn with pairnorm
    model_plain: GatedGCN with PairNorm
    value: 0.7645
    std: 0.0128
    paper_value: 0.7645
    paper_std: 0.0128
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 152
    true_value: 0.7645
    true_std: 0.0128
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7645
    sort_std: 0.0128
    is_best: false
  - model: GCN + VN
    model_key: gcn + vn
    model_plain: GCN + VN
    value: 0.7599
    std: 0.0119
    paper_value: 0.7599
    paper_std: 0.0119
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
    global_rank: 167
    true_value: 0.7599
    true_std: 0.0119
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7599
    sort_std: 0.0119
    is_best: false
  - model: GatedGCN + mean
    model_key: gatedgcn + mean
    model_plain: GatedGCN + mean
    value: 0.7594
    std: 0.0096
    paper_value: 0.7594
    paper_std: 0.0096
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 168
    true_value: 0.7594
    true_std: 0.0096
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7594
    sort_std: 0.0096
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
  dataset: ogbg-molpcba
  rows:
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.2823
    std: 0.0026
    paper_value: 0.2823
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 1
    true_value: 0.3141
    true_std: 0.0019
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.031799999999999995
    value_note: ''
    paper_rank: 31
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
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
    value: 0.2714
    std: 0.0014
    paper_value: 0.2714
    paper_std: 0.0014
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 3
    true_value: 0.3066
    true_std: 0.0013
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03520000000000001
    value_note: ''
    paper_rank: 40
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  - model: LGI-GT
    model_key: lgi-gt
    model_plain: LGI-GT
    value: 0.304
    std: 0.0029
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
    global_rank: 4
    sort_value: 0.304
    sort_std: 0.0029
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.2986
    std: 0.0025
    paper_value: 0.2986
    paper_std: 0.0025
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
    global_rank: 5
    true_value: 0.2986
    true_std: 0.0025
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2986
    sort_std: 0.0025
    is_best: false
  - model: CRaWI
    model_key: crawi
    model_plain: CRaWI
    value: 0.2986
    std: 0.0025
    metric: AP
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
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.2986
    sort_std: 0.0025
    is_best: false
  - model: GatedGCN+PE+VN_G
    model_key: gatedgcn+pe+vn_g
    model_plain: GatedGCN+PE+VN_G
    value: 0.2917
    std: 0.0027
    paper_value: 0.2917
    paper_std: 0.0027
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
    global_rank: 18
    true_value: 0.2917
    true_std: 0.0027
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2917
    sort_std: 0.0027
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2907
    std: 0.0028
    paper_value: 0.2907
    paper_std: 0.0028
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
    global_rank: 21
    true_value: 0.2907
    true_std: 0.0028
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2907
    sort_std: 0.0028
    is_best: false
  - model: GatedGCN + mean
    model_key: gatedgcn + mean
    model_plain: GatedGCN + mean
    value: 0.2866
    std: 0.0016
    paper_value: 0.2866
    paper_std: 0.0016
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 26
    true_value: 0.2866
    true_std: 0.0016
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2866
    sort_std: 0.0016
    is_best: false
  - model: DeeperGCN
    model_key: deepergcn
    model_plain: DeeperGCN
    value: 0.2781
    std: 0.0038
    paper_value: 0.2781
    paper_std: 0.0038
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
    global_rank: 33
    true_value: 0.2781
    true_std: 0.0038
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2781
    sort_std: 0.0038
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2765
    std: 0.0042
    paper_value: 0.2765
    paper_std: 0.0042
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
    global_rank: 36
    true_value: 0.2765
    true_std: 0.0042
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2765
    sort_std: 0.0042
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.202
    std: 0.0024
    paper_value: 0.202
    paper_std: 0.0024
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
    global_rank: 40
    true_value: 0.2721
    true_std: 0.0046
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0701
    value_note: ''
    paper_rank: 54
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.2721
    sort_std: 0.0046
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2266
    std: 0.0028
    paper_value: 0.2266
    paper_std: 0.0028
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
    global_rank: 41
    true_value: 0.2703
    true_std: 0.0024
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04369999999999999
    value_note: ''
    paper_rank: 54
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.2703
    sort_std: 0.0024
    is_best: false
  - model: GINE + VN
    model_key: gine + vn
    model_plain: GINE + VN
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 43
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GatedGCN with PairNorm
    model_key: gatedgcn with pairnorm
    model_plain: GatedGCN with PairNorm
    value: 0.2621
    std: 0.0026
    paper_value: 0.2621
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 47
    true_value: 0.2621
    true_std: 0.0026
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2621
    sort_std: 0.0026
    is_best: false
  - model: GCN+PE+VN
    model_key: gcn+pe+vn
    model_plain: GCN+PE+VN
    value: 0.2481
    std: 0.0032
    paper_value: 0.2481
    paper_std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 50
    true_value: 0.2481
    true_std: 0.0032
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0032
    is_best: false
  - model: GCN + VN
    model_key: gcn + vn
    model_plain: GCN + VN
    value: 0.2424
    std: 0.0034
    paper_value: 0.2424
    paper_std: 0.0034
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
    global_rank: 51
    true_value: 0.2424
    true_std: 0.0034
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2424
    sort_std: 0.0034
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
- benchmark: GNNBenchmark
  datasets:
  - *id002
- benchmark: OGB
  datasets:
  - *id003
  - *id004
single_proposed_model: GatedGCN+PE+VN_G
main_figure: /figures/2405.13526/main_figure.png
---

