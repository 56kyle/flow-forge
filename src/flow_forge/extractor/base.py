from functools import partial
from typing import Callable, runtime_checkable

import fsspec
from fsspec.core import OpenFile
from typing_extensions import Protocol, Concatenate

from flow_forge.custom_typing import P, DataType, T
from flow_forge.data_endpoint.base import DataEndpointType, DataEndpoint
from flow_forge.data_endpoint.file import FileDataEndpoint, FileDataEndpointType
from flow_forge.process_step import ProcessStep


class Extractor(ProcessStep[Concatenate[DataEndpoint[P, T], P], DataType]):
    """Protocol specification for a Generic Extractor."""

    def __call__(self, source: DataEndpoint[P, T], *args: P.args, **kwargs: P.kwargs) -> DataType:
        """Runs the Extractor."""
        ...


def FileExtractor(path: str) -> Extractor[FileDataEndpoint[P], OpenFile]:
    return partial(fsspec.open, path)


if __name__ == '__main__':
    print(isinstance(FileExtractor, Extractor[File]))


