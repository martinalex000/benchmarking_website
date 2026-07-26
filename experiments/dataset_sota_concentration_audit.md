# Dataset SOTA concentration audit

Generated 2026-07-26 from the local SQLite database and local LaTeX sources. The analysis itself was read-only; the remediation recorded below was applied afterward.

## Executive summary

- Datasets checked: **142**.
- Concentrated-gap candidates: **85**.
- Datasets with no eligible primary-metric rows: **26**.
- Candidate driver rows audited: **159** across local `expanded.tex` sources.
- The strongest confirmed mismatches are Amazon-ratings, arxiv-year, ogbl-wikikg2, FB15k-237/WN18RR, MUTAG, and the missing MD17 value. PCQM4Mv2 has a split-variant conflation, and BBBP/RDT-B/ClinTox have protocol or external-pretraining caveats.

## Method

Rows were restricted to eligible canonical standard variants, primary metrics, `protocol_decision=standard`, and non-problematic results. Results were reduced to the best directional value per paper. A candidate has at least three independent papers and either a top-two driver share of at least 50% of the historical directional improvement or a largest improvement at least three times the median positive improvement. Multiple model rows in one paper therefore count as one driver.

## All datasets

| Dataset | Task | Metric | Papers | Milestones | Final SOTA | Total gain | Top-2 share | Jump/median | Classification | Main drivers |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 20News | graph_classification | Accuracy | 3 | 1 | 0.7002 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| ACM | node_classification | Micro-F1 | 18 | 5 | 0.979 | 0.0512 | 86.1% | 4.0x | CONCENTRATED CANDIDATE | 2510.05750:HetGNN +0.0321; 2207.02547:SeHGNN +0.012 |
| AMAP | node_classification | F1 | 6 | 1 | 0.8208 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| AQSOL | graph_regression | MAE | 3 | 1 | 0.92 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| Actor | node_classification | Accuracy | 96 | 7 | 0.4535 | 0.0745 | 83.6% | 10.7x | CONCENTRATED CANDIDATE | 2106.10994:BernNet +0.0389; 2408.13471:DiGGR +0.0234 |
| Algorithmic Reasoning | graph_classification | Accuracy | 1 | 1 | 0.9971 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Amazon-Computers | node_classification | Accuracy | 118 | 7 | 0.9461 | 0.0943 | 61.1% | 3.8x | CONCENTRATED CANDIDATE | 2009.00934:SAIL +0.0422; 2112.14531:F^2GAT +0.0154 |
| Amazon-Photo | node_classification | Accuracy | 131 | 9 | 0.9766 | 0.0486 | 51.6% | 2.8x | CONCENTRATED CANDIDATE | 2205.11172:JacobiConv +0.0133; 2305.12677:NAGphormer +0.0118 |
| Amazon-ratings | node_classification | Accuracy | 30 | 6 | 0.8562 | 0.3199 | 93.3% | 22.8x | CONCENTRATED CANDIDATE | 2407.14732:Meta-GPS++ +0.2644; 2502.04591:GCN +0.0342 |
| Amazon2M | node_classification | Accuracy | 15 | 2 | 0.9755 | 0.0225 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2508.09320:MEAN +0.0225 |
| BA graph | graph_classification | Accuracy | 3 | 3 | 0.9793 | 0.4773 | 100.0% | 1.2x | CONCENTRATED CANDIDATE | 2505.11298:F4-MPNN +0.2981; 2402.16029:GraphWiz +0.1792 |
| BACE | graph_classification | ROC-AUC | 57 | 2 | 0.934 | 0.027 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2112.00544:KG(GCN) +0.027 |
| BAT | node_classification | F1 | 5 | 3 | 0.7777 | 0.0555 | 100.0% | 1.1x | CONCENTRATED CANDIDATE | 2212.03559:GraphLearner +0.0318; 2308.08963:CONVERT +0.0237 |
| BBBP | graph_classification | ROC-AUC | 59 | 4 | 0.961 | 0.236 | 93.6% | 5.3x | CONCENTRATED CANDIDATE | 2106.04509:MoCL+AttrMask-G(CL) +0.186; 2112.00544:KG(KMPNN) +0.035 |
| BlueSky | node_classification | MAE | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Bridges | graph_classification | F1 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| CAMELS-SAM | graph_regression | R^2 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| CIFAR10 | graph_classification | Accuracy | 14 | 3 | 0.7942 | 0.0594 | 100.0% | 1.9x | CONCENTRATED CANDIDATE | 2404.09774:RandAlign +0.05612; 2201.12674:Ours(100K) +0.00328 |
| CLUSTER | node_classification | Accuracy | 16 | 4 | 0.8159 | 0.05196 | 93.2% | 4.8x | CONCENTRATED CANDIDATE | 2201.12787:GRPE-Small +0.04011; 2201.09332:FeTA + LPE + Sparse +0.00834 |
| COCO-SP | node_classification | F1 | 5 | 3 | 0.3891 | 0.0661 | 100.0% | 2.0x | CONCENTRATED CANDIDATE | 2405.11951:GPS +0.0654; 2411.12732:GraphGPS + RWSE +0.0007 |
| COLLAB | graph_classification | Accuracy | 80 | 5 | 0.964 | 0.157 | 76.9% | 3.8x | CONCENTRATED CANDIDATE | 2505.15015:MSH-GNN +0.0918; 1905.13192:GNTK +0.029 |
| COVID | graph_regression | RMSE | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| CS-Trees | graph_regression | R2 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| CS-Trees-200 | graph_classification | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| CSL | graph_classification | Accuracy | 16 | 2 | 1 | 0.2 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2005.01214:GHC-Cycles +0.2 |
| Case 1 | graph_regression | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Case 2 | graph_regression | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Chameleon | node_classification | Accuracy | 63 | 6 | 0.8693 | 0.1683 | 84.1% | 6.9x | CONCENTRATED CANDIDATE | 2105.07634:FSGNN +0.0713; 2406.12539:Hetero-S (GAT 8-layer) +0.0702 |
| Chip Design | graph_generation | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| CiteSeer | node_classification | Accuracy | 177 | 6 | 0.9575 | 0.2325 | 84.7% | 8.4x | CONCENTRATED CANDIDATE | 1805.07984:Clean +0.155; 2306.15902:IS-GIB +0.042 |
| ClinTox | graph_classification | ROC-AUC | 49 | 8 | 0.993 | 0.243 | 64.2% | 4.4x | CONCENTRATED CANDIDATE | 2106.06130:D-MPNN +0.0928; 2106.05819:JOAO +0.0632 |
| Coauthor-CS | node_classification | Accuracy | 54 | 6 | 0.969 | 0.0507 | 80.3% | 5.9x | CONCENTRATED CANDIDATE | 2002.06755:GCN-LPA +0.0297; 2503.12563:DoG (EXPHORMER) +0.011 |
| Coauthor-Physics | node_classification | Accuracy | 58 | 8 | 0.9878 | 0.0429 | 70.2% | 5.9x | CONCENTRATED CANDIDATE | 2002.06755:GCN-LPA +0.0241; 2505.15015:MSH-GNN +0.006 |
| Code | graph_classification | F1 | 3 | 2 | 0.1948 | 0.0429 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2405.11951:LGI-GT +0.0429 |
| Combinatorial Optimization | node_classification | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Congress | node_classification | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Cora | node_classification | Accuracy | 183 | 6 | 0.9635 | 0.1305 | 64.8% | 2.8x | CONCENTRATED CANDIDATE | 1711.08920:SplineCNN +0.0618; 2412.04064:GraphSAGE+CNA +0.0228 |
| Cora-CA | node_classification | Accuracy | 3 | 2 | 0.8236 | 0.0021 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2406.06642:EDGNN +0.0021 |
| Cornell | node_classification | Accuracy | 121 | 12 | 0.9541 | 0.1051 | 51.1% | 6.6x | CONCENTRATED CANDIDATE | 2106.10994:BernNet +0.0429; 2103.06064:transparent GNN architecture +0.0108 |
| D&D | graph_classification | Accuracy | 36 | 7 | 0.921 | 0.1365 | 77.6% | 6.8x | CONCENTRATED CANDIDATE | 2309.00738:GC-GNN (GraphSAGE) +0.0807; 1704.02901:structure2vec +0.0252 |
| DBLP | node_classification | Micro-F1 | 27 | 2 | 0.9993 | 0.1773 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 1912.10832:HERec +0.1773 |
| DBLP-CA | node_classification | Accuracy | 1 | 1 | 0.9198 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Deezer | node_classification | ROC-AUC | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| EAT | node_classification | F1 | 5 | 1 | 0.7277 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| ECHO-Charge | graph_regression | MAE | 1 | 1 | 0.006109 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| ECHO-Energy | graph_regression | MAE | 1 | 1 | 0.053 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| ECHO-Synth | graph_regression | MAE | 2 | 2 | 0.035 | 0.086 | 100.0% | 1.0x | INSUFFICIENT COVERAGE | 2605.18387:GHR +0.086 |
| ENZYMES | graph_classification | Accuracy | 50 | 6 | 0.8068 | 0.2078 | 81.0% | 5.7x | CONCENTRATED CANDIDATE | 1906.01277:WWL +0.1142; 2002.09518:GMN +0.0541 |
| ER graph | graph_classification | Accuracy | 3 | 3 | 0.9793 | 0.5283 | 100.0% | 1.9x | CONCENTRATED CANDIDATE | 2402.16029:GraphWiz (LLaMA 2-13B) +0.4965; 2505.11298:F_4-MPNN +0.0318 |
| ESOL | graph_regression | RMSE | 21 | 1 | 0.278 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| Eccentricity | graph_regression | MSE | 1 | 1 | 0.3046 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Electronic Circuits | graph_classification | MAE | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| FB15k-237 | link_prediction | MRR | 10 | 4 | 0.979 | 0.641 | 97.8% | 35.9x | CONCENTRATED CANDIDATE | 2210.02636:GDGNN-Vert +0.61; 1911.03082:CompGCN +0.017 |
| Film | node_classification | Accuracy | 17 | 4 | 0.432 | 0.0539 | 98.3% | 3.2x | CONCENTRATED CANDIDATE | 2503.12563:DoG (ACM-GCN) +0.0404; 2307.16092:ADR-GNN_S +0.0126 |
| Flow | graph_regression | MAE | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| FreeSolv | graph_regression | RMSE | 19 | 3 | 0.354 | 1.347 | 100.0% | 1.7x | CONCENTRATED CANDIDATE | 2109.11730:GeomGCL +1.16; 2312.07633:SE(3)-I MPPH +0.187 |
| Freebase | node_classification | Macro-F1 | 6 | 5 | 0.6247 | 0.106 | 79.7% | 2.6x | CONCENTRATED CANDIDATE | 2403.04780:MuseGraph (LLaMA3-8B) +0.056; 2404.02810:GC-HGNN +0.0285 |
| HSG-12M | graph_classification | Accuracy | 1 | 1 | 0.546 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| HSG-topology | graph_classification | Accuracy | 1 | 1 | 0.62 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| House | node_classification | Accuracy | 1 | 1 | 0.747 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| IMDB | node_classification | Micro-F1 | 17 | 3 | 0.8133 | 0.0747 | 100.0% | 1.2x | CONCENTRATED CANDIDATE | 2208.06129:MHGCN +0.0434; 2210.05920:GAT BGNN(m)-SC +0.0313 |
| IMDB-BINARY | graph_classification | Accuracy | 20 | 4 | 0.7863 | 0.0694 | 75.1% | 1.9x | CONCENTRATED CANDIDATE | 1810.00826:GIN-0 +0.0341; 2005.01214:GNTK +0.018 |
| IMDB-MULTI | graph_classification | Accuracy | 13 | 3 | 0.779 | 0.294 | 100.0% | 1.7x | CONCENTRATED CANDIDATE | 2206.02059:GraphSNN +0.251; 2005.01214:GNTK +0.043 |
| LEN | node_classification | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| LRIM | node_regression | log-MSE | 2 | 1 | -4.345 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Lipophilicity | graph_regression | RMSE | 10 | 1 | 0.556 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| London | node_classification | Accuracy | 1 | 1 | 0.554 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Los Angeles | node_classification | Accuracy | 1 | 1 | 0.638 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| MD17 | graph_regression | MAE | 25 | 3 | -1 | 1.04 | 100.0% | 2.0x | CONCENTRATED CANDIDATE | 2304.04757:GemNet (T/Q) +1.039; 2210.16518:ViSNet +0.001 |
| MNIST | graph_classification | Accuracy | 22 | 1 | 0.9914 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| MST | graph_classification | F1 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| MUTAG | graph_classification | Accuracy | 163 | 7 | 0.991 | 0.133 | 69.4% | 4.8x | CONCENTRATED CANDIDATE | 1605.05273:PSCN k=10E +0.0683; 2006.02587:GCN +0.024 |
| MalNet-Tiny | graph_classification | Accuracy | 3 | 2 | 0.9354 | 0.0009 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2505.11356:GCN +0.0009 |
| Max Clique | graph_classification | F1 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Max Matching | graph_classification | F1 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Minesweeper | node_classification | ROC-AUC | 16 | 4 | 0.985 | 0.0447 | 76.7% | 1.3x | CONCENTRATED CANDIDATE | 2403.01232:Polynormer-r +0.0196; 2305.16780:CDE-GRAND-GAT +0.0147 |
| NCI1 | graph_classification | Accuracy | 116 | 4 | 0.962 | 0.103 | 98.1% | 32.7x | CONCENTRATED CANDIDATE | 2312.10943:MSA-AUD +0.098; 2210.01906:FGW +0.003 |
| PATTERN | node_classification | Accuracy | 17 | 5 | 0.9066 | 0.06107 | 96.9% | 3.6x | CONCENTRATED CANDIDATE | 2303.00579:DeepGraph (48) +0.039; 2010.05421:FactorGCN +0.0202 |
| PCQM-Contact | link_prediction | MRR | 6 | 4 | 0.4737 | 0.1387 | 94.5% | 3.6x | CONCENTRATED CANDIDATE | 2411.12732:Exphormer + LapPE +0.1024; 2406.12059:Exphormer +0.0287 |
| PCQM4Mv2 | graph_regression | MAE | 6 | 3 | 0.0722 | 0.0483 | 100.0% | 1.4x | CONCENTRATED CANDIDATE | 2201.12787:EGT-Large +0.0333; 2212.02229:All (Ensemble) +0.015 |
| PPI | node_classification | F1 | 40 | 7 | 0.9982 | 0.3862 | 97.1% | 77.5x | CONCENTRATED CANDIDATE | 1803.07294:GaAN +0.3371; 1802.08888:N-SAGE +0.038 |
| PROTEINS | graph_classification | Accuracy | 96 | 3 | 0.8383 | 0.0743 | 100.0% | 1.8x | CONCENTRATED CANDIDATE | 1905.11577:lapool +0.0657; 1904.05003:SAGE +0.0086 |
| Paris | node_classification | Accuracy | 1 | 1 | 0.551 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| PascalVOC-SP | node_classification | F1 | 9 | 6 | 0.78 | 0.457 | 86.5% | 10.1x | CONCENTRATED CANDIDATE | 2411.12732:GCN +0.3323; 2310.07430:Graph-Mamba +0.0631 |
| Penn94 | node_classification | Accuracy | 18 | 4 | 0.8669 | 0.0183 | 73.8% | 1.2x | CONCENTRATED CANDIDATE | 2303.06344:GloGNN +0.0074; 2405.16185:DC-GNN +0.0061 |
| Peptides-func | graph_classification | AP | 21 | 4 | 0.7311 | 0.0872 | 88.1% | 1.0x | CONCENTRATED CANDIDATE | 2310.07430:NBA-GCN+LapPE +0.039; 2302.08647:MGT+WavePE +0.0378 |
| Peptides-struct | graph_regression | MAE | 15 | 4 | 0.2421 | 0.0108 | 97.2% | 2.6x | CONCENTRATED CANDIDATE | 2302.08647:MGT+WavePE +0.0076; 2310.07430:NBA-GIN+LapPE +0.0029 |
| Pokec | node_classification | Accuracy | 9 | 3 | 0.861 | 0.0377 | 100.0% | 1.6x | CONCENTRATED CANDIDATE | 2403.01232:Polynormer-r +0.0308; 2311.05185:MoE-H2GCN +0.0069 |
| PubMed | node_classification | Accuracy | 170 | 11 | 0.9517 | 0.1407 | 63.4% | 9.5x | CONCENTRATED CANDIDATE | 2002.06755:GCN-LPA +0.067; 2308.07134:Flan-T5-large +0.0222 |
| QM7b | graph_regression | MAE | 7 | 1 | 2.86 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| QM9 | graph_regression | gap | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Questions | node_classification | ROC-AUC | 22 | 2 | 0.9733 | 0.0006 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2405.20445:MLP +0.0006 |
| Quijote | graph_regression | R^2 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| RB graph | graph_classification | Accuracy | 1 | 1 | 0.9793 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| RCDD | link_prediction | MRR | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| RDT-B | graph_classification | Accuracy | 18 | 4 | 0.963 | 0.153 | 81.7% | 2.4x | CONCENTRATED CANDIDATE | 2006.09963:GCC (MoCo, freeze) +0.088; 2009.03294:GraphNorm +0.037 |
| REDDIT-BINARY | graph_classification | Accuracy | 7 | 3 | 0.91 | 0.0228 | 100.0% | 1.3x | CONCENTRATED CANDIDATE | 2210.11790:Last layer FA +0.015; 2512.12642:bnpool +0.0078 |
| REDDIT-MULTI-5K | graph_classification | Accuracy | 5 | 3 | 0.5944 | 0.0194 | 100.0% | 1.9x | CONCENTRATED CANDIDATE | 2410.10365:SpeGCL +0.0184; 2401.16011:GIN +0.001 |
| Reddit | node_classification | F1 | 40 | 7 | 0.9728 | 0.0188 | 67.0% | 5.1x | CONCENTRATED CANDIDATE | 1803.07294:GaAN +0.0096; 2104.09376:SAGN+SLE +0.003 |
| Ribonanza | graph_regression | RMSE | 2 | 2 | 0.505 | 0.024 | 100.0% | 1.0x | INSUFFICIENT COVERAGE | 2506.19862:DualEquiNet +0.024 |
| Roman-empire | node_classification | Accuracy | 32 | 7 | 0.9477 | 0.0554 | 65.0% | 4.3x | CONCENTRATED CANDIDATE | 2305.16780:CDE-GRAND-GAT +0.0241; 2604.08980:Dir-NT +0.0119 |
| SAT Solving | node_classification | Accuracy | 1 | 1 | 0.51 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| SIDER | graph_classification | ROC-AUC | 45 | 6 | 0.847 | 0.219 | 80.5% | 5.1x | CONCENTRATED CANDIDATE | 2604.16586:KA-GAT +0.137; 2106.06130:ChemRL-GEM +0.0392 |
| SSSP | graph_regression | MSE | 1 | 1 | -3.402 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Senate | node_classification | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Shanghai | node_classification | Accuracy | 1 | 1 | 0.702 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| ShapeNet-Part | node_classification | F1 | 1 | 1 | 0.814 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Squirrel | node_classification | Accuracy | 60 | 6 | 0.7763 | 0.1863 | 98.8% | 94.4x | CONCENTRATED CANDIDATE | 2105.07634:FSGNN +0.151; 2412.04064:Trans.Conv+CNA +0.033 |
| Steiner Trees | graph_classification | F1 | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| TSP | link_prediction | F1 | 3 | 3 | 0.863 | 0.055 | 100.0% | 1.1x | CONCENTRATED CANDIDATE | 2003.00982:GatedGCN-E +0.03; 2407.00696:GIG-GatedGCN +0.025 |
| Tc-Ribo | graph_regression | RMSE | 2 | 1 | 0.548 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Texas | node_classification | Accuracy | 134 | 10 | 0.9672 | 0.1132 | 68.2% | 17.6x | CONCENTRATED CANDIDATE | 2106.10994:BernNet +0.0582; 2105.07634:FSGNN +0.019 |
| Tolokers | node_classification | ROC-AUC | 21 | 2 | 0.8591 | 0.0108 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2403.01232:Polynormer-r +0.0108 |
| Topological Sorting | node_classification | MAE | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| TorsionAngle | graph_regression | Circular MAE | 1 | 1 | 15.87 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| Tox21 | graph_classification | ROC-AUC | 59 | 2 | 0.874 | 0.0398 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2011.15069:HIMP +0.0398 |
| ToxCast | graph_classification | ROC-AUC | 42 | 3 | 0.8073 | 0.0583 | 100.0% | 1.5x | CONCENTRATED CANDIDATE | 2311.04837:SCI +0.0443; 2109.11730:GeomGCL +0.014 |
| UAT | node_classification | F1 | 4 | 1 | 0.7277 | 0 | 0.0% | 0.0x | NO CONCENTRATED GAP | - |
| WN18 | link_prediction | MRR | 4 | 3 | 0.949 | 0.011 | 100.0% | 1.5x | CONCENTRATED CANDIDATE | 1902.10197:RotatE +0.008; 1703.06103:ComplEx +0.003 |
| WN18RR | link_prediction | MRR | 14 | 4 | 0.949 | 0.473 | 99.4% | 19.4x | CONCENTRATED CANDIDATE | 2210.02636:GDGNN-Hor +0.447; 2009.14332:MAGNA + DistMult +0.023 |
| Walmart | node_classification | Accuracy | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| Weather Forecasting | node_classification | MAE | 0 | 0 | - | 0 | 0.0% | 0.0x | NO ELIGIBLE ROWS | - |
| WikiCS | node_classification | Accuracy | 43 | 3 | 0.9302 | 0.1318 | 100.0% | 2.0x | CONCENTRATED CANDIDATE | 2204.04874:GCN +0.1288; 2102.06514:GRACE +0.003 |
| Wisconsin | node_classification | Accuracy | 36 | 5 | 0.958 | 0.085 | 75.2% | 4.5x | CONCENTRATED CANDIDATE | 2504.19785:ACM-GCN +0.0521; 2404.17099:F-GREAD-BS +0.0118 |
| ZINC | graph_regression | MAE | 13 | 5 | 0.02 | 1.346 | 96.4% | 12.0x | CONCENTRATED CANDIDATE | 2012.09699:GatedGCN +1.152; 2201.09332:FeTA + GCKN + 3RW +0.146 |
| arxiv-year | node_classification | Accuracy | 14 | 5 | 0.8561 | 0.2961 | 91.5% | 4.6x | CONCENTRATED CANDIDATE | 2506.08298:H^2GFM +0.1979; 2210.00513:G^2-GraphSAGE +0.073 |
| ogbg-molhiv | graph_classification | ROC-AUC | 66 | 6 | 0.997 | 0.206 | 88.9% | 17.8x | CONCENTRATED CANDIDATE | 2210.08443:CLEAR +0.1567; 2205.11678:HIG with DeeperGCN +0.0264 |
| ogbg-molpcba | graph_classification | AP | 19 | 3 | 0.3167 | 0.022 | 100.0% | 1.8x | CONCENTRATED CANDIDATE | 2201.12787:GRPE-Large +0.0203; 2205.11678:HIG with Graphormer +0.0017 |
| ogbg-ppa | graph_classification | Accuracy | 12 | 6 | 0.8149 | 0.0951 | 80.9% | 4.2x | CONCENTRATED CANDIDATE | 2103.16584:DeeperGCN+FLAG +0.0554; 2305.06102:GPS +0.0215 |
| ogbl-biokg | link_prediction | MRR | 1 | 1 | 0.8309 | 0 | 0.0% | 0.0x | INSUFFICIENT COVERAGE | - |
| ogbl-citation2 | link_prediction | MRR | 18 | 3 | 0.9072 | 0.0305 | 100.0% | 1.4x | CONCENTRATED CANDIDATE | 2202.13538:SUREL +0.0207; 2309.00976:MPLP +0.0098 |
| ogbl-collab | link_prediction | Hits@50 | 15 | 6 | 0.765 | 0.243 | 92.2% | 9.9x | CONCENTRATED CANDIDATE | 2010.16103:SEAL +0.1254; 2410.01802:PROXI +0.0986 |
| ogbl-ddi | link_prediction | Hits@20 | 14 | 3 | 0.9777 | 0.3547 | 100.0% | 1.9x | CONCENTRATED CANDIDATE | 2012.15024:MPNNs +0.3308; 2310.14166:ELGNN +0.0239 |
| ogbl-ppa | link_prediction | Hits@100 | 19 | 6 | 0.6524 | 0.3104 | 73.4% | 3.7x | CONCENTRATED CANDIDATE | 2010.16103:SEAL +0.146; 2302.00890:NCNC +0.0819 |
| ogbl-wikikg2 | link_prediction | MRR | 4 | 2 | 0.749 | 0.02 | 100.0% | 1.0x | CONCENTRATED CANDIDATE | 2307.01026:NAT +0.02 |
| ogbn-arxiv | node_classification | Accuracy | 28 | 5 | 0.7764 | 0.0453 | 85.0% | 3.6x | CONCENTRATED CANDIDATE | 2111.00064:GIANT-XRT +0.0271; 2309.14907:REVGAT with X_LD +0.0114 |
| ogbn-mag | node_classification | Accuracy | 14 | 5 | 0.5784 | 0.0974 | 80.1% | 4.5x | CONCENTRATED CANDIDATE | 2104.09376:NARS_SAGN+0-SLE +0.063; 2108.10097:NARS-GAMLP+RLU +0.015 |
| ogbn-papers100M | node_classification | Accuracy | 24 | 6 | 0.791 | 0.1399 | 83.1% | 6.2x | CONCENTRATED CANDIDATE | 2403.13268:SGC +0.0874; 2104.09376:SAGN+SLE +0.0289 |
| ogbn-products | node_classification | Accuracy | 67 | 7 | 0.8931 | 0.1023 | 53.5% | 2.4x | CONCENTRATED CANDIDATE | 2009.03509:UniMP +0.0348; 2010.13993:FDiff-scale (MLP) +0.0199 |
| ogbn-proteins | node_classification | ROC-AUC | 13 | 3 | 0.8942 | 0.0716 | 100.0% | 1.2x | CONCENTRATED CANDIDATE | 2009.03509:UniMP +0.0416; 2309.14907:X_LD +0.03 |
| snap-patents | node_classification | Accuracy | 8 | 4 | 0.751 | 0.243 | 92.5% | 4.9x | CONCENTRATED CANDIDATE | 2210.00513:G^2-GraphSAGE +0.187; 2310.02232:FaberNet +0.0378 |
| twitch-gamers | node_classification | Accuracy | 11 | 4 | 0.6977 | 0.0371 | 94.6% | 3.7x | CONCENTRATED CANDIDATE | 2505.14033:CPF +0.0277; 2303.06344:HLCL +0.0074 |

