from utils import create_response_data
from middleware.exception_handler import exception_handler_middleware

@exception_handler_middleware
def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = create_response_data(200, body)
    return response
