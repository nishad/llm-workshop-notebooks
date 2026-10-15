TITLE = "03 · Semantic search over a controlled vocabulary"
CELLS = [
    ("md", """# 03 · Semantic search over a controlled vocabulary ⏱️ 25 minutes

Keyword search finds the words you typed. Semantic search finds the concept you meant, in any language the embedding model
knows. We index the STW Thesaurus for Economics (German and English, CC BY 4.0) and the UNESCO Thesaurus (English, French,
Spanish; CC BY-SA 3.0 IGO) and query them with free text.

Apertus is a chat model and cannot do this; we use an open-weights embedding model (`bge-m3`, MIT licence) beside it.

**What you'll learn**
1. Turn SKOS concepts into short documents and embed them in one batch
2. Search by meaning: a free-text query, a cross-lingual query, a held-out synonym, a scope-note question
3. Decide with a threshold and a human: suggest three, pick one
4. Persist the index with sqlite-vec and measure recall on a gold set"""),
    ("md", "## 03.01 Configuration"),
    ("code", """import os
os.environ.setdefault("WORKSHOP_TIER", "16gb")
from workshop.config import load_settings
settings = load_settings(); EMBED_MODEL = settings.embed_model
print("Embedding model:", EMBED_MODEL)"""),
    ("md", """## 03.02 From SKOS to documents

Each concept becomes one short text: preferred label, alternative labels in parentheses, scope note. That is what we embed."""),
    ("code", """from scripts.build_vocab_extracts import load_vocab, concept_document
stw = load_vocab("data/vocab/stw.json")
unesco = load_vocab("data/vocab/unesco.json")
print(len(stw), "STW descriptors;", len(unesco), "UNESCO concepts")
c = next(x for x in stw if x["pref"].get("de") == "Bibliothek") if any(x["pref"].get("de") == "Bibliothek" for x in stw) else stw[0]
print(concept_document(c, "de")); print(concept_document(c, "en"))"""),
    ("md", """## 03.03 Embed the German STW in one batch

About 6,200 short texts. On a laptop CPU this takes a few minutes the first time; the index is saved afterwards.
The helper applies the prefix convention of the embedding model (none for bge-m3) and returns unit vectors."""),
    ("code", """import time
from pathlib import Path
from workshop.search import build_index, save_index, load_index

ids = [c["id"] for c in stw if c["pref"].get("de")]
docs = [concept_document(c, "de") for c in stw if c["pref"].get("de")]
Path("runs").mkdir(exist_ok=True)
index_path = "runs/stw-de.sqlite"
if Path(index_path).exists():
    index = load_index(index_path); print("loaded", len(index.ids), "vectors from", index_path)
else:
    t = time.time(); index = build_index(ids, docs, model=EMBED_MODEL); save_index(index, index_path)
    print(f"embedded {len(ids)} concepts in {time.time()-t:.0f} s, dimension {index.vectors.shape[1]}, saved to {index_path}")"""),
    ("md", """## 03.04 Four kinds of query

1. Free text that is not a label: *"Geld, das Eltern für Kinder bekommen"*
2. Cross-lingual: an English query against the German index
3. A synonym that is **not** in the document: *"Fernsehproduktion"* (the descriptor is "Filmproduktion")
4. A scope-note question"""),
    ("code", """from workshop.search import search
from workshop.display import show_table

def show(query, k=3):
    hits = search(query, index, k=k)
    show_table([{"score": f"{s:.3f}", "concept": t, "id": i.rsplit('/', 1)[-1]} for i, t, s in hits])

show("Geld, das Eltern für Kinder bekommen")
show("wheat production")
show("Fernsehproduktion")
show("Which concept covers the taxation of inheritances?")"""),
    ("md", """## 03.05 Suggest three, let a person choose

A score is not a decision. Below a threshold we show nothing; above it we show three candidates and record the choice.
This is the pattern for indexing support: the machine proposes, the cataloguer decides."""),
    ("code", """def suggest(text, k=3, threshold=0.55):
    hits = [h for h in search(text, index, k=k) if h[2] >= threshold]
    if not hits:
        print(f"No confident suggestion for: {text!r}"); return None
    for n, (i, t, s) in enumerate(hits, 1):
        print(f"[{n}] {s:.3f}  {t[:90]}")
    choice = input("Pick 1-3, or 0 for none: ") if os.environ.get("WORKSHOP_AUTO_APPROVE") != "1" else "1"
    return hits[int(choice) - 1][0] if choice in ("1", "2", "3") else None

print("chosen:", suggest("Streik der Lokführer"))"""),
    ("md", """## 03.06 The UNESCO Thesaurus: French and English

Build a second, smaller index (English documents) and query it in French. Cross-lingual retrieval is where embedding
models differ most; the gold set in 03.07 measures it."""),
    ("code", """u_ids = [c["id"] for c in unesco if c["pref"].get("en")]
u_docs = [concept_document(c, "en") for c in unesco if c["pref"].get("en")]
u_path = "runs/unesco-en.sqlite"
u_index = load_index(u_path) if Path(u_path).exists() else build_index(u_ids, u_docs, model=EMBED_MODEL)
save_index(u_index, u_path)
for q in ("Grossesse", "bibliothèque numérique", "Rechte der Frau"):
    hits = search(q, u_index, k=3)
    print(q, "→", [(t[:40], round(s, 3)) for _, t, s in hits])"""),
    ("md", """## 03.07 Measure, don't guess: recall on the gold set

Fifty queries with known targets (held-out German synonyms, STW English→German, UNESCO French↔English, scope-note questions).
recall@1 is the share of queries whose correct concept is the top hit. Last year's English-only model scored 0.17 on
English→German; see how a multilingual model does."""),
    ("code", """import json, numpy as np
from workshop.embed import embed
from workshop.search import top_k
gold = json.loads(Path("data/vocab/goldset.json").read_text(encoding="utf-8"))
corpora = json.loads(Path("data/vocab/goldset-corpora.json").read_text(encoding="utf-8"))
results = {}
for name, docs in corpora.items():
    uris = list(docs); vecs = embed([docs[u] for u in uris], "document", model=EMBED_MODEL)
    results[name] = (uris, vecs)
hits1 = hits5 = 0
by_kind = {}
for g in gold:
    uris, vecs = results[g["corpus"]]
    q = embed([g["query"]], "query", model=EMBED_MODEL)[0]
    ranked = [uris[i] for i, _ in top_k(q, vecs, 5)]
    r1 = ranked[0] == g["target"]; r5 = g["target"] in ranked
    hits1 += r1; hits5 += r5
    by_kind.setdefault(g["kind"], [0, 0, 0]); by_kind[g["kind"]][0] += r1; by_kind[g["kind"]][1] += r5; by_kind[g["kind"]][2] += 1
print(f"{EMBED_MODEL}: recall@1 {hits1/len(gold):.2f}, recall@5 {hits5/len(gold):.2f}")
for kind, (a, b, n) in by_kind.items():
    print(f"  {kind:32} recall@1 {a}/{n}  recall@5 {b}/{n}")"""),
    ("md", """## 03.08 sqlite-vec did the storing; it can also do the searching

The index lives in one SQLite file. Any program that can open SQLite can query it; the vector search is a SQL clause."""),
    ("code", """from workshop.search import knn_sqlite
q = embed(["Inflation"], "query", model=EMBED_MODEL)[0]
for i, t, d in knn_sqlite(index_path, q, k=3):
    print(f"distance {d:.3f}  {t[:80]}")"""),
    ("md", """## 03.09 Exercises

🔧 **Run and change:** lower the threshold in 03.05 to 0.4 and query something outside economics ("Mondlandung"). What does the
model suggest, and would a cataloguer accept it?

🔧 **Run and change:** query the German index in Italian or Spanish. Which kinds of terms survive translation, which do not?

🚀 **Stretch:** set `WORKSHOP_EMBED_MODEL=qwen3-embedding:0.6b` (pull it first), restart the kernel, re-run 03.07 and compare the
per-kind recall. Note the query prefix the helper adds for this model (`workshop.embed.prefix_for`).

🚀 **Stretch:** build an index over a GND subject-heading subset (the DNB publishes GND dumps under CC0 at https://data.dnb.de/opendata/) and query it with
STW labels: a first step towards vocabulary mapping."""),
    ("md", """## ✅ Checkpoint

- SKOS concepts became documents and vectors; a query is a dot product away from its nearest concepts
- Cross-lingual search works to a measurable degree, and you measured it
- A threshold plus a person turns scores into indexing decisions
- The index is a SQLite file you can hand to a colleague

Next: `04_rag.ipynb`."""),
]
