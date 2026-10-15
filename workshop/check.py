"""Readiness checks for the Part 2 notebooks: Python, memory, disk, Ollama, models, one smoke call each."""

from __future__ import annotations

import json
import os
import shutil
import sys

import ollama

from workshop.config import Settings, load_settings
from workshop.llm import _server_version

Check = tuple[str, bool, str]
GB = 1024**3


def check_python(version_info=None) -> Check:
    v = tuple(version_info or sys.version_info[:3])
    ok = v >= (3, 12)
    return ("Python 3.12 or newer", ok, f"found {v[0]}.{v[1]}.{v[2]}")


def _total_memory_bytes() -> int | None:
    try:
        if hasattr(os, "sysconf") and os.sysconf_names.get("SC_PHYS_PAGES"):
            return os.sysconf("SC_PHYS_PAGES") * os.sysconf("SC_PAGE_SIZE")
    except (ValueError, OSError):
        pass
    try:  # Windows
        import ctypes

        class MemoryStatus(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong), ("ullTotalPhys", ctypes.c_ulonglong),
                        ("ullAvailPhys", ctypes.c_ulonglong), ("ullTotalPageFile", ctypes.c_ulonglong),
                        ("ullAvailPageFile", ctypes.c_ulonglong), ("ullTotalVirtual", ctypes.c_ulonglong),
                        ("ullAvailVirtual", ctypes.c_ulonglong), ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]

        status = MemoryStatus()
        status.dwLength = ctypes.sizeof(MemoryStatus)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))
        return int(status.ullTotalPhys)
    except Exception:
        return None


def check_memory(total_bytes: int | None = None) -> Check:
    total = total_bytes if total_bytes is not None else _total_memory_bytes()
    if total is None:
        return ("Memory", True, "could not read memory size; assume the 8 GB tier if unsure")
    gb = round(total / GB)
    if gb < 7:
        return ("Memory", False, f"{gb} GB is below the 8 GB minimum")
    tier = "nishad/apertus:4b (8 GB tier)" if gb < 15 else "nishad/apertus:8b (16 GB tier)"
    return ("Memory", True, f"{gb} GB, use {tier}")


def check_disk(free_bytes: int | None = None, path: str = ".") -> Check:
    free = free_bytes if free_bytes is not None else shutil.disk_usage(path).free
    gb = round(free / GB)
    return ("Free disk 20 GB", gb >= 20, f"{gb} GB free")


def _client(client, host):
    return client or ollama.Client(host=host)


def check_ollama(host: str) -> Check:
    version = _server_version(host)
    if version is None:
        return ("Ollama reachable", False, f"no answer from {host}/api/version. Is the Ollama app running?")
    major, minor = (int(x) for x in version.split(".")[:2])
    ok = (major, minor) >= (0, 40)
    return ("Ollama 0.40 or newer", ok, f"version {version} at {host}")


def check_model(model: str, client=None, host: str | None = None) -> Check:
    try:
        names = [m.model for m in _client(client, host or load_settings().host).list().models]
    except Exception as exc:
        return (f"Model {model}", False, str(exc))
    if model in names or f"{model}:latest" in names:
        return (f"Model {model}", True, "present")
    return (f"Model {model}", False, f"not found; run: ollama pull {model}")


def check_template(model: str, client=None, host: str | None = None) -> Check:
    try:
        template = _client(client, host or load_settings().host).show(model).template or ""
    except Exception as exc:
        return ("Chat template", False, str(exc))
    if ":4b" in model:
        ok = "<SPECIAL_63>" in template and "Tool Capabilities" in template
        return ("Chat template (4B tool wrapper)", ok, "wrapper present" if ok else "wrong template; pull nishad/apertus:4b again")
    ok = template.lstrip().startswith("{# Unsloth template fixes #}")
    return ("Chat template (Unsloth fixes)", ok, "present" if ok else "unexpected template; tool calls will fail")


def check_embedding(embed_model: str, client=None, host: str | None = None) -> Check:
    try:
        vec = _client(client, host or load_settings().host).embed(model=embed_model, input=["Bibliothek"]).embeddings[0]
    except Exception as exc:
        return (f"Embedding model {embed_model}", False, f"{exc}; run: ollama pull {embed_model}")
    return (f"Embedding model {embed_model}", True, f"{len(vec)} dimensions")


def smoke_chat(model: str, client=None, host: str | None = None) -> Check:
    try:
        r = _client(client, host or load_settings().host).chat(
            model=model, messages=[{"role": "user", "content": "Reply with the single word OK."}],
            options={"temperature": 0, "num_predict": 5},
        )
        text = (r.message.content or "").strip()
    except Exception as exc:
        return ("Smoke chat", False, str(exc))
    return ("Smoke chat", bool(text), f"model said: {text[:40]!r}")


def smoke_tool(model: str, client=None, host: str | None = None) -> Check:
    def lookup_authority(name: str) -> str:
        """Look up a person in an authority file.

        Args:
            name: the person's name
        """
        return json.dumps({"id": "test"})

    try:
        r = _client(client, host or load_settings().host).chat(
            model=model, messages=[{"role": "user", "content": "Find the authority record for Hannah Arendt."}],
            tools=[lookup_authority], options={"temperature": 0},
        )
    except Exception as exc:
        return ("Smoke tool call", False, str(exc))
    calls = r.message.tool_calls or []
    if calls:
        return ("Smoke tool call", True, f"proposed {calls[0].function.name}({dict(calls[0].function.arguments)})")
    return ("Smoke tool call", False, "no structured tool call; check the model tag and template")


def run_all(settings: Settings | None = None) -> list[Check]:
    s = settings or load_settings()
    checks = [check_python(), check_memory(), check_disk(), check_ollama(s.host)]
    if not checks[-1][1]:
        return checks
    checks += [check_model(s.model, host=s.host), check_template(s.model, host=s.host),
               check_embedding(s.embed_model, host=s.host), smoke_chat(s.model, host=s.host), smoke_tool(s.model, host=s.host)]
    return checks


def print_report(checks: list[Check]) -> bool:
    all_ok = True
    for name, ok, msg in checks:
        print(f"{'✅' if ok else '❌'} {name}: {msg}")
        all_ok = all_ok and ok
    print("\nAll good." if all_ok else "\nFix the ❌ lines, then run this cell again. Paste the output when asking for help.")
    return all_ok
