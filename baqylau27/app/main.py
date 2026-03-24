from fastapi import FastAPI
from baqylau27.app.api.api_router import router

app = FastAPI()

app.include_router(router)