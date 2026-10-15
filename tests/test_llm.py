import json

from workshop import llm


class FakeClient:
    def __init__(self):
        self.last = None

    def chat(self, **kwargs):
        self.last = kwargs
        return type("R", (), {"message": type("M", (), {"content": "ok", "tool_calls": None})()})()

    def list(self):
        m = type("Mo", (), {"model": "nishad/apertus:8b", "digest": "abc123"})()
        return type("L", (), {"models": [m]})()

    def show(self, model):
        details = type("D", (), {"parameter_size": "8.1B", "quantization_level": "Q4_K_M"})()
        return type(
            "S",
            (),
            {
                "details": details,
                "template": "{# Unsloth template fixes #}\n...",
                "modelinfo": {"apertus.context_length": 65536},
            },
        )()


def test_chat_sets_temperature_zero_and_num_ctx_by_default():
    fake = FakeClient()
    llm.chat([{"role": "user", "content": "hi"}], model="nishad/apertus:4b", client=fake)
    assert fake.last["options"]["num_ctx"] == 4096
    assert fake.last["options"]["temperature"] == 0
    assert "think" not in fake.last


def test_chat_refuses_tools_with_format():
    fake = FakeClient()
    try:
        llm.chat([{"role": "user", "content": "hi"}], format={"type": "object"}, tools=[len], client=fake)
    except ValueError as exc:
        assert "tools" in str(exc) and "format" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_provenance_fields(monkeypatch):
    monkeypatch.setattr(llm, "_server_version", lambda host: "0.40.1")
    p = llm.provenance("nishad/apertus:8b", client=FakeClient())
    assert p["digest"] == "abc123"
    assert p["quantization"] == "Q4_K_M"
    assert p["template_header"].startswith("{# Unsloth")
    assert p["ollama_version"] == "0.40.1"
    assert p["captured_at"]


def test_server_version_returns_none_when_unreachable(monkeypatch):
    def boom(*a, **k):
        raise llm.requests.ConnectionError("offline")

    monkeypatch.setattr(llm.requests, "get", boom)
    assert llm._server_version("http://localhost:1") is None


def test_log_run_appends_jsonl(tmp_path):
    path = tmp_path / "log.jsonl"
    llm.log_run({"a": 1}, path=str(path))
    llm.log_run({"b": 2}, path=str(path))
    lines = path.read_text(encoding="utf-8").splitlines()
    assert [json.loads(l) for l in lines] == [{"a": 1}, {"b": 2}]
