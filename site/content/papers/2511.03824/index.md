---
title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
  Neural Networks
arxiv_id: '2511.03824'
source_url: ''
authors: []
published_date: Nov 2025
published_date_iso: 2025-11
abstract: 'Graph Neural Networks learn on graph-structured data by iteratively aggregating
  local neighborhood information. While this local message passing paradigm imparts
  a powerful inductive bias and exploits graph sparsity, it also yields three key
  challenges: (i) oversquashing of long-range information, (ii) oversmoothing of node
  representations, and (iii) limited expressive power. In this work we inject randomized
  global embeddings of node features, which we term Sketched Random Features, into
  standard GNNs, enabling them to efficiently capture long-range dependencies. The
  embeddings are unique, distance-sensitive, and topology-agnostic---properties which
  we analytically and empirically show alleviate the aforementioned limitations when
  injected into GNNs. Experimental results on real-world graph learning tasks confirm
  that this strategy consistently improves performance over baseline GNNs, offering
  both a standalone solution and a complementary enhancement to existing techniques
  such as graph positional encodings. Our source code is available at https://github.com/ryienh/sketched-random-features.'
codebase_url: https://github.com/ryienh/sketched-random-features
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- SRF (linear, AG)
- SRF (L, AG)
- SRF (RBF, AG)
mrr: 0.0909
adjusted_mrr: 0.0303
mrr_dataset_count: 1
benchmark_categories:
- TU Dortmund
- LRGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
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
    paper_value: 0.243
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 2
    true_value: 0.243
    true_std: null
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.2438
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.2438
    sort_std: 0.0014
    is_best: true
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.245
    std: null
    paper_value: 0.245
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
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
    paper_rank: 7
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: true
  - model: R-PEARL+SRF
    model_key: r-pearl+srf
    model_plain: R-PEARL+SRF
    value: 0.245
    std: null
    paper_value: 0.245
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 9
    true_value: 0.245
    true_std: null
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.245
    sort_std: null
    is_best: false
  - model: R-PEARL
    model_key: r-pearl
    model_plain: R-PEARL
    value: 0.247
    std: null
    paper_value: 0.247
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pearl et al.
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 25
    true_value: 0.247
    true_std: null
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.247
    sort_std: null
    is_best: false
  - model: B-PEARL
    model_key: b-pearl
    model_plain: B-PEARL
    value: 0.248
    std: null
    paper_value: 0.248
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pearl et al.
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 40
    true_value: 0.248
    true_std: null
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.248
    sort_std: null
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.252
    std: null
    paper_value: 0.252
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 50
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
    paper_rank: 62
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.25
    std: null
    paper_value: 0.25
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 54
    true_value: 0.25
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
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
    std: null
    paper_value: 0.255
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 73
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005000000000000004
    value_note: global 0.2545 within std
    paper_rank: 74
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.274
    std: null
    paper_value: 0.274
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 92
    true_value: 0.274
    true_std: 0.0
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.274
    sort_std: 0.0
    is_best: false
  metric: MAE
  higher_is_better: false
- &id001
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
  - model: SRF (RBF, AG)
    model_key: srf (rbf, ag)
    model_plain: SRF (RBF, AG)
    value: 0.6053
    std: 0.0029
    paper_value: 0.6053
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 9
    true_value: 0.6053
    true_std: 0.0029
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6053
    sort_std: 0.0029
    is_best: false
  - model: SRF (L, AG)
    model_key: srf (l, ag)
    model_plain: SRF (L, AG)
    value: 0.6033
    std: 0.0037
    paper_value: 0.6033
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 10
    true_value: 0.6033
    true_std: 0.0037
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6033
    sort_std: 0.0037
    is_best: false
  - model: SRF (linear, AG)
    model_key: srf (linear, ag)
    model_plain: SRF (linear, AG)
    value: 0.6018
    std: 0.0039
    paper_value: 0.6018
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 11
    true_value: 0.6018
    true_std: 0.0039
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6018
    sort_std: 0.0039
    is_best: false
  - model: R-PEARL
    model_key: r-pearl
    model_plain: R-PEARL
    value: 0.594
    std: 0.01
    paper_value: 0.594
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 12
    true_value: 0.594
    true_std: 0.01
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.594
    sort_std: 0.01
    is_best: false
  - model: GCN + SRF (RBF, AG)
    model_key: gcn + srf (rbf, ag)
    model_plain: GCN + SRF (RBF, AG)
    value: 0.5808
    std: 0.0089
    paper_value: 0.5808
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 13
    true_value: 0.5808
    true_std: 0.0089
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5808
    sort_std: 0.0089
    is_best: false
  - model: GCN + SRF (L, AG)
    model_key: gcn + srf (l, ag)
    model_plain: GCN + SRF (L, AG)
    value: 0.572
    std: 0.009
    paper_value: 0.572
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 15
    true_value: 0.572
    true_std: 0.009
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.572
    sort_std: 0.009
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 16
    true_value: 0.57
    true_std: 0.021
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: GINE (No PE)
    model_key: gine (no pe)
    model_plain: GINE (No PE)
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 17
    true_value: 0.569
    true_std: 0.02
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.569
    sort_std: 0.02
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.414
    std: 0.027
    paper_value: 0.414
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 29
    true_value: 0.552
    true_std: 0.029
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13800000000000007
    value_note: ''
    paper_rank: 60
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.552
    sort_std: 0.029
    is_best: false
  - model: GATv2 + SRF (linear, AG)
    model_key: gatv2 + srf (linear, ag)
    model_plain: GATv2 + SRF (linear, AG)
    value: 0.5204
    std: 0.0056
    paper_value: 0.5204
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 36
    true_value: 0.5204
    true_std: 0.0056
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5204
    sort_std: 0.0056
    is_best: false
  - model: GCN + SRF (linear, AG)
    model_key: gcn + srf (linear, ag)
    model_plain: GCN + SRF (linear, AG)
    value: 0.514
    std: 0.0104
    paper_value: 0.514
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 37
    true_value: 0.514
    true_std: 0.0104
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.514
    sort_std: 0.0104
    is_best: false
  - model: GAT + SRF (L, AG)
    model_key: gat + srf (l, ag)
    model_plain: GAT + SRF (L, AG)
    value: 0.4876
    std: 0.0089
    paper_value: 0.4876
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 44
    true_value: 0.4876
    true_std: 0.0089
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4876
    sort_std: 0.0089
    is_best: false
  - model: GAT + SRF (RBF, AG)
    model_key: gat + srf (rbf, ag)
    model_plain: GAT + SRF (RBF, AG)
    value: 0.484
    std: 0.0127
    paper_value: 0.484
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 45
    true_value: 0.484
    true_std: 0.0127
    value_gap_source_arxiv: '2511.03824'
    value_gap_source_title: Sketch-Augmented Features Improve Learning Long-Range
      Dependencies in Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.484
    sort_std: 0.0127
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
main_figure: /figures/2511.03824/main_figure.png
---

