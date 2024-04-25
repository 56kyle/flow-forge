"""Module containing the base Protocol specification for an Extractor."""

from typing_extensions import Concatenate

from flow_forge.custom_typing import P, DataType, T
from flow_forge.data_endpoint.base import DataEndpoint
from flow_forge.process_step import ProcessStep


class Extractor(ProcessStep[Concatenate[DataEndpoint[P, T], P], DataType]):
    """Protocol specification for a Generic Extractor."""

    def __call__(self, source: DataEndpoint[P, T], /, *args: P.args, **kwargs: P.kwargs) -> DataType:
        """Runs the Extractor."""
        ...


