import os
import json
from datetime import datetime

from utils import utils


def upload(client, ufile, ufolder, ufilename, uext):
    # params    :
    # client    : initialized client - s3 aws service
    # ufile     : in-fact file to be uploaded
    # ufolder   : folder to be persisted on s3
    # ufilename : arbitrary filename 
    # uext      : file extension
    try:
        filepath = f"{ufolder}{ufilename}.{uext}"
        bucket_name = os.environ.get("S3_BUCKET_NAME")
        client.put_object(
            ACL     = 'public-read',
            Bucket  = bucket_name,
            Key     = filepath,
            Body    = ufile
        )
        res = f"https://{bucket_name}.s3.amazonaws.com/{filepath}"    
        return res
    except:
        raise Exception('upload audio file into s3')

def delete(client, ufolder, ufilename, uext):
    # params    :
    # client    : initialized client - s3 aws service
    # ufolder   : folder to be persisted on s3
    # ufilename : arbitrary filename 
    # uext      : file extension
    try:
        filepath = f"{ufolder}{ufilename}.{uext}"
        bucket_name = os.environ.get("S3_BUCKET_NAME")
        client.delete_object(
            Bucket=bucket_name,
            Key=filepath,
        )
    except:
        raise Exception('delete item from s3')