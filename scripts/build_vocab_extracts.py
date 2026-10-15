"""Turn SKOS vocabularies into compact JSON concept lists for the notebooks.

Usage:
  uv run python scripts/build_vocab_extracts.py stw data/raw/stw.ttl data/vocab/stw.json
  uv run python scripts/build_vocab_extracts.py unesco data/raw/unesco-thesaurus.ttl data/vocab/unesco.json
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

import rdflib
from rdflib.namespace import OWL, RDF, SKOS

ZBW_DESCRIPTOR = "http://zbw.eu/namespaces/zbw-extensions/Descriptor"
PROFILES = {
    "stw": {"only_types": {ZBW_DESCRIPTOR}},
    "unesco": {"only_types": None},
}


def extract_concepts(graph: rdflib.Graph, *, only_types: set[str] | None = None) -> list[dict]:
    wanted = {rdflib.URIRef(t) for t in only_types} if only_types else None
    out = []
    for subject in sorted(set(graph.subjects(RDF.type, SKOS.Concept))):
        if wanted and not any((subject, RDF.type, t) in graph for t in wanted):
            continue
        if (subject, OWL.deprecated, rdflib.Literal(True)) in graph:
            continue  # STW keeps retired descriptors in the data; a search tool must not suggest them
        pref = {str(o.language): str(o) for o in graph.objects(subject, SKOS.prefLabel) if o.language}
        alt: dict[str, list[str]] = {}
        for o in graph.objects(subject, SKOS.altLabel):
            if o.language:
                alt.setdefault(str(o.language), []).append(str(o))
        scope = {str(o.language): str(o) for o in graph.objects(subject, SKOS.scopeNote) if o.language}
        broader = sorted(str(o) for o in graph.objects(subject, SKOS.broader))
        out.append({"id": str(subject), "pref": pref, "alt": {k: sorted(v) for k, v in sorted(alt.items())}, "scope": scope, "broader": broader})
    return out


def concept_document(concept: dict, lang: str) -> str:
    """The text we embed for one concept in one language: prefLabel (altLabels). Scope note."""
    label = concept["pref"].get(lang)
    if not label:
        return ""
    alts = concept["alt"].get(lang, [])
    text = f"{label} ({'; '.join(alts)})" if alts else label
    note = concept["scope"].get(lang)
    return f"{text}. {note}" if note else text


def load_vocab(path: str) -> list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _load_graph(path: Path) -> rdflib.Graph:
    g = rdflib.Graph()
    if path.suffix == ".zip":
        with zipfile.ZipFile(path) as z:
            inner = next(n for n in z.namelist() if n.endswith((".ttl", ".nt", ".rdf")))
            fmt = {"ttl": "turtle", "nt": "nt", "rdf": "xml"}[inner.rsplit(".", 1)[1]]
            g.parse(data=z.read(inner).decode("utf-8"), format=fmt)
        return g
    fmt = {".ttl": "turtle", ".nt": "nt", ".rdf": "xml"}[path.suffix]
    g.parse(str(path), format=fmt)
    return g


def main(argv: list[str]) -> None:
    profile, source, target = argv
    graph = _load_graph(Path(source))
    concepts = extract_concepts(graph, **PROFILES[profile])
    Path(target).parent.mkdir(parents=True, exist_ok=True)
    Path(target).write_text(json.dumps(concepts, ensure_ascii=False, indent=0), encoding="utf-8")
    langs = sorted({l for c in concepts for l in c["pref"]})
    print(f"{profile}: {len(concepts)} concepts, languages {langs}, wrote {target}")


if __name__ == "__main__":
    main(sys.argv[1:])
