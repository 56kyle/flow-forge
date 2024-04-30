"""Module containing the base Protocol specification for a File Extractor."""

from flow_forge.custom_typing import DataType
from flow_forge.custom_typing import P
from flow_forge.data_endpoint.file import FileDataEndpoint
from flow_forge.extractor.base import Extractor


class FileExtractor(Extractor[FileDataEndpoint[P], DataType]):
    """Implementation for a Generic File Extractor."""

    def __call__(
        self, source: FileDataEndpoint[P], /, *args: P.args, **kwargs: P.kwargs
    ) -> DataType:
        """Returns a DataType extracted from a given file."""
        ...