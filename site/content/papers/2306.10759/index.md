---
title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
arxiv_id: '2306.10759'
source_url: ''
authors: []
published_date: Jun 19, 2023
published_date_iso: '2023-06-19'
published_venue: ''
abstract: Learning representations on large-sized graphs is a long-standing challenge
  due to the inter-dependence nature involved in massive data points. Transformers,
  as an emerging class of foundation encoders for graph-structured data, have shown
  promising performance on small graphs due to its global attention capable of capturing
  all-pair influence beyond neighboring nodes. Even so, existing approaches tend to
  inherit the spirit of Transformers in language and vision tasks, and embrace complicated
  models by stacking deep multi-head attentions. In this paper, we critically demonstrate
  that even using a one-layer attention can bring up surprisingly competitive performance
  across node property prediction benchmarks where node numbers range from thousand-level
  to billion-level. This encourages us to rethink the design philosophy for Transformers
  on large graphs, where the quadratic global attention is a computation overhead
  hindering the scalability. We frame the proposed scheme as Simplified Graph Transformers
  (SGFormer), which is empowered by a simple attention model that can efficiently
  propagate information among arbitrary nodes at the minimal cost of one propagation
  layer and linear complexity w.r.t. node numbers. Moreover, SGFormer requires none
  of positional encodings, feature/graph pre-processing or extra loss. Empirically,
  SGFormer successfully scales to the web-scale graph ogbn-papers100M and yields up
  to 141x inference acceleration over SOTA Transformers on medium-sized graphs. Beyond
  current results, we believe the proposed methodology alone enlightens a new technical
  path of independent interest for building Transformers on large graphs. The codes
  are publicly available at.
