from fastapi import FastAPI
from core.config import settings
from api.v1.api import api_router

app = FastAPI(title = 'API da equipe 1')

@app.get('/')
def home():
    return "Projeto da Equipe 1!!!"


app.include_router(api_router, prefix = settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)