# Data sources and licences

| File | Source | Licence | Retrieved | Modifications |
|---|---|---|---|---|
| `vocab/stw.json` | STW Thesaurus for Economics, ZBW, https://zbw.eu/stw/ (version as recorded in `vocab/VERSIONS.txt`) | CC BY 4.0 | 2026-10-15 | extracted descriptors with prefLabel, altLabel, scopeNote, broader into JSON |
| `vocab/unesco.json` | UNESCO Thesaurus, https://vocabularies.unesco.org/ | CC BY-SA 3.0 IGO | 2026-10-15 | extracted concepts with labels and scope notes into JSON |
| `vocab/goldset.json`, `vocab/goldset-corpora.json` | built for this workshop from the two vocabularies above | labels keep their source licences; structure CC BY 4.0 | 2026-10-09 | held-out synonyms and cross-lingual pairs |
| `texts/sample-works.txt` | written for the 2024 edition of this workshop | CC BY 4.0 | 2024-11 | none |
| `cards/*.txt`, `cards/cards-gold.json` | written for this workshop | CC BY 4.0 | 2026-10 | none |
| `docs/ifla-lrm.md` | IFLA Library Reference Model, https://repository.ifla.org/handle/20.500.14598/40 | CC BY 4.0 | 2026-10-15 | text extracted from the PDF, section titles kept as plain lines |
| `docs/dcmi-terms.md` | DCMI Metadata Terms, https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ | CC BY 4.0 | 2026-10-15 | HTML converted to text |
| `../fixtures/**.json` | lobid-gnd (hbz, CC0), Wikidata (CC0 for data; CC BY-SA 3.0 for text), LINDAS (Swiss federal open data) | as stated | 2026-10-15 | recorded API responses for offline fallback |

Replace each YYYY-MM-DD with the actual retrieval date when running the download steps. The 2025 dataset "Made with Creative Commons" (CC BY-SA 4.0) is no longer used.
