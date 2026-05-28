---
title: Learning Graph Quantized Tokenizers
arxiv_id: '2410.13798'
source_url: ''
authors: []
published_date: Oct 17, 2024
published_date_iso: '2024-10-17'
abstract: Transformers serve as the backbone architectures of Foundational Models,
  where domain-specific tokenizers allow them to adapt to various domains. Graph Transformers
  (GTs) have recently emerged as leading models in geometric deep learning, outperforming
  Graph Neural Networks (GNNs) in various graph learning tasks. However, the development
  of tokenizers for graphs has lagged behind other modalities. To address this, we
  introduce GQT (Graph Quantized Tokenizer), which decouples tokenizer training from
  Transformer training by leveraging multi-task graph self-supervised learning, yielding
  robust and generalizable graph tokens. Furthermore, the GQT utilizes Residual Vector
  Quantization (RVQ) to learn hierarchical discrete tokens, resulting in significantly
  reduced memory requirements and improved generalization capabilities. By combining
  the GQT with token modulation, a Transformer encoder achieves state-of-the-art performance
  on 20 out of 22 benchmarks, including large-scale homophilic and heterophilic datasets.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- GQT
mrr: 0.0415
adjusted_mrr: 0.0415
mrr_dataset_count: 9
benchmark_categories:
- Classic
- Heterophilic Graphs
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
- &id008
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
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.4007
    std: 0.0125
    paper_value: 0.4007
    paper_std: 0.0125
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 8
    true_value: 0.4007
    true_std: 0.0125
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4007
    sort_std: 0.0125
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.396
    std: 0.0175
    paper_value: 0.396
    paper_std: 0.0175
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 12
    true_value: 0.396
    true_std: 0.0175
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.396
    sort_std: 0.0175
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 14
    true_value: 0.3884
    true_std: 0.0055
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04720000000000002
    value_note: ''
    paper_rank: 31
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.3884
    sort_std: 0.0055
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.343
    std: 0.0108
    paper_value: 0.343
    paper_std: 0.0108
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 31
    true_value: 0.3455
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0024999999999999467
    value_note: global 0.3455 within std
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3455
    sort_std: 0.0009
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
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
  metric: F1
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.765
    std: 0.0136
    paper_value: 0.765
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.048899999999999944
    value_note: ''
    paper_rank: 56
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7655
    std: 0.0123
    paper_value: 0.7655
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03970000000000007
    value_note: ''
    paper_rank: 56
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7742
    std: 0.0141
    paper_value: 0.7742
    paper_std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 26
    true_value: 0.8012
    true_std: 0.0124
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.027000000000000024
    value_note: ''
    paper_rank: 40
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0124
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7713
    std: 0.0167
    paper_value: 0.7713
    paper_std: 0.0167
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 25
    true_value: 0.8012
    true_std: 0.0083
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029900000000000038
    value_note: ''
    paper_rank: 43
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0083
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7633
    std: 0.0059
    paper_value: 0.7633
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 30
    true_value: 0.7956
    true_std: 0.011
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.032299999999999995
    value_note: ''
    paper_rank: 59
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.7956
    sort_std: 0.011
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.7653
    std: 0.0116
    paper_value: 0.7653
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 32
    true_value: 0.7933
    true_std: 0.0035
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.028000000000000025
    value_note: ''
    paper_rank: 56
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.7933
    sort_std: 0.0035
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7558
    std: 0.0133
    paper_value: 0.7558
    paper_std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 34
    true_value: 0.7923
    true_std: 0.0053
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03649999999999998
    value_note: ''
    paper_rank: 76
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.7923
    sort_std: 0.0053
    is_best: false
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.7784
    std: 0.0094
    paper_value: 0.7784
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 38
    true_value: 0.7784
    true_std: 0.0094
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7784
    sort_std: 0.0094
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7699
    std: 0.0112
    paper_value: 0.7699
    paper_std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 47
    true_value: 0.7699
    true_std: 0.0112
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7699
    sort_std: 0.0112
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7689
    std: 0.0119
    paper_value: 0.7689
    paper_std: 0.0119
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 50
    true_value: 0.7689
    true_std: 0.0119
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7689
    sort_std: 0.0119
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7683
    std: 0.0124
    paper_value: 0.7683
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 52
    true_value: 0.7683
    true_std: 0.0124
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7683
    sort_std: 0.0124
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.7672
    std: 0.0068
    paper_value: 0.7672
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 54
    true_value: 0.7672
    true_std: 0.0068
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7672
    sort_std: 0.0068
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.6712
    std: 0.0031
    paper_value: 0.6712
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 25
    true_value: 0.8857
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21450000000000002
    value_note: ''
    paper_rank: 263
    rank_delta: 238
    rank_delta_abs: 238
    rank_delta_direction: worse
    sort_value: 0.8857
    sort_std: 0.0069
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6447
    std: 0.0018
    paper_value: 0.6447
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2377999999999999
    value_note: ''
    paper_rank: 274
    rank_delta: 243
    rank_delta_abs: 243
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7151
    std: 0.0013
    paper_value: 0.7151
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 33
    true_value: 0.882
    true_std: 0.005
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16690000000000005
    value_note: ''
    paper_rank: 233
    rank_delta: 200
    rank_delta_abs: 200
    rank_delta_direction: worse
    sort_value: 0.882
    sort_std: 0.005
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.6516
    std: 0.0028
    paper_value: 0.6516
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 39
    true_value: 0.88
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22840000000000005
    value_note: ''
    paper_rank: 273
    rank_delta: 234
    rank_delta_abs: 234
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6176
    std: 0.0014
    paper_value: 0.6176
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2602
    value_note: ''
    paper_rank: 279
    rank_delta: 231
    rank_delta_abs: 231
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.5576
    std: 0.0023
    paper_value: 0.5576
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 114
    true_value: 0.8387
    true_std: 0.0096
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2811
    value_note: ''
    paper_rank: 293
    rank_delta: 179
    rank_delta_abs: 179
    rank_delta_direction: worse
    sort_value: 0.8387
    sort_std: 0.0096
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6909
    std: 0.0072
    paper_value: 0.6909
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 124
    true_value: 0.8329
    true_std: 0.0136
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14200000000000002
    value_note: ''
    paper_rank: 252
    rank_delta: 128
    rank_delta_abs: 128
    rank_delta_direction: worse
    sort_value: 0.8329
    sort_std: 0.0136
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.7137
    std: 0.0011
    paper_value: 0.7137
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 130
    true_value: 0.829
    true_std: 0.014
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11529999999999996
    value_note: ''
    paper_rank: 234
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.829
    sort_std: 0.014
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.5901
    std: 0.0034
    paper_value: 0.5901
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 143
    true_value: 0.8191
    true_std: 0.0342
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2290000000000001
    value_note: ''
    paper_rank: 286
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.8191
    sort_std: 0.0342
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.6105
    std: 0.0038
    paper_value: 0.6105
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 230
    true_value: 0.7184
    true_std: 0.0062
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1079
    value_note: ''
    paper_rank: 280
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.7184
    sort_std: 0.0062
    is_best: false
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.7181
    std: 0.0021
    paper_value: 0.7181
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 232
    true_value: 0.7181
    true_std: 0.0021
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 232
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7181
    sort_std: 0.0021
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.7167
    std: 0.001
    paper_value: 0.7167
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 233
    true_value: 0.7167
    true_std: 0.001
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 233
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7167
    sort_std: 0.001
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.6785
    std: 0.0021
    paper_value: 0.6785
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 258
    true_value: 0.6785
    true_std: 0.0021
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 258
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6785
    sort_std: 0.0021
    is_best: false
  - model: PPRGo
    model_key: pprgo
    model_plain: PPRGo
    value: 0.6354
    std: 0.0025
    paper_value: 0.6354
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 276
    true_value: 0.6354
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 276
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6354
    sort_std: 0.0025
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9906999999999999
    std: 0.0025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9906999999999999
    sort_std: 0.0025
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9899
    std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9899
    sort_std: 0.0016
    is_best: true
  - model: Tango<sub>GPS</sub>
    model_key: tango\textsubscript{gps}
    model_plain: TangoGPS
    value: 0.9839
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
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
    global_rank: 3
    sort_value: 0.9839
    sort_std: 0.0054
    is_best: true
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.9528
    std: 0.0044
    paper_value: 0.9528
    paper_std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 23
    true_value: 0.9528
    true_std: 0.0044
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9528
    sort_std: 0.0044
    is_best: false
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.9528
    std: 0.0044
    paper_value: 0.9528
    paper_std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 22
    true_value: 0.9528
    true_std: 0.0044
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9528
    sort_std: 0.0044
    is_best: false
  - model: Linear
    model_key: linear
    model_plain: Linear
    value: 0.9024
    std: 0.0049
    paper_value: 0.9024
    paper_std: 0.0049
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 71
    true_value: 0.9024
    true_std: 0.0049
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9024
    sort_std: 0.0049
    is_best: false
  - model: RQ-VAE
    model_key: rq-vae
    model_plain: RQ-VAE
    value: 0.8969
    std: 0.0035
    paper_value: 0.8969
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 78
    true_value: 0.8969
    true_std: 0.0035
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8969
    sort_std: 0.0035
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
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
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 4
    true_value: 0.4703
    true_std: 0.0014
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1366
    value_note: ''
    paper_rank: 48
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.4703
    sort_std: 0.0014
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
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
    value: 0.3587
    std: 0.0025
    paper_value: 0.3587
    paper_std: 0.0025
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 10
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0050000000000000044
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3637
    sort_std: 0.002
    is_best: false
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.3427
    std: 0.0012
    paper_value: 0.3427
    paper_std: 0.0012
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 31
    true_value: 0.3427
    true_std: 0.0012
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3427
    sort_std: 0.0012
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.3395
    std: 0.0013
    paper_value: 0.3395
    paper_std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 39
    true_value: 0.3395
    true_std: 0.0013
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3395
    sort_std: 0.0013
    is_best: false
  metric: MRR
  higher_is_better: true
