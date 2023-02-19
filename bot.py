import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

HELP_COMMAND = """
/start - начать работу с ботом
/help - список команд
/description - описание бота
"""

BOT_DESCRIPTION = """
Этот милый бот плод моего творения,
наслаждайтесь его работой:)
"""
# логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# объект бота
bot = Bot(token=TOKEN_API)
# Диспетчер
dp = Dispatcher(bot)


# # хэндлер на команду /start
# @dp.message(commands=['start'])
# async def cmd_start(message: types.Message):
#     await message.answer('Hello!')
#
# # запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)
@dp.message_handler()
async def echo(message: types.Message):
    import random, string
    bot_message = random.choice(string.ascii_lowercase)

    await message.answer(text=bot_message)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Добро пожаловать!')
    await message.delete()


if __name__ == '__main__':
    # asyncio.run(main())
    executor.start_polling(dp)
