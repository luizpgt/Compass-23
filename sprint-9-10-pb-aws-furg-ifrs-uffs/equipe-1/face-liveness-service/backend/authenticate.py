from services.rekognition_service import get_liveness_session_results, compare_faces
from services.dynamodb_service import *
from utils import create_response
from exceptions.base_exception import BaseException
from config import settings
import traceback
import json
from exceptions.auth_exception import AuthException
import requests

def handler(event, context):
    try:
        body = json.loads(event['body'])
        session_id = body['session']
        student_id = body['student_id']
        chat_id = body.get('chat_id')
        print(chat_id)
        liveness_results = get_liveness_session_results(session_id)
        if float(liveness_results.get('Confidence')) < 50.0:
            raise AuthException(400, "Não podemos confirmar liveness da sua face. Tente novamente.")
        liveness_image = liveness_results['ReferenceImage'].get('Bytes')
        token = authenticate(student_id, liveness_image)
        update_session_state(chat_id, token, student_id)
        return create_response(200, {"status": "SUCCEEDED"})
    except BaseException as be:
        return create_response(be.status_code, {"status": str(be)})
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        response = create_response(500,{"status": "Erro no serviço de Autenticação"})
        return response

def authenticate(student_id, liveness_image):

    student = get_student_from_id(student_id)
    if not student:
        raise AuthException(400, "Matrícula não encontrada. Por favor tente novamente!")
    print(student)
    similarity = compare_faces(student, liveness_image)
    print(similarity)
    if float(similarity) < 80:
        raise AuthException(400, "Não podemos confirmar seu rosto é similar ao cadastrado. Tente novamente")
    unique_id = update_student(student)
    return unique_id


def update_session_state(chat_id, token, student_id):
    url = settings.BOT_BACKEND_API_URL +'lex'

    data = {
            "chat_id": chat_id,
            "student_id": student_id,
            "token":token
    }

    print(data)

    response = requests.post(url, json=data)
    print(response)
    