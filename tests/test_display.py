from workshop import display


def test_neutralize_html_escapes_tags_outside_code():
    out = display.neutralize_html('Hello <img src=x onerror="alert(1)"> **world** <script>x</script>')
    assert "<img" not in out and "<script" not in out
    assert "&lt;img" in out and "**world**" in out


def test_neutralize_html_keeps_code_spans_intact():
    text = (
        "Query:\n```sparql\nSELECT ?s WHERE { ?s ?p <http://example.org/x> }\n```\n"
        "and `<http://www.wikidata.org/entity/Q42>` inline, and 1 < 2 in prose."
    )
    assert display.neutralize_html(text) == text


def test_neutralize_html_breaks_script_links():
    out = display.neutralize_html("[click](javascript:alert(1)) and [ok](https://example.org)")
    assert "](javascript:" not in out and "](https://example.org)" in out
