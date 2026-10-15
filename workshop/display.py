"""Small display helpers for notebooks."""

from __future__ import annotations

import html
import re

from IPython.display import HTML, Markdown, display

# A fenced block the way CommonMark sees it: the opening fence at line start, the closing fence on its own
# line; or an inline code span. Anything else is prose.
_CODE_SPAN = re.compile(r"^ {0,3}(```+|~~~+)[^\n]*\n.*?^ {0,3}\1[ \t]*$|`[^`\n]*`", re.DOTALL | re.MULTILINE)
_TAG_START = re.compile(r"<(?=[A-Za-z/!?])")
_LINK_DEST = re.compile(r"\]\(\s*([^)\s]*)")
_REF_DEF = re.compile(r"^( {0,3}\[[^\]\n]+\]):\s*(\S*)", re.MULTILINE)
_SAFE_DEST = re.compile(r"^(?:https?://|mailto:|#|/|\./|\.\./)", re.IGNORECASE)


def _neutralize_prose(part: str) -> str:
    """Escape HTML tags and break links whose destination is not an allowed scheme."""
    part = _TAG_START.sub("&lt;", part)
    part = _LINK_DEST.sub(lambda m: m.group(0) if _SAFE_DEST.match(m.group(1)) else "] (" + m.group(0)[2:], part)
    part = _REF_DEF.sub(
        lambda m: m.group(0) if _SAFE_DEST.match(m.group(2)) else m.group(1) + " " + m.group(0)[len(m.group(1)) :],
        part,
    )
    return part


def neutralize_html(text: str) -> str:
    """Make model output safe to render as Markdown.

    Model text is untrusted: a retrieved document or a tool result can smuggle HTML into it, and
    JupyterLab renders Markdown from a running kernel without sanitizing it. Outside code spans, HTML
    tags are escaped so they show as text, and links are kept only for http(s), mailto, anchors and
    relative paths, so javascript: and data: URLs cannot hide behind entities or odd spacing. Code
    spans are left alone so SPARQL IRIs such as <http://www.wikidata.org/entity/Q42> still display.
    """
    out, last = [], 0
    for m in _CODE_SPAN.finditer(text):
        out.append(_neutralize_prose(text[last : m.start()]))
        out.append(m.group(0))
        last = m.end()
    out.append(_neutralize_prose(text[last:]))
    return "".join(out)


def show_markdown(text: str) -> None:
    display(Markdown(neutralize_html(text)))


def show_table(rows: list[dict], columns: list[str] | None = None) -> None:
    """Render a list of dicts as an HTML table with escaped cells."""
    if not rows:
        display(HTML("<p><em>no rows</em></p>"))
        return
    columns = columns or list(rows[0].keys())
    head = "".join(f"<th style='text-align:left'>{html.escape(str(c))}</th>" for c in columns)
    body = "".join(
        "<tr>" + "".join(f"<td style='vertical-align:top'>{html.escape(str(r.get(c, '')))}</td>" for c in columns) + "</tr>"
        for r in rows
    )
    display(HTML(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"))


def stream_markdown(chunks) -> str:
    """Render a streaming ollama.chat response as it arrives; return the full text."""
    from IPython.display import clear_output

    text = ""
    for chunk in chunks:
        text += chunk.message.content or ""
        clear_output(wait=True)
        display(Markdown(neutralize_html(text)))
    return text
