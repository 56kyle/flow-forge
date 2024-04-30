"""Module containing the specification for a FileDataEndpoint to OpenFile Extractor."""

from fsspec.core import OpenFile

from flow_forge.custom_typing import P
from flow_forge.data_endpoint.file import FileDataEndpoint
from flow_forge.extractor.file import FileExtractor


FileToOpenFileExtractor = FileExtractor[FileDataEndpoint[P], OpenFile]
