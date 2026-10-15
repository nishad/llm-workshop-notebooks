# tests/test_tools.py
import json

import pytest

from workshop import tools


def test_validate_sparql_accepts_select_and_adds_limit():
    q = "PREFIX wdt: <http://www.wikidata.org/prop/direct/> SELECT ?item WHERE { ?item wdt:P227 '118540238' }"
    out = tools.validate_sparql(q)
    assert out.rstrip().endswith("LIMIT 50")


def test_validate_sparql_caps_large_limit():
    out = tools.validate_sparql("SELECT ?s WHERE { ?s ?p ?o } LIMIT 5000")
    assert "LIMIT 50" in out and "5000" not in out


def test_validate_sparql_rejects_updates():
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("DELETE WHERE { ?s ?p ?o }")
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("SELECT ?s WHERE { ?s ?p ?o } ; DROP GRAPH <x>")


def test_sparql_rejects_unknown_endpoint():
    with pytest.raises(tools.ToolError):
        tools.sparql("SELECT ?s WHERE { ?s ?p ?o }", endpoint="https://evil.example/sparql")


def test_fixture_fallback_when_network_fails(tmp_path, monkeypatch):
    fixtures = tmp_path / "fixtures"
    (fixtures / "search_gnd").mkdir(parents=True)
    (fixtures / "search_gnd" / "goethe_person.json").write_text(
        json.dumps([{"label": "Goethe, Johann Wolfgang von", "id": "https://d-nb.info/gnd/118540238"}]),
        encoding="utf-8",
    )
    tools.set_fixture_dir(str(fixtures))

    def boom(*a, **k):
        raise tools.requests.ConnectionError("offline")

    monkeypatch.setattr(tools.requests, "get", boom)
    out = json.loads(tools.search_gnd("Goethe", "Person"))
    assert out["fixture"] is True
    assert out["results"][0]["id"].endswith("118540238")


def test_approve_auto_mode(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")
    assert tools.approve("search_gnd", {"name": "Arendt"}) == {"name": "Arendt"}


def test_approve_edit_arguments(monkeypatch):
    monkeypatch.delenv("WORKSHOP_AUTO_APPROVE", raising=False)
    answers = iter(['{"name": "Hannah Arendt"}'])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    assert tools.approve("search_gnd", {"name": "Hanah Arent"}) == {"name": "Hannah Arendt"}


def test_approve_bad_json_declines(monkeypatch):
    monkeypatch.delenv("WORKSHOP_AUTO_APPROVE", raising=False)
    monkeypatch.setattr("builtins.input", lambda prompt="": "{not json")
    assert tools.approve("search_gnd", {"name": "x"}) is None


def test_approve_decline(monkeypatch):
    monkeypatch.delenv("WORKSHOP_AUTO_APPROVE", raising=False)
    monkeypatch.setattr("builtins.input", lambda prompt="": "n")
    assert tools.approve("search_gnd", {"name": "x"}) is None


class ScriptedChat:
    """Returns prepared responses in order, mimicking ollama.chat."""

    def __init__(self, replies):
        self.replies = iter(replies)

    def __call__(self, model, messages, tools):
        content, calls = next(self.replies)
        tool_calls = [
            type("TC", (), {"function": type("F", (), {"name": n, "arguments": a})()})() for n, a in calls
        ]
        message = type("M", (), {"content": content, "tool_calls": tool_calls or None})()
        return type("R", (), {"message": message})()


def test_loop_executes_approved_call_and_returns_answer(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")

    def fake_tool(name: str) -> str:
        """Fake. Args: name: a name."""
        return json.dumps({"results": [{"id": "gnd/1"}], "fixture": False})

    chat = ScriptedChat([("", [("fake_tool", {"name": "Arendt"})]), ("The GND id is gnd/1 [verified].", [])])
    out = tools.run_tool_loop([{"role": "user", "content": "Find Arendt"}], [fake_tool], chat_fn=chat)
    assert out[-1]["role"] == "assistant"
    assert "gnd/1" in out[-1]["content"]
    assert any(m["role"] == "tool" for m in out)


def test_loop_flags_identifier_without_tool_call(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")
    chat = ScriptedChat([("Her GND number is 118502158.", [])])
    out = tools.run_tool_loop([{"role": "user", "content": "GND of Arendt?"}], [], chat_fn=chat)
    assert "UNVERIFIED" in out[-1]["content"]


def test_loop_detects_tool_call_leaked_as_text(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")
    chat = ScriptedChat([('{"search_gnd": {"name": "Arendt"}}', [])])

    def search_gnd(name: str) -> str:
        """Stand-in tool. Args: name: a name."""
        return "{}"

    with pytest.raises(tools.ToolError, match="model tag"):
        tools.run_tool_loop([{"role": "user", "content": "Find Arendt"}], [search_gnd], chat_fn=chat)


def test_loop_keeps_json_answer_that_is_not_a_tool_call(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")
    chat = ScriptedChat([('{"answer": "Arendt was born in 1906."}', [])])

    def search_gnd(name: str) -> str:
        """Stand-in tool. Args: name: a name."""
        return "{}"

    out = tools.run_tool_loop([{"role": "user", "content": "When was Arendt born?"}], [search_gnd], chat_fn=chat)
    assert out[-1]["role"] == "assistant" and "1906" in out[-1]["content"]


def test_loop_reports_bad_arguments_as_tool_error_message(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")

    def fake_tool(name: str) -> str:
        """Fake. Args: name: a name."""
        return "{}"

    chat = ScriptedChat([("", [("fake_tool", {"nam": "Arendt"})]), ("Sorry, that did not work.", [])])
    out = tools.run_tool_loop([{"role": "user", "content": "Find Arendt"}], [fake_tool], chat_fn=chat)
    tool_msgs = [m for m in out if m["role"] == "tool"]
    assert "error" in json.loads(tool_msgs[0]["content"])
    assert out[-1]["role"] == "assistant"


def test_validate_sparql_rejects_federation_but_allows_label_service():
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("SELECT ?s WHERE { SERVICE <https://evil.example/sparql> { ?s ?p ?o } }")
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("SELECT ?s WHERE { SERVICE ?endpoint { ?s ?p ?o } }")
    out = tools.validate_sparql(
        'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q5 . SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }'
    )
    assert "SERVICE wikibase:label" in out
