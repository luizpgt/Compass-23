import os

class ExceptionMessagesConfig:
    USER_DEFAULT_ERROR = os.environ.get('USER_DEFAULT_ERROR')
    MISSING_PARAM_ERROR = os.environ.get('MISSING_PARAM_ERROR')

    REKOGNITION_DEFAULT_ERROR = os.environ.get('REKOGNITION_DEFAULT_ERROR')
    REKOGNITION_INVALID_S3_ERROR = os.environ.get('REKOGNITION_INVALID_S3_ERROR')
    REKOGNITION_RATE_LIMIT_ERROR = os.environ.get('REKOGNITION_RATE_LIMIT_ERROR')

    S3_DEFAULT_ERROR = os.environ.get('S3_DEFAULT_ERROR')
    S3_BUCKET_NOT_FOUND_ERROR = os.environ.get('S3_BUCKET_NOT_FOUND_ERROR')
    S3_ACCESS_DENIED_ERROR = os.environ.get('S3_ACCESS_DENIED_ERROR')
    S3_KEY_NOT_FOUND_ERROR = os.environ.get('S3_KEY_NOT_FOUND_ERROR')


exceptions = ExceptionMessagesConfig()
