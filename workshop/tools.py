"""Tools the model may propose and a human approves: GND lookup, Wikidata lookup, read-only SPARQL.

Every tool returns a JSON string. Network failures fall back to recorded fixtures and say so.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

import requests
from rdflib.plugins.sparql.parser import parseQuery
from rdflib.plugins.sparql.parserutils import CompValue

from workshop.config import USER_AGENT, load_settings
from workshop.llm import chat

ALLOWED_ENDPOINTS: dict[str, str] = {
    "wikidata": "https://query.wikidata.org/sparql",
    "qlever": "https://qlever.dev/api/wikidata",
    "lindas": "https://lindas.admin.ch/query",
    "stw": "https://zbw.eu/beta/sparql/stw/query",
    "bnf": "https://data.bnf.fr/sparql",
}
TIMEOUT = 60
WIKIBASE = "http://wikiba.se/ontology#"
FIXTURE_USED = "[fixture]"
_FIXTURE_DIR = Path(__file__).resolve().parent.parent / "fixtures"


class ToolError(Exception):
    """A tool call was rejected or the model misbehaved."""


def set_fixture_dir(path: str) -> None:
    global _FIXTURE_DIR
    _FIXTURE_DIR = Path(path)


def _slug(*parts: str) -> str:
    text = "_".join(parts).lower()
    return re.sub(r"[^a-z0-9]+", "_", text).strip("_")[:80]


def _fixture(tool: str, slug: str):
    path = _FIXTURE_DIR / tool / f"{slug}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return None


def _result(results, fixture: bool, **extra) -> str:
    payload = {"results": results, "fixture": fixture}
    payload.update(extra)
    return json.dumps(payload, ensure_ascii=False)


def _headers() -> dict[str, str]:
    return {"User-Agent": USER_AGENT, "Accept": "application/json"}


_LIMIT = re.compile(r"\bLIMIT\s+(\d+)\s*$", re.IGNORECASE)
_PROLOGUE_DECL = re.compile(r"((?:PREFIX\s+\S+|BASE)\s*<[^>]*>)", re.IGNORECASE)


def _parse(q: str):
    """Parse with rdflib. A `#` inside a prologue IRI on the same line as later keywords trips rdflib's
    parser, so on failure retry with each PREFIX/BASE declaration on its own line (whitespace only)."""
    try:
        return q, parseQuery(q)
    except Exception as first:  # pyparsing raises ParseException; deeply nested patterns raise RecursionError
        unfolded = _PROLOGUE_DECL.sub(r"\1\n", q)
        if unfolded != q:
            try:
                return unfolded, parseQuery(unfolded)
            except Exception:
                pass
        raise ToolError(f"The query does not parse as SPARQL: {str(first).splitlines()[0][:120]}") from None


def _walk(node):
    """Yield every CompValue node in an rdflib parse tree."""
    if isinstance(node, CompValue):
        yield node
        for value in node.values():
            yield from _walk(value)
    elif isinstance(node, (list, tuple)):
        for value in node:
            yield from _walk(value)


def _is_label_service(term, prefixes: dict[str, str]) -> bool:
    """True only for Wikidata's label service, with the wikibase prefix undeclared or bound to its real IRI."""
    if isinstance(term, CompValue) and term.name == "pname":
        return (
            str(term.prefix) == "wikibase"
            and str(term.localname) == "label"
            and prefixes.get("wikibase", WIKIBASE) == WIKIBASE
        )
    return str(term) == WIKIBASE + "label"


def _top_level_limit(body) -> int | None:
    """The LIMIT of the outer query from the parse tree, or None when there is none."""
    clauses = body.get("limitoffset")
    if isinstance(clauses, CompValue) and "limit" in clauses:
        return int(clauses["limit"].toPython())
    return None


def validate_sparql(query: str, *, max_limit: int = 50) -> str:
    """Parse the query and allow only what the workshop endpoints should see.

    SELECT and ASK only; no SERVICE except Wikidata's label service; a LIMIT of at most `max_limit`.
    Parsing instead of pattern-matching means a query the endpoint would read differently from us is rejected.
    """
    q, (prologue, body) = _parse(query.strip())
    if body.name not in ("SelectQuery", "AskQuery"):
        raise ToolError("Only SELECT or ASK queries are allowed.")
    prefixes = {str(d.prefix): str(d.iri) for d in prologue if isinstance(d, CompValue) and d.name == "PrefixDecl"}
    for node in _walk(body):
        if node.name == "ServiceGraphPattern" and not _is_label_service(node.term, prefixes):
            raise ToolError("SERVICE is only allowed for wikibase:label; federated queries to other endpoints are not allowed.")
    if body.name == "AskQuery":
        return q
    limit = _top_level_limit(body)
    if limit is None:
        return f"{q}\nLIMIT {max_limit}"
    if limit <= max_limit:
        return q
    if _LIMIT.search(q):
        capped = _LIMIT.sub(f"LIMIT {max_limit}", q)
        _, (_, capped_body) = _parse(capped)
        capped_limit = _top_level_limit(capped_body)
        if capped_limit is not None and capped_limit <= max_limit:
            return capped
    raise ToolError(f"LIMIT must be at most {max_limit}.")


