---
title: A Scalable and Effective Alternative to Graph Transformers
arxiv_id: '2406.12059'
source_url: ''
authors: []
published_date: Jun 2024
published_date_iso: 2024-06
abstract: Graph Neural Networks (GNNs) have shown impressive performance in graph
  representation learning, but they face challenges in capturing long-range dependencies
  due to their limited expressive power. To address this, Graph Transformers (GTs)
  were introduced, utilizing self-attention mechanism to effectively model pairwise
  node relationships. Despite their advantages, GTs suffer from quadratic complexity
  w.r.t. the number of nodes in the graph, hindering their applicability to large
  graphs. In this work, we present, a scalable and effective alternative to GTs that
  leverages neighborhood propagation and global convolutions to effectively capture
  local and global dependencies in quasiliniear time. Our study on synthetic datasets
  reveals that reaches $169 $ speedup on a graph with 2M nodes w.r.t. optimized attention.
  Further evaluations on diverse range of benchmarks showcase that scales to large
  graphs where traditional GTs often face memory and time limitations. Notably, consistently
  achieves comparable or superior quality compared to baselines, improving the SOTA
  up to $4.5\ and offering a scalable and effective solution for large-scale graph
  learning.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GECO
mrr: 0.0722
adjusted_mrr: 0.0722
mrr_dataset_count: 9
benchmark_categories:
- Classic
- LRGB
- OGB
task_categories:
- graph_classification
- graph_regression
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id006
  dataset: COCO-SP
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.4901
    std: null
    metric: F1
    higher_is_better: true
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
    sort_value: 0.4901
    sort_std: null
    is_best: true
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.4752
    std: 0.0032
    metric: F1
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
    global_rank: 2
    sort_value: 0.4752
    sort_std: 0.0032
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.4483
    std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
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
    global_rank: 3
    sort_value: 0.4483
    sort_std: 0.0070999999999999995
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.3412
    std: 0.0044
    paper_value: 0.3412
    paper_std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.3884
    true_std: 0.0055000000000000005
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04720000000000002
    value_note: ''
    paper_rank: 31
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.3884
    sort_std: 0.0055000000000000005
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2641
    std: 0.0045
    paper_value: 0.2641
    paper_std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 21
    true_value: 0.3802
    true_std: 0.0015
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11609999999999998
    value_note: ''
    paper_rank: 47
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.3802
    sort_std: 0.0015
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3455
    std: 0.0009
    paper_value: 0.3455
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 31
    true_value: 0.3455
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3455
    sort_std: 0.0009
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.332
    std: 0.0032
    paper_value: 0.332
    paper_std: 0.0032
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 34
    true_value: 0.332
    true_std: 0.0032
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.332
    sort_std: 0.0032
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.0841
    std: 0.001
    paper_value: 0.0841
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 45
    true_value: 0.2733
    true_std: 0.0041
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18919999999999998
    value_note: ''
    paper_rank: 76
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.2733
    sort_std: 0.0041
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2618
    std: 0.0031
    paper_value: 0.2618
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 48
    true_value: 0.2618
    true_std: 0.0031
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2618
    sort_std: 0.0031
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2592
    std: 0.0158
    paper_value: 0.2592
    paper_std: 0.0158
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 53
    true_value: 0.2592
    true_std: 0.0158
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2592
    sort_std: 0.0158
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.2574
    std: 0.0034
    paper_value: 0.2574
    paper_std: 0.0034
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 57
    true_value: 0.2574
    true_std: 0.0034
    value_gap_source_arxiv: '2407.02758'
    value_gap_source_title: Differential Encoding for Improved Representation Learning
      over Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2574
    sort_std: 0.0034
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.2434
    std: 0.0156
    paper_value: 0.2434
    paper_std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 59
    true_value: 0.2434
    true_std: 0.0156
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2434
    sort_std: 0.0156
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.1339
    std: 0.0044
    paper_value: 0.1339
    paper_std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 64
    true_value: 0.2125
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0786
    value_note: ''
    paper_rank: 67
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.2125
    sort_std: 0.0009
    is_best: false
  metric: F1
  higher_is_better: true
