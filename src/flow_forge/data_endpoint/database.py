"""Module containing implementations of sqlalchemy Database related DataEndpoints."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property

from requests import Session
from sqlalchemy import Column
from sqlalchemy import Engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from flow_forge.custom_typing import P
from flow_forge.data_endpoint.base import DataEndpoint


@dataclass(frozen=True)
class DatabaseDataEndpoint(DataEndpoint[P, Session, MetaData]):
    """Implementation of a sqlalchemy Database DataEndpoint."""

    engine: Engine

    @cached_property
    def sessionmaker(self) -> sessionmaker:
        """Returns a sessionmaker instance."""
        return sessionmaker(bind=self.engine)

    @cached_property
    def scoped_session(self) -> scoped_session:
        """Returns a scoped Session instance."""
        return scoped_session(self.sessionmaker)

    def get_connection(self, *args: P.args, **kwargs: P.kwargs) -> Session:
        """Returns a Session for the current sqlalchemy Database."""
        with self.scoped_session(**kwargs) as session:
            return session

    def get_metadata(self, *args: P.args, **kwargs: P.kwargs) -> MetaData:
        """Returns a MetaData instance for the current sqlalchemy Database."""
        metadata: MetaData = MetaData()
        MetaData.reflect(bind=self.engine)
        return metadata


@dataclass(frozen=True)
class TableDataEndpoint(DatabaseDataEndpoint[P, Table]):
    """Implementation of a sqlalchemy.Table DataEndpoint."""

    engine: Engine
    schema: str
    table_name: str

    def get_metadata(self, *args: P.args, **kwargs: P.kwargs) -> Table:
        """Returns a sqlalchemy.Table instance for the current Database."""
        metadata: MetaData = MetaData()
        metadata.reflect(bind=self.engine, schema=self.schema, only=[self.table_name])
        table: Table | None = metadata.tables.get(self.table_name, None)
        if table is None:
            raise ValueError(
                f"Table {self.table_name} does not exist in the provided Database."
            )
        return table


@dataclass(frozen=True)
class ColumnDataEndpoint(DatabaseDataEndpoint[P, Column]):
    """Implementation of a sqlalchemy.Column DataEndpoint."""

    engine: Engine
    schema: str
    table_name: str
    column_name: str

    def get_metadata(self, *args: P.args, **kwargs: P.kwargs) -> Column:
        """Returns a sqlalchemy.Column instance for the current Database."""
        table: Table = self.get_table(*args, **kwargs)
        column: Column | None = table.columns.get(self.column_name, None)
        if column is None:
            raise ValueError(
                f"Column {self.column_name} does not exist in the provided Database."
            )
        return column

    def get_table(self, *args: P.args, **kwargs: P.kwargs) -> Table:
        """Returns the table this Column belongs to."""
        table_data_endpoint: TableDataEndpoint[P] = TableDataEndpoint(
            engine=self.engine, schema=self.schema, table_name=self.table_name
        )
        return table_data_endpoint.get_metadata()
