import json

from workshop import llm


class FakeClient:
    def __init__(self):
        self.last = None

    def chat(self, **kwargs):
        self.last = kwargs
        return type("R", (), {"message": type("M", (), {"content": "ok", "tool_calls": None})()})()

    def list(self):
        m = type("Mo", (), {"model": "thalhath/apertus:8b", "digest": "abc123"})()
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
    llm.chat([{"role": "user", "content": "hi"}], model="thalhath/apertus:4b", client=fake)
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
    p = llm.provenance("thalhath/apertus:8b", client=FakeClient())
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


LOG_KEYS = {"captured_at", "model", "digest", "options", "prompt", "answer", "tool_calls", "format"}


def test_chat_logs_one_line_per_call(tmp_path, monkeypatch):
    path = tmp_path / "log.jsonl"
    monkeypatch.setenv("WORKSHOP_LOG", str(path))
    llm.chat([{"role": "user", "content": "x" * 100 + "y" * 300}], model="thalhath/apertus:8b", format={"type": "object"}, client=FakeClient())
    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    record = json.loads(lines[0])
    assert set(record) == LOG_KEYS
    assert record["digest"] == "abc123" and record["answer"] == "ok" and record["tool_calls"] == 0
    assert record["prompt"] == "y" * 300 and record["format"] == "schema" and record["options"]["num_ctx"] == 8192


def test_chat_logs_streams_without_answer(tmp_path, monkeypatch):
    path = tmp_path / "log.jsonl"
    monkeypatch.setenv("WORKSHOP_LOG", str(path))
    llm.chat([{"role": "user", "content": "hi"}], model="thalhath/apertus:8b", stream=True, client=FakeClient())
    record = json.loads(path.read_text(encoding="utf-8"))
    assert record["answer"] is None and record["stream"] is True and record["format"] is None


def test_chat_with_log_false_writes_nothing(tmp_path, monkeypatch):
    path = tmp_path / "log.jsonl"
    monkeypatch.setenv("WORKSHOP_LOG", str(path))
    llm.chat([{"role": "user", "content": "hi"}], model="thalhath/apertus:8b", client=FakeClient(), log=False)
    assert not path.exists()


def test_chat_survives_an_unwritable_log(tmp_path, monkeypatch):
    blocker = tmp_path / "a-file"
    blocker.write_text("not a folder", encoding="utf-8")
    monkeypatch.setenv("WORKSHOP_LOG", str(blocker / "log.jsonl"))
    response = llm.chat([{"role": "user", "content": "hi"}], model="thalhath/apertus:8b", client=FakeClient())
    assert response.message.content == "ok"
