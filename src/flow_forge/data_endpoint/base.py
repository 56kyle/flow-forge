"""TODO."""
from __future__ import annotations

from typing_extensions import Protocol, TypeVar

from flow_forge.custom_typing import P, T


class DataEndpoint(Protocol[P, T]):
    """Protocol specification for a Generic DataEndpoint."""
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        """TODO."""
        ...


DataEndpointType: TypeVar = TypeVar("DataEndpointType", bound=DataEndpoint)
DataSourceType: TypeVar = TypeVar("DataSourceType", bound=DataEndpoint)
DataSinkType: TypeVar = TypeVar("DataSinkType", bound=DataEndpoint)


