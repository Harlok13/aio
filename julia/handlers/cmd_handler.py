from aiogram import types
from aiogram.types import InputFile

from julia.dispatcher import *
from julia.keyboards.reply_keyboard import *
from julia.keyboards.inline_keyboard import *


async def start_cmd(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Выберите действие',
                           reply_markup=MENU_BOARD)


async def get_cat_cmd(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aws.random.cat/meow') as resp:
            res = await resp.json()
    await message.answer_photo(photo=res['file'],
                               reply_markup=GET_CAT)
    # await bot.send_photo(message.chat.id,
    #                      photo=res['file'],
    #                      reply_markup=GET_CAT)
    await message.delete()


async def info_cmd(message: types.Message):
    mes = 'Выберите книгу:'
    await bot.send_message(message.chat.id,
                           text=mes,
                           reply_markup=BOOK_CHOICE_MENU)


async def get_book_cmd(message: types.Message):
    file = InputFile('handlers/road_to.pdf')
    await bot.send_document(message.from_user.id,
                            document=file)
    await message.delete()


def register_cmd_handler(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start', 'help'])
    dp.register_message_handler(get_book_cmd, commands=['book'])
    dp.register_message_handler(info_cmd, commands=['info'])
