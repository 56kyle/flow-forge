"""Module containing the base Protocol specification for a File Extractor."""
from typing import Any

from flow_forge.custom_typing import DataType
from flow_forge.data_endpoint.file import FileDataEndpoint
from flow_forge.extractor.base import Extractor


class FileExtractor(Extractor[FileDataEndpoint, DataType]):
    """Implementation for a Generic File Extractor."""

    def __call__(
        self, source: FileDataEndpoint, *args: Any, **kwargs: Any
    ) -> DataType:
        """Returns a DataType extracted from a given file."""
        ...
