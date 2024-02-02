import os
from dotenv import load_dotenv

load_dotenv()

LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')