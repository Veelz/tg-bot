from jinja2 import Environment, FileSystemLoader
import config


class TelegramMessageRenderer:
    _env: Environment

    def __init__(self) -> None:
        self._env = Environment(loader=FileSystemLoader(config.TEMPLATES_DIR))
        

    def render(self, template_name: str, data: dict | None = None) -> str:
        template = self._env.get_template(template_name)
        rendered = template.render(**data)
        return rendered
