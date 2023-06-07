from typing import Any
from fastapi import Response, HTTPException


class BaseException(HTTPException):
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
        self.body = {
            "errorType": self.error_type,
            "errorDesc": self.error_message,
            "errorDetails": self.error_details,
        }
        super().__init__(
            status_code=self.status_code, detail=self.body, *args, **kwargs
        )

    def getError(self):
        return {
            "body": self.body,
            "status_code": self.status_code,
        }


class ConfigNotFoundException(HTTPException):
    pass


class UnknownError(HTTPException):
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
