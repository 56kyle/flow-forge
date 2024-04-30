"""Module containing the Protocol specification for a sqlalchemy.Session Extractor."""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from typing import Any
from typing import Callable

from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm import Session

from flow_forge.custom_typing import T
from flow_forge.data_endpoint.database import DatabaseDataEndpoint
from flow_forge.extractor.base import Extractor


@dataclass(frozen=True)
class DatabaseExtractor(Extractor[DatabaseDataEndpoint, T]):
    """Generic template for a sqlalchemy DatabaseDataEndpoint Extractor."""

    impl: Callable[[Session, ...], T]

    def __call__(
        self, source: DatabaseDataEndpoint, *args: Any, **kwargs: Any
    ) -> Session:
        """Extract data from the sqlalchemy.Session using the current implementation."""
        with source.get_connection(*args, *kwargs) as session:
            return self.impl(session, **asdict(source))


def __get_database_session(session: Session, *args: Any, **kwargs: Any) -> Session:
    """Returns self."""
    return session


get_database_session: DatabaseExtractor[Session] = DatabaseExtractor[Session](
    impl=__get_database_session
)


def __get_database_table(
    session: Session, *args: Any, schema: str, table_name: str, **kwargs: Any
) -> Table:
    """Returns a sqlalchemy.Table object for the given schema and table name."""
    metadata: MetaData = MetaData(schema=schema)
    metadata.reflect(bind=session.bind, schema=schema, only=[table_name])
    table: Table | None = metadata.tables.get(table_name, None)
    if table is None:
        raise ValueError(f"Table {table_name} does not exist in the provided Database.")
    return table


get_database_table: DatabaseExtractor[Table] = DatabaseExtractor[Table](
    impl=__get_database_table
)


def __get_database_table_column(
    session: Session, *args: Any, schema: str, table_name: str, column_name: str
) -> Column:
    """Returns a Column object from the given database details."""
    table: Table = __get_database_table(session, schema=schema, table_name=table_name)
    column: Column | None = table.columns.get(column_name, None)
    if column is None:
        raise ValueError(
            f"Column {column_name} does not exist in the provided Database."
        )
    return column


get_database_table_column: DatabaseExtractor[Column] = DatabaseExtractor[Column](
    impl=__get_database_table_column
)
