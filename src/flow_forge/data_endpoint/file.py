"""Module containing the implementation of a File DataEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from typing import TypeVar

import fsspec
from fsspec import AbstractFileSystem
from fsspec.core import OpenFile

from flow_forge.custom_typing import P
from flow_forge.data_endpoint.base import DataEndpoint


@dataclass(frozen=True)
class FileDataEndpoint(DataEndpoint[P, OpenFile, dict[str, Any]]):
    """Implementation of a File DataEndpoint."""

    path: str

    def get_connection(self, *args: P.args, **kwargs: P.kwargs) -> OpenFile:
        """Returns a connection to the file."""
        return fsspec.open(self.path, *args, **kwargs)

    def get_metadata(self, *args: P.args, **kwargs: P.kwargs) -> dict[str, Any]:
        """Returns metadata about the file."""
        with self.get_connection(*args, **kwargs) as file:
            file_system: AbstractFileSystem = file.fs
            return file_system.stat(self.path)


FileDataEndpointType = TypeVar("FileDataEndpointType", bound=FileDataEndpoint)
