"""Module containing the Protocol specification for a Generic sqlalchemy.Table Transformer."""

from sqlalchemy import Table

from flow_forge.custom_typing import OutputDataType
from flow_forge.custom_typing import P
from flow_forge.transformer.base import Transformer


class DbTableTransformer(Transformer[Table, P, OutputDataType]):
    """Protocol specification for a Generic sqlalchemy.Table Transformer."""

    def __call__(
        self, data: Table, /, *args: P.args, **kwargs: P.kwargs
    ) -> OutputDataType:
        """Transforms the given sqlalchemy.Table into the given OutputDataType."""
        ...
