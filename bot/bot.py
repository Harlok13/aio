import logging
from aiogram import types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile

from contextlib import contextmanager
import random
from keyboard import *

HELP_COMMAND = """
Все возможности бота описаны в decription
<b>/start</b> - <em>начать работу с ботом/октрыть клавиатуру</em>
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>описание бота</em>
<b>/count</b> - <em>количество отправленных сообщений</em>
<b>/give</b> - <em>отправить стикер</em>
<b>/picture</b> - <em>отправить картинку</em>
<b>/location</b> - <em>отправить местоположение</em>
<b>/кайф</b> - <em>тупо кайф</em>
<b>/botfather</b> - <em>кто тут папочка</em>
<b>/phrase</b> - <em>а ты попробуй</em>
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

PHRASE1 = ('королева', 'стерва', 'фуфыря', 'малюся', 'накрасюся', 'микросюся',
           'милафка', 'инфузория', 'кровосися', 'микродырочка', 'сюсипуси', 'обжора', 'выдра')
PHRASE2 = ('заморская', 'приплюснутая', 'обычная', 'обыкновенная', 'чудоковатая',
           'нафуфыренная', 'унитазолюбивая', 'раздупленная', 'недоделанная', 'недоделанная',
           'расколбассная', 'придурковатая', 'миленькая', 'бензоколоночная')

PHOTO = ('kayf1.jpeg', 'kayf2.jpeg',
         'kayf3.jpeg', 'kayf4.jpeg',
         'morning.jpeg', 'morningcat.jpeg',
         'ozornica.png', 'botfather.png')

DESCRIPTION_PHOTO = ('about kayf1', 'about kayf2',
                     'about kayf3', 'about kayf4',
                     'about morning', 'about morningcat',
                     'about ozornica', 'about botfather')

PHOTO_DATA = dict(zip(PHOTO, DESCRIPTION_PHOTO))

# логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



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


async def send_random(message: types.Message):
    flag = random.choice(tuple(PHOTO_DATA.keys()))
    photo = InputFile(flag)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         caption=PHOTO_DATA.get(flag, False),
                         reply_markup=ikb_photo)
    # await message.delete()


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


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    """Обрабатывает колбеки при нажатии на инлайн клавиатуре send_random_photo"""
    if callback.data == 'like':
        await callback.answer('Вам понравилось!')
    elif callback.data == 'dislike':
        await callback.answer('Вам не понравилось!')
    else:
        await send_random(message=callback.message)
        await callback.answer()


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
