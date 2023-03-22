from sqlalchemy import text, update
from sqlalchemy.orm import sessionmaker

from bot_ai.data.schemas.user_model import User


class UserRequest:
    def __init__(self, session: sessionmaker):
        self.session: sessionmaker = session

    async def set_default_sub(self, status: str, user_id: int) -> None:
        """
        Set default subscription status in database
        :param status: subscription type to be set
        :param user_id: just a user id
        :return:
        """
        print('set_default_sub', status, user_id)
        async with self.session.begin():
            stmt = update(User).where(User.user_id == user_id).values(status=status)
        await self.session.execute(stmt)  # type: ignore
        await self.session.commit()  # type: ignore

