from exceptions.base_exception import BaseException
from core.exceptions import exceptions
class RekognitionException(BaseException):
    def __init__(self,message=exceptions.REKOGNITION_DEFAULT_ERROR, status_code=500):
        super().__init__(message, status_code)

    @staticmethod
    def handle_rekognition_exception(error_code):
        """
        Handle Amazon Rekognition exceptions based on the error code.

        @param error_code (str): Error code returned by Amazon Rekognition.

        @return RekognitionException: Custom Rekognition exception based on the error code.
        """
        rekognition_exceptions = {
            "InvalidS3ObjectException": RekognitionInvalidS3ObjectException(),
            "ProvisionedThroughputExceededException": RekognitionRateLimitExceededException()
        }

        return rekognition_exceptions.get(error_code, RekognitionException())

class RekognitionInvalidS3ObjectException(RekognitionException):
    def __init__(self, message=exceptions.REKOGNITION_INVALID_S3_ERROR):
        super().__init__(message,status_code=404)

class RekognitionRateLimitExceededException(RekognitionException):
    def __init__(self, message=exceptions.REKOGNITION_RATE_LIMIT_ERROR):
        super().__init__(message, status_code=429)