- &id010
  dataset: Code
  rows:
  - model: CodeT5-small + GFSA
    model_key: codet5-small + gfsa
    model_plain: CodeT5-small + GFSA
    value: 0.9494
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9494
    sort_std: null
    is_best: true
  - model: CodeT5-base + GFSA
    model_key: codet5-base + gfsa
    model_plain: CodeT5-base + GFSA
    value: 0.9492
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.9492
    sort_std: null
    is_best: false
  - model: CodeT5-small
    model_key: codet5-small
    model_plain: CodeT5-small
    value: 0.9436
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9436
    sort_std: null
    is_best: false
  - model: K-Subtree SAT
    model_key: k-subtree sat
    model_plain: K-Subtree SAT
    value: 0.1937
    std: 0.0028
    paper_value: 0.1937
    paper_std: 0.0028
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 10
    true_value: 0.1937
    true_std: 0.0028
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1937
    sort_std: 0.0028
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.1915
    std: 0.002
    paper_value: 0.1915
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 13
    true_value: 0.1915
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1915
    sort_std: 0.002
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.1894
    std: 0.0024
    paper_value: 0.1894
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 16
    true_value: 0.1894
    true_std: 0.0024
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1894
    sort_std: 0.0024
    is_best: false
  - model: GraphTrans (GCN-Virtual)
    model_key: graphtrans (gcn-virtual)
    model_plain: GraphTrans (GCN-Virtual)
    value: 0.183
    std: 0.0024
    paper_value: 0.183
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 18
    true_value: 0.183
    true_std: 0.0024
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.183
    sort_std: 0.0024
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: PCQM-Contact
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.6143
    std: null
    metric: MRR
    higher_is_better: true
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
    sort_value: 0.6143
    sort_std: null
    is_best: true
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
    value: 0.5341
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.5341
    sort_std: null
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4707
    std: 0.0007
    metric: MRR
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
    global_rank: 3
    sort_value: 0.4707
    sort_std: 0.0007
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3218
    std: 0.0011
    paper_value: 0.3218
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.467
    true_std: 0.0004
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14520000000000005
    value_note: ''
    paper_rank: 61
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.467
    sort_std: 0.0004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3234
    std: 0.0006
    paper_value: 0.3234
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 7
    true_value: 0.4526
    true_std: 0.0006
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12919999999999998
    value_note: ''
    paper_rank: 60
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.4526
    sort_std: 0.0006
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3637
    std: 0.002
    paper_value: 0.3637
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 10
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3637
    sort_std: 0.002
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.3526
    std: 0.0016
    paper_value: 0.3526
    paper_std: 0.0016
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.3526
    true_std: 0.0016
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3526
    sort_std: 0.0016
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.318
    std: 0.0027
    paper_value: 0.318
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.3509
    true_std: 0.0006
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.032899999999999985
    value_note: ''
    paper_rank: 61
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.3509
    sort_std: 0.0006
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.3337
    std: 0.0006
    paper_value: 0.3337
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 27
    true_value: 0.3442
    true_std: 0.0009
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01050000000000001
    value_note: ''
    paper_rank: 48
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.3442
    sort_std: 0.0009
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.335
    std: 0.0003
    paper_value: 0.335
    paper_std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 45
    true_value: 0.335
    true_std: 0.0003
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.335
    sort_std: 0.0003
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.3341
    std: 0.0006
    paper_value: 0.3341
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 46
    true_value: 0.335
    true_std: 0.0003
    value_gap_source_arxiv: '2310.19285'
    value_gap_source_title: Facilitating Graph Neural Networks with Random Walk on
      Simplicial Complexes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0009000000000000119
    value_note: ''
    paper_rank: 48
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.335
    sort_std: 0.0003
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3242
    std: 0.0008
    paper_value: 0.3242
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 60
    true_value: 0.3242
    true_std: 0.0008
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3242
    sort_std: 0.0008
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.3174
    std: 0.002
    paper_value: 0.3174
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 62
    true_value: 0.3174
    true_std: 0.002
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3174
    sort_std: 0.002
    is_best: false
  metric: MRR
  higher_is_better: true
