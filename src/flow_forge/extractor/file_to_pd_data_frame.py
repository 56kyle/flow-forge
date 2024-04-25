from dataclasses import dataclass, field
from typing import ClassVar

import pandas as pd
from fsspec.implementations.http import HTTPFile

from flow_forge.custom_typing import P
from flow_forge.data_endpoint.file import FileDataEndpoint
from flow_forge.extractor.file import FileExtractor
from flow_forge.transformer.open_file_to_pd_data_frame import OpenFileToPdDataFrameTransformer, \
    CsvFileToPdDataFrameTransformer, ExcelFileToPdDataFrameTransformer, HdfFileToPdDataFrameTransformer, \
    JsonFileToPdDataFrameTransformer


@dataclass(frozen=True)
class FileToPdDataFrameExtractor(FileExtractor[P, pd.DataFrame]):
    """Protocol specification for a FileDataEndpoint to pd.DataFrame extractor."""
    decoder: ClassVar[OpenFileToPdDataFrameTransformer[P]] = field(init=False)

    def __call__(self, source: FileDataEndpoint[P], /, *args: P.args, **kwargs: P.kwargs) -> pd.DataFrame:
        """Extracts a pd.DataFrame from the given FileDataEndpoint."""
        with source(*args, **kwargs) as file:
            return self.decoder(file)


@dataclass(frozen=True)
class CsvFileToPdDataFrameExtractor(FileToPdDataFrameExtractor[P]):
    """Implementation for a Csv encoded FileDataEndpoint to pd.DataFrame Extractor."""
    decoder: ClassVar[CsvFileToPdDataFrameTransformer[P]] = field(
        init=False,
        default=CsvFileToPdDataFrameTransformer()
    )


@dataclass(frozen=True)
class ExcelFileToPdDataFrameExtractor(FileToPdDataFrameExtractor[P]):
    """Implementation for an Excel encoded FileDataEndpoint to pd.DataFrame Extractor."""
    decoder: ClassVar[ExcelFileToPdDataFrameTransformer[P]] = field(
        init=False,
        default=ExcelFileToPdDataFrameTransformer()
    )


@dataclass(frozen=True)
class HdfFileToPdDataFrameExtractor(FileToPdDataFrameExtractor[P]):
    """Implementation for a Hdf encoded FileDataEndpoint to pd.DataFrame Extractor."""
    decoder: ClassVar[HdfFileToPdDataFrameTransformer[P]] = field(
        init=False,
        default=HdfFileToPdDataFrameTransformer()
    )


@dataclass(frozen=True)
class JsonFileToPdDataFrameExtractor(FileToPdDataFrameExtractor[P]):
    """Implementation for a Json encoded FileDataEndpoint to pd.DataFrame Extractor."""
    decoder: ClassVar[JsonFileToPdDataFrameTransformer[P]] = field(
        init=False,
        default=JsonFileToPdDataFrameTransformer()
    )


