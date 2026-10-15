from scripts import fetch_docs


def test_html_to_text_keeps_headings_and_paragraphs():
    html = "<html><body><h2>Terms</h2><p>dcterms:title<br>A name given to the resource.</p><script>x()</script></body></html>"
    text = fetch_docs.html_to_text(html)
    assert "## Terms" in text
    assert "A name given to the resource." in text
    assert "x()" not in text
