import datetime
import logging
from typing import Any, Callable, Dict, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select, ScalarResult, update
from sqlalchemy.orm import sessionmaker

from bot_ai.data.schemas.user_model import User
from bot_ai.utils.bot_models import companion_bot_model


class UserRegisterCheck(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        logger = logging.getLogger(__name__)
        session_maker: sessionmaker = data['session_maker']
        data['model'] = companion_bot_model
        async with session_maker() as session:
            async with session.begin():
                result: ScalarResult = await session.execute(  # type: ignore
                    select(User).where(User.user_id == event.from_user.id))  # type: ignore
                user: User = result.one_or_none()

                if user is not None:
                    logger.info(f'Пользователь {event.from_user.username} уже зарегистрирован')
                    await session.execute(
                        update(User).where(User.user_id == event.from_user.id).values(
                            update_date=datetime.datetime.today())
                    )
                else:
                    user: User = User(
                        user_id=event.from_user.id,
                        username=event.from_user.username,
                        nickname=event.from_user.first_name,
                        update_date=datetime.datetime.today()
                    )
                    await session.merge(user)
                    logger.info(f'Пользователь {event.from_user.username} зарегистрирован')

        return await handler(event, data)
