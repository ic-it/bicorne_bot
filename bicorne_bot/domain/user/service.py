from .repo import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.__user_repo = user_repo

    async def register(self, user_id: int, name: str):
        ...
