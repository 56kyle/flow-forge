"""Module containing the base Protocol specification for a DataEndpoint."""

from __future__ import annotations

from typing_extensions import Protocol
from typing_extensions import TypeVar

from flow_forge.custom_typing import P
from flow_forge.custom_typing import T


class DataEndpoint(Protocol[P, T]):
    """Protocol specification for a Generic DataEndpoint."""

    def get_connection(self, *args: P.args, **kwargs: P.kwargs) -> T:
        """Returns a connection to the Generic DataEndpoint."""
        ...


DataEndpointType: TypeVar = TypeVar("DataEndpointType", bound=DataEndpoint)
DataSourceType: TypeVar = TypeVar("DataSourceType", bound=DataEndpoint)
DataSinkType: TypeVar = TypeVar("DataSinkType", bound=DataEndpoint)
