---
title: Learning Efficient Positional Encodings with Graph Neural Networks
arxiv_id: '2502.01122'
authors: []
published_date: Feb 2025
abstract: 'Positional encodings (PEs) are essential for effective graph representation
  learning because they provide position awareness in inherently position-agnostic
  transformer architectures and increase the expressive capacity of Graph Neural Networks
  (GNNs). However, designing powerful and efficient PEs for graphs poses significant
  challenges due to the absence of canonical node ordering and the scale of the graph.
  In this work, we identify four key properties that graph PEs should satisfy: stability,
  expressive power, scalability, and genericness. We find that existing eigenvector-based
  PE methods often fall short of jointly satisfying these criteria. To address this
  gap, we introduce , a novel framework of learnable PEs for graphs. Our primary insight
  is that message-passing GNNs function as nonlinear mappings of eigenvectors, enabling
  the design of GNN architectures for generating powerful and efficient PEs. A crucial
  challenge lies in initializing node attributes in a manner that is both expressive
  and permutation equivariant. We tackle this by initializing GNNs with random node
  inputs or standard basis vectors, thereby unlocking the expressive power of message-passing
  operations, while employing statistical pooling functions to maintain permutation
  equivariance. Our analysis demonstrates that ~approximates equivariant functions
  of eigenvectors with linear complexity, while rigorously establishing its stability
  and high expressive power. Experimental evaluations show that ~outperforms lightweight
  versions of eigenvector-based PEs and achieves comparable performance to full eigenvector-based
  PEs, but with one or two orders of magnitude lower complexity. Our code is available
  at~https://github.com/ehejin/Pearl-PE.'
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- SignNet
- R-method
- B-method
mrr: 0.0103
results:
- &id005
  dataset: CSL
  rows:
  - model: R-method
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: ''
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: B-method
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: Transformer+LapPE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: Transformer+RWSE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: A_2+LapPE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: true
  - model: Message-passing GNNs with WL-related PEs
    value: 0.1
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: ''
    source_ref: this paper
    global_rank: 24
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    metric_values:
    - 0.989
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HAC (BFS)
    metric_values:
    - 0.981
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
    metric_values:
    - 0.976
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: SignNet
    metric_values:
    - 0.1086
    - 0.9243
    metric_stds:
    - null
    - 0.0027
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: SignNet-8S
    metric_values:
    - 0.1086
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: NoPE
    metric_values:
    - 0.1073
    - 0.9289
    metric_stds:
    - null
    - 0.0014
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: SPE
    metric_values:
    - null
    - 0.9294
    metric_stds:
    - null
    - 0.0015
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: R-method
    metric_values:
    - null
    - 0.9292
    metric_stds:
    - null
    - 0.0012
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: BasisNet
    metric_values:
    - null
    - 0.8942
    metric_stds:
    - null
    - 0.0118
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: SPE-8S
    metric_values:
    - null
    - 0.9262
    metric_stds:
    - null
    - 0.001
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: B-method
    metric_values:
    - null
    - 0.9081
    metric_stds:
    - null
    - 0.0079
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: PEG
    metric_values:
    - null
    - 0.9257
    metric_stds:
    - null
    - 0.0022
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  metrics:
  - MAP
  - ROC-AUC
  primary_metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Peptides-struct
  rows:
  - model: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Tango_GPS
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: Graph ViT
    value: 0.245
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: he2023generalization
    global_rank: 26
    is_best: true
  - model: R-method
    value: 0.247
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 65
    is_best: false
  - model: B-method
    value: 0.248
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 90
    is_best: false
  - model: SUN
    value: 0.25
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: frasca_2022
    global_rank: 115
    is_best: false
  - model: GPS
    value: 0.252
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampavsek2022recipe
    global_rank: 119
    is_best: false
  - model: SAN+RWSE
    value: 0.255
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 1
    source_ref: kruezer_2021
    global_rank: 164
    is_best: false
  - model: SAN+LapPE
    value: 0.268
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: kruezer_2021
    global_rank: 213
    is_best: false
  - model: GNN (a)
    value: 0.274
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2022from
    global_rank: 220
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: R-method
    value: 0.606
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GIN + rand id
    value: 0.57
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GIN
    value: 0.569
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GSN with cliques
    value: 0.562
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SignNet-8S
    value: 0.552
    std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN
    value: 0.2
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: ESA
    value: 0.010894100678479495
    std: 0.00022839903839981288
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ESA (PE)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: PST
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: B-method
    value: 0.0644
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 66
    is_best: false
  - model: SPE
    value: 0.0693
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 96
    is_best: false
  - model: R-method
    value: 0.0699
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 97
    is_best: false
  - model: SPE-8S
    value: 0.0736
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 110
    is_best: false
  - model: SignNet
    value: 0.0853
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: limsign
    global_rank: 14
    is_best: false
  - model: SignNet-8S
    value: 0.1034
    std: 0.0056
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: limsign
    global_rank: 164
    is_best: false
  - model: GSN with cycles
    value: 0.115
    std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 175
    is_best: false
  - model: BasisNet-8S
    value: 0.1554
    std: 0.0048
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 213
    is_best: false
  - model: BasisNet
    value: 0.1555
    std: 0.0124
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 214
    is_best: false
  - model: NoPE
    value: 0.1772
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 220
    is_best: false
  - model: GIN
    value: 0.209
    std: 0.018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: GIN + rand id
    value: 0.279
    std: 0.023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 241
    is_best: false
  - model: GCN
    value: 0.469
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    global_rank: 115
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
- benchmark: GNNBenchmark
  datasets:
  - *id005
main_figure: /figures/2502.01122/main_figure.png
---

