#!/usr/bin/env uv run python3
"""Build config/arxiv_ids.csv and config/arxiv_ids.txt from all OGB leaderboards."""
from __future__ import annotations

import csv
import json
import os
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config"
ENV_FILE = ROOT / ".env"

# Load .env
if ENV_FILE.exists():
    for line in ENV_FILE.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ[k.strip()] = v.strip()

API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
HEADERS = {"x-api-key": API_KEY} if API_KEY else {}

# (method_name, datasets) — unique methods across all OGB leaderboards
METHODS: list[tuple[str, str]] = [
    # === Graph property prediction ===
    ("Multi-RF Fusion + Multi-GNN", "ogbg-molhiv"),
    ("HyperFusion", "ogbg-molhiv,ogbg-molpcba,ogbl-collab,ogbl-ddi"),
    ("PAS+FPs", "ogbg-molhiv"),
    ("HIG", "ogbg-molhiv"),
    ("HIG(pre-trained on PCQM4M)", "ogbg-molpcba"),
    ("DeepAUC", "ogbg-molhiv"),
    ("FingerPrint+GMAN", "ogbg-molhiv"),
    ("Neural FingerPrints", "ogbg-molhiv"),
    ("Graphormer + FPs", "ogbg-molhiv"),
    ("Molecular FP + Random Forest", "ogbg-molhiv"),
    ("CIN", "ogbg-molhiv"),
    ("GSAT", "ogbg-molhiv"),
    ("MorganFP+Rand. Forest", "ogbg-molhiv,ogbg-molpcba"),
    ("CIN-small", "ogbg-molhiv"),
    ("Graphormer (pre-trained on PCQM4M)", "ogbg-molhiv,ogbg-molpcba"),
    ("GatedGCN+", "ogbg-molhiv,ogbg-molpcba,ogbg-ppa"),
    ("directional GSN", "ogbg-molhiv"),
    ("P-WL", "ogbg-molhiv"),
    ("DGN", "ogbg-molhiv,ogbg-molpcba"),
    ("DeeperGCN+FLAG", "ogbg-molhiv,ogbg-molpcba,ogbg-ppa,ogbn-products,ogbn-proteins,ogbn-arxiv"),
    ("PHC-GNN", "ogbg-molhiv,ogbg-molpcba"),
    ("GINE", "ogbg-molhiv"),
    ("GIN", "ogbg-molhiv,ogbg-molpcba,ogbg-ppa,ogbg-code2"),
    ("PNA", "ogbg-molhiv,ogbg-molpcba"),
    ("GINE+HE", "ogbg-molhiv"),
    ("GCN+GraphNorm", "ogbg-molhiv"),
    ("HIMP", "ogbg-molhiv"),
    (
        "DeeperGCN",
        "ogbg-molhiv,ogbg-molpcba,ogbg-ppa,ogbn-products,ogbn-proteins,ogbn-arxiv,ogbl-collab",
    ),
    ("EGC-M (No Edge Features)", "ogbg-molhiv,ogbg-code2"),
    ("GSN", "ogbg-molhiv"),
    ("WEGL", "ogbg-molhiv"),
    ("EGC-S (No Edge Features)", "ogbg-molhiv,ogbg-code2"),
    ("GCN (in Julia)", "ogbg-molhiv"),
    ("PDF", "ogbg-molpcba"),
    ("PAS", "ogbg-molpcba,ogbg-ppa"),
    ("Nested GIN+virtual node (ensemble)", "ogbg-molpcba"),
    ("GINE+bot", "ogbg-molpcba"),
    ("CRaWl", "ogbg-molpcba"),
    ("GINE+ w/ APPNP", "ogbg-molpcba"),
    ("GIN-AK", "ogbg-molpcba"),
    ("GINE+ w/ virtual nodes", "ogbg-molpcba"),
    ("RandomGIN-vn+FLAG", "ogbg-molpcba"),
    ("DeeperGCN+virtual node+FLAG", "ogbg-molpcba"),
    ("GIN+virtual node+FLAG", "ogbg-molpcba,ogbg-ppa"),
    ("DeeperGCN+virtual node", "ogbg-molpcba"),
    ("GIN+virtual node", "ogbg-molpcba,ogbg-ppa,ogbg-code2"),
    ("GCN+virtual node+FLAG", "ogbg-molpcba,ogbg-ppa"),
    ("GCN+virtual node", "ogbg-molpcba,ogbg-ppa,ogbg-code2"),
    ("GIN+FLAG", "ogbg-molpcba,ogbg-ppa"),
    ("ChebNet", "ogbg-molpcba"),
    ("GCN+FLAG", "ogbg-molpcba,ogbn-arxiv"),
    (
        "GCN",
        "ogbg-molpcba,ogbg-ppa,ogbg-code2,ogbn-products,ogbn-arxiv,ogbl-ppa,ogbl-collab,ogbl-ddi,ogbl-citation2,ogbl-vessel",
    ),
    ("PAS+F2GNN", "ogbg-ppa"),
    ("ExpC*+bag of tricks", "ogbg-ppa"),
    ("GIN+", "ogbg-ppa"),
    ("GCN+", "ogbg-ppa"),
    ("ExpC", "ogbg-ppa"),
    ("GC-T+MCL(6.0)", "ogbg-ppa"),
    ("SAT++ with Magnetic Laplacian", "ogbg-code2"),
    ("DAGformer", "ogbg-code2"),
    ("SAT", "ogbg-code2"),
    ("GraphTrans (GCN-Virtual)", "ogbg-code2"),
    ("GMAN+bag of tricks", "ogbg-code2"),
    ("DAGNN", "ogbg-code2,ogbn-arxiv"),
    ("GraphTrans (GCN)", "ogbg-code2"),
    ("GAT", "ogbg-code2,ogbn-proteins,ogbn-arxiv"),
    ("MPNN-Max (No Edge Features)", "ogbg-code2"),
    ("DiffPool w/ graphSAGE", "ogbg-code2"),
    ("Graphormer", "ogbg-molhiv"),
    ("GatedGCN", "ogbg-molhiv,ogbg-molpcba"),
    ("GraphTrans (GCN-Virtual)", "ogbg-code2"),
    ("FLAG", "ogbg-molhiv,ogbn-products,ogbn-proteins,ogbn-arxiv,ogbn-mag"),
    (
        "GraphSAGE",
        "ogbg-code2,ogbn-products,ogbn-proteins,ogbn-arxiv,ogbl-ppa,ogbl-collab,ogbl-ddi,ogbl-citation2,ogbl-vessel",
    ),
    ("DiffPool", "ogbg-code2"),
    # === Node property prediction ===
    ("GLEM+GIANT+SAGN+SCR", "ogbn-products"),
    ("LD+GIANT+SAGN+SCR", "ogbn-products"),
    ("GraDBERT+GIANT & SAGN+SLE+CnS", "ogbn-products"),
    ("GIANT-XRT+R-SAGN+SCR+C&S", "ogbn-products"),
    ("GIANT-XRT+SAGN+SCR+C&S", "ogbn-products"),
    ("GIANT-XRT+SAGN+MCR+C&S", "ogbn-products"),
    ("GIANT-XRT+SAGN+SCR", "ogbn-products"),
    ("GIANT-XRT+SAGN+MCR", "ogbn-products"),
    ("LD+GAMLP", "ogbn-products"),
    ("GIANT-XRT+SAGN+SLE+C&S (use raw text)", "ogbn-products"),
    ("GIANT-XRT+SAGN+SLE (use raw text)", "ogbn-products"),
    ("GIANT-XRT+GAMLP+MCR", "ogbn-products"),
    ("GAMLP+RLU+SCR+C&S", "ogbn-products,ogbn-papers100M,ogbn-mag"),
    ("GAMLP+RLU+SCR", "ogbn-products,ogbn-papers100M"),
    ("SAGN+SLE (4 stages)+C&S", "ogbn-products,ogbn-papers100M"),
    ("SAGN+SLE (4 stages)", "ogbn-products,ogbn-papers100M"),
    ("GAMLP+MCR", "ogbn-products"),
    ("GAMLP+RLU", "ogbn-products,ogbn-papers100M,ogbn-mag"),
    ("Spec-MLP-Wide + C&S", "ogbn-products"),
    ("SAGN+MCR", "ogbn-products"),
    ("SAGN+SLE", "ogbn-products,ogbn-papers100M,ogbn-mag"),
    ("MLP + C&S", "ogbn-products,ogbn-arxiv"),
    ("GIANT-XRT+GraphSAINT(use raw text)", "ogbn-products"),
    ("Polynormer", "ogbn-products,ogbn-arxiv"),
    ("GAMLP", "ogbn-products,ogbn-papers100M,ogbn-mag"),
    ("AGDN", "ogbn-products,ogbn-proteins,ogbn-arxiv,ogbl-ppa,ogbl-ddi,ogbl-citation2"),
    ("RevGNN-112", "ogbn-products"),
    ("Linear + C&S", "ogbn-products,ogbn-arxiv"),
    ("UniMP", "ogbn-products,ogbn-proteins,ogbn-arxiv"),
    ("Plain Linear + C&S", "ogbn-products,ogbn-arxiv"),
    ("GAT+FLAG", "ogbn-products,ogbn-arxiv"),
    ("GraphSAGE + C&S + node2vec", "ogbn-products"),
    ("SAGN", "ogbn-products,ogbn-papers100M,ogbn-mag"),
    ("PCAPass + XGBoost", "ogbn-products,ogbn-arxiv"),
    ("E2EG (use raw text)", "ogbn-products,ogbn-arxiv"),
    ("GAT w/NS + C&S", "ogbn-products"),
    ("SIGN", "ogbn-products,ogbn-arxiv,ogbn-papers100M,ogbn-mag"),
    ("GIANT-XRT+MLP (use raw text)", "ogbn-products,ogbn-arxiv"),
    ("GraphSAGE w/NS + C&S", "ogbn-products"),
    ("GraphSAINT-inductive", "ogbn-products"),
    ("ClusterGCN+residual+3 layers", "ogbn-products"),
    ("GAT with NeighborSampling", "ogbn-products"),
    ("GraphSAGE+FLAG", "ogbn-products,ogbn-arxiv"),
    ("Cluster-GAT", "ogbn-products"),
    ("GraphSAINT (SAGE aggr)", "ogbn-products"),
    ("ClusterGCN (SAGE aggr)", "ogbn-products"),
    ("NeighborSampling (SAGE aggr)", "ogbn-products,ogbl-citation2"),
    ("Full-batch GraphSAGE", "ogbn-products"),
    ("TCNN", "ogbn-products"),
    ("Full-batch GCN", "ogbn-products,ogbl-citation2"),
    ("GraphZoom (Node2vec)", "ogbn-products,ogbn-arxiv"),
    (
        "Node2vec",
        "ogbn-products,ogbn-proteins,ogbn-arxiv,ogbn-papers100M,ogbl-ppa,ogbl-collab,ogbl-ddi,ogbl-citation2",
    ),
    ("CoLinkDistMLP", "ogbn-products,ogbn-arxiv,ogbn-mag"),
    ("MLP+FLAG", "ogbn-products,ogbn-arxiv"),
    ("MLP", "ogbn-products,ogbn-proteins,ogbn-arxiv,ogbn-papers100M,ogbn-mag,ogbl-vessel"),
    ("LD+GAT", "ogbn-proteins"),
    ("GIPA(Wide&Deep)", "ogbn-proteins"),
    ("RevGNN-Wide", "ogbn-proteins"),
    ("GAT+BOT+NGNN", "ogbn-proteins"),
    ("RevGNN-Deep", "ogbn-proteins"),
    ("GAT+BoT", "ogbn-proteins"),
    ("GAT + labels + node2vec", "ogbn-proteins"),
    ("GIPA", "ogbn-proteins"),
    ("UniMP+CrossEdgeFeat", "ogbn-proteins"),
    ("GAT+EdgeFeatureAtt", "ogbn-proteins"),
    ("DeepGCN", "ogbn-proteins"),
    ("MWE-DGCN", "ogbn-proteins"),
    ("GEN + FLAG + node2vec", "ogbn-proteins"),
    ("DVCNN", "ogbn-proteins"),
    ("GeniePath-BS", "ogbn-proteins"),
    ("GaAN", "ogbn-proteins,ogbn-arxiv"),
    ("SimTeG+TAPE+RevGAT", "ogbn-arxiv"),
    ("TAPE+RevGAT", "ogbn-arxiv"),
    ("SimTeG+TAPE+GraphSAGE", "ogbn-arxiv"),
    ("LD+REVGAT", "ogbn-arxiv"),
    ("GraDBERT & RevGAT+KD", "ogbn-arxiv"),
    ("GLEM+RevGAT", "ogbn-arxiv"),
    ("GIANT-XRT+AGDN+BoT+self-KD", "ogbn-arxiv"),
    ("GIANT-XRT+RevGAT+KD+DCN", "ogbn-arxiv"),
    ("GIANT-XRT+R-RevGAT+KD", "ogbn-arxiv"),
    ("GIANT-XRT+DRGAT+KD", "ogbn-arxiv"),
    ("GIANT-XRT+AGDN+BoT", "ogbn-arxiv"),
    ("GIANT-XRT+RevGAT+KD (use raw text)", "ogbn-arxiv"),
    ("GIANT-XRT+DRGAT", "ogbn-arxiv"),
    ("GIANT-XRT+RevGAT (use raw text)", "ogbn-arxiv"),
    ("GIANT-XRT+LGGNN+LabelReuse+C&S", "ogbn-arxiv"),
    ("LGGNN+LabelReuse+C&S", "ogbn-arxiv"),
    ("SciBERT & EHGCN (use MAG data)", "ogbn-arxiv"),
    ("GIANT-XRT+GraphSAGE (use raw text)", "ogbn-arxiv"),
    ("AGDN+BoT+self-KD+C&S", "ogbn-arxiv"),
    ("AGDN+BoT+self-KD", "ogbn-arxiv"),
    ("RevGAT+N.Adj+LabelReuse+SelfKD", "ogbn-arxiv"),
    ("BiGTex+C&S", "ogbn-arxiv"),
    ("GAT-node2vec + BoT + self-KD", "ogbn-arxiv"),
    ("DRGAT", "ogbn-arxiv"),
    ("GAT+label reuse+self KD", "ogbn-arxiv"),
    ("AGDN+BoT", "ogbn-arxiv"),
    ("GIANT+XRT+GATv2", "ogbn-arxiv"),
    ("AGDN (GAT-HA+3_heads+labels)", "ogbn-arxiv"),
    ("UniMP_v2", "ogbn-arxiv"),
    ("GAT(norm.adj.)+label reuse+C&S", "ogbn-arxiv"),
    ("GAT+norm. adj.+label reuse", "ogbn-arxiv"),
    ("GAT + C&S", "ogbn-arxiv"),
    ("UniMP_large", "ogbn-arxiv"),
    ("AGDN (GAT-HA+3_heads)", "ogbn-arxiv"),
    ("LEGNN + AS-Train", "ogbn-arxiv,ogbn-mag"),
    ("BiGTex", "ogbn-arxiv"),
    ("GAT+norm. adj.+labels", "ogbn-arxiv"),
    ("GAT+norm.adj.+labels", "ogbn-arxiv"),
    ("GCN_res + C&S_v2", "ogbn-arxiv"),
    ("GCN+linear+labels", "ogbn-arxiv"),
    ("GCN_res + C&S", "ogbn-arxiv"),
    ("GTAN", "ogbn-arxiv"),
    ("GCN+residual+6 layers", "ogbn-arxiv"),
    ("GCN+residual+node2vec", "ogbn-arxiv"),
    ("GCN_res + 8 layers + FLAG", "ogbn-arxiv"),
    ("GCNII", "ogbn-arxiv"),
    ("GCN_res + 8 layers", "ogbn-arxiv"),
    ("GTCN", "ogbn-arxiv"),
    ("EGC-S (100k)", "ogbn-arxiv"),
    ("JKNet (GCN-based)", "ogbn-arxiv"),
    ("EGC-M (100k)", "ogbn-arxiv"),
    ("GLEM+GIANT+GAMLP", "ogbn-papers100M"),
    ("GIANT-XRT+GAMLP+RLU (use raw text)", "ogbn-papers100M"),
    ("GAMLP+SCR-m", "ogbn-papers100M"),
    ("GAMLP+SCR", "ogbn-papers100M"),
    ("FSGNN", "ogbn-papers100M"),
    ("TransformerConv", "ogbn-papers100M"),
    ("GraphSAGE_res_incep", "ogbn-papers100M"),
    ("SIGN-XL", "ogbn-papers100M"),
    ("PCAPass + LightGBM", "ogbn-papers100M"),
    ("SGC", "ogbn-papers100M,ogbl-vessel"),
    ("HGAMLP-HOPE", "ogbn-mag"),
    ("gHAWK(Bloom+TransE)", "ogbn-mag"),
    ("HGAMLP+LP+MS(LINE embs)", "ogbn-mag"),
    ("LMSPS (w/o embs)", "ogbn-mag"),
    ("RpHGNN+LP+CR (LINE embs)", "ogbn-mag"),
    ("PSHGCN", "ogbn-mag"),
    ("SeHGNN (ComplEx embs)", "ogbn-mag"),
    ("SeHGNN", "ogbn-mag"),
    ("NARS-GAMLP+RLU+SCR", "ogbn-mag"),
    ("NARS-GAMLP+RLU", "ogbn-mag"),
    ("NARS-GAMLP+SCR-m", "ogbn-mag"),
    ("NARS_SAGN+SLE", "ogbn-mag"),
    ("NARS-GAMLP+SCR", "ogbn-mag"),
    ("NARS-GAMLP", "ogbn-mag"),
    ("LEGNN", "ogbn-arxiv,ogbn-mag"),
    ("NARS", "ogbn-mag"),
    ("R-HGNN", "ogbn-mag"),
    ("R-GSN + metapath2vec", "ogbn-mag"),
    ("HGConv", "ogbn-mag"),
    ("R-GSN", "ogbn-mag"),
    ("HGT (TransE embs)", "ogbn-mag"),
    ("GraphSAINT + metapath2vec", "ogbn-mag"),
    ("HGT (LADIES Sample)", "ogbn-mag"),
    ("GraphSAINT (R-GCN aggr)", "ogbn-mag"),
    ("R-GCN+FLAG", "ogbn-mag"),
    ("NeighborSampling (R-GCN aggr)", "ogbn-mag"),
    ("Full-batch R-GCN", "ogbn-mag"),
    ("ClusterGCN (R-GCN aggr)", "ogbn-mag"),
    ("MetaPath2vec", "ogbn-mag"),
    # === Link property prediction ===
    ("GraphGPT(SMTP)", "ogbl-ppa,ogbl-citation2"),
    ("GraphGPT(d1n30)", "ogbl-citation2"),
    ("Refined-GAE", "ogbl-ppa,ogbl-collab,ogbl-ddi"),
    ("MPLP", "ogbl-ppa,ogbl-citation2"),
    ("GCN (node embedding)", "ogbl-ppa,ogbl-ddi"),
    ("SIEG", "ogbl-ppa,ogbl-citation2,ogbl-vessel"),
    ("Neural Common Neighbor", "ogbl-ppa"),
    ("NGNN + SEAL", "ogbl-ppa,ogbl-citation2"),
    ("SUREL+", "ogbl-ppa,ogbl-vessel"),
    ("SUREL", "ogbl-citation2"),
    ("RA+Edge Proposal Set", "ogbl-ppa"),
    ("MLP+CN&RA&AA", "ogbl-ppa"),
    ("BUDDY", "ogbl-ppa,ogbl-collab,ogbl-ddi,ogbl-citation2"),
    ("SEAL", "ogbl-ppa,ogbl-collab,ogbl-ddi,ogbl-citation2,ogbl-vessel"),
    ("S3GRL (PoS Plus)", "ogbl-ppa,ogbl-collab,ogbl-citation2,ogbl-vessel"),
    ("NGNN + GraphSAGE", "ogbl-ppa,ogbl-collab,ogbl-ddi"),
    ("NGNN + GCN", "ogbl-ppa,ogbl-collab,ogbl-ddi"),
    ("Matrix Factorization", "ogbl-ppa,ogbl-collab,ogbl-ddi,ogbl-citation2,ogbl-vessel"),
    ("DeepWalk", "ogbl-ppa,ogbl-collab,ogbl-ddi,ogbl-ddi"),
    ("GIDN@YITU", "ogbl-collab,ogbl-ddi"),
    ("PLNLP + SIGN", "ogbl-collab"),
    ("PLNLP (random walk aug.)", "ogbl-collab"),
    ("HOP-REC", "ogbl-collab"),
    ("PLNLP+ LRGA", "ogbl-collab"),
    ("PLNLP (val as input)", "ogbl-collab"),
    ("AA-DC", "ogbl-collab"),
    ("TopoLink", "ogbl-collab"),
    ("ELPH", "ogbl-collab,ogbl-ddi"),
    ("SEAL-nofeat (val as input)", "ogbl-collab"),
    ("SEAL-nofeat", "ogbl-collab"),
    ("GraphSAGE (val as input)", "ogbl-collab"),
    ("LRGA + GCN", "ogbl-collab,ogbl-ddi,ogbl-vessel"),
    ("ELGNN", "ogbl-ddi"),
    ("PSG", "ogbl-ddi"),
    ("PLNLP", "ogbl-ddi,ogbl-citation2"),
    ("GDNN", "ogbl-ddi"),
    ("GraphSAGE + Edge Attr", "ogbl-ddi"),
    ("CFLP (w/ JKNet)", "ogbl-ddi"),
    ("GraphSAGE+anchor distance", "ogbl-ddi"),
    ("NeuralCommonNeighbor", "ogbl-ddi"),
    ("DEA + JKNet", "ogbl-ddi"),
    ("GraphSAGE+Edge Proposal Set", "ogbl-ddi"),
    ("LRGA+GCN(Node2Vec+Augment)", "ogbl-ddi"),
    ("MAD Learning", "ogbl-ddi"),
    ("GCN+JKNet", "ogbl-ddi"),
    ("CFG", "ogbl-citation2"),
    ("GCN + Heuristic Encoding", "ogbl-citation2"),
    ("AGDN w/GraphSAINT", "ogbl-citation2"),
    ("HPE - Pre-trained Initialized", "ogbl-citation2"),
    ("ClusterGCN (GCN aggr)", "ogbl-citation2"),
    ("GraphSAINT (GCN aggr)", "ogbl-citation2"),
    ("RelEns", "ogbl-wikikg2,ogbl-biokg"),
    ("StarGraph + TripleRE + Text", "ogbl-wikikg2"),
    ("InterHT+", "ogbl-wikikg2"),
    ("StarGraph + TripleRE", "ogbl-wikikg2"),
    ("A*Net", "ogbl-wikikg2"),
    ("CompoundE3D", "ogbl-wikikg2"),
    ("TranS", "ogbl-wikikg2"),
    ("TripleRE + NodePiece", "ogbl-wikikg2"),
    ("InterHT", "ogbl-wikikg2"),
    ("ComplEx-RP (50dim)", "ogbl-wikikg2"),
    ("TransERR", "ogbl-wikikg2"),
    ("tripleRE", "ogbl-wikikg2"),
    ("NodePiece + AutoSF", "ogbl-wikikg2"),
    ("Rot-Pro", "ogbl-wikikg2"),
    ("AutoSF", "ogbl-wikikg2,ogbl-biokg"),
    ("PairRE (200dim)", "ogbl-wikikg2"),
    ("RotatE (250dim)", "ogbl-wikikg2,ogbl-biokg"),
    ("TransE (500dim)", "ogbl-wikikg2,ogbl-biokg"),
    ("ComplEx (250dim)", "ogbl-wikikg2"),
    ("ComplEx (50dim)", "ogbl-wikikg2"),
    ("DistMult (500dim)", "ogbl-wikikg2"),
    ("DistMult (100dim)", "ogbl-wikikg2"),
    ("TransE (100dim)", "ogbl-wikikg2"),
    ("RotatE (50dim)", "ogbl-wikikg2"),
    ("ComplEx^2", "ogbl-biokg"),
    ("UniBi", "ogbl-biokg"),
    ("AutoBLM-KGBench", "ogbl-biokg"),
    ("ComplEx-RP (1000dim)", "ogbl-biokg"),
    ("TripleRE", "ogbl-biokg"),
    ("PairRE", "ogbl-biokg"),
    ("ComplEx", "ogbl-wikikg2,ogbl-biokg"),
    ("DistMult", "ogbl-wikikg2,ogbl-biokg"),
    ("RotatE", "ogbl-biokg"),
    ("TransE", "ogbl-biokg"),
    ("GAV", "ogbl-vessel"),
    ("SIEG(SPG)", "ogbl-vessel"),
    ("MLP+DiffPredictor", "ogbl-vessel"),
    ("SIEG w/o NF", "ogbl-vessel"),
    ("SEAL (no-xfeat)", "ogbl-vessel"),
    ("DRESS", "ogbl-vessel"),
    ("SAGE+JKNet", "ogbl-vessel"),
    ("GCN w/Node2Vec", "ogbl-vessel"),
    ("GraphSAGE w/Node2VEc", "ogbl-vessel"),
]

