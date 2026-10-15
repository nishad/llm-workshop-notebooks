#!/usr/bin/env python3
"""Tool-calling / structured-output reliability harness, from the October 2026 research for the SWIB26 workshop. Run: uv run python scripts/tool_harness.py --base-url http://localhost:11434/v1 --model NAME --out results.jsonl
stdlib only (urllib). Writes one JSON line per request.
Usage: python3 -I harness.py --base-url http://localhost:11434/v1 --model NAME [--model NAME2] --out results.jsonl [--api-key KEY] [--only tools,controls,mt,so,probes]
"""
import argparse, json, re, sys, time, urllib.request, urllib.error

TOOLS = [
 {"type":"function","function":{"name":"lookup_gnd",
   "description":"Search the GND (Gemeinsame Normdatei) authority file via lobid-gnd for an entity by name. Returns matching authority records with their GND identifiers.",
   "parameters":{"type":"object","properties":{
      "name":{"type":"string","description":"Name of the person, organisation, place, subject or work to look up"},
      "type":{"type":"string","enum":["Person","CorporateBody","PlaceOrGeographicName","SubjectHeading","Work"],"description":"Optional GND entity type filter"}},
    "required":["name"]}}},
 {"type":"function","function":{"name":"run_sparql",
   "description":"Run a read-only SPARQL SELECT query against a public endpoint and return the result rows as JSON.",
   "parameters":{"type":"object","properties":{
      "endpoint":{"type":"string","enum":["wikidata","dbpedia"],"description":"Which public SPARQL endpoint to query"},
      "query":{"type":"string","description":"A complete SPARQL SELECT query"}},
    "required":["endpoint","query"]}}},
]

GND_PROMPTS = [
 "Find the GND authority record for Hannah Arendt.",
 "Which GND ID does the Deutsche Nationalbibliothek have? Look it up in the authority file.",
 "Suche in der GND nach der Person Max Frisch.",
 "Cherche dans le fichier d'autorité GND l'entité 'Bibliothèque nationale suisse'.",
 "I need the GND identifier for the city of Basel. Please check the authority file.",
 "Look up 'Semantic Web' as a subject heading in the GND.",
 "Is there a GND record for the author Annemarie Schwarzenbach? Check it.",
 "Retrieve the authority record for the organisation 'ETH Zürich' from the GND.",
 "Finde den GND-Normdatensatz zum Werk 'Der Zauberberg'.",
 "Can you verify the GND entry for Friedrich Dürrenmatt and tell me his GND number?",
]
SPARQL_PROMPTS = [
 "Using Wikidata, how many Nobel Prize in Literature laureates were born in Switzerland? Write and run the SPARQL query.",
 "Query Wikidata for the date of birth of Hermann Hesse (Q25973).",
 "Run a SPARQL query on DBpedia that returns the abstract of the resource dbr:Library.",
 "Frage Wikidata per SPARQL ab: Welche Kantone der Schweiz gibt es? Gib mir die Labels auf Deutsch.",
 "Give me the Wikidata item for the ETH Library: run a SPARQL query that finds items with the label 'ETH-Bibliothek'.",
 "List five national libraries (instances of Q22806) from Wikidata with their country, using SPARQL.",
 "Using SPARQL on Wikidata, find the GND ID (property P227) of Hannah Arendt (Q60025).",
 "Exécute une requête SPARQL sur Wikidata pour trouver la population de Zurich (Q72).",
 "Run this exact query on Wikidata: SELECT ?item WHERE { ?item wdt:P31 wd:Q5 ; wdt:P19 wd:Q70 } LIMIT 3",
 "Which works by Johanna Spyri are in Wikidata? Query it with SPARQL and return their labels.",
]
CONTROL_PROMPTS = [
 "What does the acronym RDF stand for and what is it used for?",
 "Explain in two sentences what a quantized model is.",
 "Translate 'The library opens at nine' into German.",
 "Write a haiku about card catalogues.",
 "What is the difference between an authority file and a thesaurus?",
 "Summarise in one sentence: 'Apertus is a fully open multilingual language model family developed by the Swiss AI Initiative.'",
 "Wie viele Tage hat ein Schaltjahr?",
 "Give me three tips for writing a good prompt.",
 "Convert 15 degrees Celsius to Fahrenheit and show the formula.",
 "Who are you and what can you do?",
]
# multi-turn fixtures: (prompt, tool, synthetic args if the model does not call, tool result JSON, expected substring in final answer)
MT_CASES = [
 ("Find the GND authority record for Hannah Arendt.", "lookup_gnd", {"name":"Hannah Arendt","type":"Person"},
  {"totalItems":1,"member":[{"gndIdentifier":"118503990","preferredName":"Arendt, Hannah","dateOfBirth":["1906-10-14"],"dateOfDeath":["1975-12-04"],"type":["Person"]}]}, "118503990"),
 ("Query Wikidata for the date of birth of Hermann Hesse (Q25973).", "run_sparql", {"endpoint":"wikidata","query":"SELECT ?dob WHERE { wd:Q25973 wdt:P569 ?dob }"},
  {"rows":[{"dob":"1877-07-02T00:00:00Z"}]}, "1877"),
 ("Retrieve the authority record for the organisation 'ETH Zürich' from the GND.", "lookup_gnd", {"name":"ETH Zürich","type":"CorporateBody"},
  {"totalItems":1,"member":[{"gndIdentifier":"TEST-7731-X","preferredName":"Eidgenössische Technische Hochschule Zürich","type":["CorporateBody"]}]}, "TEST-7731-X"),
 ("Frage Wikidata per SPARQL ab: Welche Kantone der Schweiz gibt es? Gib mir die Labels auf Deutsch.", "run_sparql", {"endpoint":"wikidata","query":"SELECT ?kantonLabel WHERE { ?kanton wdt:P31 wd:Q23058 . SERVICE wikibase:label { bd:serviceParam wikibase:language \"de\" } } LIMIT 3"},
  {"rows":[{"kantonLabel":"Zürich"},{"kantonLabel":"Bern"},{"kantonLabel":"Uri"}]}, "Uri"),
 ("Look up 'Zqorbital Vexlund' in the GND authority file.", "lookup_gnd", {"name":"Zqorbital Vexlund"},
  {"totalItems":0,"member":[]}, None),  # expect: states not found; any GND number is a hallucination
]
LEAK_RE = re.compile(r'<\|tools_prefix\|>|<SPECIAL_71>|\{\s*"(lookup_gnd|run_sparql)"\s*:|\[TOOL_REQUEST\]|"name"\s*:\s*"(lookup_gnd|run_sparql)"|<tool_call>')
GND_ID_RE = re.compile(r'\b\d{7,9}[0-9X]?\b|\b\d{1,7}-[0-9X]\b')

