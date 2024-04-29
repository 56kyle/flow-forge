"""Module containing the Protocol specification for a sqlalchemy.Session Extractor."""

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy.orm import Session

from flow_forge.custom_typing import P
from flow_forge.data_endpoint.base import DataEndpoint
from flow_forge.data_endpoint.database import ColumnDataEndpoint
from flow_forge.extractor.base import Extractor


class DatabaseSessionExtractor(Extractor[P, Session]):
    """Implementation for a sqlalchemy.Session Extractor."""

    def __call__(
        self, source: DataEndpoint[P, Session], /, *args: P.args, **kwargs: P.kwargs
    ) -> Session:
        """Extracts a sqlalchemy.Session from a DatabaseDataEndpoint."""
        with source.get_connection(*args, **kwargs) as session:
            return session


class DatabaseTableExtractor(Extractor[P, Table]):
    """Implementation for a sqlalchemy.Table Extractor."""

    def __call__(
        self, source: DataEndpoint[P, Session], /, *args: P.args, **kwargs: P.kwargs
    ) -> Table:
        """Extracts a sqlalchemy.Table from a DatabaseDataEndpoint."""
        return source.get_metadata(*args, **kwargs)


class DatabaseColumnExtractor(Extractor[ColumnDataEndpoint[P], Column]):
    """Implementation for a sqlalchemy.Column Extractor."""

    def __call__(
        self,
        source: ColumnDataEndpoint[P, Session],
        /,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> Column:
        """Extracts a sqlalchemy.Column from a DatabaseDataEndpoint."""
        return source.get_metadata(*args, **kwargs)
