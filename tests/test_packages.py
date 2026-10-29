import importlib

import pytest

PACKAGES = (
    "app",
    "app.domain",
    "app.services",
    "app.storage",
    "app.adapters",
    "app.api",
)


@pytest.mark.parametrize("name", PACKAGES)
def test_package_imports(name: str) -> None:
    assert importlib.import_module(name).__name__ == name