def post(base_url, path, body, api_key, timeout=300, stream=False):
    url = base_url.rstrip('/') + path
    data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', 'Bearer ' + (api_key or 'local'))
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if stream:
                lines = [l.decode('utf-8','replace').rstrip('\n') for l in r]
                return r.status, '\n'.join(lines), time.time()-t0
            return r.status, r.read().decode('utf-8','replace'), time.time()-t0
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8','replace'), time.time()-t0
    except Exception as e:
        return -1, repr(e), time.time()-t0

def parse_args_obj(a):
    try:
        d = json.loads(a) if isinstance(a, str) else a
        return d if isinstance(d, dict) else None
    except Exception:
        return None

def analyze(status, raw, expect_tool=None, expected_arg_key=None):
    out = {'status': status}
    if status != 200:
        out['error'] = raw[:600]; out['verdict'] = 'http_error'; return out, None
    try:
        j = json.loads(raw)
    except Exception:
        out['error'] = 'non-json body: ' + raw[:300]; out['verdict'] = 'bad_body'; return out, None
    ch = (j.get('choices') or [{}])[0]
    msg = ch.get('message') or {}
    content = msg.get('content') or ''
    tcs = msg.get('tool_calls') or []
    out['finish_reason'] = ch.get('finish_reason')
    out['n_tool_calls'] = len(tcs)
    out['tool_names'] = [ (tc.get('function') or {}).get('name') for tc in tcs ]
    out['args'] = [ (tc.get('function') or {}).get('arguments') for tc in tcs ]
    out['args_json_ok'] = [ parse_args_obj((tc.get('function') or {}).get('arguments')) is not None for tc in tcs ]
    out['content'] = content[:500]
    out['leak'] = bool(LEAK_RE.search(content))
    out['usage'] = j.get('usage')
    if expect_tool:
        d = parse_args_obj((tcs[0].get('function') or {}).get('arguments')) if tcs else None
        if tcs and out['tool_names'][0] == expect_tool and d is not None and expected_arg_key in d:
            out['verdict'] = 'proper'
        elif tcs:
            out['verdict'] = 'wrong_tool_or_args'
        elif out['leak']:
            out['verdict'] = 'leak_unparsed'
        else:
            out['verdict'] = 'no_call'
    else:
        out['verdict'] = 'hallucinated_call' if tcs else ('leak_unparsed' if out['leak'] else 'clean')
    return out, msg

