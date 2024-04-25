"""Module containing the base Protocol specification for a Transformer."""
from typing_extensions import Concatenate

from flow_forge.custom_typing import P, InputDataType, OutputDataType
from flow_forge.process_step import ProcessStep


class Transformer(ProcessStep[Concatenate[InputDataType, P], OutputDataType]):
    """Protocol specification for a Generic Transformer."""
    def __call__(self, data: InputDataType, /, *args: P.args, **kwargs: P.kwargs) -> OutputDataType:
        """Runs the Transformer."""
        ...

