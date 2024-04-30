"""Module containing the base Protocol specification for an Extractor."""

from typing import Any

from flow_forge.custom_typing import T
from flow_forge.data_endpoint.base import DataEndpointType
from flow_forge.process_step import ProcessStep


class Extractor(ProcessStep[DataEndpointType, T]):
    """Protocol specification for a Generic Extractor."""

    def __call__(self, source: DataEndpointType, /, *args: Any, **kwargs: Any) -> T:
        """Runs the Extractor."""
        ...
