from fastapi import FastAPI

from api import weather

app = FastAPI()

app.include_router(weather.router)

