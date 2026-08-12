from scripts.audit_dataset_metadata import REQUIRED_DETAIL_SECTIONS, audit_dataset


def test_complete_dataset_metadata_passes_audit():
    dataset = {
        "short_description": "Predict molecular activity from a graph.",
        "description": "**Binary graph classification** predicting activity. Evaluated by AP.",
        "detailed_description": dict.fromkeys(REQUIRED_DETAIL_SECTIONS, "Established information."),
        "sources": [{"title": "Primary source", "arxiv_id": "2401.00001"}],
    }

    assert audit_dataset(dataset) == []


def test_audit_reports_missing_sections_and_invalid_sources():
    dataset = {
        "short_description": "Predict a label.",
        "description": "A concise description.",
        "detailed_description": {"task": "Known task."},
        "sources": [{"title": "No locator"}],
    }

    issues = audit_dataset(dataset)

    assert "missing detail section: data" in issues
    assert "source 1 is missing a URL or arXiv ID" in issues


def test_audit_requires_task_first_short_description():
    dataset = {
        "short_description": "Predict a label.",
        "description": "A general overview without a task or metric.",
        "detailed_description": dict.fromkeys(REQUIRED_DETAIL_SECTIONS, "Known information."),
        "sources": [{"title": "Primary source", "arxiv_id": "2401.00001"}],
    }

    issues = audit_dataset(dataset)

    assert "concise description lacks a bold task specification" in issues
    assert "concise description lacks the evaluation metric" in issues


def test_audit_rejects_missing_or_formatted_one_line_description():
    dataset = {
        "short_description": "**Node classification** Predict a label.",
        "description": "**Node classification** Predict a label. Evaluated by Accuracy.",
        "detailed_description": dict.fromkeys(REQUIRED_DETAIL_SECTIONS, "Known information."),
        "sources": [{"title": "Primary source", "arxiv_id": "2401.00001"}],
    }

    assert "one-line description contains presentation markup" in audit_dataset(dataset)
