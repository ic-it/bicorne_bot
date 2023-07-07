from bicorne_bot.config import Service
from functools import cached_property


class Config(Service):
    @cached_property
    def service(self):
        return Service()
