---
title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
arxiv_id: '2402.08678'
authors: []
published_date: '2024-02-13'
abstract: 'Graph Neural Networks (GNNs) have shown promising potential in graph representation
  learning. The majority of GNNs define a local message-passing mechanism, propagating
  information over the graph by stacking multiple layers. These methods, however,
  are known to suffer from two major limitations: over-squashing and poor capturing
  of long-range dependencies. Recently, Graph Transformers (GTs) emerged as a powerful
  alternative to Message-Passing Neural Networks (MPNNs). GTs, however, have quadratic
  computational cost, lack inductive biases on graph structures, and rely on complex
  Positional/Structural Encodings (SE/PE). In this paper, we show that while Transformers,
  complex message-passing, and SE/PE are sufficient for good performance in practice,
  neither is necessary. Motivated by the recent success of State Space Models (SSMs),
  such as Mamba, we present Graph Mamba Networks (GMNs), a general framework for a
  new class of GNNs based on selective SSMs. We discuss and categorize the new challenges
  when adapting SSMs to graph-structured data, and present four required and one optional
  steps to design GMNs, where we choose (1) Neighborhood Tokenization, (2) Token Ordering,
  (3) Architecture of Bidirectional Selective SSM Encoder, (4) Local Encoding, and
  dispensable (5) PE and SE. We further provide theoretical justification for the
  power of GMNs. Experiments demonstrate that despite much less computational cost,
  GMNs attain an outstanding performance in long-range, small-scale, large-scale,
  and heterophilic benchmark datasets.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GMN
mrr: 0.0683
results:
- &id002
  dataset: Amazon-ratings
  rows:
  - model: GENs
    value: 0.5592
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GAT
    value: 0.5554
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GraphSAGE
    value: 0.554
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GMN
    value: 0.5407
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: Exphormer
    value: 0.5351
    std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: GMN w/o MPNN
    value: 0.5312
    std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: GPS
    value: 0.531
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: GPM w/o PE
    value: 0.5308
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 30
    is_best: false
  - model: GMN PPR ordering
    value: 0.5299
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 31
    is_best: false
  - model: Nagphormer
    value: 0.5126
    std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: GMN w/o bidirectional Mamba
    value: 0.5016
    std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: GCN
    value: 0.487
    std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: GPS + Mamba
    value: 0.4513
    std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: GOAT
    value: 0.4461
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: GatedGCN
    value: 0.43
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 61
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: CIFAR10
  rows:
  - model: GRASS
    value: 0.8375
    std: 0.00141
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
  - model: NeuralWalker
    value: 0.80027
    std: 0.00185
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
    global_rank: 2
    is_best: false
  - model: Ours
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GMN
    value: 0.7576
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: GRED
    value: 0.7537
    std: 0.621
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Ding et al.
    global_rank: 11
    is_best: true
  - model: Exphormer
    value: 0.7469
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 31
    is_best: false
  - model: GPS + Mamba
    value: 0.7341
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: GPS
    value: 0.7226
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 51
    is_best: false
  - model: S4G
    value: 0.7065
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: De Bortoli et al.
    global_rank: 75
    is_best: false
  - model: GPS + BigBird
    value: 0.7048
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 77
    is_best: false
  - model: CRaWl
    value: 0.6901
    std: 0.0259
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 92
    is_best: false
  - model: GatedGCN
    value: 0.6731
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: GCN
    value: 0.5571
    std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 87
    is_best: false
  - model: GIN
    value: 0.5526
    std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 89
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GMN
    value: 0.3974
    std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GPS + Mamba
    value: 0.3895
    std: 0.0125
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GPS
    value: 0.3774
    std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: Nagphormer
    value: 0.3458
    std: 0.007
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 28
    is_best: false
  - model: Exphormer
    value: 0.343
    std: 0.0108
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: CRaWl
    value: 0.3219
    std: 0.00106
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: GatedGCN
    value: 0.2641
    std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: GPS + BigBird
    value: 0.2622
    std: 0.0008
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: SAN+LapPE
    value: 0.2592
    std: 0.0158
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: this paper
    global_rank: 51
    is_best: false
  - model: GIN
    value: 0.1339
    std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 56
    is_best: false
  - model: GCN
    value: 0.0841
    std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 43
    is_best: false
  metric: F1
  higher_is_better: true
