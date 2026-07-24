"""Download and parse LaTeX source from arXiv papers.

Downloads the LaTeX source tarball from arXiv, runs ``latexpand`` to flatten
all ``\\input`` / ``\\include`` directives into a single file, then extracts:

  - All ``table`` / ``table*`` / ``longtable`` / ``wraptable`` /
    ``sidewaystable`` / ``sidewaystable*`` environments with captions
    (including appendix tables — missed by PDF/HTML extraction)
  - All section / subsection / subsubsection / paragraph headings and their
    content, with appendix-awareness

This provides qualitatively better context for LLM extraction than PDF-derived
plain text: result tables are structurally complete, and section boundaries are
explicit so experiment sections can be isolated.

Usage::

    from backend.latex_source import download_and_parse
    from backend.paper_storage import PaperStorage

    storage = PaperStorage("2206.08164")
    paper = download_and_parse("2206.08164", storage.latex_dir)
    if paper:
        print(paper.section_headings)
        print(paper.all_table_captions)
"""

from __future__ import annotations

import io
import logging
import re
import subprocess
import tarfile
import tempfile
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from backend.text_cleanup import clean_extracted_text

logger = logging.getLogger(__name__)

_ARXIV_SRC_URL = "https://arxiv.org/src/{arxiv_id}"
_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; GraphBenchBot/1.0)",
    "Accept-Encoding": "identity",  # prevent gzip so we can sniff magic bytes
}
MAX_SOURCE_DOWNLOAD_BYTES = 200 * 1024 * 1024
MAX_EXPANDED_SOURCE_BYTES = 500 * 1024 * 1024
MAX_SOURCE_ARCHIVE_MEMBERS = 5000
_DOWNLOAD_CHUNK_SIZE = 1024 * 1024

# Section levels we track, in order of specificity
_SECTION_LEVELS = ("section", "subsection", "subsubsection", "paragraph")

# Keywords that identify experiment-related sections (lower-case).
# These are used to select which section bodies are included in RAG context.
_EXPERIMENT_KEYWORDS = frozenset(
    {
        "experiment",
        "result",
        "evaluation",
        "benchmark",
        "comparison",
        "performance",
        "ablation",
        "analysis",
        "baseline",
        "main result",
        "empirical",
        "numerical",
        "leaderboard",
    }
)

_LATEXPAND = Path(__file__).parent / "latexpand"

# ── Data classes ───────────────────────────────────────────────────────────────


@dataclass
class LatexTable:
    """A table environment extracted from expanded LaTeX source."""

    number: int  # 1-based sequential counter across the document
    caption: str  # plain-text caption (LaTeX commands stripped)
    label: str  # value of \\label{...} or empty string
    body: str  # full raw LaTeX of the table environment
    in_appendix: bool = False

    @property
    def markdown(self) -> str:
        """Raw LaTeX body — LLMs read LaTeX tables well."""
        return self.body

    @property
    def header(self) -> str:
        """Raw LaTeX column-header rows: all rows between \\toprule and the first \\midrule.

        Returns the unstripped LaTeX so the LLM can see \\multicolumn, \\multirow, etc.
        Falls back to the first \\hline-delimited block or the very first data rows when
        neither \\toprule nor \\midrule is present.
        """
        # Locate the tabular body — after \begin{tabular...}{colspec}
        m = re.search(
            r"\\begin\{(?:tabular[*x]?|longtable|tabulary|tabu)\s*\}"
            r"(?:\s*\[[^\]]*\])?\s*\{[^}]*\}(.*?)(?=\\end\{)",
            self.body,
            re.DOTALL,
        )
        content = m.group(1) if m else self.body

        # Prefer the block between \toprule and first \midrule
        top_m = re.search(r"\\toprule(.*?)\\(?:midrule|hline)", content, re.DOTALL)
        if top_m:
            header_block = top_m.group(1)
        else:
            # No \toprule — take everything before the first \midrule / \hline
            parts = re.split(r"\\(?:midrule|hline)", content, maxsplit=1)
            header_block = parts[0]

        # Collect non-empty, non-rule rows from the header block
        rows: list[str] = []
        for row in re.split(r"\\\\", header_block):
            stripped = row.strip()
            if not stripped:
                continue
            if re.match(r"\\(?:toprule|midrule|cmidrule|bottomrule|hline|cline)", stripped):
                continue
            rows.append(stripped)

        if not rows:
            return ""
        # Join multiple header rows with \\  so the LLM sees the full structure
        return (" \\\\ ".join(rows))[:400]


