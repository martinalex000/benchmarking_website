from scripts.audit_dataset_metadata import REQUIRED_DETAIL_SECTIONS, audit_dataset


def test_complete_dataset_metadata_passes_audit():
    dataset = {
        "description": "A concise description.",
        "detailed_description": dict.fromkeys(REQUIRED_DETAIL_SECTIONS, "Established information."),
        "sources": [{"title": "Primary source", "arxiv_id": "2401.00001"}],
    }

    assert audit_dataset(dataset) == []


def test_audit_reports_missing_sections_and_invalid_sources():
    dataset = {
        "description": "A concise description.",
        "detailed_description": {"task": "Known task."},
        "sources": [{"title": "No locator"}],
    }

    issues = audit_dataset(dataset)

    assert "missing detail section: data" in issues
    assert "source 1 is missing a URL or arXiv ID" in issues
