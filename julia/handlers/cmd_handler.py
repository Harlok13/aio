import random
import os

from aiogram import types, Router
from aiogram.filters import Command
import aiohttp

from julia.keyboards.reply_keyboard import *
from julia.keyboards.inline_keyboard import *

RANDOM_GIF = f'https://api.giphy.com/v1/gifs/random?api_key={os.getenv("GIPHY_API")}&tag=&rating=g'

r = Router()


async def start_cmd(message: types.Message):
    await message.answer(text='Выберите действие',
                         reply_markup=MENU_BOARD)
    await message.delete()


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
    await message.delete()


async def info_cmd(message: types.Message):
    await message.answer(text='Выберите категорию:',
                         reply_markup=CAT_CHOICE_MENU)



def register_cmd_handler(r: Router):
    r.message.register(start_cmd, Command(commands=['start', 'help']))
    # r.message.register(info_cmd, Command(commands=['info']))
    r.message.register(get_cat_cmd, Command(commands=['cat']))
    r.message.register(get_gif_cmd, Command(commands=['gif']))
