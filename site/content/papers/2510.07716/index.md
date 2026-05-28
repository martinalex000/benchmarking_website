---
title: Computationally-efficient Graph Modeling with Refined Graph Random Features
arxiv_id: '2510.07716'
source_url: ''
authors: []
published_date: ''
published_date_iso: ''
abstract: We propose refined GRFs (GRFs++), a new class of Graph Random Features (GRFs)
  for efficient and accurate computations involving kernels defined on the nodes of
  a graph. GRFs++ resolve some of the long-standing limitations of regular GRFs, including
  difficulty modeling relationships between more distant nodes. They reduce dependence
  on sampling long graph random walks via a novel walk-stitching technique, concatenating
  several shorter walks without breaking unbiasedness. By applying these techniques,
  GRFs++ inherit the approximation quality provided by longer walks but with greater
  efficiency, trading sequential, inefficient sampling of a long walk for parallel
  computation of short walks and matrix-matrix multiplication. Furthermore, GRFs++
  extend the simplistic GRFs walk termination mechanism (Bernoulli schemes with fixed
  halting probabilities) to a broader class of strategies, applying general distributions
  on the walks' lengths. This improves the approximation accuracy of graph kernels,
  without incurring extra computational cost. We provide empirical evaluations to
  showcase all our claims and complement our results with theoretical analysis.
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
main_figure: /figures/2510.07716/main_figure.png
---