@dataclass
class LatexSection:
    """A section/subsection/... with its raw LaTeX body."""

    level: str  # "section", "subsection", "subsubsection", "paragraph"
    title: str  # plain-text title (LaTeX commands stripped)
    content: str  # raw LaTeX content until the next section of the same or higher level
    in_appendix: bool = False

    @property
    def is_experiment_related(self) -> bool:
        title_lower = self.title.lower()
        return any(kw in title_lower for kw in _EXPERIMENT_KEYWORDS)


@dataclass
class LatexPaper:
    """Structured representation of a parsed LaTeX paper."""

    arxiv_id: str
    main_tex: str  # full expanded LaTeX
    tables: list[LatexTable] = field(default_factory=list)
    sections: list[LatexSection] = field(default_factory=list)

    # ── Derived views used by the extraction pipeline ─────────────────────

    @property
    def all_table_captions(self) -> str:
        """One-line summary of every table — compact yet informative for discovery."""
        lines: list[str] = []
        for t in self.tables:
            appendix = " [appendix]" if t.in_appendix else ""
            label = f" ({t.label})" if t.label else ""
            lines.append(f"Table {t.number}{label}{appendix}: {t.caption[:200]}")
        return "\n".join(lines)

    @property
    def section_headings(self) -> str:
        """Indented listing of all section headings with levels."""
        indent = {"section": "", "subsection": "  ", "subsubsection": "    ", "paragraph": "      "}
        lines: list[str] = []
        for s in self.sections:
            pad = indent.get(s.level, "")
            appendix = " [appendix]" if s.in_appendix else ""
            lines.append(f"{pad}\\{s.level}{{{s.title}}}{appendix}")
        return "\n".join(lines)

    @property
    def experiment_sections(self) -> list[LatexSection]:
        """All sections whose title suggests experiment/result content."""
        return [s for s in self.sections if s.is_experiment_related]

    @property
    def experiment_text(self) -> str:
        """Concatenated raw LaTeX content of all experiment-related sections."""
        parts: list[str] = []
        for s in self.experiment_sections:
            parts.append(f"=== {s.title} ===\n{s.content}")
        return "\n\n".join(parts)

    @property
    def intro_text(self) -> str:
        """Content of the introduction / first main section (up to 8 000 chars)."""
        for s in self.sections:
            if s.level == "section" and any(
                kw in s.title.lower() for kw in ("intro", "abstract", "overview", "preliminar")
            ):
                return s.content[:8_000]
        # Fallback: text before the first \\section{} command
        m = re.search(r"\\section\s*\*?\s*\{", self.main_tex)
        return (self.main_tex[: m.start()] if m else self.main_tex)[:8_000]


# ── Public entry point ─────────────────────────────────────────────────────────


