import json

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Dataset, Paper, PendingDataset
from backend.pending_datasets import collect_pending_datasets


def test_pending_upsert_preserves_review_fields_and_payload(monkeypatch, tmp_path):
    root = tmp_path / "workspace"
    for name in ("data", "papers", "datasets", "logs", "config"):
        (root / name).mkdir(parents=True)
    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "data_dir", root / "data")
    monkeypatch.setattr(cfg, "papers_dir", root / "papers")
    monkeypatch.setattr(cfg, "datasets_dir", root / "datasets")
    monkeypatch.setattr(cfg, "logs_dir", root / "logs")
    monkeypatch.setattr(cfg, "config_dir", root / "config")
    monkeypatch.setattr(cfg, "db_path", root / "data" / "benchmarks.db")

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
    init_db()
    with session_scope() as session:
        session.add(Paper(arxiv_id="2501.12345", title="Pending paper"))
        session.add(Dataset(name="Resolved", task_type="graph_classification"))

    observation = {
        "name": "NovelGraphSet",
        "description": "A graph benchmark discovered in the paper.",
        "task_type": "graph_classification",
        "primary_metric": "Accuracy",
        "metrics_seen": ["Accuracy", "F1"],
        "expected_model_count": 12,
        "variant_hint": "large",
        "num_graphs": 5000,
        "statistics_mentioned": True,
    }
    raw = {"results": {"discovered_datasets": [observation], "results": []}}

    assert collect_pending_datasets("2501.12345", raw) == 1
    with session_scope() as session:
        row = session.query(PendingDataset).one()
        row.status = "approved"
        row.resolved_dataset_id = session.query(Dataset).filter_by(name="Resolved").one().id

    observation["expected_model_count"] = 14
    assert (
        collect_pending_datasets("2501.12345", {"results": {"discovered_datasets": [observation]}})
        == 1
    )
    with session_scope() as session:
        row = session.query(PendingDataset).one()
        assert row.status == "approved"
        assert row.resolved_dataset_id is not None
        assert row.metrics_seen_list == ["Accuracy", "F1"]
        assert json.loads(row.discovery_payload)["expected_model_count"] == 14
