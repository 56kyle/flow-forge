"""Module containing various implementations of OpenFile to pd.DataFrame Extractors."""

from dataclasses import dataclass
from typing import Callable, Any

import pandas as pd

from flow_forge.data_endpoint.file import FileDataEndpoint
from flow_forge.extractor.file import FileExtractor
from flow_forge.transformer.open_file_to_pd_data_frame import (
    json_file_to_pd_data_frame, excel_file_to_pd_data_frame, csv_file_to_pd_data_frame,
)


@dataclass(frozen=True)
class FileToPdDataFrameExtractor(FileExtractor[pd.DataFrame]):
    """Protocol specification for a FileDataEndpoint to pd.DataFrame extractor."""
    decoder: Callable[..., pd.DataFrame]

    def __call__(
        self, source: FileDataEndpoint, *args: Any, **kwargs: Any
    ) -> pd.DataFrame:
        """Extracts a pd.DataFrame from the given FileDataEndpoint."""
        with source.get_connection(*args, **kwargs) as file:
            return self.decoder(file)


get_pd_data_frame_from_csv: FileToPdDataFrameExtractor = FileToPdDataFrameExtractor(csv_file_to_pd_data_frame)
get_pd_data_frame_from_excel: FileToPdDataFrameExtractor = FileToPdDataFrameExtractor(excel_file_to_pd_data_frame)
get_pd_data_frame_from_json: FileToPdDataFrameExtractor = FileToPdDataFrameExtractor(json_file_to_pd_data_frame)

