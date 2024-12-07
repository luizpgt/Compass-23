import boto3
import sagemaker
import numpy as np
from sagemaker.serializers import CSVSerializer

from core.config import settings
from schemas.Booking import Booking
from schemas.Prediction import Prediction
from . import booking_formatter

class PredictionService:
    @staticmethod
    def predict(data: Booking):
        boto_session = boto3.Session(
            aws_access_key_id     = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
            region_name           = settings.AWS_REGION_NAME
        )
        session  = sagemaker.Session(boto_session=boto_session)
        endpoint = settings.ML_MODEL_ENDPOINT
        predictor = sagemaker.predictor.Predictor(
            endpoint_name     = endpoint, 
            sagemaker_session = session
        )
        predictor.serializer = CSVSerializer()

        dummied_booking_values = booking_formatter.dummy_transform(data)
        
        X_entries = np.array(dummied_booking_values)

        prediction = predictor.predict(X_entries).decode('utf-8')

        return Prediction(result = prediction)