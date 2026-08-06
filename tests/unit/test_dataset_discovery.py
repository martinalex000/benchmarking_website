from backend.dataset_discovery import classify_dataset_info
from backend.llm_tasks import _merge_dataset_lists
from backend.llm_types import DatasetInfo, DatasetList


class _Query:
    def __init__(self, rows):
        self.rows = rows

    def all(self):
        return self.rows


class _Session:
    def __init__(self, datasets):
        self.datasets = datasets

    def query(self, _model):
        return _Query(self.datasets)


class _Dataset:
    def __init__(self, name, task_type, variants, **stats):
        self.name = name
        self.task_type = task_type
        self.variants = variants
        self.num_classes = stats.get("num_classes")
        self.num_graphs = stats.get("num_graphs")
        self.avg_nodes = stats.get("avg_nodes")
        self.avg_edges = stats.get("avg_edges")
        self.extra_stats = None


class _Variant:
    def __init__(self, name, dataset, *, standard=False, **stats):
        self.name = name
        self.dataset = dataset
        self.dataset_id = id(dataset)
        self.id = id(self)
        self.is_standard = standard
        self.num_graphs = stats.get("num_graphs")
        self.avg_nodes = stats.get("avg_nodes")
        self.avg_edges = stats.get("avg_edges")
        self.extra_stats = None


def test_cora_statistics_select_unique_variant():
    dataset = _Dataset("Cora", "node_classification", [])
    standard = _Variant("Planetoid split", dataset, standard=True, num_graphs=2708)
    random = _Variant("Random 10-fold", dataset, num_graphs=10000)
    dataset.variants = [standard, random]

    resolution = classify_dataset_info(
        _Session([dataset]), DatasetInfo(name="Cora", num_graphs=2708)
    )

    assert resolution.status == "tracked"
    assert resolution.variant is standard


def test_zinc_graph_count_selects_full_or_subset():
    dataset = _Dataset("ZINC", "graph_regression", [])
    subset = _Variant("Subset (12k)", dataset, num_graphs=12000)
    full = _Variant("Full", dataset, standard=True, num_graphs=249456)
    dataset.variants = [subset, full]
    session = _Session([dataset])

    assert (
        classify_dataset_info(session, DatasetInfo(name="ZINC", num_graphs=12000)).variant is subset
    )
    assert (
        classify_dataset_info(session, DatasetInfo(name="ZINC", num_graphs=249456)).variant is full
    )


def test_conflicting_statistics_and_unsupported_task_are_rejected():
    dataset = _Dataset("Cora", "node_classification", [])
    variant = _Variant("Planetoid split", dataset, standard=True, num_graphs=2708)
    dataset.variants = [variant]
    session = _Session([dataset])

    conflict = classify_dataset_info(session, DatasetInfo(name="Cora", num_graphs=1))
    unsupported = classify_dataset_info(
        session, DatasetInfo(name="Cora", task_type="image_generation")
    )

    assert conflict.status == "statistics_conflict"
    assert unsupported.status == "unsupported_task"


def test_unknown_variant_is_audit_only():
    dataset = _Dataset("Cora", "node_classification", [])
    dataset.variants = [_Variant("Planetoid split", dataset, standard=True)]

    resolution = classify_dataset_info(
        _Session([dataset]), DatasetInfo(name="Cora", variant_hint="Temporal split")
    )

    assert resolution.status == "unknown_variant"
    assert not resolution.tracked


def test_standard_variant_hint_is_understood():
    dataset = _Dataset("Cora", "node_classification", [])
    standard = _Variant("Planetoid split", dataset, standard=True)
    dataset.variants = [standard]

    resolution = classify_dataset_info(
        _Session([dataset]), DatasetInfo(name="Cora", variant_hint="standard")
    )

    assert resolution.status == "tracked"
    assert resolution.variant is standard


def test_discovery_merge_preserves_observed_metadata():
    merged = _merge_dataset_lists(
        DatasetList(
            datasets=[
                DatasetInfo(name="NovelGraphSet", description="graphs", primary_metric="Accuracy")
            ]
        ),
        DatasetList(
            datasets=[
                DatasetInfo(
                    name="NovelGraphSet",
                    task_type="graph_classification",
                    metrics_seen=["Accuracy", "F1"],
                    expected_model_count=8,
                    num_graphs=5000,
                    avg_nodes=12.5,
                    avg_edges=20.0,
                    num_classes=3,
                )
            ]
        ),
    )

    dataset = merged.datasets[0]
    assert dataset.description == "graphs"
    assert dataset.task_type == "graph_classification"
    assert dataset.metrics_seen == ["Accuracy", "F1"]
    assert dataset.expected_model_count == 8
    assert dataset.num_graphs == 5000
