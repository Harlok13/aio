import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API
from contextlib import contextmanager

HELP_COMMAND = """
Все возможности бота описаны в decription
<b>/start</b> - <em>начать работу с ботом</em>
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>описание бота</em>
<b>/count</b> - <em>количество отправленных сообщений</em>
<b>/give</b> - <em>отправить стикер</em>
<b>/picture</b> - <em>отправить картинку</em>
<b>/location</b> - <em>отправить местоположение</em>
"""

BOT_DESCRIPTION = """
Этот милый бот плод моего творения,
наслаждайтесь его работой:)

Возможности:
- при отправке стикера вернет его айди
- дублирует сообщение. если в сообщении красное сердечко, то меняет его на черное
- команда /start откроет клавиатуру
p.s.
полное описание возможностей в доработке
"""

# счетчик сообщений и файл, записывающий состояние счетчика
_count_calls = 0
_COUNTER_FILE = 'counter'

tup_of_kayf = ['kayf1.jpeg', 'kayf2.jpeg', 'kayf3.jpeg', 'kayf4.jpeg']

# логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# объект бота
bot = Bot(token=TOKEN_API)
# Диспетчер
dp = Dispatcher(bot)
# Клавиатура
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)  # убирает клавиатуру, после выбранного действия
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/count')
b4 = KeyboardButton('/give')
b5 = KeyboardButton('/picture')
b6 = KeyboardButton('/location')
b7 = KeyboardButton('/❤️')
b8 = KeyboardButton('/кайф')
kb.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6).add(b7).insert(b8)


class FileCounter:
    """
    Позволяет записывать состояние счетчика,
    сохраняя его даже при завершении работы.
    """

    def __init__(self, file_name, method='wr'):
        self.opened_obj = open(file_name, method)

    def __enter__(self):
        return self.opened_obj

    def __exit__(self, type, value, traceback):
        # self.opened_obj.write()
        self.opened_obj.close()


@contextmanager
def open_counter_file(file_name, method='r+'):
    """Позволяет записывать состояние счетчика,
    сохраняя его даже при завершении работы."""
    opened_file = open(file_name, method)
    try:
        yield opened_file
    finally:
        opened_file.write(f'\n{_count_calls}')
        opened_file.close()


async def on_startup(_):
    with open_counter_file(_COUNTER_FILE) as file:
        res = file.readlines()
        print(res)
        global _count_calls
        _count_calls = int(res[-1])

    print(f'А вот и счетчик: {_count_calls}')


@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    await message.answer(f'Всего отправлено сообщений: {_count_calls}')
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text=BOT_DESCRIPTION)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em><b>Добро</b> пожаловать!</em>',
                         parse_mode='HTML',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['❤️'])
async def heart_command(message: types.Message):
    """Бот отправляет стикер."""
    await message.answer('смотри какой смешной котик\nшутка')
    await bot.send_sticker(message.chat.id,
                           sticker="CAACAgIAAxkBAAEH0p9j8z9SA9n8DxwWkHiDxCZcn87M4QACZwEAApafjA6u9uvd6FBSAS4E")
    await message.delete()


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    """Бот отправляет стикер."""
    await message.answer('смотри какой смешной котик\nшутка')
    await bot.send_sticker(message.chat.id,
                           sticker="CAACAgIAAxkBAAEH0p9j8z9SA9n8DxwWkHiDxCZcn87M4QACZwEAApafjA6u9uvd6FBSAS4E")
    await message.delete()


@dp.message_handler(commands=['кайф'])
async def kayf_command(message: types.Message):
    import random
    messages = ('кайф', 'кайф кайф', 'кайф?', 'КАААЙЙЙФФФ')
    picture = random.choice(tup_of_kayf)
    photo = InputFile(picture)
    indx = [char for char in picture if char.isdigit()]
    await message.reply(text=messages[int(indx[0])-1])
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)
    await message.delete()


@dp.message_handler(commands=['picture'])
async def picture_command(message: types.Message):
    photo = InputFile('dog.jpeg')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)
    await message.delete()


@dp.message_handler(commands=['botfather'])
async def picture_command(message: types.Message):
    photo = InputFile('botfather.png')
    await message.answer('Кто тут папочка')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)
    await message.delete()


@dp.message_handler(commands=['location'])
async def location_command(message: types.Message):
    """Отправляет местоположение."""
    import random
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.random() * 100,
                            longitude=random.random() * 100)
    await message.delete()


@dp.message_handler(content_types=['sticker'])
async def get_sticker_id(message: types.Message):
    """Возвращает айди стикера."""
    await bot.send_message(chat_id=message.from_user.id,
                           text=message.sticker.file_id)


@dp.message_handler()
async def echo(message: types.Message):
    bot_message = message.text
    if '❤️' in message.text:
        bot_message = message.text.replace('❤️', '🖤')
    if 'location' in message.text:
        res_coord = [float(coord) for coord in message.text.split() if coord.isdigit()]
        return await bot.send_location(chat_id=message.chat.id,
                                       latitude=res_coord[0],
                                       longitude=res_coord[1])
    global _count_calls
    _count_calls += 1
    await message.answer(text=bot_message)


@dp.message_handler()
async def echo(message: types.Message):
    """Отправляет сообщение в чат указанный в chat_id"""
    global _count_calls
    _count_calls += 1
    # chat_id=message.from_user.id будет отправлять только в личку пользователю
    await bot.send_message(chat_id=message.chat.id, text=message.text)


if __name__ == '__main__':
    # asyncio.run(main())
    # skip_updates будет скипать обновления, если бот не в сети
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
