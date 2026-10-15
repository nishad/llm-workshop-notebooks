TITLE = "03 · Semantic search over a controlled vocabulary"
CELLS = [
    ("md", """# 03 · Semantic search over a controlled vocabulary ⏱️ 25 minutes

Keyword search finds the words you typed. Semantic search finds the concept you meant, in any language the embedding model
knows. We index the STW Thesaurus for Economics (German and English, CC BY 4.0) and the UNESCO Thesaurus (English, French,
Spanish; CC BY-SA 3.0 IGO) and query them with free text.

Apertus is a chat model and cannot do this; we use an open-weights embedding model (`qwen3-embedding:0.6b`, Apache-2.0) beside it.

**What you'll learn**
1. Turn SKOS labels into index entries and embed them in one batch
2. Search by meaning: a free-text query, a cross-lingual query, a held-out synonym, a scope-note question
3. Decide with a threshold and a human: suggest three, pick one
4. Persist the index with sqlite-vec, measure recall on a gold set, and see why index design matters as much as the model"""),
    ("md", "## 03.01 Configuration"),
    ("code", """import os
os.environ.setdefault("WORKSHOP_TIER", "16gb")
from workshop.config import load_settings
settings = load_settings(); EMBED_MODEL = settings.embed_model
print("Embedding model:", EMBED_MODEL)"""),
    ("md", """## 03.02 From SKOS to index entries

Each preferred and alternative label becomes one entry that remembers its concept, so a one-word query meets one-word entries.
In the October 2026 tests, one long document per concept (label, all alternatives, scope note) put *Fernsehproduktion* below
*Produktionsprozess* although the word is in the document; the label index puts it first. `concept_document` still builds
the one-document form, which the gold set in 03.07 uses because it is the harder case."""),
    ("code", """from scripts.build_vocab_extracts import load_vocab, concept_document
stw = load_vocab("data/vocab/stw.json")
unesco = load_vocab("data/vocab/unesco.json")
print(len(stw), "STW descriptors;", len(unesco), "UNESCO concepts")
c = next((x for x in stw if x["pref"].get("de") == "Bibliothek"), stw[0])
print("preferred:", c["pref"]["de"], "| alternatives:", c["alt"].get("de", []))
print("as one document:", concept_document(c, "de"))"""),
    ("md", """## 03.03 Embed the German STW labels in one batch

About 20,000 short labels. Building the index takes about five minutes on an Apple Silicon Mac with 64 GB and far longer on a
CPU-only laptop. The prebuilt file `runs/stw-de-labels.sqlite` is linked from the download post on the SWIB26 forum topic; put it
in `runs/` and the cell loads it instead of building. On the 8 GB tier, downloading it is the way to follow this notebook live.
The helper applies the embedding model's prefix convention (qwen3-embedding wants an instruction in front of every query and
nothing in front of documents) and returns unit vectors."""),
    ("code", """import time
from pathlib import Path
from workshop.search import build_index, save_index, load_index

entries = []   # (entry id, label): every German preferred and alternative label, remembering its concept
for c in stw:
    for n, label in enumerate([c["pref"].get("de")] + c["alt"].get("de", [])):
        if label:
            entries.append((f'{c["id"]}#{n}', label))
pref = {c["id"]: c["pref"].get("de", "") for c in stw}
Path("runs").mkdir(exist_ok=True)
index_path = "runs/stw-de-labels.sqlite"
if Path(index_path).exists():
    index = load_index(index_path); print("loaded", len(index.ids), "label vectors from", index_path)
    if index.model != EMBED_MODEL:
        print(f"warning: index built with {index.model} but the session uses {EMBED_MODEL}; delete the file to rebuild")
else:
    t = time.time(); index = build_index([e for e, _ in entries], [l for _, l in entries], model=EMBED_MODEL); save_index(index, index_path)
    print(f"embedded {len(entries)} labels in {time.time()-t:.0f} s, dimension {index.vectors.shape[1]}, saved to {index_path}")"""),
    ("md", """## 03.04 Four kinds of query

1. Free text that is not a label: *"Geld, das Eltern für Kinder bekommen"*
2. Cross-lingual: an English query against the German index
3. A synonym that is an alternative label: *Fernsehproduktion* (the descriptor is *Filmproduktion*)
4. A scope-note question

Hits are labels; we keep the best label per concept and show the concept's preferred label next to the label that matched."""),
    ("code", """from workshop.search import search
from workshop.display import show_table

def search_concepts(query, index, pref, k=3):
    \"\"\"Search the labels and keep the best label per concept: (concept id, preferred label, matched label, score).\"\"\"
    best = {}
    for entry_id, label, score in search(query, index, k=k * 10):
        cid = entry_id.rsplit("#", 1)[0]
        if cid not in best or score > best[cid][1]:
            best[cid] = (label, score)
    ranked = sorted(best.items(), key=lambda kv: -kv[1][1])[:k]
    return [(cid, pref[cid], label, score) for cid, (label, score) in ranked]

def show(query, k=3):
    rows = [{"score": f"{s:.3f}", "concept": p, "matched label": l, "id": cid.rsplit("/", 1)[-1]}
            for cid, p, l, s in search_concepts(query, index, pref, k)]
    show_table(rows)

show("Geld, das Eltern für Kinder bekommen")
show("wheat production")
show("Fernsehproduktion")
show("Which concept covers the taxation of inheritances?")"""),
    ("md", """## 03.05 Suggest three, let a person choose

A score is not a decision. Below a threshold we show nothing; above it we show three candidates and record the choice.
This is the pattern for indexing support: the machine proposes, the cataloguer decides."""),
    ("code", """def suggest(text, k=3, threshold=0.55):
    hits = [h for h in search_concepts(text, index, pref, k) if h[3] >= threshold]
    if not hits:
        print(f"No confident suggestion for: {text!r}"); return None
    for n, (cid, p, label, s) in enumerate(hits, 1):
        print(f"[{n}] {s:.3f}  {p}  (matched: {label})")
    choice = input("Pick 1-3, or 0 for none: ") if os.environ.get("WORKSHOP_AUTO_APPROVE") != "1" else "1"
    return hits[int(choice) - 1][0] if choice in ("1", "2", "3") and int(choice) <= len(hits) else None

print("chosen:", suggest("Streik der Lokführer"))"""),
    ("md", """## 03.06 The UNESCO Thesaurus: French and English

Build a second label index from the English preferred and alternative labels and query it in French and German. Cross-lingual retrieval is where embedding models differ most; some of these queries will miss, and 03.07 measures how often.

`runs/unesco-en-labels.sqlite` is the second prebuilt file in the download post; with it in `runs/` the cell loads the index instead of building it."""),
    ("code", """u_entries = [(f'{c["id"]}#{n}', label) for c in unesco
             for n, label in enumerate([c["pref"].get("en")] + c["alt"].get("en", [])) if label]
u_pref = {c["id"]: c["pref"].get("en", "") for c in unesco}
u_path = "runs/unesco-en-labels.sqlite"
if Path(u_path).exists():
    u_index = load_index(u_path)
else:
    u_index = build_index([e for e, _ in u_entries], [l for _, l in u_entries], model=EMBED_MODEL); save_index(u_index, u_path)
for q in ("Grossesse", "bibliothèque numérique", "Rechte der Frau", "changement climatique"):
    print(q, "→", [(p, round(s, 3)) for _, p, _, s in search_concepts(q, u_index, u_pref)])"""),
    ("md", """## 03.07 Measure, don't guess: recall on the gold set (🚀 optional, about six minutes)

Fifty queries with known targets (held-out German synonyms, STW English→German, UNESCO French↔English, scope-note questions),
scored against one document per concept with the synonym removed: the hard case, and the same corpus for every model, so models
can be compared. recall@1 is the share of queries whose correct concept is the top hit. Last year's English-only model scored 0.17
on English→German. This cell embeds 15,198 documents; if you are short on time, skip it and read the committed output."""),
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
    ("md", "## 03.07 continued: the same queries against your label index\n\nThe same held-out queries against the label index from 03.03, with the query's own label removed first, as the gold set does. This isolates the effect of index design with the model held constant. The label index helps the synonym kind most (A: 5/12 to 8/12 at rank 1) and does not help the cross-lingual kind B at rank 1 (8/12 to 6/12, 10/12 within the top five): one-word labels carry less context for a translation than a document does."),
    ("code", """import json, numpy as np
from workshop.embed import embed
gold = json.loads(Path("data/vocab/goldset.json").read_text(encoding="utf-8"))

def label_recall(kind, index=index):
    items = [g for g in gold if g["kind"] == kind]; r1 = r5 = 0
    for g in items:
        q = embed([g["query"]], "query", model=EMBED_MODEL)[0]
        scores = index.vectors @ q
        held_out = [j for j, text in enumerate(index.texts) if text.lower() == g["query"].lower()]
        scores[held_out] = -1
        ranked, seen = [], set()
        for j in np.argsort(-scores):
            cid = index.ids[j].rsplit("#", 1)[0]
            if cid not in seen:
                seen.add(cid); ranked.append(cid)
            if len(ranked) == 5:
                break
        r1 += ranked[0] == g["target"]; r5 += g["target"] in ranked
    return r1, r5, len(items)

for kind in ("A_stw_de_alt_to_concept", "B_stw_en_to_de"):
    r1, r5, n = label_recall(kind)
    print(f"label index  {kind:32} recall@1 {r1}/{n}  recall@5 {r5}/{n}")"""),
    ("md", """## 03.08 sqlite-vec did the storing; it can also do the searching

The index lives in one SQLite file. Any program that can open SQLite can query it; the vector search is a SQL clause."""),
    ("code", """from workshop.search import knn_sqlite
q = embed(["Inflation"], "query", model=EMBED_MODEL)[0]
for i, t, d in knn_sqlite(index_path, q, k=3):
    print(f"distance {d:.3f}  {t[:80]}")"""),
    ("md", """## 03.09 Exercises

🖥️ **GUI:** this notebook has no chat-app equivalent. Read the four tables in 03.04 and decide for each query which hit a
cataloguer would accept.

🔧 **Run and change:** lower the threshold in 03.05 to 0.4 and query something outside economics ("Mondlandung"). What does the
model suggest, and would a cataloguer accept it?

🔧 **Run and change:** query the German index in Italian or Spanish. Which kinds of terms survive translation, which do not?

🚀 **Stretch:** switch the embedding model to `embeddinggemma` (pull it first; it is under Google's Gemma Terms of Use, not an open-source licence). Set `WORKSHOP_EMBED_MODEL=embeddinggemma` in the shell before `uv run jupyter lab`, or add `os.environ["WORKSHOP_EMBED_MODEL"] = "embeddinggemma"` in 03.01 before `load_settings()`. Delete or rename the two index files in `runs/` first (they hold qwen3-embedding vectors), restart the kernel and run from 03.01 to 03.07. In the October 2026 tests it scored recall@1 0.68 against 0.62 for qwen3-embedding and 0.34 for bge-m3. Note the prefixes the helper adds for each model (`workshop.embed.prefix_for`).

🚀 **Stretch:** build an index over a GND subject-heading subset (the DNB publishes GND dumps under CC0 at https://data.dnb.de/opendata/) and query it with
STW labels: a first step towards vocabulary mapping."""),
    ("md", """## ✅ Checkpoint

- SKOS labels became vectors; a query is a dot product away from its nearest labels, and labels point to concepts
- Cross-lingual search works to a measurable degree, and you measured it
- A threshold plus a person turns scores into indexing decisions
- Index design changed recall as much as the model did, and you measured both
- The index is a SQLite file you can hand to a colleague

Next: `04_rag.ipynb`."""),
]
