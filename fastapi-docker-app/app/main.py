from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Docker App"}

app.include_router(api_router)