"""Module containing the base Protocol specification for a DataEndpoint."""

from __future__ import annotations

from typing import Any

from typing_extensions import Protocol
from typing_extensions import TypeVar

from flow_forge.custom_typing import ConnectionType


class DataEndpoint(Protocol[ConnectionType]):
    """Protocol specification for a Generic DataEndpoint."""

    def get_connection(self, *args: Any, **kwargs: Any) -> ConnectionType:
        """Returns a connection to the Generic DataEndpoint."""
        ...


DataEndpointType: TypeVar = TypeVar("DataEndpointType", bound=DataEndpoint)
DataSourceType: TypeVar = TypeVar("DataSourceType", bound=DataEndpoint)
DataSinkType: TypeVar = TypeVar("DataSinkType", bound=DataEndpoint)