## Source-audited driver rows

Evidence flags: `D` dataset mention, `T` expected task evidence near the dataset mention, `M` metric evidence, `P` protocol evidence. These compact flags supplement the manual findings below; `SOURCE-UNCLEAR` means the paper source does not provide enough local lexical evidence to certify the mapping automatically.

| Dataset | Driver paper | Model | Gain | Audit status | Local-source/task audit |
|---|---|---|---:|---|---|
| ACM | 2510.05750 | HetGNN | 0.0321 | SOURCE-COMPATIBLE | Local TeX=papers/2510.05750/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split for ACM node classification. |
| ACM | 2207.02547 | SeHGNN | 0.012 | SOURCE-COMPATIBLE | Local TeX=papers/2207.02547/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification on ACM heterogeneous graph. |
| Actor | 2106.10994 | BernNet | 0.0389 | SOURCE-COMPATIBLE | Local TeX=papers/2106.10994/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Geom-GCN 10 fixed splits.. |
| Actor | 2408.13471 | DiGGR | 0.0234 | SOURCE-COMPATIBLE | Local TeX=papers/2408.13471/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification on heterophilous dataset Actor using standard split/task.. |
| Amazon-Computers | 2009.00934 | SAIL | 0.0422 | SOURCE-COMPATIBLE | Local TeX=papers/2009.00934/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on Computers dataset. |
| Amazon-Computers | 2112.14531 | F^2GAT | 0.0154 | COMPATIBLE | The source explicitly uses 60/20/20 for Cora/DBLP/Computers/PubMed/Physics and reserves Geom-GCN masks for Wisconsin and Actor; expanded.tex:522-523, 561-565. |
| Amazon-Photo | 2205.11172 | JacobiConv | 0.0133 | COMPATIBLE | The source explicitly defines node classification with random 60/20/20 splits for the Amazon co-purchase graphs; expanded.tex:927-932. |
| Amazon-Photo | 2305.12677 | NAGphormer | 0.0118 | SOURCE-COMPATIBLE | Local TeX=papers/2305.12677/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Mean accuracy reported over 10 trials; uses NrAug. |
| Amazon-ratings | 2407.14732 | Meta-GPS++ | 0.2644 | MISMATCH | The source evaluates Amazon-Clothing/Electronics in 5-way/3-shot and 5-way/5-shot meta-learning tables, not canonical Amazon-ratings full-task node classification; expanded.tex:474-494, 575-600. |
| Amazon-ratings | 2502.04591 | GCN | 0.0342 | MISMATCH | The source value is an accuracy-ratio entry in an oversmoothing correlation table, not a benchmark test accuracy; expanded.tex:901-911. |
| Amazon2M | 2508.09320 | MEAN | 0.0225 | SOURCE-UNCLEAR | Local TeX=papers/2508.09320/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Test set accuracy for node classification using mean aggregation.. |
| BA graph | 2505.11298 | F4-MPNN | 0.2981 | COMPATIBLE | The source evaluates graph labels derived from cycle counts with graph classification and 10-fold evaluation. The database description says node classification, which is a metadata-description error, not a result-task mismatch; expanded.tex:276, 779, 798-800. |
| BA graph | 2402.16029 | GraphWiz | 0.1792 | SOURCE-PARTIAL | Local TeX=papers/2402.16029/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Average accuracy reported for BA graphs across six tasks (Cycle, Connectivity, Bipartite, Hamilton, Shortest, . |
| BACE | 2112.00544 | KG(GCN) | 0.027 | SOURCE-COMPATIBLE | Local TeX=papers/2112.00544/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Fine-tune protocol on BACE scaffold split. |
| BAT | 2212.03559 | GraphLearner | 0.0318 | SOURCE-PARTIAL | Local TeX=papers/2212.03559/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Clustering performance reported as mean ± std. |
| BAT | 2308.08963 | CONVERT | 0.0237 | SOURCE-PARTIAL | Local TeX=papers/2308.08963/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Clustering performance evaluated via ten runs. |
| BBBP | 2106.04509 | MoCL+AttrMask-G(CL) | 0.186 | PROTOCOL | The driver value is from a linear-probe evaluation of pretrained representations, while canonical BBBP comparison rows are supervised molecular property evaluation on the scaffold split; expanded.tex:378-384, 494-512. |
| BBBP | 2112.00544 | KG(KMPNN) | 0.035 | SOURCE-COMPATIBLE | Local TeX=papers/2112.00544/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Fine-tune protocol on BBBP scaffold split. |
| CIFAR10 | 2404.09774 | RandAlign | 0.05612 | SOURCE-COMPATIBLE | Local TeX=papers/2404.09774/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Superpixel graph classification on CIFAR10, L=8. |
| CIFAR10 | 2201.12674 | Ours(100K) | 0.00328 | SOURCE-PARTIAL | Local TeX=papers/2201.12674/latex/expanded.tex; evidence flags DTmP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Standard graph classification task on CIFAR10 super-pixel graphs.. |
| CLUSTER | 2201.12787 | GRPE-Small | 0.04011 | SOURCE-COMPATIBLE | Local TeX=papers/2201.12787/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Weighted Accuracy on CLUSTER node classification task. |
| CLUSTER | 2201.09332 | FeTA + LPE + Sparse | 0.00834 | SOURCE-COMPATIBLE | Local TeX=papers/2201.09332/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification task on CLUSTER dataset. |
| COCO-SP | 2405.11951 | GPS | 0.0654 | SOURCE-PARTIAL | Local TeX=papers/2405.11951/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Test F1 on COCO-SP. |
| COCO-SP | 2411.12732 | GraphGPS + RWSE | 0.0007 | SOURCE-COMPATIBLE | Local TeX=papers/2411.12732/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split for COCO-SP. |
| COLLAB | 2505.15015 | MSH-GNN | 0.0918 | SOURCE-COMPATIBLE | Local TeX=papers/2505.15015/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Mean accuracy on COLLAB dataset. |
| COLLAB | 1905.13192 | GNTK | 0.029 | SOURCE-COMPATIBLE | Local TeX=papers/1905.13192/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Standard graph classification task on COLLAB. |
| CSL | 2005.01214 | GHC-Cycles | 0.2 | COMPATIBLE | The source reports 10-fold cross-validation for the synthetic graph classification benchmark; this matches the intended CSL evaluation convention; expanded.tex: results section around the CSL table. |
| Chameleon | 2105.07634 | FSGNN | 0.0713 | SOURCE-COMPATIBLE | Local TeX=papers/2105.07634/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Geom-GCN 10 fixed splits.. |
| Chameleon | 2406.12539 | Hetero-S (GAT 8-layer) | 0.0702 | SOURCE-COMPATIBLE | Local TeX=papers/2406.12539/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=8-layer GAT with Hetero-S reported in text.. |
| CiteSeer | 1805.07984 | Clean | 0.155 | SOURCE-COMPATIBLE | Local TeX=papers/1805.07984/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Planetoid split (20% labeled, 80% unlabeled) as described in setup.. |
| CiteSeer | 2306.15902 | IS-GIB | 0.042 | SOURCE-COMPATIBLE | Local TeX=papers/2306.15902/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Planetoid split (Yang et al. 2016 fixed split). |
| ClinTox | 2106.06130 | D-MPNN | 0.0928 | SOURCE-PARTIAL | Local TeX=papers/2106.06130/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Scaffold split (implied by context of molecular property benchmarks and standard ClinTox usage). |
| ClinTox | 2106.05819 | JOAO | 0.0632 | EXTERNAL | The downstream task matches, but the driver uses ZINC-2M pretraining; this is a provenance distinction rather than a task mismatch. |
| Coauthor-CS | 2002.06755 | GCN-LPA | 0.0297 | SOURCE-COMPATIBLE | Local TeX=papers/2002.06755/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Test set accuracy on Coauthor-CS. |
| Coauthor-CS | 2503.12563 | DoG (EXPHORMER) | 0.011 | SOURCE-COMPATIBLE | Local TeX=papers/2503.12563/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split following baseline methods. |
| Coauthor-Physics | 2002.06755 | GCN-LPA | 0.0241 | SOURCE-UNCLEAR | Local TeX=papers/2002.06755/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=test set accuracy. |
| Coauthor-Physics | 2505.15015 | MSH-GNN | 0.006 | SOURCE-COMPATIBLE | Local TeX=papers/2505.15015/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification on CoauthorPhy benchmark graph. |
| Code | 2405.11951 | LGI-GT | 0.0429 | SOURCE-UNCLEAR | Local TeX=papers/2405.11951/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Test F1 on ogbg-code2. |
| Cora | 1711.08920 | SplineCNN | 0.0618 | SOURCE-COMPATIBLE | Local TeX=papers/1711.08920/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Planetoid split (Yang et al. 2016 fixed 20-per-class train split). |
| Cora | 2412.04064 | GraphSAGE+CNA | 0.0228 | SOURCE-COMPATIBLE | Local TeX=papers/2412.04064/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Planetoid split (Yang et al. 2016 fixed 20-per-class train split). |
| Cora-CA | 2406.06642 | EDGNN | 0.0021 | SOURCE-PARTIAL | Local TeX=papers/2406.06642/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Test accuracy on real hypergraph dataset CORA-CA. |
| Cornell | 2106.10994 | BernNet | 0.0429 | SOURCE-COMPATIBLE | Local TeX=papers/2106.10994/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split for Cornell node classification. |
| Cornell | 2103.06064 | transparent GNN architecture | 0.0108 | SOURCE-COMPATIBLE | Local TeX=papers/2103.06064/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split and features provided by Pei et al. 2020 for heterophily datasets.. |
| D&D | 2309.00738 | GC-GNN (GraphSAGE) | 0.0807 | SOURCE-UNCLEAR | Local TeX=papers/2309.00738/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Accuracy reported for D&D dataset. |
| D&D | 1704.02901 | structure2vec | 0.0252 | SOURCE-UNCLEAR | Local TeX=papers/1704.02901/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=10-fold CV. |
| DBLP | 1912.10832 | HERec | 0.1773 | SOURCE-COMPATIBLE | Local TeX=papers/1912.10832/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Paper classification task on DBLP. |
| ENZYMES | 1906.01277 | WWL | 0.1142 | SOURCE-COMPATIBLE | Local TeX=papers/1906.01277/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=10-fold CV on continuous node/edge attributes. |
| ENZYMES | 2002.09518 | GMN | 0.0541 | COMPATIBLE | The source reports mean accuracy over 10-fold cross-validation for binary graph datasets including ENZYMES. |
| ER graph | 2402.16029 | GraphWiz (LLaMA 2-13B) | 0.4965 | SOURCE-PARTIAL | Local TeX=papers/2402.16029/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Evaluated on GraphInstruct test set which uses ER graphs.. |
| ER graph | 2505.11298 | F_4-MPNN | 0.0318 | COMPATIBLE | The source evaluates graph labels derived from cycle counts with graph classification and 10-fold evaluation. The database description says node classification, which is a metadata-description error, not a result-task mismatch; expanded.tex:779, 798-800. |
| FB15k-237 | 2210.02636 | GDGNN-Vert | 0.61 | MISMATCH | The source table reports inductive Hit@10 percentages, while the stored row is labeled MRR; expanded.tex:229-253. |
| FB15k-237 | 1911.03082 | CompGCN | 0.017 | SOURCE-COMPATIBLE | Local TeX=papers/1911.03082/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Toutanova & Chen 2015 split; filtered setting. |
| Film | 2503.12563 | DoG (ACM-GCN) | 0.0404 | SOURCE-PARTIAL | Local TeX=papers/2503.12563/latex/expanded.tex; evidence flags DTmP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split for heterophilic node classification as per canonical setup for Film.. |
| Film | 2307.16092 | ADR-GNN_S | 0.0126 | SOURCE-COMPATIBLE | Local TeX=papers/2307.16092/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=10 fixed splits as per Geom-GCN protocol. |
| FreeSolv | 2109.11730 | GeomGCL | 1.16 | SOURCE-PARTIAL | Local TeX=papers/2109.11730/latex/expanded.tex; evidence flags DTMp (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=Scaffold split. |
| FreeSolv | 2312.07633 | SE(3)-I MPPH | 0.187 | SOURCE-COMPATIBLE | Local TeX=papers/2312.07633/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=Scaffold split (80/10/10) as per MoleculeNet/OGB convention mentioned in text. |
| Freebase | 2403.04780 | MuseGraph (LLaMA3-8B) | 0.056 | SOURCE-COMPATIBLE | Local TeX=papers/2403.04780/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Heterogeneous Node Classification on Freebase. |
| Freebase | 2404.02810 | GC-HGNN | 0.0285 | SOURCE-COMPATIBLE | Local TeX=papers/2404.02810/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification on Freebase using features and structure. |
| IMDB | 2208.06129 | MHGCN | 0.0434 | SOURCE-COMPATIBLE | Local TeX=papers/2208.06129/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification on IMDB. |
| IMDB | 2210.05920 | GAT BGNN(m)-SC | 0.0313 | SOURCE-PARTIAL | Local TeX=papers/2210.05920/latex/expanded.tex; evidence flags DTmP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification task on IMDB dataset. |
| IMDB-BINARY | 1810.00826 | GIN-0 | 0.0341 | COMPATIBLE | The source reports 10-fold cross-validation for graph classification, matching the IMDB-BINARY variant; expanded.tex: dataset and evaluation sections. |
| IMDB-BINARY | 2005.01214 | GNTK | 0.018 | SOURCE-COMPATIBLE | Local TeX=papers/2005.01214/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=One run of stratified 10-folds CV. |
| IMDB-MULTI | 2206.02059 | GraphSNN | 0.251 | COMPATIBLE | The source reports 10-fold cross-validation accuracy for the TU graph classification protocol. |
| IMDB-MULTI | 2005.01214 | GNTK | 0.043 | SOURCE-COMPATIBLE | Local TeX=papers/2005.01214/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=One run of stratified 10-folds CV. |
| MD17 | 2304.04757 | GemNet (T/Q) | 1.039 | INVALID | The stored -1.0 is the source table dash for an unreported GemNet energy value, not a measured MAE; the source separates force and energy tables; expanded.tex:416-446, 769-779. |
| MD17 | 2210.16518 | ViSNet | 0.001 | SOURCE-COMPATIBLE | Local TeX=papers/2210.16518/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=Force MAE for Naphthalene. |
| MUTAG | 1605.05273 | PSCN k=10E | 0.0683 | SOURCE-COMPATIBLE | Local TeX=papers/1605.05273/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Standard accuracy for MUTAG graph classification. |
| MUTAG | 2006.02587 | GCN | 0.024 | MISMATCH | The source explicitly labels the extracted 0.963 as training accuracy for an interpretation model, not held-out benchmark accuracy; expanded.tex:417-426. |
| MalNet-Tiny | 2505.11356 | GCN | 0.0009 | SOURCE-COMPATIBLE | Local TeX=papers/2505.11356/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Published results for MalNet-Tiny. |
| Minesweeper | 2403.01232 | Polynormer-r | 0.0196 | SOURCE-COMPATIBLE | Local TeX=papers/2403.01232/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Averaged results over 10 runs on heterophilic datasets. |
| Minesweeper | 2305.16780 | CDE-GRAND-GAT | 0.0147 | SOURCE-COMPATIBLE | Local TeX=papers/2305.16780/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=ROC-AUC on Minesweeper. |
| NCI1 | 2312.10943 | MSA-AUD | 0.098 | SOURCE-COMPATIBLE | Local TeX=papers/2312.10943/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=10-fold CV. |
| NCI1 | 2210.01906 | FGW | 0.003 | SOURCE-COMPATIBLE | Local TeX=papers/2210.01906/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Performances taken from original paper.. |
| PATTERN | 2303.00579 | DeepGraph (48) | 0.039 | SOURCE-COMPATIBLE | Local TeX=papers/2303.00579/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification task on PATTERN dataset. |
| PATTERN | 2010.05421 | FactorGCN | 0.0202 | SOURCE-COMPATIBLE | Local TeX=papers/2010.05421/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=10-fold evaluation protocol as used in [xu2018powerful]. |
| PCQM-Contact | 2411.12732 | Exphormer + LapPE | 0.1024 | SOURCE-PARTIAL | Local TeX=papers/2411.12732/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard split for PCQM-Contact. |
| PCQM-Contact | 2406.12059 | Exphormer | 0.0287 | SOURCE-PARTIAL | Local TeX=papers/2406.12059/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard MRR metric for PCQM-Contact link prediction task.. |
| PCQM4Mv2 | 2201.12787 | EGT-Large | 0.0333 | SOURCE-COMPATIBLE | Local TeX=papers/2201.12787/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=Test-dev split for PCQM4Mv2. |
| PCQM4Mv2 | 2212.02229 | All (Ensemble) | 0.015 | VARIANT | The result is the OGB-LSC test-challenge competition split and should not be merged with test-dev rows; expanded.tex:143, 159, 186, 586. |
| PPI | 1803.07294 | GaAN | 0.3371 | SOURCE-COMPATIBLE | Local TeX=papers/1803.07294/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Inductive node classification on PPI split as described in setup (20 train, 2 val, 2 test sub-graphs).. |
| PPI | 1802.08888 | N-SAGE | 0.038 | SOURCE-COMPATIBLE | Local TeX=papers/1802.08888/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=PPI multi-class node classification using the split from sage. |
| PROTEINS | 1905.11577 | lapool | 0.0657 | COMPATIBLE | The source explicitly reports best accuracy on 10-fold cross-validation for PROTEINS. |
| PROTEINS | 1904.05003 | SAGE | 0.0086 | SOURCE-PARTIAL | Local TeX=papers/1904.05003/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=10-fold CV. |
| PascalVOC-SP | 2411.12732 | GCN | 0.3323 | SOURCE-COMPATIBLE | Local TeX=papers/2411.12732/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=LRGB evaluation protocol. |
| PascalVOC-SP | 2310.07430 | Graph-Mamba | 0.0631 | SOURCE-UNCLEAR | Local TeX=papers/2310.07430/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=LRGB benchmark node classification task. |
| Penn94 | 2303.06344 | GloGNN | 0.0074 | SOURCE-COMPATIBLE | Local TeX=papers/2303.06344/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard heterophily benchmark task and split.. |
| Penn94 | 2405.16185 | DC-GNN | 0.0061 | SOURCE-COMPATIBLE | Local TeX=papers/2405.16185/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on Penn94. |
| Peptides-func | 2310.07430 | NBA-GCN+LapPE | 0.039 | SOURCE-UNCLEAR | Local TeX=papers/2310.07430/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=LRGB benchmark standard split. |
| Peptides-func | 2302.08647 | MGT+WavePE | 0.0378 | SOURCE-COMPATIBLE | Local TeX=papers/2302.08647/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Standard split as per Peptides-func evaluation settings in [long_range]. |
| Peptides-struct | 2302.08647 | MGT+WavePE | 0.0076 | SOURCE-COMPATIBLE | Local TeX=papers/2302.08647/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=Standard split as per Peptides-struct evaluation settings in [long_range]. |
| Peptides-struct | 2310.07430 | NBA-GIN+LapPE | 0.0029 | SOURCE-UNCLEAR | Local TeX=papers/2310.07430/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=LRGB benchmark standard split. |
| Pokec | 2403.01232 | Polynormer-r | 0.0308 | SOURCE-COMPATIBLE | Local TeX=papers/2403.01232/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Polynormer with ReLU activation.. |
| Pokec | 2311.05185 | MoE-H2GCN | 0.0069 | SOURCE-COMPATIBLE | Local TeX=papers/2311.05185/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification split as per LinkX protocol.. |
| PubMed | 2002.06755 | GCN-LPA | 0.067 | SOURCE-COMPATIBLE | Local TeX=papers/2002.06755/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Planetoid split (Yang et al. 2016 fixed split). |
| PubMed | 2308.07134 | Flan-T5-large | 0.0222 | SOURCE-COMPATIBLE | Local TeX=papers/2308.07134/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Planetoid split (Yang et al. 2016). |
| Questions | 2405.20445 | MLP | 0.0006 | SOURCE-PARTIAL | Local TeX=papers/2405.20445/latex/expanded.tex; evidence flags DtmP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split (50/25/25) as defined in Table 3. |
| RDT-B | 2006.09963 | GCC (MoCo, freeze) | 0.088 | EXTERNAL | The task and graph-classification benchmark match, but the GCC driver uses graph pretraining/external data; it is not a clean from-scratch comparison. |
| RDT-B | 2009.03294 | GraphNorm | 0.037 | SOURCE-COMPATIBLE | Local TeX=papers/2009.03294/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Test accuracy on RDT-B graph classification. |
| REDDIT-BINARY | 2210.11790 | Last layer FA | 0.015 | SOURCE-COMPATIBLE | Local TeX=papers/2210.11790/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=10-fold CV. |
| REDDIT-BINARY | 2512.12642 | bnpool | 0.0078 | SOURCE-COMPATIBLE | Local TeX=papers/2512.12642/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Test accuracy on graph-level classification. |
| REDDIT-MULTI-5K | 2410.10365 | SpeGCL | 0.0184 | SOURCE-PARTIAL | Local TeX=papers/2410.10365/latex/expanded.tex; evidence flags DTMp (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Unsupervised learning on REDDIT-M-5K. |
| REDDIT-MULTI-5K | 2401.16011 | GIN | 0.001 | SOURCE-UNCLEAR | Local TeX=papers/2401.16011/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Averaged accuracy over five runs. |
| Reddit | 1803.07294 | GaAN | 0.0096 | SOURCE-COMPATIBLE | Local TeX=papers/1803.07294/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Inductive node classification on Reddit using maximum number sampling strategy with S1=25 and S2=10. |
| Reddit | 2104.09376 | SAGN+SLE | 0.003 | SOURCE-COMPATIBLE | Local TeX=papers/2104.09376/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Inductive node classification task on Reddit dataset. |
| Roman-empire | 2305.16780 | CDE-GRAND-GAT | 0.0241 | SOURCE-COMPATIBLE | Local TeX=papers/2305.16780/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on Roman-empire. |
| Roman-empire | 2604.08980 | Dir-NT | 0.0119 | SOURCE-PARTIAL | Local TeX=papers/2604.08980/latex/expanded.tex; evidence flags DTMp (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Averaged accuracy scores in 10 runs on heterophilic graphs.. |
| SIDER | 2604.16586 | KA-GAT | 0.137 | SOURCE-PARTIAL | Local TeX=papers/2604.16586/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=MoleculeNet SIDER task using scaffold split as per canonical definition. |
| SIDER | 2106.06130 | ChemRL-GEM | 0.0392 | SOURCE-PARTIAL | Local TeX=papers/2106.06130/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Scaffold split. |
| Squirrel | 2105.07634 | FSGNN | 0.151 | SOURCE-COMPATIBLE | Local TeX=papers/2105.07634/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Geom-GCN 10 fixed splits.. |
| Squirrel | 2412.04064 | Trans.Conv+CNA | 0.033 | SOURCE-COMPATIBLE | Local TeX=papers/2412.04064/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on Squirrel dataset.. |
| TSP | 2003.00982 | GatedGCN-E | 0.03 | SOURCE-COMPATIBLE | Local TeX=papers/2003.00982/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Test split results for edge classification task. |
| TSP | 2407.00696 | GIG-GatedGCN | 0.025 | SOURCE-COMPATIBLE | Local TeX=papers/2407.00696/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Edge classification task on TSP dataset. |
| Texas | 2106.10994 | BernNet | 0.0582 | SOURCE-COMPATIBLE | Local TeX=papers/2106.10994/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Mean accuracy reported for Texas node classification task.. |
| Texas | 2105.07634 | FSGNN | 0.019 | SOURCE-COMPATIBLE | Local TeX=papers/2105.07634/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Geom-GCN 10 fixed splits; results typically averaged.. |
| Tolokers | 2403.01232 | Polynormer-r | 0.0108 | SOURCE-COMPATIBLE | Local TeX=papers/2403.01232/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Averaged results over 10 runs on heterophilic datasets. |
| Tox21 | 2011.15069 | HIMP | 0.0398 | SOURCE-PARTIAL | Local TeX=papers/2011.15069/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Test split performance for Tox21 graph classification. |
| ToxCast | 2311.04837 | SCI | 0.0443 | SOURCE-PARTIAL | Local TeX=papers/2311.04837/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=ROC-AUC on OGB classification task. |
| ToxCast | 2109.11730 | GeomGCL | 0.014 | SOURCE-PARTIAL | Local TeX=papers/2109.11730/latex/expanded.tex; evidence flags DTMp (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Standard classification task on ToxCast dataset. Uses 2D-3D geometric contrastive learning (unlabeled data) fo. |
| WN18 | 1902.10197 | RotatE | 0.008 | SOURCE-COMPATIBLE | Local TeX=papers/1902.10197/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard link prediction task on WN18 split. |
| WN18 | 1703.06103 | ComplEx | 0.003 | SOURCE-COMPATIBLE | Local TeX=papers/1703.06103/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Filtered MRR on WN18 standard split. |
| WN18RR | 2210.02636 | GDGNN-Hor | 0.447 | MISMATCH | The source v1 table reports inductive Hit@10 percentages, while the stored row is labeled MRR; the separate transductive MRR table has different values; expanded.tex:229-253, 517-532. |
| WN18RR | 2009.14332 | MAGNA + DistMult | 0.023 | SOURCE-COMPATIBLE | Local TeX=papers/2009.14332/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard link prediction task on WN18RR split. |
| WikiCS | 2204.04874 | GCN | 0.1288 | SOURCE-COMPATIBLE | Local TeX=papers/2204.04874/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification on WikiCS. |
| WikiCS | 2102.06514 | GRACE | 0.003 | SOURCE-PARTIAL | Local TeX=papers/2102.06514/latex/expanded.tex; evidence flags DTmP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Transductive node classification using linear evaluation on frozen embeddings.. |
| Wisconsin | 2504.19785 | ACM-GCN | 0.0521 | SOURCE-COMPATIBLE | Local TeX=papers/2504.19785/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Comparison with other heterophily-aware GNNs. |
| Wisconsin | 2404.17099 | F-GREAD-BS | 0.0118 | SOURCE-PARTIAL | Local TeX=papers/2404.17099/latex/expanded.tex; evidence flags DTMp (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification accuracy on heterophilic datasets using standard splits.. |
| ZINC | 2012.09699 | GatedGCN | 1.152 | SOURCE-COMPATIBLE | Local TeX=papers/2012.09699/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=Baseline from dwivedi2020benchmarking. |
| ZINC | 2201.09332 | FeTA + GCKN + 3RW | 0.146 | SOURCE-PARTIAL | Local TeX=papers/2201.09332/latex/expanded.tex; evidence flags DTMp (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_regression; note=Standard graph regression task on ZINC. |
| arxiv-year | 2506.08298 | H^2GFM | 0.1979 | MISMATCH | The extracted 0.8561 is the He_Arxiv co-training result. The source distinguishes Arxiv from He_Arxiv and reports the value in the He_Arxiv CT table; expanded.tex:337-342, 366-390, 519-527. |
| arxiv-year | 2210.00513 | G^2-GraphSAGE | 0.073 | SOURCE-PARTIAL | Local TeX=papers/2210.00513/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on arXiv-year dataset.. |
| ogbg-molhiv | 2210.08443 | CLEAR | 0.1567 | SOURCE-COMPATIBLE | Local TeX=papers/2210.08443/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Official OGB scaffold split for ogbg-molhiv. |
| ogbg-molhiv | 2205.11678 | HIG with DeeperGCN | 0.0264 | SOURCE-UNCLEAR | Local TeX=papers/2205.11678/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Average performance and std. across 10 random seeds for Molhiv. |
| ogbg-molpcba | 2201.12787 | GRPE-Large | 0.0203 | SOURCE-COMPATIBLE | Local TeX=papers/2201.12787/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=OGB scaffold split; AP is averaged across all 128 tasks.. |
| ogbg-molpcba | 2205.11678 | HIG with Graphormer | 0.0017 | SOURCE-UNCLEAR | Local TeX=papers/2205.11678/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Teacher results taken from OGB Leaderboards; reported as average across 10 seeds.. |
| ogbg-ppa | 2103.16584 | DeeperGCN+FLAG | 0.0554 | SOURCE-COMPATIBLE | Local TeX=papers/2103.16584/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=OGB species split. |
| ogbg-ppa | 2305.06102 | GPS | 0.0215 | SOURCE-COMPATIBLE | Local TeX=papers/2305.06102/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=graph_classification; note=Default OGB split. |
| ogbl-citation2 | 2202.13538 | SUREL | 0.0207 | SOURCE-UNCLEAR | Local TeX=papers/2202.13538/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard link prediction task on ogbl-citation2 using MRR metric.. |
| ogbl-citation2 | 2309.00976 | MPLP | 0.0098 | SOURCE-UNCLEAR | Local TeX=papers/2309.00976/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard attributed benchmark evaluation. |
| ogbl-collab | 2010.16103 | SEAL | 0.1254 | SOURCE-COMPATIBLE | Local TeX=papers/2010.16103/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=OGB link prediction standard test split. |
| ogbl-collab | 2410.01802 | PROXI | 0.0986 | SOURCE-COMPATIBLE | Local TeX=papers/2410.01802/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard OGB split for link prediction. |
| ogbl-ddi | 2012.15024 | MPNNs | 0.3308 | SOURCE-COMPATIBLE | Local TeX=papers/2012.15024/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Official OGB link prediction split. |
| ogbl-ddi | 2310.14166 | ELGNN | 0.0239 | SOURCE-COMPATIBLE | Local TeX=papers/2310.14166/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=OGB official split for ogbl-ddi. |
| ogbl-ppa | 2010.16103 | SEAL | 0.146 | SOURCE-COMPATIBLE | Local TeX=papers/2010.16103/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=OGB link prediction test split. |
| ogbl-ppa | 2302.00890 | NCNC | 0.0819 | SOURCE-PARTIAL | Local TeX=papers/2302.00890/latex/expanded.tex; evidence flags DTmP (D=dataset, T=task, M=metric, P=protocol). Stored task=link_prediction; note=Standard link prediction task on ogbl-ppa. |
| ogbl-wikikg2 | 2307.01026 | NAT | 0.02 | MISMATCH | The source is TGB tgbl-wiki temporal link property prediction, not OGB ogbl-wikikg2; it uses a chronological split and dynamic destination prediction; expanded.tex:94-99, 529-533, 700-706. |
| ogbn-arxiv | 2111.00064 | GIANT-XRT | 0.0271 | SOURCE-COMPATIBLE | Local TeX=papers/2111.00064/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=OGB official split. |
| ogbn-arxiv | 2309.14907 | REVGAT with X_LD | 0.0114 | SOURCE-COMPATIBLE | Local TeX=papers/2309.14907/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=OGB official split (test set). |
| ogbn-mag | 2104.09376 | NARS_SAGN+0-SLE | 0.063 | SOURCE-COMPATIBLE | Local TeX=papers/2104.09376/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Test accuracy on ogbn-mag. |
| ogbn-mag | 2108.10097 | NARS-GAMLP+RLU | 0.015 | SOURCE-PARTIAL | Local TeX=papers/2108.10097/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=ogbn-mag test split. |
| ogbn-papers100M | 2403.13268 | SGC | 0.0874 | SOURCE-UNCLEAR | Local TeX=papers/2403.13268/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on ogbn-papers100m as per dataset statistics.. |
| ogbn-papers100M | 2104.09376 | SAGN+SLE | 0.0289 | SOURCE-COMPATIBLE | Local TeX=papers/2104.09376/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Test accuracy on ogbn-papers100M split; uses label information. |
| ogbn-products | 2009.03509 | UniMP | 0.0348 | SOURCE-COMPATIBLE | Local TeX=papers/2009.03509/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=OGB standard split for ogbn-products node classification. |
| ogbn-products | 2010.13993 | FDiff-scale (MLP) | 0.0199 | SOURCE-UNCLEAR | Local TeX=papers/2010.13993/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Uses both train and validation labels. |
| ogbn-proteins | 2009.03509 | UniMP | 0.0416 | SOURCE-COMPATIBLE | Local TeX=papers/2009.03509/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=OGB standard split for ogbn-proteins node classification. |
| ogbn-proteins | 2309.14907 | X_LD | 0.03 | SOURCE-UNCLEAR | Local TeX=papers/2309.14907/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard test split for ogbn-protein node classification. |
| snap-patents | 2210.00513 | G^2-GraphSAGE | 0.187 | SOURCE-PARTIAL | Local TeX=papers/2210.00513/latex/expanded.tex; evidence flags DtMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on snap-patents. |
| snap-patents | 2310.02232 | FaberNet | 0.0378 | SOURCE-COMPATIBLE | Local TeX=papers/2310.02232/latex/expanded.tex; evidence flags DTMP (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard split as provided in lim2021large. |
| twitch-gamers | 2505.14033 | CPF | 0.0277 | SOURCE-UNCLEAR | Local TeX=papers/2505.14033/latex/expanded.tex; evidence flags NO-DATASET (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Node classification on heterophilic graphs. |
| twitch-gamers | 2303.06344 | HLCL | 0.0074 | SOURCE-PARTIAL | Local TeX=papers/2303.06344/latex/expanded.tex; evidence flags DTMp (D=dataset, T=task, M=metric, P=protocol). Stored task=node_classification; note=Standard node classification task on heterophily dataset. |

## Confirmed and high-priority findings

| Dataset / paper | Finding | Action implied by audit |
|---|---|---|
| Amazon-ratings / 2407.14732 | MISMATCH: source has Amazon-Clothing and Amazon-Electronics few-shot tables, not Amazon-ratings. The 0.822 row is not the canonical full-task benchmark. | Exclude the row/paper from canonical Amazon-ratings comparison and fix dataset mapping. |
| Amazon-ratings / 2502.04591 | MISMATCH: 0.8562 is the accuracy ratio from an oversmoothing correlation table, not test accuracy. | Exclude the row from the leaderboard and add a guard against auxiliary ratios/correlations being parsed as the primary metric. |
| arxiv-year / 2506.08298 | MISMATCH: 0.8561 comes from He_Arxiv co-training. He_Arxiv is a heterogeneous text-attributed graph, not the canonical arxiv-year/OGB-Arxiv dataset. | Exclude from arxiv-year; retain only under a correctly canonicalized dataset if one exists. |
| ogbl-wikikg2 / 2307.01026 | MISMATCH: source is TGB `tgbl-wiki`, a temporal destination-prediction task with chronological evaluation, not OGB `ogbl-wikikg2`. | Exclude from ogbl-wikikg2 and create/use a temporal TGB dataset entry if desired. |
| FB15k-237 and WN18RR / 2210.02636 | MISMATCH: the extracted rows use inductive Hit@10 percentages but are stored as MRR; the source's separate transductive MRR table is not the source of these values. | Remove these rows or correct their metrics and variants before comparing link-prediction SOTA. |
| MD17 / 2304.04757 | INVALID VALUE: -1.0 is extraction of a source dash for an unreported GemNet energy value. It is not an MAE and artificially creates a huge lower-is-better jump. | Delete or mark the result problematic; never allow sentinel values into SOTA. |
| MUTAG / 2006.02587 | MISMATCH: the 0.963 value is training accuracy for an explanation model, not test-set graph-classification accuracy. | Remove the row from MUTAG SOTA. |
| PCQM4Mv2 / 2212.02229 | VARIANT MISMATCH: 0.0722 is test-challenge competition performance, while other rows use test-dev. | Separate test-dev and test-challenge variants before comparing. |
| BBBP / 2106.04509 | PROTOCOL CAVEAT: 0.911 is linear evaluation of pretrained representations, not the ordinary supervised scaffold comparison. | Exclude from the canonical leaderboard or place in an explicitly separate linear-probe variant. |
| RDT-B / 2006.09963 | EXTERNAL-DATA CAVEAT: GCC uses graph pretraining; the task and dataset match, but it is not a clean from-scratch result. | Retain only if external pretraining is allowed and visibly mark provenance. |
| ClinTox / 2106.05819 | EXTERNAL-DATA CAVEAT: the downstream task matches, but the driver uses ZINC-2M pretraining. | Retain only with external-pretraining provenance or separate comparisons. |
| BA graph and ER graph / 2505.11298 | TASK MATCH: source uses graph labels based on cycle counts and graph classification with 10-fold evaluation. The database descriptions incorrectly say node classification. | Correct dataset descriptions; do not remove the result on task grounds. |
| Amazon-Computers / 2112.14531; Amazon-Computers and Amazon-Photo / 2205.11172 | VALID PROTOCOL: local sources explicitly use 60/20/20 for these Amazon node-classification datasets; this is not the Geom-GCN-only setup used for Actor/Wisconsin. | Retain; do not apply the Wisconsin protocol rule to Amazon datasets. |

## Remediation applied

- Added curation exclusions for the confirmed task, metric, split, missing-value, and provenance mismatches listed above.
- Removed **54** matching legacy result rows from the database and regenerated the comparison exports.
- Corrected the BA graph and ER graph descriptions from node classification to graph classification.
- Added parser/prompt guards against negative error sentinels, out-of-range accuracy-like values, training/validation metrics, auxiliary ratios, correlation diagnostics, and missing table cells.
- Generated `config/re_evaluate_sota_drivers.txt` and marked **121** unique audited driver papers manually important and pending for forced re-evaluation.
- Re-evaluation command: `uv run python scripts/mark_reextract_papers.py mark-list --file config/re_evaluate_sota_drivers.txt --yes --requeue --reason dataset_sota_concentration_audit`.

### Detection-gap analysis

| Failure | Underlying cause | Should the old pipeline have caught it? | Permanent guard |
|---|---|---|---|
| Amazon-ratings / 2407.14732 | Few-shot Amazon-Clothing/Electronics tables were mapped into the canonical dataset comparison. | Yes. The row carried a few-shot/nonstandard note, but the old protocol cue list did not cover every few-shot formulation and dataset resolution was too permissive. | Broader nonstandard cues, ambiguous-name protection, and the paper/dataset exclusion. |
| Amazon-ratings / 2502.04591 | The model returned an `Accuracy ratio` column as `Accuracy`; the note explicitly described the ratio and correlation table. | No, not with the old rules: `accuracy ratio` and correlation evidence were not protocol-invalidating cues. | Metric-column evidence requirement, auxiliary-diagnostic caption rejection, and ratio/correlation cue detection. |
| arxiv-year / 2506.08298 | Heterogeneous `He_Arxiv` was confused with canonical arxiv-year/Arxiv during fuzzy resolution. | Partly. The task was node classification, but dataset identity was wrong; the old resolver had no protected `He_*` names. | Ambiguous heterogeneous-Arxiv names are never fuzzy-matched; arxiv-year contracts reject He-Arxiv/co-training evidence. |
| ogbl-wikikg2 / 2307.01026 | Temporal `tgbl-wiki` was treated as an OGB link-prediction dataset. | No. OGB family protection did not distinguish temporal TGB (`tgbl`) from OGB link datasets (`ogbl`), and the old protocol cues did not recognize TGB/chronological destination prediction. | Temporal-TGB versus OGB link-family fuzzy matching and TGB/chronological protocol cues are blocked. |
| FB15k-237/WN18RR / 2210.02636 | Inductive Hit@10 percentage columns were labeled MRR; the separate transductive MRR table was not selected. | Partly. The old protocol path validated task/split but did not validate the metric named in the row-local evidence. | `MRR` plus Hit@K evidence is rejected, and prompts now require the exact metric column in `protocol_note`. |
| MUTAG / 2006.02587 | Training accuracy of the interpreted GCN was treated as benchmark test accuracy. | No. The old cue list did not recognize `training accuracy` when the metric field was simply `Accuracy`. | Training/validation accuracy cues and metric normalization reject non-test metrics. |
| MD17 / 2304.04757 | A source dash for an unreported value became numeric `-1.0`. | The parser rejected textual dashes, but did not reject numeric negative sentinels for nonnegative error metrics. | Negative MAE/RMSE/MSE/error/loss values are invalid. |
| PCQM4Mv2 / 2212.02229 | Test-challenge competition results were conflated with test-dev under one standard variant. | Partly. The old protocol note could mark validation rows nonstandard, but there was no persistent test-challenge variant for explicit routing. | A nonstandard `Test challenge` variant and challenge-cue resolver routing. |

## Coverage and limitations

- The concentration detector intentionally produces broad candidates; concentration alone is not evidence of contamination.
- A large jump can be caused by a new task, split, pretraining regime, or a copied/mis-mapped row. The source audit separates these cases.
- The current database has 142 standard variants, but 26 datasets have no eligible primary-metric rows under the stated filters and therefore cannot support a SOTA-gap conclusion.
- The audit was generated before remediation; the remediation counts above are from the subsequent cleanup run.
