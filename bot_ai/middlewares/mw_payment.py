import logging
from typing import Dict, Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from bot_ai.utils.user_requsts import UserRequest


class Payment(BaseMiddleware):
    """
    Create session for requests
    """

    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        logger = logging.getLogger(__name__)
        session_maker: sessionmaker = data.get('session_maker')
        async with session_maker() as session:
            data['request']: UserRequest = UserRequest(session)
        return await handler(event, data)  # type: ignore
