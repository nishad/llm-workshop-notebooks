from workshop import display


def test_neutralize_html_escapes_tags_outside_code():
    out = display.neutralize_html('Hello <img src=x onerror="alert(1)"> **world** <script>x</script>')
    assert "<img" not in out and "<script" not in out
    assert "&lt;img" in out and "**world**" in out


def test_neutralize_html_keeps_code_spans_intact():
    text = (
        "Query:\n```sparql\nSELECT ?s WHERE { ?s ?p <http://example.org/x> }\n```\n"
        "and `<http://www.wikidata.org/entity/Q42>` inline, and 1 < 2 in prose.\n"
        "~~~\n<b>tilde fence</b>\n~~~\n"
    )
    assert display.neutralize_html(text) == text


def test_neutralize_html_only_trusts_real_fences():
    midline = "text ```\n\n<img src=x onerror=alert(1)>\n\n```"
    assert "<img" not in display.neutralize_html(midline)
    unterminated = "```python\nprint(1)\n<img src=x onerror=alert(1)>"
    assert "<img" not in display.neutralize_html(unterminated)


def test_neutralize_html_allow_lists_link_destinations():
    text = (
        "[a](javascript:alert(1)) [b](&#106;avascript:alert(1)) [c](java\tscript:alert(1)) "
        "![d](data:image/svg+xml;base64,AAA) [e](https://example.org) [f](mailto:a@b.c) [g](#top) [h](./x.md)"
    )
    out = display.neutralize_html(text)
    for broken in ("[a] (", "[b] (", "[c] (", "![d] ("):
        assert broken in out
    for kept in ("[e](https://example.org)", "[f](mailto:a@b.c)", "[g](#top)", "[h](./x.md)"):
        assert kept in out


def test_neutralize_html_breaks_unsafe_reference_definitions():
    out = display.neutralize_html("[id]: javascript:alert(1)\n[ok]: https://example.org/\n[text][id]")
    assert "[id] : javascript:" in out and "[ok]: https://example.org/" in out


def test_neutralize_html_is_idempotent():
    text = "x < y, <b>bold</b>, [a](javascript:x), `<kept>`"
    once = display.neutralize_html(text)
    assert display.neutralize_html(once) == once
