from dataclasses import dataclass


@dataclass
class WeatherModel:
    city: str
    current_temp: float
    weather_description: str
    humidity: int
    pressure: int
    wind: float
    sunrise_datetime: str
    sunset_datetime: str
    local_datetime: str
