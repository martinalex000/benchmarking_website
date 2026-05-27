---
title: Graph Convolutions Enrich the Self-Attention in Transformers!
arxiv_id: '2312.04234'
source_url: ''
authors: []
published_date: Dec 2023
published_date_iso: 2023-12
abstract: 'Transformers, renowned for their self-attention mechanism, have achieved
  state-of-the-art performance across various tasks in natural language processing,
  computer vision, time-series modeling, etc. However, one of the challenges with
  deep Transformer models is the oversmoothing problem, where representations across
  layers converge to indistinguishable values, leading to significant performance
  degradation. We interpret the original self-attention as a simple graph filter and
  redesign it from a graph signal processing (GSP) perspective. We propose a graph-filter-based
  self-attention (GFSA) The source code of GFSA is available at: https://github.com/jeongwhanchoi/GFSA.
  to learn a general yet effective one, whose complexity, however, is slightly larger
  than that of the original self-attention mechanism. We demonstrate that GFSA improves
  the performance of Transformers in various fields, including computer vision, natural
  language processing, graph-level tasks, speech recognition, and code classification.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Graphormer + GFSA
- GPS + GFSA
- Graph-ViT + GFSA
- GPT2 + GFSA
- CodeT5-small + GFSA
- CodeT5-base + GFSA
mrr: 0.0526
adjusted_mrr: 0.0351
mrr_dataset_count: 2
benchmark_categories:
- Classic
- LRGB
- GNNBenchmark
- OGB
- MoleculeNet
- Power Flow Benchmarks
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
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6967
    std: 0.004
    paper_value: 0.6967
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 36
    true_value: 0.73961
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042910000000000004
    value_note: ''
    paper_rank: 91
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.73961
    sort_std: 0.0033
    is_best: false
  - model: GPS + GFSA
    model_key: gps + gfsa
    model_plain: GPS + GFSA
    value: 0.7244
    std: 0.0048
    paper_value: 0.7244
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 50
    true_value: 0.7244
    true_std: 0.0048
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7244
    sort_std: 0.0048
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.723
    std: 0.0036
    paper_value: 0.723
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 53
    true_value: 0.72356
    true_std: 0.0032300000000000002
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005600000000000049
    value_note: global 0.7236 within std
    paper_rank: 56
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.72356
    sort_std: 0.0032300000000000002
    is_best: false
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.6987
    std: 0.0028
    paper_value: 0.6987
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 89
    true_value: 0.6987
    true_std: 0.0028
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6987
    sort_std: 0.0028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: Case 2
  rows:
  - model: GLR
    model_key: glr
    model_plain: GLR
    value: 0.47090000000000004
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.47090000000000004
    sort_std: null
    is_best: true
  - model: GLP
    model_key: glp
    model_plain: GLP
    value: 0.5072
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.5072
    sort_std: null
    is_best: false
  - model: MGL
    model_key: mgl
    model_plain: MGL
    value: 0.9606999999999999
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9606999999999999
    sort_std: null
    is_best: false
  - model: GPT2 + GFSA
    model_key: gpt2 + gfsa
    model_plain: GPT2 + GFSA
    value: 20.923
    std: null
    paper_value: 20.923
    paper_std: null
    metric: Perplexity
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: 20.923
    sort_std: null
    is_best: false
  - model: GPT2 + GFSA(K=2)
    model_key: gpt2 + gfsa(k=2)
    model_plain: GPT2 + GFSA(K=2)
    value: 20.923
    std: null
    paper_value: 20.923
    paper_std: null
    metric: Perplexity
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to case 2 (score=86)'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: 20.923
    sort_std: null
    is_best: false
  - model: GPT2
    model_key: gpt2
    model_plain: GPT2
    value: 20.966
    std: null
    paper_value: 20.966
    paper_std: null
    metric: Perplexity
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 117.0
    table_ref: Table 1
    source_ref: Radford et al. 2019
    variant_inference_reason: 'dataset: fuzzy match to case 2 (score=86)'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: null
    sort_value: 20.966
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
- &id008
  dataset: Code
  rows:
  - model: CodeT5-small + GFSA
    model_key: codet5-small + gfsa
    model_plain: CodeT5-small + GFSA
    value: 0.9494
    std: null
    paper_value: 0.9494
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 1
    true_value: 0.9494
    true_std: null
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9494
    sort_std: null
    is_best: true
  - model: CodeT5-base + GFSA
    model_key: codet5-base + gfsa
    model_plain: CodeT5-base + GFSA
    value: 0.9492
    std: null
    paper_value: 0.9492
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 2
    true_value: 0.9492
    true_std: null
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9492
    sort_std: null
    is_best: false
  - model: CodeT5-small
    model_key: codet5-small
    model_plain: CodeT5-small
    value: 0.9436
    std: null
    paper_value: 0.9436
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Wang et al. 2021
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 3
    true_value: 0.9436
    true_std: null
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9436
    sort_std: null
    is_best: false
  - model: CodeT5-base
    model_key: codet5-base
    model_plain: CodeT5-base
    value: 0.9431
    std: null
    paper_value: 0.9431
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Wang et al. 2021
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 4
    true_value: 0.9431
    true_std: null
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9431
    sort_std: null
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.1957
    std: 0.0025
    metric: F1
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
    global_rank: 5
    sort_value: 0.1957
    sort_std: 0.0025
    is_best: false
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 0.1948
    std: 0.0021
    metric: F1
    higher_is_better: true
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
    global_rank: 6
    sort_value: 0.1948
    sort_std: 0.0021
    is_best: false
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 0.1942
    std: 0.001
    metric: F1
    higher_is_better: true
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
    global_rank: 7
    sort_value: 0.1942
    sort_std: 0.001
    is_best: false
  metric: F1
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
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.9826
    std: 0.0004
    paper_value: 0.9826
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.9826
    true_std: 0.0004
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9826
    sort_std: 0.0004
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.982
    std: 0.0005
    paper_value: 0.982
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 39
    true_value: 0.982
    true_std: 0.0005
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.982
    sort_std: 0.0005
    is_best: false
  - model: GPS + GFSA
    model_key: gps + gfsa
    model_plain: GPS + GFSA
    value: 0.9814
    std: 0.0014
    paper_value: 0.9814
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 45
    true_value: 0.9814
    true_std: 0.0014
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9814
    sort_std: 0.0014
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.9805
    std: 0.0013
    paper_value: 0.9805
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 51
    true_value: 0.9811
    true_std: 0.0011
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005999999999999339
    value_note: global 0.9811 within std
    paper_rank: 62
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.9811
    sort_std: 0.0011
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: Graphormer + GFSA
    model_key: graphormer + gfsa
    model_plain: Graphormer + GFSA
    value: 0.086
    std: 0.0
    paper_value: 0.086
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 10
    true_value: 0.086
    true_std: 0.0
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.086
    sort_std: 0.0
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.0862
    std: 0.0
    paper_value: 0.0862
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 2
    source_ref: Ying et al. 2021
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 11
    true_value: 0.0862
    true_std: 0.0
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0862
    sort_std: 0.0
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
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6919
    std: 0.0085
    paper_value: 0.6919
    paper_std: 0.0085
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 60
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005099999999999993
    value_note: global 0.6970 within std
    paper_rank: 79
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.6964
    std: 0.0025
    paper_value: 0.6964
    paper_std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 65
    true_value: 0.6964
    true_std: 0.0025
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6964
    sort_std: 0.0025
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 152
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 166
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: GPS + GFSA
    model_key: gps + gfsa
    model_plain: GPS + GFSA
    value: 0.6593
    std: 0.0094
    paper_value: 0.6593
    paper_std: 0.0094
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 153
    true_value: 0.6593
    true_std: 0.0094
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6593
    sort_std: 0.0094
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
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.2474
    std: 0.0016
    paper_value: 0.2474
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 30
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0025000000000000022
    value_note: ''
    paper_rank: 82
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.2461
    std: 0.0024
    paper_value: 0.2461
    paper_std: 0.0024
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 57
    true_value: 0.2461
    true_std: 0.0024
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2461
    sort_std: 0.0024
    is_best: false
  - model: GPS + GFSA
    model_key: gps + gfsa
    model_plain: GPS + GFSA
    value: 0.2496
    std: 0.0013
    paper_value: 0.2496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 127
    true_value: 0.2496
    true_std: 0.0013
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2496
    sort_std: 0.0013
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 132
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  metric: MAE
  higher_is_better: false
