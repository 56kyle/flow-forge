"""Module containing the specification for a FileDataEndpoint to OpenFile Extractor."""

from fsspec.core import OpenFile

from flow_forge.custom_typing import P
from flow_forge.data_endpoint.file import FileDataEndpoint
from flow_forge.extractor.file import FileExtractor


class FileToOpenFileExtractor(FileExtractor[P, OpenFile]):
    """Protocol specification for a FileDataEndpoint to OpenFile Extractor."""

    def __call__(
        self, source: FileDataEndpoint[P], /, *args: P.args, **kwargs: P.kwargs
    ) -> OpenFile:
        """Extracts an OpenFile from the given FileDataEndpoint."""
        with source.get_connection(*args, **kwargs) as file:
            return file
