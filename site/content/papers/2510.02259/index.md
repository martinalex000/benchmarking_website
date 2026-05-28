---
title: Transformers Discover Molecular Structure Without Graph Priors
arxiv_id: '2510.02259'
source_url: ''
authors: []
published_date: ''
published_date_iso: ''
abstract: 'Graph Neural Networks (GNNs) are the dominant architecture for molecular
  machine learning, particularly for molecular property prediction and machine learning
  interatomic potentials (MLIPs). GNNs perform message passing on predefined graphs
  often induced by a fixed radius cutoff or $k$-nearest neighbor scheme. While this
  design aligns with the locality present in many molecular tasks, a hard-coded graph
  can limit expressivity due to the fixed receptive field and slows down inference
  with sparse graph operations. In this work, we investigate whether pure, unmodified
  Transformers trained directly on Cartesian coordinateswithout predefined graphs
  or physical priorscan approximate molecular energies and forces. As a starting point
  for our analysis, we demonstrate how to train a Transformer to competitive energy
  and force mean absolute errors under a matched training compute budget, relative
  to a state-of-the-art equivariant GNN on the OMol25 dataset. We discover that the
  Transformer learns physically consistent patternssuch as attention weights that
  decay inversely with interatomic distanceand flexibly adapts them across different
  molecular environments due to the absence of hard-coded biases. The use of a standard
  Transformer also unlocks predictable improvements with respect to scaling training
  resources, consistent with empirical scaling laws observed in other domains. Our
  results demonstrate that many favorable properties of GNNs can emerge adaptively
  in Transformers, challenging the necessity of hard-coded graph inductive biases
  and pointing toward standardized, scalable architectures for molecular modeling.
  Project Page with animations and an interactive demo: https://tkreiman.github.io/projects/graph-free-transformers/'
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
main_figure: /figures/2510.02259/main_figure.png
---

