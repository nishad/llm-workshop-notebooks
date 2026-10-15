import pytest


@pytest.fixture(autouse=True)
def _isolated_run_log(tmp_path, monkeypatch):
    """Model calls made in tests log into the test's own folder, never into runs/log.jsonl."""
    from workshop import llm

    monkeypatch.setenv("WORKSHOP_LOG", str(tmp_path / "run-log.jsonl"))
    monkeypatch.setattr(llm, "_DIGESTS", {})
