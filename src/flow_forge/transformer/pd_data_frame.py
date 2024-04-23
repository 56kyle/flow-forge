from functools import partial

import pandas as pd
from fsspec.core import OpenFile

from flow_forge.custom_typing import OutputDataType, P
from flow_forge.transformer.base import Transformer


class PdDataFrameTransformer(Transformer[pd.DataFrame, P, OutputDataType]):
    """Protocol specification for a generic pd.DataFrame transformer."""
    def __call__(self, data: pd.DataFrame, *args: P.args, **kwargs: P.kwargs) -> OutputDataType:
        """Transforms the provided pd.DataFrame into the OutputDataType."""
        ...

