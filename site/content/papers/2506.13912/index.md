---
title: Density-aware Walks for Coordinated Campaign Detection
arxiv_id: '2506.13912'
source_url: ''
authors: []
published_date: Jun 2025
published_date_iso: 2025-06
abstract: Coordinated campaigns frequently exploit social media platforms by artificially
  amplifying topics, making inauthentic trends appear organic, and misleading users
  into engagement. Distinguishing these coordinated efforts from genuine public discourse
  remains a significant challenge due to the sophisticated nature of such attacks.
  Our work focuses on detecting coordinated campaigns by modeling the problem as a
  graph classification task. We leverage the recently introduced Large Engagement
  Networks (LEN) dataset, which contains over 300 networks capturing engagement patterns
  from both fake and authentic trends on Twitter prior to the 2023 Turkish elections.
  The graphs in LEN were constructed by collecting interactions related to campaigns
  that stemmed from ephemeral astroturfing. Established graph neural networks (GNNs)
  struggle to accurately classify campaign graphs, highlighting the challenges posed
  by LEN due to the large size of its networks. To address this, we introduce a new
  graph classification method that leverages the density of local network structures.
  We propose a random weighted walk (RWW) approach in which node transitions are biased
  by local density measures such as degree, core number, or truss number. These RWWs
  are encoded using the Skip-gram model, producing density-aware structural embeddings
  for the nodes. Training message-passing neural networks (MPNNs) on these density-aware
  embeddings yields superior results compared to the simpler node features available
  in the dataset, with nearly a 12% and 5% improvement in accuracy for binary and
  multiclass classification, respectively. Our findings demonstrate that incorporating
  density-aware structural encoding with MPNNs provides a robust framework for identifying
  coordinated inauthentic behavior on social media networks such as Twitter.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN (RWW, Degree, mid)
