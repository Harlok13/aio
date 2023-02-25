import logging
import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv, find_dotenv

from handlers import message_handler, cmd_handler, cmd_callback

load_dotenv(find_dotenv())

logging.basicConfig(level='INFO')

bot = Bot(token=os.getenv('TOKEN_API'))
dp = Dispatcher(bot)

cmd_callback.register_callback_cmd(dp)
cmd_handler.register_cmd_handler(dp)
message_handler.register_message_handler(dp)


def main():
    executor.start_polling(dp, skip_updates=True)
