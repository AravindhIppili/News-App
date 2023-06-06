# from . import BaseException, ValidationError
# import logging
# import traceback
# import json
# from fastapi import Response

# logger = logging.getLogger()


# def exceptionHandler(exception, return_error_body=False):
#     try:
#         raise exception
#     except ValidationError as e:
#         response = e.getError()
#     # except Exception as e:
#     #     logger.error(traceback.format_exc())
#     #     logger.error(e)
#     #     response = BaseException("Unexpected error occured.").getError()
#     # print("c")
#     print("xbdhd")
#     if isinstance(response, Response):
#         return response

#     if not return_error_body:
#         body = json.dumps(response.get("body"))
#         response = Response(
#             status_code=response.get("statusCode", response.get("status_code")),
#             body=body,
#             content_type=response.get("contentType", "application/json"),
#             headers=response.get("headers"),
#         )
#     print(response)
#     return response