def _with_gnd(results: list) -> list:
    """Add the bare GND number next to lobid's URL id, so a model can pass it on as a string literal."""
    return [{**item, "gnd": str(item.get("id", "")).rsplit("/", 1)[-1]} if isinstance(item, dict) else item for item in results]


def search_gnd(name: str, type: str = "Person") -> str:
    """Look up a name in the GND authority file via lobid-gnd. Each result carries the bare GND number in `gnd`.

    Args:
        name: the person, organization or subject to search for
        type: GND entity type, one of Person, CorporateBody, SubjectHeading, PlaceOrGeographicName, Work
    """
    slug = _slug(name, type)
    try:
        r = requests.get(
            "https://lobid.org/gnd/search",
            params={"q": name, "filter": f"type:{type}", "format": "json:suggest", "size": 5},
            headers=_headers(),
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        return _result(_with_gnd(r.json()), False)
    except (requests.RequestException, ValueError):
        fx = _fixture("search_gnd", slug)
        if fx is None:
            raise ToolError(f"lobid-gnd unreachable and no fixture for {slug}")
        return _result(_with_gnd(fx), True)


def wikidata_lookup(label: str, lang: str = "en") -> str:
    """Find Wikidata items by label.

    Args:
        label: the label to search for
        lang: two-letter language code of the label, for example en, de or fr
    """
    slug = _slug(label, lang)
    try:
        r = requests.get(
            "https://www.wikidata.org/w/api.php",
            params={"action": "wbsearchentities", "search": label, "language": lang, "format": "json", "limit": 5},
            headers=_headers(),
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        items = [{"id": s["id"], "label": s.get("label"), "description": s.get("description")} for s in r.json().get("search", [])]
        return _result(items, False)
    except (requests.RequestException, ValueError, KeyError):
        fx = _fixture("wikidata_lookup", slug)
        if fx is None:
            raise ToolError(f"Wikidata unreachable and no fixture for {slug}")
        return _result(fx, True)


def sparql(query: str, endpoint: str = "wikidata") -> str:
    """Run a read-only SPARQL SELECT or ASK query against an approved endpoint.

    Args:
        query: the SPARQL query; a LIMIT of at most 50 is enforced
        endpoint: one of wikidata, qlever, lindas, stw, bnf
    """
    if endpoint not in ALLOWED_ENDPOINTS:
        raise ToolError(f"Endpoint not allowed: {endpoint}. Allowed: {', '.join(ALLOWED_ENDPOINTS)}")
    safe = validate_sparql(query)
    slug = _slug(endpoint, safe)
    try:
        r = requests.get(
            ALLOWED_ENDPOINTS[endpoint],
            params={"query": safe, "format": "json"},
            headers={"User-Agent": USER_AGENT, "Accept": "application/sparql-results+json"},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
        if "boolean" in data:
            return _result(data["boolean"], False, query=safe)
        rows = [{k: v.get("value") for k, v in b.items()} for b in data["results"]["bindings"]]
        return _result(rows, False, query=safe)
    except (requests.RequestException, ValueError, KeyError):
        fx = _fixture("sparql", slug)
        if fx is None:
            raise ToolError(f"{endpoint} unreachable and no fixture for this query")
        return _result(fx, True, query=safe)


TOOLS = [search_gnd, wikidata_lookup, sparql]


def approve(name: str, arguments: dict) -> dict | None:
    """Show the proposed call and ask the human. Returns the (possibly edited) arguments, or None to refuse.

    Set WORKSHOP_AUTO_APPROVE=1 to approve everything (used for headless notebook execution).
    """
    if os.environ.get("WORKSHOP_AUTO_APPROVE") == "1":
        return dict(arguments)
    print(f"\nThe model proposes: {name}({json.dumps(arguments, ensure_ascii=False)})")
    reply = input("Run it? [y]es / [n]o / or paste corrected JSON arguments: ").strip()
    if reply.lower() in ("y", "yes"):
        return dict(arguments)
    if reply.startswith("{"):
        try:
            return json.loads(reply)
        except json.JSONDecodeError:
            print("That was not valid JSON; treating it as no.")
            return None
    return None


# GND numbers (118540238, 11850391X, 4006445-3), Wikidata items (Q60025), and any other run of six or more digits
# (HLS article numbers, and long numbers a model invents), so every such number must have come from a tool result.
_IDENTIFIER = re.compile(r"\b\d{6,8}-[0-9X]\b|\b\d{6,}X?\b|\bQ\d{3,}\b")
_LEAKED_CALL = re.compile(r"^\s*[\[{]\s*\"?[a-zA-Z_]+\"?\s*[:(]", re.IGNORECASE)


def _returned_text(result: str) -> str:
    """The part of a tool result that came from the service, without the model's own query echo."""
    try:
        payload = json.loads(result)
    except ValueError:
        return result
    if isinstance(payload, dict):
        payload = {k: v for k, v in payload.items() if k != "query"}
    return json.dumps(payload, ensure_ascii=False)


def _was_returned(identifier: str, outputs: list[str]) -> bool:
    """True when the identifier appears as a whole token in some tool result."""
    pattern = re.compile(rf"(?<![\w-]){re.escape(identifier)}(?![\w-])")
    return any(pattern.search(out) for out in outputs)


def run_tool_loop(
    messages: list[dict],
    tools: list,
    *,
    model: str | None = None,
    max_turns: int = 3,
    approve_fn=approve,
    chat_fn=None,
) -> list[dict]:
    """Model proposes a call, the human approves, Python executes, the result goes back. One call per turn, at most max_turns rounds; identifiers the model states without a tool having returned them are marked. A reply that only names a tool, or says nothing, gets one reminder.

    By default each model call goes through workshop.llm.chat: temperature 0, the tier's num_ctx, one line in runs/log.jsonl."""
    model = model or load_settings().model
    if chat_fn is None:

        def chat_fn(model, messages, tools):
            return chat(messages, model=model, tools=tools)

    by_name = {fn.__name__: fn for fn in tools}
    messages = list(messages)
    tool_outputs: list[str] = []  # every tool result, so identifiers in the final answer can be checked against them
    nudged = False  # one reminder per run when the model announces a call, or says nothing, instead of calling
    for _ in range(max_turns):
        response = chat_fn(model, messages, tools)
        content = response.message.content or ""
        calls = response.message.tool_calls or []
        if not calls:
            if tools and _LEAKED_CALL.match(content) and any(name in content for name in by_name):
                raise ToolError(
                    "The model wrote a tool call as text instead of a structured call. "
                    "Check the model tag: use thalhath/apertus:8b (Unsloth template), not a community tag."
                )
            if tools and not nudged and (not content.strip("` \n\t") or any(name in content for name in by_name)):
                nudged = True
                messages.append({"role": "assistant", "content": content})
                messages.append({"role": "user", "content": "Call the next tool now, or give your final answer."})
                continue
            unverified = sorted({i for i in _IDENTIFIER.findall(content) if not _was_returned(i, tool_outputs)})
            if unverified:
                content += f"\n\n[UNVERIFIED: {', '.join(unverified)} did not come from any tool result.]"
            messages.append({"role": "assistant", "content": content})
            return messages
        dropped = len(calls) - 1
        calls = calls[:1]  # one call per turn: the human sees each result before the next call is proposed
        messages.append({"role": "assistant", "content": content, "tool_calls": [
            {"function": {"name": c.function.name, "arguments": dict(c.function.arguments)}} for c in calls
        ]})
        for call in calls:
            name = call.function.name
            arguments = approve_fn(name, dict(call.function.arguments))
            if arguments is None:
                result = json.dumps({"error": "The user declined this call."})
            elif name not in by_name:
                result = json.dumps({"error": f"Unknown tool {name}"})
            else:
                try:
                    result = by_name[name](**arguments)
                except (ToolError, TypeError, ValueError) as exc:
                    result = json.dumps({"error": str(exc)})
            tool_outputs.append(_returned_text(result))
            if dropped:
                try:
                    payload = json.loads(result)
                    payload["note"] = f"You proposed {dropped + 1} tool calls at once; only this one ran. Read its result, then call the next tool."
                    result = json.dumps(payload, ensure_ascii=False)
                except (ValueError, TypeError):
                    pass
            messages.append({"role": "tool", "tool_name": name, "content": result})
    messages.append({"role": "assistant", "content": "[Stopped after the maximum number of tool rounds.]"})
    return messages
