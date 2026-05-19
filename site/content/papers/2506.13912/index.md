---
title: Density-aware Walks for Coordinated Campaign Detection
arxiv_id: '2506.13912'
authors: []
published_date: Jun 2025
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
  in the dataset, with nearly a 12\% and 5\% improvement in accuracy for binary and
  multiclass classification, respectively. Our findings demonstrate that incorporating
  density-aware structural encoding with MPNNs provides a robust framework for identifying
  coordinated inauthentic behavior on social media networks such as Twitter.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
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
results:
- &id001
  dataset: LEN
  rows:
  - model: SAGE (RWW, Degree, 0.5)
    value: 0.852
    std: 0.01
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
  - model: SAGE (RWW, Truss, 0.5)
    value: 0.813
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GAT (RWW, Core, mid)
    value: 0.808
    std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GCN (NF+RWW, Truss, 0.5)
    value: 0.803
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GCN (RWW, Truss, median)
    value: 0.8
    std: 0.019
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
  - model: GAT (RWW, Degree, median)
    value: 0.792
    std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GAT (NF+RWW, Truss, median)
    value: 0.792
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GIN (NF+RWW, Core, mid)
    value: 0.792
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: SAGE (NF+RWW, Core, 0.5)
    value: 0.79
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GCN (RWW, Core, 0.5)
    value: 0.787
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GAT (NF+RWW, Core, 0.5)
    value: 0.785
    std: 0.01
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
  - model: GCN (RWW, Degree, mid)
    value: 0.784
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GIN (NF+RWW, Truss, mid)
    value: 0.782
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: SAGE (RWW, Core, mid)
    value: 0.774
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GIN (RWW, Truss, 0.5)
    value: 0.771
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GCN (NF+RWW, Core, median)
    value: 0.766
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: SAGE (NF+RWW, Degree, median)
    value: 0.758
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: GIN (RWW, Degree, 0.5)
    value: 0.751
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: GAT (NF)
    value: 0.735
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: SAGE (NF)
    value: 0.729
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: GCN (NF)
    value: 0.702
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: GIN (NF)
    value: 0.633
    std: 0.065
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
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id001
main_figure: /figures/2506.13912/main_figure.png
---