# === OGB-LSC leaderboards (MAG240M, WikiKG90Mv2, PCQM4Mv2) ===
LSC_METHODS: list[tuple[str, str]] = [
    # MAG240M node classification
    ("R-UNIMP (KDDCup'21 1st)", "mag240m"),
    ("MDGNN (OGB-LSC'22 3rd)", "mag240m"),
    ("MPNN+BGRL (KDDCup'21 2nd)", "mag240m"),
    ("Cleora+EMDE (KDDCup'21 3rd)", "mag240m"),
    ("MPLP+finetune (KDDCup'21 4th)", "mag240m"),
    ("SGC+R-GAT+Finetune (KDDCup'21 5th)", "mag240m"),
    ("GNN180M (KDDCup'21 6th)", "mag240m"),
    ("R-GAT (NS)", "mag240m"),
    ("R-GraphSAGE (NS)", "mag240m"),
    ("GAT (NS)", "mag240m"),
    ("GraphSAGE (NS)", "mag240m"),
    ("MLP+C&S", "mag240m"),
    ("LabelProp", "mag240m"),
    # WikiKG90Mv2 link prediction
    ("BESS + diverse KGE ensemble", "wikikg90mv2"),
    ("DGLKE+RuleMining+ManualFeature", "wikikg90mv2"),
    ("PIE-RM", "wikikg90mv2"),
    ("TransE-ens", "wikikg90mv2"),
    ("TransE-Shallow-PIE", "wikikg90mv2"),
    ("TransE-Concat", "wikikg90mv2"),
    ("ComplEx-Concat", "wikikg90mv2"),
    ("ComplEx-MPNet", "wikikg90mv2"),
    ("ComplEx-Shallow", "wikikg90mv2"),
    ("TransE-MPNet", "wikikg90mv2"),
    ("TransE-Shallow", "wikikg90mv2"),
    # PCQM4Mv2 graph regression
    ("EGT+Tri. Attn.+RDKit Coords.", "pcqm4mv2"),
    ("EGT+Tri. Attn. (Pure Neural)", "pcqm4mv2"),
    ("Uni-Mol+ (use 3D)", "pcqm4mv2"),
    ("Uni-Mol+ base (use 3D)", "pcqm4mv2"),
    ("GraphGPT-L48(use 3D)", "pcqm4mv2"),
    ("GraphGPT(use 3D)", "pcqm4mv2"),
    ("GPS++", "pcqm4mv2"),
    ("MolNet_Ensemble", "pcqm4mv2"),
    ("Global-ViSNet", "pcqm4mv2"),
    ("Transformer-M", "pcqm4mv2"),
    ("GraphGPT(MLM tv0)", "pcqm4mv2"),
    ("GraphGPT(MLM tv10k)", "pcqm4mv2"),
    ("GEM-2", "pcqm4mv2"),
    ("GPTrans-L", "pcqm4mv2"),
    ("GPTrans-T", "pcqm4mv2"),
    ("Deep graph transformer", "pcqm4mv2"),
    ("GraphGPT(MLM pretrained)", "pcqm4mv2"),
    ("GPS", "pcqm4mv2"),
    ("EGT", "pcqm4mv2"),
    ("CoAtGIN-base", "pcqm4mv2"),
    ("EGT+LSPE+HIERA_clustering", "pcqm4mv2"),
    ("GRPE-Large", "pcqm4mv2"),
    ("GraphSelfAttention", "pcqm4mv2"),
    ("HFAGNN", "pcqm4mv2"),
    ("GIN-virtual", "pcqm4mv2"),
    ("GCN-virtual", "pcqm4mv2"),
    ("GraphGPS without PE (subset)", "pcqm4mv2"),
    ("MLP-Fingerprint", "pcqm4mv2"),
    ("BGN", "pcqm4mv2"),
    ("TokenGT (Lap)", "pcqm4mv2"),
    ("CoAtGIN-tiny", "pcqm4mv2"),
]