- &id009
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
    date: Feb 13, 2025
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
    date: Feb 13, 2025
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
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.0841
    std: null
    paper_value: 0.0841
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 4
    true_value: 0.0841
    true_std: null
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0841
    sort_std: null
    is_best: false
  - model: GPS-medium
    model_key: gps-medium
    model_plain: GPS-medium
    value: 0.0858
    std: null
    paper_value: 0.0858
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 19.4
    table_ref: Table 2
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 7
    true_value: 0.0858
    true_std: null
    value_gap_source_arxiv: '2504.12588'
    value_gap_source_title: Plain Transformers Can be Powerful Graph Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0858
    sort_std: null
    is_best: false
  - model: GPS-med
    model_key: gps-med
    model_plain: GPS-med
    value: 0.0858
    std: null
    paper_value: 0.0858
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.0858
    true_std: null
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0858
    sort_std: null
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.0864
    std: null
    paper_value: 0.0864
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 48.3
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 11
    true_value: 0.0862
    true_std: 0.0
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00020000000000000573
    value_note: ''
    paper_rank: 12
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.0862
    sort_std: 0.0
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.0869
    std: null
    paper_value: 0.0869
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 89.3
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 13
    true_value: 0.0869
    true_std: null
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0869
    sort_std: null
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.089
    std: null
    paper_value: 0.089
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 46.2
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 15
    true_value: 0.089
    true_std: null
    value_gap_source_arxiv: '2504.12588'
    value_gap_source_title: Plain Transformers Can be Powerful Graph Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.089
    sort_std: null
    is_best: false
  - model: GPS-small
    model_key: gps-small
    model_plain: GPS-small
    value: 0.0938
    std: null
    paper_value: 0.0938
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 6.2
    table_ref: Table 2
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 20
    true_value: 0.0938
    true_std: null
    value_gap_source_arxiv: '2504.12588'
    value_gap_source_title: Plain Transformers Can be Powerful Graph Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0938
    sort_std: null
    is_best: false
  - model: GPS-sm
    model_key: gps-sm
    model_plain: GPS-sm
    value: 0.0938
    std: null
    paper_value: 0.0938
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 21
    true_value: 0.0938
    true_std: null
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0938
    sort_std: null
    is_best: false
  - model: GCN-virtual
    model_key: gcn-virtual
    model_plain: GCN-virtual
    value: 0.1083
    std: null
    paper_value: 0.1083
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 4.9
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 28
    true_value: 0.1083
    true_std: null
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1083
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1379
    std: null
    paper_value: 0.1379
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 33
    true_value: 0.1195
    true_std: null
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0184
    value_note: ''
    paper_rank: 46
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.1195
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1195
    std: null
    paper_value: 0.1195
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 3.8
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 34
    true_value: 0.1195
    true_std: null
    value_gap_source_arxiv: '2504.12588'
    value_gap_source_title: Plain Transformers Can be Powerful Graph Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1195
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: PascalVOC-SP
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.567
    std: 0.0049
    metric: F1
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
    sort_value: 0.567
    sort_std: 0.0049
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4912
    std: 0.0042
    metric: F1
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
    sort_value: 0.4912
    sort_std: 0.0042
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.4653
    std: 0.0097
    metric: F1
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
    global_rank: 3
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.3748
    std: 0.0109
    paper_value: 0.3748
    paper_std: 0.0109
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 12
    true_value: 0.444
    true_std: 0.006500000000000001
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06919999999999998
    value_note: ''
    paper_rank: 46
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.444
    sort_std: 0.006500000000000001
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2873
    std: 0.0219
    paper_value: 0.2873
    paper_std: 0.0219
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 19
    true_value: 0.4263
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.139
    value_note: ''
    paper_rank: 74
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.4263
    sort_std: 0.0057
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.421
    std: 0.008
    paper_value: 0.421
    paper_std: 0.008
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 22
    true_value: 0.421
    true_std: 0.008
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.421
    sort_std: 0.008
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3975
    std: 0.0037
    paper_value: 0.3975
    paper_std: 0.0037
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 35
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3975
    sort_std: 0.0037
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1268
    std: 0.006
    paper_value: 0.1268
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 46
    true_value: 0.376
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2492
    value_note: ''
    paper_rank: 109
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.376
    sort_std: 0.001
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.323
    std: 0.0039
    paper_value: 0.323
    paper_std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 61
    true_value: 0.323
    true_std: 0.0039
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.323
    sort_std: 0.0039
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.3216
    std: 0.0027
    paper_value: 0.3216
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 65
    true_value: 0.3216
    true_std: 0.0027
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3216
    sort_std: 0.0027
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.286
    std: 0.0085
    paper_value: 0.286
    paper_std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 75
    true_value: 0.286
    true_std: 0.0085
    value_gap_source_arxiv: '2407.02758'
    value_gap_source_title: Differential Encoding for Improved Representation Learning
      over Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.286
    sort_std: 0.0085
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.1265
    std: 0.0076
    paper_value: 0.1265
    paper_std: 0.0076
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 80
    true_value: 0.2718
    true_std: 0.0054
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14529999999999998
    value_note: ''
    paper_rank: 109
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.2718
    sort_std: 0.0054
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2694
    std: 0.0098
    paper_value: 0.2694
    paper_std: 0.0098
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 81
    true_value: 0.2694
    true_std: 0.0098
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2694
    sort_std: 0.0098
    is_best: false
  metric: F1
  higher_is_better: true
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.6975
    std: 0.0025
    paper_value: 0.6975
    paper_std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 58
    true_value: 0.6975
    true_std: 0.0025
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6975
    sort_std: 0.0025
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
    table_ref: Table 3
    source_ref: He 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.697
    std: 0.008
    paper_value: 0.697
    paper_std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: He 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 63
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.008
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 171
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0041
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
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 32
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.002599999999999991
    value_note: ''
    paper_rank: 83
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.2464
    std: 0.0009
    paper_value: 0.2464
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
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 64
    true_value: 0.2464
    true_std: 0.0009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2464
    sort_std: 0.0009
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 140
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
  metric: MAE
  higher_is_better: false
