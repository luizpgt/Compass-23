import os
from boto3 import Session

''' enable on local env:
from dotenv import load_dotenv
load_dotenv()
'''

def get_session(aws_access_key_id, aws_secret_access_key, region_name):
    try:
        session = Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        return session
    except:
        raise Exception

def client_init(service):
    # 'service' must be a valid service from aws
    try:
        aws_access_key_id     = os.environ.get(f"{service.upper()}_AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.environ.get(f"{service.upper()}_AWS_SECRET_ACCESS_KEY")
        region_name           = os.environ.get(f"{service.upper()}_AWS_REGION")
        client = get_session(aws_access_key_id,aws_secret_access_key,region_name).client(service)
        return client
    except:
        raise Exception(f'connect {service} client')