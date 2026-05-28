---
title: Generalizable Insights for Graph Transformers in Theory and Practice
arxiv_id: '2511.08028'
source_url: ''
authors: []
published_date: Nov 2025
published_date_iso: 2025-11
abstract: Graph transformers (GTs) have shown strong empirical performance, yet current
  architectures vary widely in their use of attention mechanisms, positional embeddings
  (PEs), and expressivity. Existing expressivity results are often tied to specific
  design choices and lack comprehensive empirical validation on large-scale data.
  This leaves a gap between theory and practice, preventing generalizable insights
  that exceed particular application domains. Here, we propose the Generalized-Distance
  Transformer (GDT), a GT architecture based on standard attention that incorporates
  many recent advancements for GTs, and we develop a fine-grained understanding of
  the GDT's representation power in terms of attention and PEs. Through extensive
  experiments, we identify design choices that consistently perform well across various
  applications, tasks, and model scales, demonstrating strong performance in a few-shot
  transfer setting without fine-tuning. Our evaluation covers over eight million graphs
  with roughly 270M tokens across diverse domains, including image-based object detection,
  molecular property prediction, code summarization, and out-of-distribution algorithmic
  reasoning. We distill our theoretical and practical findings into several generalizable
  insights about effective GT design, training, and inference.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GT (no PE)
- GDT (LPE)
- GDT (SPE)
- GDT (RWSE)
- GDT (RRWP)
- RRWP
mrr: 0.1429
adjusted_mrr: 0.0476
mrr_dataset_count: 1
benchmark_categories:
- LRGB
- TU Dortmund
- GNNBenchmark
- OGB
- GraphBench
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
  dataset: Bridges
  rows:
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 0.9921
    std: 0.0009
    paper_value: 0.9921
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 1
    true_value: 0.9921
    true_std: 0.0009
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9921
    sort_std: 0.0009
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9831
    std: 0.0184
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9831
    sort_std: 0.0184
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.9269
    std: 0.0103
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9269
    sort_std: 0.0103
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.9176000000000001
    std: 0.0766
    paper_value: 0.9176000000000001
    paper_std: 0.0766
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 4
    true_value: 0.9176000000000001
    true_std: 0.0766
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9176000000000001
    sort_std: 0.0766
    is_best: true
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.8734000000000001
    std: 0.0397
    paper_value: 0.8734000000000001
    paper_std: 0.0397
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 5
    true_value: 0.8734000000000001
    true_std: 0.0397
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8734000000000001
    sort_std: 0.0397
    is_best: false
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 0.5536
    std: 0.2494
    paper_value: 0.5536
    paper_std: 0.2494
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 6
    true_value: 0.5536
    true_std: 0.2494
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5536
    sort_std: 0.2494
    is_best: false
  - model: GDT (SPE)
    model_key: gdt (spe)
    model_plain: GDT (SPE)
    value: 0.5481
    std: 0.212
    paper_value: 0.5481
    paper_std: 0.212
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 7
    true_value: 0.5481
    true_std: 0.212
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5481
    sort_std: 0.212
    is_best: false
  metric: F1
  higher_is_better: true
