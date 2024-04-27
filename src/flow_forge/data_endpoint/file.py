"""Module containing the implementation of a File DataEndpoint."""
from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property, partial, wraps
from typing import TypeVar, TypedDict, Callable, cast, Any

import fsspec
from fsspec import AbstractFileSystem
from fsspec.core import OpenFile
from typing_extensions import Concatenate, TypeAlias, Unpack

from flow_forge.custom_typing import P, T
from flow_forge.data_endpoint.base import DataEndpoint


@dataclass(frozen=True)
class FileDataEndpoint(DataEndpoint[P, OpenFile]):
    """Implementation of a File DataEndpoint."""
    path: str

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> OpenFile:
        """TODO."""
        return fsspec.open(self.path, *args, **kwargs)


FileDataEndpointType = TypeVar("FileDataEndpointType", bound=FileDataEndpoint)

