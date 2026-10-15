"""Small display helpers for notebooks."""

from __future__ import annotations

import html

from IPython.display import HTML, display
from markdown_it import MarkdownIt

# Raw HTML is disabled: model output is untrusted, and JupyterLab renders output from a running kernel
# without sanitizing it. markdown-it also refuses javascript:, vbscript:, file: and data: links by default.
_MARKDOWN = MarkdownIt("commonmark", {"html": False, "linkify": False, "typographer": False}).enable("table")


def render_markdown(text: str) -> str:
    """Render model Markdown to HTML with raw HTML shown as text, so markup smuggled into a retrieved
    document or a tool result cannot run in the notebook."""
    return _MARKDOWN.render(text)


def show_markdown(text: str) -> None:
    display(HTML(render_markdown(text)))


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
        display(HTML(render_markdown(text)))
    return text