def download_and_parse(
    arxiv_id: str,
    cache_dir: Path,
    force: bool = False,
) -> LatexPaper | None:
    """Download arXiv LaTeX source, expand, cache, and parse.

    Results are cached in *cache_dir*/expanded.tex so subsequent calls are
    instant.  Pass ``force=True`` to re-download and re-expand.

    Returns ``None`` when the source is unavailable or cannot be processed.
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    expanded_path = cache_dir / "expanded.tex"

    if not force and expanded_path.exists() and expanded_path.stat().st_size > 100:
        logger.info("Using cached LaTeX source for arXiv:%s", arxiv_id)
        tex = _strip_comment_environments(
            expanded_path.read_text(encoding="utf-8", errors="replace")
        )
        return _parse_expanded(arxiv_id, tex)

    # ── Download ───────────────────────────────────────────────────────────
    logger.info("Downloading LaTeX source for arXiv:%s", arxiv_id)
    url = _ARXIV_SRC_URL.format(arxiv_id=arxiv_id)
    try:
        req = urllib.request.Request(url, headers=_REQUEST_HEADERS)
        with urllib.request.urlopen(req, timeout=90) as resp:  # nosec B310
            src_bytes = _read_limited_response(resp, arxiv_id)
    except Exception as exc:
        logger.warning("Could not download LaTeX source for %s: %s", arxiv_id, exc)
        return None

    if not src_bytes:
        logger.warning("Empty response for LaTeX source of %s", arxiv_id)
        return None

    # ── Expand ─────────────────────────────────────────────────────────────
    tex = _expand_source(arxiv_id, src_bytes)
    if tex is None:
        return None

    # Cache
    expanded_path.write_text(tex, encoding="utf-8")
    logger.info("Cached expanded LaTeX for %s (%d chars)", arxiv_id, len(tex))
    return _parse_expanded(arxiv_id, tex)


# ── Download helpers ───────────────────────────────────────────────────────────


def _read_limited_response(resp, arxiv_id: str) -> bytes:
    """Read an HTTP response with an explicit in-memory size limit."""
    content_length = resp.headers.get("Content-Length")
    if content_length is not None:
        try:
            if int(content_length) > MAX_SOURCE_DOWNLOAD_BYTES:
                raise ValueError(f"LaTeX source for {arxiv_id} exceeds 200 MB download limit")
        except ValueError as exc:
            if "exceeds" in str(exc):
                raise
            logger.warning(
                "Ignoring invalid source Content-Length for %s: %r", arxiv_id, content_length
            )

    chunks: list[bytes] = []
    total = 0
    while True:
        chunk = resp.read(_DOWNLOAD_CHUNK_SIZE)
        if not chunk:
            break
        total += len(chunk)
        if total > MAX_SOURCE_DOWNLOAD_BYTES:
            raise ValueError(f"LaTeX source for {arxiv_id} exceeds 200 MB download limit")
        chunks.append(chunk)
    return b"".join(chunks)


def _expand_source(arxiv_id: str, src_bytes: bytes) -> str | None:
    """Extract tarball (or single .tex file) and run latexpand."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Detect whether it's a tarball or a bare .tex file
        if (
            src_bytes[:2] in (b"\x1f\x8b", b"BZ")
            or src_bytes[:5] == b"ustar"
            or (len(src_bytes) > 4 and src_bytes[:4] == b"PK\x03\x04")
            or _is_tar(src_bytes)
        ):
            main_tex = _extract_tarball(src_bytes, tmppath, arxiv_id)
        elif b"\\documentclass" in src_bytes[:4096] or b"\\begin{document}" in src_bytes[:4096]:
            # Bare .tex file
            main_tex = tmppath / "main.tex"
            main_tex.write_bytes(src_bytes)
        else:
            # Try treating as tarball anyway (some arXiv responses have no magic bytes)
            main_tex = _extract_tarball(src_bytes, tmppath, arxiv_id)
            if main_tex is None:
                logger.warning("Cannot parse source format for %s", arxiv_id)
                return None

        if main_tex is None:
            return None

        return _run_latexpand(main_tex, tmppath, arxiv_id)


def _is_tar(data: bytes) -> bool:
    """Check whether data looks like a tar archive."""
    try:
        with tarfile.open(fileobj=io.BytesIO(data)):
            return True
    except tarfile.TarError:
        return False


def _extract_tarball(src_bytes: bytes, dest: Path, arxiv_id: str) -> Path | None:
    """Extract tarball to dest and return path to the main .tex file."""
    try:
        with tarfile.open(fileobj=io.BytesIO(src_bytes)) as tar:
            members = tar.getmembers()
            if len(members) > MAX_SOURCE_ARCHIVE_MEMBERS:
                raise ValueError(
                    f"Source archive for {arxiv_id} has too many files: {len(members)}"
                )
            total_size = sum(member.size for member in members if member.isfile())
            if total_size > MAX_EXPANDED_SOURCE_BYTES:
                raise ValueError(f"Source archive for {arxiv_id} expands beyond 500 MB")
            tar.extractall(dest, filter="data")  # Python 3.12+ safe extraction
    except (tarfile.TarError, ValueError) as exc:
        logger.warning("Tarball extraction failed for %s: %s", arxiv_id, exc)
        return None
    return _find_main_tex(dest)


