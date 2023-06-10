from ConfigManager import Config
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.engine.base import Engine
import logging
from ..BaseClass import Base

logger = logging.getLogger()


class MySQLConnector(Base):
    _connection_name = "mysql"
    _local_session: Session = None

    host_config_key = "MYSQL_HOST"
    db_config_key = "MYSQL_DB"
    user_config_key = "MYSQL_USERNAME"
    password_config_key = "MYSQL_PASSWORD"
    connection_type_config_key = "SA_CONN_TYPE"
    pool_size_config_key = "SA_CONN_POLL_SIZE"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def initConnection(self):
        engine = self.activeConnections.get(self._connection_name)

        host = Config.get(self.host_config_key)
        db = Config.get(self.db_config_key)
        user = Config.get(self.user_config_key)
        password = Config.get(self.password_config_key)
        connection_type = Config.get(self.connection_type_config_key)
        engine = create_engine(
            f"{connection_type}+mysqlconnector://{user}:{password}@{host}/{db}",
            pool_size=Config.get(self.pool_size_config_key, 1),
        )
        engine.connect()
        self._registerConnection(self._connection_name, engine)
        if not self.__class__._local_session:
            self.__class__._local_session = sessionmaker(autoflush=True, bind=engine)
        return engine

    def terminateConnection(self) -> None:
        logger.debug("Terminating connection.")
        engine: Engine = self.activeConnections.get(self._connection_name)
        if engine:
            engine.dispose()
            self._registerConnection(self._connection_name, None)
            logger.debug("Engine disposed.")

    @contextmanager
    def session(self) -> Session:
        engine: Engine = self.activeConnections.get(self._connection_name)
        session = self.__class__._local_session()

        if not engine or not self.__class__._local_session:
            self.initConnection()
        try:
            yield session
        finally:
            session.flush()
            session.close()

    def getEngine(self) -> Engine:
        return self.activeConnections.get(self._connection_name)
