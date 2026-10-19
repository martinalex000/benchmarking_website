"""Conservative contradiction checks for source-scoped repetition protocols."""

import re


def protocol_consistency_errors(protocol: dict, source: str) -> list[str]:
    """Reject omitted CV cycles; never infer a replacement count or broader scope."""
    if protocol.get("design") != "single_cv":
        return []
    lines = source.splitlines()
    spans = protocol.get("evidence", [])
    if not spans:
        return ["missing_protocol_evidence"]
    texts = []
    for span in spans:
        start, end = span.get("start_line"), span.get("end_line")
        if type(start) is not int or type(end) is not int or not 1 <= start <= end <= len(lines):
            return ["invalid_protocol_evidence"]
        texts.append("\n".join(lines[start - 1 : end]))
    text = re.sub(r"[${}~]", " ", "\n".join(texts))
    for word, number in (("two", 2), ("three", 3), ("five", 5), ("ten", 10), ("twenty", 20)):
        text = re.sub(rf"\b{word}\b", str(number), text, flags=re.I)
    # Restrict this guard to explicit repetitions of the overall experiment.
    # A caption's '10 runs' alone cannot distinguish folds from full CV cycles.
    repetitions = re.findall(
        r"\b(?:perform(?:ing|ed)?|repeat(?:ing|ed)?)\s+(?:the\s+)?overall\s+"
        r"experiments?\s+(\d+)\s+times\b",
        text,
        flags=re.I,
    )
    if any(int(count) > 1 for count in repetitions):
        return ["single_cv_omits_explicit_overall_repetitions"]
    return []
