"""Module containing implementations for OpenFile to pd.DataFrame Transformers."""
from dataclasses import dataclass
from typing import Callable, Any

import pandas as pd
from fsspec.core import OpenFile

from flow_forge.transformer.open_file import OpenFileTransformer


@dataclass(frozen=True)
class OpenFileToPdDataFrameTransformer(OpenFileTransformer[pd.DataFrame]):
    """Protocol specification for an OpenFile to pd.DataFrame Transformer."""
    decoder: Callable[..., pd.DataFrame]

    def __call__(
        self, data: OpenFile, *args: Any, **kwargs: Any
    ) -> pd.DataFrame:
        """Transforms the provided OpenFile into a pd.DataFrame."""
        return self.decoder(data, *args, **kwargs)


csv_file_to_pd_data_frame: OpenFileToPdDataFrameTransformer = OpenFileToPdDataFrameTransformer(pd.read_csv)
excel_file_to_pd_data_frame: OpenFileToPdDataFrameTransformer = OpenFileToPdDataFrameTransformer(pd.read_excel)
json_file_to_pd_data_frame: OpenFileToPdDataFrameTransformer = OpenFileToPdDataFrameTransformer(pd.read_json)

