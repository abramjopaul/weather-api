import fastapi

import services.weather as weather_service
import utils.weather_utils as weather_utils

router = fastapi.APIRouter()

@router.get("/headquarter-weather")
def get_weather(include_maximum: bool = False):
    response = weather_service.compute_weather(include_maximum)
    print(response)
    return response

