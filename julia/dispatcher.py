import logging
import os

from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv, find_dotenv
from aioredis import Redis

from aiogram import Bot, Dispatcher

from aiogram.client.session.aiohttp import AiohttpSession

from handlers import message_handler, cmd_handler, cmd_callback

load_dotenv(find_dotenv())

logging.basicConfig(level='INFO')

redis = Redis()
storage = RedisStorage(redis=redis)

session = AiohttpSession()

bot = Bot(token=os.getenv('TOKEN_API'), session=session)
dp = Dispatcher(storage=storage)

cmd_callback.register_callback_cmd(dp)
cmd_handler.register_cmd_handler(dp)
message_handler.register_message_handler(dp)


async def main():
    await dp.start_polling(bot, skip_updates=True)