def rec(fh, **kw):
    fh.write(json.dumps(kw, ensure_ascii=False) + '\n'); fh.flush()
    v = kw.get('result', {}).get('verdict') if isinstance(kw.get('result'), dict) else kw.get('verdict')
    print(f"[{kw.get('model')}] {kw.get('case')}: {v} ({kw.get('latency_s', 0):.1f}s)", flush=True)

def run_model(base_url, model, api_key, fh, only, seed=42, system=None):
    pass
    def chat(messages, **extra):
        if system and not (messages and messages[0].get('role') == 'system'):
            messages = [{"role":"system","content":system}] + messages
        body = {"model": model, "messages": messages, "seed": seed}
        body.update(extra)
        return post(base_url, '/chat/completions', body, api_key, stream=extra.get('stream', False))

    if 'tools' in only:
        for i, p in enumerate(GND_PROMPTS):
            st, raw, dt = chat([{"role":"user","content":p}], tools=TOOLS, max_tokens=300)
            res, _ = analyze(st, raw, 'lookup_gnd', 'name')
            rec(fh, model=model, group='tool_gnd', case=f'gnd_{i+1:02d}', prompt=p, latency_s=dt, result=res)
        for i, p in enumerate(SPARQL_PROMPTS):
            st, raw, dt = chat([{"role":"user","content":p}], tools=TOOLS, max_tokens=400)
            res, _ = analyze(st, raw, 'run_sparql', 'query')
            rec(fh, model=model, group='tool_sparql', case=f'sparql_{i+1:02d}', prompt=p, latency_s=dt, result=res)
    if 'controls' in only:
        for i, p in enumerate(CONTROL_PROMPTS):
            st, raw, dt = chat([{"role":"user","content":p}], tools=TOOLS, max_tokens=160)
            res, _ = analyze(st, raw, None)
            rec(fh, model=model, group='control', case=f'ctrl_{i+1:02d}', prompt=p, latency_s=dt, result=res)
    if 'mt' in only:
        for i, (p, tool, synth_args, tool_result, expected) in enumerate(MT_CASES):
            st, raw, dt = chat([{"role":"user","content":p}], tools=TOOLS, max_tokens=300)
            res1, msg = analyze(st, raw, tool, list(synth_args.keys())[0])
            used_model_call = res1.get('verdict') == 'proper'
            if used_model_call:
                assistant_msg = {"role":"assistant","content": msg.get('content') or "", "tool_calls": msg['tool_calls']}
                call_id = msg['tool_calls'][0].get('id') or 'call_1'
            else:
                call_id = 'call_synth_1'
                assistant_msg = {"role":"assistant","content":"","tool_calls":[{"id":call_id,"type":"function","function":{"name":tool,"arguments":json.dumps(synth_args)}}]}
            messages = [{"role":"user","content":p}, assistant_msg, {"role":"tool","tool_call_id":call_id,"content":json.dumps(tool_result)}]
            st2, raw2, dt2 = chat(messages, tools=TOOLS, max_tokens=250)
            res2, msg2 = analyze(st2, raw2, None)
            content2 = (res2.get('content') or '')
            if expected is None:
                ids = [m for m in GND_ID_RE.findall(content2) if not m.startswith('1975') and not m.startswith('1906')]
                answer_ok = (res2.get('status') == 200 and not res2.get('n_tool_calls') and not ids and bool(re.search(r'(no|not|keine|kein|nicht|aucun|found|gefunden|trouv)', content2, re.I)))
            else:
                answer_ok = (res2.get('status') == 200 and expected in content2)
            rec(fh, model=model, group='multiturn', case=f'mt_{i+1:02d}', prompt=p, latency_s=dt+dt2,
                result={'step1': res1, 'used_model_call': used_model_call, 'step2': res2, 'answer_uses_tool_result': answer_ok,
                        'verdict': ('ok' if answer_ok else ('step2_http_error' if res2.get('status') != 200 else ('called_again' if res2.get('n_tool_calls') else 'answer_mismatch')))})
    if 'so' in only:
        def so_case(case, prompt, schema, max_tokens=200, note=''):
            rf = {"type":"json_schema","json_schema":{"name":"out","schema":schema,"strict":True}}
            st, raw, dt = chat([{"role":"user","content":prompt}], response_format=rf, max_tokens=max_tokens)
            res = {'status': st}
            if st == 200:
                try:
                    j = json.loads(raw); content = (j['choices'][0]['message'].get('content') or '')
                    res['content'] = content[:500]; res['finish_reason'] = j['choices'][0].get('finish_reason')
                    try:
                        obj = json.loads(content); res['json_parses'] = True; res['parsed'] = obj
                    except Exception:
                        res['json_parses'] = False
                except Exception as e:
                    res['error'] = 'bad body ' + raw[:300]
            else:
                res['error'] = raw[:600]
            res['note'] = note
            rec(fh, model=model, group='structured', case=case, prompt=prompt, latency_s=dt, result=res, verdict=str(res.get('status')) + ('/json' if res.get('json_parses') else '/nojson'))
            return res
        biblio = ("Extract the bibliographic record from this text. Record: 'Mann, Thomas: Der Zauberberg. Roman. Berlin: S. Fischer, 1924. 2 Bände.' "
                  "Fields: title, authors (list), year (integer), isbn (string, or null if the record has no ISBN).")
        r1 = so_case('so_01_biblio_null', biblio,
            {"type":"object","properties":{"title":{"type":"string"},"authors":{"type":"array","items":{"type":"string"}},"year":{"type":"integer"},"isbn":{"type":["string","null"]}},"required":["title","authors","year","isbn"],"additionalProperties":False},
            note='expects isbn null, year 1924')
        so_case('so_02_adversarial', "Answer in plain English prose only, never in JSON: why is the sky blue?",
            {"type":"object","properties":{"zzqx_code":{"type":"string","enum":["ALPHA-7"]},"n":{"type":"integer"}},"required":["zzqx_code","n"],"additionalProperties":False},
            max_tokens=60, note='if output conforms despite the prompt, decoding is grammar-constrained')
        so_case('so_03_impossible_minmax', "Give me a number.", {"type":"integer","minimum":10,"maximum":5}, max_tokens=30, note='unsatisfiable schema: look for a compile error vs. junk')
        so_case('so_04_impossible_enum', "Give me a word.", {"type":"string","enum":[]}, max_tokens=30, note='unsatisfiable schema (empty enum)')
        so_case('so_05_enum_language', "Which language is this sentence in: 'Die Bibliothek öffnet um neun Uhr.'", {"type":"object","properties":{"language":{"type":"string","enum":["de","fr","it","en","rm"]}},"required":["language"],"additionalProperties":False}, max_tokens=30, note='expects de')
        # legacy json mode
        st, raw, dt = chat([{"role":"user","content":"Return a JSON object with keys city and country for the capital of Switzerland."}], response_format={"type":"json_object"}, max_tokens=80)
        ok = False
        try: ok = isinstance(json.loads(json.loads(raw)['choices'][0]['message']['content']), dict)
        except Exception: pass
        rec(fh, model=model, group='structured', case='so_06_json_object_mode', latency_s=dt, result={'status': st, 'json_parses': ok, 'body': raw[:300]}, verdict=f'{st}/{"json" if ok else "nojson"}')
    if 'probes' in only:
        # tool_choice handling
        st, raw, dt = chat([{"role":"user","content":GND_PROMPTS[0]}], tools=TOOLS, tool_choice="none", max_tokens=200)
        res, _ = analyze(st, raw, 'lookup_gnd', 'name'); res['note'] = 'tool_choice=none on a tool prompt; a tool call means tool_choice was ignored'
        rec(fh, model=model, group='probe', case='probe_tool_choice_none', latency_s=dt, result=res)
        st, raw, dt = chat([{"role":"user","content":CONTROL_PROMPTS[3]}], tools=TOOLS, tool_choice="required", max_tokens=200)
        res, _ = analyze(st, raw, None); res['note'] = 'tool_choice=required on a no-tool prompt; no call means tool_choice was ignored'
        rec(fh, model=model, group='probe', case='probe_tool_choice_required', latency_s=dt, result=res)
        st, raw, dt = chat([{"role":"user","content":CONTROL_PROMPTS[3]}], tools=TOOLS, tool_choice={"type":"function","function":{"name":"run_sparql"}}, max_tokens=200)
        res, _ = analyze(st, raw, None); res['note'] = 'tool_choice=specific function on a no-tool prompt'
        rec(fh, model=model, group='probe', case='probe_tool_choice_named', latency_s=dt, result=res)
        # logprobs
        st, raw, dt = chat([{"role":"user","content":GND_PROMPTS[0]}], tools=TOOLS, logprobs=True, max_tokens=100)
        rec(fh, model=model, group='probe', case='probe_logprobs_with_tools', latency_s=dt, result={'status': st, 'body': raw[:400]}, verdict=f'HTTP {st}')
        st, raw, dt = chat([{"role":"user","content":CONTROL_PROMPTS[6]}], logprobs=True, max_tokens=40)
        has_lp = False
        try: has_lp = json.loads(raw)['choices'][0].get('logprobs') is not None
        except Exception: pass
        rec(fh, model=model, group='probe', case='probe_logprobs_no_tools', latency_s=dt, result={'status': st, 'logprobs_present': has_lp, 'body': raw[:300]}, verdict=f'HTTP {st} logprobs={has_lp}')
        # streaming tool call
        st, raw, dt = chat([{"role":"user","content":GND_PROMPTS[0]}], tools=TOOLS, stream=True, max_tokens=200)
        n_tc_chunks = 0; fin = None; names = set(); content_acc = ''
        for line in raw.split('\n'):
            if not line.startswith('data:'): continue
            payload = line[5:].strip()
            if payload == '[DONE]': continue
            try:
                c = json.loads(payload); ch = (c.get('choices') or [{}])[0]; d = ch.get('delta') or {}
                if d.get('tool_calls'):
                    n_tc_chunks += 1
                    for tc in d['tool_calls']:
                        if (tc.get('function') or {}).get('name'): names.add(tc['function']['name'])
                if d.get('content'): content_acc += d['content']
                if ch.get('finish_reason'): fin = ch['finish_reason']
            except Exception: pass
        rec(fh, model=model, group='probe', case='probe_stream_tool_call', latency_s=dt, result={'status': st, 'tool_call_chunks': n_tc_chunks, 'names': sorted(names), 'finish_reason': fin, 'content': content_acc[:200]}, verdict=f'HTTP {st} tc_chunks={n_tc_chunks} finish={fin}')
        # parallel calls
        st, raw, dt = chat([{"role":"user","content":"Look up both Hannah Arendt and Max Frisch in the GND authority file."}], tools=TOOLS, max_tokens=300)
        res, _ = analyze(st, raw, 'lookup_gnd', 'name'); res['note'] = 'two entities; count calls'
        rec(fh, model=model, group='probe', case='probe_parallel_calls', latency_s=dt, result=res, verdict=f"{res.get('verdict')} n={res.get('n_tool_calls')}")
        # system prompt + tool (workshop style)
        sysm = "You are a cataloguing assistant for a library. Use the lookup_gnd tool to verify names in the GND before answering. Answer in the user's language."
        st, raw, dt = chat([{"role":"system","content":sysm},{"role":"user","content":"Bitte prüfe den Namen 'Gottfried Keller' in der GND."}], tools=TOOLS, max_tokens=300)
        res, _ = analyze(st, raw, 'lookup_gnd', 'name')
        rec(fh, model=model, group='probe', case='probe_system_prompt_tool', latency_s=dt, result=res)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base-url', default='http://localhost:11434/v1')
    ap.add_argument('--model', action='append', required=True)
    ap.add_argument('--api-key', default=None)
    ap.add_argument('--out', required=True)
    ap.add_argument('--only', default='tools,controls,mt,so,probes')
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--system', default=None)
    a = ap.parse_args()
    only = set(a.only.split(','))
    with open(a.out, 'a', encoding='utf-8') as fh:
        for m in a.model:
            print(f"===== {m} @ {a.base_url} =====", flush=True)
            t0 = time.time()
            try:
                run_model(a.base_url, m, a.api_key, fh, only, a.seed, a.system)
            except Exception as e:
                rec(fh, model=m, group='fatal', case='fatal', result={'error': repr(e)}, verdict='fatal')
            print(f"===== done {m} in {time.time()-t0:.0f}s =====", flush=True)

if __name__ == '__main__':
    main()
