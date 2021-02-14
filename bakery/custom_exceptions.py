from rest_framework import status
from rest_framework.exceptions import APIException


class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Unexpected error occurred! Please try again"

    def __init__(self, detail_text=None):
        if detail_text is None:
            detail_text = self.default_detail
        self.detail = {
            "error": detail_text,
        }


class PermissionDenied(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_text = "You don't have permission to perform this action!"

    def __init__(self, error_text=None):
        if error_text is not None:
            self.default_text = error_text
        self.detail = {
            "error": self.__class__.__name__,
            "data": self.default_text
        }


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail_text):
        self.detail = {
            "error": detail_text,
        }
