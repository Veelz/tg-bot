import logging
from jinja2 import Environment, FileSystemLoader
from aiogram import types
from model.open_weather_api import OpenWeatherApi
import config


logger = logging.getLogger(__name__)


class WeatherTelegramBotView:

    _open_weather_api: OpenWeatherApi
    _env: Environment

    def __init__(self, open_weather_api: OpenWeatherApi) -> None:
        self._open_weather_api = open_weather_api
        self._env = Environment(loader=FileSystemLoader(config.TEMPLATES_DIR), enable_async=True)

    async def start_command(self, message: types.Message):
        await message.reply("Привет! Напиши название города и я пришлю сводку погоды")

    async def get_weather(self, message: types.Message):
        try:
            weather_model = await self._open_weather_api.get_weather(message.text)
            reply = await self.render('weather_data_message.j2', data={"weather_data": weather_model})
            await message.reply(reply)
        except Exception:
            import traceback
            err_message = traceback.format_exc()
            logger.warning(err_message)
            await message.reply(f"Ошибка {err_message}")

    async def render(self, template_name: str, data: dict | None = None) -> str:
        template = self._env.get_template(template_name)
        return await template.render_async(**data)