- &id002
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
    paper_value: 0.4483
    paper_std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 3
    true_value: 0.4483
    true_std: 0.0070999999999999995
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4483
    sort_std: 0.0070999999999999995
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4398
    std: 0.0033
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
    global_rank: 4
    sort_value: 0.4398
    sort_std: 0.0033
    is_best: false
  - model: GDT (SPE)
    model_key: gdt (spe)
    model_plain: GDT (SPE)
    value: 0.4387
    std: 0.0054
    paper_value: 0.4387
    paper_std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 5
    true_value: 0.4387
    true_std: 0.0054
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4387
    sort_std: 0.0054
    is_best: false
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.4382
    std: 0.0101
    paper_value: 0.4382
    paper_std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 6
    true_value: 0.4382
    true_std: 0.0101
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4382
    sort_std: 0.0101
    is_best: false
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 0.43119999999999997
    std: 0.0085
    paper_value: 0.43119999999999997
    paper_std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 7
    true_value: 0.43119999999999997
    true_std: 0.0085
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.43119999999999997
    sort_std: 0.0085
    is_best: false
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 0.39909999999999995
    std: 0.010700000000000001
    paper_value: 0.39909999999999995
    paper_std: 0.010700000000000001
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 9
    true_value: 0.39909999999999995
    true_std: 0.010700000000000001
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39909999999999995
    sort_std: 0.010700000000000001
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
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
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 0.1948
    std: 0.0021
    paper_value: 0.1948
    paper_std: 0.0021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 6
    true_value: 0.1948
    true_std: 0.0021
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1948
    sort_std: 0.0021
    is_best: false
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 0.1942
    std: 0.001
    paper_value: 0.1942
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 7
    true_value: 0.1942
    true_std: 0.001
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1942
    sort_std: 0.001
    is_best: false
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.19390000000000002
    std: 0.004699999999999999
    paper_value: 0.19390000000000002
    paper_std: 0.004699999999999999
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 8
    true_value: 0.19390000000000002
    true_std: 0.004699999999999999
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.19390000000000002
    sort_std: 0.004699999999999999
    is_best: false
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.1935
    std: 0.0021
    paper_value: 0.1935
    paper_std: 0.0021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 11
    true_value: 0.1935
    true_std: 0.0021
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1935
    sort_std: 0.0021
    is_best: false
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 0.19269999999999998
    std: 0.002
    paper_value: 0.19269999999999998
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 12
    true_value: 0.19269999999999998
    true_std: 0.002
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.19269999999999998
    sort_std: 0.002
    is_best: false
  metric: F1
  higher_is_better: true
