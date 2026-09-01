from backend.extraction_runner import (
    _failed_core_extraction_calls,
    _failed_core_extraction_reasons,
)
from backend.llm_types import CallRecord


def _call(call_type: str, *, success: bool, parse_error: str | None = None) -> CallRecord:
    return CallRecord(
        call_type=call_type,
        system_prompt="",
        user_content="",
        success=success,
        parse_error=parse_error,
    )


def test_failed_core_calls_are_reported_but_statistics_failures_are_nonfatal() -> None:
    records = [
        _call("extract_dataset:CIFAR10", success=False, parse_error="connection error"),
        _call("extract_dataset_statistics", success=False, parse_error="connection error"),
        _call("extract_sota_claims", success=False, parse_error="connection error"),
    ]

    assert _failed_core_extraction_calls(records) == ["extract_dataset:CIFAR10: connection error"]


def test_successful_core_calls_do_not_block_promotion() -> None:
    records = [
        _call("discover_datasets:latex", success=True),
        _call("select_tables:all", success=True),
        _call("extract_dataset:CIFAR10", success=True),
    ]

    assert _failed_core_extraction_calls(records) == []


def test_failed_notes_are_detected_when_transport_errors_have_no_call_record() -> None:
    output = {
        "results": {
            "results": [],
            "extraction_notes": "[CIFAR10] failed: Connection error\n[metadata] ok",
        }
    }

    assert _failed_core_extraction_reasons(output, []) == ["[CIFAR10] failed: Connection error"]
