"""Module containing the base Protocol specification for a DataEndpoint."""

from __future__ import annotations

from typing_extensions import Protocol
from typing_extensions import TypeVar

from flow_forge.custom_typing import ConnectionType
from flow_forge.custom_typing import MetadataType
from flow_forge.custom_typing import P


class DataEndpoint(Protocol[P, ConnectionType, MetadataType]):
    """Protocol specification for a Generic DataEndpoint."""

    def get_connection(self, *args: P.args, **kwargs: P.kwargs) -> ConnectionType:
        """Returns a connection to the Generic DataEndpoint."""
        ...

    def get_metadata(self, *args: P.args, **kwargs: P.kwargs) -> MetadataType:
        """Returns a metadata representation of the DataEndpoint."""
        ...


DataEndpointType: TypeVar = TypeVar("DataEndpointType", bound=DataEndpoint)
DataSourceType: TypeVar = TypeVar("DataSourceType", bound=DataEndpoint)
DataSinkType: TypeVar = TypeVar("DataSinkType", bound=DataEndpoint)
