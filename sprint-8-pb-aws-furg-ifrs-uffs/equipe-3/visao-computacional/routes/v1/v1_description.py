from utils import create_response_data
from middleware.exception_handler import exception_handler_middleware

@exception_handler_middleware
def v1_description(event, context):
    body = {
        "message": "VISION api version 1."
    }
    return create_response_data(200, body)