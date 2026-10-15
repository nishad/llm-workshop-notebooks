"""Evaluate Ollama embedding models on the vocabulary gold set, from the October 2026 research for the SWIB26 workshop. Run: uv run python scripts/eval_embeddings.py GOLD_DIR out.json MODEL ...
Usage: python3 -I eval_embed.py GOLD_DIR OUT_JSON model[:tag][=prefixmode] ...
prefixmode: 'none' (raw text) or 'model' (the model's documented query/document prefixes) or 'both' (default).
Metrics per gold kind and overall: recall@1, recall@5, MRR; wall-clock for corpus embedding.
"""
import json, sys, time, urllib.request
import numpy as np

OLLAMA = "http://localhost:11434/api/embed"
# documented conventions (verified on the model cards; Ollama itself adds nothing)
PREFIXES = {
    "nomic-embed-text":        {"q": "search_query: ",   "d": "search_document: "},
    "nomic-embed-text-v2-moe": {"q": "search_query: ",   "d": "search_document: "},
    "qwen3-embedding":         {"q": "Instruct: Given a search term, retrieve the matching thesaurus concept\nQuery:", "d": ""},
    "embeddinggemma":          {"q": "task: search result | query: ", "d": "title: none | text: "},
    "embeddinggemma-2":        {"q": "task: search result | query: ", "d": "title: none | text: "},
    "snowflake-arctic-embed2": {"q": "query: ", "d": ""},
    "granite-embedding":       {"q": "", "d": ""},
    "bge-m3":                  {"q": "", "d": ""},
    "paraphrase-multilingual": {"q": "", "d": ""},
    "multilingual-e5":         {"q": "query: ", "d": "passage: "},   # for any hf.co/... e5 tag, match on substring
}
def prefixes_for(model):
    base = model.split("/")[-1].split(":")[0].lower()
    for k, v in PREFIXES.items():
        if k in base: return v
    return {"q": "", "d": ""}

import os, hashlib
CACHE = os.environ.get("EMB_CACHE", "emb_cache"); os.makedirs(CACHE, exist_ok=True)
def embed(model, texts, batch=32, timeout=3600, retries=3):
    """Embed via Ollama /api/embed with retries; cache the whole array on disk keyed by model+texts."""
    key = hashlib.sha1((model + "\x1f".join(texts)).encode()).hexdigest()[:20]
    path = f"{CACHE}/{model.replace('/', '_').replace(':', '_')}_{key}.npy"
    if os.path.exists(path): return np.load(path)
    out = []
    for i in range(0, len(texts), batch):
        body = json.dumps({"model": model, "input": texts[i:i+batch], "truncate": True}).encode()
        for attempt in range(retries):
            try:
                req = urllib.request.Request(OLLAMA, data=body, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    out.extend(json.load(r)["embeddings"]); break
            except Exception as e:
                print(f"    retry {attempt+1}/{retries} after error on batch {i}: {e}", file=sys.stderr)
                if attempt == retries - 1: raise
        if (i // batch) % 20 == 0: print(f"    {model}: {min(i+batch, len(texts))}/{len(texts)} texts", file=sys.stderr)
    arr = np.array(out, dtype=np.float32); np.save(path, arr); return arr

def run(model, mode, corpora, gold):
    pre = prefixes_for(model) if mode == "model" else {"q": "", "d": ""}
    res = {"model": model, "prefix_mode": mode, "query_prefix": pre["q"], "doc_prefix": pre["d"], "corpus_seconds": {}, "per_kind": {}, "ranks": {}}
    emb = {}
    for cname, docs in corpora.items():
        uris = list(docs.keys()); texts = [pre["d"] + docs[u] for u in uris]
        t = time.time(); E = embed(model, texts); dt = time.time() - t
        E /= np.linalg.norm(E, axis=1, keepdims=True) + 1e-12
        emb[cname] = (uris, E); res["corpus_seconds"][cname] = round(dt, 1)
        print(f"  {model} [{mode}] embedded {cname}: {len(uris)} docs in {dt:.1f}s ({len(uris)/dt:.0f} docs/s), dim={E.shape[1]}", file=sys.stderr)
    qE = embed(model, [pre["q"] + g["query"] for g in gold]); qE /= np.linalg.norm(qE, axis=1, keepdims=True) + 1e-12
    for g, q in zip(gold, qE):
        uris, E = emb[g["corpus"]]
        scores = E @ q; order = np.argsort(-scores)
        rank = int(np.where(np.array(uris)[order] == g["target"])[0][0]) + 1
        res["ranks"][g["id"]] = {"rank": rank, "top1": corpora[g["corpus"]][uris[order[0]]][:80]}
    kinds = sorted({g["kind"] for g in gold})
    def agg(ids):
        r = np.array([res["ranks"][i]["rank"] for i in ids])
        return {"n": len(r), "recall@1": round(float((r <= 1).mean()), 3), "recall@5": round(float((r <= 5).mean()), 3), "mrr": round(float((1 / r).mean()), 3)}
    for k in kinds: res["per_kind"][k] = agg([g["id"] for g in gold if g["kind"] == k])
    res["overall"] = agg([g["id"] for g in gold])
    return res

def main():
    gold_dir, out_json, *specs = sys.argv[1:]
    corpora = json.load(open(f"{gold_dir}/corpora.json")); gold = json.load(open(f"{gold_dir}/goldset.json"))
    try: results = json.load(open(out_json))
    except Exception: results = []
    for spec in specs:
        model, _, mode = spec.partition("="); mode = mode or "both"
        modes = ["none", "model"] if mode == "both" else [mode]
        for m in modes:
            if m == "model" and not any(prefixes_for(model).values()): continue
            r = run(model, m, corpora, gold)
            results = [x for x in results if not (x["model"] == model and x["prefix_mode"] == m)] + [r]
            json.dump(results, open(out_json, "w"), ensure_ascii=False, indent=1)
            o = r["overall"]; pk = r["per_kind"]
            print(f"{model:<38} {m:<6} R@1={o['recall@1']:.2f} R@5={o['recall@5']:.2f} MRR={o['mrr']:.2f} | " + " ".join(f"{k.split('_')[0]}:R@1={v['recall@1']:.2f}" for k, v in pk.items()) + f" | corpus s={r['corpus_seconds']}")

main()
