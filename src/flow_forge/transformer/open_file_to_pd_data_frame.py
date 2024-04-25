"""Module containing implementations for OpenFile to pd.DataFrame Transformers."""
import pandas as pd
from fsspec.core import OpenFile

from flow_forge.custom_typing import P
from flow_forge.transformer.open_file import OpenFileTransformer


class OpenFileToPdDataFrameTransformer(OpenFileTransformer[P, pd.DataFrame]):
    """Protocol specification for an OpenFile to pd.DataFrame Transformer."""

    def __call__(self, data: OpenFile, /, *args: P.args, **kwargs: P.kwargs) -> pd.DataFrame:
        """Transforms the provided OpenFile into a pd.DataFrame."""
        ...


class CsvFileToPdDataFrameTransformer(OpenFileToPdDataFrameTransformer[P]):
    """Implementation for a Csv encoded OpenFile to pd.DataFrame Transformer."""
    __call__ = staticmethod(pd.read_csv)


class ExcelFileToPdDataFrameTransformer(OpenFileToPdDataFrameTransformer[P]):
    """Implementation for an Excel encoded OpenFile to pd.DataFrameTransformer."""
    __call__ = staticmethod(pd.read_excel)


class HdfFileToPdDataFrameTransformer(OpenFileToPdDataFrameTransformer[P]):
    """Implementation for a Hdf encoded OpenFile to pd.DataFrame Transformer."""
    __call__ = staticmethod(pd.read_hdf)


class JsonFileToPdDataFrameTransformer(OpenFileToPdDataFrameTransformer[P]):
    """Implementation for a Json encoded OpenFile to pd.DataFrame Transformer."""
    __call__ = staticmethod(pd.read_json)



