from julia.dispatcher import *
from aiogram import types


# @dp.message_handler()
async def start_cmd(message: types.Message):
    await message.answer(message.text)


def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(start_cmd)
