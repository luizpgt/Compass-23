from exceptions.base_exception import BaseException
from core.exceptions import exceptions


class S3Exception(BaseException):
    def __init__(self, message=exceptions.S3_DEFAULT_ERROR, status_code=500):
        super().__init__(message, status_code)

    @staticmethod
    def handle_s3_exception(error_code):

        s3_exceptions = {
            "NoSuchBucket": S3BucketNotFoundException(),
            "NoSuchKey": S3KeyNotFoundException(),
            "AccessDenied": S3BucketAccessDeniedException()
        }

        return s3_exceptions.get(error_code, S3Exception())


class S3BucketNotFoundException(BaseException):
    def __init__(self, message=exceptions.S3_BUCKET_NOT_FOUND_ERROR,
                 status_code=404):
        super().__init__(message, status_code)


class S3BucketAccessDeniedException(BaseException):
    def __init__(self, message=exceptions.S3_ACCESS_DENIED_ERROR, status_code=403):
        super().__init__(message, status_code)


class S3KeyNotFoundException(BaseException):
    def __init__(self, message=exceptions.S3_KEY_NOT_FOUND_ERROR, status_code=404):
        super().__init__(message, status_code)