- GCN (RWW, Core, 0.5)
- GCN (RWW, Truss, median)
- GCN (NF+RWW, Core, median)
- GCN (NF+RWW, Truss, 0.5)
- GAT (RWW, Degree, median)
- GAT (RWW, Core, mid)
- GAT (NF+RWW, Core, 0.5)
- GAT (NF+RWW, Truss, median)
- GIN (RWW, Degree, 0.5)
- GIN (RWW, Truss, 0.5)
- GIN (NF+RWW, Core, mid)
- GIN (NF+RWW, Truss, mid)
- SAGE (RWW, Degree, 0.5)
- SAGE (RWW, Core, mid)
- SAGE (RWW, Truss, 0.5)
- SAGE (NF+RWW, Degree, median)
- SAGE (NF+RWW, Core, 0.5)
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- Hypergraph Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id001
  dataset: LEN
  rows:
  - model: SAGE (RWW, Degree, 0.5)
    model_key: sage (rww, degree, 0.5)
    model_plain: SAGE (RWW, Degree, 0.5)
    value: 0.852
    std: 0.01
    paper_value: 0.852
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 0.852
    true_std: 0.01
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.852
    sort_std: 0.01
    is_best: true
  - model: SAGE (RWW, Truss, 0.5)
    model_key: sage (rww, truss, 0.5)
    model_plain: SAGE (RWW, Truss, 0.5)
    value: 0.813
    std: 0.018
    paper_value: 0.813
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.813
    true_std: 0.018
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.813
    sort_std: 0.018
    is_best: false
  - model: GAT (RWW, Core, mid)
    model_key: gat (rww, core, mid)
    model_plain: GAT (RWW, Core, mid)
    value: 0.808
    std: 0.022
    paper_value: 0.808
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.808
    true_std: 0.022
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.808
    sort_std: 0.022
    is_best: false
  - model: GCN (NF+RWW, Truss, 0.5)
    model_key: gcn (nf+rww, truss, 0.5)
    model_plain: GCN (NF+RWW, Truss, 0.5)
    value: 0.803
    std: 0.019
    paper_value: 0.803
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 0.803
    true_std: 0.019
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.803
    sort_std: 0.019
    is_best: false
  - model: GCN (RWW, Truss, median)
    model_key: gcn (rww, truss, median)
    model_plain: GCN (RWW, Truss, median)
    value: 0.8
    std: 0.019
    paper_value: 0.8
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.8
    true_std: 0.019
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.019
    is_best: false
  - model: GAT (RWW, Degree, median)
    model_key: gat (rww, degree, median)
    model_plain: GAT (RWW, Degree, median)
    value: 0.792
    std: 0.022
    paper_value: 0.792
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.792
    true_std: 0.022
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.022
    is_best: false
  - model: GAT (NF+RWW, Truss, median)
    model_key: gat (nf+rww, truss, median)
    model_plain: GAT (NF+RWW, Truss, median)
    value: 0.792
    std: 0.03
    paper_value: 0.792
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.792
    true_std: 0.03
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.03
    is_best: false
  - model: GIN (NF+RWW, Core, mid)
    model_key: gin (nf+rww, core, mid)
    model_plain: GIN (NF+RWW, Core, mid)
    value: 0.792
    std: 0.014
    paper_value: 0.792
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 8
    true_value: 0.792
    true_std: 0.014
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.014
    is_best: false
  - model: SAGE (NF+RWW, Core, 0.5)
    model_key: sage (nf+rww, core, 0.5)
    model_plain: SAGE (NF+RWW, Core, 0.5)
    value: 0.79
    std: 0.017
    paper_value: 0.79
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 9
    true_value: 0.79
    true_std: 0.017
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79
    sort_std: 0.017
    is_best: false
  - model: GCN (RWW, Core, 0.5)
    model_key: gcn (rww, core, 0.5)
    model_plain: GCN (RWW, Core, 0.5)
    value: 0.787
    std: 0.01
    paper_value: 0.787
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 10
    true_value: 0.787
    true_std: 0.01
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.787
    sort_std: 0.01
    is_best: false
  - model: GAT (NF+RWW, Core, 0.5)
    model_key: gat (nf+rww, core, 0.5)
    model_plain: GAT (NF+RWW, Core, 0.5)
    value: 0.785
    std: 0.01
    paper_value: 0.785
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 11
    true_value: 0.785
    true_std: 0.01
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.01
    is_best: false
  - model: GCN (RWW, Degree, mid)
    model_key: gcn (rww, degree, mid)
    model_plain: GCN (RWW, Degree, mid)
    value: 0.784
    std: 0.006
    paper_value: 0.784
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 12
    true_value: 0.784
    true_std: 0.006
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.006
    is_best: false
  - model: GIN (NF+RWW, Truss, mid)
    model_key: gin (nf+rww, truss, mid)
    model_plain: GIN (NF+RWW, Truss, mid)
    value: 0.782
    std: 0.019
    paper_value: 0.782
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 13
    true_value: 0.782
    true_std: 0.019
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.019
    is_best: false
  - model: SAGE (RWW, Core, mid)
    model_key: sage (rww, core, mid)
    model_plain: SAGE (RWW, Core, mid)
    value: 0.774
    std: 0.025
    paper_value: 0.774
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 14
    true_value: 0.774
    true_std: 0.025
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.774
    sort_std: 0.025
    is_best: false
  - model: GIN (RWW, Truss, 0.5)
    model_key: gin (rww, truss, 0.5)
    model_plain: GIN (RWW, Truss, 0.5)
    value: 0.771
    std: 0.006
    paper_value: 0.771
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 15
    true_value: 0.771
    true_std: 0.006
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.006
    is_best: false
  - model: GCN (NF+RWW, Core, median)
    model_key: gcn (nf+rww, core, median)
    model_plain: GCN (NF+RWW, Core, median)
    value: 0.766
    std: 0.014
    paper_value: 0.766
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 16
    true_value: 0.766
    true_std: 0.014
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
    sort_std: 0.014
    is_best: false
  - model: SAGE (NF+RWW, Degree, median)
    model_key: sage (nf+rww, degree, median)
    model_plain: SAGE (NF+RWW, Degree, median)
    value: 0.758
    std: 0.01
    paper_value: 0.758
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 17
    true_value: 0.758
    true_std: 0.01
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.01
    is_best: false
  - model: GIN (RWW, Degree, 0.5)
    model_key: gin (rww, degree, 0.5)
    model_plain: GIN (RWW, Degree, 0.5)
    value: 0.751
    std: 0.005
    paper_value: 0.751
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 18
    true_value: 0.751
    true_std: 0.005
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.005
    is_best: false
  - model: GAT (NF)
    model_key: gat (nf)
    model_plain: GAT (NF)
    value: 0.735
    std: 0.015
    paper_value: 0.735
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 19
    true_value: 0.735
    true_std: 0.015
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.015
    is_best: false
  - model: SAGE (NF)
    model_key: sage (nf)
    model_plain: SAGE (NF)
    value: 0.729
    std: 0.006
    paper_value: 0.729
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 20
    true_value: 0.729
    true_std: 0.006
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.729
    sort_std: 0.006
    is_best: false
  - model: GCN (NF)
    model_key: gcn (nf)
    model_plain: GCN (NF)
    value: 0.702
    std: 0.018
    paper_value: 0.702
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 21
    true_value: 0.702
    true_std: 0.018
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.702
    sort_std: 0.018
    is_best: false
  - model: GIN (NF)
    model_key: gin (nf)
    model_plain: GIN (NF)
    value: 0.633
    std: 0.065
    paper_value: 0.633
    paper_std: 0.065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 22
    true_value: 0.633
    true_std: 0.065
    value_gap_source_arxiv: '2506.13912'
    value_gap_source_title: Density-aware Walks for Coordinated Campaign Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.633
    sort_std: 0.065
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id001
main_figure: /figures/2506.13912/main_figure.png
---

