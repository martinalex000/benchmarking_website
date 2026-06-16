from pathlib import Path

from scripts.mark_priority_papers import parse_priority_file


def test_parse_priority_file_skips_comments_and_dedupes(tmp_path: Path) -> None:
    path = tmp_path / "priority.txt"
    path.write_text(
        "\n".join(
            [
                "# header",
                "2005.00687  # OGB",
                "",
                "1706.08566",
                "2005.00687  # duplicate",
                "not-an-id",
            ]
        ),
        encoding="utf-8",
    )

    assert parse_priority_file(path) == ["2005.00687", "1706.08566"]
