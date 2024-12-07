import os
from dotenv import load_dotenv
load_dotenv()

class Settings():
    API_V1_STR              = '/api/v1'
    AWS_ACCESS_KEY_ID       = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY   = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_REGION_NAME         = os.environ.get("AWS_REGION_NAME")
    ML_MODEL_ENDPOINT       = os.environ.get("ML_MODEL_ENDPOINT")

settings = Settings()