- &id005
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
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
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.6903
    std: 0.0085
    paper_value: 0.6903
    paper_std: 0.0085
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 83
    true_value: 0.6903
    true_std: 0.0085
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6903
    sort_std: 0.0085
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.6739
    std: 0.0087
    paper_value: 0.6739
    paper_std: 0.0087
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 118
    true_value: 0.6739
    true_std: 0.0087
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6739
    sort_std: 0.0087
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
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
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6258
    std: 0.0092
    paper_value: 0.6258
    paper_std: 0.0092
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026899999999999924
    value_note: ''
    paper_rank: 229
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  metric: AP
  higher_is_better: true
- &id006
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
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
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.2452
    std: 0.0018
    paper_value: 0.2452
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 37
    true_value: 0.2452
    true_std: 0.0018
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2452
    sort_std: 0.0018
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.2478
    std: 0.0016
    paper_value: 0.2478
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 97
    true_value: 0.2478
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2478
    sort_std: 0.0016
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2512
    std: 0.0025
    paper_value: 0.2512
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0030999999999999917
    value_note: ''
    paper_rank: 155
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
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
    table_ref: "Table \ref{tab:LRGB}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
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
  metric: MAE
  higher_is_better: false
- &id003
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9476
    std: 0.001
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8654
    std: 0.0012
    paper_value: 0.8654
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05700000000000005
    value_note: ''
    paper_rank: 95
    rank_delta: 90
    rank_delta_abs: 90
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8632
    std: 0.0016
    paper_value: 0.8632
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05690000000000006
    value_note: ''
    paper_rank: 96
    rank_delta: 90
    rank_delta_abs: 90
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.9014
    std: 0.0016
    paper_value: 0.9014
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 18
    true_value: 0.9014
    true_std: 0.0016
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9014
    sort_std: 0.0016
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.8977
    std: 0.0015
    paper_value: 0.8977
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 25
    true_value: 0.8977
    true_std: 0.0015
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8977
    sort_std: 0.0015
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.897
    std: 0.0019
    paper_value: 0.897
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 27
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8952
    std: 0.0054
    paper_value: 0.8952
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 32
    true_value: 0.8952
    true_std: 0.0054
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8952
    sort_std: 0.0054
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.8951
    std: 0.0067
    paper_value: 0.8951
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 33
    true_value: 0.8951
    true_std: 0.0067
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8951
    sort_std: 0.0067
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8934
    std: 0.0025
    paper_value: 0.8934
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 37
    true_value: 0.8934
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8934
    sort_std: 0.0025
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8932
    std: 0.0025
    paper_value: 0.8932
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 38
    true_value: 0.8932
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8932
    sort_std: 0.0025
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.8896
    std: 0.0016
    paper_value: 0.8896
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 44
    true_value: 0.8896
    true_std: 0.0016
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8896
    sort_std: 0.0016
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8894
    std: 0.0016
    paper_value: 0.8894
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 45
    true_value: 0.8894
    true_std: 0.0016
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8894
    sort_std: 0.0016
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8879
    std: 0.0012
    paper_value: 0.8879
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 49
    true_value: 0.8879
    true_std: 0.0012
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8879
    sort_std: 0.0012
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8748
    std: 0.0038
    paper_value: 0.8748
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 54
    true_value: 0.8864
    true_std: 0.003
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.011599999999999944
    value_note: ''
    paper_rank: 81
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.8864
    sort_std: 0.003
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.8864
    std: 0.0009
    paper_value: 0.8864
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 55
    true_value: 0.8864
    true_std: 0.0009
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8864
    sort_std: 0.0009
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.8843
    std: 0.0015
    paper_value: 0.8843
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 58
    true_value: 0.8843
    true_std: 0.0015
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8843
    sort_std: 0.0015
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.8822
    std: 0.0015
    paper_value: 0.8822
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 67
    true_value: 0.8822
    true_std: 0.0015
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8822
    sort_std: 0.0015
    is_best: false
  - model: PPRGo
    model_key: pprgo
    model_plain: PPRGo
    value: 0.8738
    std: 0.0011
    paper_value: 0.8738
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 85
    true_value: 0.8738
    true_std: 0.0011
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8738
    sort_std: 0.0011
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8687
    std: 0.0024
    paper_value: 0.8687
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 92
    true_value: 0.8687
    true_std: 0.0024
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8687
    sort_std: 0.0024
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
    value: 0.7174
    std: 0.0029
    paper_value: 0.7174
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017899999999999916
    value_note: ''
    paper_rank: 64
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7195
    std: 0.0036
    paper_value: 0.7195
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013499999999999956
    value_note: ''
    paper_rank: 55
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: GQT
    model_key: gqt
    model_plain: GQT
    value: 0.7314
    std: 0.0016
    paper_value: 0.7314
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 22
    true_value: 0.7314
    true_std: 0.0016
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7314
    sort_std: 0.0016
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7149
    std: 0.0027
    paper_value: 0.7149
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 26
    true_value: 0.73
    true_std: 0.0028
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.015100000000000002
    value_note: ''
    paper_rank: 67
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.73
    sort_std: 0.0028
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7263
    std: 0.0013
    paper_value: 0.7263
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 31
    true_value: 0.7276
    true_std: 0.0033
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0013000000000000789
    value_note: global 0.7276 within std
    paper_rank: 35
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7276
    sort_std: 0.0033
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7241
    std: 0.004
    paper_value: 0.7241
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 33
    true_value: 0.7276
    true_std: 0.0029
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0035000000000000586
    value_note: global 0.7276 within std
    paper_rank: 42
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.7276
    sort_std: 0.0029
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
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
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
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.7195
    std: 0.0011
    paper_value: 0.7195
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 56
    true_value: 0.7195
    true_std: 0.0011
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7195
    sort_std: 0.0011
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7013
    std: 0.0055
    paper_value: 0.7013
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 67
    true_value: 0.7152
    true_std: 0.0024
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013899999999999912
    value_note: ''
    paper_rank: 77
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.7152
    sort_std: 0.0024
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7097
    std: 0.0041
    paper_value: 0.7097
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 71
    true_value: 0.7123
    true_std: 0.0059
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0026000000000000467
    value_note: global 0.7123 within std
    paper_rank: 75
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7123
    sort_std: 0.0059
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.711
    std: 0.0012
    paper_value: 0.711
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 75
    true_value: 0.711
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.711
    sort_std: 0.0012
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.599
    std: 0.0042
    paper_value: 0.599
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 89
    true_value: 0.6778
    true_std: 0.0028
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07879999999999998
    value_note: ''
    paper_rank: 96
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.6778
    sort_std: 0.0028
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.6618
    std: 0.0033
    paper_value: 0.6618
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023simplifying, luo2024structure
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 93
    true_value: 0.6618
    true_std: 0.0033
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6618
    sort_std: 0.0033
    is_best: false
  - model: RQ-VAE
    model_key: rq-vae
    model_plain: RQ-VAE
    value: 0.6605
    std: 0.0048
    paper_value: 0.6605
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 17, 2024
    date_display: Oct 2024
    date_iso: '2024-10-17'
    global_rank: 94
    true_value: 0.6605
    true_std: 0.0048
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6605
    sort_std: 0.0048
    is_best: false
  metric: Accuracy
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
- benchmark: LRGB
  datasets:
  - *id005
  - *id006
  - *id007
  - *id008
- benchmark: OGB
  datasets:
  - *id009
single_proposed_model: GQT
main_figure: /figures/2410.13798/main_figure.png
---

