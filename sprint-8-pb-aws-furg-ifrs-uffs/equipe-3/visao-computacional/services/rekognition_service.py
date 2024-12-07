import boto3
from botocore.exceptions import ClientError
from exceptions.aws_exceptions.rekognition_exception import RekognitionException
from core.config import settings
rekognition_client = boto3.client('rekognition')

def detect_labels(imageName, bucketName=settings.BUCKET_NAME):
    """
     Detect labels (objects) in an image using Amazon Rekognition.
     
     @param imageName (str) - Name of the image to detect labels
     @param bucketName (str, optional) - S3 bucket to use for detection

     @return dict: A dictionary containing the detected labels and their confidence scores.
    """
    if bucketName is None:
     bucketName = settings.BUCKET_NAME
    try:
        response = rekognition_client.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": bucketName,
                    "Name": imageName
                }
            },
            MaxLabels=10,
            MinConfidence=85.0
        )
        return response
    except ClientError as e:
        error_code = e.response['Error']['Code']
        raise RekognitionException.handle_rekognition_exception(error_code)


def detect_faces(imageName, bucketName=settings.BUCKET_NAME):
  """
  Detect faces in an image using Amazon Rekognition.
  
  @param imageName (str): The name of the image to be analyzed.
  @param bucketName (str, optional): The name of the Amazon S3 bucket where the image is stored.
                                      Defaults to the value in settings.BUCKET_NAME.
  
  @return dict: A dictionary containing information about the detected faces.
  """

  if bucketName is None:
     bucketName = settings.BUCKET_NAME
  
     
  try:
    response = rekognition_client.detect_faces(
      Image={
        'S3Object': {
          'Bucket': bucketName, 
          'Name': imageName
          }
      },
      Attributes=['ALL'])
    return response
  except ClientError as e:
    error_code = e.response['Error']['Code']
    raise RekognitionException.handle_rekognition_exception(error_code)

