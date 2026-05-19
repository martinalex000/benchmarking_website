---
title: Generalizable Insights for Graph Transformers in Theory and Practice
arxiv_id: '2511.08028'
authors: []
published_date: Nov 2025
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
proposed_models:
- GT (no PE)
- GDT (LPE)
- GDT (SPE)
- GDT (RWSE)
- GDT (RRWP)
- RRWP
mrr: 0.1429
results:
- &id008
  dataset: Bridges
  rows:
  - model: GDT (RRWP)
    value: 0.9921
    std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GDT (RRWP)
    value: 0.9921
    std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GIN
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
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GT
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
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GDT (LPE)
    value: 0.9176000000000001
    std: 0.0766
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GDT (LPE)
    value: 0.9176000000000001
    std: 0.0766
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GDT (RWSE)
    value: 0.8734000000000001
    std: 0.0397
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GDT (RWSE)
    value: 0.8734000000000001
    std: 0.0397
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GT (no PE)
    value: 0.5536
    std: 0.2494
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GT (no PE)
    value: 0.5536
    std: 0.2494
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GDT (SPE)
    value: 0.5481
    std: 0.212
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GDT (SPE)
    value: 0.5481
    std: 0.212
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  metric: F1
  higher_is_better: true
- &id002
  dataset: COCO-SP
  rows:
  - model: FloydNet
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GRASS
    value: 0.4752
    std: 0.0032
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: GDT (LPE)
    value: 0.4483
    std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: NeuralWalker
    value: 0.4398
    std: 0.0033
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: GDT (SPE)
    value: 0.4387
    std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GDT (RWSE)
    value: 0.4382
    std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GT (no PE)
    value: 0.43119999999999997
    std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GDT (RRWP)
    value: 0.39909999999999995
    std: 0.010700000000000001
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: Code
  rows:
  - model: CodeT5-small + GFSA
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: CodeT5-base + GFSA
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: CodeT5-small
    value: 0.9436
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 60.0
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: LPE
    value: 0.1948
    std: 0.0021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: RRWP
    value: 0.1942
    std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: RWSE
    value: 0.19390000000000002
    std: 0.004699999999999999
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: SPE
    value: 0.1935
    std: 0.0021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: NoPE
    value: 0.19269999999999998
    std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 12
    is_best: false
  metric: F1
  higher_is_better: true
- &id003
  dataset: D&D
  rows:
  - model: GDT (RRWP)
    value: 0.9921
    std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: MPNN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
  - model: HAC (BFS)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GDT (LPE)
    value: 0.9176000000000001
    std: 0.0766
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: GDT (RWSE)
    value: 0.8734000000000001
    std: 0.0397
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GT (no PE)
    value: 0.5536
    std: 0.2494
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GDT (SPE)
    value: 0.5481
    std: 0.212
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Flow
  rows:
  - model: RRWP
    value: 1.45
    std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: RRWP
    value: 1.45
    std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: RWSE
    value: 1.49
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: RWSE
    value: 1.49
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: NoPE
    value: 1.73
    std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: NoPE
    value: 1.73
    std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: LPE
    value: 1.75
    std: 0.12
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: LPE
    value: 1.75
    std: 0.12
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: agg + I
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: SPE
    value: 1.98
    std: 0.14
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: SPE
    value: 1.98
    std: 0.14
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GIN
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
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    is_best: false
  - model: Graph transformer
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 8
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: MNIST
  rows:
  - model: GRASS
    value: 0.98932
    std: 0.00076
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GSM++ (MoT)
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: NeuralWalker
    value: 0.9876
    std: 0.00079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GDT (RRWP)
    value: 0.9604
    std: 0.0091
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GT (no PE)
    value: 0.9329000000000001
    std: 0.0088
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GDT (RWSE)
    value: 0.9326000000000001
    std: 0.0045000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GDT (SPE)
    value: 0.9251999999999999
    std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GDT (LPE)
    value: 0.9107999999999999
    std: 0.0095
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: MST
  rows:
  - model: GDT (RRWP)
    value: 0.9604
    std: 0.0091
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GDT (RRWP)
    value: 0.9604
    std: 0.0091
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GT (no PE)
    value: 0.9329000000000001
    std: 0.0088
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GT (no PE)
    value: 0.9329000000000001
    std: 0.0088
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GDT (RWSE)
    value: 0.9326000000000001
    std: 0.0045000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GDT (RWSE)
    value: 0.9326000000000001
    std: 0.0045000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GDT (SPE)
    value: 0.9251999999999999
    std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GDT (SPE)
    value: 0.9251999999999999
    std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GDT (LPE)
    value: 0.9107999999999999
    std: 0.0095
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GDT (LPE)
    value: 0.9107999999999999
    std: 0.0095
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GT
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
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    is_best: false
  - model: GIN
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
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: PCQM-Contact
  rows:
  - model: SOTA (Range)
    value: 0.0809
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: N/A (Text)
    source_ref: chen2023gpropagation, mueller2024et, ma+2023+GRIT, rampasek+2022+graphgps
    global_rank: null
    is_best: true
  - model: GatedGCN (L=2)
    value: 0.1927
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
  - model: GCN (L=2)
    value: 0.1944
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: GINE (L=2)
    value: 0.1949
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GDT (RRWP)
    value: 90.4
    std: 0.3
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GDT (LPE)
    value: 92.7
    std: 0.9
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GDT (RWSE)
    value: 92.9
    std: 0.6
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GT (no PE)
    value: 93.6
    std: 0.5
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GDT (SPE)
    value: 94.1
    std: 0.6
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
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

