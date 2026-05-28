---
title: Random Search Neural Networks for Efficient and Expressive Graph Learning
arxiv_id: '2510.22520'
source_url: ''
authors: []
published_date: ''
published_date_iso: ''
abstract: Random walk neural networks (RWNNs) have emerged as a promising approach
  for graph representation learning, leveraging recent advances in sequence models
  to process random walks. However, under realistic sampling constraints, RWNNs often
  fail to capture global structure even in small graphs due to incomplete node and
  edge coverage, limiting their expressivity. To address this, we propose random search
  neural networks (RSNNs), which operate on random searches, each of which guarantees
  full node coverage. Theoretically, we demonstrate that in sparse graphs, only $O(|V|)$
  searches are needed to achieve full edge coverage, substantially reducing sampling
  complexity compared to the $O(|V|)$ walks required by RWNNs (assuming walk lengths
  scale with graph size). Furthermore, when paired with universal sequence models,
  RSNNs are universal approximators. We lastly show RSNNs are probabilistically invariant
  to graph isomorphisms, ensuring their expectation is an isomorphism-invariant graph
  function. Empirically, RSNNs consistently outperform RWNNs on molecular and protein
  benchmarks, achieving comparable or superior performance with up to 16$ $ fewer
  sampled sequences. Our work bridges theoretical and practical advances in random
  walk based approaches, offering an efficient and expressive framework for learning
  on sparse graphs.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories: []
task_categories: []
experiment_scopes: []
results: []
results_grouped: []
main_figure: /figures/2510.22520/main_figure.png
---

