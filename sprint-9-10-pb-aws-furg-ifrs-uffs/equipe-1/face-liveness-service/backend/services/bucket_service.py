import boto3
from config import settings
from utils import get_formatted_datetime

def save_to_bucket(image, student_id,bucket=settings.BUCKET_NAME):
    s3 = boto3.client('s3')
    object_key = f'{student_id}-{get_formatted_datetime()}.jpeg'
    s3.put_object(Bucket = bucket, Key = f'users/{object_key}',Body=image)
    return object_key

def delete_from_bucket(key, bucket = settings.BUCKET_NAME):
    s3 = boto3.client('s3')
    s3.delete_object(Bucket = bucket, Key = key)

def list_objects(prefix = 'users/'):
    s3 = boto3.client('s3')
    return s3.list_objects(Bucket=settings.BUCKET_NAME, Prefix =prefix)['Contents']