- &id001
  dataset: Reddit
  rows:
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.9665
    std: 0.0005
    paper_value: 0.9665
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.9665
    sort_std: 0.0005
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.965
    std: 0.0011
    paper_value: 0.965
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.965
    sort_std: 0.0011
    is_best: true
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.965
    std: 0.0003
    paper_value: 0.965
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.965
    sort_std: 0.0003
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.959
    std: 0.0015
    paper_value: 0.959
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.959
    sort_std: 0.0015
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.957
    std: 0.0006
    paper_value: 0.957
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.957
    sort_std: 0.0006
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.9558
    std: 0.0007
    paper_value: 0.9558
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.9558
    sort_std: 0.0007
    is_best: false
  - model: ANS-GT
    model_key: ans-gt
    model_plain: ANS-GT
    value: 0.953
    std: 0.0081
    paper_value: 0.953
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.953
    sort_std: 0.0081
    is_best: false
  - model: SAT-SAMPLE
    model_key: sat-sample
    model_plain: SAT-SAMPLE
    value: 0.9337
    std: 0.0032
    paper_value: 0.9337
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.9337
    sort_std: 0.0032
    is_best: false
  - model: Graphormer-SAMPLE
    model_key: graphormer-sample
    model_plain: Graphormer-SAMPLE
    value: 0.9305
    std: 0.0022
    paper_value: 0.9305
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.9305
    sort_std: 0.0022
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9278
    std: 0.0011
    paper_value: 0.9278
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.9278
    sort_std: 0.0011
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8719
    sort_std: 0.0156
    is_best: false
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8482
    sort_std: 0.0162
    is_best: false
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8425
    sort_std: 0.0113
    is_best: false
  metric: F1
  higher_is_better: true
