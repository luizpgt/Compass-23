from exceptions.base_exception import BaseException
from core.exceptions import exceptions


class UserException(BaseException):
    def __init__(self, message=exceptions.USER_DEFAULT_ERROR, status_code=500):
        super().__init__(message, status_code)


class MissingParamException(UserException):
    def __init__(self, param_name, message=exceptions.MISSING_PARAM_ERROR, status_code=400):
        super().__init__(f"{message}: {param_name}", status_code)
