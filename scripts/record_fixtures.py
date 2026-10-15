"""Record live API responses for the tool exercises so the notebooks work offline.

Usage: uv run python scripts/record_fixtures.py
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from workshop import tools

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "fixtures"

GND = [("Hannah Arendt", "Person"), ("Johann Wolfgang von Goethe", "Person"), ("Annemarie Schwarzenbach", "Person"),
       ("Albert Einstein", "Person"), ("Bibliothek", "SubjectHeading"), ("Semantic Web", "SubjectHeading"),
       ("Zürich", "PlaceOrGeographicName"), ("Deutsche Nationalbibliothek", "CorporateBody")]
WIKIDATA = [("Hannah Arendt", "en"), ("Johann Wolfgang von Goethe", "de"), ("Annemarie Schwarzenbach", "de"),
            ("Semantic Web", "en"), ("Zürich", "de"), ("Albert Einstein", "en")]
SPARQL = [
    ("wikidata", "SELECT ?item ?itemLabel WHERE { ?item wdt:P227 '118540238' . ?item rdfs:label ?itemLabel FILTER(LANG(?itemLabel)='en') }"),
    ("wikidata", "SELECT ?item ?itemLabel WHERE { ?item wdt:P227 '11850391X' . ?item rdfs:label ?itemLabel FILTER(LANG(?itemLabel)='en') }"),
    ("wikidata", "SELECT ?hls WHERE { ?item wdt:P227 '118997718' . ?item wdt:P902 ?hls }"),
    ("wikidata", "SELECT ?work ?workLabel WHERE { ?work wdt:P50 wd:Q5879 . ?work wdt:P31 wd:Q7725634 . ?work rdfs:label ?workLabel FILTER(LANG(?workLabel)='de') }"),
    ("lindas", "SELECT ?scheme ?title WHERE { ?scheme a <http://www.w3.org/2004/02/skos/core#ConceptScheme> . OPTIONAL { ?scheme <http://purl.org/dc/terms/title> ?title } }"),
]


def _save(tool: str, slug: str, payload) -> None:
    folder = FIXTURES / tool
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{slug}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> None:
    for name, type_ in GND:
        out = json.loads(tools.search_gnd(name, type_))
        assert not out["fixture"], f"live call failed for {name}"
        _save("search_gnd", tools._slug(name, type_), out["results"])
    for label, lang in WIKIDATA:
        out = json.loads(tools.wikidata_lookup(label, lang))
        assert not out["fixture"]
        _save("wikidata_lookup", tools._slug(label, lang), out["results"])
    for endpoint, query in SPARQL:
        safe = tools.validate_sparql(query)
        out = json.loads(tools.sparql(safe, endpoint))
        assert not out["fixture"]
        _save("sparql", tools._slug(endpoint, safe), out["results"])
    (FIXTURES / "README.md").write_text(
        f"Recorded on {date.today()} from lobid-gnd (CC0), Wikidata (CC0) and LINDAS with scripts/record_fixtures.py. "
        "Used automatically by workshop.tools when a live call fails.\n",
        encoding="utf-8",
    )
    print("fixtures recorded")


if __name__ == "__main__":
    main()
