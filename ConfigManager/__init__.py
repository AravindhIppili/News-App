from kink import di
import logging
import os
from typing import Any

from kink.errors.service_error import ServiceError
from Exceptions import ConfigNotFoundException, UnknownError

logger = logging.getLogger()


class Config:
    di = di

    @classmethod
    def get(
        cls,
        configKey: Any,
        default_value: None = None,
        raise_error: bool = True,
        check_env: bool = True,
    ) -> Any:
        if default_value != None:
            raise_error = False
        try:
            return cls.di[configKey]
        except ServiceError:
            message = f"Config for key {configKey} not initialized."
            if check_env:
                config = os.environ.get(configKey)
                if config is not None:
                    return config
            if raise_error:
                logger.warning(message)
                raise ConfigNotFoundException
            logger.debug(message)
            return default_value
        except Exception:
            raise UnknownError("Unexpected error encountered.")

    @classmethod
    def registerDict(cls, config: dict) -> None:
        for key, value in config.items():
            cls.register(key, value)

    @classmethod
    def register(cls, configKey: Any, config: Any) -> None:
        cls.di[configKey] = config

    @classmethod
    def deleteAll(cls) -> None:
        cls.di.clear_cache()
        cls.di._services = {}
