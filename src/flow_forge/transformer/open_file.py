from fsspec.core import OpenFile

from flow_forge.custom_typing import P, OutputDataType
from flow_forge.transformer.base import Transformer


class OpenFileTransformer(Transformer[OpenFile, P, OutputDataType]):
    """Protocol specification for a Generic fsspec.OpenFile Transformer."""

    def __call__(self, data: OpenFile, *args: P.args, **kwargs: P.kwargs) -> OutputDataType:
        """Transforms the provided OpenFile data into the OutputDataType."""
        ...



