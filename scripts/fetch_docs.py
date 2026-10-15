"""Fetch the openly licensed documents for the RAG exercise and convert them to text.

Usage: uv run python scripts/fetch_docs.py          (writes data/docs/*.md; raw files in data/raw/)
IFLA LRM is CC BY 4.0, DCMI Terms CC BY 4.0, the SKOS Reference may be copied under the W3C Document Licence
(fetched for local use only, not committed).
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import requests

from workshop.config import USER_AGENT

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
DOCS = ROOT / "data" / "docs"
IFLA_LRM_HANDLE = "https://repository.ifla.org/handle/20.500.14598/40"
DCMI_TERMS = "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/"
SKOS_REFERENCE = "https://www.w3.org/TR/skos-reference/"
_BITSTREAM = re.compile(r'href="((?:https://repository\.ifla\.org)?/bitstreams/[0-9a-f-]+/download)"')


class _Text(HTMLParser):
    SKIP = {"script", "style", "nav", "header", "footer"}
    HEAD = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### "}

    def __init__(self):
        super().__init__()
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1
        elif tag in self.HEAD:
            self.parts.append("\n\n" + self.HEAD[tag])
        elif tag in ("p", "li", "tr", "br", "div"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def html_to_text(html: str) -> str:
    parser = _Text()
    parser.feed(html)
    text = "".join(parser.parts)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def pdf_to_text(path: Path) -> str:
    from pypdf import PdfReader

    return "\n\n".join((p.extract_text() or "") for p in PdfReader(str(path)).pages)


def _get(url: str) -> requests.Response:
    r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=120)
    r.raise_for_status()
    return r


def _ifla_pdf() -> bytes:
    """The repository is DSpace: the page links bitstreams, not .pdf files, and one of them is an HTML stub."""
    page = _get(IFLA_LRM_HANDLE).text
    tried: list[str] = []
    for href in _BITSTREAM.findall(page):
        url = href if href.startswith("http") else "https://repository.ifla.org" + href
        if url in tried:
            continue
        tried.append(url)
        content = _get(url).content
        if content.startswith(b"%PDF"):
            return content
    raise SystemExit("Could not find the IFLA LRM PDF; download it manually to data/raw/ifla-lrm.pdf")


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    pdf = RAW / "ifla-lrm.pdf"
    if not pdf.exists():
        pdf.write_bytes(_ifla_pdf())
    (DOCS / "ifla-lrm.md").write_text(
        "# IFLA Library Reference Model (text extract)\n\nSource: " + IFLA_LRM_HANDLE + " (CC BY 4.0)\n\n" + pdf_to_text(pdf),
        encoding="utf-8",
    )
    (DOCS / "dcmi-terms.md").write_text(
        "# DCMI Metadata Terms (text extract)\n\nSource: " + DCMI_TERMS + " (CC BY 4.0)\n\n" + html_to_text(_get(DCMI_TERMS).text),
        encoding="utf-8",
    )
    (RAW / "skos-reference.md").write_text(html_to_text(_get(SKOS_REFERENCE).text), encoding="utf-8")
    for p in DOCS.glob("*.md"):
        print(f"{p.name}: {len(p.read_text(encoding='utf-8').split())} words")


if __name__ == "__main__":
    sys.exit(main())
