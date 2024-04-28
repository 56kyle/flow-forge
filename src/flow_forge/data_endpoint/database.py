"""Module containing the implementation of a sqlalchemy Database DataEndpoint."""

from dataclasses import dataclass
from functools import cached_property

from requests import Session
from sqlalchemy import Engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from flow_forge.custom_typing import P
from flow_forge.data_endpoint.base import DataEndpoint


@dataclass(frozen=True)
class DatabaseDataEndpoint(DataEndpoint[P, Session]):
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