- &id009
  dataset: Tox21
  rows:
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.874
    std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.874
    sort_std: 0.005
    is_best: true
  - model: Ours(dual readout)
    model_key: ours(dual readout)
    model_plain: Ours(dual readout)
    value: 0.851
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.851
    sort_std: 0.008
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.85
    std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.85
    sort_std: 0.009
    is_best: false
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.7895
    std: 0.0069
    paper_value: 0.7895
    paper_std: 0.0069
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to tox21 (score=90)'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 12
    true_value: 0.7895
    true_std: 0.0069
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7895
    sort_std: 0.0069
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.7851
    std: 0.0077
    paper_value: 0.7851
    paper_std: 0.0077
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to tox21 (score=90)'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 13
    true_value: 0.7851
    true_std: 0.0077
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7851
    sort_std: 0.0077
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
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
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:gps_vit)
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
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
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.124
    std: null
    paper_value: 0.124
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.099
    value_note: ''
    paper_rank: 200
    rank_delta: 182
    rank_delta_abs: 182
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.124
    std: 0.006
    paper_value: 0.124
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1 (tab:gnn_zinc_std)
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.099
    value_note: ''
    paper_rank: 200
    rank_delta: 182
    rank_delta_abs: 182
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.0849
    std: 0.0047
    paper_value: 0.0849
    paper_std: 0.0047
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:gps_vit)
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 34
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0499
    value_note: ''
    paper_rank: 150
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: GPS + GFSA
    model_key: gps + gfsa
    model_plain: GPS + GFSA
    value: 0.069
    std: 0.002
    paper_value: 0.069
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:gps_vit)
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 100
    true_value: 0.069
    true_std: 0.002
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.002
    is_best: false
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.0845
    std: 0.0032
    paper_value: 0.0845
    paper_std: 0.0032
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:gps_vit)
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 150
    true_value: 0.0845
    true_std: 0.0032
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0845
    sort_std: 0.0032
    is_best: false
  - model: Graphormer + GFSA
    model_key: graphormer + gfsa
    model_plain: Graphormer + GFSA
    value: 0.1189
    std: null
    paper_value: 0.1189
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 193
    true_value: 0.1189
    true_std: 0.002
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 193
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1189
    sort_std: 0.002
    is_best: false
  - model: Graphormer + GFSA
    model_key: graphormer + gfsa
    model_plain: Graphormer + GFSA
    value: 0.1189
    std: 0.002
    paper_value: 0.1189
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1 (tab:gnn_zinc_std)
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 193
    true_value: 0.1189
    true_std: 0.002
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 193
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1189
    sort_std: 0.002
    is_best: false
  metric: MAE
  higher_is_better: false
- &id006
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
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.783
    std: 0.0109
    paper_value: 0.783
    paper_std: 0.0109
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 90
    true_value: 0.783
    true_std: 0.0109
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.783
    sort_std: 0.0109
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.7792
    std: 0.0149
    paper_value: 0.7792
    paper_std: 0.0149
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 108
    true_value: 0.7792
    true_std: 0.0149
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7792
    sort_std: 0.0149
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
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
  - *id007
  - *id008
- benchmark: MoleculeNet
  datasets:
  - *id009
- benchmark: Power Flow Benchmarks
  datasets:
  - *id010
main_figure: /figures/2312.04234/main_figure.png
---

