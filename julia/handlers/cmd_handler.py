import random

from aiogram import types
from aiogram.filters import Command
import aiohttp

from julia.dispatcher import *
from julia.keyboards.reply_keyboard import *
from julia.keyboards.inline_keyboard import *

RANDOM_GIF = f'https://api.giphy.com/v1/gifs/random?api_key={os.getenv("GIPHY_API")}&tag=&rating=g'


async def start_cmd(message: types.Message):
    await message.answer(text='Выберите действие',
                         reply_markup=MENU_BOARD)


async def get_cat_cmd(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aws.random.cat/meow') as resp:
            res = await resp.json()
    await message.answer_photo(photo=res['file'],
                               reply_markup=GET_CAT)
    await message.delete()


async def get_gif_cmd(message: types.Message):
    # logger = logging.getLogger(__name__)
    async with aiohttp.ClientSession() as session:
        param = {'api_key': os.getenv('GIPHY_API'),
                 'q': 'cat',
                 'limit': 25,
                 'offset': random.randrange(1000),
                 'rating': 'g',
                 'language': 'en'}
        async with session.get(
                f'https://api.giphy.com/v1/gifs/search?api_key={os.getenv("GIPHY_API")}&q=cat&limit=25&offset={random.randrange(1000)}&rating=g&lang=en') as resp:
            res = await resp.json()
    await message.answer_animation(animation=res['data'][0]['images']['original']['mp4'])
    # await bot.send_animation(message.chat.id,
    #                          animation=res['data'][0]['images']['original']['mp4'])
    await message.delete()


# ['data']['images']['original_mp4']['mp4']


async def info_cmd(message: types.Message):
    await message.answer(text='Выберите книгу:',
                         reply_markup=BOOK_CHOICE_MENU)




def register_cmd_handler(dp: Dispatcher):
    dp.message.register(start_cmd, Command(commands=['start', 'help']))
    dp.message.register(info_cmd, Command(commands=['info']))
    dp.message.register(get_cat_cmd, Command(commands=['cat']))
    dp.message.register(get_gif_cmd, Command(commands=['gif']))
