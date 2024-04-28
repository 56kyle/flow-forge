"""Module containing the Protocol specification for a Generic sqlalchemy.Session Transformer."""

from sqlalchemy.orm import Session

from flow_forge.custom_typing import OutputDataType
from flow_forge.custom_typing import P
from flow_forge.transformer.base import Transformer


class DbSessionTransformer(Transformer[Session, P, OutputDataType]):
    """Protocol specification for a Generic sqlalchemy.Session Transformer."""

    def __call__(
        self, data: Session, /, *args: P.args, **kwargs: P.kwargs
    ) -> OutputDataType:
        """Transforms the given sqlalchemy.Session into the given OutputDataType."""
        ...
