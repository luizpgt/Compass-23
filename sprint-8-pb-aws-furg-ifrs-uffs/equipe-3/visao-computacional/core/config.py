import os

class Settings:
    BUCKET_NAME = os.environ.get('BUCKET_NAME')
    
settings = Settings()