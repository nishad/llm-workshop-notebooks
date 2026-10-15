"""Small display helpers for notebooks."""

from __future__ import annotations

import html
import re

from IPython.display import HTML, Markdown, display

_CODE_SPAN = re.compile(r"(```.*?```|`[^`\n]*`)", re.DOTALL)
_TAG_START = re.compile(r"<(?=[A-Za-z/!?])")
_UNSAFE_LINK = re.compile(r"\]\(\s*(?=(?:javascript|data|vbscript):)", re.IGNORECASE)


def neutralize_html(text: str) -> str:
    """Make model output safe to render as Markdown.

    Model text is untrusted: a retrieved document or a tool result can smuggle HTML into it, and
    JupyterLab renders Markdown from a running kernel without sanitizing it. HTML tags outside code
    spans are escaped so they show as text, and links to javascript:/data: URLs are broken. Code spans
    are left alone so SPARQL IRIs such as <http://www.wikidata.org/entity/Q42> still display.
    """
    parts = _CODE_SPAN.split(text)
    safe = []
    for i, part in enumerate(parts):
        if i % 2:  # odd parts are the code spans captured by the split
            safe.append(part)
        else:
            safe.append(_UNSAFE_LINK.sub("] (", _TAG_START.sub("&lt;", part)))
    return "".join(safe)


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
