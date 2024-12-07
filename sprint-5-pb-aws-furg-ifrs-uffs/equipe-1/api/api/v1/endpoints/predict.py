from fastapi import APIRouter, status, HTTPException
from schemas.Booking import Booking
from schemas.Prediction import Prediction
from services.prediction_service import PredictionService

router = APIRouter()

@router.post('/', response_model = Prediction, status_code = status.HTTP_200_OK)
def post_predict(booking: Booking):
    try:
        return PredictionService.predict(booking)
    except Exception as e:
        raise HTTPException(detail = "Internal Server Error", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
    

