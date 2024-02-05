from fastapi import FastAPI

from api.weather import router

app = FastAPI()

app.include_router(router)

