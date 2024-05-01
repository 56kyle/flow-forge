"""Module containing the base Protocol specification for an Extractor."""
from __future__ import annotations

from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable

import pandas as pd
from typing_extensions import Concatenate

from flow_forge.custom_typing import T, DataType, P, ConnectionType
from flow_forge.data_endpoint.base import DataEndpointType, DataEndpoint
from flow_forge.process_step import ProcessStep









@dataclass(frozen=True)
class Extractor(ProcessStep[DataEndpointType, T]):
    """Generic implementation of an Extractor."""
    impl: Callable[[DataEndpointType], T]

    def __call__(self, source: DataEndpointType, *args: Any, **kwargs: Any) -> T:
        """Runs the Extractor."""
        with source.get_connection(*args, **kwargs) as connection:
            return self.impl(connection)

    def __add__(self, other: Callable[[T], DataType]) -> "Extractor[DataEndpointType, DataType]":
        """Adds a callable onto the Extractor."""
        @wraps(self.impl)
        def wrapper(data: T) -> DataType:
            return other(self.impl(data))

        return Extractor[DataEndpointType, DataType](impl=wrapper)



def extractor(
    method: Callable[Concatenate[ConnectionType, P], T]
) -> Extractor[DataEndpoint[ConnectionType], T]:
    return Extractor[DataEndpoint[ConnectionType], T](impl=method)


@extractor
def pd_data_frame_extractor(data: pd.DataFrame, *args, **kwargs) -> T:
    return data.to_csv(*args, **kwargs)


pd_data_frame_extractor()


