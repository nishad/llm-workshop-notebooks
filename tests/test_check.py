# tests/test_check.py
from workshop import check


def test_python_floor():
    assert check.check_python((3, 12, 4))[1] is True
    assert check.check_python((3, 11, 9))[1] is False


def test_memory_tiers():
    name, ok, msg = check.check_memory(total_bytes=8 * 1024**3)
    assert ok is True and "8 GB" in msg and "4b" in msg
    name, ok, msg = check.check_memory(total_bytes=16 * 1024**3)
    assert ok is True and "8b" in msg
    assert check.check_memory(total_bytes=4 * 1024**3)[1] is False


def test_disk_needs_20gb():
    assert check.check_disk(free_bytes=25 * 1024**3)[1] is True
    assert check.check_disk(free_bytes=5 * 1024**3)[1] is False


def test_template_check_recognizes_unsloth_header():
    class Fake:
        def show(self, model):
            return type("S", (), {"template": "{# Unsloth template fixes #}\nrest"})()

    assert check.check_template("thalhath/apertus:8b", client=Fake())[1] is True


def test_template_check_accepts_4b_wrapper():
    class Fake:
        def show(self, model):
            return type("S", (), {"template": "<s>\n{{- $hasSystem := false -}} <SPECIAL_63>Deliberation\n# Tool Capabilities\nYou may call tools."})()

    assert check.check_template("thalhath/apertus:4b", client=Fake())[1] is True


def test_print_report_returns_overall(capsys):
    ok = check.print_report([("a", True, "fine"), ("b", False, "bad")])
    out = capsys.readouterr().out
    assert ok is False and "❌ b" in out and "✅ a" in out


def test_run_all_stops_when_server_is_unreachable(monkeypatch):
    from workshop.config import Settings

    monkeypatch.setattr(check, "_server_version", lambda host: None)
    checks = check.run_all(Settings(model="m", embed_model="e", host="http://localhost:1", tier="16gb"))
    assert len(checks) == 4 and checks[-1][1] is False


def test_run_all_continues_past_an_old_version(monkeypatch):
    from workshop.config import Settings

    monkeypatch.setattr(check, "_server_version", lambda host: "0.35.1")
    for name in ("check_model", "check_template", "check_embedding", "smoke_chat", "smoke_tool"):
        monkeypatch.setattr(check, name, lambda *a, _n=name, **k: (_n, True, "stub"))
    checks = check.run_all(Settings(model="m", embed_model="e", host="http://localhost:1", tier="16gb"))
    assert len(checks) == 9
    assert checks[3][1] is False and all(ok for _, ok, _ in checks[4:])


def test_check_ollama_survives_a_non_numeric_version(monkeypatch):
    monkeypatch.setattr(check, "_server_version", lambda host: "dev-build")
    name, ok, msg = check.check_ollama("http://localhost:11434")
    assert ok is False and "dev-build" in msg
