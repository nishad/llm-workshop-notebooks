"""Small display helpers for notebooks."""

from __future__ import annotations

import html

from IPython.display import HTML, Markdown, display


def show_markdown(text: str) -> None:
    display(Markdown(text))


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
        display(Markdown(text))
    return text
