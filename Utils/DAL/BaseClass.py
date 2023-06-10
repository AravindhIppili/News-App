from abc import ABC, abstractmethod, ABCMeta
from typing import Any
from sqlalchemy.ext.declarative import declarative_base, declared_attr, DeclarativeMeta
from sqlalchemy import DateTime, Column
from sqlalchemy.sql import func


class Base(ABC):
    _activeConnections: dict = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def activeConnections(self) -> dict:
        return self.__class__._activeConnections

    @classmethod
    def _registerConnection(cls, connection_name: str, connection: Any) -> None:
        cls._activeConnections[connection_name] = connection

    @abstractmethod
    def initConnection(self, *args, **kwargs) -> None:
        """
        Method provided by inheriting client to connect to the database.
        """

    @abstractmethod
    def terminateConnection(self, *args, **kwargs) -> None:
        """
        To be called to terminate connection with db if needed.
        """

    @abstractmethod
    def create(self, *args, **kwargs) -> Any:
        """To be used to create resource"""

    @abstractmethod
    def get(self, *args, **kwargs) -> Any:
        """To be used to get one resource"""

    @abstractmethod
    def filter(self, *args, **kwargs) -> Any:
        """To be used to get many resources"""

    @abstractmethod
    def update(self, *args, **kwargs) -> Any:
        """To be used to update resource"""

    @abstractmethod
    def delete(self, *args, **kwargs) -> Any:
        """To be used to delete resource"""


class DeclarativeABCMeta(DeclarativeMeta, ABCMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


DeclarativeBase = declarative_base(metaclass=DeclarativeABCMeta)


class ModelBase(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __init__(self, *args, **kwargs):
        self.model = self.__class__
        super().__init__(*args, **kwargs)

    createdAt = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updatedAt = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