- &id003
  dataset: D&D
  rows:
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 0.9921
    std: 0.0009
    paper_value: 0.9921
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.9921
    sort_std: 0.0009
    is_best: true
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.989
    std: null
    metric: Accuracy
    higher_is_better: true
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
    global_rank: 1
    sort_value: 0.989
    sort_std: null
    is_best: false
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    value: 0.981
    std: null
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.981
    sort_std: null
    is_best: false
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    value: 0.976
    std: null
    metric: Accuracy
    higher_is_better: true
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
    global_rank: 3
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.9176000000000001
    std: 0.0766
    paper_value: 0.9176000000000001
    paper_std: 0.0766
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.9176000000000001
    sort_std: 0.0766
    is_best: true
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.8734000000000001
    std: 0.0397
    paper_value: 0.8734000000000001
    paper_std: 0.0397
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.8734000000000001
    sort_std: 0.0397
    is_best: false
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 0.5536
    std: 0.2494
    paper_value: 0.5536
    paper_std: 0.2494
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.5536
    sort_std: 0.2494
    is_best: false
  - model: GDT (SPE)
    model_key: gdt (spe)
    model_plain: GDT (SPE)
    value: 0.5481
    std: 0.212
    paper_value: 0.5481
    paper_std: 0.212
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.5481
    sort_std: 0.212
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Flow
  rows:
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 1.45
    std: 0.06
    paper_value: 1.45
    paper_std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 1
    true_value: 1.45
    true_std: 0.06
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.45
    sort_std: 0.06
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 1.49
    std: 0.02
    paper_value: 1.49
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 2
    true_value: 1.49
    true_std: 0.02
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.49
    sort_std: 0.02
    is_best: true
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 1.73
    std: 0.09
    paper_value: 1.73
    paper_std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 3
    true_value: 1.73
    true_std: 0.09
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.73
    sort_std: 0.09
    is_best: false
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 1.75
    std: 0.12
    paper_value: 1.75
    paper_std: 0.12
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 4
    true_value: 1.75
    true_std: 0.12
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.75
    sort_std: 0.12
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 1.83
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    sort_value: 1.83
    sort_std: 0.01
    is_best: false
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 1.98
    std: 0.14
    paper_value: 1.98
    paper_std: 0.14
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 6
    true_value: 1.98
    true_std: 0.14
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.98
    sort_std: 0.14
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 3.4387
    std: 0.0631
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 3.4387
    sort_std: 0.0631
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 4.27
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 8
    sort_value: 4.27
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
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
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 0.9604
    std: 0.0091
    paper_value: 0.9604
    paper_std: 0.0091
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.9604
    sort_std: 0.0091
    is_best: false
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 0.9329000000000001
    std: 0.0088
    paper_value: 0.9329000000000001
    paper_std: 0.0088
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.9329000000000001
    sort_std: 0.0088
    is_best: false
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.9326000000000001
    std: 0.0045000000000000005
    paper_value: 0.9326000000000001
    paper_std: 0.0045000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.9326000000000001
    sort_std: 0.0045000000000000005
    is_best: false
  - model: GDT (SPE)
    model_key: gdt (spe)
    model_plain: GDT (SPE)
    value: 0.9251999999999999
    std: 0.0012
    paper_value: 0.9251999999999999
    paper_std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.9251999999999999
    sort_std: 0.0012
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.9107999999999999
    std: 0.0095
    paper_value: 0.9107999999999999
    paper_std: 0.0095
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.9107999999999999
    sort_std: 0.0095
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: MST
  rows:
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 0.9604
    std: 0.0091
    paper_value: 0.9604
    paper_std: 0.0091
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 1
    true_value: 0.9604
    true_std: 0.0091
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9604
    sort_std: 0.0091
    is_best: true
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 0.9329000000000001
    std: 0.0088
    paper_value: 0.9329000000000001
    paper_std: 0.0088
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 2
    true_value: 0.9329000000000001
    true_std: 0.0088
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9329000000000001
    sort_std: 0.0088
    is_best: false
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.9326000000000001
    std: 0.0045000000000000005
    paper_value: 0.9326000000000001
    paper_std: 0.0045000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 3
    true_value: 0.9326000000000001
    true_std: 0.0045000000000000005
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9326000000000001
    sort_std: 0.0045000000000000005
    is_best: false
  - model: GDT (SPE)
    model_key: gdt (spe)
    model_plain: GDT (SPE)
    value: 0.9251999999999999
    std: 0.0012
    paper_value: 0.9251999999999999
    paper_std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 4
    true_value: 0.9251999999999999
    true_std: 0.0012
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9251999999999999
    sort_std: 0.0012
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.9107999999999999
    std: 0.0095
    paper_value: 0.9107999999999999
    paper_std: 0.0095
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 5
    true_value: 0.9107999999999999
    true_std: 0.0095
    value_gap_source_arxiv: '2511.08028'
    value_gap_source_title: Generalizable Insights for Graph Transformers in Theory
      and Practice
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9107999999999999
    sort_std: 0.0095
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8566
    std: 0.0068
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.8566
    sort_std: 0.0068
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7288
    std: 0.0894
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.7288
    sort_std: 0.0894
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: PCQM-Contact
  rows:
  - model: SOTA (Range)
    model_key: sota (range)
    model_plain: SOTA (Range)
    value: 0.0809
    std: null
    paper_value: 0.0809
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: N/A (Text)
    source_ref: chen2023gpropagation, mueller2024et, ma+2023+GRIT, rampasek+2022+graphgps
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 0.0809
    sort_std: null
    is_best: true
  - model: GatedGCN
    model_key: gatedgcn (l=2)
    model_plain: GatedGCN
    value: 0.1927
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_display: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.1927
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn (l=2)
    model_plain: GCN
    value: 0.1944
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_display: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.1944
    sort_std: 0.002
    is_best: false
  - model: GINE
    model_key: gine (l=2)
    model_plain: GINE
    value: 0.1949
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_display: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.1949
    sort_std: 0.0006
    is_best: false
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 90.4
    std: 0.3
    paper_value: 90.4
    paper_std: 0.3
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 90.4
    sort_std: 0.3
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 92.7
    std: 0.9
    paper_value: 92.7
    paper_std: 0.9
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 92.7
    sort_std: 0.9
    is_best: false
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 92.9
    std: 0.6
    paper_value: 92.9
    paper_std: 0.6
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 92.9
    sort_std: 0.6
    is_best: false
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 93.6
    std: 0.5
    paper_value: 93.6
    paper_std: 0.5
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 93.6
    sort_std: 0.5
    is_best: false
  - model: GDT (SPE)
    model_key: gdt (spe)
    model_plain: GDT (SPE)
    value: 94.1
    std: 0.6
    paper_value: 94.1
    paper_std: 0.6
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: null
    sort_value: 94.1
    sort_std: 0.6
    is_best: false
  metric: MRR
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
- benchmark: TU Dortmund
  datasets:
  - *id003
- benchmark: GNNBenchmark
  datasets:
  - *id004
- benchmark: OGB
  datasets:
  - *id005
- benchmark: GraphBench
  datasets:
  - *id006
  - *id007
  - *id008
main_figure: /figures/2511.08028/main_figure.png
---

