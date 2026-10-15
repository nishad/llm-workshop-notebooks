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

    assert check.check_template("nishad/apertus:8b", client=Fake())[1] is True


def test_template_check_accepts_4b_wrapper():
    class Fake:
        def show(self, model):
            return type("S", (), {"template": "<s>\n{{- $hasSystem := false -}} <SPECIAL_63>Deliberation\n# Tool Capabilities\nYou may call tools."})()

    assert check.check_template("nishad/apertus:4b", client=Fake())[1] is True


def test_print_report_returns_overall(capsys):
    ok = check.print_report([("a", True, "fine"), ("b", False, "bad")])
    out = capsys.readouterr().out
    assert ok is False and "❌ b" in out and "✅ a" in out
