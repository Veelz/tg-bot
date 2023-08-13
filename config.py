import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
OPEN_WEATHER_TOKEN = os.getenv("OPEN_WEATHER_TOKEN", "")

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "view"

BASE_OPEN_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
