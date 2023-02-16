import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# объект бота
bot = Bot(token='5889825944')
# Диспетчер
dp = Dispatcher


# хэндлер на команду /start
@dp.message(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Hello!')

# запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
