"""Fixtures used in all tests."""
import uuid

import pytest
from _pytest.fixtures import FixtureRequest

from flow_forge.data_endpoint.file import FileDataEndpoint

pytest_plugins: list[str] = [
    "pytest_static"
]


@pytest.fixture(scope="function")
def file_data_endpoint(
    request: FixtureRequest,
    file_data_endpoint__path: str
) -> FileDataEndpoint:
    return getattr(request, 'param', FileDataEndpoint(
        path=file_data_endpoint__path
    ))


@pytest.fixture(scope="function")
def file_data_endpoint__path(request: FixtureRequest) -> str:
    return getattr(request, 'param', str(uuid.uuid4()))




