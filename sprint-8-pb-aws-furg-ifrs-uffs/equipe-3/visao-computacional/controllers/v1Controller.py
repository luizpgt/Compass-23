from utils import create_response_data, create_body, get_data_from_body
from services.rekognition_service import detect_labels
from services.s3_service import created_image_datetime
from middleware.exception_handler import exception_handler_middleware
import json


@exception_handler_middleware
def handle_v1_vision(event):
    """
    Handle the request for the v1/vision endpoint. 

    @param event (dict): The request body.
    
    @return dict: The response body.
    """

    # Obtain the image name and bucket name from the request body
    bucket, imageName = get_data_from_body(json.loads(event['body']))

    # Get the datetime when the image was created
    createdImageResponse = created_image_datetime(imageName, bucket)
    # Get labels from image
    detectLabelsResponse = detect_labels(imageName, bucket)
    
    # Prepare response body
    labels = [{'Confidence': label['Confidence'],'Name': label['Name']} for label in detectLabelsResponse['Labels']]

    responseBody = create_body(imageName, createdImageResponse, labels, 'labels', bucket)

    # detectLabelsResponse log for CloudWatch
    print(detectLabelsResponse)

    # Return the answer
    return create_response_data(200, responseBody)
