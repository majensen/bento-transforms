import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def samplesd():
    tdir = Path("tests/").resolve() if Path("tests").exists() else Path().resolve()
    return tdir / "samples"
