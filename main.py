import os

from fastapi import FastAPI
from dotenv import load_dotenv

from api import weather

app = FastAPI()

app.include_router(weather.router)

