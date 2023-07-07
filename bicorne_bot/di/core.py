from functools import cached_property
from bicorne_bot.application import ApplicationService
from .config import Config


class Core:
    @cached_property
    def config(self):
        return Config()

    @cached_property
    def application(self):
        return ApplicationService()
