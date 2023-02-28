import asyncio
import logging
import os
from dotenv import load_dotenv, find_dotenv
from aioredis import Redis

from aiogram.fsm.storage.redis import RedisStorage
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from handlers import message_handler, cmd_handler, cmd_callback


async def start_bot(logger: logging.Logger = None) -> None:
    logging.basicConfig(level='INFO')
    load_dotenv(find_dotenv())

    redis = Redis()
    storage = RedisStorage(redis=redis)

    session = AiohttpSession()

    bot = Bot(token=os.getenv('TOKEN_API'), session=session)
    dp = Dispatcher(storage=storage)

    cmd_callback.register_callback_cmd(dp)
    cmd_handler.register_cmd_handler(dp)
    message_handler.register_message_handler(dp)

    await dp.start_polling(bot)


# def setup_env() -> None:
#     """Настройка переменных окружения."""
#     from dotenv import load_dotenv
#     path = pathlib.Path(__file__).parent.parent
#     dotenv_path = path.joinpath('.env')
#     if dotenv_path.exists():
#         load_dotenv(dotenv_path)


def main():
    logger = logging.getLogger(__name__)
    try:
        # setup_env()
        asyncio.run(start_bot(logger))
        logger.info('start')
    except (KeyboardInterrupt, SystemExit):
        pass
        logger.info('stop')


if __name__ == '__main__':
    main()
