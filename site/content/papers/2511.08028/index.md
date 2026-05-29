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
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- RRWP
- GDT + RRWP
mrr: 0.2
adjusted_mrr: 0.0667
mrr_dataset_count: 1
benchmark_categories:
- LRGB
- GraphBench
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id004
  dataset: Bridges
  rows:
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 0.9921
    std: 0.0009
    paper_value: 0.9921
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 16.0
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
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
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 0.9176
    std: 0.0766
    paper_value: 0.9176
    paper_std: 0.0766
    metric: F1
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
    global_rank: 2
    true_value: 0.9176
    true_std: 0.0766
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
    sort_value: 0.9176
    sort_std: 0.0766
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.8734
    std: 0.0397
    paper_value: 0.8734
    paper_std: 0.0397
    metric: F1
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
    global_rank: 3
    true_value: 0.8734
    true_std: 0.0397
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
    sort_value: 0.8734
    sort_std: 0.0397
    is_best: false
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 0.5536
    std: 0.2494
    paper_value: 0.5536
    paper_std: 0.2494
    metric: F1
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
    global_rank: 4
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
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5536
    sort_std: 0.2494
    is_best: false
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.5481
    std: 0.212
    paper_value: 0.5481
    paper_std: 0.212
    metric: F1
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
    global_rank: 5
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
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5481
    sort_std: 0.212
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: COCO-SP
  rows:
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 0.4483
    std: 0.0071
    paper_value: 0.4483
    paper_std: 0.0071
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to coco-sp (score=90)'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 1
    true_value: 0.4483
    true_std: 0.0071
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
    sort_value: 0.4483
    sort_std: 0.0071
    is_best: true
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.4387
    std: 0.0054
    paper_value: 0.4387
    paper_std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to coco-sp (score=90)'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 2
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
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4387
    sort_std: 0.0054
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.4382
    std: 0.0101
    paper_value: 0.4382
    paper_std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to coco-sp (score=90)'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 3
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
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4382
    sort_std: 0.0101
    is_best: true
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 0.4312
    std: 0.0085
    paper_value: 0.4312
    paper_std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to coco-sp (score=90)'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 4
    true_value: 0.4312
    true_std: 0.0085
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
    sort_value: 0.4312
    sort_std: 0.0085
    is_best: false
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 0.3991
    std: 0.0107
    paper_value: 0.3991
    paper_std: 0.0107
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 16.0
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to coco-sp (score=90)'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 5
    true_value: 0.3991
    true_std: 0.0107
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
    sort_value: 0.3991
    sort_std: 0.0107
    is_best: false
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.3596
    std: 0.0022
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.3596
    sort_std: 0.0022
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3455
    std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.3455
    sort_std: 0.0009
    is_best: false
  - model: GTs
    model_key: gts
    model_plain: GTs
    value: 0.3412
    std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_display: May 2022
    date_iso: 2022-05
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.3412
    sort_std: 0.0044
    is_best: false
  metric: F1
  higher_is_better: true
- &id002
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
    params_millions: 16.0
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
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
    variant_inference_reason: 'dataset: exact match'
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
    variant_inference_reason: 'dataset: exact match'
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
    variant_inference_reason: 'dataset: exact match'
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
    uses_external_data: false
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
    variant_inference_reason: 'dataset: exact match'
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
    value: 3.44
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
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 3.44
    sort_std: null
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
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
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 4.27
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
  dataset: MST
  rows:
  - model: GDT + RRWP
    model_key: gdt + rrwp
    model_plain: GDT + RRWP
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
    variant_inference_reason: 'dataset: exact match'
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
  - model: GDT + NoPE
    model_key: gdt + nope
    model_plain: GDT + NoPE
    value: 0.9329
    std: 0.0088
    paper_value: 0.9329
    paper_std: 0.0088
    metric: F1
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
    global_rank: 2
    true_value: 0.9329
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
    sort_value: 0.9329
    sort_std: 0.0088
    is_best: false
  - model: GDT + RWSE
    model_key: gdt + rwse
    model_plain: GDT + RWSE
    value: 0.9326
    std: 0.0045
    paper_value: 0.9326
    paper_std: 0.0045
    metric: F1
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
    global_rank: 3
    true_value: 0.9326
    true_std: 0.0045
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
    sort_value: 0.9326
    sort_std: 0.0045
    is_best: false
  - model: GDT + SPE
    model_key: gdt + spe
    model_plain: GDT + SPE
    value: 0.9252
    std: 0.0012
    paper_value: 0.9252
    paper_std: 0.0012
    metric: F1
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
    global_rank: 4
    true_value: 0.9252
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
    sort_value: 0.9252
    sort_std: 0.0012
    is_best: false
  - model: GDT + LPE
    model_key: gdt + lpe
    model_plain: GDT + LPE
    value: 0.9108
    std: 0.0095
    paper_value: 0.9108
    paper_std: 0.0095
    metric: F1
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
    global_rank: 5
    true_value: 0.9108
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
    sort_value: 0.9108
    sort_std: 0.0095
    is_best: false
  metric: F1
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
- benchmark: GraphBench
  datasets:
  - *id002
  - *id003
  - *id004
main_figure: /figures/2511.08028/main_figure.png
---