- &id008
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
  - model: Exphormer
    value: 0.9855
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GMN
    value: 0.9839
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: GRED
    value: 0.9822
    std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Ding et al.
    global_rank: 21
    is_best: true
  - model: GPS + Mamba
    value: 0.9821
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: GPS + BigBird
    value: 0.9817
    std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GPS
    value: 0.9811
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 50
    is_best: false
  - model: CRaWl
    value: 0.9794
    std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 69
    is_best: true
  - model: GatedGCN
    value: 0.9734
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GIN
    value: 0.9649
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 28
    is_best: false
  - model: S4G
    value: 0.9637
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: De Bortoli et al.
    global_rank: 83
    is_best: false
  - model: GCN
    value: 0.9071
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 22
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: MalNet-Tiny
  rows:
  - model: ESA
    value: 0.948
    std: 0.00424
    metric: Accuracy
    higher_is_better: true
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
  - model: GSM++ (MoT)
    value: 0.9437
    std: 0.0058
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
    global_rank: 3
    is_best: true
  - model: GSM++ (BFS)
    value: 0.9417
    std: 0.002
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
    global_rank: 4
    is_best: false
  - model: GMN
    value: 0.9415
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: Exphormer
    value: 0.9402
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GPS + Mamba
    value: 0.9311
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GPS
    value: 0.9298
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: GPS + BigBird
    value: 0.9234
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: GatedGCN
    value: 0.9223
    std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GIN
    value: 0.8898
    std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GCN
    value: 0.81
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Minesweeper
  rows:
  - model: CSNN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: BuNN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Tango\textsubscript{GPS}
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GMN
    value: 0.9101
    std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: Exphormer
    value: 0.9074
    std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: GPS
    value: 0.9063
    std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 68
    is_best: false
  - model: GPM w/o PE
    value: 0.9011
    std: 0.0025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: GPS + Mamba
    value: 0.8993
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: GMN PPR ordering
    value: 0.8991
    std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 75
    is_best: false
  - model: GMN w/o MPNN
    value: 0.8983
    std: 0.0031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: GCN
    value: 0.8975
    std: 0.0052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GatedGCN
    value: 0.8754
    std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 69
    is_best: false
  - model: GMN w/o bidirectional Mamba
    value: 0.8597
    std: 0.0028
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 86
    is_best: false
  - model: Nagphormer
    value: 0.8419
    std: 0.0066
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: GOAT
    value: 0.8109
    std: 0.0102
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 88
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id009
  dataset: PATTERN
  rows:
  - model: GRIT (our run)
    value: 0.90405
    std: 0.00232
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with - Quantum Computed Encodings
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GRIT 2-QiQRW
    value: 0.90165
    std: 0.00446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with - Quantum Computed Encodings
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: PPGT
    value: 0.89752
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GMN
    value: 0.8714
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: S4G
    value: 0.8687
    std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: s4g
    global_rank: 33
    is_best: false
  - model: GRED
    value: 0.8676
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ding2023recurrent
    global_rank: 45
    is_best: false
  - model: Exphormer
    value: 0.867
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GPS
    value: 0.8664
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: GPS + Mamba
    value: 0.866
    std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: Nagphormer
    value: 0.8644
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: GPS + BigBird
    value: 0.86
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 71
    is_best: false
  - model: GatedGCN
    value: 0.8557
    std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: GIN
    value: 0.8539
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 38
    is_best: false
  - model: GCN
    value: 0.7189
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 24
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: S4G
    value: 0.7293
    std: 0.0004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: s4g
    global_rank: 6
    is_best: false
  - model: GMN
    value: 0.7071
    std: 0.0083
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: GRED
    value: 0.7041
    std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ding2023recurrent
    global_rank: 29
    is_best: false
  - model: CRaWl
    value: 0.6963
    std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 35
    is_best: false
  - model: Graph ViT
    value: 0.6855
    std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 59
    is_best: false
  - model: GPS + Mamba
    value: 0.6624
    std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 139
    is_best: false
  - model: GPS
    value: 0.6575
    std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 151
    is_best: false
  - model: Exphormer
    value: 0.6527
    std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 174
    is_best: false
  - model: SAN+LapPE
    value: 0.6384
    std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: this paper
    global_rank: 204
    is_best: false
  - model: GCN
    value: 0.593
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GatedGCN
    value: 0.5864
    std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: GPS + BigBird
    value: 0.5854
    std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 182
    is_best: false
  - model: GIN
    value: 0.5498
    std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 39
    is_best: false
  metric: AP
  higher_is_better: true
- &id005
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
  - model: IPR-MPNN
    value: 0.2422
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: Graph ViT
    value: 0.2468
    std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: GMN
    value: 0.2473
    std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 73
    is_best: false
  - model: Exphormer
    value: 0.2481
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 93
    is_best: false
  - model: S4G
    value: 0.2485
    std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: s4g
    global_rank: 100
    is_best: false
  - model: GRED
    value: 0.2503
    std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ding2023recurrent
    global_rank: 38
    is_best: false
  - model: CRaWl
    value: 0.2506
    std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 130
    is_best: false
  - model: GPS
    value: 0.251
    std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 120
    is_best: false
  - model: GPS + Mamba
    value: 0.2518
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 138
    is_best: false
  - model: SAN+LapPE
    value: 0.2683
    std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: this paper
    global_rank: 214
    is_best: false
  - model: GPS + BigBird
    value: 0.2842
    std: 0.013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 177
    is_best: false
  - model: GatedGCN
    value: 0.342
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GCN
    value: 0.3496
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GIN
    value: 0.3547
    std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
  dataset: Tolokers
  rows:
  - model: GRAMA$_{GCN}$
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GRAMA
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Polynormer
    value: 0.8591
    std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GMN
    value: 0.8452
    std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: Exphormer
    value: 0.8377
    std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: GPS
    value: 0.8371
    std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: GPS + Mamba
    value: 0.837
    std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GCN
    value: 0.8364
    std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GOAT
    value: 0.8311
    std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: Nagphormer
    value: 0.7832
    std: 0.0095
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: GatedGCN
    value: 0.7731
    std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 53
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: LRGB
  datasets:
  - *id004
  - *id005
  - *id006
- benchmark: GNNBenchmark
  datasets:
  - *id007
  - *id008
  - *id009
- benchmark: Other Graph Benchmarks
  datasets:
  - *id010
single_proposed_model: GMN
main_figure: /figures/2402.08678/main_figure.png
---