- &id008
  dataset: ogbg-molpcba
  rows:
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
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
    global_rank: 1
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
    value: 0.3066
    std: 0.0013
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
    global_rank: 3
    sort_value: 0.3066
    sort_std: 0.0013
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
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.2986
    true_std: 0.0025
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
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
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.2961
    std: 0.0008
    paper_value: 0.2961
    paper_std: 0.0008
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 10
    true_value: 0.2961
    true_std: 0.0008
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2961
    sort_std: 0.0008
    is_best: false
  - model: GIN-AK+
    model_key: gin-ak+
    model_plain: GIN-AK+
    value: 0.293
    std: 0.0044
    paper_value: 0.293
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.293
    true_std: 0.0044
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.293
    sort_std: 0.0044
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
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 21
    true_value: 0.2907
    true_std: 0.0028
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
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
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.2885
    std: 0.003
    paper_value: 0.2885
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 24
    true_value: 0.2885
    true_std: 0.003
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2885
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.2838
    std: 0.0035
    paper_value: 0.2838
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 29
    true_value: 0.2838
    true_std: 0.0035
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2838
    sort_std: 0.0035
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
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
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
  - model: GraphTrans (GCN-Virtual)
    model_key: graphtrans (gcn-virtual)
    model_plain: GraphTrans (GCN-Virtual)
    value: 0.2761
    std: 0.0029
    paper_value: 0.2761
    paper_std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 39
    true_value: 0.2761
    true_std: 0.0029
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2761
    sort_std: 0.0029
    is_best: false
  - model: GCN + virtual node
    model_key: gcn + virtual node
    model_plain: GCN + virtual node
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
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 42
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GatedGCN+LapPE
    model_key: gatedgcn+lappe
    model_plain: GatedGCN+LapPE
    value: 0.267
    std: 0.002
    paper_value: 0.267
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 45
    true_value: 0.267
    true_std: 0.002
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.267
    sort_std: 0.002
    is_best: false
  - model: ExpC
    model_key: expc
    model_plain: ExpC
    value: 0.2342
    std: 0.0029
    paper_value: 0.2342
    paper_std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 53
    true_value: 0.2342
    true_std: 0.0029
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2342
    sort_std: 0.0029
    is_best: false
  metric: AP
  higher_is_better: true
- &id007
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7593
    sort_std: 0.0019
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7025
    std: 0.0022
    paper_value: 0.7025
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03279999999999994
    value_note: ''
    paper_rank: 77
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7159
    std: 0.0038
    paper_value: 0.7159
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017100000000000004
    value_note: ''
    paper_rank: 66
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.731
    std: 0.0024
    paper_value: 0.731
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 23
    true_value: 0.731
    true_std: 0.0024
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.0024
    is_best: false
  - model: HSGT
    model_key: hsgt
    model_plain: HSGT
    value: 0.7258
    std: 0.0031
    paper_value: 0.7258
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 36
    true_value: 0.7258
    true_std: 0.0031
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7258
    sort_std: 0.0031
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7244
    std: 0.0028
    paper_value: 0.7244
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 41
    true_value: 0.7244
    true_std: 0.0028
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7244
    sort_std: 0.0028
    is_best: false
  - model: ANS-GT
    model_key: ans-gt
    model_plain: ANS-GT
    value: 0.682
    std: 0.0046
    paper_value: 0.682
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
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 43
    true_value: 0.7234
    true_std: 0.005
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04139999999999999
    value_note: ''
    paper_rank: 82
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.7234
    sort_std: 0.005
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.72
    std: 0.0016
    paper_value: 0.72
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 52
    true_value: 0.72
    true_std: 0.0016
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.0016
    is_best: false
  - model: Graphormer-SAMPLE
    model_key: graphormer-sample
    model_plain: Graphormer-SAMPLE
    value: 0.7043
    std: 0.002
    paper_value: 0.7043
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 77
    true_value: 0.7043
    true_std: 0.002
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7043
    sort_std: 0.002
    is_best: false
  - model: SAT-SAMPLE
    model_key: sat-sample
    model_plain: SAT-SAMPLE
    value: 0.682
    std: 0.0046
    paper_value: 0.682
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
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 83
    true_value: 0.682
    true_std: 0.0046
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.682
    sort_std: 0.0046
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.68
    std: 0.0059
    paper_value: 0.68
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 84
    true_value: 0.68
    true_std: 0.0059
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.0059
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.6795
    std: 0.0024
    paper_value: 0.6795
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 87
    true_value: 0.6795
    true_std: 0.0024
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6795
    sort_std: 0.0024
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
- benchmark: OGB
  datasets:
  - *id007
  - *id008
  - *id009
  - *id010
single_proposed_model: GECO
main_figure: /figures/2406.12059/main_figure.png
---

