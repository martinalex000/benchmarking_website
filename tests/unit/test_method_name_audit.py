import json

from backend.method_name_audit import audit_method_names, audit_single_paper
from backend.paper_storage import PaperStorage


def _write_paper(tmp_path, arxiv_id: str, title: str, payload: dict, overrides: str = ""):
    storage = PaperStorage(arxiv_id, papers_root=tmp_path)
    storage.ensure_dirs()
    storage.metadata_path.write_text(json.dumps({"title": title}), encoding="utf-8")
    storage.llm_output_path.write_text(json.dumps({"results": payload}), encoding="utf-8")
    if overrides:
        storage.overrides_path.write_text(overrides, encoding="utf-8")
    return storage


def test_audit_flags_benchmark_paper_with_proposed_model(tmp_path):
    _write_paper(
        tmp_path,
        "2206.08164",
        "LRGB: A Large-Scale Benchmark for Graph Neural Networks",
        {
            "proposed_model": {"name": "LRGB Benchmark (Proposed Datasets)"},
            "results": [
                {"model": "GCN", "is_proposed": False},
                {"model": "GINE", "is_proposed": False},
            ],
        },
    )

    finding = audit_single_paper("2206.08164", papers_root=tmp_path)

    assert finding is not None
    assert "benchmark paper has a proposed model name" in finding.reasons
    assert finding.benchmark_title is True


def test_audit_suggests_single_proposed_row_when_proposed_model_missing(tmp_path):
    _write_paper(
        tmp_path,
        "2310.01618",
        "PIGN: Efficient Path Integral Graph Networks",
        {
            "proposed_model": None,
            "results": [
                {"model": "PIGN", "is_proposed": True},
                {"model": "GCN", "is_proposed": False},
            ],
        },
    )

    finding = audit_single_paper("2310.01618", papers_root=tmp_path)

    assert finding is not None
    assert "proposed rows exist but proposed_model is missing" in finding.reasons
    assert finding.suggested_name == "PIGN"
    assert finding.candidate_names == ["PIGN"]


def test_audit_flags_rendering_artifacts_and_existing_renames(tmp_path):
    _write_paper(
        tmp_path,
        "2306.05955",
        "Path Neural Networks for Graph Classification",
        {
            "proposed_model": {"name": r"PathNN-\mathcal{SP}^+"},
            "results": [
                {"model": r"PathNN-\mathcal{SP}^+", "is_proposed": True},
                {"model": r"GCN from Ref.~\cite{dwivedi2022long}", "is_proposed": False},
            ],
        },
        overrides="paper_arxiv_id: '2306.05955'\nmodel_renames:\n  'GCN from Ref.~\\cite{dwivedi2022long}': 'GCN'\n",
    )

    finding = audit_single_paper("2306.05955", papers_root=tmp_path)

    assert finding is not None
    assert "proposed model name still contains LaTeX or citation text" in finding.reasons
    assert "result rows contain suspicious method labels" in finding.reasons
    assert finding.has_model_renames is True


def test_audit_method_names_skips_clean_papers(tmp_path):
    _write_paper(
        tmp_path,
        "2401.00001",
        "GraphGPS: General Powerful Scalable Graph Transformers",
        {
            "proposed_model": {"name": "GraphGPS"},
            "results": [
                {"model": "GraphGPS", "is_proposed": True},
                {"model": "GCN", "is_proposed": False},
            ],
        },
    )

    findings = audit_method_names(papers_root=tmp_path)

    assert findings == []