def _find_main_tex(root: Path) -> Path | None:
    """Find the main LaTeX file (the one containing \\documentclass)."""
    tex_files = sorted(root.rglob("*.tex"), key=lambda p: p.stat().st_size, reverse=True)
    if not tex_files:
        return None
    for f in tex_files:
        try:
            head = f.read_bytes()[:4096]
            if b"\\documentclass" in head:
                return f
        except OSError:
            continue
    # Fallback: the largest .tex file
    return tex_files[0]


def _run_latexpand(main_tex: Path, cwd: Path, arxiv_id: str) -> str:
    """Run latexpand on *main_tex* and remove explicit comment environments."""
    try:
        result = subprocess.run(
            ["perl", str(_LATEXPAND), str(main_tex)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=str(cwd),
        )
        if result.returncode == 0 and result.stdout.strip():
            logger.debug("latexpand succeeded for %s (%d chars)", arxiv_id, len(result.stdout))
            return _strip_comment_environments(result.stdout)
        logger.warning(
            "latexpand returned exit %d for %s: %s",
            result.returncode,
            arxiv_id,
            result.stderr[:200],
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
        logger.warning("latexpand unavailable/timed out for %s: %s", arxiv_id, exc)

    # Fallback: read the main file directly (\\input directives will be unresolved)
    return _strip_comment_environments(main_tex.read_text(encoding="utf-8", errors="replace"))


_COMMENT_BEGIN_LINE = re.compile(r"^[ \t]*\\begin\{comment\}[ \t]*$")
_COMMENT_END_LINE = re.compile(r"^[ \t]*\\end\{comment\}(?=[ \t]|$)")


def _strip_comment_environments(tex: str) -> str:
    """Remove balanced, line-oriented ``comment`` environments conservatively.

    The bundled latexpand removes percent comments but intentionally does not
    interpret the ``comment`` package.  Only standalone begin/end lines are
    recognized here.  If a block is unbalanced, it is preserved rather than
    risking removal of real document content.
    """
    output: list[str] = []
    block: list[str] = []
    depth = 0

    for line in tex.splitlines(keepends=True):
        line_without_newline = line.rstrip("\r\n")
        if _COMMENT_BEGIN_LINE.fullmatch(line_without_newline):
            if depth == 0:
                block = []
            block.append(line)
            depth += 1
            continue

        if depth:
            end_match = _COMMENT_END_LINE.match(line_without_newline)
            if end_match:
                depth -= 1
                suffix = line[end_match.end() :]
                if depth == 0:
                    block = []
                    if suffix.strip():
                        output.append(suffix)
                else:
                    if suffix.strip():
                        block.append(suffix)
                continue

            block.append(line)
            continue

        output.append(line)

    if depth:
        logger.warning(
            "Unbalanced \\begin{comment} environment in expanded LaTeX; preserving its content"
        )
        output.extend(block)

    return "".join(output)


# ── User macro expansion ───────────────────────────────────────────────────────


# Regex matching the expansion body with up to 2 levels of nested braces.
# Covers the vast majority of dataset-name macros like:
#   \newcommand{\foo}{Bar}          → Bar
#   \newcommand{\foo}{\textit{Bar}} → \textit{Bar}  (stripped later)
_EXPANSION_BODY = r"(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*"

_NEWCMD_RE = re.compile(
    r"\\(?:new|renew)command\s*\*?\s*"
    r"(?:\{\\([a-zA-Z]{3,})\}|\\([a-zA-Z]{3,}))"  # {\cmdname} or \cmdname
    r"\s*(?:\[0\])?"  # explicit zero-arg form like \newcommand\foo[0]{...}
    r"\s*(?!\[[1-9])"  # NOT followed by [N] for N>=1 arguments
    r"\{(" + _EXPANSION_BODY + r")\}",
)

_DEF_RE = re.compile(
    r"\\def\s*\\([a-zA-Z]{3,})\s*"  # \def\cmdname  — ≥ 3 chars
    r"(?!#)"  # NOT a parametric \def\foo#1{...}
    r"\{(" + _EXPANSION_BODY + r")\}",
)


def _expand_user_macros(tex: str) -> tuple[str, dict[str, str]]:
    """Extract zero-argument \\newcommand / \\renewcommand / \\def macros and expand them.

    Only expands macros whose names are ≥ 3 characters (to avoid stomping on
    standard LaTeX one-/two-letter commands) and which take no arguments.
    Applies up to 3 substitution passes so chained macros (e.g.
    ``\\lrgb`` → ``\\pascal, ...`` → actual names) resolve correctly.

    Returns ``(expanded_tex, macro_map)`` where *macro_map* maps command
    name → raw expansion string (may still contain LaTeX markup, which
    ``_strip_latex`` will clean up later).
    """
    macro_map: dict[str, str] = {}

    for m in _NEWCMD_RE.finditer(tex):
        name = m.group(1) or m.group(2)
        expansion = m.group(3)
        macro_map[name] = expansion

    for m in _DEF_RE.finditer(tex):
        if m.group(1) not in macro_map:  # \newcommand takes priority over \def
            macro_map[m.group(1)] = m.group(2)

    if not macro_map:
        return tex, macro_map

    logger.debug(
        "Found %d user-defined macros: %s",
        len(macro_map),
        list(macro_map)[:15],
    )

    # Apply substitutions — longest name first (avoids \foo clobbering \foobar),
    # up to 3 passes to handle macro chains.
    for _pass in range(3):
        prev = tex
        for name in sorted(macro_map, key=len, reverse=True):
            # Match \name NOT followed by a letter or @ (avoids partial matches)
            tex = re.sub(
                r"\\" + re.escape(name) + r"(?![a-zA-Z@])",
                lambda m, exp=macro_map[name]: exp,
                tex,
            )
        if tex == prev:
            break  # nothing changed — no point in further passes

    return tex, macro_map


# ── LaTeX parsing ──────────────────────────────────────────────────────────────


def _parse_expanded(arxiv_id: str, tex: str) -> LatexPaper:
    """Parse expanded LaTeX into structured components."""
    tex, macro_map = _expand_user_macros(tex)
    if macro_map:
        logger.info(
            "Expanded %d user-defined macros for %s: %s",
            len(macro_map),
            arxiv_id,
            list(macro_map)[:10],
        )
    tables = _extract_tables(tex)
    sections = _extract_sections(tex)
    return LatexPaper(arxiv_id=arxiv_id, main_tex=tex, tables=tables, sections=sections)


# ── Table extraction ───────────────────────────────────────────────────────────

# Longer names first so ``table*`` is not matched as ``table``.
TABLE_ENV_NAMES: tuple[str, ...] = (
    "sidewaystable*",
    "sidewaystable",
    "table*",
    "table",
    "longtable",
    "wraptable",
)

_TABLE_BEGIN_PAT = re.compile(
    r"\\begin\{(" + "|".join(re.escape(name) for name in TABLE_ENV_NAMES) + r")\}"
)


@dataclass
class LatexTableSpan:
    """Character span of a parsed table-like LaTeX environment."""

    env_name: str
    start: int
    end: int


@dataclass
class LatexTableDiagnostic:
    """Heuristic LaTeX table-coverage issue for one paper."""

    kind: Literal["wraptable", "sidewaystable", "unparsed_tabular_lines"]
    detail: str
    sample_lines: list[str] = field(default_factory=list)


def _extract_tables_with_spans(tex: str) -> tuple[list[LatexTable], list[LatexTableSpan]]:
    """Extract table-like environments and their source spans."""
    appendix_pos = _find_appendix_start(tex)

    tables: list[LatexTable] = []
    spans: list[LatexTableSpan] = []
    table_number = 0

    for m in _TABLE_BEGIN_PAT.finditer(tex):
        env_name = m.group(1)
        env_end = _find_matching_end(tex, m.start(), env_name)
        if env_end is None:
            continue

        body = tex[m.start() : env_end]
        table_number += 1

        caption = _strip_latex(_extract_caption_text(body))
        label = _extract_label_text(body)

        tables.append(
            LatexTable(
                number=table_number,
                caption=caption,
                label=label,
                body=body,
                in_appendix=m.start() >= appendix_pos,
            )
        )
        spans.append(LatexTableSpan(env_name=env_name, start=m.start(), end=env_end))

    return tables, spans


def _extract_tables(tex: str) -> list[LatexTable]:
    """Extract all supported table-like LaTeX environments."""
    tables, _spans = _extract_tables_with_spans(tex)
    return tables


def _blank_spans(tex: str, spans: list[LatexTableSpan]) -> str:
    chars = list(tex)
    for span in sorted(spans, key=lambda item: item.start, reverse=True):
        for index in range(span.start, span.end):
            chars[index] = " "
    return "".join(chars)


def _find_unparsed_tabular_lines(
    tex: str,
    spans: list[LatexTableSpan],
    *,
    min_ampersands: int = 2,
    max_samples: int = 3,
) -> list[str]:
    """Return sample lines with column separators outside parsed table environments."""
    uncovered = _blank_spans(tex, spans)
    hits: list[str] = []
    for line in uncovered.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("%"):
            continue
        if stripped.count("&") < min_ampersands:
            continue
        hits.append(stripped[:240])
        if len(hits) >= max_samples:
            break
    return hits


def diagnose_latex_table_coverage(tex: str) -> list[LatexTableDiagnostic]:
    """Flag LaTeX sources whose benchmark tables may have been missed by the parser."""
    tables, spans = _extract_tables_with_spans(tex)
    diagnostics: list[LatexTableDiagnostic] = []

    wrap_count = len(re.findall(r"\\begin\{wraptable\}", tex))
    if wrap_count:
        parsed_wrap = sum(1 for span in spans if span.env_name == "wraptable")
        diagnostics.append(
            LatexTableDiagnostic(
                kind="wraptable",
                detail=(
                    f"Contains {wrap_count} wraptable environment(s); parsed {parsed_wrap}. "
                    "Papers processed before wraptable support need full LLM re-extraction."
                ),
            )
        )

    sideways_count = len(re.findall(r"\\begin\{(?:sidewaystable\*?)\}", tex))
    if sideways_count:
        parsed_sideways = sum(
            1 for span in spans if span.env_name in {"sidewaystable", "sidewaystable*"}
        )
        diagnostics.append(
            LatexTableDiagnostic(
                kind="sidewaystable",
                detail=(
                    f"Contains {sideways_count} sidewaystable environment(s); "
                    f"parsed {parsed_sideways}. Rotated tables may need re-extraction "
                    "if processed with an older parser."
                ),
            )
        )

    unparsed_lines = _find_unparsed_tabular_lines(tex, spans)
    if unparsed_lines:
        diagnostics.append(
            LatexTableDiagnostic(
                kind="unparsed_tabular_lines",
                detail=(
                    "Found lines with two or more '&' column separators outside parsed "
                    "table environments (possible standalone tabular or unsupported layout)."
                ),
                sample_lines=unparsed_lines,
            )
        )

    _ = tables
    return diagnostics


def scan_latex_source_file(path: Path) -> list[LatexTableDiagnostic]:
    """Load expanded LaTeX from *path* and return table-coverage diagnostics."""
    if not path.is_file():
        return []
    tex = path.read_text(encoding="utf-8", errors="replace")
    return diagnose_latex_table_coverage(tex)


_APPENDIX_HEADING_RE = re.compile(
    r"^(?:appendix|appendices|supplement(?:ary)?(?:\s+(?:material|information))?"
    r"|supplemental(?:\s+(?:material|information))?)\b",
    re.IGNORECASE,
)
_SECTION_HEADING_RE = re.compile(
    r"\\(?:part|chapter|section|subsection|subsubsection|paragraph)\s*\*?\s*\{([^}]*)\}",
    re.DOTALL,
)


def _find_appendix_start(tex: str) -> int:
    """Return the first explicit appendix/supplement boundary, if any."""
    positions: list[int] = []
    directive = re.search(r"\\appendix\b", tex)
    if directive:
        positions.append(directive.start())

    for heading in _SECTION_HEADING_RE.finditer(tex):
        title = _strip_latex(heading.group(1)).strip()
        if _APPENDIX_HEADING_RE.match(title):
            positions.append(heading.start())

    return min(positions) if positions else len(tex)


def _find_matching_end(tex: str, begin_pos: int, env_name: str) -> int | None:
    """Return the position *after* the \\end{env_name} that matches \\begin at begin_pos."""
    begin_re = re.compile(r"\\begin\{" + re.escape(env_name) + r"\}")
    end_re = re.compile(r"\\end\{" + re.escape(env_name) + r"\}")

    # Skip past the opening \begin{env_name}
    pos = begin_pos + len(f"\\begin{{{env_name}}}")
    depth = 1

    while pos < len(tex) and depth > 0:
        nb = begin_re.search(tex, pos)
        ne = end_re.search(tex, pos)

        if ne is None:
            return None  # unmatched

        if nb is not None and nb.start() < ne.start():
            depth += 1
            pos = nb.end()
        else:
            depth -= 1
            if depth == 0:
                return ne.end()
            pos = ne.end()

    return None


def _extract_caption_text(body: str) -> str:
    """Extract text from \\caption{...} handling nested braces."""
    m = re.search(r"\\caption\s*\{", body)
    if not m:
        # Try \caption[short]{long}
        m = re.search(r"\\caption\s*\[[^\]]*\]\s*\{", body)
        if not m:
            return ""
    start = m.end()
    depth = 1
    pos = start
    while pos < len(body) and depth > 0:
        if body[pos] == "{" and (pos == 0 or body[pos - 1] != "\\"):
            depth += 1
        elif body[pos] == "}" and (pos == 0 or body[pos - 1] != "\\"):
            depth -= 1
        pos += 1
    return body[start : pos - 1]


def _extract_label_text(body: str) -> str:
    """Extract \\label{...} value."""
    m = re.search(r"\\label\s*\{([^}]+)\}", body)
    return m.group(1) if m else ""


# ── Section extraction ─────────────────────────────────────────────────────────


def _extract_sections(tex: str) -> list[LatexSection]:
    """Extract all section-level headings with their content bodies."""
    appendix_pos = _find_appendix_start(tex)

    # Match \section*{...}, \subsection{...}, etc.
    heading_pat = re.compile(
        r"\\(section|subsection|subsubsection|paragraph)\s*\*?\s*\{([^}]*)\}",
        re.DOTALL,
    )

    matches = list(heading_pat.finditer(tex))
    sections: list[LatexSection] = []

    for i, m in enumerate(matches):
        level = m.group(1)
        title = _strip_latex(m.group(2).strip())

        content_start = m.end()
        content_end = matches[i + 1].start() if i + 1 < len(matches) else len(tex)
        content = tex[content_start:content_end]

        sections.append(
            LatexSection(
                level=level,
                title=title,
                content=content,
                in_appendix=m.start() >= appendix_pos,
            )
        )

    return sections


# ── LaTeX markup stripping ─────────────────────────────────────────────────────


def _strip_latex(text: str) -> str:
    """Strip common LaTeX markup to produce readable plain text."""
    # Remove comments
    text = re.sub(r"%[^\n]*", "", text)
    text = text.replace("~", " ")
    # Normalize explicit LaTeX line breaks before removing bare commands, or
    # sequences like "\\with" lose the following word entirely.
    text = re.sub(r"\\\\(?:\s*\[[^\]]*\])?", " ", text)
    text = re.sub(r"\\(?:newline|linebreak)\b", " ", text)
    text = re.sub(r"\\xspace\b", " ", text)
    # Remove \footnote{...} (and similar whole-arg commands we don't want)
    for cmd in ("footnote", "footnotetext", "label", "cite", "citep", "citet", "ref", "url"):
        text = re.sub(r"\\" + cmd + r"\s*\{[^}]*\}", "", text)
    # Keep content of formatting commands: \textbf{x} → x
    for _ in range(3):  # iterate to handle nested
        text = re.sub(
            r"\\(?:text[a-zA-Z]+|emph|mbox|mathbf|mathrm|mathit|mathsf|mathtt|operatorname)\s*\{([^{}]*)\}",
            r"\1",
            text,
        )
    # Remove remaining \command{...} — drop argument
    text = re.sub(r"\\[a-zA-Z@]+\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}", " ", text)
    # Remove remaining bare \command
    text = re.sub(r"\\[a-zA-Z@]+\s*", " ", text)
    # Remove leftover braces
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\s+([:;,!.?])", r"\1", text)
    return clean_extracted_text(text)
