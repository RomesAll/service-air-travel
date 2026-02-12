from src.config import app
from src.presentation.api.rest.v1 import router as api_router
from fastapi import FastAPI
import uvicorn

app = FastAPI()
app.include_router(api_router)

@app.get('/')
def hello_world():
    return {'message': 'Hello World'}

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
