from . import BaseException, ValidationError, UnAuthorized
import logging
import traceback
import json
from fastapi import Response

logger = logging.getLogger()


def exceptionHandler(exception):
    try:
        raise exception
    except ValidationError as e:
        response = e.getError()
    except UnAuthorized as e:
        response = e.getError()
    except Exception as e:
        logger.error(traceback.format_exc())
        logger.error(e)
        response = BaseException("Unexpected error occured.").getError()

    if isinstance(response, Response):
        return response
    body = response.get("body")
    response = Response(
        status_code=response.get("status_code"),
        content=json.dumps(body),
        headers=response.get("headers"),
        media_type="application/json",
    )
    return response
