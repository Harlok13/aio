import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API


# логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# объект бота
bot = Bot(token=TOKEN_API )
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
    await message.answer(text=message.text.upper())


if __name__ == '__main__':
    # asyncio.run(main())
    executor.start_polling(dp)
