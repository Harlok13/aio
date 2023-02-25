from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile

from julia.dispatcher import *
from julia.keyboards.reply_keyboard import *
from julia.keyboards.inline_keyboard import *

BOOKS = {'Бьюли': 91, 'Фаулер': 93}

async def start_cmd(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Выберите действие',
                           reply_markup=MENU_BOARD)


async def info_cmd(message: types.Message):
    # mes = {"message_id": 1099, "from": {"id": 5485747686, "is_bot": false, "first_name": "Harlok", "username": "Harlok13", "language_code": "ru"}, "chat": {"id": 5485747686, "first_name": "Harlok", "username": "Harlok13", "type": "private"}, "date": 1677322127, "text": "sdf"}
    mes = [i for i in BOOKS.keys()]
    await bot.send_message(message.chat.id,
                           text='\n'.join(mes),
                           reply_markup=BOOK_MENU)

# async def get_contact_cmd(message: types.Message):
#     await bot.send_message(message.chat.id,
#                            'Вот мои контакты',
#                            reply_markup=ReplyKeyboardRemove())
#
#
# async def get_location_cmd(message: types.Message):
#     await bot.send_message(message.chat.id,
#                            'моя геопозиция',
#                            reply_markup=ReplyKeyboardRemove())


async def get_book_cmd(message: types.Message):
    file = InputFile('handlers/road_to.pdf')
    await bot.send_document(message.from_user.id,
                            document=file)
    await message.delete()


def register_cmd_handler(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start', 'help'])
    dp.register_message_handler(get_book_cmd, commands=['book'])
    dp.register_message_handler(info_cmd, commands=['info'])
    # dp.register_message_handler(get_contact_cmd, commands=['contacts'])
    # dp.register_message_handler(get_location_cmd, commands=['location'])
