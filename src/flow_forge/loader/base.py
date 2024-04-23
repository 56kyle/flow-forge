from typing_extensions import Protocol, Concatenate

from flow_forge.custom_typing import P, T, DataType
from flow_forge.data_endpoint.base import DataSinkType
from flow_forge.process_step import ProcessStep


class Loader(ProcessStep[Concatenate[DataType, DataSinkType, P], None]):
    """Protocol specification for a Generic Loader."""
    def __call__(self, data: DataType, sink: DataSinkType, *args: P.args, **kwargs: P.kwargs) -> None:
        """Runs the Loader."""
        ...

