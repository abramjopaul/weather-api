import requests
import json

from datetime import datetime, timedelta

def get_round_off_hour(timezone):
    current_time = datetime.now(timezone)
    current_time = (current_time.replace(second = 0, microsecond = 0, minute = 0, hour = current_time.hour, tzinfo = None)
                 + timedelta (hours = current_time.minute // 30))
    return current_time.isoformat(timespec = 'minutes')

def get_hourly_weather(latitude: int, longitude: int):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": latitude,
	"longitude": longitude,
	"hourly": ["temperature_2m", "apparent_temperature"],
	"timezone": "GMT",
	"forecast_days": 1
    }
    response = requests.get(url, params)
    return response.json()

