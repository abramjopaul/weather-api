import pandas as pd

from pytz import timezone

import utils.weather_utils as weather_utils
import utils.config as config

def compute_weather(include_maximum: bool):
    
    latitude = config.LATITUDE
    longitude = config.LONGITUDE

    weather_data = weather_utils.get_hourly_weather(latitude, longitude)
    current_time = weather_utils.get_round_off_hour(timezone('UTC'))

     
    hourly_data = weather_data["hourly"]
    hourly_data_pd = pd.DataFrame(hourly_data)
    print(hourly_data_pd)
    current_temp = hourly_data_pd.loc[hourly_data_pd['time'] == current_time,'temperature_2m'].values[0]
    if not include_maximum:
        response = {"current_temperature": current_temp,"current_time": current_time}
    else :
        max_temp_row = hourly_data_pd.loc[hourly_data_pd['temperature_2m'].idxmax()]
        max_temp_time = max_temp_row['time']
        max_temp = max_temp_row['temperature_2m']

        max_apparent_temp_row = hourly_data_pd.loc[hourly_data_pd['apparent_temperature'].idxmax()]
        max_apparent_temp_time = max_apparent_temp_row['time']
        max_apparent_temp = max_apparent_temp_row['apparent_temperature']
    
        response  = {"current_temperature": current_temp,"current_time": current_time, 
            "max_temperature": max_temp, "max_temperature_time": max_temp_time,
            "max_apparent_temperature": max_apparent_temp, "max_apparent_temperature_time": max_apparent_temp_time }
    return response
