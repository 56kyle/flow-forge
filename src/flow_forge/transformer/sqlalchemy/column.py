"""Module containing the Protocol specification for a Generic sqlalchemy.Column Transformer."""

from sqlalchemy import Column

from flow_forge.custom_typing import OutputDataType
from flow_forge.custom_typing import P
from flow_forge.transformer.base import Transformer


class DbColumnTransformer(Transformer[Column, P, OutputDataType]):
    """Protocol specification for a Generic sqlalchemy.Column Transformer."""

    def __call__(
        self, data: Column, /, *args: P.args, **kwargs: P.kwargs
    ) -> OutputDataType:
        """Transforms the given sqlalchemy.Table into the given OutputDataType."""
        ...
