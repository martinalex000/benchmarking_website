---
title: Missing Datasets
type: dev
description: Datasets detected in extraction but not yet mapped into DB
---

## Datasets Still Missing From The DB

This page distinguishes between entries that are truly unresolved and stale pending rows that already resolve against the current benchmark database.

Source: pending_datasets table in benchmarks.db

<<<<<<< Updated upstream
**Tracked entries in DB:** 98
**Still unresolved:** 98
=======
**Tracked entries in DB:** 113
**Still unresolved:** 113
>>>>>>> Stashed changes
**Already covered now:** 0

### Still unresolved

| Status | Dataset | Paper | Metrics Seen | Suggested Benchmark | PyG |
|--------|---------|-------|--------------|---------------------|-----|
| pending | AIFB | 1703.06103 | Accuracy | OGB | yes |
| pending | Alchemy | 2007.08663 | MAE, logMAE | OGB | yes |
| pending | alchemy | 2110.00577 | MAE | OGB-LSC | yes |
| pending | Alchemy | 2206.11168 | MAE |  | yes |
| pending | Alchemy | 2310.02156 | MAE | OGB | yes |
| pending | Alchemy | 2410.09737 | MAE | OGB | yes |
| pending | Alchemy (10k) | 2202.13013 | MAE | OGB-LSC | yes |
| pending | Aminer | 2403.16030 | Accuracy |  |  |
| pending | Associative recall 30k | 2405.19121 | Accuracy | GNNBench |  |
| pending | Beijing | 2306.08277 | MAE |  |  |
| pending | BGP | 2106.06586 | Accuracy |  |  |
| pending | BGS | 1703.06103 | Accuracy |  |  |
| pending | Blog | 2501.18739 | Accuracy |  |  |
| pending | BlogCatalog | 1403.6652 | Micro-F1 |  | yes |
| pending | BlogCatalog | 2505.23345 | Accuracy |  | yes |
| pending | Brazil | 2106.06586 | Accuracy |  |  |
| pending | Brazil-Airports | 2301.09505 | Accuracy |  |  |
| pending | C.ele | 1802.09691 | AUC |  | yes |
| pending | CEXP | 2110.02910 | Accuracy |  |  |
| pending | Cuneiform | 2605.04834 | Accuracy |  |  |
| pending | DIEL | 1603.08861 | Recall@k | DIEL |  |
| pending | E.coli | 1802.09691 | AUC |  | yes |
| pending | Email | 1906.04817 | ROC-AUC |  | yes |
| pending | Europe | 2106.06586 | Accuracy |  |  |
| pending | Europe-Airports | 2301.09505 | Accuracy |  |  |
| pending | EXP | 2110.02910 | Accuracy | TUDataset |  |
| pending | EXP | 2110.13197 | Accuracy |  |  |
| pending | Exp | 2206.11168 | Accuracy |  |  |
| pending | EXP | 2309.16014 | Accuracy |  |  |
| pending | Facebook | 2505.23345 | Accuracy |  |  |
| pending | Facebook | 2506.22727 | Accuracy |  |  |
| pending | Flickr | 2004.11198 | F1 | OGB | yes |
| pending | flickr | 2406.09675 | Accuracy | OGBG | yes |
| pending | Flickr | 2501.18739 | Accuracy |  | yes |
| pending | Flickr-S | 2501.18739 | Accuracy |  |  |
| pending | FRANKENSTEIN | 1904.08082 | Accuracy | FRANKENSTEIN |  |
| pending | FRANKENSTEIN | 2305.15747 | Accuracy | FRANKENSTEIN Benchmark |  |
| pending | GCB | 2405.14094 | Accuracy | GCB |  |
| pending | genius | 2205.07308 | Accuracy |  |  |
| pending | Genius | 2406.01249 | Accuracy |  |  |
| pending | genius | 2406.09675 | ROC AUC |  |  |
| pending | github_star | 2007.08663 | Accuracy |  |  |
| pending | GLUE | 2312.04234 | Avg | GLUE |  |
| pending | GRAPH8c | 2306.02866 | GRAPH8c | GraphBench |  |
| pending | Grid | 1906.04817 | ROC-AUC |  |  |
| pending | GRN | 2410.14109 | MAE |  |  |
| pending | Harbin | 2306.08277 | MAE |  |  |
| pending | HCP-Age | 2407.18480 | Accuracy |  |  |
| pending | HCP-Task | 2407.18480 | Accuracy |  |  |
| pending | Image | 2310.02980 | Accuracy |  |  |
| pending | ImageNet-1k | 2312.04234 | Accuracy |  |  |
| pending | ImageNet-1K | 2406.16722 | Accuracy |  |  |
| pending | KIBA | 2309.16685 | MSE | KIBA | yes |
| pending | LastFM | 2406.02740 | AUC |  |  |
| pending | Lattice | 2410.14109 | MAE |  |  |
| pending | LBA | 2309.16685 | RMSE | Long-Range Graph Benchmark (LGB) |  |
| pending | LCC(N) | 2002.03155 | ROC-AUC | LCC |  |
| pending | LCC(X) | 2002.03155 | ROC-AUC | LCC Benchmark |  |
| pending | ListOps | 2310.02980 | Accuracy | ListOps |  |
| pending | ListOps | 2408.05822 | Accuracy | ListOps |  |
| pending | MetaQA-3 | 2605.23467 | Hits@1 | MetaQA |  |
| pending | Metr-LA | 2505.18728 | MSE |  |  |
| pending | Mini-ImageNet | 2306.08385 | Accuracy | Few-Shot Learning Benchmarks |  |
| pending | MOOC | 2406.02740 | AUC |  |  |
| pending | MSRC 21 | 2605.04834 | Accuracy |  |  |
| pending | MUV | 2412.07407 | AUROC | MoleculeNet | yes |
| pending | NAME | 2505.15405 | F1 |  |  |
| pending | NTU2012 | 2603.00599 | Accuracy |  |  |
| pending | ORIENT | 2505.15405 | F1 |  |  |
| pending | PathX | 2310.02980 | Accuracy | PathX |  |
| pending | PathX-256 | 2310.02980 | Accuracy | PathX |  |
| pending | PCQM4M-LSC | 2303.00579 | MAE | OGB-LSC | yes |
| pending | Perturb-seq | 2410.14109 | MAE |  |  |
| pending | Pinterest | 1806.01973 | Hit-rate, Hit-rate@1000 | OGB |  |
| pending | Polymer | 2302.08647 | MAE |  |  |
| pending | PPA | 2502.02479 | HR@100 |  |  |
| pending | PTB | 2312.04234 | Perplexity |  |  |
| pending | PTC | 1810.00826 | Accuracy |  | yes |
| pending | PTC | 1812.09902 | Accuracy | TUDataset | yes |
| pending | PTC | 1901.00596 | Accuracy | TUDataset | yes |
| pending | PTC | 1912.06058 | Accuracy | TUDataset | yes |
| pending | PTC | 2106.04319 | Accuracy | TUDataset | yes |
| pending | PTC | 2106.12575 | Accuracy |  | yes |
| pending | PTC | 2110.02910 | Accuracy | TUDataset | yes |
| pending | PTC | 2110.03753 | Accuracy |  | yes |
| pending | PTC | 2111.06283 | Accuracy | TU-Molecular | yes |
| pending | PTC | 2210.17224 | Accuracy | TUDataset | yes |
| pending | PTC | 2406.01249 | Accuracy |  | yes |
| pending | PTC | 2406.06984 | Accuracy |  | yes |
| pending | PTC | 2502.09263 | Accuracy |  | yes |
| pending | PTC-MR | 2205.13328 | Accuracy | TUDataset | yes |
| pending | PTC-MR | 2405.02795 | Accuracy | TUDataset | yes |
| pending | PTC-MR | 2406.11714 | Accuracy | TUDataset | yes |
| pending | PTC_FM | 2402.07568 | Accuracy | MoleculeNet | yes |
| pending | PTC_MR | 2112.07160 | Accuracy | TUDataset | yes |
| pending | PTC_MR | 2310.02156 | Accuracy | TUDataset | yes |
| pending | PTC_MR | 2402.07568 | Accuracy | TUDataset | yes |
| pending | Retrieval | 2310.02980 | Accuracy |  |  |
| pending | RootNeighbors | 2310.01267 | MAE |  |  |
| pending | School | 2511.16767 | Accuracy |  |  |
<<<<<<< Updated upstream
| pending | sCIFAR | 2310.02980 | Accuracy |  |  |
| pending | SCOPe | 2306.04667 | F1-Score |  |  |
| pending | SF2-30 | 2601.18917 | F1 |  |  |
| pending | SF4-30 | 2601.18917 | F1 |  |  |
| pending | Shortest Path (Erdős–Rényi) (15k) | 2402.10793 | MCC | Graph Generation Benchmark |  |
| pending | Shortest Path (Erdős–Rényi) (30k) | 2402.10793 | MCC | GraphGen |  |
| pending | Springs | 2601.18917 | MSE | GNN-Generalization-Benchmark |  |
| pending | SR | 2410.06460 | Ranking |  |  |
| pending | sr25 | 2407.18480 | Undistinguished Pairs | Graph Isomorphism Benchmark |  |
| pending | SR25 | 2501.18739 | Accuracy |  |  |
| pending | SST2 | 2401.03350 | AUROC |  | yes |
| pending | subgraph counting | 2102.08786 | MAE | GraphGym |  |
| pending | Superblue | 2404.00477 | RMSE | Superblue |  |
| pending | Synthetic | 2309.04941 | Normalized MAE |  |  |
| pending | Synthetic Subgraph Counting | 2403.13749 | MAE |  |  |
| pending | TCGA | 2406.04377 | C-index |  |  |
| pending | TGBL-Coin | 2412.03783 | MRR | TGB |  |
| pending | tgbl-review-v2 | 2406.02740 | MRR | TGBL |  |
| pending | thgl-forum | 2406.09639 | MRR |  |  |
| pending | thgl-software | 2406.09639 | MRR |  |  |
| pending | TIME | 2410.06460 | Ranking |  |  |
| pending | tkgl-icews | 2406.09639 | MRR | TKGL |  |
| pending | tkgl-polecat | 2406.09639 | MRR | TKGL |  |
| pending | TOSCA | 2402.04821 | Accuracy | TOSCA |  |
| pending | TPUGraphs | 2405.19121 | Kendall tau |  |  |
| pending | Triangle Counting | 2411.15671 | RMSE |  |  |
| pending | UCI | 2506.05393 | MRR |  |  |
| pending | User-post-comment | 2502.01122 | MAP |  |  |
| pending | WikiMath | 2410.05593 | MSE |  |  |
=======
| pending | Text | 2310.02980 | Accuracy |  |  |
| pending | tgbl-coin-v2 | 2406.02740 | MRR | TGB (Time-Bench Graph) |  |
| pending | tgbl-comment | 2406.02740 | MRR | TGB (Temporal Graph Benchmark) |  |
| pending | tgbl-review-v2 | 2406.02740 | MRR | TGB (Time-Bench Graph) |  |
| pending | TRI(N) | 2002.03155 | ROC-AUC | TRI(N) |  |
| pending | TRI(X) | 2002.03155 | ROC-AUC | TRI(X) Benchmark |  |
| pending | USAir | 1802.09691 | AUC |  |  |
| pending | VarMisuse | 2105.14491 | Accuracy |  |  |
>>>>>>> Stashed changes
| pending | WikiText-103 | 2312.04234 | Perplexity |  |  |
| pending | XUAMP | 2501.17901 | AUROC |  |  |
| pending | Yelp | 2004.11198 | F1 | OGB | yes |
| pending | Yelp | 2201.07858 | F1-micro | OGB | yes |
| pending | YouTube | 1403.6652 | Micro-F1 | OGBN-YouTube |  |