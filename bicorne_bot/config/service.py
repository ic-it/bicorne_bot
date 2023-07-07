from pydantic import BaseSettings


class Service(BaseSettings):
    name: str = "bicorne_bot"
    version: str = "0.0.1"

