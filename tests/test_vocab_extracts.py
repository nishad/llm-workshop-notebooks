from pathlib import Path

import rdflib

from scripts import build_vocab_extracts as bve

FIX = Path(__file__).parent / "fixtures" / "mini.ttl"


def _graph():
    g = rdflib.Graph()
    g.parse(str(FIX), format="turtle")
    return g


def test_extract_all_concepts():
    concepts = {c["id"]: c for c in bve.extract_concepts(_graph())}
    assert set(concepts) == {"http://example.org/c1", "http://example.org/c0"}
    c1 = concepts["http://example.org/c1"]
    assert c1["pref"] == {"de": "Bibliothek", "en": "Library"}
    assert c1["alt"] == {"de": ["Bücherei"]}
    assert c1["scope"]["de"].startswith("Einrichtung")
    assert c1["broader"] == ["http://example.org/c0"]


def test_only_types_filters_to_descriptors():
    concepts = bve.extract_concepts(_graph(), only_types={"http://zbw.eu/namespaces/zbw-extensions/Descriptor"})
    assert [c["id"] for c in concepts] == ["http://example.org/c1"]


def test_concept_document_combines_labels_and_scope():
    c = bve.extract_concepts(_graph(), only_types={"http://zbw.eu/namespaces/zbw-extensions/Descriptor"})[0]
    assert bve.concept_document(c, "de") == "Bibliothek (Bücherei). Einrichtung zur Sammlung von Medien."
    assert bve.concept_document(c, "en") == "Library"


def test_deprecated_concepts_are_skipped():
    ids = {c["id"] for c in bve.extract_concepts(_graph())}
    assert "http://example.org/c9" not in ids
