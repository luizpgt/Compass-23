import json
from exceptions.user_exceptions.user_exception import MissingParamException
from core.config import settings

def create_response_data(statusCode, body):
    """
     Create response data to send to API.
     
     @param statusCode - status code of the response
     @param body - JSON - encoded body of the response. It is assumed that the content type is application / json
     
     @return dict with response data in JSON format.
    """
    return {
        'statusCode': statusCode,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        'body': json.dumps(body)
    }

def create_body(imageName, createdImageDateTime, receivedBody, keyType = 'labels', bucket=settings.BUCKET_NAME):
    """
    Creates a response body based on the provided parameters.

    @param imageName (str): The name of the image.
    @param createdImageDateTime (str): The creation date and time of the image in the "dd-mm-YYYY HH:MM:SS" format.
    @param receivedBody (list): A list of objects with information, such as 'labels' or 'faces'.
    @param keyType (str, optional): The type of key to use in the response body ('labels' or 'faces'). Default is 'labels'.
    @param bucket (str): The name of the S3 bucket.

    @return dict: The formatted response body.
    """

    # Build the image URL
    if bucket is None: bucket = settings.BUCKET_NAME
    imageUrl = f"https://{bucket}.s3.amazonaws.com/{imageName}"
    

    # Build the response body
    response = {
        'url_to_image': imageUrl,
        'created_image': createdImageDateTime
    }

    # Add the labels or faces to the response body
    response[keyType] = receivedBody

    return response


def get_data_from_body(body):
    bucket = body.get('bucket')
    if bucket == "": bucket = None
    imageName = body.get('imageName')
    if not imageName: raise MissingParamException(param_name = 'imageName')
    return bucket, imageName
