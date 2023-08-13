from dataclasses import dataclass
import datetime
import math


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


code_to_smile = {
     "Clear": "\U00002600",
     "Clouds": "\U00002601",
     "Rain": "\U00002614",
     "Drizzle": "\U00002614",
     "Thunderstorm": "\U000026A1",
     "Snow": "\U0001F328",
     "Mist": "\U0001F32B"
}


def parse_weather_dict(weather_dict: dict) -> WeatherModel:
    city = weather_dict["name"]
    cur_temp = weather_dict["main"]["temp"]
    humidity = weather_dict["main"]["humidity"]
    pressure = weather_dict["main"]["pressure"]
    wind = weather_dict["wind"]["speed"]

    timezone = weather_dict["timezone"]
    tz = datetime.timezone(datetime.timedelta(seconds=timezone))

    sunrise_timestamp = datetime.datetime.fromtimestamp(weather_dict["sys"]["sunrise"], tz).strftime('%Y-%m-%d %H:%M')
    sunset_timestamp = datetime.datetime.fromtimestamp(weather_dict["sys"]["sunset"], tz).strftime('%Y-%m-%d %H:%M')
    local_datetime = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M')

    wd = weather_dict["weather"][0]["description"]
    if (weather_description := weather_dict["weather"][0]["main"]) in code_to_smile:
        wd += " " + code_to_smile[weather_description]

    return WeatherModel(city=city, current_temp=cur_temp, weather_description=wd, 
                        humidity=humidity, pressure=math.ceil(pressure/1.333), wind=wind, 
                        sunrise_datetime=sunrise_timestamp, sunset_datetime=sunset_timestamp, local_datetime=local_datetime)
