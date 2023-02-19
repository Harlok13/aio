import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

HELP_COMMAND = """
Все возможности бота описаны в decription
/start - начать работу с ботом
/help - список команд
/description - описание бота
/count - количество отправленных сообщений
"""

BOT_DESCRIPTION = """
Этот милый бот плод моего творения,
наслаждайтесь его работой:)

p.s.
полное описание возможностей в доработке
"""
#счетчик сообщений
_count_calls = 0

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
@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    await message.reply(f'Всего отправлено сообщений: {_count_calls}')


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(text=BOT_DESCRIPTION)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Добро пожаловать!')
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    # import random, string
    if '0' in message.text:
        bot_message = 'YES'
    else:
        bot_message = 'NO'
    global _count_calls
    _count_calls += 1
    # bot_message = random.choice(string.ascii_lowercase)

    await message.answer(text=bot_message)


if __name__ == '__main__':
    # asyncio.run(main())
    executor.start_polling(dp)
