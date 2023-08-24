import logging
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TELEGRAM_BOT_TOKEN, OPEN_WEATHER_TOKEN, BASE_OPEN_WEATHER_URL
from model.open_weather_api import OpenWeatherApi
from view.weather_telegram_bot_view import WeatherTelegramBotView


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

if not TELEGRAM_BOT_TOKEN or not OPEN_WEATHER_TOKEN:
    raise KeyError("TELEGRAM_BOT_TOKEN and OPEN_WEATHER_TOKEN env variables "
                   "wasn't implemented in .env")


def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dispatcher = Dispatcher(bot)
    open_weather_api = OpenWeatherApi(BASE_OPEN_WEATHER_URL, OPEN_WEATHER_TOKEN)
    weather_telegram_bot = WeatherTelegramBotView(open_weather_api)
    dispatcher.register_message_handler(weather_telegram_bot.start_command, commands=["start"])
    dispatcher.register_message_handler(weather_telegram_bot.get_weather)
    executor.start_polling(dispatcher)


if __name__ == "__main__":
    main()
