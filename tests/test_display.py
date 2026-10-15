from workshop import display


def test_render_markdown_escapes_raw_html():
    out = display.render_markdown('Hello <img src=x onerror="alert(1)"> **world** <script>x</script>')
    assert "<img" not in out and "<script" not in out
    assert "&lt;img" in out and "<strong>world</strong>" in out


def test_render_markdown_keeps_code_readable():
    out = display.render_markdown(
        "Query:\n```sparql\nSELECT ?s WHERE { ?s ?p <http://example.org/x> }\n```\n"
        "and `<http://www.wikidata.org/entity/Q42>` inline, and 1 < 2 in prose."
    )
    assert '<pre><code class="language-sparql">' in out
    assert "&lt;http://example.org/x&gt;" in out
    assert "<code>&lt;http://www.wikidata.org/entity/Q42&gt;</code>" in out
    assert "1 &lt; 2" in out


def test_render_markdown_drops_unsafe_links_and_keeps_safe_ones():
    out = display.render_markdown(
        "[a](javascript:alert(1)) [b](&#106;avascript:alert(1)) [c](java\tscript:alert(1)) "
        "![d](data:image/svg+xml;base64,AAA) [e](https://example.org) [f](mailto:a@b.c) [g](#top)"
    )
    assert out.count("<a ") == 3 and "<img" not in out
    assert 'href="javascript' not in out.lower()
    assert '<a href="https://example.org">e</a>' in out
    assert '<a href="mailto:a@b.c">f</a>' in out and '<a href="#top">g</a>' in out


def test_render_markdown_blocks_reference_definitions_and_script_autolinks():
    out = display.render_markdown(
        "[id]: javascript:alert(1)\n\n[text][id] and <https://example.org> and <javascript:alert(1)>"
    )
    assert out.count("<a ") == 1 and 'href="https://example.org"' in out
    assert "&lt;javascript:alert(1)&gt;" in out


def test_render_markdown_is_not_fooled_by_fence_tricks():
    for text in (
        "text ```\n\n<img src=x onerror=alert(1)>\n\n```",
        "\\`<img src=x onerror=alert(1)>\\`",
        "```a`b\n<img src=x onerror=1>\n```",
    ):
        out = display.render_markdown(text)
        assert "<img" not in out and "&lt;img" in out


def test_render_markdown_renders_tables():
    out = display.render_markdown("| a | b |\n|---|---|\n| <b>x</b> | 1 < 2 |")
    assert "<table>" in out and "<td>&lt;b&gt;x&lt;/b&gt;</td>" in out
