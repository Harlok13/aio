from aiogram.types import InputFile

from bot.dispatcher import bot, dp
from aiogram.dispatcher.filters import Text
from aiogram import types
from bot.keyboard import *


@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    """Открывает меню управления."""
    await message.answer('Нажмите Рандом фото',
                         reply_markup=kb_photo)
    await message.delete()


@dp.message_handler(Text(equals='Рандом фото'))
async def send_random_photo(message: types.Message):
    """Отправляет рандомное фото с описанием"""
    await send_random(message)


@dp.message_handler(Text(equals='Главное меню'))
async def open_main_menu(message: types.Message):
    await message.answer('Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['sleep'])
async def sleep_command(message: types.Message):
    photo = InputFile('sleep.jpeg')
    photo1 = InputFile('ozornica.png')
    await message.answer('хватит баловаться')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo1)
    await message.delete()


@dp.message_handler(commands=['morning'])
async def sleep_command(message: types.Message):
    photo = InputFile('morningcat.jpeg')
    photo1 = InputFile('morning.jpeg')
    await message.answer('я усталь')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)
    await message.delete()


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
    await bot.send_message(text='<em><b>Добро</b> пожаловать!</em>',
                           parse_mode='HTML',
                           reply_markup=kb,
                           chat_id=message.chat.id)
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
    messages = ('кайф', 'кайф кайф', 'кайф?', 'КАААЙЙЙФФФ')
    picture = random.choice(tup_of_kayf)
    photo = InputFile(picture)
    indx = [char for char in picture if char.isdigit()]
    await message.reply(text=messages[int(indx[0]) - 1])
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         reply_markup=ikb)
    await message.delete()


@dp.message_handler(commands=['picture'])
async def picture_command(message: types.Message):
    photo = InputFile('dog.jpeg')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)
    await message.delete()


@dp.message_handler(commands=['botfather'])
async def botfather_command(message: types.Message):
    photo = InputFile('botfather.png')
    await message.answer('Кто тут папочка')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)
    await message.delete()


@dp.message_handler(commands=['location'])
async def location_command(message: types.Message):
    """Отправляет местоположение."""
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.random() * 100,
                            longitude=random.random() * 100)
    await message.delete()


@dp.message_handler(content_types=['sticker'])
async def get_sticker_id(message: types.Message):
    """Возвращает айди стикера."""
    await bot.send_message(chat_id=message.from_user.id,
                           text=message.sticker.file_id)


@dp.message_handler(commands=['phrase'])
async def random_phrases_commands(message: types.Message):
    result = f'{random.choice(PHRASE1)} {random.choice(PHRASE2)}'
    await message.answer(text=result)
    await message.delete()


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_reply(message: types.Message):
    await message.reply('Красивенько 😍')


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
