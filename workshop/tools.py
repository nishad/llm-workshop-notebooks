"""Tools the model may propose and a human approves: GND lookup, Wikidata lookup, read-only SPARQL.

Every tool returns a JSON string. Network failures fall back to recorded fixtures and say so.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

import requests

from workshop.config import USER_AGENT, load_settings

ALLOWED_ENDPOINTS: dict[str, str] = {
    "wikidata": "https://query.wikidata.org/sparql",
    "qlever": "https://qlever.dev/api/wikidata",
    "lindas": "https://lindas.admin.ch/query",
    "stw": "https://zbw.eu/beta/sparql/stw/query",
    "bnf": "https://data.bnf.fr/sparql",
}
TIMEOUT = 60
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


_UPDATE_WORDS = re.compile(r"\b(INSERT|DELETE|LOAD|CLEAR|DROP|CREATE|COPY|MOVE|ADD)\b", re.IGNORECASE)
_FORM = re.compile(r"^\s*(?:PREFIX\s+\S+\s*<[^>]*>\s*)*(SELECT|ASK)\b", re.IGNORECASE)
_LIMIT = re.compile(r"\bLIMIT\s+(\d+)\s*$", re.IGNORECASE)
_FEDERATION = re.compile(r"\bSERVICE\s+(?:SILENT\s+)?[<?$]", re.IGNORECASE)


def validate_sparql(query: str, *, max_limit: int = 50) -> str:
    """Allow only SELECT and ASK, forbid update keywords and federated SERVICE blocks, force a small LIMIT.

    Semicolons are legal inside SPARQL (predicate-object lists), so chained updates are caught by the keyword check.
    """
    q = query.strip().rstrip(";").strip()
    form = _FORM.match(q)
    if not form:
        raise ToolError("Only SELECT or ASK queries are allowed.")
    if _UPDATE_WORDS.search(q):
        raise ToolError("Update keywords are not allowed.")
    if _FEDERATION.search(q):
        raise ToolError("Federated SERVICE queries to other endpoints are not allowed.")
    if form.group(1).upper() == "ASK":
        return q
    m = _LIMIT.search(q)
    if m:
        if int(m.group(1)) > max_limit:
            q = _LIMIT.sub(f"LIMIT {max_limit}", q)
    else:
        q = f"{q}\nLIMIT {max_limit}"
    return q


def search_gnd(name: str, type: str = "Person") -> str:
    """Look up a name in the GND authority file via lobid-gnd.

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
        return _result(r.json(), False)
    except (requests.RequestException, ValueError):
        fx = _fixture("search_gnd", slug)
        if fx is None:
            raise ToolError(f"lobid-gnd unreachable and no fixture for {slug}")
        return _result(fx, True)


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


_IDENTIFIER = re.compile(r"\b\d{8,9}[0-9X]?\b|\bQ\d{3,}\b")
_LEAKED_CALL = re.compile(r"^\s*[\[{]\s*\"?[a-zA-Z_]+\"?\s*[:(]", re.IGNORECASE)


def run_tool_loop(
    messages: list[dict],
    tools: list,
    *,
    model: str | None = None,
    max_turns: int = 3,
    approve_fn=approve,
    chat_fn=None,
) -> list[dict]:
    """Model proposes a call, the human approves, Python executes, the result goes back. At most max_turns rounds."""
    import ollama

    settings = load_settings()
    model = model or settings.model
    if chat_fn is None:
        client = ollama.Client(host=settings.host)

        def chat_fn(model, messages, tools):
            return client.chat(model=model, messages=messages, tools=tools, options={"temperature": 0})

    by_name = {fn.__name__: fn for fn in tools}
    messages = list(messages)
    executed_any = False
    for _ in range(max_turns):
        response = chat_fn(model, messages, tools)
        content = response.message.content or ""
        calls = response.message.tool_calls or []
        if not calls:
            if tools and _LEAKED_CALL.match(content) and any(name in content for name in by_name):
                raise ToolError(
                    "The model wrote a tool call as text instead of a structured call. "
                    "Check the model tag: use nishad/apertus:8b (Unsloth template), not a community tag."
                )
            if not executed_any and _IDENTIFIER.search(content):
                content += "\n\n[UNVERIFIED: this answer states an identifier without looking it up.]"
            messages.append({"role": "assistant", "content": content})
            return messages
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
                    executed_any = True
                except (ToolError, TypeError, ValueError) as exc:
                    result = json.dumps({"error": str(exc)})
            messages.append({"role": "tool", "tool_name": name, "content": result})
    messages.append({"role": "assistant", "content": "[Stopped after the maximum number of tool rounds.]"})
    return messages
