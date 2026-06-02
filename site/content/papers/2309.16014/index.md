---
title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
arxiv_id: '2309.16014'
source_url: ''
authors: []
published_date: Sep 27, 2023
published_date_iso: '2023-09-27'
published_venue: ''
abstract: Joint-Embedding Predictive Architectures (JEPAs) have recently emerged as
  a novel and powerful technique for self-supervised representation learning. They
  aim to learn an energy-based model by predicting the latent representation of a
  target signal $y$ from the latent representation of a context signal $x$. JEPAs
  bypass the need for negative and positive samples, traditionally required by contrastive
  learning while avoiding the overfitting issues associated with generative pretraining.
  In this paper, we show that graph-level representations can be effectively modeled
  using this paradigm by proposing a Graph Joint-Embedding Predictive Architecture
  (Graph-JEPA). In particular, we employ masked modeling and focus on predicting the
  latent representations of masked subgraphs starting from the latent representation
  of a context subgraph. To endow the representations with the implicit hierarchy
  that is often present in graph-level concepts, we devise an alternative prediction
  objective that consists of predicting the coordinates of the encoded subgraphs on
  the unit hyperbola in the 2D plane. Through multiple experimental evaluations, we
  show that Graph-JEPA can learn highly semantic and expressive representations, as
  shown by the downstream performance in graph classification, regression, and distinguishing
  non-isomorphic graphs. The code is available at.
codebase_url: https://github.com/geriskenderi/graph-jepa
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
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
---