codebase_url: https://github.com/qitianwu/SGFormer
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- SGFormer
mrr: 0.0466
adjusted_mrr: 0.0466
mrr_dataset_count: 7
benchmark_categories:
- Classic
- Heterophilic Graphs
- OGB
- LINKX Benchmarks
- Other Graph Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id004
  dataset: Actor
  rows:
  - model: Vicuna-7B
    model_key: vicuna-7b
    model_plain: Vicuna-7B
    value: 0.7682
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.7682
    sort_std: 0.005
    is_best: true
  - model: Bloom 560M
    model_key: bloom 560m
    model_plain: Bloom 560M
    value: 0.7616
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.7616
    sort_std: 0.006
    is_best: true
  - model: 7B-to-560M
    model_key: 7b-to-560m
    model_plain: 7B-to-560M
    value: 0.7578
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7578
    sort_std: 0.002
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.344
    std: 0.017
    paper_value: 0.344
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: h2gcn-neurips20
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 14
    true_value: 0.7073
    true_std: 0.009
    value_gap_source_arxiv: '2408.14134'
    value_gap_source_title: Exploring the Potential of Large Language Models for Heterophilic
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.36330000000000007
    value_note: ''
    paper_rank: 117
    rank_delta: 103
    rank_delta_abs: 103
    rank_delta_direction: worse
    sort_value: 0.7073
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.301
    std: 0.002
    paper_value: 0.301
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GCN-vallina
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 18
    true_value: 0.667
    true_std: 0.013
    value_gap_source_arxiv: '2408.14134'
    value_gap_source_title: Exploring the Potential of Large Language Models for Heterophilic
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.36600000000000005
    value_note: ''
    paper_rank: 160
    rank_delta: 142
    rank_delta_abs: 142
    rank_delta_direction: worse
    sort_value: 0.667
    sort_std: 0.013
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.27
    std: 0.009
    paper_value: 0.27
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: SGC-icml19
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 19
    true_value: 0.667
    true_std: 0.019
    value_gap_source_arxiv: '2402.08824'
    value_gap_source_title: Disambiguated Node Classification with Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.397
    value_note: ''
    paper_rank: 184
    rank_delta: 165
    rank_delta_abs: 165
    rank_delta_direction: worse
    sort_value: 0.667
    sort_std: 0.019
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.298
    std: 0.006
    paper_value: 0.298
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GAT
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 20
    true_value: 0.6374
    true_std: 0.067
    value_gap_source_arxiv: '2408.14134'
    value_gap_source_title: Exploring the Potential of Large Language Models for Heterophilic
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3394
    value_note: ''
    paper_rank: 163
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.6374
    sort_std: 0.067
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.365
    std: 0.01
    paper_value: 0.365
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sign-2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 41
    true_value: 0.4122
    true_std: 0.0096
    value_gap_source_arxiv: '2403.07954'
    value_gap_source_title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive
      Krylov Subspace Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04720000000000002
    value_note: ''
    paper_rank: 76
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.4122
    sort_std: 0.0096
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.313
    std: 0.015
    paper_value: 0.313
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: appnp
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 47
    true_value: 0.399
    true_std: 0.0025
    value_gap_source_arxiv: '2305.06142'
    value_gap_source_title: arXiv:2305.06142
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08600000000000002
    value_note: ''
    paper_rank: 140
    rank_delta: 93
    rank_delta_abs: 93
    rank_delta_direction: worse
    sort_value: 0.399
    sort_std: 0.0025
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.364
    std: 0.016
    paper_value: 0.364
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: glognn
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 56
    true_value: 0.382
    true_std: 0.012
    value_gap_source_arxiv: '2205.13700'
    value_gap_source_title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily
      with Edge Splitting'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018000000000000016
    value_note: ''
    paper_rank: 81
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.382
    sort_std: 0.012
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.379
    std: 0.011
    paper_value: 0.379
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 58
    true_value: 0.379
    true_std: 0.011
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.379
    sort_std: 0.011
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.369
    std: 0.01
    paper_value: 0.369
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 69
    true_value: 0.369
    true_std: 0.01
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.369
    sort_std: 0.01
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.345
    std: 0.007
    paper_value: 0.345
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhu2021graph
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 117
    true_value: 0.345
    true_std: 0.007
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.345
    sort_std: 0.007
    is_best: false
  - model: Graphormer_UltrasSmall
    model_key: graphormer_ultrassmall
    model_plain: Graphormer_UltrasSmall
    value: 0.339
    std: 0.014
    paper_value: 0.339
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphformer-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 125
    true_value: 0.339
    true_std: 0.014
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.339
    sort_std: 0.014
    is_best: false
  - model: JK-Net
    model_key: jk-net
    model_plain: JK-Net
    value: 0.308
    std: 0.007
    paper_value: 0.308
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jknet-icml18
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 127
    true_value: 0.3341
    true_std: 0.0025
    value_gap_source_arxiv: '2202.04139'
    value_gap_source_title: Simplified Graph Convolution with Heterophily
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026100000000000012
    value_note: ''
    paper_rank: 150
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.3341
    sort_std: 0.0025
    is_best: false
  - model: GraphTrans (small)
    model_key: graphtrans (small)
    model_plain: GraphTrans (small)
    value: 0.326
    std: 0.007
    paper_value: 0.326
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphtrans-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 132
    true_value: 0.326
    true_std: 0.007
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.326
    sort_std: 0.007
    is_best: false
  - model: GraphTrans_UltrasSmall
    model_key: graphtrans_ultrassmall
    model_plain: GraphTrans_UltrasSmall
    value: 0.321
    std: 0.008
    paper_value: 0.321
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphtrans-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 134
    true_value: 0.321
    true_std: 0.008
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.321
    sort_std: 0.008
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Amazon2M
  rows:
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8909
    std: 0.001
    paper_value: 0.8909
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 1
    true_value: 0.8909
    true_std: 0.001
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8909
    sort_std: 0.001
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8785
    std: 0.0024
    paper_value: 0.8785
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: NodeFormer
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 2
    true_value: 0.8785
    true_std: 0.0024
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8785
    sort_std: 0.0024
    is_best: false
  - model: GAT-NSampler
    model_key: gat-nsampler
    model_plain: GAT-NSampler
    value: 0.8517
    std: 0.0032
    paper_value: 0.8517
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 3
    true_value: 0.8517
    true_std: 0.0032
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8517
    sort_std: 0.0032
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.839
    std: 0.001
    paper_value: 0.839
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 4
    true_value: 0.839
    true_std: 0.001
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.001
    is_best: false
  - model: GCN-NSampler
    model_key: gcn-nsampler
    model_plain: GCN-NSampler
    value: 0.8384
    std: 0.0042
    paper_value: 0.8384
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 5
    true_value: 0.8384
    true_std: 0.0042
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8384
    sort_std: 0.0042
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.8121
    std: 0.0012
    paper_value: 0.8121
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 6
    true_value: 0.8121
    true_std: 0.0012
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8121
    sort_std: 0.0012
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.8098
    std: 0.0031
    paper_value: 0.8098
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 7
    true_value: 0.8098
    true_std: 0.0031
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8098
    sort_std: 0.0031
    is_best: false
  - model: DAM-GT
    model_key: dam-gt
    model_plain: DAM-GT
    value: 0.7892
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.7892
    sort_std: 0.0033
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.7743
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.7743
    sort_std: 0.0024
    is_best: false
  - model: ANS-GT
    model_key: ans-gt
    model_plain: ANS-GT
    value: 0.7629
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.7629
    sort_std: 0.0032
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.6346
    std: 0.001
    paper_value: 0.6346
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 15
    true_value: 0.6346
    true_std: 0.001
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6346
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.952
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.952
    sort_std: 0.002
    is_best: true
  - model: Policy-GNN
    model_key: policy-gnn
    model_plain: Policy-GNN
    value: 0.897
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_display: Jun 2020
    date_iso: 2020-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.897
    sort_std: 0.021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.716
    std: 0.004
    paper_value: 0.716
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GCN-vallina
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 3
    true_value: 0.88
    true_std: null
    value_gap_source_arxiv: '1805.07984'
    value_gap_source_title: Adversarial Attacks on Neural Networks for Graph Data
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16400000000000003
    value_note: ''
    paper_rank: 382
    rank_delta: 379
    rank_delta_abs: 379
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: null
    is_best: false
  - model: AdaptKry
    model_key: adaptkry
    model_plain: AdaptKry
    value: 0.8378
    std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8378
    sort_std: 0.0038
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.721
    std: 0.011
    paper_value: 0.721
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GAT
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 8
    true_value: 0.8227
    true_std: 0.0068
    value_gap_source_arxiv: '2411.17676'
    value_gap_source_title: Instance-Aware Graph Prompt Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10170000000000001
    value_note: ''
    paper_rank: 362
    rank_delta: 354
    rank_delta_abs: 354
    rank_delta_direction: worse
    sort_value: 0.8227
    sort_std: 0.0068
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.725
    std: 0.011
    paper_value: 0.725
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 26
    true_value: 0.8028
    true_std: 0.0057
    value_gap_source_arxiv: '2402.15183'
    value_gap_source_title: 'GraphEdit: Large Language Models for Graph Structure
      Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07779999999999998
    value_note: ''
    paper_rank: 339
    rank_delta: 313
    rank_delta_abs: 313
    rank_delta_direction: worse
    sort_value: 0.8028
    sort_std: 0.0057
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.724
    std: 0.008
    paper_value: 0.724
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sign-2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 27
    true_value: 0.8014
    true_std: 0.0087
    value_gap_source_arxiv: '2403.07954'
    value_gap_source_title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive
      Krylov Subspace Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07740000000000002
    value_note: ''
    paper_rank: 350
    rank_delta: 323
    rank_delta_abs: 323
    rank_delta_direction: worse
    sort_value: 0.8014
    sort_std: 0.0087
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.719
    std: 0.001
    paper_value: 0.719
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: SGC-icml19
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 34
    true_value: 0.7965
    true_std: 0.0102
    value_gap_source_arxiv: '2403.07954'
    value_gap_source_title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive
      Krylov Subspace Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07750000000000001
    value_note: ''
    paper_rank: 368
    rank_delta: 334
    rank_delta_abs: 334
    rank_delta_direction: worse
    sort_value: 0.7965
    sort_std: 0.0102
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.718
    std: 0.005
    paper_value: 0.718
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: appnp
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 36
    true_value: 0.7933
    true_std: 0.0084
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07530000000000003
    value_note: ''
    paper_rank: 372
    rank_delta: 336
    rank_delta_abs: 336
    rank_delta_direction: worse
    sort_value: 0.7933
    sort_std: 0.0084
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.721
    std: 0.006
    paper_value: 0.721
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: glognn
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 60
    true_value: 0.7741
    true_std: null
    value_gap_source_arxiv: '2205.07308'
    value_gap_source_title: Finding Global Homophily in Graph Neural Networks When
      Meeting Heterophily
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.053100000000000036
    value_note: ''
    paper_rank: 362
    rank_delta: 302
    rank_delta_abs: 302
    rank_delta_direction: worse
    sort_value: 0.7741
    sort_std: null
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.714
    std: 0.007
    paper_value: 0.714
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: h2gcn-neurips20
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 66
    true_value: 0.7711
    true_std: null
    value_gap_source_arxiv: '2206.14418'
    value_gap_source_title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05710000000000004
    value_note: ''
    paper_rank: 398
    rank_delta: 332
    rank_delta_abs: 332
    rank_delta_direction: worse
    sort_value: 0.7711
    sort_std: null
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.716
    std: 0.004
    paper_value: 0.716
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhu2021graph
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 72
    true_value: 0.7691
    true_std: 0.0181
    value_gap_source_arxiv: '2402.15326'
    value_gap_source_title: Understanding Oversmoothing in Diffusion-Based GNNs From
      the Perspective of Operator Semigroup Theory
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.053100000000000036
    value_note: ''
    paper_rank: 382
    rank_delta: 310
    rank_delta_abs: 310
    rank_delta_direction: worse
    sort_value: 0.7691
    sort_std: 0.0181
    is_best: false
  - model: JK-Net
    model_key: jk-net
    model_plain: JK-Net
    value: 0.707
    std: 0.007
    paper_value: 0.707
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jknet-icml18
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 127
    true_value: 0.7585
    true_std: null
    value_gap_source_arxiv: '2206.14418'
    value_gap_source_title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05149999999999999
    value_note: ''
    paper_rank: 464
    rank_delta: 337
    rank_delta_abs: 337
    rank_delta_direction: worse
    sort_value: 0.7585
    sort_std: null
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.726
    std: 0.002
    paper_value: 0.726
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 335
    true_value: 0.726
    true_std: 0.002
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 335
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.002
    is_best: false
  - model: GraphTrans_UltrasSmall
    model_key: graphtrans_ultrassmall
    model_plain: GraphTrans_UltrasSmall
    value: 0.702
    std: 0.008
    paper_value: 0.702
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphtrans-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 491
    true_value: 0.702
    true_std: 0.008
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 491
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.702
    sort_std: 0.008
    is_best: false
  - model: GraphTrans (small)
    model_key: graphtrans (small)
    model_plain: GraphTrans (small)
    value: 0.695
    std: 0.007
    paper_value: 0.695
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphtrans-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 519
    true_value: 0.695
    true_std: 0.007
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 519
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.007
    is_best: false
  - model: Graphormer_Small
    model_key: graphormer_small
    model_plain: Graphormer_Small
    value: 0.656
    std: 0.006
    paper_value: 0.656
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphformer-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 609
    true_value: 0.656
    true_std: 0.006
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 609
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.656
    sort_std: 0.006
    is_best: false
  - model: Graphormer_UltrasSmall
    model_key: graphormer_ultrassmall
    model_plain: Graphormer_UltrasSmall
    value: 0.636
    std: 0.01
    paper_value: 0.636
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphformer-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 647
    true_value: 0.636
    true_std: 0.01
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 647
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.636
    sort_std: 0.01
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: Self-Explainable GNN
    model_key: self-explainable gnn
    model_plain: Self-Explainable GNN
    value: 0.977
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.977
    sort_std: 0.016
    is_best: true
  - model: GCN-K
    model_key: gcn-k
    model_plain: GCN-K
    value: 0.948
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.007
    is_best: false
  - model: KP-GIN
    model_key: kp-gin
    model_plain: KP-GIN
    value: 0.946
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.946
    sort_std: 0.007
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.816
    std: 0.004
    paper_value: 0.816
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GCN-vallina
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 22
    true_value: 0.9004
    true_std: null
    value_gap_source_arxiv: '2401.09125'
    value_gap_source_title: arXiv:2401.09125
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08440000000000003
    value_note: ''
    paper_rank: 504
    rank_delta: 482
    rank_delta_abs: 482
    rank_delta_direction: worse
    sort_value: 0.9004
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.833
    std: 0.005
    paper_value: 0.833
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: appnp
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 50
    true_value: 0.8904
    true_std: 0.015
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05740000000000001
    value_note: ''
    paper_rank: 375
    rank_delta: 325
    rank_delta_abs: 325
    rank_delta_direction: worse
    sort_value: 0.8904
    sort_std: 0.015
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.83
    std: 0.007
    paper_value: 0.83
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GAT
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 54
    true_value: 0.8897
    true_std: null
    value_gap_source_arxiv: '2605.24867'
    value_gap_source_title: 'Clustering as Reasoning: A $k$-Means Interpretation of
      Chain-of-Thought Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059700000000000086
    value_note: ''
    paper_rank: 404
    rank_delta: 350
    rank_delta_abs: 350
    rank_delta_direction: worse
    sort_value: 0.8897
    sort_std: null
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.822
    std: 0.009
    paper_value: 0.822
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 71
    true_value: 0.8856
    true_std: 0.0101
    value_gap_source_arxiv: '2410.12096'
    value_gap_source_title: Bridging Large Language Models and Graph Structure Learning
      Models for Robust Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0636000000000001
    value_note: ''
    paper_rank: 462
    rank_delta: 391
    rank_delta_abs: 391
    rank_delta_direction: worse
    sort_value: 0.8856
    sort_std: 0.0101
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.819
    std: 0.004
    paper_value: 0.819
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: glognn
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 86
    true_value: 0.8833
    true_std: 0.011
    value_gap_source_arxiv: '2209.15454'
    value_gap_source_title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel
      Geometric Polynomials'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06430000000000002
    value_note: ''
    paper_rank: 485
    rank_delta: 399
    rank_delta_abs: 399
    rank_delta_direction: worse
    sort_value: 0.8833
    sort_std: 0.011
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.825
    std: 0.008
    paper_value: 0.825
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: h2gcn-neurips20
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 89
    true_value: 0.8829
    true_std: 0.0018
    value_gap_source_arxiv: '2506.08871'
    value_gap_source_title: Adapting to Heterophilic Graph Data with Structure-Guided
      Neighbor Discovery
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05790000000000006
    value_note: ''
    paper_rank: 440
    rank_delta: 351
    rank_delta_abs: 351
    rank_delta_direction: worse
    sort_value: 0.8829
    sort_std: 0.0018
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.801
    std: 0.002
    paper_value: 0.801
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: SGC-icml19
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 101
    true_value: 0.8805
    true_std: 0.0208
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0794999999999999
    value_note: ''
    paper_rank: 559
    rank_delta: 458
    rank_delta_abs: 458
    rank_delta_direction: worse
    sort_value: 0.8805
    sort_std: 0.0208
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.821
    std: 0.003
    paper_value: 0.821
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sign-2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 126
    true_value: 0.877
    true_std: 0.0069
    value_gap_source_arxiv: '2403.07954'
    value_gap_source_title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive
      Krylov Subspace Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05600000000000005
    value_note: ''
    paper_rank: 472
    rank_delta: 346
    rank_delta_abs: 346
    rank_delta_direction: worse
    sort_value: 0.877
    sort_std: 0.0069
    is_best: false
  - model: JK-Net
    model_key: jk-net
    model_plain: JK-Net
    value: 0.818
    std: 0.005
    paper_value: 0.818
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jknet-icml18
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 149
    true_value: 0.8716
    true_std: 0.0041
    value_gap_source_arxiv: '2405.18581'
    value_gap_source_title: 'Unleashing the Potential of Text-attributed Graphs: Automatic
      Relation Decomposition via Large Language Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05360000000000009
    value_note: ''
    paper_rank: 493
    rank_delta: 344
    rank_delta_abs: 344
    rank_delta_direction: worse
    sort_value: 0.8716
    sort_std: 0.0041
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.808
    std: 0.004
    paper_value: 0.808
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhu2021graph
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 150
    true_value: 0.871
    true_std: 0.0135
    value_gap_source_arxiv: '2402.15326'
    value_gap_source_title: Understanding Oversmoothing in Diffusion-Based GNNs From
      the Perspective of Operator Semigroup Theory
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06299999999999994
    value_note: ''
    paper_rank: 535
    rank_delta: 385
    rank_delta_abs: 385
    rank_delta_direction: worse
    sort_value: 0.871
    sort_std: 0.0135
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.845
    std: 0.008
    paper_value: 0.845
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 182
    true_value: 0.8624
    true_std: 0.0158
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017400000000000082
    value_note: ''
    paper_rank: 269
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.8624
    sort_std: 0.0158
    is_best: false
  - model: GraphTrans_UltrasSmall
    model_key: graphtrans_ultrassmall
    model_plain: GraphTrans_UltrasSmall
    value: 0.817
    std: 0.006
    paper_value: 0.817
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphtrans-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 499
    true_value: 0.817
    true_std: 0.006
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 499
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.817
    sort_std: 0.006
    is_best: false
  - model: GraphTrans (small)
    model_key: graphtrans (small)
    model_plain: GraphTrans (small)
    value: 0.807
    std: 0.009
    paper_value: 0.807
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphtrans-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 540
    true_value: 0.807
    true_std: 0.009
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 540
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.807
    sort_std: 0.009
    is_best: false
  - model: Graphormer_Small
    model_key: graphormer_small
    model_plain: Graphormer_Small
    value: 0.758
    std: 0.011
    paper_value: 0.758
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphformer-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 658
    true_value: 0.758
    true_std: 0.011
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 658
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.011
    is_best: false
  - model: Graphormer_UltrasSmall
    model_key: graphormer_ultrassmall
    model_plain: Graphormer_UltrasSmall
    value: 0.742
    std: 0.009
    paper_value: 0.742
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphformer-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 683
    true_value: 0.742
    true_std: 0.009
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 683
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.009
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Pokec
  rows:
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_display: May 2022
    date_iso: '2022-05-15'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: MLP for adjacency matrix only
    model_key: mlp for adjacency matrix only
    model_plain: MLP for adjacency matrix only
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_display: May 2022
    date_iso: '2022-05-15'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: GTs
    model_key: gts
    model_plain: GTs
    value: 0.7911
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7911
    sort_std: 0.0006
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7376
    std: 0.0024
    paper_value: 0.7376
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 5
    true_value: 0.7376
    true_std: 0.0024
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7376
    sort_std: 0.0024
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6231
    std: 0.0113
    paper_value: 0.6231
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 6
    true_value: 0.7309
    true_std: 0.0028
    value_gap_source_arxiv: '2202.04187'
    value_gap_source_title: 'FMP: Toward Fair Graph Message Passing against Topology
      Bias'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1078
    value_note: ''
    paper_rank: 16
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.7309
    sort_std: 0.0028
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.6015
    std: 0.0003
    paper_value: 0.6015
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 7
    true_value: 0.7248
    true_std: 0.0026
    value_gap_source_arxiv: '2202.04187'
    value_gap_source_title: 'FMP: Toward Fair Graph Message Passing against Topology
      Bias'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12329999999999997
    value_note: ''
    paper_rank: 18
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.7248
    sort_std: 0.0026
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.5203
    std: 0.0084
    paper_value: 0.5203
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 9
    true_value: 0.7146
    true_std: 0.0041
    value_gap_source_arxiv: '2202.04187'
    value_gap_source_title: 'FMP: Toward Fair Graph Message Passing against Topology
      Bias'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19430000000000003
    value_note: ''
    paper_rank: 21
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.7146
    sort_std: 0.0041
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7032
    std: 0.0045
    paper_value: 0.7032
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: NodeFormer
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 11
    true_value: 0.7032
    true_std: 0.0045
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7032
    sort_std: 0.0045
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.6801
    std: 0.0025
    paper_value: 0.6801
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 14
    true_value: 0.6801
    true_std: 0.0025
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6801
    sort_std: 0.0025
    is_best: false
  - model: GCN-NSampler
    model_key: gcn-nsampler
    model_plain: GCN-NSampler
    value: 0.6375
    std: 0.0077
    paper_value: 0.6375
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 15
    true_value: 0.6375
    true_std: 0.0077
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6375
    sort_std: 0.0077
    is_best: false
  - model: GAT-NSampler
    model_key: gat-nsampler
    model_plain: GAT-NSampler
    value: 0.6232
    std: 0.0065
    paper_value: 0.6232
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 16
    true_value: 0.6232
    true_std: 0.0065
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6232
    sort_std: 0.0065
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: AIO
    model_key: aio
    model_plain: AIO
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.96
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.96
    sort_std: 0.001
    is_best: false
  - model: SAGN
    model_key: sagn
    model_plain: SAGN
    value: 0.9517
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9517
    sort_std: null
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.799
    std: 0.01
    paper_value: 0.799
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 6
    true_value: 0.9490000000000001
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15000000000000002
    value_note: ''
    paper_rank: 373
    rank_delta: 367
    rank_delta_abs: 367
    rank_delta_direction: worse
    sort_value: 0.9490000000000001
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.788
    std: 0.006
    paper_value: 0.788
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GCN-vallina
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 29
    true_value: 0.9296
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14159999999999995
    value_note: ''
    paper_rank: 495
    rank_delta: 466
    rank_delta_abs: 466
    rank_delta_direction: worse
    sort_value: 0.9296
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.79
    std: 0.004
    paper_value: 0.79
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GAT
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 31
    true_value: 0.9233
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13329999999999997
    value_note: ''
    paper_rank: 467
    rank_delta: 436
    rank_delta_abs: 436
    rank_delta_direction: worse
    sort_value: 0.9233
    sort_std: null
    is_best: false
  - model: JK-Net
    model_key: jk-net
    model_plain: JK-Net
    value: 0.788
    std: 0.007
    paper_value: 0.788
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jknet-icml18
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 79
    true_value: 0.8968
    true_std: 0.0014
    value_gap_source_arxiv: '2405.18581'
    value_gap_source_title: 'Unleashing the Potential of Text-attributed Graphs: Automatic
      Relation Decomposition via Large Language Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10880000000000001
    value_note: ''
    paper_rank: 495
    rank_delta: 416
    rank_delta_abs: 416
    rank_delta_direction: worse
    sort_value: 0.8968
    sort_std: 0.0014
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.794
    std: 0.004
    paper_value: 0.794
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: h2gcn-neurips20
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 83
    true_value: 0.8967
    true_std: 0.003
    value_gap_source_arxiv: '2411.12330'
    value_gap_source_title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10270000000000001
    value_note: ''
    paper_rank: 416
    rank_delta: 333
    rank_delta_abs: 333
    rank_delta_direction: worse
    sort_value: 0.8967
    sort_std: 0.003
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.789
    std: 0.004
    paper_value: 0.789
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: glognn
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 84
    true_value: 0.8962
    true_std: null
    value_gap_source_arxiv: '2205.07308'
    value_gap_source_title: Finding Global Homophily in Graph Neural Networks When
      Meeting Heterophily
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10719999999999996
    value_note: ''
    paper_rank: 486
    rank_delta: 402
    rank_delta_abs: 402
    rank_delta_direction: worse
    sort_value: 0.8962
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.801
    std: 0.002
    paper_value: 0.801
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: appnp
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 93
    true_value: 0.894
    true_std: null
    value_gap_source_arxiv: '2206.14418'
    value_gap_source_title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09299999999999997
    value_note: ''
    paper_rank: 362
    rank_delta: 269
    rank_delta_abs: 269
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: null
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.803
    std: 0.006
    paper_value: 0.803
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 102
    true_value: 0.8931
    true_std: 0.0017
    value_gap_source_arxiv: '2505.17660'
    value_gap_source_title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking
      Graph Transformer for Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09009999999999996
    value_note: ''
    paper_rank: 351
    rank_delta: 249
    rank_delta_abs: 249
    rank_delta_direction: worse
    sort_value: 0.8931
    sort_std: 0.0017
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.795
    std: 0.005
    paper_value: 0.795
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sign-2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 110
    true_value: 0.8909
    true_std: 0.0043
    value_gap_source_arxiv: '2403.07954'
    value_gap_source_title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive
      Krylov Subspace Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09589999999999999
    value_note: ''
    paper_rank: 407
    rank_delta: 297
    rank_delta_abs: 297
    rank_delta_direction: worse
    sort_value: 0.8909
    sort_std: 0.0043
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.787
    std: 0.001
    paper_value: 0.787
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: SGC-icml19
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 151
    true_value: 0.88
    true_std: null
    value_gap_source_arxiv: '2407.14996'
    value_gap_source_title: 'All Against Some: Efficient Integration of Large Language
      Models for Message Passing in Graph Neural Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09299999999999997
    value_note: ''
    paper_rank: 499
    rank_delta: 348
    rank_delta_abs: 348
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: null
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.785
    std: 0.007
    paper_value: 0.785
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhu2021graph
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 164
    true_value: 0.877
    true_std: 0.0049
    value_gap_source_arxiv: '2402.15326'
    value_gap_source_title: Understanding Oversmoothing in Diffusion-Based GNNs From
      the Perspective of Operator Semigroup Theory
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09199999999999997
    value_note: ''
    paper_rank: 512
    rank_delta: 348
    rank_delta_abs: 348
    rank_delta_direction: worse
    sort_value: 0.877
    sort_std: 0.0049
    is_best: false
  - model: GraphTrans_UltrasSmall
    model_key: graphtrans_ultrassmall
    model_plain: GraphTrans_UltrasSmall
    value: 0.774
    std: 0.005
    paper_value: 0.774
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphtrans-neurips21
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 559
    true_value: 0.774
    true_std: 0.005
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 559
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.774
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: ogbn-papers100M
  rows:
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.782
    std: 0.001
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
    global_rank: 1
    sort_value: 0.782
    sort_std: 0.001
    is_best: true
  - model: Graver
    model_key: graver
    model_plain: Graver
    value: 0.7762
    std: 0.0294
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 5, 2025
    date_display: Nov 2025
    date_iso: '2025-11-05'
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.7762
    sort_std: 0.0294
    is_best: true
  - model: GraphSAINT + RWSE
    model_key: graphsaint + rwse
    model_plain: GraphSAINT + RWSE
    value: 0.775
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
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.6329
    std: 0.0019
    paper_value: 0.6329
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Xu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 30
    true_value: 0.679
    true_std: 0.0
    value_gap_source_arxiv: '2511.06443'
    value_gap_source_title: How Wide and How Deep? Mitigating Over-Squashing of GNNs
      via Channel Capacity Constrained Estimation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04610000000000003
    value_note: ''
    paper_rank: 57
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.679
    sort_std: 0.0
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.6511
    std: 0.0014
    paper_value: 0.6511
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Fey et al.
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 41
    true_value: 0.6606
    true_std: null
    value_gap_source_arxiv: '2502.19693'
    value_gap_source_title: Accurate and Scalable Graph Neural Networks via Message
      Invariance
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009499999999999953
    value_note: ''
    paper_rank: 46
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.6606
    sort_std: null
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.6601
    std: 0.0037
    paper_value: 0.6601
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 42
    true_value: 0.6601
    true_std: 0.0037
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6601
    sort_std: 0.0037
    is_best: false
  - model: GAT-NSampler
    model_key: gat-nsampler
    model_plain: GAT-NSampler
    value: 0.6347
    std: 0.0039
    paper_value: 0.6347
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 57
    true_value: 0.6347
    true_std: 0.0039
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6347
    sort_std: 0.0039
    is_best: false
  - model: GCN-NSampler
    model_key: gcn-nsampler
    model_plain: GCN-NSampler
    value: 0.6204
    std: 0.0027
    paper_value: 0.6204
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 59
    true_value: 0.6204
    true_std: 0.0027
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6204
    sort_std: 0.0027
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.4724
    std: 0.0031
    paper_value: 0.4724
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 68
    true_value: 0.4724
    true_std: 0.0031
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4724
    sort_std: 0.0031
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ogbn-proteins
  rows:
  - model: RevGNN-Wide
    model_key: revgnn-wide
    model_plain: RevGNN-Wide
    value: 0.8824
    std: 0.0015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8824
    sort_std: 0.0015
    is_best: true
  - model: RevGNN-Deep
    model_key: revgnn-deep
    model_plain: RevGNN-Deep
    value: 0.8774
    std: 0.0013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8774
    sort_std: 0.0013
    is_best: false
  - model: UniMP+CEF
    model_key: unimp+cef
    model_plain: UniMP+CEF
    value: 0.8691
    std: 0.0018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8691
    sort_std: 0.0018
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7251
    std: 0.0035
    paper_value: 0.7251
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 13
    true_value: 0.815
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08989999999999998
    value_note: ''
    paper_rank: 27
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.815
    sort_std: 0.003
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7953
    std: 0.0038
    paper_value: 0.7953
    paper_std: 0.0038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 15
    true_value: 0.7953
    true_std: 0.0038
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7953
    sort_std: 0.0038
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7745
    std: 0.0115
    paper_value: 0.7745
    paper_std: 0.0115
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al.
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 21
    true_value: 0.7745
    true_std: 0.0115
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7745
    sort_std: 0.0115
    is_best: false
  - model: GAT-NSampler
    model_key: gat-nsampler
    model_plain: GAT-NSampler
    value: 0.7463
    std: 0.0124
    paper_value: 0.7463
    paper_std: 0.0124
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 24
    true_value: 0.7463
    true_std: 0.0124
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7463
    sort_std: 0.0124
    is_best: false
  - model: GCN-NSampler
    model_key: gcn-nsampler
    model_plain: GCN-NSampler
    value: 0.7351
    std: 0.0131
    paper_value: 0.7351
    paper_std: 0.0131
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 26
    true_value: 0.7351
    true_std: 0.0131
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7351
    sort_std: 0.0131
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7204
    std: 0.0048
    paper_value: 0.7204
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 29
    true_value: 0.7204
    true_std: 0.0048
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7204
    sort_std: 0.0048
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.7124
    std: 0.0046
    paper_value: 0.7124
    paper_std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Fey et al.
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 31
    true_value: 0.7124
    true_std: 0.0046
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7124
    sort_std: 0.0046
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.7031
    std: 0.0023
    paper_value: 0.7031
    paper_std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Jun 19, 2023
    date_display: Jun 2023
    date_iso: '2023-06-19'
    published_venue: null
    global_rank: 32
    true_value: 0.7031
    true_std: 0.0023
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7031
    sort_std: 0.0023
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterophilic Graphs
  datasets:
  - *id004
- benchmark: OGB
  datasets:
  - *id005
  - *id006
- benchmark: LINKX Benchmarks
  datasets:
  - *id007
- benchmark: Other Graph Benchmarks
  datasets:
  - *id008
single_proposed_model: SGFormer
---

