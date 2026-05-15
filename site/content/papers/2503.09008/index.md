---
title: 'Towards Quantifying Long-Range Interactions in Graph Machine Learning: A Large
  Graph Dataset and a Measurement 0.8em'
arxiv_id: '2503.09008'
authors: []
published_date: Mar 2025
abstract: Long-range dependencies are critical for effective graph representation
  learning, yet most existing datasets focus on small graphs tailored to inductive
  tasks, offering limited insight into long-range interactions. Current evaluations
  primarily compare models employing global attention (e.g., graph transformers) with
  those using local neighborhood aggregation (e.g., message-passing neural networks)
  without a direct measurement of long-range dependency. In this work, we introduce
  City-Networks, a novel large-scale transductive learning dataset derived from real-world
  city road networks. This dataset features graphs with over $10^5$ nodes and significantly
  larger diameters than those in existing benchmarks, naturally embodying long-range
  information. We annotate the graphs based on local node eccentricities, ensuring
  that the classification task inherently requires information from distant nodes.
  Furthermore, we propose a generic measurement based on the Jacobians of neighbors
  from distant hops, offering a principled quantification of long-range dependencies.
  Finally, we provide theoretical justifications for both our dataset design and the
  proposed measurement—particularly by focusing on over-smoothing and influence score
  dilution, which establishes a robust foundation for further exploration of long-range
  interactions in graph neural networks. Our https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.CityNetwork.html#torch_geometric.datasets.CityNetwork
  dataset and https://pytorch-geometric.readthedocs.io/en/latest/modules/utils.html#torch_geometric.utils.total_influence
  measurement are available on https://pytorch-geometric.readthedocs.io/en/latest/index.html
  PyTorch Geometric, and the code for reproducing the experimental results can be
  found at https://github.com/LeonResearch/City-Networks github.com/LeonResearch/City-Networks.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models: []
mrr: null
results:
- &id001
  dataset: D&D
  rows:
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
    is_best: true
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
  - model: GraphSAGE
    value: 0.554
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 62
    is_best: false
  - model: ChebNet
    value: 0.547
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GAT
    value: 0.52
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: GCN
    value: 0.501
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: Exphormer
    value: 0.495
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 64
    is_best: false
  - model: SGFormer
    value: 0.483
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 45
    is_best: false
  - model: GCNII
    value: 0.482
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: this paper
    global_rank: 65
    is_best: false
  - model: + DropEdge
    value: 0.45
    std: 0.003
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
  - model: MLP
    value: 0.279
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 47
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
main_figure: /figures/2503.09008/main_figure.png
---

