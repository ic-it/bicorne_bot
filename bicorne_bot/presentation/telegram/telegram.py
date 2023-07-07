from aiogram import Router
from aiogram.filters import JOIN_TRANSITION
from aiogram.types import Message

groups_router = Router(name="groups")


@groups_router.message(JOIN_TRANSITION)
async def join_group(message: Message) -> None:
    ...

