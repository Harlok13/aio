import logging
import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv, find_dotenv

from handlers import message_handler

load_dotenv(find_dotenv())

logging.basicConfig(level='INFO')

bot = Bot(token=os.getenv('TOKEN_API'))
dp = Dispatcher(bot)

message_handler.register_message_handler(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
