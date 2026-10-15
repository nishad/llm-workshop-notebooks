import sys

import workshop


def test_python_version_floor():
    assert sys.version_info >= (3, 12)


def test_package_imports():
    assert workshop.__version__.startswith("2026")
