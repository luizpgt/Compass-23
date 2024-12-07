from exceptions.base_exception import BaseException
from utils import create_response_data

def exception_handler_middleware(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as e:
            return create_response_data(e.status_code, {'Error': str(e)})
        except Exception as e:
            return create_response_data(500, {"Error": 'Internal Server Error'})
    return wrapper