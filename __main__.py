import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TELEGRAM_BOT_TOKEN, OPEN_WEATHER_TOKEN, BASE_OPEN_WEATHER_URL
from model.weather_model import parse_weather_dict
from view.message_renderer import TelegramMessageRenderer

OPEN_WEATHER_URL = "{base_url}?q={city}&lang=ru&units=metric&appid={api_token}"


async def start_command(message: types.Message):
    await message.reply("Привет! Напиши название города и я пришлю сводку погоды")

async def get_weather(message: types.Message):
    try:
        url = OPEN_WEATHER_URL.format(base_url=BASE_OPEN_WEATHER_URL, city=message.text, api_token=OPEN_WEATHER_TOKEN)
        response = requests.get(url)
        data = response.json()
        weather_model = parse_weather_dict(data)
        reply = TelegramMessageRenderer().render('weather_data_message.j2', data={"weather_data": weather_model})
        await message.reply(reply)
    except Exception as err:
        print(err)
        await message.reply(f"Ошибка {err}")

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dispatcher = Dispatcher(bot)
    dispatcher.register_message_handler(start_command, commands=["start"])
    dispatcher.register_message_handler(get_weather)
    executor.start_polling(dispatcher)


if __name__ == "__main__":
    main()