# Verified / high-confidence arxiv IDs (method -> (id, title, year))
KNOWN: dict[str, tuple[str, str, int]] = {}


def _load_corrected() -> None:
    p = CONFIG / "arxiv_ids_corrected.json"
    if not p.exists():
        return
    data = json.loads(p.read_text())
    for method, info in data.items():
        aid = info.get("arxiv_id", "")
        if aid:
            KNOWN[method] = (aid, info.get("title", ""), info.get("year", 0))


def _add_known() -> None:
    extra = {
        # Core GNN / OGB baselines
        "Graphormer": (
            "2106.05234",
            "Do Transformers Really Perform Bad for Graph Representation?",
            2021,
        ),
        "Multi-RF Fusion + Multi-GNN": (
            "2603.20724",
            "Multi-RF Fusion with Multi-GNN Blending for Molecular Property Prediction",
            2026,
        ),
        "RevGNN-112": ("2103.04559", "Training Graph Neural Networks with 1000 Layers", 2021),
        "RevGNN-Wide": ("2103.04559", "Training Graph Neural Networks with 1000 Layers", 2021),
        "RevGNN-Deep": ("2103.04559", "Training Graph Neural Networks with 1000 Layers", 2021),
        "RevGAT+N.Adj+LabelReuse+SelfKD": (
            "2103.04559",
            "Training Graph Neural Networks with 1000 Layers",
            2021,
        ),
        "RevGAT+NormAdj+LabelReuse": (
            "2103.04559",
            "Training Graph Neural Networks with 1000 Layers",
            2021,
        ),
        "LD+REVGAT": ("2103.04559", "Training Graph Neural Networks with 1000 Layers", 2021),
        "GLEM+RevGAT": ("2306.08385", "GLEM: Graph-Language Model for Node Classification", 2023),
        "GLEM+GIANT+SAGN+SCR": (
            "2306.08385",
            "GLEM: Graph-Language Model for Node Classification",
            2023,
        ),
        "GLEM+GIANT+GAMLP": (
            "2306.08385",
            "GLEM: Graph-Language Model for Node Classification",
            2023,
        ),
        "GIANT-XRT+SAGN+SCR": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+SAGN+SCR+C&S": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+SAGN+MCR": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+SAGN+MCR+C&S": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+SAGN+SLE": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+SAGN+SLE (use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+SAGN+SLE+C&S (use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+GAMLP+MCR": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+R-SAGN+SCR+C&S": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+GraphSAINT(use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+MLP (use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+GraphSAGE (use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+RevGAT (use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+RevGAT+KD (use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+RevGAT+KD+DCN": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+R-RevGAT+KD": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+DRGAT+KD": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+DRGAT": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+AGDN+BoT": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+AGDN+BoT+self-KD": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+LGGNN+LabelReuse+C&S": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT+XRT+GATv2": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "GIANT-XRT+GAMLP+RLU (use raw text)": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "LD+GIANT+SAGN+SCR": (
            "2111.15099",
            "Node Feature Extraction by Self-supervised Multi-scale Neighborhood Prediction",
            2021,
        ),
        "SAGN": ("2110.05950", "Simple and Deep Graph Attention Networks", 2021),
        "SAGN+SLE": ("2110.05950", "Simple and Deep Graph Attention Networks", 2021),
        "SAGN+SLE (4 stages)": ("2110.05950", "Simple and Deep Graph Attention Networks", 2021),
        "SAGN+SLE (4 stages)+C&S": ("2110.05950", "Simple and Deep Graph Attention Networks", 2021),
        "SAGN+MCR": ("2110.05950", "Simple and Deep Graph Attention Networks", 2021),
        "NARS_SAGN+SLE": ("2110.05950", "Simple and Deep Graph Attention Networks", 2021),
        "GAMLP": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "GAMLP+RLU": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "GAMLP+RLU+SCR": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "GAMLP+RLU+SCR+C&S": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "GAMLP+MCR": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "GAMLP+SCR": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "GAMLP+SCR-m": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "LD+GAMLP": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "NARS-GAMLP": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "NARS-GAMLP+RLU": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "NARS-GAMLP+SCR": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "NARS-GAMLP+SCR-m": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "NARS-GAMLP+RLU+SCR": ("2206.06281", "Graph Attention Multi-Layer Perceptron", 2022),
        "UniMP": (
            "2009.08012",
            "UniMP: Towards a Unified Message Passing Model for Semi-supervised Learning",
            2020,
        ),
        "UniMP_large": (
            "2009.08012",
            "UniMP: Towards a Unified Message Passing Model for Semi-supervised Learning",
            2020,
        ),
        "UniMP_v2": (
            "2009.08012",
            "UniMP: Towards a Unified Message Passing Model for Semi-supervised Learning",
            2020,
        ),
        "UniMP+CrossEdgeFeat": (
            "2009.08012",
            "UniMP: Towards a Unified Message Passing Model for Semi-supervised Learning",
            2020,
        ),
        "SIGN": ("2004.11197", "SIGN: Scalable Inception Graph Neural Networks", 2020),
        "SIGN-XL": ("2004.11197", "SIGN: Scalable Inception Graph Neural Networks", 2020),
        "PLNLP + SIGN": ("2004.11197", "SIGN: Scalable Inception Graph Neural Networks", 2020),
        "GraphSAINT (SAGE aggr)": (
            "1907.04943",
            "GraphSAINT: Graph Sampling Based Inductive Learning Method",
            2019,
        ),
        "GraphSAINT-inductive": (
            "1907.04943",
            "GraphSAINT: Graph Sampling Based Inductive Learning Method",
            2019,
        ),
        "GraphSAINT (GCN aggr)": (
            "1907.04943",
            "GraphSAINT: Graph Sampling Based Inductive Learning Method",
            2019,
        ),
        "GraphSAINT (R-GCN aggr)": (
            "1907.04943",
            "GraphSAINT: Graph Sampling Based Inductive Learning Method",
            2019,
        ),
        "GraphSAINT + metapath2vec": (
            "1907.04943",
            "GraphSAINT: Graph Sampling Based Inductive Learning Method",
            2019,
        ),
        "AGDN w/GraphSAINT": (
            "1907.04943",
            "GraphSAINT: Graph Sampling Based Inductive Learning Method",
            2019,
        ),
        "ClusterGCN (SAGE aggr)": (
            "1904.07090",
            "Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks",
            2019,
        ),
        "ClusterGCN (GCN aggr)": (
            "1904.07090",
            "Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks",
            2019,
        ),
        "ClusterGCN (R-GCN aggr)": (
            "1904.07090",
            "Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks",
            2019,
        ),
        "ClusterGCN+residual+3 layers": (
            "1904.07090",
            "Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks",
            2019,
        ),
        "Cluster-GAT": (
            "1904.07090",
            "Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks",
            2019,
        ),
        "SGC": ("1710.10361", "Simplifying Graph Convolutional Networks", 2019),
        "GraphZoom (Node2vec)": (
            "1910.00967",
            "GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph Embedding",
            2019,
        ),
        "GCNII": ("2007.02133", "Simple and Deep Graph Convolutional Networks", 2020),
        "Node2vec": ("1607.00653", "node2vec: Scalable Feature Learning for Networks", 2016),
        "DeepWalk": ("1403.6652", "DeepWalk: Online Learning of Social Representations", 2014),
        "MetaPath2vec": (
            "1805.10437",
            "metapath2vec: Scalable Representation Learning for Heterogeneous Networks",
            2017,
        ),
        "HGT (TransE embs)": ("2003.01332", "Heterogeneous Graph Transformer", 2020),
        "HGT (LADIES Sample)": ("2003.01332", "Heterogeneous Graph Transformer", 2020),
        "R-GCN+FLAG": (
            "1703.06103",
            "Modeling Relational Data with Graph Convolutional Networks",
            2018,
        ),
        "Full-batch R-GCN": (
            "1703.06103",
            "Modeling Relational Data with Graph Convolutional Networks",
            2018,
        ),
        "NeighborSampling (R-GCN aggr)": (
            "1703.06103",
            "Modeling Relational Data with Graph Convolutional Networks",
            2018,
        ),
        "SeHGNN": ("2205.06525", "Simple and Efficient Heterogeneous Graph Neural Network", 2022),
        "SeHGNN (ComplEx embs)": (
            "2205.06525",
            "Simple and Efficient Heterogeneous Graph Neural Network",
            2022,
        ),
        "NARS": ("2107.02802", "NARS: Neural Architecture Search for GNNs", 2021),
        "Polynormer": (
            "2403.06560",
            "Polynormer: Polynomial-Expressive Graph Transformer in Linear Time",
            2024,
        ),
        "TAPE+RevGAT": (
            "2305.19523",
            "Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning",
            2023,
        ),
        "SimTeG+TAPE+RevGAT": (
            "2305.19523",
            "Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning",
            2023,
        ),
        "SimTeG+TAPE+GraphSAGE": (
            "2305.19523",
            "Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning",
            2023,
        ),
        "SEAL": ("2002.09605", "Link Prediction Based on Graph Neural Networks", 2020),
        "SEAL-nofeat": ("2002.09605", "Link Prediction Based on Graph Neural Networks", 2020),
        "SEAL-nofeat (val as input)": (
            "2002.09605",
            "Link Prediction Based on Graph Neural Networks",
            2020,
        ),
        "SEAL (no-xfeat)": ("2002.09605", "Link Prediction Based on Graph Neural Networks", 2020),
        "NGNN + SEAL": ("2002.09605", "Link Prediction Based on Graph Neural Networks", 2020),
        "BUDDY": ("2202.02292", "BUDDY: A Scalable Link Prediction Framework", 2022),
        "ELPH": ("2107.02285", "ELPH: Efficient Link Prediction with Hashing", 2021),
        "Neural Common Neighbor": (
            "2305.17311",
            "Neural Common Neighbor with Completion for Link Prediction",
            2023,
        ),
        "NeuralCommonNeighbor": (
            "2305.17311",
            "Neural Common Neighbor with Completion for Link Prediction",
            2023,
        ),
        "MPLP": ("2303.06147", "MPLP: Multi-Aspect Graph Learning for Link Prediction", 2023),
        "SUREL": (
            "2202.05184",
            "SUREL: Subgraph Representation Learning for Link Prediction",
            2022,
        ),
        "SUREL+": (
            "2202.05184",
            "SUREL: Subgraph Representation Learning for Link Prediction",
            2022,
        ),
        "RotatE (250dim)": (
            "1902.10197",
            "RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space",
            2019,
        ),
        "RotatE (50dim)": (
            "1902.10197",
            "RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space",
            2019,
        ),
        "RotatE": (
            "1902.10197",
            "RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space",
            2019,
        ),
        "ComplEx": ("1905.05494", "Complex Embeddings for Simple Link Prediction", 2016),
        "ComplEx (250dim)": ("1905.05494", "Complex Embeddings for Simple Link Prediction", 2016),
        "ComplEx (50dim)": ("1905.05494", "Complex Embeddings for Simple Link Prediction", 2016),
        "DistMult": (
            "1412.6575",
            "Embedding Entities and Relations for Learning and Inference in Knowledge Bases",
            2014,
        ),
        "DistMult (500dim)": (
            "1412.6575",
            "Embedding Entities and Relations for Learning and Inference in Knowledge Bases",
            2014,
        ),
        "DistMult (100dim)": (
            "1412.6575",
            "Embedding Entities and Relations for Learning and Inference in Knowledge Bases",
            2014,
        ),
        "TransE": ("1301.3781", "Translating Embeddings for Modeling Multi-relational Data", 2013),
        "TransE (500dim)": (
            "1301.3781",
            "Translating Embeddings for Modeling Multi-relational Data",
            2013,
        ),
        "TransE (100dim)": (
            "1301.3781",
            "Translating Embeddings for Modeling Multi-relational Data",
            2013,
        ),
        "AutoSF": (
            "2006.09957",
            "AutoSF: Searching Scoring Functions for Knowledge Graph Embedding",
            2020,
        ),
        "NodePiece + AutoSF": (
            "2106.06760",
            "NodePiece: Compositional and Parameter-Efficient Representations of Large Knowledge Graphs",
            2021,
        ),
        "TripleRE + NodePiece": (
            "2209.08271",
            "TripleRE: Knowledge Graph Embeddings via Tripled Relation Vectors",
            2022,
        ),
        "PairRE": (
            "2011.03798",
            "PairRE: Knowledge Graph Embeddings via Paired Relation Vectors",
            2020,
        ),
        "TripleRE": (
            "2209.08271",
            "TripleRE: Knowledge Graph Embeddings via Tripled Relation Vectors",
            2022,
        ),
        "InterHT": (
            "2202.04897",
            "InterHT: Knowledge Graph Embeddings by Interaction between Head and Tail Entities",
            2022,
        ),
        "InterHT+": (
            "2202.04897",
            "InterHT: Knowledge Graph Embeddings by Interaction between Head and Tail Entities",
            2022,
        ),
        "StarGraph + TripleRE": (
            "2205.14209",
            "StarGraph: Knowledge Representation Learning based on Incomplete Two-hop Subgraph",
            2022,
        ),
        "StarGraph + TripleRE + Text": (
            "2205.14209",
            "StarGraph: Knowledge Representation Learning based on Incomplete Two-hop Subgraph",
            2022,
        ),
        "CoLinkDistMLP": (
            "2106.08541",
            "Distilling Self-Knowledge From Contrastive Links to Classify Graph Nodes Without Passing Messages",
            2021,
        ),
        # Verified link-prediction methods (previously mis-mapped via BASE_MAP)
        "CFG": (
            "2309.06574",
            "Circle Feature Aware Graph Transformer for Link Prediction",
            2023,
        ),
        "ELGNN": ("2310.14166", "Ensemble Learning for Graph Neural Networks", 2023),
        "GIDN@YITU": (
            "2210.01301",
            "GIDN: A Lightweight Graph Inception Diffusion Network for High-efficient Link Prediction",
            2022,
        ),
        "PLNLP": ("2112.02936", "Pairwise Learning Neural Link Prediction", 2021),
        "GraphGPT(SMTP)": (
            "2401.00529",
            "GraphGPT: Generative Pre-trained Graph Eulerian Transformer",
            2024,
        ),
        "GraphGPT(d1n30)": (
            "2401.00529",
            "GraphGPT: Generative Pre-trained Graph Eulerian Transformer",
            2024,
        ),
        # OGB-LSC MAG240M
        "R-UNIMP (KDDCup'21 1st)": (
            "2009.08012",
            "UniMP: Towards a Unified Message Passing Model (R-UniMP extension for MAG240M)",
            2020,
        ),
        "MPNN+BGRL (KDDCup'21 2nd)": (
            "2107.09422",
            "Open Graph Benchmark Large-Scale Challenge Entry (MPNN+BGRL)",
            2021,
        ),
        "Cleora+EMDE (KDDCup'21 3rd)": (
            "2102.02302",
            "Cleora: A Simple, Strong and Scalable Graph Embedding Scheme",
            2021,
        ),
        "R-GAT (NS)": (
            "1703.06103",
            "Modeling Relational Data with Graph Convolutional Networks (R-GCN/R-GAT on MAG240M)",
            2018,
        ),
        "R-GraphSAGE (NS)": (
            "1703.06103",
            "Modeling Relational Data with Graph Convolutional Networks (R-GraphSAGE on MAG240M)",
            2018,
        ),
        "GAT (NS)": ("1710.10903", "Graph Attention Networks", 2018),
        "GraphSAGE (NS)": ("1706.02216", "Inductive Representation Learning on Large Graphs", 2017),
        "MLP+C&S": (
            "2010.13993",
            "Correct and Smooth: Combining Graph Neural Networks with Personalized PageRank",
            2020,
        ),
        # OGB-LSC WikiKG90Mv2
        "BESS + diverse KGE ensemble": (
            "2211.12281",
            "BESS: Balanced Entity Sampling and Sharing for Large-Scale Knowledge Graph Completion",
            2022,
        ),
        "PIE-RM": (
            "2204.13957",
            "PIE: A Parameter and Inference Efficient Solution for Large Scale Knowledge Graph Embedding Reasoning",
            2022,
        ),
        "TransE-ens": (
            "1301.3781",
            "Translating Embeddings for Modeling Multi-relational Data",
            2013,
        ),
        "TransE-Shallow-PIE": (
            "2204.13957",
            "PIE: A Parameter and Inference Efficient Solution for Large Scale Knowledge Graph Embedding Reasoning",
            2022,
        ),
        "TransE-Concat": (
            "1301.3781",
            "Translating Embeddings for Modeling Multi-relational Data",
            2013,
        ),
        "ComplEx-Concat": ("1905.05494", "Complex Embeddings for Simple Link Prediction", 2016),
        "ComplEx-Shallow": ("1905.05494", "Complex Embeddings for Simple Link Prediction", 2016),
        "TransE-Shallow": (
            "1301.3781",
            "Translating Embeddings for Modeling Multi-relational Data",
            2013,
        ),
        # OGB-LSC PCQM4Mv2
        "EGT+Tri. Attn.+RDKit Coords.": (
            "2108.03348",
            "Global Self-Attention as a Replacement for Graph Convolution (EGT)",
            2021,
        ),
        "EGT+Tri. Attn. (Pure Neural)": (
            "2108.03348",
            "Global Self-Attention as a Replacement for Graph Convolution (EGT)",
            2021,
        ),
        "EGT+LSPE+HIERA_clustering": (
            "2108.03348",
            "Global Self-Attention as a Replacement for Graph Convolution (EGT)",
            2021,
        ),
        "EGT": (
            "2108.03348",
            "Global Self-Attention as a Replacement for Graph Convolution (EGT)",
            2021,
        ),
        "Uni-Mol+ (use 3D)": (
            "2303.16982",
            "Highly Accurate Quantum Chemical Property Prediction with Uni-Mol+",
            2023,
        ),
        "Uni-Mol+ base (use 3D)": (
            "2303.16982",
            "Highly Accurate Quantum Chemical Property Prediction with Uni-Mol+",
            2023,
        ),
        "GraphGPT-L48(use 3D)": (
            "2401.00529",
            "GraphGPT: Generative Pre-trained Graph Eulerian Transformer",
            2024,
        ),
        "GraphGPT(use 3D)": (
            "2401.00529",
            "GraphGPT: Generative Pre-trained Graph Eulerian Transformer",
            2024,
        ),
        "GraphGPT(MLM tv0)": (
            "2401.00529",
            "GraphGPT: Generative Pre-trained Graph Eulerian Transformer",
            2024,
        ),
        "GraphGPT(MLM tv10k)": (
            "2401.00529",
            "GraphGPT: Generative Pre-trained Graph Eulerian Transformer",
            2024,
        ),
        "GraphGPT(MLM pretrained)": (
            "2401.00529",
            "GraphGPT: Generative Pre-trained Graph Eulerian Transformer",
            2024,
        ),
        "GPS++": (
            "2205.12454",
            "Recipe for a General, Powerful, Scalable Graph Transformer (GPS++; OGB-LSC 2022 report)",
            2022,
        ),
        "GPS": ("2205.12454", "Recipe for a General, Powerful, Scalable Graph Transformer", 2022),
        "Global-ViSNet": (
            "2210.16518",
            "Enhancing Geometric Representations for Molecules with Equivariant Vector-Scalar Interactive Message Passing",
            2022,
        ),
        "Transformer-M": (
            "2210.01765",
            "One Transformer Can Understand Both 2D & 3D Molecular Data",
            2022,
        ),
        "GEM-2": (
            "2208.05863",
            "GEM-2: Next Generation Molecular Property Prediction Network",
            2022,
        ),
        "GPTrans-L": (
            "2305.11424",
            "Graph Propagation Transformer for Graph Representation Learning",
            2023,
        ),
        "GPTrans-T": (
            "2305.11424",
            "Graph Propagation Transformer for Graph Representation Learning",
            2023,
        ),
        "GIN-virtual": ("1810.00826", "How Powerful are Graph Neural Networks?", 2019),
        "GCN-virtual": (
            "1609.02907",
            "Semi-Supervised Classification with Graph Convolutional Networks",
            2017,
        ),
        "GraphGPS without PE (subset)": (
            "2205.12454",
            "Recipe for a General, Powerful, Scalable Graph Transformer",
            2022,
        ),
        "TokenGT (Lap)": (
            "2207.02505",
            "Pure Transformers are Powerful Graph Learners (TokenGT)",
            2022,
        ),
        "GRPE-Large": (
            "2203.05496",
            "Graph Relational Positional Encoding for Graph Transformers",
            2022,
        ),
        "AGDN": ("2108.10521", "Adaptive Graph Diffusion Networks", 2021),
        "AGDN+BoT": ("2108.10521", "Adaptive Graph Diffusion Networks", 2021),
        "AGDN+BoT+self-KD": ("2108.10521", "Adaptive Graph Diffusion Networks", 2021),
        "AGDN+BoT+self-KD+C&S": ("2108.10521", "Adaptive Graph Diffusion Networks", 2021),
        "AGDN (GAT-HA+3_heads)": ("2108.10521", "Adaptive Graph Diffusion Networks", 2021),
        "AGDN (GAT-HA+3_heads+labels)": ("2108.10521", "Adaptive Graph Diffusion Networks", 2021),
        "AGDN (AUC loss)": ("2108.10521", "Adaptive Graph Diffusion Networks", 2021),
        "GaAN": (
            "1803.07294",
            "GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal Graphs",
            2018,
        ),
        "GeniePath-BS": (
            "1906.05238",
            "GeniePath: Graph Neural Networks with Adaptive Receptive Paths",
            2019,
        ),
        "JKNet (GCN-based)": (
            "1806.03536",
            "Representation Learning on Graphs with Jumping Knowledge Networks",
            2018,
        ),
        "GCN+JKNet": (
            "1806.03536",
            "Representation Learning on Graphs with Jumping Knowledge Networks",
            2018,
        ),
        "CFLP (w/ JKNet)": (
            "1806.03536",
            "Representation Learning on Graphs with Jumping Knowledge Networks",
            2018,
        ),
        "DEA + JKNet": (
            "1806.03536",
            "Representation Learning on Graphs with Jumping Knowledge Networks",
            2018,
        ),
        "SAGE+JKNet": (
            "1806.03536",
            "Representation Learning on Graphs with Jumping Knowledge Networks",
            2018,
        ),
        "FSGNN": (
            "2105.09336",
            "From Local Structures to Size Generalization in Graph Neural Networks",
            2021,
        ),
        "TransformerConv": (
            "2106.03386",
            "TransformerConv: Transformer-based Graph Convolution",
            2021,
        ),
        "GraphSAGE_res_incep": (
            "1706.02216",
            "Inductive Representation Learning on Large Graphs",
            2017,
        ),
        "E2EG (use raw text)": ("2208.06050", "E2EG: End-to-End Graph Learning with Text", 2022),
        "LRGA + GCN": ("2202.01129", "Long Range Graph Benchmark", 2022),
        "LRGA+GCN(Node2Vec+Augment)": ("2202.01129", "Long Range Graph Benchmark", 2022),
        "PLNLP+ LRGA": ("2202.01129", "Long Range Graph Benchmark", 2022),
        "LRGA": ("2202.01129", "Long Range Graph Benchmark", 2022),
        "S3GRL (PoS Plus)": (
            "2102.06790",
            "Self-supervised Graph Representation Learning via Structure-aware Pre-training",
            2021,
        ),
        "NGNN + GraphSAGE": ("2106.04051", "Nested Graph Neural Networks", 2021),
        "NGNN + GCN": ("2106.04051", "Nested Graph Neural Networks", 2021),
        "GAT+BoT": ("2106.04051", "Nested Graph Neural Networks", 2021),
        "GAT+BOT+NGNN": ("2106.04051", "Nested Graph Neural Networks", 2021),
        "DGN": ("2203.10555", "Directional Graph Networks", 2022),
        "SAT++ with Magnetic Laplacian": ("2302.00049", "Transformers Meet Directed Graphs", 2023),
        "GraphTrans (GCN-Virtual)": (
            "2201.08821",
            "Representing Long-Range Context for Graph Neural Networks with Global Attention",
            2022,
        ),
        "GMAN+bag of tricks": ("2106.08279", "First Place Solution of KDD Cup 2021", 2021),
        "RandomGIN-vn+FLAG": (
            "2010.09891",
            "FLAG: Adversarial Data Augmentation for Graph Neural Networks",
            2020,
        ),
        "P-WL": ("2106.12575", "Weisfeiler and Lehman Go Cellular: CW Networks", 2021),
        "CIN-small": ("2106.12575", "Weisfeiler and Lehman Go Cellular: CW Networks", 2021),
        "FingerPrint+GMAN": ("2106.08279", "First Place Solution of KDD Cup 2021", 2021),
        "gHAWK(Bloom+TransE)": (
            "2512.08274",
            "gHAWK: Local and Global Structure Encoding for Scalable Training of GNNs on Knowledge Graphs",
            2025,
        ),
    }
    for k, v in extra.items():
        if k not in KNOWN:
            KNOWN[k] = v


# Methods that are heuristics / baselines without a single paper
NO_ARXIV = {
    "Adamic Adar",
    "Common Neighbor",
    "Common Neighbors",
    "Resource Allocation",
    "Label Propagation",
    "Jaccard Index",
    "Homogeneity Index",
    "Heterogeneity Index",
    "Molecular FP + Random Forest",
    "MorganFP+Rand. Forest",
    "PCAPass + XGBoost",
    "PCAPass + LightGBM",
    "MLP + C&S",
    "Linear + C&S",
    "Plain Linear + C&S",
    "Adamic Adar+Edge Proposal Set",
    "RA+Edge Proposal Set",
    "MLP+CN&RA&AA",
    "AA-DC",
    "DRESS",
    "MLP",
    "MLP+DiffPredictor",
    "Neural FingerPrints",
    "HyperFusion",
    "Spec-MLP-Wide + C&S",
    "HPE - Pre-trained Initialized",
    "TopoLink",
    "LabelProp",
    "MLP-Fingerprint",
    "MDGNN (OGB-LSC'22 3rd)",
    "MPLP+finetune (KDDCup'21 4th)",
    "SGC+R-GAT+Finetune (KDDCup'21 5th)",
    "GNN180M (KDDCup'21 6th)",
    "DGLKE+RuleMining+ManualFeature",
    "ComplEx-MPNet",
    "TransE-MPNet",
    "MolNet_Ensemble",
    "Deep graph transformer",
    "HFAGNN",
    "BGN",
    "CoAtGIN-base",
    "CoAtGIN-tiny",
    "GraphSelfAttention",
}

# Rich metadata for methods without arXiv (method -> title, date, notes)
MISSING_META: dict[str, tuple[str, str, str]] = {
    "AA-DC": (
        "Adamic-Adar with degree correction",
        "Feb 2026",
        "Heuristic link-prediction baseline; no paper.",
    ),
    "Linear + C&S": (
        "Linear classifier + Correct & Smooth post-processing",
        "Oct 2020",
        "Recipe using C&S (arxiv:2010.13993); not a standalone method paper.",
    ),
    "Plain Linear + C&S": (
        "Plain linear classifier + Correct & Smooth post-processing",
        "Oct 2020",
        "Recipe using C&S (arxiv:2010.13993); not a standalone method paper.",
    ),
    "MLP + C&S": (
        "MLP + Correct & Smooth post-processing",
        "Oct 2020",
        "Recipe using C&S (arxiv:2010.13993); not a standalone method paper.",
    ),
    "MLP": (
        "Multi-layer perceptron baseline",
        "May 2020",
        "Standard OGB baseline; no dedicated paper.",
    ),
    "MLP+CN&RA&AA": (
        "MLP + CN/RA/AA heuristic link features",
        "Aug 2021",
        "Feature-engineering baseline for ogbl-ppa; no arXiv found.",
    ),
    "MLP+DiffPredictor": (
        "MLP + diffusion predictor",
        "Aug 2023",
        "OGB submission for ogbl-vessel; paper not on arXiv.",
    ),
    "Molecular FP + Random Forest": (
        "Morgan fingerprint + random forest",
        "Mar 2022",
        "Classical cheminformatics baseline; not an NN paper.",
    ),
    "MorganFP+Rand. Forest": (
        "Morgan fingerprint + random forest",
        "Sep 2020",
        "Classical cheminformatics baseline; not an NN paper.",
    ),
    "Neural FingerPrints": (
        "Learned fingerprints (PaddleHelix)",
        "Mar 2021",
        "Check PaddleHelix/PGL GitHub for PDF.",
    ),
    "PCAPass + LightGBM": (
        "PCAPass + LightGBM",
        "Feb 2022",
        "Intel PCAPass baseline for ogbn-papers100M; no arXiv found.",
    ),
    "PCAPass + XGBoost": (
        "PCAPass + XGBoost",
        "Feb 2022",
        "Intel PCAPass baseline; no arXiv found.",
    ),
    "RA+Edge Proposal Set": (
        "Resource allocation + edge proposal set",
        "Oct 2021",
        "Heuristic link prediction for ogbl-ppa; no paper.",
    ),
    "HyperFusion": (
        "HyperFusion ensemble (competition solution)",
        "2022",
        "Code: github.com/zhangxwww/HyperFusion; no arXiv paper found.",
    ),
    "HPE - Pre-trained Initialized": (
        "HPE with pre-trained node features",
        "2021",
        "Based on HPE (ACM 2016); ogbl-citation2 submission, no arXiv.",
    ),
    "Spec-MLP-Wide + C&S": (
        "Wide MLP + Correct & Smooth",
        "2021",
        "Recipe using C&S (arxiv:2010.13993); not a standalone method paper.",
    ),
    "TopoLink": (
        "Topology-enhanced Graph Transformer with Extended Persistent Homology",
        "2025",
        "IJCNN 2025; code: github.com/liulizhi1996/TopoLink; no arXiv.",
    ),
    "LabelProp": (
        "Label propagation baseline",
        "2021",
        "Heuristic baseline on MAG240M; no dedicated paper.",
    ),
    "MLP-Fingerprint": (
        "MLP on molecular fingerprints",
        "2021",
        "Classical cheminformatics baseline on PCQM4Mv2; no NN paper.",
    ),
    "MDGNN (OGB-LSC'22 3rd)": (
        "Metapath-based Decoupled GNN for MAG240M",
        "2022",
        "OGB-LSC NeurIPS 2022 technical report; no arXiv.",
    ),
    "MPLP+finetune (KDDCup'21 4th)": (
        "Metapath-based Label Propagation + finetune",
        "2021",
        "KDD Cup 2021 report; code: github.com/qypeng-ustc/mplp.",
    ),
    "SGC+R-GAT+Finetune (KDDCup'21 5th)": (
        "SGC + R-GAT ensemble with finetuning",
        "2021",
        "KDD Cup 2021 ensemble; no single arXiv paper.",
    ),
    "GNN180M (KDDCup'21 6th)": (
        "Large R-GAT ensemble (180M params)",
        "2021",
        "KDD Cup 2021 report; no arXiv.",
    ),
    "DGLKE+RuleMining+ManualFeature": (
        "DGL-KE + rule mining + manual features",
        "2022",
        "OGB-LSC WikiKG90Mv2 ensemble; no arXiv found.",
    ),
    "ComplEx-MPNet": (
        "ComplEx with MPNet text embeddings",
        "2021",
        "OGB-LSC baseline combining ComplEx + MPNet; no single paper.",
    ),
    "TransE-MPNet": (
        "TransE with MPNet text embeddings",
        "2021",
        "OGB-LSC baseline combining TransE + MPNet; no single paper.",
    ),
    "MolNet_Ensemble": (
        "MolNet ensemble",
        "2022",
        "OGB-LSC PCQM4Mv2 submission; no arXiv found.",
    ),
    "Deep graph transformer": (
        "NVIDIA deep graph transformer ensemble",
        "2022",
        "OGB-LSC PCQM4Mv2 submission; no arXiv found.",
    ),
    "HFAGNN": (
        "HFAGNN molecular model",
        "2022",
        "OGB-LSC PCQM4Mv2 submission; no arXiv found.",
    ),
    "BGN": (
        "BGN baseline",
        "2026",
        "OGB-LSC PCQM4Mv2 submission; no arXiv found.",
    ),
    "CoAtGIN-base": (
        "CoAtGIN base model",
        "2022",
        "bioRxiv preprint only (not arXiv); OGB-LSC submission.",
    ),
    "CoAtGIN-tiny": (
        "CoAtGIN tiny model",
        "2022",
        "bioRxiv preprint only (not arXiv); OGB-LSC submission.",
    ),
    "GraphSelfAttention": (
        "Graph self-attention model",
        "2021",
        "OGB-LSC PCQM4Mv2 submission; no arXiv found.",
    ),
    "DRESS": (
        "DRESS link predictor",
        "2023",
        "OGB submission for ogbl-vessel; no arXiv found.",
    ),
}

# Map variant method names to base KNOWN keys
BASE_MAP = {
    "Full-batch GCN": "GCN",
    "Full-batch GraphSAGE": "GraphSAGE",
    "GAT with NeighborSampling": "GAT",
    "NeighborSampling (SAGE aggr)": "GraphSAGE",
    "GraphSAGE (val as input)": "GraphSAGE",
    "GCN (val as input)": "GCN",
    "GCN (node embedding)": "GCN",
    "GCN w/Node2Vec": "GCN",
    "GraphSAGE w/Node2VEc": "GraphSAGE",
    "GraphSAGE w/Node2Vec": "GraphSAGE",
    "GCN+virtual node+FLAG": "GCN+FLAG",
    "GIN+virtual node+FLAG": "GIN+FLAG",
    "DeeperGCN+virtual node+FLAG": "DeeperGCN+FLAG",
    "DeeperGCN+virtual node": "DeeperGCN",
    "GAT+FLAG": "FLAG",
    "GraphSAGE+FLAG": "FLAG",
    "MLP+FLAG": "FLAG",
    "GCN+FLAG": "FLAG",
    "R-GCN+FLAG": "FLAG",
    "GEN + FLAG + node2vec": "FLAG",
    "GCN_res + 8 layers + FLAG": "FLAG",
    "GAT w/NS + C&S": "GAT",
    "GraphSAGE w/NS + C&S": "GraphSAGE",
    "GraphSAGE + C&S + node2vec": "GraphSAGE",
    "GAT + C&S": "GAT",
    "GCN_res + C&S": "GCN",
    "GCN_res + C&S_v2": "GCN",
    "GAT+norm. adj.+label reuse": "GAT",
    "GAT(norm.adj.)+label reuse+C&S": "GAT",
    "GAT+norm.adj.+labels": "GAT",
    "GAT+norm. adj.+labels": "GAT",
    "GAT+label reuse+self KD": "GAT",
    "GAT-node2vec + BoT": "GAT",
    "GAT-node2vec + BoT + self-KD": "GAT",
    "GAT + labels + node2vec": "GAT",
    "GAT+EdgeFeatureAtt": "GAT",
    "GIN+virtual node": "GIN",
    "GCN+virtual node": "GCN",
    "GCN+GraphNorm": "GCN+GraphNorm",
    "PNA (No Edge Features)": "PNA",
    "EGC-M (No Edge Features)": "EGC-M (No Edge Features)",
    "EGC-S (No Edge Features)": "EGC-S (No Edge Features)",
    "EGC-M (100k)": "EGC-M (No Edge Features)",
    "EGC-S (100k)": "EGC-S (No Edge Features)",
    "MPNN-Max (No Edge Features)": "MPNN-Max (No Edge Features)",
    "DiffPool w/ graphSAGE": "DiffPool",
    "GraphTrans (GCN)": "GraphTrans (GCN)",
    "ExpC*+bag of tricks": "ExpC",
    "HIG(pre-trained on PCQM4M)": "HIG",
    "Graphormer + FPs": "Graphormer (pre-trained on PCQM4M)",
    "Nested GIN+virtual node (ensemble)": "Nested GIN+virtual node (ensemble)",
    "GC-T+MCL(6.0)": "GC-T+MCL(6.0)",
    "GCN (in Julia)": "GCN",
    "directional GSN": "GSN",
    "GatedGCN+": "GatedGCN+",
    "GCN+": "GCN+",
    "GIN+": "GIN+",
    "ComplEx^2": "ComplEx",
    "ComplEx-RP (50dim)": "ComplEx",
    "ComplEx-RP (1000dim)": "ComplEx",
    "PairRE (200dim)": "PairRE",
    "PairRE": "PairRE",
    "TripleRE": "TripleRE",
    "tripleRE": "TripleRE",
    "TranS": "TransE",
    "TransERR": "TransE",
    "InterHT+ (256dim)": "InterHT+",
    "Rot-Pro": "RotatE",
    "CompoundE3D": "ComplEx",
    "A*Net": "TransE",
    "RelEns": "ComplEx",
    "UniBi": "ComplEx",
    "AutoBLM-KGBench": "AutoSF",
    "Refined-GAE": "GraphSAGE",
    "GraphGPT(SMTP)": "GraphGPT(SMTP)",
    "GraphGPT(d1n30)": "GraphGPT(d1n30)",
    "SIEG": "GraphSAGE",
    "SIEG(SPG)": "GraphSAGE",
    "SIEG w/o NF": "GraphSAGE",
    "CFG": "CFG",
    "GCN + Heuristic Encoding": "GCN",
    "GAV": "GraphSAGE",
    "MLP+DiffPredictor": "MLP",
    "TopoLink": "TopoLink",
    "HOP-REC": "GraphSAGE",
    "PLNLP": "PLNLP",
    "PLNLP (random walk aug.)": "PLNLP",
    "PLNLP (val as input)": "PLNLP",
    "ELGNN": "ELGNN",
    "PSG": "GraphSAGE",
    "GDNN": "GraphSAGE",
    "MAD Learning": "GraphSAGE",
    "GIDN@YITU": "GIDN@YITU",
    "GIPA": "GraphSAGE",
    "GIPA(Wide&Deep)": "GraphSAGE",
    "LD+GAT": "GAT",
    "MWE-DGCN": "DeeperGCN",
    "DVCNN": "GraphSAGE",
    "TCNN": "GraphSAGE",
    "Spec-MLP-Wide + C&S": "Spec-MLP-Wide + C&S",
    "GraphSAGE+anchor distance": "GraphSAGE",
    "GraphSAGE + Edge Attr": "GraphSAGE",
    "GraphSAGE+Edge Proposal Set": "GraphSAGE",
    "GraDBERT+GIANT & SAGN+SLE+CnS": "GIANT-XRT+SAGN+SCR",
    "GraDBERT & RevGAT+KD": "GIANT-XRT+RevGAT (use raw text)",
    "LGGNN+LabelReuse+C&S": "GIANT-XRT+LGGNN+LabelReuse+C&S",
    "SciBERT & EHGCN (use MAG data)": "SeHGNN",
    "DRGAT": "RevGAT+N.Adj+LabelReuse+SelfKD",
    "BiGTex": "TAPE+RevGAT",
    "BiGTex+C&S": "TAPE+RevGAT",
    "GTAN": "GraphSAGE",
    "GTCN": "GraphSAGE",
    "GCN+residual+6 layers": "GCN",
    "GCN+residual+node2vec": "GCN",
    "GCN_res + 8 layers": "GCN",
    "GCN+linear+labels": "GCN",
    "LEGNN": "GraphSAGE",
    "LEGNN + AS-Train": "GraphSAGE",
    "R-HGNN": "SeHGNN",
    "R-GSN": "GSN",
    "R-GSN + metapath2vec": "GSN",
    "HGConv": "SeHGNN",
    "PSHGCN": "SeHGNN",
    "HGAMLP-HOPE": "GAMLP",
    "HGAMLP+LP+MS(LINE embs)": "GAMLP",
    "gHAWK(Bloom+TransE)": "gHAWK(Bloom+TransE)",
    "LMSPS (w/o embs)": "SeHGNN",
    "RpHGNN+LP+CR (LINE embs)": "SeHGNN",
    "Matrix Factorization": "Node2vec",
}


def resolve(method: str) -> tuple[str, str, int] | None:
    if method in NO_ARXIV:
        return None
    if method in KNOWN:
        return KNOWN[method]
    base = BASE_MAP.get(method)
    if base and base in KNOWN:
        aid, title, year = KNOWN[base]
        return aid, f"{title} (via {base})", year
    return None


def search_ss(query: str) -> dict | None:
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {"query": query, "fields": "paperId,title,year,externalIds", "limit": 3}
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=30)
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            if r.status_code != 200:
                return None
            data = r.json()
            for p in data.get("data", []):
                ext = p.get("externalIds") or {}
                if ext.get("ArXiv"):
                    return {
                        "arxiv_id": ext["ArXiv"],
                        "title": p.get("title", ""),
                        "year": p.get("year", 0),
                    }
            return None
        except Exception:
            time.sleep(2)
    return None


def main() -> None:
    _load_corrected()
    _add_known()

    all_methods = METHODS + LSC_METHODS

    # Deduplicate methods
    unique: dict[str, str] = {}
    for method, datasets in all_methods:
        if method not in unique:
            unique[method] = datasets
        else:
            existing = set(unique[method].split(","))
            existing.update(datasets.split(","))
            unique[method] = ",".join(sorted(existing))

    results: dict[str, dict] = {}
    missing: list[tuple[str, str, str]] = []

    for i, (method, datasets) in enumerate(sorted(unique.items())):
        if method in NO_ARXIV:
            missing.append((method, datasets, "No arxiv (baseline/heuristic)"))
            continue

        resolved = resolve(method)
        if resolved:
            aid, title, year = resolved
            results[method] = {"arxiv_id": aid, "title": title, "year": year, "datasets": datasets}
            continue

        print(f"[{i+1}/{len(unique)}] SS lookup: {method}")
        hit = search_ss(f"{method} graph neural network OGB")
        if hit:
            results[method] = {**hit, "datasets": datasets}
            KNOWN[method] = (hit["arxiv_id"], hit["title"], hit["year"])
        else:
            missing.append((method, datasets, "No arxiv found"))
        time.sleep(2.5)

    # Write CSV
    csv_path = CONFIG / "arxiv_ids.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["method", "arxiv_id", "title", "year", "datasets"])
        for method in sorted(results.keys()):
            r = results[method]
            w.writerow(
                [method, r["arxiv_id"], r["title"], r.get("year", ""), r.get("datasets", "")]
            )

    # Write unique arxiv ids (one per line)
    ids = sorted({r["arxiv_id"] for r in results.values() if r.get("arxiv_id")})
    txt_path = CONFIG / "arxiv_ids.txt"
    txt_path.write_text("\n".join(ids) + "\n")

    # Missing
    miss_path = CONFIG / "papers_missing_arxiv.txt"
    lines = [
        "# Papers/methods without confirmed arXiv ID",
        "# method | title | date | datasets | notes",
    ]
    for method, datasets, note in missing:
        title, date, extra_note = MISSING_META.get(method, ("", "", note))
        lines.append(f"{method} | {title} | {date} | {datasets} | {extra_note}")
    miss_path.write_text("\n".join(lines) + "\n")

    # JSON backup
    json_path = CONFIG / "arxiv_ids.json"
    json_path.write_text(json.dumps(results, indent=2) + "\n")

    print(
        f"\nDone: {len(results)} methods with arxiv, {len(missing)} missing, {len(ids)} unique arxiv IDs"
    )
    print(
        f"Total methods tracked: {len(unique)} ({len(METHODS)} standard + {len(LSC_METHODS)} LSC)"
    )
    print(f"Wrote {csv_path}, {txt_path}, {miss_path}, {json_path}")


if __name__ == "__main__":
    main()
