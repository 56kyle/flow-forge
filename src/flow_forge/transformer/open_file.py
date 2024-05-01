"""Module containing the Protocol specification for an OpenFile Transformer."""
from typing import Any

from fsspec.core import OpenFile

from flow_forge.custom_typing import OutputDataType
from flow_forge.transformer.base import Transformer


class OpenFileTransformer(Transformer[OpenFile, OutputDataType]):
    """Protocol specification for a Generic fsspec.OpenFile Transformer."""

    def __call__(self, data: OpenFile, *args: Any, **kwargs: Any) -> OutputDataType:
        """Transforms the provided OpenFile data into the OutputDataType."""
        ...



