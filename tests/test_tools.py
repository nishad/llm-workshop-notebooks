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


def test_search_gnd_adds_bare_identifier(tmp_path, monkeypatch):
    fixtures = tmp_path / "fixtures"
    (fixtures / "search_gnd").mkdir(parents=True)
    (fixtures / "search_gnd" / "arendt_person.json").write_text(
        json.dumps([{"label": "Arendt, Hannah", "id": "https://d-nb.info/gnd/11850391X"}]), encoding="utf-8"
    )
    tools.set_fixture_dir(str(fixtures))

    def boom(*a, **k):
        raise tools.requests.ConnectionError("offline")

    monkeypatch.setattr(tools.requests, "get", boom)
    out = json.loads(tools.search_gnd("Arendt", "Person"))
    assert out["results"][0]["gnd"] == "11850391X"


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


def test_loop_runs_one_call_per_turn(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")
    ran = []

    def tool_a(name: str) -> str:
        """A. Args: name: a name."""
        ran.append("a"); return json.dumps({"results": [{"id": "gnd/118997718"}], "fixture": False})

    def tool_b(query: str) -> str:
        """B. Args: query: a query."""
        ran.append("b"); return json.dumps({"results": [], "fixture": False})

    chat = ScriptedChat([("", [("tool_a", {"name": "x"}), ("tool_b", {"query": "y"})]), ("Found 118997718.", [])])
    out = tools.run_tool_loop([{"role": "user", "content": "chain"}], [tool_a, tool_b], chat_fn=chat)
    assert ran == ["a"]
    tool_msgs = [m for m in out if m["role"] == "tool"]
    assert len(tool_msgs) == 1 and "only this one ran" in tool_msgs[0]["content"]
    assert len([m for m in out if m["role"] == "assistant"][0]["tool_calls"]) == 1
    assert "UNVERIFIED" not in out[-1]["content"]


def test_loop_flags_identifier_no_tool_returned(monkeypatch):
    monkeypatch.setenv("WORKSHOP_AUTO_APPROVE", "1")

    def fake_tool(name: str) -> str:
        """Fake. Args: name: a name."""
        return json.dumps({"results": [{"id": "https://d-nb.info/gnd/11850391X"}], "fixture": False})

    chat = ScriptedChat([("", [("fake_tool", {"name": "Arendt"})]), ("Her GND is 11850391X and her HLS id is 1595223-8.", [])])
    out = tools.run_tool_loop([{"role": "user", "content": "q"}], [fake_tool], chat_fn=chat)
    assert "UNVERIFIED: 1595223-8" in out[-1]["content"] and "11850391X did not" not in out[-1]["content"]


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
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("SELECT ?s WHERE { SERVICE<https://evil.example/sparql> { ?s ?p ?o } }")
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("PREFIX ev: <https://evil.example/> SELECT ?s WHERE { SERVICE ev:sparql { ?s ?p ?o } }")
    with pytest.raises(tools.ToolError):
        tools.validate_sparql(
            "PREFIX wikibase: <https://evil.example/> SELECT ?s WHERE { SERVICE wikibase:label { ?s ?p ?o } }"
        )
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("SELECT ?s WHERE { S\\u0045RVICE <https://evil.example/sparql> { ?s ?p ?o } }")
    out2 = tools.validate_sparql(
        "PREFIX wikibase: <http://wikiba.se/ontology#> SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q5 . "
        'SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }'
    )
    assert "SERVICE wikibase:label" in out2
    out = tools.validate_sparql(
        'SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q5 . SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }'
    )
    assert "SERVICE wikibase:label" in out

def test_validate_sparql_accepts_update_words_as_names():
    out = tools.validate_sparql("SELECT ?created WHERE { ?s <http://purl.org/dc/terms/created> ?created }")
    assert out.rstrip().endswith("LIMIT 50")
    out = tools.validate_sparql('SELECT ?s WHERE { ?s ?p ?l FILTER(?l = "Move") }')
    assert '"Move"' in out


def test_validate_sparql_rejects_construct_and_nested_service():
    with pytest.raises(tools.ToolError):
        tools.validate_sparql("CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o }")
    with pytest.raises(tools.ToolError):
        tools.validate_sparql(
            'SELECT ?s WHERE { SERVICE wikibase:label { SERVICE <https://evil.example/> { ?s ?p ?o } } }'
        )


def test_validate_sparql_limit_with_offset():
    out = tools.validate_sparql("SELECT ?s WHERE { ?s ?p ?o } LIMIT 10 OFFSET 5")
    assert out.count("LIMIT") == 1 and "LIMIT 10" in out
    with pytest.raises(tools.ToolError, match="LIMIT"):
        tools.validate_sparql("SELECT ?s WHERE { ?s ?p ?o } LIMIT 5000 OFFSET 5")


def test_validate_sparql_rejects_limit_hidden_behind_comment():
    with pytest.raises(tools.ToolError, match="LIMIT"):
        tools.validate_sparql("SELECT ?s WHERE { ?s ?p ?o } LIMIT 5000\n# LIMIT 7")


def test_validate_sparql_ask_passes_through():
    out = tools.validate_sparql("ASK { <http://www.wikidata.org/entity/Q42> ?p ?o }")
    assert out.startswith("ASK") and "LIMIT" not in out
