from typing import Any
from fastapi import Response


class BaseException(Exception):
    def __init__(
        self,
        error_message: Any = "Internal Server Error.",
        status_code: int = 500,
        error_type: str = "ServerError",
        error_details: Any = None,
        *args,
        **kwargs
    ) -> None:
        self.error_message = error_message
        self.status_code = status_code
        self.error_type = error_type
        self.error_details = error_details
        super().__init__(error_message, *args, **kwargs)

    def get(self) -> dict:
        return {
            "body": {
                "errorType": self.error_type,
                "errorDesc": self.error_message,
                "errorDetails": self.error_details,
            },
            "status_code": self.status_code,
        }


class ConfigNotFoundException(Exception):
    pass


class UnknownError(Exception):
    pass


class ValidationError(BaseException):
    def __init__(
        self,
        error_message: Any = None,
        status_code: int = 400,
        error_type: str = "ValidationError",
        *args,
        **kwargs
    ) -> None:
        super().__init__(error_message, status_code, error_type, *args, **kwargs)
